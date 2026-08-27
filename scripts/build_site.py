#!/usr/bin/env python3
"""Generate docs/index.html — the browsable atlas — from data/cases.csv.

Deterministic: same input always produces byte-identical output, so CI can assert
the committed page is current with `git diff --exit-code docs/index.html`.

    python3 scripts/build_site.py                 # write docs/index.html
    python3 scripts/build_site.py --fragment X    # also write a headless copy to X

The fragment form drops <!doctype>/<html>/<head>/<body> for hosts that supply
their own document skeleton.
"""
import argparse
import csv
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "data" / "cases.csv"
OUT = ROOT / "docs" / "index.html"

REPO = "https://github.com/paradoksix/ai-money-workflows"
BLOB = f"{REPO}/blob/main"

# Display order and copy for each niche. Order matches the nis-NN- file prefix.
NICHES = [
    ("video-gorsel-produksiyon", 1, "Video & görsel prodüksiyon",
     "Reklam, ürün videosu, müzik videosu ve thumbnail üretimi. Talep gerçek, rekabet yüksek."),
    ("b2b-satis-lead", 2, "B2B satış & lead araştırma",
     "Hedef şirketi bul, karar vericiyi çıkar, satışçıya temiz not bırak. En iyi kaynak-doğrulanmış niş."),
    ("musteri-iletisim-destek", 3, "Müşteri iletişimi & destek",
     "Gelen mesajı karşıla, sınıflandır, eksik bilgiyi tamamla, gerekince insana devret."),
    ("ozel-yazilim-mikro-saas", 4, "Özel yazılım & mikro-SaaS",
     "Workflow değil uygulama satılan vakalar. Satış kanalı reklam değil, mevcut ilişki."),
    ("icerik-sosyal-medya", 5, "İçerik, sosyal medya & bülten",
     "Uzun içeriği parçala, bülten üret, kanal prodüksiyonu yap."),
    ("eticaret-katalog", 6, "E-ticaret & katalog",
     "Ürün verisi, katalog kalitesi, stok akışı. Türkiye için en güçlü nişlerden."),
    ("kurumsal-operasyon-maliyet", 7, "Kurumsal operasyon & maliyet",
     "Çoğunda AI ürünü satılmıyor; lisans, insan zamanı veya operasyon kaybı azaltılıyor."),
    ("ofis-belge-operasyonu", 8, "Ofis & belge operasyonu",
     "Form, e-posta ve tablo trafiğini yapılandırmak. Burada AI çoğu zaman şart değil."),
    ("veri-cikti-temizligi", 9, "Veri & AI-çıktısı temizliği",
     "AI'nın bıraktığı yarım işi güvenilir son ürüne çevirmek."),
    ("ajans-freelance-model", 10, "Ajans & freelance hizmet modeli",
     "Ne satıldığını değil, nasıl satıldığını anlatan vakalar: fiyat, scope, retainer."),
    ("yerel-isletme-saha-servisi", 11, "Yerel işletme & saha servisi",
     "Mahalledeki işletmeye yüz yüze satılabilen sistemler. Ansiklopedinin en güçlü tek vakası burada."),
    ("rag-bilgi-sistemleri", 12, "RAG & özel bilgi sistemleri",
     "Müşterinin kendi belgelerinden kaynaklı cevap. Satış argümanı zekâ değil, gizlilik."),
    ("emlak-site-yonetimi", 13, "Emlak & site yönetimi",
     "Kiracı talebi, bakım koordinasyonu, belge üretimi ve lead takibi."),
    ("muhasebe-finans-belge", 14, "Muhasebe & finans belgeleri",
     "Fatura, tahsilat, ön-muhasebe. Değişmez kural: LLM rakam hesabı yapmasın."),
    ("ik-ise-alim", 15, "İK & işe alım",
     "AI'nın alanı araştırma ve admin; insanın alanı değerlendirme ve karar."),
    ("egitim-kurs-operasyonu", 16, "Eğitim & kurs operasyonu",
     "Ders programı, veli iletişimi, ödeme takibi, öğrenci verisi normalizasyonu."),
    ("tartismali", 17, "Tartışmalı (X seviyesi)",
     "Satın alınacak iş değil; kırmızı bayrak eğitimi olarak saklanan örnek."),
]

