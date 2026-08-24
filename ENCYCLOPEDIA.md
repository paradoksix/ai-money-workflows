# AI Gelir Vakaları Ansiklopedisi

Bu bölüm, projenin başından itibaren toplanan **122 kataloglanabilir vaka + 1 tartışmalı X vakasını** tek bir araştırma ansiklopedisi altında toplar.

Amaç tek bir fikri seçip ürün geliştirmek değildir. Amaç, insanların ve işletmelerin yapay zekâ/otomasyon kullanılarak hangi küçük problemlere gerçekten para ödediğini; hangi vakaların açık kaynakla izlenebildiğini; hangilerinin yalnızca ticari self-report olduğunu; hangilerinin Türkiye'de uygulanabilir olduğunu karşılaştırmalı biçimde korumaktır.

## Kanıt sistemi

- **A — Ticari vaka + exact kaynak repo/workflow.** Aynı müşteri/gelir/operasyon vakası ile doğrudan bağlantılı kaynak kod doğrulanmıştır.
- **B — Açık çalışan workflow/repo + ticari üretici/market bağlamı.** Kod gerçektir fakat o exact workflow'un ayrı ücretli müşteri sonucu kanıtlanmamıştır ya da kaynak mirror/template niteliğindedir.
- **C — Güçlü ücretli müşteri, gelir, tasarruf veya marketplace sinyali.** Exact kaynak repo kapalıdır, bulunamamıştır veya doğrulanmamıştır.
- **X — Tartışmalı.** Gelir iddiasında promosyon, çıkar çatışması veya başka ciddi güvenilirlik problemi vardır; ana 122 sayımına dahil edilmez.

Gelir rakamlarında şu ayrım korunur:

- **F:** freelancer/hizmet sağlayıcının aldığı ücret
- **R:** ürün/SaaS/app geliri
- **S:** müşterinin bildirilen tasarrufu
- **V:** kampanya değeri, booked call, impression, geri kazanılan alacak veya operasyonel değer gibi ticari sonuç

Self-report rakamları bağımsız denetlenmiş gerçekler gibi sunulmaz.

## Sana göre uygulama önizlemeleri nasıl hazırlanıyor?

Her vakanın sonunda kısa bir **“Senin için uygulama önizlemesi”** bölümü bulunur. Bu önizleme şu çalışma profilini esas alır:

- Türkiye'den satış veya hizmet verme,
- mümkün olduğunca düşük maliyetli/açık kaynak araç kullanma,
- n8n/Sheets/yerel LLM gibi basit ve değiştirilebilir bileşenleri tercih etme,
- mevcut RTX 3060 12 GB sınıfı bilgisayarda küçük yerel modellerden yararlanabilme,
- “AI uzmanlığı” satmak yerine ölçülebilir bir işletme problemini satma,
- önce dar kapsamlı demo/pilot, sonra gerekiyorsa aylık bakım/retainer modeline geçme.

Bu önizlemeler uygulama garantisi veya gelir tahmini değildir; hangi yönden araştırılabileceğini gösteren kısa yönlendirmelerdir.

## Ciltler

### [Cilt 1 — Açık kaynakla izlenebilen çekirdek vakalar](encyclopedia/VOLUME-01-OPEN-SOURCE-CORE.md)
A001–A005 ve B001–B025. Lead intelligence, hukuk, e-ticaret kreatifleri, Gmail agent, dental voice, content repurposing, RAG, WhatsApp, CRM enrichment ve benzeri açık workflow örnekleri.

### [A006 — Jacobo Device Repair WhatsApp + Voice AI Agent](encyclopedia/A006-JACOBO-DEVICE-REPAIR.md)
Önceden C027 olan vaka exact production repo bulunmasıyla A seviyesine yükseltildi. 7 sanitised n8n workflow, doğrudan vaka sahibi bağlantısı ve pinned commit doğrulandı.

### [Cilt 2 — Operasyon, back-office ve yerel işletme: C001–C019](encyclopedia/VOLUME-02-OPERATIONS-LOCAL-BUSINESS.md)
Denizcilik lead research, fatura işleme, 50K katalog overhaul, property management, bookkeeping, monitoring, WhatsApp sipariş, HR, klinik intake, Stripe tahsilat, tutoring ve kahveci QR app gibi doğrudan işletme problemleri.

### [Cilt 3 — App, mikro-SaaS ve uzmanlık işleri: C020–C033](encyclopedia/VOLUME-03-APPS-SAAS-SPECIALIST.md)
Apple Watch uygulaması, mikro-SaaS, conversational forms, health app, Upwork otomasyon işi, Make→n8n migration, repair-shop agent, offline RAG, configurator app, bug bounty ve adversarial ML gibi daha ürün/uzmanlık ağırlıklı vakalar. C027'nin tarihsel kaydı bu ciltte görülebilir ancak kanonik derecesi artık A006'dır.

