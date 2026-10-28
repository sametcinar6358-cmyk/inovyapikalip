#!/usr/bin/env python3
"""Generates the static pages for İnovYapıKalıp into the repo folder given as argv[1]."""
import sys, pathlib

OUT = pathlib.Path(sys.argv[1])
TEL = "05313547912"
TEL_INTL = "+905313547912"
TEL_TXT = "0531 354 79 12"
WA = "https://wa.me/905313547912"
IG = "https://www.instagram.com/inovyapikalip/"
SITE = "https://klckarot.com"

ICON = {
    "phone": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.6 10.8a15.1 15.1 0 006.6 6.6l2.2-2.2a1 1 0 011-.25 11.4 11.4 0 003.6.57 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.25.2 2.45.57 3.57a1 1 0 01-.25 1z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a7 7 0 00-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 00-7-7zm0 9.5A2.5 2.5 0 1112 6.5a2.5 2.5 0 010 5z"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 100 20 10 10 0 000-20zm1 11h-5v-2h3V6h2z"/></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 12a5 5 0 100-10 5 5 0 000 10zm0 2c-4.4 0-8 2.2-8 5v3h16v-3c0-2.8-3.6-5-8-5z"/></svg>',
    "ig": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 7a5 5 0 100 10 5 5 0 000-10zm0 8.2a3.2 3.2 0 110-6.4 3.2 3.2 0 010 6.4zM17.3 5.5a1.2 1.2 0 100 2.4 1.2 1.2 0 000-2.4zM21.9 7.9c-.1-1.6-.4-3-1.6-4.2S17.7 2.2 16.1 2.1C14.4 2 9.6 2 7.9 2.1 6.3 2.2 4.9 2.5 3.7 3.7S2.2 6.3 2.1 7.9C2 9.6 2 14.4 2.1 16.1c.1 1.6.4 3 1.6 4.2s2.6 1.5 4.2 1.6c1.7.1 6.5.1 8.2 0 1.6-.1 3-.4 4.2-1.6s1.5-2.6 1.6-4.2c.1-1.7.1-6.5 0-8.2zm-2.2 10a3.3 3.3 0 01-1.9 1.9c-1.3.5-4.4.4-5.8.4s-4.5.1-5.8-.4a3.3 3.3 0 01-1.9-1.9c-.5-1.3-.4-4.4-.4-5.8s-.1-4.5.4-5.8a3.3 3.3 0 011.9-1.9c1.3-.5 4.4-.4 5.8-.4s4.5-.1 5.8.4a3.3 3.3 0 011.9 1.9c.5 1.3.4 4.4.4 5.8s.1 4.5-.4 5.8z"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-.9 1.2-.3.2-.6.1a8.2 8.2 0 01-4-3.5c-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6a1.1 1.1 0 00-.8.4 3.4 3.4 0 00-1 2.5 5.9 5.9 0 001.2 3.1 13.4 13.4 0 005.2 4.6c1.9.8 2.7.9 3.6.8a3.1 3.1 0 002-1.4 2.5 2.5 0 00.2-1.4c-.1-.1-.3-.2-.6-.3zM12 21.8a9.8 9.8 0 01-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1112 21.8zM12 0a12 12 0 00-10.3 18L0 24l6.2-1.6A12 12 0 1012 0z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2l8 3v6c0 5-3.4 9.3-8 11-4.6-1.7-8-6-8-11V5z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
    "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/></svg>',
    "ruler": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="8" width="20" height="8" rx="1"/><path d="M6 8v4M10 8v3M14 8v4M18 8v3"/></svg>',
    "handshake": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 12l4-4 5 2 5-2 4 4-7 7z"/><path d="M8 13l3 3M11 11l3 3"/></svg>',
}

NAV = [
    ("index.html", "Anasayfa"),
    ("hizmetler.html", "Hizmetlerimiz"),
    ("galeri.html", "Projeler"),
    ("hakkimizda.html", "Hakkımızda"),
    ("iletisim.html", "İletişim"),
]