GRADES = [
    ("A", "Ticari vaka + exact kaynak",
     "Belirli müşteri/gelir vakası ile doğrudan bağlantılı kaynak kod doğrulandı."),
    ("B", "Açık kaynak, gelir kanıtı eksik",
     "Kod gerçek ve çalışıyor; bu workflow'un ayrı ücretli müşteri sonucu kanıtlanmadı."),
    ("C", "Güçlü ticari sinyal, kaynak yok",
     "Ücretli müşteri, gelir veya tasarruf sinyali güçlü; exact kaynak repo bulunamadı."),
    ("X", "Tartışmalı",
     "Gelir iddiasında promosyon veya çıkar çatışması var. Ana sayıma dahil değil."),
]

REVENUE = [
    ("F", "Freelancer ücreti", "Hizmet sağlayıcının aldığı para."),
    ("R", "Ürün/SaaS geliri", "Üründen doğan tekrarlı veya doğrudan gelir."),
    ("S", "Müşteri tasarrufu", "Müşterinin kazandığı zaman veya kestiği gider."),
    ("V", "Ticari değer", "Kampanya değeri, booked call, impression, geri kazanılan alacak."),
]

SELLABILITY = [("high", "Yüksek"), ("medium", "Orta"), ("low", "Düşük")]
TR_LABEL = dict(SELLABILITY)

GRADE_ORDER = {"A": 0, "B": 1, "C": 2, "X": 3}


def e(text):
    return html.escape(str(text), quote=True)


def load():
    with CASES.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    rows.sort(key=lambda r: (GRADE_ORDER[r["evidence_grade"]], int(r["id"][1:])))
    return rows


