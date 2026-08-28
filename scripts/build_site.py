#!/usr/bin/env python3
"""Generate the docs/ wiki from data/cases.csv and the encyclopedia markdown.

Every page under docs/ is written by this script. Nothing there is edited by
hand. Output is deterministic — the same inputs always produce byte-identical
files, so CI can assert freshness with `git diff --exit-code docs`.

    python3 scripts/build_site.py                 # write the whole wiki
    python3 scripts/build_site.py --fragment X    # also write a headless copy
                                                  # of the front page to X

The wiki is one page per destination in the left menu:

    index.html              giriş
    tum-vakalar.html        arama + dört filtre, 124 örneğin tamamı
    nis-01..16-*.html       16 iş kolu, örnekler kendi çapasıyla (#C060)
    supheli-iddialar.html   X seviyesi
    desenler.html · a006-jacobo.html · arastirma-politikasi.html
"""
import argparse
import csv
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "data" / "cases.csv"
ENC = ROOT / "encyclopedia"
OUT = ROOT / "docs"

REPO = "https://github.com/paradoksix/ai-money-workflows"
BLOB = f"{REPO}/blob/main"
SITE = "AI Gelir Vakaları Ansiklopedisi"

# Display order and copy for each niche. Order matches the nis-NN- file prefix.
NICHES = [
    ("video-gorsel-produksiyon", 1, "Video ve görsel üretimi",
     "Reklam filmi, ürün videosu, müzik klibi ve video kapak görseli. Talep gerçek, rekabet yüksek."),
    ("b2b-satis-lead", 2, "Şirketlere satış: müşteri adayı bulma",
     "Hedef şirketi bul, kararı veren kişiyi çıkar, satışçıya temiz bir not bırak. Kaynak koduyla en iyi doğrulanmış grup."),
    ("musteri-iletisim-destek", 3, "Müşteri iletişimi ve destek",
     "Gelen mesajı karşıla, konusuna ayır, eksik bilgiyi sor, gerekince bir insana devret."),
    ("ozel-yazilim-mikro-saas", 4, "Sipariş üzerine yazılım ve küçük ürünler",
     "Hazır bir sistem değil, uygulama satılan işler. Müşteri reklamdan değil, mevcut tanıdıklıktan geliyor."),
    ("icerik-sosyal-medya", 5, "İçerik, sosyal medya ve bülten",
     "Uzun içeriği parçalara ayır, bülten hazırla, kanal için düzenli üretim yap."),
    ("eticaret-katalog", 6, "E-ticaret ve ürün kataloğu",
     "Ürün bilgisi, katalog kalitesi, stok akışı. Türkiye için en uygun gruplardan biri."),
    ("kurumsal-operasyon-maliyet", 7, "Büyük şirketlerde maliyet düşürme",
     "Çoğunda yapay zekâ satılmıyor; ödenen yazılım ücreti, harcanan insan saati veya kayıp azaltılıyor."),
    ("ofis-belge-operasyonu", 8, "Ofis ve evrak işleri",
     "Form, e-posta ve tablo trafiğini düzene sokmak. Burada yapay zekâ çoğu zaman şart bile değil."),
    ("veri-cikti-temizligi", 9, "Yapay zekâ çıktısını temize çekme",
     "Yapay zekânın yarım bıraktığı işi, gerçekten kullanılabilir son ürüne çevirmek."),
    ("ajans-freelance-model", 10, "Nasıl satılıyor: fiyat, kapsam, süreklilik",
     "Ne satıldığını değil, işin nasıl fiyatlandığını ve aylık gelire nasıl döndüğünü anlatan örnekler."),
    ("yerel-isletme-saha-servisi", 11, "Mahalle esnafı ve saha servisi",
     "İşletmeye yüz yüze gidip gösterilebilen sistemler. Arşivin en sağlam tek örneği burada."),
    ("rag-bilgi-sistemleri", 12, "Kendi belgelerinden cevap veren sistemler",
     "Şirketin kendi dosyalarına dayanarak cevap üreten yardımcılar. Satış gerekçesi zekâ değil, gizlilik."),
    ("emlak-site-yonetimi", 13, "Emlak ve site yönetimi",
     "Kiracı talebi, tamir koordinasyonu, belge hazırlama ve müşteri adayı takibi."),
    ("muhasebe-finans-belge", 14, "Muhasebe ve fatura işleri",
     "Fatura, tahsilat, ön muhasebe. Değişmez kural: hesabı yapay zekâ yapmasın."),
    ("ik-ise-alim", 15, "İnsan kaynakları ve işe alım",
     "Yapay zekânın işi araştırma ve evrak; değerlendirme ve karar insanda kalır."),
    ("egitim-kurs-operasyonu", 16, "Kurs ve eğitim işletmeciliği",
     "Ders programı, veli iletişimi, ödeme takibi ve öğrenci bilgilerinin düzene sokulması."),
    ("tartismali", 17, "Şüpheli iddialar",
     "Denenecek bir iş değil; nelere kanmamak gerektiğini gösteren örnek."),
]
NICHE_BY_SLUG = {slug: (order, name, desc) for slug, order, name, desc in NICHES}

GRADES = [
    ("A", "Müşteri kanıtı + kodu açık",
     "İşin gerçek bir müşteriye satıldığı ve tam olarak hangi kodla yapıldığı, ikisi birden doğrulandı."),
    ("B", "Kodu açık, kazancı belirsiz",
     "Kod gerçek ve çalışıyor; ama tam olarak bu işin para kazandırdığı ayrıca gösterilmedi."),
    ("C", "Para kazandırmış, kodu yok",
     "Ödeme yapan müşteri, gelir ya da tasarruf anlatımı güçlü; ama işin kodu paylaşılmamış veya bulunamadı."),
    ("X", "Şüpheli",
     "Kazanç iddiasında gizli reklam ya da çıkar çatışması şüphesi var. Ana sayıma katılmıyor."),
]
GRADE_TITLE = {g: t for g, t, _ in GRADES}

REVENUE = [
    ("F", "İşi yapana ödenen ücret", "Hizmeti veren kişinin cebine giren para."),
    ("R", "Üründen gelen gelir", "Satılan ürün veya abonelikten doğan gelir."),
    ("S", "Müşterinin tasarrufu", "Müşterinin kazandığı zaman ya da kestiği gider."),
    ("V", "Başka ticari sonuç", "Kampanya değeri, alınan randevu, görüntülenme, tahsil edilen alacak."),
]
REV_TITLE = {c: n for c, n, _ in REVENUE}

SELLABILITY = [("high", "Yüksek"), ("medium", "Orta"), ("low", "Düşük")]
TR_LABEL = dict(SELLABILITY)

DIFFICULTY = {
    "easy": "Kolay", "easy-medium": "Kolay–orta", "medium": "Orta",
    "medium-hard": "Orta–zor", "hard": "Zor",
}

LICENSE = {
    "unknown": "Bilinmiyor — kod bulunmadığı için lisans da bakılmadı",
    "no_root_license": "Açık lisansı yok — kod kopyalanamaz, yalnızca kaynak gösterilir",
    "private_commercial_library": "Kapalı ticari kütüphane — kodu paylaşılmıyor",
}

# What research has actually been done on a case, in plain words.
STATUS = {
    "encyclopedia_only": "Henüz araştırma kuyruğuna girmedi; yalnız ansiklopedi metninde var",
    "paid_claim_repo_missing": "Ödeme yapıldığı anlatılıyor, kodu bulunamadı",
    "verified_exact_repo": "Kodun tam olarak hangisi olduğu doğrulandı",
    "repo_missing": "Kodu bulunamadı",
    "product_revenue_repo_missing": "Üründen gelir bildiriliyor, kodu bulunamadı",
    "commercial_roi_repo_missing": "Ticari kazanç bildiriliyor, kodu bulunamadı",
    "commercial_creator_repo": "Kodu üreticisinin kendi deposunda",
    "official_template_github_mirror": "Resmî şablonun GitHub kopyası",
    "needs_verification": "Doğrulanmayı bekliyor",
    "client_claim_repo_missing": "Müşteri anlatımı var, kodu bulunamadı",
    "superseded_by_A006": "Bu kayıt A006'ya devredildi",
    "paid_claim_source_private": "Ödeme anlatılıyor, kaynağı kapalı",
    "disputed": "Şüpheli — ana sayıma katılmıyor",
}