SERVICES = [
    # slug, title, short, image, long, bullets
    ("villa", "Villa Yapımı",
     "Temelden çatıya, anahtar teslim villa inşaatı. Fransa'da 30 yıl boyunca edindiğimiz villa tecrübesini Kayseri'ye getiriyoruz.",
     "images/villa_doseme_donati_hazir.jpg",
     "Arsanızın keşfinden anahtar teslimine kadar villanızın her aşamasını tek elden yönetiyoruz. Fransa'da yıllarca villa yapımında edindiğimiz disiplin ve işçilik anlayışıyla, sağlam ve uzun ömürlü yapılar inşa ediyoruz.",
     ["Arsa keşfi ve proje üzerinden net teklif", "Hafriyat, temel ve kaba inşaatın tamamı", "Kalıp, demir ve beton işleri kendi ekibimizle", "Çatıya kadar düzenli şantiye takibi ve bilgilendirme"]),
    ("hafriyat", "Hafriyat",
     "Temel kazısı, bodrum kazısı ve saha düzenleme. Zemin hazırlığını doğru yapıyoruz ki yapınız sağlam başlasın.",
     "images/hafriyat_kaya_kazi.jpg",
     "Her sağlam yapı doğru yapılmış bir kazıyla başlar. Projeye uygun kotlarda temel ve bodrum kazısı yapıyor, zemini temel imalatına hazır hale getiriyoruz.",
     ["Temel ve bodrum kazısı", "Kot ve şev kontrolü", "Saha düzenleme ve dolgu", "Toprak ve moloz nakli organizasyonu"]),
    ("kalip", "Kalıp",
     "Temel, kolon, perde ve döşeme kalıpları. Ölçüsü tam, terazisi düzgün kalıp — betonun şeklini kalıp belirler.",
     "images/kalip_perde_donati.jpg",
     "Betonun kalitesi kalıbın kalitesiyle başlar. Temelden döşemeye kadar tüm kalıp işlerini ölçüye, şakuluna ve terazisine sadık kalarak kuruyoruz.",
     ["Radye ve sürekli temel kalıbı", "Kolon, kiriş ve perde kalıbı", "Döşeme kalıbı ve iskele", "Söküm ve temiz şantiye teslimi"]),
    ("demir", "Demir (Betonarme Donatı)",
     "Projeye uygun donatı kesimi, bükümü ve montajı. Etriye, filiz ve paspayına kadar statik projeye birebir uygulama.",
     "images/demir_kalip_perde_duvar.jpg",
     "Yapının iskeleti demirdir. Statik projeye birebir uyarak donatıyı kesiyor, büküyor ve bağlıyoruz; etriye sıklığına, bindirme boylarına ve paspayına özen gösteriyoruz.",
     ["Donatı kesim ve büküm", "Temel, kolon, kiriş ve döşeme donatısı", "Etriye, filiz ve paspayı kontrolü", "Beton öncesi donatı kontrolüne hazır teslim"]),
    ("beton", "Beton",
     "Beton dökümü, vibrasyon ve kür. Doğru sınıf beton, doğru yerleşim ve sağlam bir sonuç.",
     "images/beton_pompa_perde_dokumu.jpg",
     "Kalıp ve demir hazır olduğunda beton dökümünü planlı ve kontrollü yapıyoruz. Vibratörle doğru yerleşim, yüzey düzeltme ve kür ile betonun tam dayanımına ulaşmasını sağlıyoruz.",
     ["Temel, kolon, perde ve döşeme dökümü", "Vibrasyon ve yüzey düzeltme", "Beton kürü ve takibi", "Hazır beton sipariş koordinasyonu"]),
    ("karot", "Karot & Güçlendirme",
     "Betona karot delme ve epoksi filiz ekme. Tesisat geçişleri, baca delikleri ve kolon-temel güçlendirme.",
     "images/karot_makinesi_hilti_delme.jpeg",
     "Mevcut yapılar için de yanınızdayız. Profesyonel karot makineleriyle betonarme elemanlarda temiz ve hassas delik açıyor, gerektiğinde epoksi filiz ekme ile güçlendirme yapıyoruz.",
     ["Doğalgaz baca ve kombi çıkış delikleri", "Tesisat, boru ve kablo geçişleri", "Perde beton ve döşeme delme", "Epoksi filiz ekme ve kolon güçlendirme"]),
]

