(function(){
  const D=window.I18N||{},LANGS=['en','ko','zh'];
  const q=new URLSearchParams(location.search).get('lang');
  let lang=LANGS.includes(q)?q:(localStorage.getItem('lang')||'');
  if(!LANGS.includes(lang))lang='en';
  function t(k){return (D[lang]&&D[lang][k]!=null)?D[lang][k]:(D.en&&D.en[k])||'';}
  function apply(l){
    lang=l;localStorage.setItem('lang',l);document.documentElement.lang=l==='zh'?'zh-CN':l;
    document.querySelectorAll('[data-i]').forEach(e=>{const v=t(e.dataset.i);if(v)e.innerHTML=v;});
    document.querySelectorAll('[data-i-attr]').forEach(e=>{e.dataset.iAttr.split(';').forEach(p=>{const[a,k]=p.split(':');const v=t(k);if(v)e.setAttribute(a,v);});});
    document.querySelectorAll('video[data-base]').forEach(v=>{const s=v.dataset.base+'-'+l+'.mp4';if(!v.src.endsWith(s)){v.src=s;v.poster=v.dataset.base+'-'+l+'-poster.png';v.play&&v.play().catch(()=>{});}});
    document.querySelectorAll('.lang button').forEach(b=>b.setAttribute('aria-pressed',b.dataset.l===l));
    if(D[l]&&D[l]._title)document.title=D[l]._title;
    updateBar();
  }
  document.querySelectorAll('.lang button').forEach(b=>b.addEventListener('click',()=>apply(b.dataset.l)));
  // install tabs
  document.querySelectorAll('.install').forEach(box=>{
    box.querySelectorAll('.tabs button').forEach(b=>b.addEventListener('click',()=>{
      box.querySelectorAll('.tabs button').forEach(x=>x.setAttribute('aria-selected',x===b));
      box.querySelectorAll('.cmd').forEach(c=>c.hidden=c.dataset.tab!==b.dataset.tab);
    }));
  });
  async function copy(text,btn){const o=btn.innerHTML;try{await navigator.clipboard.writeText(text);btn.innerHTML=t('_copied')||'✓';}catch(e){btn.innerHTML='⌘C';}setTimeout(()=>btn.innerHTML=o,1500);}
  document.addEventListener('click',e=>{const b=e.target.closest('.copy[data-copy]');if(!b)return;
    if(b.dataset.copy==='picked')return copy(pickedCmd(),b);
    copy(b.closest('.cmd').querySelector('pre').innerText.trim(),b);});
  // pick bar
  const bar=document.querySelector('.bar');
  function picked(){return [...document.querySelectorAll('.pick input:checked')].map(i=>i.value);}
  function pickedCmd(){return ['/plugin marketplace add https://github.com/fivetaku/gptaku_plugins.git',...picked().map(n=>'/plugin install '+n+'@gptaku-plugins')].join('\n');}
  function updateBar(){if(!bar)return;const n=picked().length;bar.classList.toggle('show',n>0);bar.querySelector('b').textContent=(t('bar_n')||'{n}').replace('{n}',n);
    document.querySelectorAll('.pick input').forEach(i=>i.closest('.row').classList.toggle('on',i.checked));}
  document.querySelectorAll('.pick input').forEach(i=>i.addEventListener('change',updateBar));
  bar&&bar.querySelector('.clear').addEventListener('click',()=>{document.querySelectorAll('.pick input').forEach(i=>i.checked=false);updateBar();});
  apply(lang);
})();