# Terms kept as-is because they are searchable and precise, explained once here.
GLOSSARY = [
    ("n8n", "İş akışı kurmaya yarayan, kod yazmadan kutuları birbirine bağladığın açık kaynak araç."),
    ("RAG", "Yapay zekânın, kendi kafasından değil senin verdiğin belgelerden cevap üretmesi."),
    ("SaaS", "Aylık/yıllık abonelikle satılan, tarayıcıdan kullanılan yazılım."),
    ("API", "İki yazılımın birbirine otomatik veri geçirmesini sağlayan bağlantı noktası."),
    ("OCR", "Fotoğraf ya da PDF'teki yazıyı, düzenlenebilir metne çeviren teknoloji."),
    ("Repo", "Bir projenin kaynak kodunun durduğu yer — burada hep GitHub'daki hâli kastediliyor."),
]

GRADE_ORDER = {"A": 0, "B": 1, "C": 2, "X": 3}


def e(text):
    return html.escape(str(text), quote=True)


def load():
    with CASES.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    rows.sort(key=lambda r: (GRADE_ORDER[r["evidence_grade"]], int(r["id"][1:])))
    return rows


# ── markdown ────────────────────────────────────────────────────────────────
# The encyclopedia uses a deliberately narrow subset: headings, bold, inline
# code, links, bullet and numbered lists, rules. Anything outside that subset
# raises instead of being silently dropped, so a future table or code fence
# fails the build rather than vanishing from the page.

UNSUPPORTED = [
    (re.compile(r"^```"), "kod bloğu"),
    (re.compile(r"^\s*\|"), "tablo"),
    (re.compile(r"!\["), "görsel"),
]

CODE_RE = re.compile(r"`([^`\n]+)`")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*", re.S)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
BARE_URL_RE = re.compile(r"(?<![\"'>=])\bhttps?://[^\s<>()\[\]]+[^\s<>()\[\].,;:!?]")


def md_inline(text):
    """Render one line of markdown to HTML. Escapes first, so any HTML in the
    source is shown as text rather than executed."""
    out = e(text)
    stash = []

    def keep(markup):
        stash.append(markup)
        return f"\x00{len(stash) - 1}\x01"

    # Code spans first: their contents must not be re-parsed as bold or links.
    out = CODE_RE.sub(lambda m: keep(f"<code>{m.group(1)}</code>"), out)
    out = LINK_RE.sub(
        lambda m: keep(f'<a href="{m.group(2)}">{m.group(1)}</a>'), out)
    out = BARE_URL_RE.sub(lambda m: keep(f'<a href="{m.group(0)}">{m.group(0)}</a>'), out)
    out = BOLD_RE.sub(lambda m: f"<strong>{m.group(1)}</strong>", out)
    return re.sub(r"\x00(\d+)\x01", lambda m: stash[int(m.group(1))], out)


def md_blocks(lines, where, base_level=2):
    """Render a run of markdown lines. `base_level` shifts source headings so a
    page never grows a second <h1> or skips a heading level."""
    out = []
    para = []
    ul = []
    ol = []
    quote = []

    def flush():
        if para:
            out.append(f"<p>{md_inline(' '.join(para))}</p>")
            para.clear()
        if ul:
            items = "".join(f"<li>{md_inline(x)}</li>" for x in ul)
            out.append(f"<ul>{items}</ul>")
            ul.clear()
        if ol:
            items = "".join(f"<li>{md_inline(x)}</li>" for x in ol)
            out.append(f"<ol>{items}</ol>")
            ol.clear()
        if quote:
            out.append(f"<blockquote><p>{md_inline(' '.join(quote))}</p></blockquote>")
            quote.clear()

    for raw in lines:
        line = raw.rstrip()
        for pattern, what in UNSUPPORTED:
            if pattern.search(line):
                raise SystemExit(
                    f"build_site.py: {where} içinde desteklenmeyen markdown ({what}): {line[:60]!r}\n"
                    "Renderer bu yapıyı tanımıyor. Ya metni sadeleştir ya da md_blocks'a destek ekle."
                )
        if not line.strip():
            flush()
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush()
            level = min(base_level + len(m.group(1)) - 1, 6)
            out.append(f"<h{level}>{md_inline(m.group(2))}</h{level}>")
            continue
        if re.match(r"^-{3,}$", line.strip()):
            flush()
            out.append("<hr>")
            continue
        m = re.match(r"^\s*[-*+]\s+(.*)$", line)
        if m:
            if para or ol or quote:
                flush()
            ul.append(m.group(1))
            continue
        m = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if m:
            if para or ul or quote:
                flush()
            ol.append(m.group(1))
            continue
        m = re.match(r"^\s*>\s?(.*)$", line)
        if m:
            if para or ul or ol:
                flush()
            quote.append(m.group(1))
            continue
        if ul or ol or quote:
            flush()
        para.append(line.strip())
    flush()
    return "\n".join(out)


CASE_HEAD_RE = re.compile(r"^([ABCX]\d{3})\s*[—-]\s*(.*)$")


def read_markdown(path):
    """Split an encyclopedia file into its title, its opening text, and the
    sections that follow. A section is a case block when its heading starts
    with a case id."""
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    title = ""
    start = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            start = i + 1
            break
    preamble, sections = [], []
    current = None
    for line in lines[start:]:
        if line.startswith("## "):
            heading = line[3:].strip()
            m = CASE_HEAD_RE.match(heading)
            current = {
                "case_id": m.group(1) if m else None,
                "heading": m.group(2).strip() if m else heading,
                "lines": [],
            }
            sections.append(current)
        elif current is None:
            preamble.append(line)
        else:
            current["lines"].append(line)
    # A trailing `---` belongs to the separator, not to the block above it.
    for s in sections:
        while s["lines"] and not s["lines"][-1].strip():
            s["lines"].pop()
        if s["lines"] and re.match(r"^-{3,}$", s["lines"][-1].strip()):
            s["lines"].pop()
    while preamble and not preamble[-1].strip():
        preamble.pop()
    if preamble and re.match(r"^-{3,}$", preamble[-1].strip()):
        preamble.pop()
    return title, preamble, sections


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
  --nav-w:278px;
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

html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:"IBM Plex Sans","Segoe UI",system-ui,-apple-system,sans-serif;
  font-size:16px; line-height:1.6; -webkit-font-smoothing:antialiased;
}
h1,h2,h3,h4{font-family:Newsreader,Georgia,"Times New Roman",serif;font-weight:600;
  text-wrap:balance;margin:0}
a{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:3px}
.mono{font-family:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  font-variant-numeric:tabular-nums}
code{font-family:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size:.875em;background:var(--rule-soft);border:1px solid var(--rule);
  border-radius:4px;padding:.5px 5px;word-break:break-word}

/* skip link: first stop for keyboard and screen-reader users */
.skip{position:absolute;left:-9999px;top:0;z-index:100;padding:10px 16px;
  background:var(--surface);border:1px solid var(--accent);border-radius:0 0 6px 0}
.skip:focus{left:0}

/* ── shell ── */
.shell{display:grid;grid-template-columns:var(--nav-w) minmax(0,1fr);
  align-items:start;min-height:100vh}

/* ── left menu ── */
.nav{position:sticky;top:0;height:100vh;overflow-y:auto;overscroll-behavior:contain;
  background:var(--surface);border-right:1px solid var(--rule);padding:22px 0 40px}