GALLERY = [
    # img (or video:name), caption, category, extra class
    ("images/beton_pompa_doseme_dokumu.jpg", "Pompa ile döşeme betonu dökümü", "beton", "wide"),
    ("images/beton_pompa_perde_dokumu.jpg", "Perde beton dökümü", "beton", "tall"),
    ("images/hafriyat_temel_cukuru.jpg", "Temel çukuru kazısı", "hafriyat", "tall"),
    ("images/temel_radye_yalitim.jpg", "Radye temel ve yalıtım hazırlığı", "temel", ""),
    ("images/kalip_perde_donati.jpg", "Perde kalıbı ve donatı", "kalip", ""),
    ("images/villa_doseme_donati_hazir.jpg", "Döşeme donatısı beton öncesi", "beton", "wide"),
    ("images/hafriyat_kaya_kazi.jpg", "Kayalık zeminde kazı", "hafriyat", ""),
    ("images/demir_kalip_perde_duvar.jpg", "Perde duvar demir ve kalıbı", "kalip", "tall"),
    ("video:karot_perde_delme_1", "Perde betona karot delme", "karot", "tall"),
    ("images/temel_yalitim_hazirlik.jpg", "Temel yalıtımı", "temel", ""),
    ("images/villa_kaba_insaat_kalip.jpg", "Villa kaba inşaat", "beton", ""),
    ("images/hafriyat_temel_kazisi.jpg", "Temel kazısı", "hafriyat", "tall"),
    ("images/demir_perde_donati.jpg", "Perde donatısı", "kalip", ""),
    ("images/beton_perde_kalip_santiye.jpg", "Perde kalıbında beton dökümü", "beton", "tall"),
    ("images/temel_grobeton_yalitim.jpg", "Temel tabanı hazırlığı", "temel", ""),
    ("images/hafriyat_temel_aplikasyon.jpg", "Temel aplikasyonu", "hafriyat", ""),
    ("images/villa_doseme_donati_kolon_filiz.jpg", "Döşeme ve kolon filizleri", "beton", "wide"),
    ("images/kalip_perde_beton_sokum.jpg", "Kalıp sökümü sonrası perde", "kalip", ""),
    ("images/temel_perde_bodrum.jpg", "Bodrum perde duvarları", "temel", ""),
    ("images/hafriyat_derin_kazi.jpg", "Derin kazı", "hafriyat", "tall"),
    ("images/kesif_lazer_olcum.jpg", "Keşif ve lazer ölçüm", "hafriyat", ""),
    ("images/hafriyat_kanal_kazisi.jpg", "Kanal kazısı", "hafriyat", ""),
    ("video:karot_perde_delme_2", "Karot makinesi ile delme", "karot", "tall"),
    ("images/karot_makinesi_hilti_delme.jpeg", "Karot makinesi", "karot", ""),
    ("images/karot_ile_zemin_delme_islemi.jpeg", "Zeminde karot delme", "karot", ""),
    ("images/kolon_kalip_demircilik.jpg", "Kolon güçlendirme kalıp ve demir", "guclendirme", "tall"),
    ("images/kolon_guclendirme_donati_kafesi.jpeg", "Kolon donatı kafesi", "guclendirme", ""),
    ("images/kolon_guclendirme_epoksi_filiz_ekme.jpeg", "Epoksi filiz ekme", "guclendirme", ""),
    ("images/celik_kolon_temel_baglantisi.jpeg", "Çelik kolon temel bağlantısı", "guclendirme", ""),
    ("images/celik_kolon_ankraj_detay.jpg", "Çelik kolon ankraj detayı", "guclendirme", ""),
]
HOME_GALLERY = [GALLERY[1], GALLERY[0], GALLERY[2], GALLERY[3], GALLERY[4]]
GAL_CATS = [("all", "Tümü"), ("hafriyat", "Hafriyat"), ("temel", "Temel"), ("kalip", "Kalıp & Demir"), ("beton", "Beton"), ("karot", "Karot"), ("guclendirme", "Güçlendirme")]


def head(title, desc, page):
    url = SITE + ("/" if page == "index.html" else "/" + page)
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/images/logo.png">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="tr_TR">
<meta name="theme-color" content="#111214">
<link rel="icon" type="image/png" href="images/favicon.png">
<link rel="apple-touch-icon" href="images/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Barlow+Condensed:wght@600;700&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
"""


def header(page):
    links = "\n".join(
        f'        <li><a href="{href}"{" class=\"active\"" if href == page else ""}>{label}</a></li>' for href, label in NAV
    )
    return f"""
<header class="site-header">
  <div class="wrap">
    <nav class="main-nav">
      <a href="index.html" class="brand" aria-label="İnovYapıKalıp anasayfa">
        <img src="images/logo-sm.webp" alt="İnovYapıKalıp logosu" width="54" height="54">
        <span>
          <span class="brand-name">İNOVYAPIKALIP</span>
          <span class="brand-sub">Ali Kılıç · İnşaat</span>
        </span>
      </a>
      <ul class="nav-links">
{links}
      </ul>
      <a href="tel:{TEL}" class="btn btn-gold nav-cta">Hemen Ara</a>
      <button class="burger" aria-label="Menüyü aç"><span></span><span></span><span></span></button>
    </nav>
  </div>
</header>
"""


def footer():
    svc = "\n".join(f'          <li><a href="hizmetler.html">{s[1]}</a></li>' for s in SERVICES)
    pages = "\n".join(f'          <li><a href="{h}">{l}</a></li>' for h, l in NAV)
    return f"""
