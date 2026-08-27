# AI Money Workflows

Bu repo, 2025–2026 döneminde **gerçek müşteri / gelir / ticari sonuç bildirilen** AI otomasyon ve AI-destekli yazılım işlerini izlemek için hazırlanmıştır.

Amaç mümkün olduğunca çok “AI projesi” biriktirmek değil; **ticari örnek → kaynak → kodun kendisi → sürüm numarası → lisans → Türkiye'de uygulanabilirlik** zincirini mümkün olduğunca izlenebilir tutmaktır.

## Nereden başlamalı?

| Ne istiyorsun | Nereye git |
|---|---|
| **Gezinmek, filtrelemek, bir iş kolu seçmek** | **[Atlas web sayfası](docs/index.html)** — arama + iş kolu, güvenilirlik, gelir türü ve Türkiye filtreleri |
| İş kollarını okumak | [`ENCYCLOPEDIA.md`](ENCYCLOPEDIA.md) — 16 iş kolu |
| Ortak dersler | [`encyclopedia/DESENLER.md`](encyclopedia/DESENLER.md) |
| Neyin nasıl doğrulandığı | [`RESEARCH_POLICY.md`](RESEARCH_POLICY.md) |
| Veriyi analiz etmek | [`data/cases.csv`](data/cases.csv) — 124 kaydın tamamı |
| Kaynak aramaya katılmak | [`research_queue.csv`](research_queue.csv) + [`research/`](research/) |

Ansiklopedi şu anda **122 arşivlenmiş örnek + 1 şüpheli iddia** içeriyor; her örnekte A/B/C/X güvenilirlik harfi, ücret/gelir/tasarruf/değer ayrımı, kullanılan araçlar, riskler ve **Türkiye'den düşük maliyet/açık kaynak ağırlıklı nasıl uygulanabileceğine dair kısa önizleme** var.

Tek bir ürün geliştirmeye odaklanan build dalgası şu aşamada **duraklatılmıştır**. Projenin mevcut amacı, yapmaya değer AI gelir işlerinin olabildiğince geniş, güvenilirliği işaretlenmiş haritasını çıkarmaktır.

### Web sayfasını açmak

`docs/index.html` tek başına çalışan bir dosyadır; yerelde çift tıklayarak açabilirsiniz. GitHub Pages'te yayınlamak için repo **Settings → Pages → Source: `main` / `/docs`** yeterlidir. Sayfa `data/cases.csv`'den üretilir:

```bash
python3 scripts/build_site.py     # docs/index.html'i yeniden üret
```

## Son araştırma dalgası

- Altın vakalar için derin kaynak avı yapıldı: `research/GOLDEN-CASES-DEEP-DIVE-2026-08-24.md`, ikinci tur: `research/GOLDEN-CASES-DEEP-DIVE-2026-08-26.md`.
- Eski **C027 Device Repair WhatsApp + Voice Agent**, canlı ortamdaki kaynak kodu bulunduğu için **A006** seviyesine yükseltildi ve kendi satırıyla kataloglandı.
- İkinci araştırma turunda (2026-08-26) `catalog.csv`'deki 14 satırlık CSV virgül-kaçışı hatası düzeltildi ve 9 açık golden-case ipucu (C001–C008, C018) yeniden kovalandı; hiçbiri yükselmedi ama C003/C008 için yeni dolaylı sinyaller kaydedildi.
- **Arşiv iş koluna göre yeniden düzenlendi.** Sekiz "cilt" dosyası dağıtılıp örnekler 16 iş kolu dosyasına taşındı; ciltlerin sonundaki sentez bölümleri `encyclopedia/DESENLER.md` altında toplandı.
- **`data/cases.csv` eklendi:** 124 kaydın tamamı ilk kez makine-okunur hâlde. Daha önce vakaların yalnızca 42'si `catalog.csv`'deydi, 82'si sadece düz metindi.
- **`docs/index.html` eklendi:** filtrelenebilir atlas sayfası.

## Repo yapısı

**Okuma katmanı**

- `ENCYCLOPEDIA.md` — iş kolları listesi ve harflerin ne anlama geldiği.
- `encyclopedia/nis-01…16-*.md` — 16 iş kolu dosyası; her örneğin tam anlatımı, dikkat edilmesi gerekenler ve Türkiye uyarlaması.
- `encyclopedia/DESENLER.md` — örnek gruplarının tamamından çıkan ortak dersler.
- `encyclopedia/A006-JACOBO-DEVICE-REPAIR.md` — en sağlam tek örneğin ayrıntılı kartı.
- `encyclopedia/APPENDIX-X-DISPUTED.md` — X seviyesindeki şüpheli iddialar.

**Veri katmanı**