.nav-brand{display:block;padding:0 20px 16px;text-decoration:none;color:inherit}
.nav-brand b{display:block;font-family:Newsreader,Georgia,serif;font-size:1.0625rem;
  font-weight:600;line-height:1.25;letter-spacing:-.01em}
.nav-brand span{display:block;margin-top:5px;font-size:.75rem;color:var(--muted);line-height:1.45}
.nav-sec{margin-top:20px}
.nav-sec > p{margin:0 20px 7px;font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:10px;letter-spacing:.13em;text-transform:uppercase;color:var(--muted)}
.nav ul{list-style:none;margin:0;padding:0}
.nav a.item{
  display:flex;align-items:baseline;gap:9px;padding:7px 20px;
  text-decoration:none;color:var(--ink);font-size:.875rem;line-height:1.4;
  border-left:3px solid transparent
}
.nav a.item:hover{background:var(--accent-soft)}
.nav a.item[aria-current="page"]{
  border-left-color:var(--accent);background:var(--accent-soft);
  color:var(--accent);font-weight:600
}
.nav .num{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.6875rem;
  color:var(--muted);flex:none;width:16px;text-align:right}
.nav .item[aria-current="page"] .num{color:var(--accent)}
.nav .n{margin-left:auto;font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:.6875rem;color:var(--muted);flex:none;padding-left:8px}
.nav-foot{margin:22px 20px 0;padding-top:16px;border-top:1px solid var(--rule);
  font-size:.75rem;color:var(--muted);line-height:1.6}
.nav-foot a{display:block;margin-top:5px}

/* mobile: the menu becomes a disclosure above the content */
.nav-toggle{display:none}

/* ── content ── */
.page{min-width:0;padding:0 0 72px}
.col{max-width:812px;margin:0 auto;padding:0 32px}
.col-wide{max-width:1080px}
.page-head{border-bottom:1px solid var(--rule);background:var(--surface);
  padding:40px 0 30px;margin-bottom:34px}
.eyebrow{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:11px;
  letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 13px}
h1{font-size:clamp(1.8rem,1.2rem + 2.2vw,2.6rem);line-height:1.13;letter-spacing:-.015em}
.standfirst{margin:15px 0 0;max-width:64ch;color:var(--muted);font-size:1.0312rem}
.standfirst strong{color:var(--ink);font-weight:600}

/* prose rendered from the encyclopedia markdown */
.prose h2{font-size:1.375rem;margin:38px 0 12px;letter-spacing:-.01em}
.prose h3{font-size:1.125rem;margin:30px 0 10px}
.prose h4{font-size:1rem;margin:24px 0 8px}
.prose p{margin:0 0 14px}
.prose ul,.prose ol{margin:0 0 15px;padding-left:22px}
.prose li{margin-bottom:6px}
.prose hr{border:0;border-top:1px solid var(--rule);margin:30px 0}
.prose blockquote{margin:0 0 15px;padding:2px 0 2px 16px;border-left:3px solid var(--rule);
  color:var(--muted)}
.prose a{word-break:break-word}
.prose > :first-child{margin-top:0}

/* ── evidence legend ── */
.legend{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:1px;
  background:var(--rule);border:1px solid var(--rule);border-radius:6px;overflow:hidden;margin:14px 0 0}
.legend div{background:var(--surface);padding:14px 16px}
.legend dt{display:flex;align-items:center;gap:8px;font-weight:600;font-size:.875rem;margin:0 0 4px}
.legend dd{margin:0;font-size:.8125rem;color:var(--muted);line-height:1.5}

/* grade chip: the letter is always present, so colour never carries meaning alone */
.chip{display:inline-flex;align-items:center;justify-content:center;
  min-width:22px;height:22px;padding:0 6px;border-radius:4px;
  font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:12px;font-weight:600;
  border:1px solid currentColor;flex:none}
.g-A{color:var(--gA-text);background:var(--gA-wash)}
.g-B{color:var(--gB-text);background:var(--gB-wash)}
.g-C{color:var(--gC-text);background:var(--gC-wash)}
.g-X{color:var(--gX-text);background:var(--gX-wash)}

/* ── glossary ── */
.glossary{margin-top:16px;border:1px solid var(--rule);border-radius:6px;background:var(--surface)}
.glossary summary{padding:11px 16px;cursor:pointer;font-size:.875rem;font-weight:600;
  color:var(--accent);list-style:none}
.glossary summary::-webkit-details-marker{display:none}
.glossary summary::before{content:"+ ";font-family:"IBM Plex Mono",ui-monospace,monospace}
.glossary[open] summary::before{content:"\\2212 "}
.glossary[open] summary{border-bottom:1px solid var(--rule)}
.glossary dl{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));
  gap:14px 24px;margin:0;padding:16px}
.glossary dt{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.8125rem;
  font-weight:600;color:var(--ink);margin-bottom:3px}
.glossary dd{margin:0;font-size:.8125rem;color:var(--muted);line-height:1.5}

/* ── distribution meter ── */
.meter-block{margin-top:32px}
.meter-total{font-family:Newsreader,Georgia,serif;font-size:2.125rem;line-height:1;font-weight:600}
.meter-total span{font-size:.9062rem;font-family:"IBM Plex Sans",sans-serif;color:var(--muted);
  margin-left:8px;font-weight:400}