<div class="hazard thin"></div>
<footer>
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">
          <img src="images/logo-sm.webp" alt="" width="72" height="72">
          <div>
            <span class="brand-name">İNOVYAPIKALIP</span>
            <span class="brand-sub">Ali Kılıç</span>
          </div>
        </div>
        <p>Temelden çatıya güvenilir işçilik. Fransa'dan 30 yıllık villa yapım tecrübesiyle Kayseri ve çevresinde hizmetinizdeyiz.</p>
        <div class="socials">
          <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ICON['ig']}</a>
          <a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{ICON['wa']}</a>
          <a href="tel:{TEL}" aria-label="Telefon">{ICON['phone']}</a>
        </div>
      </div>
      <div>
        <h4>Hizmetler</h4>
        <ul>
{svc}
        </ul>
      </div>
      <div>
        <h4>Sayfalar</h4>
        <ul>
{pages}
        </ul>
      </div>
      <div>
        <h4>İletişim</h4>
        <ul>
          <li>Ali Kılıç</li>
          <li><a href="tel:{TEL}">{TEL_TXT}</a></li>
          <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp'tan yazın</a></li>
          <li><a href="{IG}" target="_blank" rel="noopener">@inovyapikalip</a></li>
          <li>Kayseri ve çevresi</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 İnovYapıKalıp · Ali Kılıç · Tüm hakları saklıdır.</span>
      <span>Villa · Hafriyat · Kalıp · Demir · Beton · Karot</span>
    </div>
  </div>
</footer>

<a href="{WA}" class="wa-float" target="_blank" rel="noopener" aria-label="WhatsApp ile yazın"><img src="images/whatsapp.png" alt=""></a>

<div class="modal" id="imageModal" aria-hidden="true">
  <button class="close" aria-label="Kapat">&times;</button>
  <button class="prev" aria-label="Önceki">&#8249;</button>
  <img id="modalImage" alt="">
  <button class="next" aria-label="Sonraki">&#8250;</button>
  <span class="count" id="modalCount"></span>
</div>

<script src="js/main.js"></script>
</body>
</html>
"""


def cta_band(title="Projenizi Konuşalım", text="Villa, temel ya da kaba inşaat — keşif ve teklif için hemen arayın veya WhatsApp'tan yazın."):
    return f"""
<section class="cta-band bg-coal texture">
  <div class="wrap reveal">
    <span class="kicker">Ücretsiz keşif & teklif</span>
    <h2>{title}</h2>
    <p>{text}</p>
    <div class="phone-big"><a href="tel:{TEL}" class="gold-text">{TEL_TXT}</a></div>
    <div class="hero-actions">
      <a href="tel:{TEL}" class="btn btn-gold">{ICON['phone'].replace('<svg', '<svg class="icon"')} Hemen Ara</a>
      <a href="{WA}" class="btn btn-wa" target="_blank" rel="noopener">{ICON['wa'].replace('<svg', '<svg class="icon"')} WhatsApp'tan Yaz</a>
    </div>
  </div>
</section>
"""


def page_hero(crumb, title_html, text, bg):
    return f"""
<section class="page-hero">
  <div class="hero-bg" style="background-image:url('{bg}');"></div>
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Anasayfa</a> / {crumb}</div>
    <h1>{title_html}</h1>
    <p>{text}</p>
  </div>
</section>
<div class="hazard"></div>
"""


def service_cards(link=True):
    out = []
    for i, (slug, title, short, img, *_rest) in enumerate(SERVICES, 1):
        sec = slug == "karot"
        out.append(f"""      <a href="hizmetler.html" class="service-card reveal{' secondary' if sec else ''}">
        <div class="media"><span class="num">{i:02d}</span><img src="{img}" alt="{title}" loading="lazy"></div>
        <div class="body">
          {'<span class="tag-mini">Ek hizmet</span>' if sec else ''}
          <h3>{title}</h3>
          <p>{short}</p>
          <span class="more">Detaylı bilgi →</span>
        </div>
      </a>""")
    return "\n".join(out)


def gallery_items(items, cat_attr=True):
    out = []
    for img, cap, cat, cls in items:
        if img.startswith("video:"):
            v = img[6:]
            out.append(f"""      <figure class="gallery-item is-video {cls}" data-cat="{cat}">
        <video src="video/{v}.mp4" poster="video/{v}.jpg" muted loop playsinline autoplay preload="none" aria-label="{cap}"></video>
        <span class="play-badge">▶ Video</span>
        <figcaption class="cap">{cap}</figcaption>
      </figure>""")
            continue
        out.append(f"""      <figure class="gallery-item {cls}" data-cat="{cat}">
        <img src="{img}" alt="{cap}" loading="lazy">
        <figcaption class="cap">{cap}</figcaption>
      </figure>""")
    return "\n".join(out)


# ---------------------------------------------------------------- INDEX
def index():
    p = "index.html"
    feats = [
        ("shield", "30 Yıllık Tecrübe", "Fransa'da 30 yıl villa yapımında edinilmiş saha tecrübesi ve Avrupa standartlarında işçilik."),
        ("layers", "Tek Elden Çözüm", "Hafriyattan betona kadar tüm kaba inşaat kendi ekibimizle; muhatabınız tek kişi."),
        ("ruler", "Ölçü ve Disiplin", "Kalıpta terazi, demirde paspayı, betonda vibrasyon — her detay kontrol altında."),
        ("handshake", "Şeffaf İletişim", "Net teklif, düzenli şantiye bilgilendirmesi ve söz verilen tarihte teslim."),
    ]
    feat_html = "\n".join(
        f"""      <div class="feature reveal"><div class="ico">{ICON[i]}</div><h3>{t}</h3><p>{d}</p></div>""" for i, t, d in feats
    )
    steps = [
        ("Keşif", "Arsa ve proje incelemesi, net teklif."),
        ("Hafriyat", "Temel kazısı ve zemin hazırlığı."),
        ("Temel", "Kalıp, demir ve beton ile sağlam temel."),
        ("Kaba İnşaat", "Kolon, kiriş, perde ve döşemeler."),
        ("Çatı", "Yapıyı çatıya kadar tamamlıyoruz."),
        ("Teslim", "Temiz şantiye, zamanında teslim."),
    ]
    steps_html = "\n".join(
        f"""      <div class="step reveal"><div class="dot">{n}</div><h3>{t}</h3><p>{d}</p></div>""" for n, (t, d) in enumerate(steps, 1)
    )
    return head("İnovYapıKalıp | Ali Kılıç — Villa Yapımı, Hafriyat, Kalıp, Demir, Beton · Kayseri",
                "İnovYapıKalıp - Ali Kılıç. Kayseri ve çevresinde villa yapımı, hafriyat, kalıp, demir ve beton işleri. Fransa'dan 30 yıllık villa yapım tecrübesiyle temelden çatıya güvenilir işçilik.", p) + header(p) + f"""
