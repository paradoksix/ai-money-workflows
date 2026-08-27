# AI Money Workflows

Bu repo, 2025–2026 döneminde **gerçek müşteri / gelir / ticari sonuç bildirilen** AI otomasyon ve AI-destekli yazılım işlerini izlemek için hazırlanmıştır.

Amaç mümkün olduğunca çok “AI projesi” biriktirmek değil; **ticari vaka → kaynak → exact repo/kod → commit → lisans → Türkiye'de uygulanabilirlik** zincirini mümkün olduğunca izlenebilir tutmaktır.

## Nereden başlamalı?

| Ne istiyorsun | Nereye git |
|---|---|
| **Gezinmek, filtrelemek, bir niş seçmek** | **[Atlas web sayfası](docs/index.html)** — arama + niş/kanıt/gelir tipi/TR filtreleri |
| Nişleri okumak | [`ENCYCLOPEDIA.md`](ENCYCLOPEDIA.md) — 16 nişlik indeks |
| Kesişen dersler | [`encyclopedia/DESENLER.md`](encyclopedia/DESENLER.md) |
| Kanıt standardı | [`RESEARCH_POLICY.md`](RESEARCH_POLICY.md) |
| Veriyi analiz etmek | [`data/cases.csv`](data/cases.csv) — 124 kaydın tamamı |
| Kaynak avına katılmak | [`research_queue.csv`](research_queue.csv) + [`research/`](research/) |

Ansiklopedi şu anda **122 kataloglanabilir vaka + 1 X-seviyesi tartışmalı vaka** içeriyor; her vakada A/B/C/X kanıt derecesi, ücret/gelir/tasarruf/değer ayrımı, stack, riskler ve **Türkiye'den düşük maliyet/açık kaynak ağırlıklı nasıl uygulanabileceğine dair kısa önizleme** var.

Tek bir ürün geliştirmeye odaklanan build dalgası şu aşamada **duraklatılmıştır**. Projenin mevcut amacı, yapmaya değer AI gelir işlerinin olabildiğince geniş ve kanıt dereceli haritasını çıkarmaktır.

### Web sayfasını açmak

`docs/index.html` tek başına çalışan bir dosyadır; yerelde çift tıklayarak açabilirsiniz. GitHub Pages'te yayınlamak için repo **Settings → Pages → Source: `main` / `/docs`** yeterlidir. Sayfa `data/cases.csv`'den üretilir:

```bash
python3 scripts/build_site.py     # docs/index.html'i yeniden üret
```

## Son araştırma dalgası

- Altın vakalar için derin kaynak avı yapıldı: `research/GOLDEN-CASES-DEEP-DIVE-2026-08-24.md`, ikinci tur: `research/GOLDEN-CASES-DEEP-DIVE-2026-08-26.md`.
- Eski **C027 Device Repair WhatsApp + Voice Agent**, exact production repo bulunmasıyla **A006** seviyesine yükseltildi ve kendi satırıyla kataloglandı.
- İkinci araştırma turunda (2026-08-26) `catalog.csv`'deki 14 satırlık CSV virgül-kaçışı hatası düzeltildi ve 9 açık golden-case ipucu (C001–C008, C018) yeniden kovalandı; hiçbiri yükselmedi ama C003/C008 için yeni dolaylı sinyaller kaydedildi.
- **Ansiklopedi nişe göre yeniden düzenlendi.** Sekiz "cilt" dosyası dağıtılıp vakalar 16 niş dosyasına taşındı; ciltlerin sonundaki sentez bölümleri `encyclopedia/DESENLER.md` altında toplandı.
- **`data/cases.csv` eklendi:** 124 kaydın tamamı ilk kez makine-okunur hâlde. Daha önce vakaların yalnızca 42'si `catalog.csv`'deydi, 82'si sadece düz metindi.
- **`docs/index.html` eklendi:** filtrelenebilir atlas sayfası.

## Repo yapısı

