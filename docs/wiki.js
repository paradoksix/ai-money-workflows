// Theme: three states — the viewer's saved choice, or whatever the system says.
(function(){
  var root = document.documentElement;
  try{
    var saved = localStorage.getItem("atlas-theme");
    if(saved) root.setAttribute("data-theme", saved);
  }catch(_){}
  var btn = document.getElementById("theme");
  if(btn) btn.addEventListener("click", function(){
    var dark = getComputedStyle(root).getPropertyValue("--paper").trim().toLowerCase() === "#101318";
    var next = dark ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try{ localStorage.setItem("atlas-theme", next); }catch(_){}
  });

  var toggle = document.getElementById("nav-toggle");
  var nav = document.getElementById("nav");
  if(toggle && nav) toggle.addEventListener("click", function(){
    var open = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
    toggle.textContent = open ? "Menü ▴" : "Menü ▾";
  });
})();