<section class="hero">
  <div class="hero-bg" style="background-image:url('images/beton_pompa_doseme_dokumu.jpg');"></div>
  <div class="wrap">
    <div>
      <span class="kicker">İnşaat Şirketi · Kayseri ve Çevresi</span>
      <h1>Temelden Çatıya<br><span class="gold-text">Güvenilir İşçilik</span></h1>
      <p class="lead">Fransa'dan 30 yıllık villa yapım tecrübesiyle; villa, hafriyat, kalıp, demir ve beton işlerinizi tek elden, sağlam ve zamanında teslim ediyoruz.</p>
      <div class="hero-actions">
        <a href="tel:{TEL}" class="btn btn-gold">{ICON['phone'].replace('<svg', '<svg class="icon"')} Hemen Ara</a>
        <a href="{WA}" class="btn btn-ghost" target="_blank" rel="noopener">{ICON['wa'].replace('<svg', '<svg class="icon"')} WhatsApp</a>
      </div>
      <div class="hero-meta">
        <div><strong>30 Yıl</strong>Fransa'da villa tecrübesi</div>
        <div><strong>5 Uzmanlık</strong>Villa · Hafriyat · Kalıp · Demir · Beton</div>
        <div><strong>Kayseri</strong>ve çevresi</div>
      </div>
    </div>
    <div class="hero-badge"><img src="images/logo.webp" alt="İnovYapıKalıp - Ali Kılıç logosu" width="380" height="386"></div>
  </div>
</section>

<div class="hazard"></div>

<section class="bg-black texture">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="kicker">Hizmetlerimiz</span>
      <h2>Villanızın Her Aşamasında <span class="gold-text">Yanınızdayız</span></h2>
      <p>Hafriyattan betona, kalıptan demire — kaba inşaatın tamamını kendi ekibimizle yapıyoruz.</p>
    </div>
    <div class="services-grid">
{service_cards()}
    </div>
  </div>
</section>

<section class="bg-paper">
  <div class="wrap split">
    <div class="photo reveal">
      <img src="images/beton_pompa_perde_dokumu.jpg" alt="Şantiyede pompa ile perde beton dökümü" loading="lazy">
      <img src="images/logo.webp" alt="" class="seal" loading="lazy">
    </div>
    <div class="reveal">
      <span class="fr-tr"><span class="flag flag-fr"><i></i><i></i><i></i></span> Fransa'dan Kayseri'ye <svg class="flag-tr" viewBox="0 0 1200 800" aria-label="Türkiye"><rect width="1200" height="800" fill="#E30A17"/><circle cx="425" cy="400" r="200" fill="#fff"/><circle cx="475" cy="400" r="160" fill="#E30A17"/><polygon fill="#fff" points="583.334,400 764.235,458.779 652.431,304.894 652.431,495.106 764.235,341.221"/></svg></span>
      <span class="kicker" style="display:table;">Ali Kılıç</span>
      <h2>30 Yıllık Avrupa Tecrübesi, <span style="color:var(--gold-dark)">Memleket Toprağında</span></h2>
      <p style="margin-top:1.2rem;">Ali Kılıç, Fransa'da 30 yıl boyunca villa yapımında çalıştı; temel, kalıp, demir ve beton işlerini Avrupa'nın titiz standartlarıyla öğrendi ve uyguladı.</p>
      <p>Bugün İnovYapıKalıp olarak bu tecrübeyi Kayseri ve çevresine taşıyoruz. Amacımız basit: sağlam, düzgün ve uzun ömürlü yapılar inşa etmek.</p>
      <a href="hakkimizda.html" class="btn btn-gold" style="margin-top:0.8rem;">Hikayemiz</a>
    </div>
  </div>
