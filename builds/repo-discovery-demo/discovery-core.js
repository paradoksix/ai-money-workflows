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
    .replace(/Ä±/g,'i')
    .replace(/ÄŸ/g,'g')
    .replace(/ÅŸ/g,'s')
    .replace(/Ã§/g,'c')
    .replace(/Ã¶/g,'o')
    .replace(/Ã¼/g,'u')
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g,'')
    .replace(/[â€™']/g,'')
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
  if(!A.size||!B,¹Í¥é”¥É•ÑÕÉ¸€Àì(€±•Ğ¸ôÀì™½È¡½¹ÍĞà½˜¤¥˜¡¹¡…Ì¡à¤¤¸¬¬ì(€É•ÑÕÉ¸¸½5…Ñ ¹ÍÅÉĞ¡¹Í¥é”©¹Í¥é”¤ì)ô()•áÁ½ÉĞ™Õ¹Ñ¥½¸¹•…É•ÍÑ…Í•Ì¡É•Á¼±µ½‘•°±É•…‘µ”ôœœ±±¥µ¥ĞôĞ¤ì(€½¹ÍĞÉĞõÑ½­•¹M•Ğ¡€‘íÉ•Á¼¹¹…µ•ñğœô€‘íÉ•Á¼¹™Õ±±}¹…µ•ñğœô€‘íÉ•Á¼¹‘•ÍÉ¥ÁÑ¥½¹ñğœô€‘ì¡É•Á¼¹Ñ½Á¥Íññmt¤¹©½¥¸ œ€œ¥ô€‘íÉ•…‘µ•õ€¤ì(€É•ÑÕÉ¸µ½‘•°¹…Í•Y•Ñ½ÉÌ¹µ…À¡Øôø¡í…Í”éØ¹É…Ü±Í½É”éÍ¥µ¥±…É¥ÑåM•ÑÌ¡ÉĞ±Ø¹Ñ½­•¹Ì¤¬¸Àà©Ø¹İ•¥¡Ñô¤¤¹Í½ÉĞ ¡„±ˆ¤ôùˆ¹Í½É”µ„¹Í½É”¤¹Í±¥” À±±¥µ¥Ğ¤ì)ô()•áÁ½ÉĞ™Õ¹Ñ¥½¸Á…ÑÑ•É¹M¥µ¥±…É¥Ñä¡É•Á¼±Á…ÑÑ•É¸±É•…‘µ”ôœœ¤ì(€½¹ÍĞÉĞõÑ½­•¹M•Ğ¡€‘íÉ•Á¼¹¹…µ•ñğœô€‘íÉ•Á¼¹™Õ±±}¹…µ•ñğœô€‘íÉ•Á¼¹‘•ÍÉ¥ÁÑ¥½¹ñğœô€‘ì¡É•Á¼¹Ñ½Á¥Íññmt¤¹©½¥¸ œ€œ¥ô€‘íÉ•…‘µ•õ€¤ì(€½¹ÍĞÁĞõÑ½­•¹M•Ğ¡l(€€€€¸¸¹Á…ÑÑ•É¸¹¹¥¡”¹µ…À¡àôùà¹Ù…±Õ”¤°¸¸¹Á…ÑÑ•É¸¹İ½É¬¹µ…À¡àôùà¹Ù…±Õ”¤°¸¸¹Á…ÑÑ•É¸¹±¥•¹ÑÌ¹µ…À¡àôùà¹Ù…±Õ”¤°¸¸¹Á…ÑÑ•É¸¹ÍÑ…­Ì¹µ…À¡àôùà¹Ù…±Õ”¤°¸¸¹Á…ÑÑ•É¸¹­•åİ½É‘Ì¹µ…À¡àôùà¹Ù…±Õ”¤(€t¹©½¥¸ œ€œ¤¤ì(€É•ÑÕÉ¸Í¥µ¥±…É¥ÑåM•ÑÌ¡ÉĞ±ÁĞ¤ì)ô()•áÁ½ÉĞ™Õ¹Ñ¥½¸‰•ÍÑA…ÑÑ•É¸¡É•Á¼±µ½‘•°±É•…‘µ”ôœœ¤ì(€±•Ğ‰•ÍĞõ¹Õ±°ì(€™½È¡½¹ÍĞÀ½˜µ½‘•°¹Á…ÑÑ•É¹Ì¥í½¹ÍĞÍ½É”õÁ…ÑÑ•É¹M¥µ¥±…É¥Ñä¡É•Á¼±À±É•…‘µ”¤í¥˜ …‰•ÍÑññÍ½É”ù‰•ÍĞ¹Í½É”¥‰•ÍĞõíÁ…ÑÑ•É¸éÀ±Í½É•ôíô(€É•ÑÕÉ¸‰•ÍĞì)ô()•áÁ½ÉĞ™Õ¹Ñ¥½¸Í½É•I•Á½Í¥Ñ½Éä¡É•Á¼±µ½‘•°±±¥¹•…”õmt±É•…‘µ”ôœœ¤ì(€½¹ÍĞ…”õÉ•Á¼¹ÁÕÍ¡•‘}…Ğü¡…Ñ”¹¹½Ü ¤µ¹•Ü…Ñ”¡É•Á¼¹ÁÕÍ¡•‘}…Ğ¤¤¼àØÑ”Ôèääääì(€½¹ÍĞÍÑ…ÉÌõ5…Ñ ¹µ¥¸ Ä±5…Ñ ¹±½œÄÀ ¡É•Á¼¹ÍÑ…É…é•ÉÍ}½Õ¹ÑñğÀ¤¬Ä¤¼Ğ¤ì(€½¹ÍĞÉ••¹äõ5…Ñ ¹•áÀ µ5…Ñ ¹µ…à À±…”¤¼ÔĞÀ¤ì(€½¹ÍĞ±¥•¹Í”õÉ•Á¼¹±¥•¹Í”ü¹ÍÁ‘á}¥üÄè¸ÌÔì(€½¹ÍĞ‘•ÍÉ¥ÁÑ¥½¸ô¡É•Á¼¹‘•ÍÉ¥ÁÑ¥½¹ñğœœ¤¹±•¹Ñ øÈÀüÄè¸ÌÔì(€½¹ÍĞÑ•¡¹¥…°ô¸ÌÄ©ÍÑ…ÉÌ¬¸Èä©É••¹ä¬¸È©±¥•¹Í”¬¸È©‘•ÍÉ¥ÁÑ¥½¸ì(€½¹ÍĞÁ••ÉÌõ¹•…É•ÍÑ…Í•Ì¡É•Á¼±µ½‘•°±É•…‘µ”°Ô¤ì(€½¹ÍĞ…É¡¥Ù•¥ĞõÁ••ÉÌ¹±•¹Ñ ı5…Ñ ¹µ¥¸ Ä±Á••ÉÌ¹Í±¥” À°Ì¤¹É•‘Õ” ¡„±à¤ôù„­à¹Í½É”°À¤½5…Ñ ¹µ¥¸ Ì±Á••ÉÌ¹±•¹Ñ ¤¤èÀì(€½¹ÍĞ‰Àõ‰•ÍÑA…ÑÑ•É¸¡É•Á¼±µ½‘•°±É•…‘µ”¤ì(€½¹ÍĞÁ…ÑÑ•É¹¥Ğõ‰Àü¹Í½É•ñğÀì(€½¹ÍĞÅÕ•Éå!¥ÑÌõÕ¹¥ÅÕ”¡±¥¹•…”¹µ…À¡àôùà¹ÅÕ•Éå%¤¤¹±•¹Ñ ì(€½¹ÍĞÁÉ½Ù•¹…¹”õ5…Ñ ¹µ¥¸ Ä°¸ÈÔ©ÅÕ•Éå!¥ÑÌ€¬€¸Äà©Õ¹¥ÅÕ”¡±¥¹•…”¹µ…À¡àôùà¹Á…ÑÑ•É¹%¤¹™¥±Ñ•È¡	½½±•…¸¤¤¹±•¹Ñ ¤ì(€½¹ÍĞÍ½É”õ5…Ñ ¹µ¥¸ Ä°¸ĞÌ©Ñ•¡¹¥…°¬¸ÌÄ©…É¡¥Ù•¥Ğ¬¸Äà©Á…ÑÑ•É¹¥Ğ¬¸Àà©ÁÉ½Ù•¹…¹”¤ì(€É•ÑÕÉ¸íÍ½É”±Ñ•¡¹¥…°±…É¡¥Ù•¥Ğ±Á…ÑÑ•É¹¥Ğ±ÁÉ½Ù•¹…¹”±‰•ÍÑA…ÑÑ•É¸é‰Àü¹Á…ÑÑ•É¹ññ¹Õ±°±Á••ÉÍôì)ô()•áÁ½ÉĞ™Õ¹Ñ¥½¸½Ù•É…•	åA…ÑÑ•É¸¡…¹‘¥‘…Ñ•Ì¤ì(€½¹ÍĞµ…Àõ¹•Ü5…À ¤ì(€™½È¡½¹ÍĞ¥Ñ•´½˜…¹‘¥‘…Ñ•Ì¤™½È¡½¹ÍĞÀ½˜Õ¹¥ÅÕ” ¡¥Ñ•´¹}‘¥Í½Ù•Éäü¹±¥¹•…•ññmt¤¹µ…À¡àôùà¹Á…ÑÑ•É¹%¤¹™¥±Ñ•È¡	½½±•…¸¤¤¤µ…À¹Í•Ğ¡À°¡µ…À¹•Ğ¡À¥ñğÀ¤¬Ä¤ì(€É•ÑÕÉ¸µ…Àì)ô()•áÁ½ÉĞ™Õ¹Ñ¥½¸‘¥Ù•ÉÍ¥™ä¡…¹‘¥‘…Ñ•Ì°µ½‘•°°±¥µ¥ĞôÈĞ¤ì(€½¹ÍĞÁ½½°õ…¹‘¥‘…Ñ•Ì¹µ…À¡É•Á¼ôø¡íÉ•Á¼±‰…Í”éÍ½É•I•Á½Í¥Ñ½Éä¡É•Á¼±µ½‘•°±É•Á¼¹}‘¥Í½Ù•Éäü¹±¥¹•…•ññmt¤¹Í½É•ô¤¤ì(€½¹ÍĞÍ•±•Ñ•õmtì(€İ¡¥±”¡Á½½°¹±•¹Ñ ˜™Í•±•Ñ•¹±•¹Ñ ñ±¥µ¥Ğ¥ì(€€€±•Ğ‰•ÍÑ%¹‘•àôÀ±‰•ÍÑM½É”ôµ%¹™¥¹¥Ñäì(€€€™½È¡±•Ğ¤ôÀí¤ñÁ½½°¹±•¹Ñ í¤¬¬¥ì(€€€€€½¹ÍĞ¥Ñ•´õÁ½½±m¥tì(€€€€€±•ĞÁ•¹…±ÑäôÀì(€€€€€™½È¡½¹ÍĞÌ½˜Í•±•Ñ•¹Í±¥” ´à¤¥ì(€€€€€€€½¹ÍĞõÑ½­•¹M•Ğ¡€‘í¥Ñ•´¹É•Á¼¹™Õ±±}¹…µ•ô€‘í¥Ñ•´¹É•Á¼¹‘•ÍÉ¥ÁÑ¥½¹ñğœô€‘ì¡¥Ñ•´¹É•Á¼¹Ñ½Á¥Íññmt¤¹©½¥¸ œ€œ¥õ€¤ì(€€€€€€€½¹ÍĞõÑ½­•¹M•Ğ¡€‘íÌ¹™Õ±±}¹…µ•ô€‘íÌ¹‘•ÍÉ¥ÁÑ¥½¹ñğœô€‘ì¡Ì¹Ñ½Á¥Íññmt¤¹©½¥¸ œ€œ¥õ€¤ì(€€€€€€€Á•¹…±Ñäõ5…Ñ ¹µ…à¡Á•¹…±Ñä±Í¥µ¥±…É¥ÑåM•ÑÌ¡±¤¤ì(€€€€€ô(€€€€€½¹ÍĞ©¥ÑÑ•Èõ5…Ñ ¹É…¹‘½´ ¤¨¸Ààì(€€€€€½¹ÍĞÍ½É”õ¥Ñ•´¹‰…Í”´¸ÈØ©Á•¹…±Ñä­©¥ÑÑ•Èì(€€€€€¥˜¡Í½É”ù‰•ÍÑM½É”¥í‰•ÍÑM½É”õÍ½É”í‰•ÍÑ%¹‘•àõ¤íô(€€€ô(€€€Í•±•Ñ•¹ÁÕÍ ¡Á½½°¹ÍÁ±¥”¡‰•ÍÑ%¹‘•à°Ä¥lÁt¹É•Á¼¤ì(€ô(€É•ÑÕÉ¸Í•±•Ñ•ì)ô(