# ── CSS ─────────────────────────────────────────────────────────────────────
CSS = """
*,*::before,*::after{box-sizing:border-box}

:root{
  --paper:#F7F8FA; --surface:#FFFFFF; --ink:#16191F; --muted:#5A6472;
  --rule:#DDE1E8; --rule-soft:#EAEDF2; --accent:#3B4E8C; --accent-soft:#EDF0F8;
  --gA-text:#0A5C3E; --gA-fill:#0E7A52; --gA-wash:#E4F1EA;
  --gB-text:#7D5906; --gB-fill:#CE9412; --gB-wash:#F8EFDC;
  --gC-text:#5C544E; --gC-fill:#8C8078; --gC-wash:#EDEBE9;
  --gX-text:#932A1D; --gX-fill:#C03B2B; --gX-wash:#F7E5E2;
  --shadow:0 1px 2px rgba(22,25,31,.05),0 1px 1px rgba(22,25,31,.04);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --paper:#101318; --surface:#171B22; --ink:#E6E9EF; --muted:#99A2B0;
    --rule:#262C36; --rule-soft:#1E232B; --accent:#8FA3DE; --accent-soft:#1B2130;
    --gA-text:#4FBF8B; --gA-fill:#2E9E69; --gA-wash:#12291F;
    --gB-text:#E0A93C; --gB-fill:#C8901F; --gB-wash:#2C2312;
    --gC-text:#A9A099; --gC-fill:#8C8078; --gC-wash:#232120;
    --gX-text:#E8705E; --gX-fill:#C6503E; --gX-wash:#2E1815;
    --shadow:0 1px 2px rgba(0,0,0,.30),0 1px 1px rgba(0,0,0,.22);
  }
}
:root[data-theme="dark"]{
  --paper:#101318; --surface:#171B22; --ink:#E6E9EF; --muted:#99A2B0;
  --rule:#262C36; --rule-soft:#1E232B; --accent:#8FA3DE; --accent-soft:#1B2130;
  --gA-text:#4FBF8B; --gA-fill:#2E9E69; --gA-wash:#12291F;
  --gB-text:#E0A93C; --gB-fill:#C8901F; --gB-wash:#2C2312;
  --gC-text:#A9A099; --gC-fill:#8C8078; --gC-wash:#232120;
  --gX-text:#E8705E; --gX-fill:#C6503E; --gX-wash:#2E1815;
  --shadow:0 1px 2px rgba(0,0,0,.30),0 1px 1px rgba(0,0,0,.22);
}

html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:"IBM Plex Sans","Segoe UI",system-ui,-apple-system,sans-serif;
  font-size:16px; line-height:1.6;
  -webkit-font-smoothing:antialiased;
}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
h1,h2,h3{font-family:Newsreader,Georgia,"Times New Roman",serif;font-weight:600;text-wrap:balance;margin:0}
a{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:3px}
.mono{font-family:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;font-variant-numeric:tabular-nums}

/* ── masthead ── */
.masthead{border-bottom:1px solid var(--rule);background:var(--surface)}
.masthead .wrap{padding-top:44px;padding-bottom:36px}
.eyebrow{
  font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11px;
  letter-spacing:.14em; text-transform:uppercase; color:var(--muted); margin:0 0 14px
}
h1{font-size:clamp(2rem,1.3rem + 3vw,3.1rem);line-height:1.1;letter-spacing:-.015em}
.standfirst{margin:16px 0 0;max-width:62ch;color:var(--muted);font-size:1.0625rem}
.standfirst strong{color:var(--ink);font-weight:600}

/* ── evidence legend ── */
.legend{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1px;
  background:var(--rule);border:1px solid var(--rule);border-radius:6px;overflow:hidden;margin-top:30px}
.legend div{background:var(--surface);padding:14px 16px}
.legend dt{display:flex;align-items:center;gap:8px;font-weight:600;font-size:.875rem;margin:0 0 4px}
.legend dd{margin:0;font-size:.8125rem;color:var(--muted);line-height:1.5}

/* grade chip: letter always present, so color never carries meaning alone */
.chip{
  display:inline-flex;align-items:center;justify-content:center;
  min-width:22px;height:22px;padding:0 6px;border-radius:4px;
  font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:12px;font-weight:600;
  border:1px solid currentColor;flex:none
}
.g-A{color:var(--gA-text);background:var(--gA-wash)}
.g-B{color:var(--gB-text);background:var(--gB-wash)}
.g-C{color:var(--gC-text);background:var(--gC-wash)}
.g-X{color:var(--gX-text);background:var(--gX-wash)}

/* ── distribution meter ── */
.meter-block{margin-top:34px}
.meter-head{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;margin-bottom:10px}
.meter-total{font-family:Newsreader,Georgia,serif;font-size:2.25rem;line-height:1;font-weight:600}
.meter-total span{font-size:.9375rem;font-family:"IBM Plex Sans",sans-serif;color:var(--muted);margin-left:8px;font-weight:400}
.meter{display:flex;gap:2px;height:34px;border-radius:4px;overflow:hidden}
.meter i{
  display:flex;align-items:center;justify-content:center;font-style:normal;
  font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:11px;font-weight:600;
  color:#fff;min-width:2px;transition:filter .15s
}
.meter i:hover{filter:brightness(1.12)}
.s-A{background:var(--gA-fill)} .s-B{background:var(--gB-fill)}
.s-C{background:var(--gC-fill)} .s-X{background:var(--gX-fill)}
.meter-key{display:flex;gap:18px;flex-wrap:wrap;margin-top:10px;font-size:.8125rem;color:var(--muted)}
.meter-key span{display:flex;align-items:center;gap:6px}
.dot{width:9px;height:9px;border-radius:2px;flex:none}

/* ── section headers ── */
.section{padding-top:52px}
.section > h2{font-size:1.5rem;letter-spacing:-.01em}
.section > p.lede{margin:8px 0 0;color:var(--muted);max-width:64ch;font-size:.9375rem}

/* ── niche grid ── */
.niches{display:grid;grid-template-columns:repeat(auto-fill,minmax(258px,1fr));gap:12px;margin-top:22px}
.niche{
  display:flex;flex-direction:column;gap:8px;text-align:left;cursor:pointer;
  background:var(--surface);border:1px solid var(--rule);border-radius:7px;
  padding:16px;font:inherit;color:inherit;box-shadow:var(--shadow);
  transition:border-color .15s,transform .15s
}
.niche:hover{border-color:var(--accent);transform:translateY(-1px)}
.niche[aria-pressed="true"]{border-color:var(--accent);background:var(--accent-soft)}
.niche-top{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
.niche-name{font-weight:600;font-size:.9375rem;line-height:1.3}
.niche-n{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.8125rem;color:var(--muted);flex:none}
.niche-desc{font-size:.8125rem;color:var(--muted);line-height:1.5;margin:0}
.niche-bar{display:flex;gap:2px;height:4px;border-radius:2px;overflow:hidden;margin-top:auto}

/* ── filters ── */
.filters{
  position:sticky;top:0;z-index:20;background:var(--paper);
  border-bottom:1px solid var(--rule);padding:14px 0;margin-top:26px
}
.filter-row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.search{
  flex:1 1 260px;min-width:200px;padding:9px 12px;font:inherit;font-size:.9375rem;
  background:var(--surface);color:var(--ink);
  border:1px solid var(--rule);border-radius:6px
}
.search::placeholder{color:var(--muted)}
select{
  padding:9px 10px;font:inherit;font-size:.875rem;background:var(--surface);color:var(--ink);
  border:1px solid var(--rule);border-radius:6px;cursor:pointer
}
.btn{
  padding:9px 13px;font:inherit;font-size:.875rem;background:var(--surface);color:var(--muted);
  border:1px solid var(--rule);border-radius:6px;cursor:pointer
}
.btn:hover{color:var(--ink);border-color:var(--accent)}
.count{font-size:.8125rem;color:var(--muted);margin-top:9px}
.count b{color:var(--ink);font-weight:600}

/* ── case rows ── */
.group{margin-top:38px}
.group > h3{
  font-size:1.0625rem;padding-bottom:8px;border-bottom:2px solid var(--ink);
  display:flex;justify-content:space-between;align-items:baseline;gap:12px
}
.group > h3 em{font-style:normal;font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:.75rem;color:var(--muted);font-weight:400;flex:none}
.case{display:grid;grid-template-columns:auto 1fr;gap:6px 14px;
  padding:16px 0;border-bottom:1px solid var(--rule-soft)}
.case-id{display:flex;flex-direction:column;align-items:center;gap:6px;width:52px}
.case-id .mono{font-size:.75rem;color:var(--muted)}
.case-title{font-weight:600;font-size:1rem;line-height:1.35;margin:0}
.case-sum{margin:6px 0 0;font-size:.9062rem;color:var(--muted);max-width:72ch}
.case-meta{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.tag{
  font-size:.75rem;padding:2px 8px;border-radius:4px;
  background:var(--rule-soft);color:var(--muted);border:1px solid var(--rule)
}
.tag.money{color:var(--ink);font-family:"IBM Plex Mono",ui-monospace,monospace;font-weight:600;
  background:var(--accent-soft);border-color:var(--accent)}
.case-links{display:flex;flex-wrap:wrap;gap:14px;margin-top:10px;font-size:.8125rem}
.case-links a{text-decoration:none;border-bottom:1px solid transparent}
.case-links a:hover{border-bottom-color:currentColor}
.empty{padding:46px 0;text-align:center;color:var(--muted)}

/* ── footer ── */
footer{margin-top:64px;border-top:1px solid var(--rule);background:var(--surface)}
footer .wrap{padding-top:30px;padding-bottom:44px}
footer h2{font-size:1.125rem;margin-bottom:10px}
footer p{color:var(--muted);font-size:.875rem;max-width:70ch;margin:0 0 12px}
.foot-links{display:flex;flex-wrap:wrap;gap:8px 20px;font-size:.875rem;margin-top:16px}
.disclaimer{
  margin-top:22px;padding:14px 16px;border-left:3px solid var(--gB-fill);
  background:var(--gB-wash);border-radius:0 5px 5px 0;font-size:.875rem;color:var(--ink)
}
.theme-toggle{
  position:fixed;right:18px;bottom:18px;z-index:30;width:42px;height:42px;border-radius:50%;
  background:var(--surface);color:var(--ink);border:1px solid var(--rule);
  cursor:pointer;font-size:16px;box-shadow:var(--shadow);line-height:1
}

@media (max-width:640px){
  .wrap{padding:0 16px}
  .case{grid-template-columns:1fr}
  .case-id{flex-direction:row;width:auto}
  .meter i{font-size:0}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
"""


