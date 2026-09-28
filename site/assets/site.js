(function(){
  const UI=window.UI||{};
  // 언어: 페이지마다 정적 URL이 따로 있다(/, /ko/, /zh/). 링크를 누르면 그 언어를 기억한다.
  document.querySelectorAll('.lang a').forEach(a=>a.addEventListener('click',()=>{try{localStorage.setItem('lang',a.getAttribute('hreflang').slice(0,2));}catch(e){}}));
  // 기억한 언어가 있고 지금 영어 기본 페이지로 들어왔다면 그 언어 페이지로 한 번 옮긴다. 검색엔진 봇은 localStorage가 비어 있어 영향이 없다.
  try{const saved=localStorage.getItem('lang'),cur=(document.documentElement.lang||'en').slice(0,2);
    if(saved&&saved!==cur&&cur==='en'&&!sessionStorage.getItem('langRedirected')){const t=document.querySelector('.lang a[hreflang^="'+saved+'"]');if(t){sessionStorage.setItem('langRedirected','1');location.replace(t.href);return;}}}catch(e){}
  // install tabs
  document.querySelectorAll('.install').forEach(box=>{
    box.querySelectorAll('.tabs button').forEach(b=>b.addEventListener('click',()=>{
      box.querySelectorAll('.tabs button').forEach(x=>x.setAttribute('aria-selected',x===b));
      box.querySelectorAll('.cmd').forEach(c=>c.hidden=c.dataset.tab!==b.dataset.tab);
    }));
  });
  async function copy(text,btn){const o=btn.innerHTML;try{await navigator.clipboard.writeText(text);btn.innerHTML=UI._copied||'✓';}catch(e){btn.innerHTML='⌘C';}setTimeout(()=>btn.innerHTML=o,1500);}
  document.addEventListener('click',e=>{const b=e.target.closest('.copy[data-copy]');if(!b)return;
    if(b.dataset.copy==='picked')return copy(pickedCmd(),b);
    copy(b.closest('.cmd').querySelector('pre').innerText.trim(),b);});
  // pick bar
  const bar=document.querySelector('.bar');
  function picked(){return [...document.querySelectorAll('.pick input:checked')].map(i=>i.value);}
  function pickedCmd(){return ['/plugin marketplace add https://github.com/fivetaku/gptaku_plugins.git',...picked().map(n=>'/plugin install '+n+'@gptaku-plugins')].join('\n');}
  function updateBar(){if(!bar)return;const n=picked().length;bar.classList.toggle('show',n>0);bar.querySelector('b').textContent=(UI.bar_n||'{n}').replace('{n}',n);
    document.querySelectorAll('.pick input').forEach(i=>i.closest('.row').classList.toggle('on',i.checked));}
  document.querySelectorAll('.pick input').forEach(i=>i.addEventListener('change',updateBar));
  bar&&bar.querySelector('.clear').addEventListener('click',()=>{document.querySelectorAll('.pick input').forEach(i=>i.checked=false);updateBar();});
  updateBar();
})();