.meter{display:flex;gap:2px;height:32px;border-radius:4px;overflow:hidden;margin-top:11px}
.meter i{display:flex;align-items:center;justify-content:center;font-style:normal;
  font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:11px;font-weight:600;
  color:#fff;min-width:2px}
.s-A{background:var(--gA-fill)} .s-B{background:var(--gB-fill)}
.s-C{background:var(--gC-fill)} .s-X{background:var(--gX-fill)}
.meter-key{display:flex;gap:18px;flex-wrap:wrap;margin-top:10px;font-size:.8125rem;color:var(--muted)}
.meter-key span{display:flex;align-items:center;gap:6px}
.dot{width:9px;height:9px;border-radius:2px;flex:none}

/* ── niche grid on the front page ── */
.niches{display:grid;grid-template-columns:repeat(auto-fill,minmax(252px,1fr));gap:12px;margin-top:20px}
.niche{display:flex;flex-direction:column;gap:8px;text-decoration:none;color:inherit;
  background:var(--surface);border:1px solid var(--rule);border-radius:7px;padding:16px;
  box-shadow:var(--shadow);transition:border-color .15s,transform .15s}
.niche:hover{border-color:var(--accent);transform:translateY(-1px)}
.niche-top{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
.niche-name{font-weight:600;font-size:.9375rem;line-height:1.3}
.niche-n{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.8125rem;
  color:var(--muted);flex:none}
.niche-desc{font-size:.8125rem;color:var(--muted);line-height:1.5;margin:0}
.niche-bar{display:flex;gap:2px;height:4px;border-radius:2px;overflow:hidden;margin-top:auto}

/* ── filters (all-cases page) ── */
.filters{position:sticky;top:0;z-index:20;background:var(--paper);
  border-bottom:1px solid var(--rule);padding:14px 0;margin-top:8px}
.filter-row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.search{flex:1 1 250px;min-width:190px;padding:9px 12px;font:inherit;font-size:.9375rem;
  background:var(--surface);color:var(--ink);border:1px solid var(--rule);border-radius:6px}
.search::placeholder{color:var(--muted)}
select{padding:9px 10px;font:inherit;font-size:.875rem;background:var(--surface);
  color:var(--ink);border:1px solid var(--rule);border-radius:6px;cursor:pointer}
.btn{padding:9px 13px;font:inherit;font-size:.875rem;background:var(--surface);
  color:var(--muted);border:1px solid var(--rule);border-radius:6px;cursor:pointer}
.btn:hover{color:var(--ink);border-color:var(--accent)}
.count{font-size:.8125rem;color:var(--muted);margin:9px 0 0}
.count b{color:var(--ink);font-weight:600}
.group{margin-top:34px}
.group > h2{font-size:1.0625rem;padding-bottom:8px;border-bottom:2px solid var(--ink);
  display:flex;justify-content:space-between;align-items:baseline;gap:12px}
.group > h2 em{font-style:normal;font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:.75rem;color:var(--muted);font-weight:400;flex:none}
.row{display:grid;grid-template-columns:auto 1fr;gap:6px 14px;padding:15px 0;
  border-bottom:1px solid var(--rule-soft)}
.row-id{display:flex;flex-direction:column;align-items:center;gap:6px;width:50px}
.row-id .mono{font-size:.75rem;color:var(--muted)}
.row h3{font-weight:600;font-size:.9688rem;line-height:1.35;font-family:"IBM Plex Sans",sans-serif}
.row h3 a{text-decoration:none}
.row h3 a:hover{text-decoration:underline}
.row p{margin:6px 0 0;font-size:.9062rem;color:var(--muted);max-width:72ch}
.empty{padding:44px 0;text-align:center;color:var(--muted)}

/* ── case block on a niche page ── */
.case{border:1px solid var(--rule);border-radius:8px;background:var(--surface);
  padding:20px 22px;margin-bottom:16px;box-shadow:var(--shadow);scroll-margin-top:18px}
.case:target{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}
.case-head{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:14px;
  padding-bottom:12px;border-bottom:1px solid var(--rule-soft)}
.case-head .mono{font-size:.75rem;color:var(--muted)}
.case-head h3{font-size:1.1875rem;line-height:1.3;flex:1 1 260px;letter-spacing:-.005em}
.case-head .self{text-decoration:none;color:var(--muted);font-size:.875rem;opacity:0;
  transition:opacity .15s;flex:none}
.case:hover .case-head .self,.case-head .self:focus{opacity:1}
.case-body p{margin:0 0 12px;font-size:.9375rem}
.case-body ul,.case-body ol{margin:0 0 13px;padding-left:22px;font-size:.9375rem}
.case-body li{margin-bottom:5px}
.case-body > :last-child{margin-bottom:0}

/* künye: the structured record behind the prose */
.facts{margin:16px 0 0;border-top:1px solid var(--rule-soft);padding-top:4px}
.facts summary{cursor:pointer;font-size:.8125rem;font-weight:600;color:var(--accent);
  padding:8px 0 4px;list-style:none}
.facts summary::-webkit-details-marker{display:none}
.facts summary::before{content:"+ ";font-family:"IBM Plex Mono",ui-monospace,monospace}
.facts[open] summary::before{content:"\\2212 "}
.facts dl{display:grid;grid-template-columns:minmax(130px,auto) minmax(0,1fr);
  gap:1px;margin:8px 0 0;background:var(--rule-soft);border:1px solid var(--rule-soft);
  border-radius:6px;overflow:hidden;font-size:.8125rem}
.facts dt{background:var(--surface);padding:8px 12px;color:var(--muted);font-weight:600}
.facts dd{background:var(--surface);padding:8px 12px;margin:0;word-break:break-word}
.facts dd.gap{color:var(--muted);font-style:italic}
.facts dd a{word-break:break-all}
.tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:13px}
.tag{font-size:.75rem;padding:2px 8px;border-radius:4px;background:var(--rule-soft);
  color:var(--muted);border:1px solid var(--rule)}
.tag.money{color:var(--ink);font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-weight:600;background:var(--accent-soft);border-color:var(--accent)}

/* ── in-page contents on a niche page ── */
.toc{border:1px solid var(--rule);border-radius:7px;background:var(--surface);
  padding:15px 18px;margin:22px 0 30px}
.toc h2{font-size:.9375rem;margin-bottom:9px}
.toc ul{list-style:none;margin:0;padding:0;display:grid;
  grid-template-columns:repeat(auto-fill,minmax(232px,1fr));gap:2px 16px}
.toc li{display:flex;align-items:baseline;gap:7px;font-size:.8125rem;padding:3px 0}
.toc a{text-decoration:none}
.toc a:hover{text-decoration:underline}
.toc .chip{min-width:19px;height:19px;font-size:10.5px}

/* ── prev / next ── */
.pager{display:flex;gap:12px;flex-wrap:wrap;justify-content:space-between;margin-top:36px;
  padding-top:22px;border-top:1px solid var(--rule)}
.pager a{flex:1 1 230px;text-decoration:none;color:inherit;background:var(--surface);
  border:1px solid var(--rule);border-radius:7px;padding:13px 16px}
.pager a:hover{border-color:var(--accent)}
.pager span{display:block;font-size:.6875rem;text-transform:uppercase;letter-spacing:.1em;
  color:var(--muted);font-family:"IBM Plex Mono",ui-monospace,monospace;margin-bottom:4px}
.pager b{font-size:.9062rem;font-weight:600;line-height:1.35}
.pager .next{text-align:right}

/* ── page-level notes ── */
.disclaimer{margin-top:24px;padding:14px 16px;border-left:3px solid var(--gB-fill);
  background:var(--gB-wash);border-radius:0 5px 5px 0;font-size:.875rem;color:var(--ink)}
.disclaimer p{margin:0 0 9px}
.disclaimer > :last-child{margin-bottom:0}
.pagefoot{margin-top:44px;padding-top:20px;border-top:1px solid var(--rule);
  font-size:.8125rem;color:var(--muted)}
.pagefoot a{margin-right:16px;display:inline-block}

.theme-toggle{position:fixed;right:18px;bottom:18px;z-index:30;width:42px;height:42px;
  border-radius:50%;background:var(--surface);color:var(--ink);border:1px solid var(--rule);
  cursor:pointer;font-size:16px;box-shadow:var(--shadow);line-height:1}

/* ── narrow screens: menu folds into a disclosure ── */
@media (max-width:900px){
  .shell{grid-template-columns:minmax(0,1fr)}
  .nav{position:static;height:auto;border-right:0;border-bottom:1px solid var(--rule);
    padding:14px 0 0;max-height:none;overflow:visible}
  .nav-brand{padding:0 18px 12px}
  .nav-body{display:none;padding-bottom:16px}
  .nav.open .nav-body{display:block}
  .nav-toggle{display:block;width:calc(100% - 36px);margin:0 18px 14px;padding:9px 13px;
    font:inherit;font-size:.875rem;text-align:left;background:var(--paper);color:var(--ink);
    border:1px solid var(--rule);border-radius:6px;cursor:pointer}
  .col{padding:0 18px}
  .page-head{padding:26px 0 22px;margin-bottom:26px}
  .row{grid-template-columns:1fr}
  .row-id{flex-direction:row;width:auto}
  .meter i{font-size:0}
  .case{padding:17px 16px}
  .facts dl{grid-template-columns:1fr}
  .facts dt{padding-bottom:0;background:var(--surface)}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
@media print{.nav,.theme-toggle,.filters{display:none}.shell{display:block}}
"""


# ── page addresses ──────────────────────────────────────────────────────────
HOME = "index.html"
ALL_CASES = "tum-vakalar.html"
DISPUTED = "supheli-iddialar.html"
PATTERNS = "desenler.html"
JACOBO = "a006-jacobo.html"
POLICY = "arastirma-politikasi.html"


def niche_href(slug):
    if slug == "tartismali":
        return DISPUTED
    order, _, _ = NICHE_BY_SLUG[slug]
    return f"nis-{order:02d}-{slug}.html"


def case_href(row):
    """A case lives in a section of its niche page, and keeps a stable address."""
    return f"{niche_href(row['niche'])}#{row['id']}"


# Cross-references inside the encyclopedia point at markdown files. On the wiki
# they have to point at wiki pages instead. Both forms are rewritten: a link
# target keeps its own label, a bare `file.md` mention becomes a proper link.
DOC_LINKS = [
    ("../RESEARCH_POLICY.md", POLICY, "güvenilirlik ölçütleri"),
    ("../ENCYCLOPEDIA.md", HOME, "iş kolları listesi"),
    ("DESENLER.md", PATTERNS, "ortak dersler"),
    ("A006-JACOBO-DEVICE-REPAIR.md", JACOBO, "A006 vakası"),
    ("APPENDIX-X-DISPUTED.md", DISPUTED, "şüpheli iddialar"),
    ("https://paradoksix.github.io/ai-money-workflows/", ALL_CASES, "bütün örnekler"),
]


# Two preamble lines exist in every niche file purely as navigation aids for
# reading the markdown on GitHub: the case count (now in the page header) and
# the "where do I find X" pointer (now the left menu, on every page). Rendering
# them again would repeat the header one line below itself.
MOVED_TO_CHROME = (
    re.compile(r"^\*\*Bu grupta \d+ örnek var\.\*\*"),
    re.compile(r"^Harflerin ne anlama geldiği için"),
)


def drop_moved(lines):
    return [l for l in lines if not any(p.match(l.strip()) for p in MOVED_TO_CHROME)]


def relink(lines):
    out = []
    for line in lines:
        for target, href, label in DOC_LINKS:
            # A link whose label is just the file name reads as a file name on
            # the wiki. Rewrite label and target together, before the two
            # narrower rules below — otherwise they nest inside each other.
            whole = re.compile(r"\[(`?)" + re.escape(target) + r"\1\]\(" + re.escape(target) + r"\)")
            line = whole.sub(f"[{label}]({href})", line)
            line = line.replace(f"]({target})", f"]({href})")
            line = line.replace(f"`{target}`", f"[{label}]({href})")
        out.append(line)
    return out


# ── shared shell ────────────────────────────────────────────────────────────
def nav(active, rows):
    by_niche = {}
    for r in rows:
        by_niche.setdefault(r["niche"], []).append(r)

    o = []
    a = o.append
    a('<nav class="nav" id="nav" aria-label="Site menüsü">')
    a(f'<a class="nav-brand" href="{HOME}"><b>{e(SITE)}</b>'
      "<span>Yapay zekâyla para kazanıldığı bildirilen işlerin, her birinin ne kadar "
      "kanıtlı olduğu işaretlenmiş arşivi.</span></a>")
    a('<button class="nav-toggle" id="nav-toggle" type="button" '
      'aria-expanded="false" aria-controls="nav-body">Menü ▾</button>')
    a('<div class="nav-body" id="nav-body">')

    def item(href, label, num=None, count=None):
        cur = ' aria-current="page"' if href == active else ""
        n = f'<span class="num">{e(num)}</span>' if num else ""
        c = f'<span class="n">{count}</span>' if count is not None else ""
        a(f'<li><a class="item" href="{href}"{cur}>{n}<span>{e(label)}</span>{c}</a></li>')

    a("<ul>")
    item(HOME, "Giriş")
    item(ALL_CASES, "Bütün örnekler", count=len(rows))
    a("</ul>")

    a('<div class="nav-sec"><p>İş kolları</p><ul>')
    for slug, order, name, _ in NICHES:
        if slug == "tartismali":
            continue
        item(niche_href(slug), name, num=f"{order:02d}", count=len(by_niche.get(slug, [])))
    a("</ul></div>")

    a('<div class="nav-sec"><p>Arşiv</p><ul>')
    item(JACOBO, "En sağlam örnek: A006")
    item(PATTERNS, "Örneklerden çıkan ortak dersler")
    item(DISPUTED, "Şüpheli iddialar", count=len(by_niche.get("tartismali", [])))
    item(POLICY, "Bir örnek arşive nasıl giriyor?")
    a("</ul></div>")

    a('<div class="nav-foot">Metin ve veri CC BY 4.0. Atıf verilen kodlar kapsam dışı.'
      f'<a href="{REPO}">Proje deposu →</a>'
      f'<a href="{BLOB}/data/cases.csv">Ham veri tablosu →</a></div>')
    a("</div></nav>")
    return "\n".join(o)


def page_footer(extra=()):
    links = [("Proje deposu", REPO), ("Ham veri tablosu", f"{BLOB}/data/cases.csv"),
             ("Hâlâ aranan kaynaklar", f"{BLOB}/research_queue.csv")]
    links.extend(extra)
    body = "".join(f'<a href="{e(href)}">{e(label)}</a>' for label, href in links)
    return ('<div class="pagefoot"><p>Bu sayfa <code>data/cases.csv</code> ve ansiklopedi '
            "metinlerinden üretiliyor; elle düzenlenmiyor.</p>"
            f'<p style="margin-top:8px">{body}</p></div>')


def shell(*, active, title, description, head_html, body_html, rows, extra_js=""):
    desc = e(description)
    page_title = title if title == SITE else f"{title} · {SITE}"
    head = (
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f"<title>{e(page_title)}</title>\n"
        f'<meta name="description" content="{desc}">\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:'
        "opsz,wght@6..72,500;6..72,600&family=IBM+Plex+Mono:wght@400;600&"
        'family=IBM+Plex+Sans:wght@400;600&display=swap">\n'
        '<link rel="stylesheet" href="wiki.css">'
    )
    body = "\n".join([
        f'<a class="skip" href="#icerik">İçeriğe geç</a>',
        '<div class="shell">',
        nav(active, rows),
        '<div class="page" id="icerik">',
        head_html,
        body_html,
        "</div></div>",
        '<button class="theme-toggle" id="theme" type="button" '
        'aria-label="Açık ve koyu tema arasında geçiş yap">◐</button>',
        '<script src="wiki.js"></script>',
        extra_js,
    ])
    return head, body


def write_page(name, *, active, title, description, head_html, body_html, rows, extra_js=""):
    head, body = shell(active=active, title=title, description=description,
                       head_html=head_html, body_html=body_html, rows=rows, extra_js=extra_js)
    (OUT / name).write_text(
        f'<!doctype html>\n<html lang="tr">\n<head>\n{head}\n</head>\n'
        f"<body>\n{body}\n</body>\n</html>\n",
        encoding="utf-8",
    )
    return head, body


def page_head(eyebrow, title, standfirst="", wide=False):
    col = "col col-wide" if wide else "col"
    o = [f'<header class="page-head"><div class="{col}">']
    if eyebrow:
        o.append(f'<p class="eyebrow">{e(eyebrow)}</p>')
    o.append(f"<h1>{e(title)}</h1>")
    if standfirst:
        o.append(f'<p class="standfirst">{standfirst}</p>')
    o.append("</div></header>")
    return "\n".join(o)


def grade_bar(group):
    parts = []
    for g, _, _ in GRADES:
        n = sum(1 for r in group if r["evidence_grade"] == g)
        if n:
            parts.append(f'<i class="s-{g}" style="flex:{n}"></i>')
    return "".join(parts)


def grade_summary(group):
    bits = [f"{g}: {sum(1 for r in group if r['evidence_grade'] == g)}"
            for g, _, _ in GRADES
            if any(r["evidence_grade"] == g for r in group)]
    return " · ".join(bits)


# ── one case, as it appears on its niche page ───────────────────────────────
def facts_list(row):
    """The structured record behind the prose. Missing values are stated as
    missing rather than hidden — the gaps are part of what the archive records."""
    out = []

    def add(label, value, gap):
        if value:
            out.append(f"<dt>{e(label)}</dt><dd>{value}</dd>")
        else:
            out.append(f'<dt>{e(label)}</dt><dd class="gap">{e(gap)}</dd>')

    rev = row["revenue_type"].strip()
    add("Para nereden geliyor",
        f'<b class="mono">{e(rev)}</b> — {e(REV_TITLE[rev])}' if rev in REV_TITLE else "",
        "kaydedilmedi")
    add("Bildirilen tutar",
        f'<b class="mono">{e(row["reported_amount"])}</b>' if row["reported_amount"].strip() else "",
        "rakam kaydedilmedi")
    add("Bildirilen sonuç", e(row["reported_result"]) if row["reported_result"].strip() else "",
        "kaydedilmedi")
    add("Yapılan iş", e(row["work_model"]) if row["work_model"].strip() else "", "kaydedilmedi")
    add("Müşteri", e(row["client_type"]) if row["client_type"].strip() else "", "kaydedilmedi")
    add("Kullanılan araçlar", e(row["stack"]) if row["stack"].strip() else "", "kaydedilmedi")
    add("Kurma zorluğu", e(DIFFICULTY.get(row["difficulty"], row["difficulty"])), "kaydedilmedi")
    add("Türkiye'ye uygunluk",
        e(TR_LABEL.get(row["tr_sellability"], row["tr_sellability"])), "kaydedilmedi")

    src = row["source_url"].strip()
    add("Anlatıldığı yer", f'<a href="{e(src)}">{e(src)}</a>' if src else "",
        "kaynağın tam adresi kaydedilmemiş")
    repo = row["repo_url"].strip()
    add("İşin kodu", f'<a href="{e(repo)}">{e(repo)}</a>' if repo else "",
        "kodu paylaşılmamış veya bulunamadı")
    commit = row["pinned_commit"].strip()
    add("Kodun sabitlenmiş sürümü",
        f'<code title="{e(commit)}">{e(commit[:12])}…</code>' if commit else "",
        "sabitlenmiş sürüm yok")
    add("Kodu kullanma izni", e(LICENSE.get(row["license_status"], row["license_status"])), "—")
    add("Araştırmanın durumu", e(STATUS.get(row["status"], row["status"])), "—")
    return f'<dl>{"".join(out)}</dl>'


def case_tags(row):
    tags = []
    if row["reported_amount"].strip():
        rev = row["revenue_type"].strip()
        title = REV_TITLE.get(rev, "Bildirilen sonuç")
        tags.append(f'<span class="tag money" title="{e(title)}">{e(row["reported_amount"])}</span>')
    elif row["reported_result"].strip():
        tags.append(f'<span class="tag">{e(row["reported_result"])}</span>')
    if row["work_model"].strip():
        tags.append(f'<span class="tag">{e(row["work_model"])}</span>')
    if row["stack"].strip():
        tags.append(f'<span class="tag">{e(row["stack"])}</span>')
    tr = TR_LABEL.get(row["tr_sellability"], row["tr_sellability"])
    tags.append('<span class="tag" title="Türkiye\'de satması ne kadar kolay olur — '
                f'kaba bir tahmin, garanti değil">Türkiye\'ye uygunluk: {e(tr)}</span>')
    return f'<div class="tags">{"".join(tags)}</div>'


def case_block(row, section, where):
    cid = row["id"]
    grade = row["evidence_grade"]
    prose = md_blocks(relink(section["lines"]), f"{where} / {cid}", base_level=4)
    return "\n".join([
        f'<article class="case" id="{e(cid)}">',
        '<div class="case-head">',
        f'<span class="chip g-{grade}" title="{e(GRADE_TITLE[grade])}">{grade}</span>',
        f'<span class="mono">{e(cid)}</span>',
        f'<h3>{md_inline(section["heading"] or row["title"])}</h3>',
        f'<a class="self" href="#{e(cid)}" aria-label="{e(cid)} örneğinin bağlantısı">#</a>',
        "</div>",
        f'<div class="case-body">{prose}</div>',
        case_tags(row),
        '<details class="facts"><summary>Künye ve kaynak</summary>',
        facts_list(row),
        "</details>",
        "</article>",
    ])


def toc(pairs):
    if not pairs:
        return ""
    o = ['<nav class="toc" aria-label="Bu sayfadaki örnekler">',
         f"<h2>Bu sayfadaki {len(pairs)} örnek</h2><ul>"]
    for row, section in pairs:
        g = row["evidence_grade"]
        o.append(f'<li><span class="chip g-{g}" title="{e(GRADE_TITLE[g])}">{g}</span>'
                 f'<a href="#{e(row["id"])}">'
                 f'{md_inline(section["heading"] or row["title"])}</a></li>')
    o.append("</ul></nav>")
    return "\n".join(o)


def pager(prev, nxt):
    if not prev and not nxt:
        return ""
    o = ['<nav class="pager" aria-label="Önceki ve sonraki iş kolu">']
    if prev:
        o.append(f'<a href="{prev[0]}"><span>← Önceki</span><b>{e(prev[1])}</b></a>')
    if nxt:
        o.append(f'<a class="next" href="{nxt[0]}"><span>Sonraki →</span><b>{e(nxt[1])}</b></a>')
    o.append("</nav>")
    return "\n".join(o)


# ── pages ───────────────────────────────────────────────────────────────────
def build_niche_page(slug, rows, by_niche, seq):
    order, name, desc = NICHE_BY_SLUG[slug]
    group = by_niche.get(slug, [])
    by_id = {r["id"]: r for r in group}

    if slug == "tartismali":
        src = ENC / "APPENDIX-X-DISPUTED.md"
        eyebrow = "Arşiv"
    else:
        src = ENC / f"nis-{order:02d}-{slug}.md"
        eyebrow = f"İş kolu {order:02d} / 16"
    _, preamble, sections = read_markdown(src)
    where = src.name

    pairs, tail = [], []
    for section in sections:
        cid = section["case_id"]
        if cid and cid in by_id:
            pairs.append((by_id[cid], section))
        else:
            tail.append(section)

    seen = {r["id"] for r, _ in pairs}
    missing = [r for r in group if r["id"] not in seen]

    body = ['<div class="col">']
    intro = md_blocks(drop_moved(relink(preamble)), f"{where} / giriş", base_level=2)
    if intro:
        body.append(f'<div class="prose">{intro}</div>')
    body.append(toc(pairs))
    for row, section in pairs:
        body.append(case_block(row, section, where))
    for row in missing:
        # A record with no encyclopedia block still gets its card, from the CSV alone.
        body.append(case_block(row, {"heading": row["title"], "lines": [row["summary"]]}, where))
    for section in tail:
        body.append(f'<div class="prose"><h2>{e(section["heading"])}</h2>'
                    + md_blocks(relink(section["lines"]), where, base_level=2) + "</div>")
    body.append(pager(*seq))
    body.append(page_footer([("Bu iş kolunun kaynak metni", f"{BLOB}/encyclopedia/{src.name}")]))
    body.append("</div>")

    stand = (f"<strong>Bu grupta {len(group)} örnek var</strong> — ne kadar güvenilir "
             f"oldukları: {e(grade_summary(group))}. Her örneğin künyesi, kaynağı ve "
             "Türkiye'de nasıl uygulanabileceği kendi bölümünde.")
    head = page_head(eyebrow, name, stand)
    name_for_title = "Şüpheli iddialar" if slug == "tartismali" else name
    write_page(niche_href(slug), active=niche_href(slug), title=name_for_title,
               description=f"{desc} {len(group)} örnek.", head_html=head,
               body_html="\n".join(body), rows=rows)


def build_index(rows, by_niche):
    total = len(rows)
    disputed = sum(1 for r in rows if r["evidence_grade"] == "X")
    superseded = sum(1 for r in rows if r["status"].startswith("superseded"))
    catalogable = total - disputed - superseded
    counts = {g: sum(1 for r in rows if r["evidence_grade"] == g) for g, _, _ in GRADES}

    stand = (f"İnsanların ve işletmelerin yapay zekâ ile hangi küçük işlere <strong>gerçekten "
             f"para ödediğini</strong> derleyen {catalogable} örneklik arşiv. Her örneğin yanında "
             "ne kadar güvenilir olduğu yazıyor: hangisinin kodu açıkta duruyor, hangisi sadece "
             "anlatan kişinin kendi beyanı — ikisi birbirine karıştırılmıyor.")
    head = page_head("Neyin kanıtlı, neyin iddia olduğu ayrılmış arşiv · 2026", SITE, stand)

    o = ['<div class="col">']
    o.append("<h2>Yanlarındaki harf ne demek?</h2>")
    o.append('<dl class="legend">')
    for g, title, desc in GRADES:
        o.append(f'<div><dt><span class="chip g-{g}">{g}</span> {e(title)}</dt>'
                 f"<dd>{e(desc)}</dd></div>")
    o.append("</dl>")

    o.append('<details class="glossary"><summary>Sayfada geçen birkaç terim</summary><dl>')
    for term, meaning in GLOSSARY:
        o.append(f"<div><dt>{e(term)}</dt><dd>{e(meaning)}</dd></div>")
    o.append("</dl></details>")

    o.append('<div class="meter-block">')
    o.append(f'<span class="meter-total">{catalogable}<span>arşivlenmiş örnek · ayrıca {disputed} '
             f"şüpheli ve {superseded} eski kayıt (A006'ya taşındı) · toplam {total} satır</span></span>")
    o.append('<div class="meter" role="img" aria-label="'
             + e(", ".join(f"{g} harfi: {counts[g]} örnek" for g, _, _ in GRADES)) + '">')
    for g, title, _ in GRADES:
        pct = counts[g] / total * 100
        label = f"{g} · {counts[g]}" if pct > 7 else (g if pct > 2.5 else "")
        a_title = f"{title}: {counts[g]} örnek"
        o.append(f'<i class="s-{g}" style="width:{pct:.4f}%" title="{e(a_title)}">{label}</i>')
    o.append("</div>")
    o.append('<div class="meter-key">')
    for g, title, _ in GRADES:
        o.append(f'<span><i class="dot s-{g}"></i> <b class="mono">{g}</b> {e(title)} — {counts[g]}</span>')
    o.append("</div></div>")

    o.append('<h2 style="margin-top:44px">Hangi iş kolu ilgini çekiyor?</h2>')
    o.append('<p class="standfirst" style="margin-bottom:2px">Örnekler, satılan işin türüne göre '
             "ayrıldı. Bir kutuya tıkladığında o iş kolunun kendi sayfası açılır: oradaki her "
             "örneğin tam anlatımı, künyesi, nelere dikkat edilmesi gerektiği ve Türkiye'de nasıl "
             "uygulanabileceği yazıyor. Hepsini birden arayıp süzmek istersen "
             f'<a href="{ALL_CASES}">bütün örnekler</a> sayfasına git.</p>')
    o.append('<div class="niches">')
    for slug, order, name, desc in NICHES:
        group = by_niche.get(slug, [])
        if not group:
            continue
        o.append(f'<a class="niche" href="{niche_href(slug)}">')
        o.append(f'<span class="niche-top"><span class="niche-name">{e(name)}</span>'
                 f'<span class="niche-n">{len(group)}</span></span>')
        o.append(f'<span class="niche-desc">{e(desc)}</span>')
        o.append(f'<span class="niche-bar">{grade_bar(group)}</span>')
        o.append("</a>")
    o.append("</div>")

    o.append('<h2 style="margin-top:44px">Bu sayfa neye göre hazırlandı?</h2>')
    o.append('<p class="standfirst">Burası bir kazanç vaadi değil, bir araştırma kaydı. Tek bir '
             "ekran görüntüsü kanıt sayılmıyor. Bir örneğin arşive girmesi için sırasıyla şunlar "
             "aranıyor: net bir müşteri problemi, çalışan sistemin anlatımı, elde edilen ticari "
             "sonuç, işin kaynak kodu, o kodun geçmişi ve lisansı. Ölçütlerin tamamı "
             f'<a href="{POLICY}">bir örnek arşive nasıl giriyor?</a> sayfasında.</p>')
    o.append('<div class="disclaimer"><p><strong>Rakamlar hakkında.</strong> Sayfadaki tutarların '
             "neredeyse tamamı, işi yapan kişilerin kendi beyanı. Hiçbiri bağımsız olarak "
             "denetlenmedi.</p><p>Ayrıca birbirine benzeyen ama aynı olmayan dört şey ayrı "
             "tutuluyor: işi yapana ödenen ücret, üründen gelen gelir, müşterinin tasarrufu ve "
             "başka ticari sonuçlar — her örnekte F/R/S/V harfiyle işaretli.</p><p>Son olarak: bir "
             "kodun GitHub'da herkese açık olması, onu kopyalayıp kendi adına kullanma izni "
             "vermez.</p></div>")
    o.append(page_footer())
    o.append("</div>")

    return write_page(HOME, active=HOME, title=SITE,
                      description=("Yapay zekâyla para kazanıldığı bildirilen "
                                   f"{catalogable} gerçek örnek. Her birinin yanında ne kadar "
                                   "güvenilir olduğu yazıyor: hangisinin kodu açıkta, hangisi "
                                   "sadece anlatanın kendi beyanı."),
                      head_html=head, body_html="\n".join(o), rows=rows)


def build_all_cases(rows, by_niche):
    stand = (f"Arşivdeki {len(rows)} örneğin tamamı tek listede. Yazarak ara, ya da güvenilirlik "
             "harfine, iş koluna, paranın nereden geldiğine ve Türkiye'ye uygunluğuna göre süz. "
             "Bir örneğin başlığına tıkladığında, o örneğin iş kolu sayfasındaki tam anlatımına "
             "gidersin.")
    head = page_head("Arama ve süzme", "Bütün örnekler", stand, wide=True)

    o = ['<div class="col col-wide">']
    o.append('<div class="filters"><div class="filter-row">')
    o.append('<input class="search" id="q" type="search" '
             'placeholder="Ara: iş adı, sektör, kullanılan araç…" '
             'aria-label="Örnekler arasında ara">')
    o.append('<select id="f-niche" aria-label="İş kolu"><option value="">Bütün iş kolları</option>')
    for slug, _, name, _ in NICHES:
        if by_niche.get(slug):
            o.append(f'<option value="{e(slug)}">{e(name)}</option>')
    o.append("</select>")
    o.append('<select id="f-grade" aria-label="Ne kadar güvenilir">'
             '<option value="">Güvenilirlik: hepsi</option>')
    for g, title, _ in GRADES:
        o.append(f'<option value="{g}">{g} — {e(title)}</option>')
    o.append("</select>")
    o.append('<select id="f-rev" aria-label="Para nereden geliyor">'
             '<option value="">Para nereden geliyor: hepsi</option>')
    for code, name, _ in REVENUE:
        o.append(f'<option value="{code}">{code} — {e(name)}</option>')
    o.append("</select>")
    o.append('<select id="f-tr" aria-label="Türkiye\'ye uygunluk">'
             '<option value="">Türkiye\'ye uygunluk: hepsi</option>')
    for val, name in SELLABILITY:
        o.append(f'<option value="{e(val)}">Türkiye\'ye uygunluk: {e(name)}</option>')
    o.append("</select>")
    o.append('<button class="btn" type="button" id="reset">Sıfırla</button>')
    o.append("</div>")
    o.append('<p class="count" id="count" role="status"></p>')
    o.append("</div>")
    o.append('<div id="results"></div>')
    o.append(page_footer())
    o.append("</div>")

    write_page(ALL_CASES, active=ALL_CASES, title="Bütün örnekler",
               description=f"Arşivdeki {len(rows)} örneğin tamamı: arayıp süzülebilir liste.",
               head_html=head, body_html="\n".join(o), rows=rows,
               extra_js='<script src="vakalar.js"></script>')


def build_doc_page(name, src, *, eyebrow, title, standfirst, description, rows, source_label):
    _, preamble, sections = read_markdown(src)
    where = src.name
    body = ['<div class="col"><div class="prose">']
    intro = md_blocks(relink(preamble), f"{where} / giriş", base_level=2)
    if intro:
        body.append(intro)
    for section in sections:
        heading = section["heading"]
        if section["case_id"]:
            heading = f'{section["case_id"]} — {heading}'
        body.append(f'<h2 id="{e(section["case_id"])}">{md_inline(heading)}</h2>'
                    if section["case_id"] else f"<h2>{md_inline(heading)}</h2>")
        body.append(md_blocks(relink(section["lines"]), where, base_level=2))
    body.append("</div>")
    body.append(page_footer([(source_label, f"{BLOB}/{src.relative_to(ROOT).as_posix()}")]))
    body.append("</div>")
    write_page(name, active=name, title=title, description=description,
               head_html=page_head(eyebrow, title, standfirst),
               body_html="\n".join(body), rows=rows)


# ── scripts ─────────────────────────────────────────────────────────────────
SHARED_JS = """
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
"""

CASES_JS = """
const NICHE_NAMES = __NICHES__;
const CASES = __CASES__;
const GRADE_TITLE = __GRADETITLE__;
const REV_TITLE = __REVTITLE__;
const TR_LABEL = __TRLABEL__;

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

function rowHTML(c){
  const tags = [];
  if(c.amount) tags.push(`<span class="tag money" title="${esc(REV_TITLE[c.rev]||"Bildirilen sonuç")}">${esc(c.amount)}</span>`);
  else if(c.result) tags.push(`<span class="tag">${esc(c.result)}</span>`);
  if(c.work) tags.push(`<span class="tag">${esc(c.work)}</span>`);
  if(c.stack) tags.push(`<span class="tag">${esc(c.stack)}</span>`);
  tags.push(`<span class="tag" title="Türkiye'de satması ne kadar kolay olur — kaba bir tahmin, garanti değil">Türkiye'ye uygunluk: ${esc(TR_LABEL[c.tr]||c.tr)}</span>`);

  return `<article class="row">
    <div class="row-id">
      <span class="chip g-${c.grade}" title="${esc(GRADE_TITLE[c.grade])}">${c.grade}</span>
      <span class="mono">${esc(c.id)}</span>
    </div>
    <div>
      <h3><a href="${esc(c.href)}">${esc(c.title)}</a></h3>
      <p>${esc(c.summary)}</p>
      <div class="tags">${tags.join("")}</div>
    </div>
  </article>`;
}

function render(){
  const hits = CASES.filter(matches);
  $("count").innerHTML = hits.length === CASES.length
    ? `<b>${CASES.length}</b> örneğin tamamı gösteriliyor.`
    : `<b>${hits.length}</b> örnek eşleşti · toplam ${CASES.length} arasından.`;

  if(!hits.length){
    $("results").innerHTML = `<p class="empty">Bu seçimlerle eşleşen örnek yok. Filtreleri gevşetmeyi deneyin.</p>`;
    return;
  }
  const groups = new Map();
  for(const c of hits){
    if(!groups.has(c.niche)) groups.set(c.niche, []);
    groups.get(c.niche).push(c);
  }
  let out = "";
  for(const [slug, name, href] of NICHE_NAMES){
    const g = groups.get(slug);
    if(!g) continue;
    out += `<section class="group"><h2><a href="${esc(href)}">${esc(name)}</a><em>${g.length} örnek</em></h2>${g.map(rowHTML).join("")}</section>`;
  }
  $("results").innerHTML = out;
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

render();
"""


def build_cases_js(rows):
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
            "href": case_href(r), "hay": hay,
        })
    niche_names = [[slug, name, niche_href(slug)] for slug, _, name, _ in NICHES]
    js = CASES_JS
    js = js.replace("__NICHES__", json.dumps(niche_names, ensure_ascii=False))
    js = js.replace("__CASES__", json.dumps(payload, ensure_ascii=False, separators=(",", ":")))
    js = js.replace("__GRADETITLE__", json.dumps(GRADE_TITLE, ensure_ascii=False))
    js = js.replace("__REVTITLE__", json.dumps(REV_TITLE, ensure_ascii=False))
    js = js.replace("__TRLABEL__", json.dumps(TR_LABEL, ensure_ascii=False))
    return js.strip() + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fragment", type=Path, help="also write a headless copy of the front page")
    args = ap.parse_args()

    rows = load()
    by_niche = {}
    for r in rows:
        by_niche.setdefault(r["niche"], []).append(r)

    OUT.mkdir(exist_ok=True)
    (OUT / "wiki.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    (OUT / "wiki.js").write_text(SHARED_JS.strip() + "\n", encoding="utf-8")
    (OUT / "vakalar.js").write_text(build_cases_js(rows), encoding="utf-8")

    head, body = build_index(rows, by_niche)
    build_all_cases(rows, by_niche)

    ordered = [slug for slug, _, _, _ in NICHES if by_niche.get(slug)]
    for i, slug in enumerate(ordered):
        prev = nxt = None
        if i:
            p = ordered[i - 1]
            prev = (niche_href(p), NICHE_BY_SLUG[p][1])
        if i + 1 < len(ordered):
            n = ordered[i + 1]
            nxt = (niche_href(n), NICHE_BY_SLUG[n][1])
        build_niche_page(slug, rows, by_niche, (prev, nxt))

    build_doc_page(
        JACOBO, ENC / "A006-JACOBO-DEVICE-REPAIR.md",
        eyebrow="Arşivin en sağlam tek örneği", title="A006 — Jacobo cihaz tamiri",
        standfirst="Arşivde <strong>hem müşteri kanıtı hem de kodu</strong> aynı anda doğrulanmış "
                   "örneklerin en ayrıntılısı. Bu sayfa, bir vakanın A harfini nasıl hak ettiğini "
                   "adım adım gösteriyor.",
        description="Arşivin en sağlam örneği: WhatsApp ve telefon trafiğini yöneten n8n sistemi, "
                    "doğrulanmış kaynak koduyla birlikte.",
        rows=rows, source_label="Bu sayfanın kaynak metni")

    build_doc_page(
        PATTERNS, ENC / "DESENLER.md",
        eyebrow="Arşiv", title="Örneklerden çıkan ortak dersler",
        standfirst="Tek tek örneklerden değil, <strong>örnek gruplarının tamamından</strong> çıkan "
                   "dersler. Hangi işin neden para kazandırdığına dair tekrar eden desenler.",
        description="Arşivdeki örnek gruplarının tamamından çıkan ortak dersler ve tekrar eden desenler.",
        rows=rows, source_label="Bu sayfanın kaynak metni")

    build_doc_page(
        POLICY, ROOT / "RESEARCH_POLICY.md",
        eyebrow="Ölçütler", title="Bir örnek arşive nasıl giriyor?",
        standfirst="A, B, C ve X harflerinin tam karşılığı; bir iddianın kanıt sayılması için neyin "
                   "arandığı; ve <strong>başkasının kodunun neden buraya kopyalanmadığı</strong>.",
        description="Kanıt dereceleri, gelir etiketleri ve lisans kuralları — arşivin kural kitabı.",
        rows=rows, source_label="Kural kitabının kaynak metni")

    pages = sorted(p.name for p in OUT.glob("*.html"))
    print(f"wrote {len(pages)} pages + wiki.css/wiki.js/vakalar.js into "
          f"{OUT.relative_to(ROOT)}/ ({len(rows)} cases)")

    if args.fragment:
        args.fragment.parent.mkdir(parents=True, exist_ok=True)
        args.fragment.write_text(f"{head}\n{body}\n", encoding="utf-8")
        print(f"wrote {args.fragment} (fragment)")


if __name__ == "__main__":
    main()
