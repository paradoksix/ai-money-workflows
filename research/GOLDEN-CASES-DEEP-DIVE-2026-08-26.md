# Altın Vakalar Derin Araştırma — 2026-08-26 (İkinci Tur)

Bu rapor, `research/GOLDEN-CASES-DEEP-DIVE-2026-08-24.md` raporunun ve GitHub Issue #1 checklist'inin bıraktığı **9 açık exact-source ipucunu** yeniden kovalar: C001, C002, C003, C004, C005, C006, C007 (08-24 turunda hiç işlenmemişti), C008 ve C018.

## Sonuç özeti

- Bu turda **hiçbir vaka A/B seviyesine yükselmedi.**
- **En güçlü yeni sinyal — C003:** `github.com/conor-is-my-name` hesabı gerçek ve teknik olarak son derece uyumlu (`n8n-autoscaling` 730★, `google-maps-scraper` 324★, `crawlee-server`; LinkedIn `conorbolich` / X `@conorbolich` ile bağlı gerçek kimlik). Ancak bu hesabın orijinal Reddit gönderisinin (`r/n8n/comments/1kql6nm`) yazarı olduğu bu turda da **doğrulanamadı** — Reddit'e erişim ortam kısıtı nedeniyle mümkün olmadı (aşağıya bakın). Dolaylı/güçlü aday, doğrulanmamış.
- **C008 için olumsuz ama değerli bulgu:** `github.com/anassy1` hesabı gerçek fakat **0 public repo, bio yok**. Bu, "Linktree'den GitHub'a çıkış var mı" sorusunu kapatıyor — böyle bir çıkış yok. Temiz template hâlâ yalnız Linktree/profil üzerinden dağıtılıyor.
- **C004 Powerprozesse:** `powerprozesse.de` bağımsız olarak yeniden doğrulandı (Worms, Almanya merkezli, property-management otomasyonu, n8n + make.com, aktif işe alım). GitHub organizasyonu veya açık kaynak izi yok — kapalı kaynak teyit edildi.
- **C006 AigencyTracker:** Gerçek ürün sayfası bulundu (`aigencytracker.carrd.co`) — çok-müşterili dashboard tanımı önceki bulguyla birebir örtüşüyor. Proprietary, GitHub yok.
- **C001, C002, C005, C007, C018:** Bu turda yeni bir iz bulunamadı; genel web araması exact repo/yazar kimliği getirmedi.

### Ortam kısıtı (önemli — sonraki oturum için not)