**Okuma katmanı**

- `ENCYCLOPEDIA.md` — niş indeksi ve kanıt sisteminin açıklaması.
- `encyclopedia/nis-01…16-*.md` — 16 niş dosyası; her vakanın tam anlatımı, riskleri ve Türkiye uyarlaması.
- `encyclopedia/DESENLER.md` — vaka gruplarının tamamından çıkan kesişen dersler.
- `encyclopedia/A006-JACOBO-DEVICE-REPAIR.md` — en güçlü tek vakanın ayrıntılı kartı.
- `encyclopedia/APPENDIX-X-DISPUTED.md` — X-seviyesi tartışmalı vakalar.

**Veri katmanı**

- `data/cases.csv` — 124 kaydın tamamı: niş, kanıt derecesi, gelir tipi, tutar, stack, zorluk, TR uygunluğu, kaynak/repo/commit ve özet.
- `catalog.csv` — **pinned kaynaklı çekirdek** (42 kayıt): upstream repo + doğrulanmış commit taşıyan daha sıkı alt küme.
- `research_queue.csv` — exact kaynağı hâlâ bulunamamış yüksek değerli vakaların araştırma kuyruğu.
- `sources.csv` — ilk kaynak indeksinin geriye dönük kopyası.

**Araç katmanı**

- `docs/index.html` — üretilmiş atlas sayfası (elle düzenlenmez).
- `scripts/build_site.py` — `data/cases.csv`'den sayfayı üretir; deterministiktir.
- `scripts/validate_cases.py` — `cases.csv` şeması + `catalog.csv` ile alan uyumu + her vakanın gerçekten yazıldığı yerde olduğu kontrolü.
- `scripts/validate_catalog.py` — çekirdek katalog tutarlılık kontrolü.
- `clone_originals.ps1` / `clone_originals.sh` — doğrulanmış upstream repoları sabit commit'e pinleyerek çeker (A006 dâhil).
- `clone_disputed.ps1` / `clone_disputed.sh` — tartışmalı örnekleri bilinçli olarak ayrı çeker.

**Strateji notları**

- `RESEARCH_POLICY.md` — A/B/C/X kanıt standardı ve lisans politikası.
- `TURKIYE_OPPORTUNITIES.md` — yerel nişlerin satış/demonstrasyon açıları.
- `BUILD_SHORTLIST.md` — önceki build kısa listesi; araştırma aşamasında aktif geliştirme planı değildir.

## Kanıt seviyeleri

- **A:** belirli ticari/operasyonel vaka + vakaya doğrudan bağlı exact GitHub repo/workflow.
- **B:** açık çalışan kaynak/JSON + güçlü ticari üretici veya marketplace bağlamı; fakat exact workflow'un ayrıca ne kadar kazandırdığı tam kanıtlı değil.
- **C:** ücretli müşteri, gelir, tasarruf veya ölçülebilir ticari sonuç güçlü; exact public kaynak repo kapalı, eksik veya bulunamadı.
- **X:** gelir iddiası var fakat promosyon, çıkar çatışması veya başka ciddi şüphe bulunuyor.

Gelir rakamları birbirine karıştırılmaz:

- **F:** freelancer/hizmet sağlayıcının aldığı ücret
- **R:** ürün/SaaS/app geliri
- **S:** müşterinin tasarrufu
- **V:** kampanya değeri, booked call, impression, geri kazanılan alacak veya operasyonel değer gibi ticari sonuç

## A — Doğrulanmış ticari/operasyonel vaka + exact GitHub

Altı A-seviyesi vakanın repo/commit özeti. Tam anlatımları için ilgili niş dosyalarına bakın: [B2B satış & lead](encyclopedia/nis-02-b2b-satis-lead.md) (A002, A003, A005), [video & görsel](encyclopedia/nis-01-video-gorsel-produksiyon.md) (A001), [içerik & sosyal medya](encyclopedia/nis-05-icerik-sosyal-medya.md) (A004), [yerel işletme & saha servisi](encyclopedia/nis-11-yerel-isletme-saha-servisi.md) (A006).

