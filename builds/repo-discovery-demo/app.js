const API='https://api.github.com';
const DB_NAME='ai-money-repo-discovery';
const DB_VERSION=1;
const CACHE_TTL=1000*60*60*12;
const POOL_TARGET=120;
const BATCH_SIZE=20;
const LOW_WATER=5;
const RECENT_DIVERSITY_WINDOW=10;

const MODES={
  'money-ai':['ai automation stars:>20 archived:false','n8n ai stars:>10 archived:false','agent workflow stars:>20 archived:false'],
  automation:['automation workflow stars:>20 archived:false','n8n stars:>20 archived:false','zapier alternative stars:>10 archived:false'],
  agents:['ai agent framework stars:>20 archived:false','multi agent stars:>20 archived:false','agentic workflow stars:>10 archived:false'],
  'local-ai':['local llm stars:>20 archived:false','ollama workflow stars:>10 archived:false','comfyui automation stars:>10 archived:false'],
  scraping:['scraping research automation stars:>20 archived:false','browser automation ai stars:>20 archived:false','web research agent stars:>10 archived:false']
};

const state={pool:[],queue:[],seen:new Set(),recent:[],current:null,allowSeenFallback:false,loading:false,token:'',mode:'money-ai',minStars:20,rate:null,db:null};
const $=s=>document.querySelector(s);
const els={card:$('#repoCard'),github:$('#githubLink'),wikiBtn:$('#wikiBtn'),deepWiki:$('#deepWikiLink'),wikiPanel:$('#wikiPanel'),wikiTitle:$('#wikiTitle'),wikiBody:$('#wikiBody'),diag:$('#diag'),network:$('#networkStatus'),rate:$('#rateStatus'),mode:$('#modeSelect'),minStars:$('#minStars'),token:$('#tokenInput'),apply:$('#applyBtn'),export:$('#exportBtn'),import:$('#importInput'),skipSeen:$('#skipSeenBtn'),closeWiki:$('#closeWikiBtn')};

function openDb(){return new Promise((resolve,reject)=>{const req=indexedDB.open(DB_NAME,DB_VERSION);req.onupgradeneeded=()=>{const db=req.result;if(!db.objectStoreNames.contains('repos'))db.createObjectStore('repos',{keyPath:'id'});if(!db.objectStoreNames.contains('seen'))db.createObjectStore('seen',{keyPath:'id'});if(!db.objectStoreNames.contains('wiki'))db.createObjectStore('wiki',{keyPath:'key'});};req.onsuccess=()=>resolve(req.result);req.onerror=()=>reject(req.error);});}
function tx(store,mode='readonly'){return state.db.transaction(store,mode).objectStore(store)}
function idbGetAll(store){return new Promise((resolve,reject)=>{const r=tx(store).getAll();r.onsuccess=()=>resolve(r.result);r.onerror=()=>reject(r.error)})}
function idbPut(store,value){return new Promise((resolve,reject)=>{const r=tx(store,'readwrite').put(value);r.onsuccess=()=>resolve();r.onerror=()=>reject(r.error)})}

async function api(path,{search=false}={}){
  const headers={'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'};
  if(state.token)headers.Authorization=`Bearer ${state.token}`;
  const res=await fetch(`${API}${path}`,{headers});
  state.rate={remaining:res.headers.get('x-ratelimit-remaining'),limit:res.headers.get('x-ratelimit-limit'),reset:res.headers.get('x-ratelimit-reset'),resource:res.headers.get('x-ratelimit-resource')||(search?'search':'core')};
  renderStatus();
  if(res.status===403||res.status===429)throw new Error(`GitHub rate-limit / erişim hatası (${res.status}). Bir süre sonra yeniden dene veya isteğe bağlı token kullan.`);
  if(!res.ok)throw new Error(`GitHub API ${res.status}: ${await res.text()}`);
  return res.json();
}