def build_body(rows):
    total = len(rows)
    disputed = sum(1 for r in rows if r["evidence_grade"] == "X")
    superseded = sum(1 for r in rows if r["status"].startswith("superseded"))
    catalogable = total - disputed - superseded
    counts = {g: sum(1 for r in rows if r["evidence_grade"] == g) for g, _, _ in GRADES}
    by_niche = {}
    for r in rows:
        by_niche.setdefault(r["niche"], []).append(r)

    o = []
    a = o.append

    # ── masthead ──
    a('<header class="masthead"><div class="wrap">')
    a('<p class="eyebrow">Kanıt dereceli araştırma atlası · 2026</p>')
    a("<h1>AI Gelir Vakaları Ansiklopedisi</h1>")
    a('<p class="standfirst">İnsanların ve işletmelerin yapay zekâ ile hangi küçük problemlere '
      f'<strong>gerçekten para ödediğini</strong> izleyen {catalogable} vakalık araştırma. Her vaka '
      'kanıt derecesine göre ayrılır: neyin kaynak koduyla doğrulandığı, neyin yalnızca '
      'self-report olduğu karıştırılmaz.</p>')

    a('<dl class="legend">')
    for g, title, desc in GRADES:
        a(f'<div><dt><span class="chip g-{g}">{g}</span> {e(title)}</dt>'
          f"<dd>{e(desc)}</dd></div>")
    a("</dl>")

    # ── distribution meter (status scale: every segment directly labelled) ──
    a('<div class="meter-block">')
    a('<div class="meter-head">')
    a(f'<span class="meter-total">{catalogable}<span>kataloglanabilir vaka · ayrıca {disputed} tartışmalı '
      f"ve {superseded} tarihsel kayıt (A006'ya taşındı) · toplam {total} kayıt</span></span>")
    a("</div>")
    a('<div class="meter" role="img" aria-label="'
      + e(", ".join(f"{g} derecesi {counts[g]} vaka" for g, _, _ in GRADES)) + '">')
    for g, title, _ in GRADES:
        pct = counts[g] / total * 100
        label = f"{g} · {counts[g]}" if pct > 7 else (g if pct > 2.5 else "")
        a(f'<i class="s-{g}" style="width:{pct:.4f}%" title="{e(title)}: {counts[g]} vaka">{label}</i>')
    a("</div>")
    a('<div class="meter-key">')
    for g, title, _ in GRADES:
        a(f'<span><i class="dot s-{g}"></i> <b class="mono">{g}</b> {e(title)} — {counts[g]}</span>')
    a("</div></div>")
    a("</div></header>")

    a('<main class="wrap">')

    # ── niche grid ──
    a('<section class="section" id="nisler">')
    a("<h2>Bir niş seçin</h2>")
    a('<p class="lede">Vakalar sektöre ve satılan işe göre gruplanmıştır. Bir kart seçtiğinizde '
      "aşağıdaki liste yalnızca o nişi gösterir; kartın kendi dosyasında ise her vakanın tam "
      "anlatımı, riskleri ve Türkiye uyarlaması bulunur.</p>")
    a('<div class="niches">')
    for slug, order, name, desc in NICHES:
        group = by_niche.get(slug, [])
        if not group:
            continue
        a(f'<button class="niche" type="button" data-niche="{e(slug)}" aria-pressed="false">')
        a('<span class="niche-top">'
          f'<span class="niche-name">{e(name)}</span>'
          f'<span class="niche-n">{len(group)}</span></span>')
        a(f'<span class="niche-desc">{e(desc)}</span>')
        a('<span class="niche-bar">')
        for g, _, _ in GRADES:
            n = sum(1 for r in group if r["evidence_grade"] == g)
            if n:
                a(f'<i class="s-{g}" style="flex:{n}"></i>')
        a("</span></button>")
    a("</div></section>")

    # ── filters ──
    a('<section class="section" id="vakalar"><h2>Vakalar</h2>')
    a('<div class="filters"><div class="filter-row">')
    a('<input class="search" id="q" type="search" placeholder="Ara: başlık, stack, sektör, özet…" '
      'aria-label="Vakalarda ara">')
    a('<select id="f-niche" aria-label="Niş"><option value="">Tüm nişler</option>')
    for slug, order, name, _ in NICHES:
        if by_niche.get(slug):
            a(f'<option value="{e(slug)}">{e(name)}</option>')
    a("</select>")
    a('<select id="f-grade" aria-label="Kanıt derecesi"><option value="">Tüm kanıt dereceleri</option>')
    for g, title, _ in GRADES:
        a(f'<option value="{g}">{g} — {e(title)}</option>')
    a("</select>")
    a('<select id="f-rev" aria-label="Gelir tipi"><option value="">Tüm gelir tipleri</option>')
    for code, name, _ in REVENUE:
        a(f'<option value="{code}">{code} — {e(name)}</option>')
    a("</select>")
    a('<select id="f-tr" aria-label="Türkiye uygunluğu"><option value="">TR uygunluğu: hepsi</option>')
    for val, name in SELLABILITY:
        a(f'<option value="{e(val)}">TR uygunluğu: {e(name)}</option>')
    a("</select>")
    a('<button class="btn" type="button" id="reset">Sıfırla</button>')
    a("</div>")
    a('<p class="count" id="count"></p>')
    a("</div>")
    a('<div id="results"></div>')
    a("</section>")
    a("</main>")

    # ── footer ──
    a("<footer><div class=\"wrap\">")
    a("<h2>Yöntem ve sınırlar</h2>")
    a("<p>Bu atlas bir gelir vaadi değil, bir araştırma kaydıdır. Tek bir ekran görüntüsü kanıt "
      "sayılmaz; tercih sırası belirli müşteri problemi, çalışan sistem açıklaması, ticari sonuç, "
      "exact kaynak kod, repo geçmişi ve lisanstır.</p>")
    a('<div class="disclaimer"><strong>Rakamlar hakkında.</strong> Sayfadaki tutarların neredeyse '
      "tamamı kaynak kişilerin kendi beyanıdır (self-report) ve bağımsız denetlenmemiştir. "
      "Freelancer ücreti, ürün geliri, müşteri tasarrufu ve ticari değer birbirine karıştırılmaz — "
      "her vakada F/R/S/V etiketiyle ayrılır. Public bir GitHub reposu, yeniden dağıtım veya "
      "yeniden lisanslama izni vermez.</div>")
    a('<div class="foot-links">')
    for label, href in [
        ("Depo", REPO),
        ("Niş indeksi", f"{BLOB}/ENCYCLOPEDIA.md"),
        ("Kesişen desenler", f"{BLOB}/encyclopedia/DESENLER.md"),
        ("Kanıt standardı", f"{BLOB}/RESEARCH_POLICY.md"),
        ("Ham veri (cases.csv)", f"{BLOB}/data/cases.csv"),
        ("Araştırma kuyruğu", f"{BLOB}/research_queue.csv"),
    ]:
        a(f'<a href="{e(href)}">{e(label)}</a>')
    a("</div></div></footer>")
    a('<button class="theme-toggle" id="theme" type="button" aria-label="Temayı değiştir">◐</button>')
    return "\n".join(o)


