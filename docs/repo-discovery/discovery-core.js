const STOP_WORDS = new Set([
  'the','and','for','with','from','into','that','this','your','our','you','are','was','were','has','have','had','but','not','via','using','use','used',
  'bir','ile','icin','olan','olarak','gibi','ve','veya','bu','su','daha','cok','az','yapan','yapilan','sistem','workflow','automation','automated','automatic',
  'ai','llm','agent','agents','tool','tools','app','service','services','platform','system','project','open','source'
]);

const PHRASE_ALIASES = [
  [/b2b[-\s]?satis[-\s]?lead|b2b.*lead|musteri adayi/i, ['b2b lead generation','sales prospecting']],
  [/musteri[-\s]?iletisim[-\s]?destek|misafir iletisim|destek/i, ['customer support','customer service']],
  [/yerel[-\s]?isletme[-\s]?saha[-\s]?servisi|oto servis|servis operasyon/i, ['local business','field service']],
  [/ofis[-\s]?belge[-\s]?operasyonu|belge|dokuman|e-posta/i, ['document automation','office operations']],
  [/icerik[-\s]?sosyal[-\s]?medya|icerik|sosyal medya/i, ['content automation','social media']],
  [/video[-\s]?gorsel[-\s]?produksiyon|gorsel|video/i, ['creative automation','video generation']],
  [/ik[-\s]?ise[-\s]?alim|ise alim|hiring|recruit/i, ['recruiting automation','hiring workflow']],
  [/e[-\s]?ticaret|ecommerce|e-commerce/i, ['ecommerce automation','commerce operations']],
  [/randevu|appointment|booking/i, ['appointment automation','booking workflow']],
  [/whatsapp/i, ['whatsapp automation']],
  [/sesli|voice|telefon|call/i, ['voice agent','call automation']],
  [/arastirma|research|istihbarat|intelligence/i, ['research automation','intelligence workflow']],
  [/scrap|crawl|tarama/i, ['web scraping','data extraction']],
  [/crm/i, ['crm automation']],
  [/email|gmail|e-mail/i, ['email automation']],
  [/newsletter|bulten/i, ['newsletter automation']],
  [/reklam|ads|creative|kampanya/i, ['marketing automation','ad creative']],
  [/lead generation|prospect|outreach/i, ['lead generation','outreach automation']]
];

const STACK_CANONICAL = new Map([
  ['n8n','n8n'],['zapier','zapier'],['make','make.com'],['make.com','make.com'],['whatsapp','whatsapp'],['wati','whatsapp'],['elevenlabs','voice ai'],
  ['firecrawl','firecrawl'],['apify','apify'],['gemini','gemini'],['openai','openai'],['chatgpt','openai'],['airtable','airtable'],['slack','slack'],
  ['gmail','gmail'],['sheets','google sheets'],['google sheets','google sheets'],['docs','google docs'],['calendar','google calendar'],['salesforce','salesforce'],
  ['crm','crm'],['telegram','telegram'],['discord','discord'],['supabase','supabase'],['ollama','ollama'],['comfyui','comfyui'],['langchain','langchain']
]);