Bu oturumda `reddit.com` (hem `www` hem `old` alt domain'i) doğrudan WebFetch için **erişilemez** durumdaydı (`EGRESS_BLOCKED` benzeri hata). Tüm Reddit kaynaklı bulgular yalnızca genel web araması (WebSearch) sonuçlarına dayanıyor; orijinal post/yorum gövdeleri bu turda doğrudan okunamadı. 2026-08-24 raporunda yalnız C018 için not edilen bu erişim sorunu, bu turda **9 vakanın tamamına** yayıldı. Reddit'e doğrudan erişimi olan bir sonraki oturum, özellikle C003 (yazar-repo eşleşmesi) ve C001/C002/C005/C007/C018 (yorumlardaki olası kaynak linkleri) için bu listeyi yeniden denemeli.

---

## C001 — Ship Manager Lead Capture

Puppeteer scraper'ın public artefact'ı veya yazar kimliği aranmaya devam edildi. Genel web araması yeni bir iz getirmedi; post flair'i zaten `Code Not Included` olarak biliniyordu. **Karar: C kalır.**

## C002 — Japanese Google Ads Invoice Processor

Hosted control panel/repo izi ve geliştirici portföy sayfası arandı. Sonuç: n8n+Claude fatura otomasyonu genel olarak yaygın bir desen (bkz. genel örnekler) fakat bu spesifik Japon reklam ajansı vakasına ait public kod veya panel bulunamadı. **Karar: C kalır.**

## C003 — 50K Product Catalog Overhaul

`conor-is-my-name` GitHub hesabı yeniden incelendi:

- Gerçek, aktif, 113 takipçili hesap; LinkedIn (`conorbolich`) ve X (`@conorbolich`) ile bağlı — anonim değil.
- Repo'ları tam olarak bu vakanın gerektirdiği altyapıyla örtüşüyor: `n8n-autoscaling` (queue-mode + puppeteer, 730★), `google-maps-scraper` (324★), `crawlee-server`, `Headful-Chrome-Remote-Puppeteer`.
- **Ama:** hiçbir repo README'si 50K ürün kataloğu, SEO/spec overhaul veya bu Reddit thread'ini (`r/n8n/comments/1kql6nm`) doğrudan referans almıyor. Reddit gönderisinin gerçek yazar kullanıcı adı bu turda doğrulanamadı (erişim kısıtı).

**Karar:** C kalır; bu, listedeki en güçlü doğrulanmamış adaydır. Sonraki adım net: Reddit erişimi olan biri post yazarının kullanıcı adını `conor-is-my-name` ile karşılaştırmalı, ya da doğrudan Reddit üzerinden yazara sorulmalı.

## C004 — Powerprozesse Property-Management Vertical

`powerprozesse.de` bağımsız kaynaklardan yeniden doğrulandı: Worms merkezli, property-management/Hausverwaltung dikeyine odaklı, n8n ağırlıklı + kısmen make.com, aktif "Automation Developer" ilanları (Glassdoor/Arbeitnow), YouTube kanalı mevcut. Somut örnek anlatımı (`hasar bildirimi → AI analiz → yükleniciye atama → kiracı bilgilendirme`) önceki bulguyla birebir aynı. GitHub organizasyonu veya açık kaynak repo bulunamadı — resmi sistem kapalı kaynak. **Karar: C kalır**, ticari süreklilik bir kez daha teyit edildi.

## C005 — Bookkeeping Process Automation

Yazar/proje kimliği ve kaynak kod için yeniden arandı; yeni bir iz bulunamadı. **Karar: C kalır.**

## C006 — Automation Monitoring Dashboard / AigencyTracker

Ürünün gerçek genel tanıtım sayfası bulundu: `aigencytracker.carrd.co` — "tüm müşterilerinizi tek panelde yönetin" tanımı, orijinal vaka ile tutarlı. Domain kayıt bilgisi (`aigencytracker.com`, Ekim 2025) ürünün gerçek/aktif olduğunu destekliyor. GitHub reposu yok — proprietary SaaS teyit edildi (thread'deki `FlowMetr` hâlâ farklı bir proje, bu vakanın exact sistemi değil). **Karar: C kalır.**

## C007 — 50K Shopify Inventory Shock Absorber

2026-08-24 raporunda hiç işlenmemiş, yalnızca Issue #1 checklist'inde açık kalmıştı — bu turda ilk kez kovalandı. Genel arama yazar kimliği veya kod bulamadı; ancak Shopify'ın kendi geliştirici forumlarında 50K–120K varyant ölçeğinde inventory-sync'in gerçek ve bilinen bir performans problemi olduğu doğrulandı (bağımsız kaynak, aynı iddiayı destekleyen teknik bağlam). Bu, iddianın **teknik olarak makul** olduğunu gösterir ama vakanın kendisini doğrulamaz. **Karar: C / needs_verification kalır**; artık en azından bir kez araştırıldığı kayıtlı.

## C008 — Bookstore WhatsApp AI Order Assistant

`github.com/anassy1` hesabı bulundu ve incelendi: hesap gerçek fakat **0 public repository, bio yok**. Temiz template'in "Linktree/profil üzerinden, GitHub değil" paylaşıldığı önceki bulgusu bu turda doğrulandı — GitHub üzerinden bir çıkış yolu olmadığı netleşti. `$500` / `$1,500` kaynak kirliliği notu (2026-08-24 raporu) geçerliliğini koruyor. **Karar: C kalır**, kaynak kirliliği notu ve şimdi de "GitHub hesabı boş" notuyla güçlendirildi.

## C018 — Tutoring Business $5K WhatsApp Automation

Orijinal Reddit thread'i ve ikincil "AI Pulse Daily" arşiv kaynağı bu turda da doğrudan bulunamadı/erişilemedi. **Karar: C kalır**, `source_revalidation_needed` durumu değişmedi.

---

# Sonraki exact-source avı (üçüncü tur için)

1. Reddit'e doğrudan erişimi olan bir oturumda tüm 9 vakanın orijinal post + yorumlarını yeniden tara (bu turun temel kısıtı buydu).
2. C003 — `conor-is-my-name`'in gerçekten `r/n8n/comments/1kql6nm` yazarı olup olmadığını doğrudan doğrula (post-history karşılaştırması veya yazara doğrudan soru).
3. C004 — Powerprozesse müşterisi tarafından yazılmış bağımsız bir public case study/yorum ara (şirketin kendi sitesi dışında).
4. C001, C002, C005 — yazar kimliği hâlâ tamamen açık; başka bir arama motoru/dil kombinasyonu (ör. Japonca kaynaklar C002 için) denenebilir.