### A001 — AI Creative Director / moda kampanyası
- Repo: https://github.com/sirlifehacker/Nano-Banana-Pro-Creative-Director
- Commit: `1c82b35f1db29e9f0ed35f5e0680148241a371b5`
- Vaka: `$9K campaign`; bunun freelancer net ücreti olduğu kanıtlanmıyor.

### A002 — LinkedIn Jobs + Decision Maker Research
- Repo: https://github.com/sirlifehacker/n8n-automations
- Commit: `dcab49176024e410a1cc555ea8bda3f21f4c6f1f`
- Vaka: ilk staffing müşterisinin ardından birden fazla müşterinin aynı sistemi istediği bildiriliyor.

### A003 — B2B Lead Search Engine
- Repo: https://github.com/sirlifehacker/lead-gen-hacker
- Commit: `9ed891f4bc2666f19941ea8c03841555c4812b66`
- Vaka: B2B girişimcilerin varyantları için geliştiriciyi tuttuğu bildiriliyor.

### A004 — Social Story Scraper
- Repo: https://github.com/sirlifehacker/social-story-scraper
- Commit: `69de2889cbe8a80124581d5f5b2abede4d221b3f`
- Vaka: ~2.9M impression ve 10+ high-ticket inbound lead bildiriliyor.

### A005 — Insurance Lawyer Lead Gen Automation
- Repo: https://github.com/lucaswalter/n8n-ai-automations
- Exact workflow: `deal_breakdown_lawyer_lead_gen.json`
- Commit: `08e33b6d589789bc06957611cf932d3602b81117`
- Vaka: Austin'deki butik hukuk firmasına `$1,800` ücretle satıldığı bildiriliyor; geliştirici standart teklifini `$2,500 build + $400/month` olarak açıklıyor.

### A006 — Jacobo Device Repair WhatsApp + Voice AI Agent
- Case card: `encyclopedia/A006-JACOBO-DEVICE-REPAIR.md`
- Repo: https://github.com/santifer/jacobo-workflows
- Commit: `b26601dde3f35edddf3690bd2f5a6656420df073`
- Exact source: 7 sanitised production n8n workflow.
- Bildirilen sonuç: ~%90 self-service, ~80 saat/ay otomasyon, `<30s` response, `<€200/ay` altyapı.
- Gelir semantiği: bağımsız freelance satış fiyatı yok; sistem işletmenin operasyonel varlığı olarak kullanılmış ve işletmeyle birlikte devredilmiş.
- Repo metadata'sında açık root lisans görünmüyor.

## Araştırmada özellikle kovalanacak C vakaları

1. C004 — Property-management vertical / Powerprozesse
2. C003 — 50K ürün katalog overhaul (`conor-is-my-name` doğrulanmamış aday)
3. C002 — Japon Google Ads invoice processor
4. C006 — 115+ workflow monitoring
5. C005 — Bookkeeping process automation
6. C001 — Ship manager lead capture
7. C007 — 50K Shopify inventory shock absorber
8. C008 — Bookstore WhatsApp order assistant
9. C018 — $5K tutoring operations system
10. C029 — Offline university RAG
11. C076 — Medical-device expiry/spoilage automation

Bunların ayrıntıları `ENCYCLOPEDIA.md` ve derin araştırma raporları (2026-08-24, 2026-08-26) üzerinden izlenir.

## Lisans notu

Public GitHub reposu otomatik olarak yeniden dağıtım veya yeniden lisanslama izni vermez. Açık lisansı bulunmayan upstream kodları bu repoya kopyalanmaz; orijinal repo, Git geçmişi ve sabit commit korunarak doğrudan upstream'den referanslanır/çekilir. Private/paid kaynaklar araştırma amacıyla kayda alınabilir fakat kopyalanmaz.