JS = """
const NICHE_NAMES = __NICHES__;
const CASES = __CASES__;
const GRADE_TITLE = __GRADETITLE__;
const REV_TITLE = __REVTITLE__;
const TR_LABEL = __TRLABEL__;
const BLOB = "__BLOB__";

const $ = id => document.getElementById(id);
const state = {q:"", niche:"", grade:"", rev:"", tr:""};

function esc(s){
  return String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
}

function matches(c){
  if(state.niche && c.niche !== state.niche) return false;
  if(state.grade && c.grade !== state.grade) return false;
  if(state.rev && c.rev !== state.rev) return false;
  if(state.tr && c.tr !== state.tr) return false;
  if(state.q && !c.hay.includes(state.q)) return false;
  return true;
}

function caseHTML(c){
  const tags = [];
  if(c.amount) tags.push(`<span class="tag money" title="${esc(REV_TITLE[c.rev]||"Bildirilen sonuç")}">${esc(c.amount)}</span>`);
  else if(c.result) tags.push(`<span class="tag">${esc(c.result)}</span>`);
  if(c.work) tags.push(`<span class="tag">${esc(c.work)}</span>`);
  if(c.stack) tags.push(`<span class="tag">${esc(c.stack)}</span>`);
  tags.push(`<span class="tag" title="Türkiye'de satılabilirlik — kaba araştırma önceliği">TR: ${esc(TR_LABEL[c.tr]||c.tr)}</span>`);

  const links = [`<a href="${esc(BLOB + "/" + c.file)}">Tam anlatım →</a>`];
  if(c.source) links.push(`<a href="${esc(c.source)}">Kaynak vaka</a>`);
  if(c.repo) links.push(`<a href="${esc(c.repo)}">Kaynak kod${c.commit ? " @" + esc(c.commit.slice(0,7)) : ""}</a>`);

  return `<article class="case">
    <div class="case-id">
      <span class="chip g-${c.grade}" title="${esc(GRADE_TITLE[c.grade])}">${c.grade}</span>
      <span class="mono">${esc(c.id)}</span>
    </div>
    <div>
      <h4 class="case-title">${esc(c.title)}</h4>
      <p class="case-sum">${esc(c.summary)}</p>
      <div class="case-meta">${tags.join("")}</div>
      <div class="case-links">${links.join("")}</div>
    </div>
  </article>`;
}

function render(){
  const hits = CASES.filter(matches);
  $("count").innerHTML = hits.length === CASES.length
    ? `<b>${CASES.length}</b> vakanın tamamı gösteriliyor.`
    : `<b>${hits.length}</b> vaka eşleşti · ${CASES.length} vaka arasından.`;

  if(!hits.length){
    $("results").innerHTML = `<p class="empty">Bu filtrelerle eşleşen vaka yok. Filtreleri gevşetmeyi deneyin.</p>`;
    return;
  }
  const groups = new Map();
  for(const c of hits){
    if(!groups.has(c.niche)) groups.set(c.niche, []);
    groups.get(c.niche).push(c);
  }
  let out = "";
  for(const [slug, name] of NICHE_NAMES){
    const g = groups.get(slug);
    if(!g) continue;
    out += `<section class="group"><h3>${esc(name)}<em>${g.length} vaka</em></h3>${g.map(caseHTML).join("")}</section>`;
  }
  $("results").innerHTML = out;

  document.querySelectorAll(".niche").forEach(b => {
    b.setAttribute("aria-pressed", String(b.dataset.niche === state.niche));
  });
}

$("q").addEventListener("input", ev => { state.q = ev.target.value.toLowerCase().trim(); render(); });
$("f-niche").addEventListener("change", ev => { state.niche = ev.target.value; render(); });
$("f-grade").addEventListener("change", ev => { state.grade = ev.target.value; render(); });
$("f-rev").addEventListener("change", ev => { state.rev = ev.target.value; render(); });
$("f-tr").addEventListener("change", ev => { state.tr = ev.target.value; render(); });
$("reset").addEventListener("click", () => {
  Object.assign(state, {q:"", niche:"", grade:"", rev:"", tr:""});
  $("q").value = ""; $("f-niche").value = ""; $("f-grade").value = "";
  $("f-rev").value = ""; $("f-tr").value = "";
  render();
});

document.querySelectorAll(".niche").forEach(btn => {
  btn.addEventListener("click", () => {
    state.niche = state.niche === btn.dataset.niche ? "" : btn.dataset.niche;
    $("f-niche").value = state.niche;
    render();
    document.getElementById("vakalar").scrollIntoView({behavior:"smooth", block:"start"});
  });
});

// theme toggle: remembers the viewer's choice, tolerates blocked storage
const root = document.documentElement;
try{
  const saved = localStorage.getItem("atlas-theme");
  if(saved) root.setAttribute("data-theme", saved);
}catch(_){}
$("theme").addEventListener("click", () => {
  const dark = getComputedStyle(root).getPropertyValue("--paper").trim().toLowerCase() === "#101318";
  const next = dark ? "light" : "dark";
  root.setAttribute("data-theme", next);
  try{ localStorage.setItem("atlas-theme", next); }catch(_){}
});

render();
"""


