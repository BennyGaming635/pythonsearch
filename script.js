document.querySelectorAll('.bn-mainmenu-toggle, .bn-search-toggle, .close-search').forEach(el => {
 el.setAttribute('role','button'); el.setAttribute('tabindex','0');
 el.addEventListener('keydown', event => {if(event.key === 'Enter' || event.key === ' '){event.preventDefault();el.click();}});
});
const menu=document.querySelector('.bn-mainmenu-toggle');
if(menu)menu.addEventListener('click',()=>menu.setAttribute('aria-expanded',String(menu.classList.contains('active'))));
document.querySelectorAll('video').forEach(video=>{video.muted=true;video.play().catch(()=>{});});