function daysSince(iso){if(!iso)return 3650;return Math.max(0,(Date.now()-new Date(iso).getTime())/86400000)}
function clamp(v,a=0,b=1){return Math.max(a,Math.min(b,v))}
function tokenize(repo){return new Set([...(repo.topics||[]),repo.language||'',repo.owner?.login||'',...(repo.name||'').toLowerCase().split(/[-_.]/)].filter(Boolean).map(x=>String(x).toLowerCase()))}
function overlap(a,b){const A=tokenize(a),B=tokenize(b);if(!A.size||!B.size)return 0;let i=0;for(const x of A)if(B.has(x))i++;return i/Math.max(A.size,B.size)}
function relevance(repo){const text=`${repo.name} ${repo.description||''} ${(repo.topics||[]).join(' ')}`.toLowerCase();const terms=['ai','automation','workflow','agent','llm','n8n','scrap','research','lead','sales','content','marketing','rag','local'];return clamp(terms.reduce((s,t)=>s+(text.includes(t)?1:0),0)/5)}
function quality(repo){const stars=Math.log10((repo.stargazers_count||0)+1)/5;const forks=Math.log10((repo.forks_count||0)+1)/4;const freshness=Math.exp(-daysSince(repo.pushed_at)/365);const license=repo.license?.spdx_id&&repo.license.spdx_id!=='NOASSERTION'?1:.35;const desc=repo.description?1:.4;let q=.31*clamp(stars)+.14*clamp(forks)+.22*freshness+.12*license+.09*desc+.12*relevance(repo);if(repo.archived)q*=.1;if(repo.fork)q*=.55;return clamp(q)}
function discoveryWeight(repo){const q=quality(repo);const maxSim=state.recent.reduce((m,r)=>Math.max(m,overlap(repo,r)),0);const diversityPenalty=.38*maxSim;const novelty=state.seen.has(repo.id)?0:.18;return Math.max(.01,q+novelty-diversityPenalty)}
function weightedSampleWithoutReplacement(items,n){return items.map(item=>({item,key:Math.pow(Math.random(),1/discoveryWeight(item))})).sort((a,b)=>b.key-a.key).slice(0,n).map(x=>x.item)}

async function hydrateCache(){const [repos,seen]=await Promise.all([idbGetAll('repos'),idbGetAll('seen')]);const now=Date.now();state.pool=repos.filter(x=>now-x.cachedAt<CACHE_TTL).map(x=>x.repo);state.seen=new Set(seen.map(x=>x.id));}
async function markSeen(repo){if(!repo||state.seen.has(repo.id))return;state.seen.add(repo.id);await idbPut('seen',{id:repo.id,seenAt:Date.now()});}

async function searchPool(force=false){if(state.loading)return;state.loading=true;renderStatus('GitHub aranıyor…');try{if(force){state.pool=[];state.queue=[];}const queries=MODES[state.mode]||MODES['money-ai'];const seenIds=new Set(state.pool.map(r=>r.id));for(const q0 of queries){if(state.pool.length>=POOL_TARGET)break;const q=`${q0} stars:>=${state.minStars}`;const data=await api(`/search/repositories?q=${encodeURIComponent(q)}&sort=updated&order=desc&per_page=50`,{search:true});for(const repo of data.items||[]){if(seenIds.has(repo.id))continue;seenIds.add(repo.id);state.pool.push(repo);await idbPut('repos',{id:repo.id,cachedAt:Date.now(),repo});}}refillQueue();renderStatus('hazır');}catch(err){renderStatus(err.message,true);if(!state.queue.length)refillQueue();}finally{state.loading=false;renderDiag();}}
function eligiblePool(){let items=state.pool.filter(r=>(r.stargazers_count||0)>=state.minStars&&!r.archived);const unseen=items.filter(r=>!state.seen.has(r.id));if(unseen.length)return unseen;if(state.allowSeenFallback)return items.sort((a,b)=>daysSince(a.pushed_at)-daysSince(b.pushed_at));return []}
function refillQueue(){const candidates=eligiblePool().filter(r=>!state.queue.some(q=>q.id===r.id)&&r.id!==state.current?.id);if(candidates.length)state.queue.push(...weightedSampleWithoutReplacement(candidates,Math.min(BATCH_SIZE,candidates.length)));}
async function nextRepo(){if(state.current)await markSeen(state.current);if(state.queue.length<LOW_WATER){refillQueue();if(state.queue.length<LOW_WATER&&!state.loading)searchPool(false);}let next=state.queue.shift();if(!next){refillQueue();next=state.queue.shift();}if(!next){renderEmpty();return;}state.current=next;state.recent.unshift(next);state.recent=state.recent.slice(0,RECENT_DIVERSITY_WINDOW);renderRepo(next);history.replaceState(null,'',`#/r/${next.id}/${slug(next.full_name)}`);if(state.queue.length<LOW_WATER)refillQueue();renderDiag();}