def build_js(rows):
    payload = []
    for r in rows:
        hay = " ".join([
            r["id"], r["title"], r["summary"], r["stack"], r["work_model"],
            r["client_type"], r["reported_amount"], r["reported_result"],
        ]).lower()
        payload.append({
            "id": r["id"], "title": r["title"], "niche": r["niche"],
            "grade": r["evidence_grade"], "rev": r["revenue_type"],
            "amount": r["reported_amount"], "result": r["reported_result"],
            "work": r["work_model"], "stack": r["stack"],
            "tr": r["tr_sellability"], "summary": r["summary"],
            "source": r["source_url"], "repo": r["repo_url"],
            "commit": r["pinned_commit"], "file": r["detail_file"],
            "hay": hay,
        })
    niche_names = [[slug, name] for slug, _, name, _ in NICHES]
    js = JS
    js = js.replace("__NICHES__", json.dumps(niche_names, ensure_ascii=False))
    js = js.replace("__CASES__", json.dumps(payload, ensure_ascii=False, separators=(",", ":")))
    js = js.replace("__GRADETITLE__", json.dumps({g: t for g, t, _ in GRADES}, ensure_ascii=False))
    js = js.replace("__REVTITLE__", json.dumps({c: n for c, n, _ in REVENUE}, ensure_ascii=False))
    js = js.replace("__TRLABEL__", json.dumps(TR_LABEL, ensure_ascii=False))
    js = js.replace("__BLOB__", BLOB)
    return js.replace("</script", "<\\/script")


HEAD = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Gelir Vakaları Ansiklopedisi</title>
<meta name="description" content="Kanıt dereceli 122 AI gelir vakası: neyin kaynak koduyla doğrulandığı, neyin yalnızca self-report olduğu ayrılmış hâlde.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;600&display=swap">
<style>__CSS__</style>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fragment", type=Path, help="also write a headless copy here")
    args = ap.parse_args()

    rows = load()
    head = HEAD.replace("__CSS__", CSS.strip())
    body = build_body(rows)
    script = f"<script>\n{build_js(rows).strip()}\n</script>"

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(
        f'<!doctype html>\n<html lang="tr">\n<head>\n{head}\n</head>\n<body>\n{body}\n{script}\n</body>\n</html>\n',
        encoding="utf-8",
    )
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size:,} bytes, {len(rows)} cases)")

    if args.fragment:
        args.fragment.parent.mkdir(parents=True, exist_ok=True)
        args.fragment.write_text(f"{head}\n{body}\n{script}\n", encoding="utf-8")
        print(f"wrote {args.fragment} (fragment)")


if __name__ == "__main__":
    main()