</section>

<section class="bg-coal">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="kicker">Çalışma Sürecimiz</span>
      <h2>Keşiften <span class="gold-text">Teslime</span></h2>
      <p>Villanız adım adım, planlı ve kontrollü şekilde yükselir.</p>
    </div>
    <div class="process">
{steps_html}
    </div>
  </div>
</section>

<section class="bg-black texture">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Neden İnovYapıKalıp?</span>
      <h2>İşini Bilen Bir <span class="gold-text">Usta</span></h2>
    </div>
    <div class="features">
{feat_html}
    </div>
  </div>
</section>

<section class="bg-graphite">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="kicker">Projelerimizden</span>
      <h2>Şantiyeden <span class="gold-text">Kareler</span></h2>
    </div>
    <div class="gallery-grid" data-gallery>
{gallery_items(HOME_GALLERY)}
    </div>
    <p style="text-align:center;margin-top:2.5rem;"><a href="galeri.html" class="btn btn-ghost">Tüm Projeleri Gör</a></p>
  </div>
</section>

<section class="bg-paper" style="text-align:center;">
  <div class="wrap reveal">
    <div class="section-head center">
      <span class="kicker">Hizmet Bölgemiz</span>
      <h2>Kayseri ve Çevresi</h2>
      <p>Merkez ilçeler ve çevre bölgelerde hizmet veriyoruz.</p>
    </div>
    <div class="region">
      <span class="main">Kayseri</span><span>Melikgazi</span><span>Kocasinan</span><span>Talas</span><span>Hacılar</span><span>İncesu</span><span>Develi</span><span>ve çevresi</span>
    </div>
  </div>
</section>
""" + cta_band() + footer()


# ---------------------------------------------------------------- HIZMETLER
def hizmetler():
    p = "hizmetler.html"
    rows = []
    for i, (slug, title, short, img, long, bullets) in enumerate(SERVICES, 1):
        bl = "\n".join(f"          <li>{b}</li>" for b in bullets)
        extra = '<span class="tag-mini">Ek hizmet</span><br>' if slug == "karot" else ""
        media = f'<img src="{img}" alt="{title}" loading="lazy">'
        rows.append(f"""    <div class="svc-row" id="{slug}">
      <div class="svc-media reveal">{media}<span class="big-num">{i:02d}</span></div>
      <div class="svc-text reveal">
        {extra}<span class="kicker">Hizmet {i:02d}</span>
        <h2>{title}</h2>
        <p>{long}</p>
        <ul class="check-list">
{bl}
        </ul>
        <div class="hero-actions" style="margin-top:1.6rem;">
          <a href="{WA}?text={('Merhaba, ' + title + ' hakkında bilgi almak istiyorum.').replace(' ', '%20')}" class="btn btn-gold" target="_blank" rel="noopener">Teklif Al</a>
        </div>
      </div>
    </div>""")
    return head("Hizmetlerimiz | İnovYapıKalıp — Villa, Hafriyat, Kalıp, Demir, Beton",
                "Villa yapımı, hafriyat, kalıp, betonarme demir, beton dökümü ve karot delme hizmetleri. Kayseri ve çevresinde İnovYapıKalıp - Ali Kılıç.", p) + header(p) + page_hero(
        "Hizmetlerimiz", 'Temelden Çatıya <span class="gold-text">Tüm Hizmetler</span>',
        "Villa yapımından hafriyata, kalıptan betona kadar yapınızın her aşamasında uzman ekibimizle yanınızdayız.",
        "images/kalip_perde_donati.jpg") + f"""
<section class="bg-black texture" style="padding-top:2rem;">
  <div class="wrap">
{chr(10).join(rows)}
  </div>
