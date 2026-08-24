# AI Money Workflows

Bu repo, 2025–2026 döneminde **gerçek müşteri / gelir / ticari sonuç bildirilen** AI otomasyon ve AI-destekli yazılım işlerini izlemek için hazırlanmıştır.

Amaç mümkün olduğunca çok “AI projesi” biriktirmek değil; **ticari vaka → kaynak → exact repo/kod → commit → lisans → Türkiye'de uygulanabilirlik** zincirini mümkün olduğunca izlenebilir tutmaktır.

## Güncel durum

Ana katalog şu anda **41 ticari vaka** içeriyor:

- **5 × A:** ticari vaka + doğrudan ilişkili exact GitHub kaynak.
- **2 × B:** ticari bağlam + GitHub kaynak/mirror var, fakat A standardının tamamı yok.
- **33 × C:** müşteri/gelir/ROI sinyali güçlü; exact public kaynak aranıyor.
- **1 × X:** promosyon/çıkar çatışması nedeniyle tartışmalı.

`BUILD_SHORTLIST.md`, bunların içinden Türkiye'de ilk kurulacak 10 ürünü sıralar.

## Repo yapısı

- `catalog.csv` — ana katalog: iş modeli, müşteri tipi, bildirilen sonuç, kanıt derecesi, repo, commit, lisans, zorluk ve Türkiye'de satılabilirlik.
- `research_queue.csv` — C seviyesindeki 33 vakanın exact kaynak-repo arama kuyruğu.
- `BUILD_SHORTLIST.md` — Türkiye'de ilk kurulacak 10 ürün ve ilk beş build sırası.
- `TURKIYE_OPPORTUNITIES.md` — yerel nişlerin satış/demonstrasyon açıları.
- `RESEARCH_POLICY.md` — A/B/C/X kanıt standardı ve lisans politikası.
- `sources.csv` — ilk kaynak indeksinin geriye dönük kopyası.
- `clone_originals.ps1` / `clone_originals.sh` — yalnız A seviyesindeki doğrulanmış upstream repoları belirli commit'e sabitleyerek çeker.
- `clone_disputed.ps1` / `clone_disputed.sh` — tartışmalı örnekleri bilinçli olarak ayrı çeker.
- `scripts/validate_catalog.py` — katalog tutarlılık kontrolü.
- `.github/workflows/validate-catalog.yml` — catalog değişikliklerinde otomatik doğrulama.

## Kanıt seviyeleri

- **A:** belirli ticari vaka/sonuç + vakaya doğrudan bağlı exact GitHub repo.
- **B:** ticari bağlam + GitHub kaynak var; fakat workflow-bazlı gelir kanıtı, kaynak sahipliği veya orijinallik A seviyesinden zayıf.
- **C:** ücretli müşteri, gelir veya ölçülebilir ticari sonuç güçlü; exact public kaynak repo henüz bulunmadı.
- **X:** gelir iddiası var fakat promosyon, çıkar çatışması veya başka ciddi şüphe bulunuyor.

Ayrıntı: `RESEARCH_POLICY.md`.

## A — Doğrulanmış ticari vaka + exact GitHub

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
- Akış: dizin scrape → firma/site doğrulama → avukat profili → Gemini qualification → iletişim verisi → kişiselleştirilmiş outreach taslağı → Sheets/Docs.

## B — Kaynak var fakat A standardının tamamı yok

### B001 — Job Hacker
Exact creator repo mevcut; ancak bu belirli workflow'un ayrı ücretli satış kanıtı yok.

### B002 — Hotel High-Spender Reward Email Automation
Kaynak vakada Kanadalı otel yöneticisinin `$200` ödediği bildiriliyor. Resmî n8n template'in GitHub aynası bulundu fakat bu repo vaka yazarının orijinal deposu değil; bu nedenle A'ya yükseltilmedi.

## C — Ticari vaka güçlü, exact public kaynak aranıyor

33 C-vaka `research_queue.csv` içinde tek tek source-repo arama hedefleriyle tutuluyor. Öne çıkanlar:

- `$500` — kitapçı için WhatsApp sipariş/asistan sistemi.
- `€3,000` — HR automation packaged MVP.
- `$5,000` — tutoring/scheduling/WhatsApp/payment agent.
- `$700` — kahveci QR sipariş mikro-uygulaması.
- `$5,500` — üniversite için offline/local RAG chatbot.
- `$2,530` — pazarlama ajansı için AI video content agent iddiası.
- `$1,000+` — ilk Upwork n8n otomasyon işi.
- `£1,000` — UK agency Make→n8n migration + workflow contract ilk ayı.
- `$4,200 recovered` — Stripe invoice chaser sonucu bildirimi.
- `40+ booked calls/month` — daily lead finder + personalized outreach sonucu.

Kaynak kodu doğrulanmadan bunlar upstream koleksiyonuna alınmaz.

## Türkiye build dalgası

İlk sıra `BUILD_SHORTLIST.md` içinde:

1. E-ticaret katalog doktoru
2. B2B lead araştırma/zenginleştirme
3. Muhasebe/fatura ön işleme
4. Yerel işletme WhatsApp sipariş/asistan sistemi
5. Kahveci/restoran QR sipariş mikro-uygulaması
6. Emlak/site yönetimi talep triyajı
7. Klinik/ofis intake otomasyonu
8. Eğitim işletmesi scheduling + ödeme bildirim sistemi
9. E-ticaret görsel/içerik pipeline'ı
10. Automation maintenance / monitoring aboneliği

## Orijinalleri çekmek

Windows:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\clone_originals.ps1
```

Linux / macOS / WSL:

```bash
chmod +x clone_originals.sh
./clone_originals.sh
```

Scriptler A001–A005 kaynak repolarını `upstreams/` altında clone eder ve araştırmada doğrulanan commit'e checkout yapar.

## Lisans notu

Public GitHub reposu otomatik olarak yeniden dağıtım veya yeniden lisanslama izni vermez. Açık lisansı bulunmayan upstream kodları bu repoya kopyalanmaz; orijinal repo, Git geçmişi ve sabit commit korunarak doğrudan upstream'den çekilir. Private/paid kaynaklar araştırma amacıyla kayda alınabilir fakat kopyalanmaz.