- `data/cases.csv` — 124 kaydın tamamı: iş kolu, güvenilirlik harfi, gelir türü, tutar, kullanılan araçlar, zorluk, Türkiye'ye uygunluk, kaynak bağlantıları ve özet.
- `catalog.csv` — **kaynağı sabitlenmiş çekirdek** (42 kayıt): kaynak kodu deposu ve doğrulanmış sürüm numarası taşıyan daha sıkı alt küme.
- `research_queue.csv` — kaynak kodu hâlâ bulunamamış, değerli örneklerin araştırma listesi.
- `sources.csv` — ilk kaynak indeksinin geriye dönük kopyası.

**Araç katmanı**

- `docs/index.html` — üretilmiş atlas sayfası (elle düzenlenmez).
- `scripts/build_site.py` — `data/cases.csv`'den sayfayı üretir; deterministiktir.
- `scripts/validate_cases.py` — `cases.csv` yapısı, `catalog.csv` ile alan uyumu ve her örneğin gerçekten yazıldığı yerde olduğu kontrolü.
- `scripts/validate_catalog.py` — çekirdek katalog tutarlılık kontrolü.
- `clone_originals.ps1` / `clone_originals.sh` — doğrulanmış kaynak depolarını sabit bir sürüme kilitleyerek indirir (A006 dâhil).
- `clone_disputed.ps1` / `clone_disputed.sh` — şüpheli örnekleri bilerek ayrı indirir.

**Strateji notları**

- `RESEARCH_POLICY.md` — A/B/C/X güvenilirlik ölçütleri ve lisans politikası.
- `TURKIYE_OPPORTUNITIES.md` — yerel iş kollarının satış ve tanıtım açıları.
- `BUILD_SHORTLIST.md` — önceki build kısa listesi; araştırma aşamasında aktif geliştirme planı değildir.

## Yanlarındaki harf ne demek?

- **A — Müşteri kanıtı + kodu açık.** İşin gerçek bir müşteriye satıldığı ve tam olarak hangi kodla yapıldığı, ikisi birden doğrulandı.
- **B — Kodu açık, kazancı belirsiz.** Kod gerçek ve çalışıyor; ama tam olarak bu işin para kazandırdığı ayrıca gösterilmedi.
- **C — Para kazandırmış, kodu yok.** Ödeme yapan müşteri, gelir ya da tasarruf anlatımı güçlü; ama işin kodu paylaşılmamış veya bulunamadı.
- **X — Şüpheli.** Kazanç iddiasında gizli reklam ya da çıkar çatışması şüphesi var.

Rakamlarda dört ayrı şey birbirine karıştırılmaz:

- **F:** işi yapana ödenen ücret
- **R:** satılan üründen veya abonelikten gelen gelir
- **S:** müşterinin kazandığı tasarruf
- **V:** kampanya değeri, alınan randevu, görüntülenme, tahsil edilen alacak gibi başka ticari sonuçlar

## A — Müşteri kanıtı da kodu da doğrulanmış örnekler

Altı A örneğinin kaynak kodu ve sürüm özeti. Tam anlatımları için ilgili iş kolu dosyalarına bakın: [şirketlere satış](encyclopedia/nis-02-b2b-satis-lead.md) (A002, A003, A005), [video ve görsel](encyclopedia/nis-01-video-gorsel-produksiyon.md) (A001), [içerik ve sosyal medya](encyclopedia/nis-05-icerik-sosyal-medya.md) (A004), [mahalle esnafı ve saha servisi](encyclopedia/nis-11-yerel-isletme-saha-servisi.md) (A006).

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
- Doğrulanan dosya: `deal_breakdown_lawyer_lead_gen.json`
- Commit: `08e33b6d589789bc06957611cf932d3602b81117`
- Vaka: Austin'deki butik hukuk firmasına `$1,800` ücretle satıldığı bildiriliyor; geliştirici standart teklifini `$2,500 build + $400/month` olarak açıklıyor.

### A006 — Jacobo Device Repair WhatsApp + Voice AI Agent
- Case card: `encyclopedia/A006-JACOBO-DEVICE-REPAIR.md`
- Repo: https://github.com/santifer/jacobo-workflows
- Commit: `b26601dde3f35edddf3690bd2f5a6656420df073`
- Kaynak: gizli bilgileri temizlenmiş, canlı ortamda çalışmış 7 n8n iş akışı.
- Bildirilen sonuç: müşterilerin ~%90'ı kendi kendine hallediyor, ayda ~80 saat kazanç, 30 saniyenin altında yanıt, ayda €200'den az altyapı.
- Gelir semantiği: bağımsız freelance satış fiyatı yok; sistem işletmenin operasyonel varlığı olarak kullanılmış ve işletmeyle birlikte devredilmiş.
- Repo metadata'sında açık root lisans görünmüyor.

## Araştırmada özellikle kovalanacak C vakaları

1. C004 — Property-management vertical / Powerprozesse
2. C003 — 50K ürün katalog overhaul (`conor-is-my-name` doğrulanmamış aday)
3. C002 — Japon Google Ads invoice processor
4. C006 — 115+ iş akışını izleyen panel
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
