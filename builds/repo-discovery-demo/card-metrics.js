const card=document.querySelector('#repoCard');

if(card){
  const COLORS=['#d9534f','#e5843f','#d6c84b','#4fb274'];
  const QUALITY_ORDER=['X','C','B','A'];
  const REVENUE_ORDER=['V','S','R','F'];
  const REVENUE_LABELS={
    V:'başka ticari sonuç',
    S:'müşteri tasarrufu',
    R:'ürün geliri',
    F:'işi yapana ödenen ücret'
  };
  const SELLABILITY_ORDER=['low','medium','high'];
  const DIFFICULTY_ORDER=['easy','easy-medium','medium','medium-hard','hard'];
  let gradientSeq=0;

  const esc=(s='')=>String(s??'').replace(/[&<>"']/g,c=>({
    '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'
  }[c]));

  function gradientId(prefix){
    gradientSeq+=1;
    return `${prefix}-${gradientSeq}`;
  }

  function semiGauge(level,max,labels){
    const id=gradientId('semi');
    const known=Number.isFinite(level);
    const ratio=known&&max>0?Math.max(0,Math.min(1,level/max)):.5;
    const theta=Math.PI*(1-ratio);
    const x=75+Math.cos(theta)*42;
    const y=70-Math.sin(theta)*42;
    const needle=known
      ?`<line class="gauge-needle" x1="75" y1="70" x2="${x.toFixed(2)}" y2="${y.toFixed(2)}"></line><circle class="gauge-hub" cx="75" cy="70" r="4.8"></circle>`
      :'';
    return `<div class="semi-gauge-wrap">
      <svg class="gauge-svg" viewBox="0 0 150 82" aria-hidden="true" focusable="false">
        <defs>
          <linearGradient id="${id}" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="${COLORS[0]}"></stop>
            <stop offset="33%" stop-color="${COLORS[1]}"></stop>
            <stop offset="66%" stop-color="${COLORS[2]}"></stop>
            <stop offset="100%" stop-color="${COLORS[3]}"></stop>
          </linearGradient>
        </defs>
        <path d="M23 70 A52 52 0 0 1 127 70" pathLength="100" fill="none" stroke="${known?`url(#${id})`:'#46515c'}" stroke-width="12" stroke-linecap="round"></path>
        ${needle}
      </svg>
      <div class="semi-scale">${labels.map(x=>`<span>${esc(x)}</span>`).join('')}</div>
    </div>`;
  }

  function verticalGauge(level,max,labels,kind){
    const id=gradientId('vertical');
    const known=Number.isFinite(level);
    const ratio=known&&max>0?Math.max(0,Math.min(1,level/max)):.5;
    const y=89-(ratio*70);
    const top=kind==='difficulty'?COLORS[0]:COLORS[3];
    const mid=COLORS[2];
    const bottom=kind==='difficulty'?COLORS[3]:COLORS[0];
    const marker=known
      ?`<line class="gauge-needle" x1="17" y1="${y.toFixed(2)}" x2="49" y2="${y.toFixed(2)}"></line><polygon points="49,${y.toFixed(2)} 60,${(y-6).toFixed(2)} 60,${(y+6).toFixed(2)}" fill="#f1f5f8"></polygon>`
      :'';
    return `<div class="vertical-gauge-wrap">
      <svg class="vertical-gauge-svg" viewBox="0 0 66 108" aria-hidden="true" focusable="false">
        <defs>
          <linearGradient id="${id}" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="${top}"></stop>
            <stop offset="50%" stop-color="${mid}"></stop>
            <stop offset="100%" stop-color="${bottom}"></stop>
          </linearGradient>
        </defs>
        <line x1="33" y1="19" x2="33" y2="89" stroke="${known?`url(#${id})`:'#46515c'}" stroke-width="12" stroke-linecap="round"></line>
        ${marker}
      </svg>
      <div class="vertical-scale">${labels.map(x=>`<span>${esc(x)}</span>`).join('')}</div>
    </div>`;
  }

  function textLabel(metric){
    const node=[...metric.childNodes].find(n=>n.nodeType===Node.TEXT_NODE&&n.textContent.trim());
    return node?.textContent.trim()||'';
  }

  function normalizeDifficulty(raw){
    const value=String(raw||'').trim().toLowerCase().replace(/[\s_]+/g,'-');
    if(DIFFICULTY_ORDER.includes(value)) return value;
    if(value.includes('hard')&&value.includes('medium')) return 'medium-hard';
    if(value.includes('easy')&&value.includes('medium')) return 'easy-medium';
    if(value.includes('hard')) return 'hard';
    if(value.includes('easy')) return 'easy';
    if(value.includes('medium')) return 'medium';
    return '';
  }

  function visualize(metric,label,raw){
    metric.dataset.visualized='true';
    metric.classList.add('metric-visual');

    if(label==='Kanıt'){
      const value=String(raw||'').trim().toUpperCase();
      const level=QUALITY_ORDER.indexOf(value);
      metric.dataset.kind='quality';
      metric.setAttribute('aria-label',`Quality ${value||'belirsiz'}; soldan sağa X, C, B, A`);
      metric.innerHTML=`<span class="metric-label">Quality</span>${semiGauge(level>=0?level:null,3,QUALITY_ORDER)}<span class="metric-value">${esc(value||'—')}</span>`;
      return;
    }

    if(label==='Gelir türü'){
      const value=String(raw||'').trim().toUpperCase();
      const level=REVENUE_ORDER.indexOf(value);
      const money=level>=0?'💸'.repeat(level+1):'—';
      const caption=level>=0?`${value} · ${REVENUE_LABELS[value]}`:'sınıf belirtilmemiş';
      metric.dataset.kind='revenue';
      metric.setAttribute('aria-label',`Gelir türü ${caption}; doğrudanlık göstergesi ${level>=0?level+1:'belirsiz'} / 4`);
      metric.innerHTML=`<span class="metric-label">Gelir türü</span>${semiGauge(level>=0?level:null,3,REVENUE_ORDER)}<span class="metric-value money-value">${money}</span><span class="metric-caption">${esc(caption)}</span>`;
      return;
    }

    if(label==='TR satılabilirlik'){
      const value=String(raw||'').trim().toLowerCase();
      const level=SELLABILITY_ORDER.indexOf(value);
      metric.dataset.kind='sellability';
      metric.setAttribute('aria-label',`TR satılabilirlik ${value||'belirsiz'}; alt low, orta medium, üst high`);
      metric.innerHTML=`<span class="metric-label">TR satılabilirlik</span>${verticalGauge(level>=0?level:null,2,['high','medium','low'],'sellability')}<span class="metric-value">${esc(value||'—')}</span>`;
      return;
    }

    if(label==='Zorluk'){
      const value=normalizeDifficulty(raw);
      const level=DIFFICULTY_ORDER.indexOf(value);
      metric.dataset.kind='difficulty';
      metric.setAttribute('aria-label',`Zorluk ${value||'belirsiz'}; alt easy, üst hard`);
      metric.innerHTML=`<span class="metric-label">Zorluk</span>${verticalGauge(level>=0?level:null,4,['hard','medium','easy'],'difficulty')}<span class="metric-value">${esc(value||raw||'—')}</span>`;
    }
  }

  function transformArchiveCard(){
    if(card.classList.contains('frontier')) return;

    const owner=card.querySelector('.owner');
    if(owner) owner.remove();

    const metrics=[...card.querySelectorAll('.metric')];
    for(const metric of metrics){
      if(metric.dataset.visualized==='true') continue;
      const label=textLabel(metric);
      const raw=metric.querySelector('b')?.textContent?.trim()||'';
      if(['Kanıt','Gelir türü','TR satılabilirlik','Zorluk'].includes(label)){
        visualize(metric,label,raw);
      }
    }
  }

  const observer=new MutationObserver(()=>transformArchiveCard());
  observer.observe(card,{childList:true,subtree:true});
  transformArchiveCard();
}
