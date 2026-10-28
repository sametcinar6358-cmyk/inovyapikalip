// İnovYapıKalıp — site scripts
// Every page opens at the top
if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
function goTop() { if (!location.hash) window.scrollTo({ top: 0, left: 0, behavior: 'instant' }); }
goTop();
document.addEventListener('DOMContentLoaded', goTop);
window.addEventListener('pageshow', function (e) { if (e.persisted) goTop(); });
document.addEventListener('DOMContentLoaded', function () {
  // ===== Mobile menu =====
  var burger = document.querySelector('.burger');
  var nav = document.querySelector('.main-nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // ===== Reveal on scroll =====
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  // ===== Contact form -> WhatsApp =====
  var form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = function (id) { var el = document.getElementById(id); return el ? el.value.trim() : ''; };
      var msg = 'Merhaba Ali Bey, web sitesinden ulaşıyorum.\n\n';
      msg += 'Ad Soyad: ' + v('name') + '\n';
      msg += 'Telefon: ' + v('phone') + '\n';
      msg += 'Hizmet: ' + v('service') + '\n';
      if (v('place')) msg += 'Proje yeri: ' + v('place') + '\n';
      if (v('message')) msg += '\nMesaj: ' + v('message');
      window.open('https://wa.me/905313547912?text=' + encodeURIComponent(msg), '_blank');
      form.reset();
    });
  }

  // ===== Gallery filters =====
  var filterBtns = document.querySelectorAll('.filters button');
  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      filterBtns.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      var f = btn.getAttribute('data-filter');
      document.querySelectorAll('.project-group').forEach(function (g) {
        g.classList.toggle('hide', f !== 'all' && g.getAttribute('data-cat') !== f);
      });
      var first = document.querySelector('.project-group:not(.hide)');
      var bar = document.querySelector('.projects .filters');
      if (first && bar && window.scrollY > bar.offsetTop) first.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  // ===== Lightbox =====
  var modal = document.getElementById('imageModal');
  if (!modal) return;
  var modalImg = document.getElementById('modalImage');
  var count = document.getElementById('modalCount');
  var list = [];
  var idx = 0;

  function show() {
    modalImg.src = list[idx].src;
    modalImg.alt = list[idx].alt;
    count.textContent = (idx + 1) + ' / ' + list.length;
  }
  function open(items, i) {
    list = items; idx = i; show();
    modal.classList.add('show');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }
  function close() {
    modal.classList.remove('show');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }
  function step(d) { if (!list.length) return; idx = (idx + d + list.length) % list.length; show(); }

  document.querySelectorAll('[data-gallery]').forEach(function (g) {
    g.addEventListener('click', function (e) {
      var item = e.target.closest('.gallery-item');
      if (!item || item.classList.contains('is-video')) return;
      var visible = Array.prototype.filter.call(g.querySelectorAll('.gallery-item'), function (it) { return !it.classList.contains('hide') && !it.classList.contains('is-video'); });
      var imgs = visible.map(function (it) { return it.querySelector('img'); });
      open(imgs, visible.indexOf(item));
    });
  });

  modal.querySelector('.close').addEventListener('click', close);
  modal.querySelector('.prev').addEventListener('click', function (e) { e.stopPropagation(); step(-1); });
  modal.querySelector('.next').addEventListener('click', function (e) { e.stopPropagation(); step(1); });
  modal.addEventListener('click', function (e) { if (e.target === modal) close(); });
  document.addEventListener('keydown', function (e) {
    if (!modal.classList.contains('show')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') step(-1);
    if (e.key === 'ArrowRight') step(1);
  });
});