</section>
""" + cta_band("Hangi Hizmete İhtiyacınız Var?", "Projenizi anlatın, keşif ve teklif için size dönelim.") + footer()


# ---------------------------------------------------------------- GALERI
def galeri():
    p = "galeri.html"
    groups = [
        ("hafriyat", "Hafriyat & Kazı", "Keşif, aplikasyon ve temel kazısı: her yapı doğru hazırlanmış bir zeminle başlar."),
        ("temel", "Temel & Yalıtım", "Radye temel, temel tabanı hazırlığı ve yalıtım uygulamaları."),
        ("kalip", "Kalıp & Demir", "Perde, kolon ve döşeme kalıpları; statik projeye uygun donatı."),
        ("beton", "Beton Dökümü", "Pompa ile döşeme ve perde dökümleri, villa kaba inşaatı."),
        ("karot", "Karot", "Perde betona ve zemine profesyonel karot delme."),
        ("guclendirme", "Güçlendirme", "Kolon güçlendirme, epoksi filiz ekme ve çelik kolon bağlantıları."),
    ]
    btns = ['      <button data-filter="all" class="active">Tümü</button>'] + [
        f'      <button data-filter="{k}">{t}</button>' for k, t, _ in groups]
    secs = []
    for n, (k, t, d) in enumerate(groups, 1):
        items = [(img, cap, cat, "") for img, cap, cat, _ in GALLERY if cat == k]
        extra = (-len(items)) % 4  # fill complete rows of 4
        if extra == 3:
            items[0] = items[0][:3] + ("big",)
        else:
            for x in range(extra):
                items[x] = items[x][:3] + ("wide",)
        secs.append(f"""    <div class="project-group" data-cat="{k}">
      <div class="group-head">
        <span class="group-num">{n:02d}</span>
        <div>
          <h2>{t}</h2>
          <p>{d}</p>
        </div>
        <span class="group-count">{len(items)} görsel</span>
      </div>
      <div class="project-grid" data-gallery>
{gallery_items(items)}
      </div>
    </div>""")
    return head("Projeler | İnovYapıKalıp — Şantiyeden Kareler",
                "İnovYapıKalıp projelerinden fotoğraflar: hafriyat, temel, kalıp, demir, beton, karot ve güçlendirme uygulamaları.", p) + header(p) + page_hero(
        "Projeler", 'Şantiyeden <span class="gold-text">Kareler</span>',
        "Hafriyattan betona, güçlendirmeden karota — sahada yaptığımız işlerden görüntüler.",
        "images/villa_doseme_donati_hazir.jpg") + f"""
<section class="bg-black texture projects">
  <div class="wrap">
    <div class="filters">
{chr(10).join(btns)}
    </div>
{chr(10).join(secs)}
  </div>
</section>
""" + cta_band() + footer()


# ---------------------------------------------------------------- HAKKIMIZDA
def hakkimizda():
    p = "hakkimizda.html"
    princ = [
        ("ruler", "Önce Ölçü", "Her iş öncesi ölçüm ve kontrol. Betonda geri dönüş yok; hatayı baştan önlüyoruz."),
        ("shield", "Statik Projeye Sadakat", "Kalıp, demir ve betonda projeye birebir uyum; yapının güvenliği her şeyden önce gelir."),
        ("layers", "Temiz Şantiye", "Düzenli çalışma alanı, zamanında söküm ve temiz teslim."),
        ("handshake", "Söz Verilen Tarihte Teslim", "Net teklif, düzenli bilgilendirme ve verilen sözün tutulması."),
    ]
    ph = "\n".join(f"""      <div class="feature reveal"><div class="ico">{ICON[i]}</div><h3>{t}</h3><p>{d}</p></div>""" for i, t, d in princ)
    return head("Hakkımızda | İnovYapıKalıp — Ali Kılıç",
                "Ali Kılıç ve İnovYapıKalıp: Fransa'da 30 yıllık villa yapım tecrübesi, bugün Kayseri ve çevresinde temelden çatıya güvenilir işçilik.", p) + header(p) + page_hero(
        "Hakkımızda", 'Fransa\'dan Kayseri\'ye <span class="gold-text">30 Yıllık Tecrübe</span>',
        "İşini bilen bir usta arıyorsanız doğru yerdesiniz.",
        "images/villa_kaba_insaat_kalip.jpg") + f"""
<section class="bg-paper">
  <div class="wrap split">
    <div class="reveal">
      <span class="fr-tr"><span class="flag flag-fr"><i></i><i></i><i></i></span> Fransa → Kayseri <svg class="flag-tr" viewBox="0 0 1200 800" aria-label="Türkiye"><rect width="1200" height="800" fill="#E30A17"/><circle cx="425" cy="400" r="200" fill="#fff"/><circle cx="475" cy="400" r="160" fill="#E30A17"/><polygon fill="#fff" points="583.334,400 764.235,458.779 652.431,304.894 652.431,495.106 764.235,341.221"/></svg></span>
      <span class="kicker" style="display:table;">Hikayemiz</span>
      <h2>Ali Kılıç</h2>
      <p style="margin-top:1.2rem;">Ali Kılıç, inşaat hayatının 30 yılını Fransa'da villa yapımında geçirdi. Hafriyattan temele, kalıptan demir ve betona kadar bir villanın her aşamasında bizzat çalıştı; Avrupa'nın disiplinli şantiye kültürünü ve kalite standartlarını yakından öğrendi.</p>
      <p>Bu birikimi memleketine taşımak için İnovYapıKalıp'ı kurdu. Bugün Kayseri ve çevresinde villa yapımı, hafriyat, kalıp, demir ve beton işlerini aynı titizlikle yürütüyor.</p>
      <p>Mevcut yapılar için ise karot delme ve epoksi filiz ekme ile güçlendirme hizmeti de veriyoruz.</p>
      <div class="sign">— Ali Kılıç</div>
    </div>
    <div class="photo reveal">
      <img src="images/beton_perde_kalip_santiye.jpg" alt="Villa şantiyesinde kalıp ve beton dökümü" loading="lazy">
      <img src="images/logo.webp" alt="" class="seal" loading="lazy">
    </div>
  </div>