function slug(s=''){return s.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')}
function esc(s=''){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function fmt(n){return Intl.NumberFormat('tr-TR',{notation:n>9999?'compact':'standard',maximumFractionDigits:1}).format(n||0)}
function renderRepo(r){els.card.innerHTML=`<div class="owner">${esc(r.owner?.login||'')}</div><div class="repo-name">${esc(r.name)}</div><div class="description">${esc(r.description||'Açıklama yok.')}</div><div class="meta-grid"><div class="metric">Skor<b class="score">${Math.round(quality(r)*100)}/100</b></div><div class="metric">Yıldız<b>${fmt(r.stargazers_count)}</b></div><div class="metric">Fork<b>${fmt(r.forks_count)}</b></div><div class="metric">Dil<b>${esc(r.language||'—')}</b></div><div class="metric">Son push<b>${Math.round(daysSince(r.pushed_at))} gün</b></div><div class="metric">Lisans<b>${esc(r.license?.spdx_id||'belirsiz')}</b></div></div><div class="tags">${(r.topics||[]).slice(0,12).map(t=>`<span class="tag">${esc(t)}</span>`).join('')}</div>`;els.github.href=r.html_url;els.github.classList.remove('disabled');els.wikiBtn.disabled=false;els.deepWiki.href=`https://deepwiki.com/${r.full_name}`;els.deepWiki.classList.remove('disabled');els.card.focus({preventScroll:true});}
function renderEmpty(){els.card.innerHTML=`<div class="repo-name">Yeni repo kalmadı</div><div class="description">Önce “Havuzu yenile” ile yeni aday çek. Yine boşsa “Görülmüşleri gerektiğinde aç” düğmesi, daha önce görülenleri açıkça fallback olarak kullanır.</div>`}
function renderStatus(text,error=false){if(text)els.network.textContent=text;els.network.style.color=error?'var(--danger)':'';if(state.rate){const reset=state.rate.reset?new Date(Number(state.rate.reset)*1000).toLocaleTimeString('tr-TR',{hour:'2-digit',minute:'2-digit'}):'?';els.rate.textContent=`${state.rate.resource}: ${state.rate.remaining}/${state.rate.limit} · ${reset}`}}
function renderDiag(){els.diag.textContent=JSON.stringify({pool:state.pool.length,queue:state.queue.length,seen:state.seen.size,recent:state.recent.map(r=>r.full_name),mode:state.mode,minStars:state.minStars,rate:state.rate,token:state.token?'session-only: yes':'none'},null,2)}

function extractReadmeHints(md=''){const lines=md.split(/\r?\n/);const heads=lines.filter(l=>/^#{1,3}\s+/.test(l)).slice(0,14).map(l=>l.replace(/^#+\s*/,''));const code=[];const re=/```(?:bash|sh|shell|powershell|cmd)?\n([\s\S]*?)```/gi;let m;while((m=re.exec(md))&&code.length<3)code.push(m[1].trim().split('\n').slice(0,8).join('\n'));return {heads,code}}
function opportunityRules(repo,readme){const text=`${repo.name} ${repo.description||''} ${(repo.topics||[]).join(' ')} ${readme||''}`.toLowerCase();const out=[];const add=(title,why,model)=>out.push({title,why,model});if(/scrap|crawl|browser|research|search/.test(text))add('Araştırma-as-a-service','Veri toplama ve araştırma hattı müşteriye özel rapor, lead listesi veya pazar taraması olarak paketlenebilir.','F / R');if(/agent|workflow|automation|n8n|zapier/.test(text))add('Kurulum + bakım hizmeti','Workflow/agent altyapısı KOBİ’ye kurulum, entegrasyon ve aylık bakım olarak satılabilir.','F');if(/image|video|content|social|marketing/.test(text))add('İçerik üretim paketi','Üretim zinciri belirli bir nişe uyarlanıp abonelik veya kampanya başına hizmete dönüştürülebilir.','F / R');if(/local|ollama|llm|rag|embedding/.test(text))add('Yerel AI kurulumu','Veri mahremiyeti isteyen işletmelere yerel model/RAG kurulumu ve işletim paketi sunulabilir.','F');if(/lead|sales|crm|email|outreach/.test(text))add('Lead-generation workflow','Repo satış araştırması, lead zenginleştirme veya outreach operasyonuna bağlanabilir.','F / V');if(!out.length)add('Niş otomasyon ürünü','Teknik yetenek, belirli bir sektör problemine daraltılıp kurulum hizmeti veya mikro-SaaS olarak doğrulanabilir.','F / R');return out.slice(0,4)}
async function fetchReadme(repo){const cacheKey=`${repo.id}:${repo.default_branch}:readme`;const cached=await new Promise(resolve=>{const r=tx('wiki').get(cacheKey);r.onsuccess=()=>resolve(r.result);r.onerror=()=>resolve(null)});if(cached&&Date.now()-cached.cachedAt<CACHE_TTL)return cached.data;try{const data=await api(`/repos/${repo.full_name}/readme`);const bytes=Uint8Array.from(atob(data.content.replace(/\n/g,'')),c=>c.charCodeAt(0));const md=new TextDecoder().decode(bytes);await idbPut('wiki',{key:cacheKey,cachedAt:Date.now(),data:md});return md;}catch{return ''}}
async function showWiki(){const r=state.current;if(!r)return;els.wikiBtn.disabled=true;els.wikiPanel.hidden=false;els.wikiTitle.textContent=r.full_name;els.wikiBody.innerHTML='<div class="skeleton">README ve metadata analiz ediliyor…</div>';const readme=await fetchReadme(r);const hints=extractReadmeHints(readme);const opp=opportunityRules(r,readme);els.wikiBody.innerHTML=`<section class="wiki-section"><h3>Snapshot</h3><p>${esc(r.description||'Açıklama yok.')}</p><p><b>Kalite skoru:</b> ${Math.round(quality(r)*100)}/100 · <b>Yıldız:</b> ${fmt(r.stargazers_count)} · <b>Lisans:</b> ${esc(r.license?.spdx_id||'belirsiz')} · <b>Son push:</b> ${Math.round(daysSince(r.pushed_at))} gün önce.</p></section><section class="wiki-section"><h3>README’den çıkarılan yapı</h3>${hints.heads.length?`<p>${hints.heads.map(esc).join(' · ')}</p>`:'<p>README başlıkları alınamadı.</p>'}${hints.code.length?`<pre><code>${esc(hints.code[0])}</code></pre>`:''}</section><section class="wiki-section"><h3>AI Money Workflow Opportunities</h3>${opp.map(o=>`<p><b>${esc(o.title)}</b> <span class="tag">${esc(o.model)}</span><br>${esc(o.why)}</p>`).join('')}<p><small>Bu bölüm ücretli LLM kullanmadan, repo metadata + README anahtar sinyallerinden deterministik kurallarla oluşturulur; gelir kanıtı değildir.</small></p></section><section class="wiki-section"><h3>Kaynak ve sınırlar</h3><p>Kaynak: <a href="${r.html_url}" target="_blank" rel="noreferrer">GitHub repo</a>. Genel teknik wiki için <a href="https://deepwiki.com/${r.full_name}" target="_blank" rel="noreferrer">DeepWiki</a>. README burada kopyalanmaz; yalnızca kısa yapı sinyalleri çıkarılır.</p></section>`;els.wikiBtn.disabled=false;}

function exportSeen(){const blob=new Blob([JSON.stringify({version:1,exportedAt:new Date().toISOString(),ids:[...state.seen]},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='repo-discovery-seen.json';a.click();URL.revokeObjectURL(a.href)}
async function importSeen(file){const json=JSON.parse(await file.text());if(!Array.isArray(json.ids))throw new Error('Geçersiz seen dosyası');for(const id of json.ids){const n=Number(id);if(Number.isFinite(n)){state.seen.add(n);await idbPut('seen',{id:n,seenAt:Date.now()})}}refillQueue();renderDiag()}
async function restoreRoute(){const m=location.hash.match(/^#\/r\/(\d+)/);if(!m)return false;const id=Number(m[1]);let repo=state.pool.find(r=>r.id===id);if(!repo){try{repo=await api(`/repositories/${id}`);state.pool.push(repo);await idbPut('repos',{id:repo.id,cachedAt:Date.now(),repo});}catch{return false}}state.current=repo;renderRepo(repo);return true}

els.card.addEventListener('keydown',e=>{if(e.repeat&&(e.key===' '||e.key==='Enter'))e.preventDefault()});
els.card.addEventListener('click',()=>nextRepo());
els.wikiBtn.addEventListener('click',showWiki);els.closeWiki.addEventListener('click',()=>els.wikiPanel.hidden=true);
els.apply.addEventListener('click',async()=>{state.mode=els.mode.value;state.minStars=Math.max(0,Number(els.minStars.value)||0);state.token=els.token.value.trim();sessionStorage.setItem('githubToken',state.token);await searchPool(true);await nextRepo()});
els.token.addEventListener('change',()=>{state.token=els.token.value.trim();sessionStorage.setItem('githubToken',state.token)});
els.export.addEventListener('click',exportSeen);els.import.addEventListener('change',async e=>{try{if(e.target.files[0])await importSeen(e.target.files[0])}catch(err){renderStatus(err.message,true)}});
els.skipSeen.addEventListener('click',()=>{state.allowSeenFallback=!state.allowSeenFallback;els.skipSeen.textContent=state.allowSeenFallback?'Görülmüş fallback açık':'Görülmüşleri gerektiğinde aç';refillQueue();renderDiag()});

async function init(){state.token=sessionStorage.getItem('githubToken')||'';els.token.value=state.token;try{state.db=await openDb();await hydrateCache();renderStatus(navigator.onLine?'önbellek hazır':'çevrimdışı önbellek');refillQueue();const restored=await restoreRoute();if(!restored){if(!state.queue.length)await searchPool(false);await nextRepo()}else if(state.queue.length<LOW_WATER)searchPool(false);renderDiag()}catch(err){renderStatus(err.message,true);els.card.innerHTML=`<div class="repo-name">Başlatılamadı</div><div class="description">${esc(err.message)}</div>`}}
window.addEventListener('online',()=>renderStatus('çevrimiçi'));window.addEventListener('offline',()=>renderStatus('çevrimdışı önbellek'));
init();