### [Cilt 4 — Marketplace otomasyon, RAG ve voice: C034–C049](encyclopedia/VOLUME-04-MARKETPLACE-AUTOMATION-RAG.md)
Fiverr/marketplace üzerinde gerçekten sipariş/review sinyali bulunan n8n, API integration, AI agents, voice receptionist, private RAG, WhatsApp qualification, omnichannel concierge ve customer-support chatbot hizmetleri.

### [Cilt 5 — Görsel, video, UGC ve faceless üretim: C050–C065](encyclopedia/VOLUME-05-CREATIVE-VIDEO-YOUTUBE.md)
AI UGC, product commercial, music video, avatar video, thumbnail, faceless YouTube prodüksiyonu ve aylık içerik paketleri.

### [Cilt 6 — AI sonrası temizlik, veri ve VA hizmetleri: C066–C075](encyclopedia/VOLUME-06-CLEANUP-DATA-VA.md)
AI logo düzeltme, Gamma/AI deck'i profesyonel PPT'ye çevirme, OCR→Excel, AI destekli VA ve voice/task assistant gibi “AI çıktılarını işe yarar son ürüne çeviren” işler.

### [Cilt 7 — Enterprise operasyon, maliyet düşürme ve yüksek-ROI: C076–C086](encyclopedia/VOLUME-07-ENTERPRISE-OPS-ROI.md)
Medikal stok expiry, D365 lisans ikamesi, okul veri workflow'ları, warehouse scan optimizasyonu, CRM sync replacement, real-estate document generation, tender research, 44-country localisation, internal Claude automation ve grant-funded custom app gibi yüksek-ROI vakaları.

### [Cilt 8 — AI-destekli özel yazılım ve dar sektör araçları: C087–C092](encyclopedia/VOLUME-08-AI-ASSISTED-CUSTOM-SOFTWARE.md)
$30K business-management web app, `$500` fitness-coach app, `$500/ay` pest-control inspection app, manufacturing recruiting lead-research ikamesi ve yüksek gelir bildiren dikey AI-assisted software örnekleri.

### [Ek X — Tartışmalı/şüpheli ticari vakalar](encyclopedia/APPENDIX-X-DISPUTED.md)
Ana kanıt standardını geçmeyen fakat araştırma izi olarak korunması gereken örnekler.

## Altın vakalar derin araştırması

👉 [2026-08-24 Altın Vakalar Derin Araştırma Raporu](research/GOLDEN-CASES-DEEP-DIVE-2026-08-24.md)

İlk derin taramada:

- **C027 → A006:** exact production repo bulundu.
- **C004 Powerprozesse:** 20→23 müşteri, işe alım ve somut property-management workflow örnekleriyle ticari kanıt güçlendi; resmi exact repo bulunmadı.
- **C008 Bookstore WhatsApp:** `$500` birincil Reddit vakası korunuyor; başka bir hesapta aynı hikâyenin `$1,500` olarak kopyalanması kaynak kirliliği/kırmızı bayrak olarak kaydedildi.
- **C018 Tutoring:** `$5K` iddiası ikincil arşiv tarafından destekleniyor fakat birincil kaynak yeniden doğrulanmalı.
- **C029 Offline University RAG:** teknik mimari ilginç; public exact code yok ve seller/promo bağlamı nedeniyle temkinli tutuluyor.

## Özellikle araştırılmaya devam edilecek altın vakalar

Exact repo, ikinci bağımsız müşteri kanıtı veya daha güçlü ekonomik doğrulama bulunması en değerli vakalar:

1. C004 — Property-management vertical / Powerprozesse
2. C003 — 50K ürün katalog overhaul
3. C002 — Japon Google Ads invoice processor
4. C006 — 115+ workflow monitoring / AigencyTracker
5. C005 — Bookkeeping process automation
6. C001 — Ship manager lead capture
7. C008 — Bookstore WhatsApp order assistant
8. C018 — $5K tutoring operations system
9. C029 — Offline university RAG
10. C076 — Medical-device expiry/spoilage automation

## Ana araştırma ilkesi

> Çok spesifik müşteri + çok spesifik tekrar eden problem + AI yalnız gerektiği yerde + ölçülebilir çıktı.

Ansiklopedinin amacı “AI ile para kazanmanın 122 yolu” demek değildir. Amaç, **gerçek bir insanın veya işletmenin para ödediği ya da ölçülebilir ekonomik değer bildirdiği 122 küçük problemi** arşivlemek ve güvenilirlik sorunu olan örnekleri ayrı X eki altında kaybetmemektir.