function normalize(value='') {
  return String(value ?? '')
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g,'')
    .replace(/[’']/g,'')
    .replace(/[^a-z0-9+#.\-\s]/g,' ')
    .replace(/[-_/]+/g,' ')
    .replace(/\s+/g,' ')
    .trim();
}

function words(value='') {
  return normalize(value).split(' ').filter(x => x.length > 2 && !STOP_WORDS.has(x) && !/^\d+$/.test(x));
}

function unique(list) { return [...new Set(list.filter(Boolean))]; }

function phraseAliases(value='') {
  const out=[];
  const raw=normalize(value);
  for (const [re, aliases] of PHRASE_ALIASES) if (re.test(raw)) out.push(...aliases);
  return unique(out);
}

function stackPhrases(value='') {
  const raw=normalize(value);
  const out=[];
  for (const [needle, label] of STACK_CANONICAL) {
    const re = new RegExp(`(^|\\s)${needle.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')}(?=\\s|$)`,'i');
    if (re.test(raw)) out.push(label);
  }
  return unique(out);
}

function compactPhrase(value='', maxWords=4) {
  return unique(words(value)).slice(0,maxWords).join(' ');
}

export function caseWeight(c) {
  const evidence={A:1,B:.76,C:.5,X:.05}[c.evidence_grade] ?? .3;
  const sell={high:1,medium:.66,low:.34}[normalize(c.tr_sellability)] ?? .45;
  const status=/verified|commercial|official/i.test(c.status||'') ? 1 : /encyclopedia/i.test(c.status||'') ? .68 : .5;
  const outcome=(c.reported_amount||c.reported_result) ? 1 : .55;
  const code=c.repo_url ? 1 : .5;
  return .34*evidence + .23*sell + .16*status + .15*outcome + .12*code;
}

export function caseMatchesMode(c, mode='all') {
  if (c.evidence_grade === 'X') return false;
  if (mode === 'verified') return c.evidence_grade === 'A';
  if (mode === 'high') return normalize(c.tr_sellability) === 'high';
  if (mode === 'code') return Boolean(c.repo_url);
  if (mode === 'local') return /yerel|musteri|iletisim|destek|servis|randevu|otel|klinik|repair|appointment|booking|whatsapp/i.test(`${c.niche} ${c.work_model} ${c.client_type}`);
  return true;
}

function addWeighted(map, key, weight) {
  if (!key) return;
  map.set(key,(map.get(key)||0)+weight);
}

function topEntries(map, limit=6) {
  return [...map.entries()].sort((a,b)=>b[1]-a[1]).slice(0,limit).map(([value,score])=>({value,score}));
}

function extractCaseFeatures(c) {
  const nicheAliases=phraseAliases(c.niche);
  const workAliases=phraseAliases(c.work_model);
  const clientAliases=phraseAliases(c.client_type);
  const stackAliases=stackPhrases(c.stack);
  const titleAliases=phraseAliases(c.title);
  const summaryAliases=phraseAliases(c.summary);
  const rawClients=[compactPhrase(c.client_type,4)];
  const rawWork=[compactPhrase(c.work_model,4)];
  const rawNiche=[compactPhrase(c.niche,3)];
  const rawTitle=[compactPhrase(c.title,4)];
  return {
    niche: unique([...nicheAliases,...rawNiche]).filter(Boolean),
    work: unique([...workAliases,...rawWork]).filter(Boolean),
    clients: unique([...clientAliases,...rawClients]).filter(Boolean),
    stacks: unique(stackAliases),
    keywords: unique([...titleAliases,...summaryAliases,...rawTitle,...words(c.summary).slice(0,8)]).filter(Boolean)
  };
}

function patternId(niche='unknown') { return `niche:${normalize(niche)||'unknown'}`; }

function simpleHash(text) {
  let h=2166136261;
  for (let i=0;i<text.length;i++) { h ^= text.charCodeAt(i); h = Math.imul(h,16777619); }
  return (h>>>0).toString(36);
}

export function buildDiscoveryModel(cases, {mode='all'}={}) {
  const eligible=cases.filter(c=>caseMatchesMode(c,mode));
  const groups=new Map();
  const global={niche:new Map(),work:new Map(),clients:new Map(),stacks:new Map(),keywords:new Map()};
  const caseVectors=[];

  for (const c of eligible) {
    const weight=caseWeight(c);
    const features=extractCaseFeatures(c);
    const id=patternId(c.niche);
    if (!groups.has(id)) groups.set(id,{id,label:c.niche||'unknown',score:0,support:0,caseIds:[],niche:new Map(),work:new Map(),clients:new Map(),stacks:new Map(),keywords:new Map()});
    const g=groups.get(id);
    g.score+=weight; g.support+=1; g.caseIds.push(c.id);
    for (const [field, multiplier] of [['niche',1.35],['work',1.2],['clients',1.05],['stacks',1.15],['keywords',.55]]) {
      for (const term of features[field]) {
        addWeighted(g[field],term,weight*multiplier);
        addWeighted(global[field],term,weight*multiplier);
      }
    }
    caseVectors.push({id:c.id,weight,text:`${c.title} ${c.niche} ${c.work_model} ${c.client_type} ${c.stack} ${c.summary}`,tokens:new Set(words(`${c.title} ${c.niche} ${c.work_model} ${c.client_type} ${c.stack} ${c.summary}`)),raw:c});
  }

  const patterns=[...groups.values()].map(g=>({
    id:g.id,label:g.label,caseIds:g.caseIds, support:g.support,
    score:g.score*(1+Math.log1p(g.support)*.22),
    niche:topEntries(g.niche,5), work:topEntries(g.work,6), clients:topEntries(g.clients,5), stacks:topEntries(g.stacks,6), keywords:topEntries(g.keywords,8)
  })).sort((a,b)=>b.score-a.score);

  const signature=eligible.map(c=>[c.id,c.evidence_grade,c.niche,c.work_model,c.client_type,c.stack,c.tr_sellability,c.reported_amount,c.reported_result].join('|')).sort().join('\n');
  return {
    mode,
    version:`cases-${simpleHash(signature)}`,
    eligibleCount:eligible.length,
    patterns,
    globals:{niche:topEntries(global.niche,8),work:topEntries(global.work,10),clients:topEntries(global.clients,8),stacks:topEntries(global.stacks,10),keywords:topEntries(global.keywords,12)},
    caseVectors
  };
}

function cleanQueryPart(value='') {
  return normalize(value).split(' ').filter(x=>x.length>1 && !['unknown','belirsiz'].includes(x)).slice(0,4).join(' ');
}

function makeQuery(text, meta={}) {
  const core=normalize(text).split(' ').filter(Boolean).slice(0,9).join(' ');
  if (!core) return null;
  const stars=Number.isFinite(meta.stars) && meta.stars>0 ? ` stars:>${Math.floor(meta.stars)}` : '';
  const {stars: _stars, ...rest}=meta;
  return {...rest,text:`${core}${stars} archived:false fork:false`,signature:`${core}|stars>${Math.max(0,Math.floor(meta.stars||0))}`};
}

export function synthesizeQueries(model,{limit=6,stars=3}={}) {
  const queries=[];
  const seen=new Set();
  const push=(text,meta)=>{
    const q=makeQuery(text,meta); if(!q||seen.has(q.signature)||queries.length>=limit)return;
    seen.add(q.signature); queries.push({...q,id:`q${queries.length+1}`});
  };

  for (const p of model.patterns) {
    if (queries.length>=limit) break;
    const niche=cleanQueryPart(p.niche[0]?.value || p.label);
    const work=cleanQueryPart(p.work[0]?.value || p.keywords[0]?.value);
    const client=cleanQueryPart(p.clients[0]?.value);
    const stack=cleanQueryPart(p.stacks[0]?.value);
    push(`${stack} ${work}`,{stage:'anchor',patternId:p.id,caseIds:p.caseIds.slice(0,8),confidence:p.score,stars});
    push(`${client} ${work}`,{stage:'buyer',patternId:p.id,caseIds:p.caseIds.slice(0,8),confidence:p.score*.92,stars});
    push(`${niche} ${stack||work}`,{stage:'implementation',patternId:p.id,caseIds:p.caseIds.slice(0,8),confidence:p.score*.88,stars});
  }

  if (queries.length<limit) {
    const gWork=cleanQueryPart(model.globals.work[0]?.value);
    const gStack=cleanQueryPart(model.globals.stacks[0]?.value);
    const gClient=cleanQueryPart(model.globals.clients[0]?.value);
    push(`${gStack} ${gWork}`,{stage:'global',patternId:null,caseIds:[],confidence:.5,stars});
    push(`${gClient} ${gWork}`,{stage:'global',patternId:null,caseIds:[],confidence:.45,stars});
  }
  return queries;
}

export function synthesizeRefinementQueries(model, coverage=new Map(), existing=[], {limit=3}={}) {
  const seen=new Set(existing.map(q=>q.signature||normalize(q.text)));
  const queries=[];
  const push=(text,meta)=>{
    const q=makeQuery(text,meta); if(!q||seen.has(q.signature)||queries.length>=limit)return;
    seen.add(q.signature); queries.push({...q,id:`r${queries.length+1}`});
  };
  const under=model.patterns.slice().sort((a,b)=>(coverage.get(a.id)||0)-(coverage.get(b.id)||0) || b.score-a.score);
  for (const p of under) {
    if(queries.length>=limit) break;
    const work=cleanQueryPart(p.work[0]?.value || p.keywords[0]?.value);
    const niche=cleanQueryPart(p.niche[0]?.value || p.label);
    const stack=cleanQueryPart(p.stacks[0]?.value);
    push(`${work||niche} ${stack}`,{stage:'refine',patternId:p.id,caseIds:p.caseIds.slice(0,8),confidence:p.score*.75,stars:1});
  }
  return queries;
}

function tokenSet(value='') { return new Set(words(value)); }
function similaritySets(A,B) {
  if(!A.size||!B.size)return 0;
  let n=0; for(const x of A) if(B.has(x)) n++;
  return n/Math.sqrt(A.size*B.size);
}

export function nearestCases(repo,model,readme='',limit=4) {
  const rt=tokenSet(`${repo.name||''} ${repo.full_name||''} ${repo.description||''} ${(repo.topics||[]).join(' ')} ${readme}`);
  return model.caseVectors.map(v=>({case:v.raw,score:similaritySets(rt,v.tokens)+.08*v.weight})).sort((a,b)=>b.score-a.score).slice(0,limit);
}

export function patternSimilarity(repo,pattern,readme='') {
  const rt=tokenSet(`${repo.name||''} ${repo.full_name||''} ${repo.description||''} ${(repo.topics||[]).join(' ')} ${readme}`);
  const pt=tokenSet([
    ...pattern.niche.map(x=>x.value),...pattern.work.map(x=>x.value),...pattern.clients.map(x=>x.value),...pattern.stacks.map(x=>x.value),...pattern.keywords.map(x=>x.value)
  ].join(' '));
  return similaritySets(rt,pt);
}

export function bestPattern(repo,model,readme='') {
  let best=null;
  for(const p of model.patterns){const score=patternSimilarity(repo,p,readme);if(!best||score>best.score)best={pattern:p,score};}
  return best;
}

export function scoreRepository(repo,model,lineage=[],readme='') {
  const age=repo.pushed_at?(Date.now()-new Date(repo.pushed_at))/864e5:9999;
  const stars=Math.min(1,Math.log10((repo.stargazers_count||0)+1)/4);
  const recency=Math.exp(-Math.max(0,age)/540);
  const license=repo.license?.spdx_id?1:.35;
  const description=(repo.description||'').length>20?1:.35;
  const technical=.31*stars+.29*recency+.2*license+.2*description;
  const peers=nearestCases(repo,model,readme,5);
  const archiveFit=peers.length?Math.min(1,peers.slice(0,3).reduce((a,x)=>a+x.score,0)/Math.min(3,peers.length)):0;
  const bp=bestPattern(repo,model,readme);
  const patternFit=bp?.score||0;
  const queryHits=unique(lineage.map(x=>x.queryId)).length;
  const provenance=Math.min(1,.25*queryHits + .18*unique(lineage.map(x=>x.patternId).filter(Boolean)).length);
  const score=Math.min(1,.43*technical+.31*archiveFit+.18*patternFit+.08*provenance);
  return {score,technical,archiveFit,patternFit,provenance,bestPattern:bp?.pattern||null,peers};
}

export function coverageByPattern(candidates) {
  const map=new Map();
  for(const item of candidates) for(const p of unique((item._discovery?.lineage||[]).map(x=>x.patternId).filter(Boolean))) map.set(p,(map.get(p)||0)+1);
  return map;
}

export function diversify(candidates, model, limit=24) {
  const pool=candidates.map(repo=>({repo,base:scoreRepository(repo,model,repo._discovery?.lineage||[]).score}));
  const selected=[];
  while(pool.length&&selected.length<limit){
    let bestIndex=0,bestScore=-Infinity;
    for(let i=0;i<pool.length;i++){
      const item=pool[i];
      let penalty=0;
      for(const s of selected.slice(-8)){
        const A=tokenSet(`${item.repo.full_name} ${item.repo.description||''} ${(item.repo.topics||[]).join(' ')}`);
        const B=tokenSet(`${s.full_name} ${s.description||''} ${(s.topics||[]).join(' ')}`);
        penalty=Math.max(penalty,similaritySets(A,B));
      }
      const jitter=Math.random()*.08;
      const score=item.base-.26*penalty+jitter;
      if(score>bestScore){bestScore=score;bestIndex=i;}
    }
    selected.push(pool.splice(bestIndex,1)[0].repo);
  }
  return selected;
}