</section>

<section class="bg-black texture">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="kicker">İlkelerimiz</span>
      <h2>Nasıl <span class="gold-text">Çalışırız</span></h2>
    </div>
    <div class="features">
{ph}
    </div>
  </div>
</section>
""" + cta_band("Projenizi Birlikte Değerlendirelim", "Bir telefon kadar yakınız.") + footer()


# ---------------------------------------------------------------- ILETISIM
def iletisim():
    p = "iletisim.html"
    opts = "\n".join(f'            <option value="{s[1]}">{s[1]}</option>' for s in SERVICES)
    return head("İletişim | İnovYapıKalıp — Ali Kılıç · 0531 354 79 12",
                "İnovYapıKalıp ile iletişime geçin. Ali Kılıç: 0531 354 79 12. Kayseri ve çevresinde villa, hafriyat, kalıp, demir ve beton işleri için keşif ve teklif.", p) + header(p) + page_hero(
        "İletişim", 'Bir Telefon Kadar <span class="gold-text">Yakınız</span>',
        "Keşif ve teklif için arayın, WhatsApp'tan yazın ya da formu doldurun.",
        "images/villa_doseme_donati_kolon_filiz.jpg") + f"""
<section class="bg-black texture">
  <div class="wrap contact-grid">
    <div class="info-card reveal">
      <span class="kicker">Doğrudan Ulaşın</span>
      <h2 style="margin-bottom:1.2rem;">İletişim Bilgileri</h2>
      <ul class="info-list">
        <li><span class="ico">{ICON['user']}</span><div><small>Yetkili</small><strong>Ali Kılıç</strong></div></li>
        <li><span class="ico">{ICON['phone']}</span><div><small>Telefon</small><a href="tel:{TEL}">{TEL_TXT}</a></div></li>
        <li><span class="ico">{ICON['wa']}</span><div><small>WhatsApp</small><a href="{WA}" target="_blank" rel="noopener">Mesaj gönderin</a></div></li>
        <li><span class="ico">{ICON['ig']}</span><div><small>Instagram</small><a href="{IG}" target="_blank" rel="noopener">@inovyapikalip</a></div></li>
        <li><span class="ico">{ICON['pin']}</span><div><small>Bölge</small><strong>Kayseri ve çevresi</strong></div></li>
      </ul>
      <div class="hero-actions" style="margin-top:1.6rem;">
        <a href="tel:{TEL}" class="btn btn-gold">Hemen Ara</a>
        <a href="{WA}" class="btn btn-wa" target="_blank" rel="noopener">WhatsApp</a>
      </div>
    </div>
    <div class="form-box reveal">
      <h3>Hızlı Teklif Formu</h3>
      <p>Formu doldurun, mesajınız WhatsApp üzerinden Ali Kılıç'a iletilsin.</p>
      <form id="contactForm">
        <input type="text" id="name" placeholder="Adınız Soyadınız" required class="form-control">
        <input type="tel" id="phone" placeholder="Telefon Numaranız" required class="form-control">
        <select id="service" required class="form-control">
          <option value="">Hizmet Seçiniz</option>
{opts}
          <option value="Diğer">Diğer</option>
        </select>
        <input type="text" id="place" placeholder="Proje yeri (ilçe / mahalle)" class="form-control">
        <textarea id="message" placeholder="Projenizden kısaca bahsedin (isteğe bağlı)" rows="4" class="form-control"></textarea>
        <button type="submit" class="btn btn-gold">{ICON['wa'].replace('<svg', '<svg class="icon"')} WhatsApp'ta Gönder</button>
      </form>
    </div>
  </div>
</section>
""" + footer()


for name, fn in [("index.html", index), ("hizmetler.html", hizmetler), ("galeri.html", galeri), ("hakkimizda.html", hakkimizda), ("iletisim.html", iletisim)]:
    (OUT / name).write_text(fn(), encoding="utf-8")
    print("wrote", name)
