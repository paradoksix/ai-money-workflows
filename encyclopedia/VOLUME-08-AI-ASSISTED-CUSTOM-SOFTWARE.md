# Cilt 8 — AI-destekli özel yazılım ve dar sektör araçları

Bu cilt **C087–C092** vakalarını içerir. Buradaki ortak desen “genel SaaS fikri bulup kullanıcı beklemek” değil; çoğunlukla mevcut ilişki veya çok belirgin sektör problemi üzerinden küçük/özel yazılım satılmasıdır.

---

## C087 — $30K Business Management Web App

**Ne satılmış?** Bir işletmenin operasyonunu yönetmek için özel web tabanlı management system.

**Ticari kanıt:** Geliştirici **F: $30.000 sözleşmeyi tamamladığını** bildiriyor.

**Müşteri edinme:** Geliştirici öğretmenlik yaparken öğrencilerinden birinin arkadaşının büyük bir yazılım şirketinden ürün almak üzere olduğunu öğreniyor. Ders sırasında Replit ile müşterinin istediği şeye benzer basit frontend demo gösteriyor; bu demo karar vericiye ulaşıyor ve birkaç ay sonra özel yazılım sözleşmesi imzalanıyor.

**AI rolü:** İlk görsel demo Replit; asıl uygulama geliştirme Claude Code ağırlıklı. Kaynak sahibi temel yazılım tasarımı/pentest geçmişi olduğunu da belirtiyor; bu nedenle “sıfır teknik bilgiyle bir günde $30K” şeklinde yorumlanmamalı.

**Kaynak:** Reddit r/ClaudeAI, 10 Şubat 2026 — “I just delivered on a $30,000 contract thanks to Claude Code”.

**Source durumu:** Müşteri uygulamasının exact source'u public değil. C kalır.

**Risk:** Custom software'da bakım, güvenlik, authentication, veri migration, scope creep ve production support.

**Senin için uygulama önizlemesi:** Buradaki asıl ders `$30K app` değil, **önce müşterinin mevcut sürecini görüp küçük çalışan demo göstermek**. Türkiye'de teknik servis, küçük üretici, eğitim merkezi veya distribütör için Excel/WhatsApp ile yürüyen tek bir süreci basit web paneline çevirmek; tam ERP yapmaya çalışmamak daha doğru başlangıç.

---

## C088 — Fitness Coach Habit + Daily Check-In App

**Ne satılmış?** Fitness coach için müşterilerin alışkanlıklarını ve günlük check-in'lerini takip eden küçük özel uygulama.

**Ticari kanıt:** **F: $500**. Geliştirici uygulamayı teslim ettiğini ve live olduğunu bildiriyor.

**Müşteri edinme:** Önceden tanıdığı fitness coach'a kendi yaptığı siteyi gösteriyor; coach bunun üzerine özel uygulama istiyor. Fiyatı geliştirici değil müşteri, “bana ne kadar değer sağlar?” sorusuna cevap verirken `$500` olarak belirliyor.

**Stack:** Claude Code + Vercel + Supabase authentication/database.

**Kaynak:** Reddit r/vibecoding, 7 Nisan 2026 — “I made my first $500 coding with claude”.

**Source durumu:** Exact repo public olarak doğrulanmadı. C kalır.

**Risk:** Kişisel/sağlık verisi, hosting ve bakım sorumluluğu. Kaynak yorumlarında tek seferlik ücret karşılığında sürekli hosting/bakımın nasıl karşılanacağı özellikle sorgulanıyor.

**Senin için uygulama önizlemesi:** B2C fitness app çıkarmak yerine **mevcut koç/eğitmen için müşteri takip mini-paneli** daha mantıklı. Özel ders, dil öğretmeni veya kişisel antrenörde “check-in + hedef + randevu + not” gibi basit kayıtları merkezileştirmek aynı desendir.

---

## C089 — Pest-Control Inspection App, $500/ay

**Ne satılmış?** Pest-control inspection sürecine özel, sahada test edilmiş dar sektör uygulaması.

**Ticari kanıt:** Reddit yorumcusu **R: $500/ay imzalı kontrat** ve ayrıca cold inbound lead aldığını bildiriyor. Uygulamanın yaklaşık iki ay sahada test edildiğini ve word-of-mouth ile yayıldığını söylüyor.

**Kaynak:** Reddit r/vibecoding, 11 Şubat 2026 “Real success stories” tartışmasındaki yorum.

**Source durumu:** Ürün adı/exact repo kaynak yorumda görünmüyor. C kalır.

**Neden önemli?** Generic checklist/SaaS yerine **tek saha mesleğinin inspection workflow'u** için ödeme var. Recurring revenue kanıtı olan dar dikey app örneği.

**Risk:** Inspection raporu yasal/teknik kayıt olarak kullanılıyorsa doğruluk, audit trail ve offline saha kullanımı gerekir.

**Senin için uygulama önizlemesi:** Türkiye'de pest control yerine **motosiklet/oto ekspertiz checklist'i, klima/beyaz eşya servis formu, yangın tüpü/periyodik kontrol, bina bakım turu** gibi saha denetimlerini araştır. İlk sürüm fotoğraf + checklist + PDF rapor + imza taslağı olabilir; AI zorunlu değil.

---

## C090 — Manufacturing Recruiting Lead Research, £3.600/ay Araştırmacı İkamesi

**Ne yapılmış?** Manufacturing recruiting nişinde hangi şirketlerin büyüdüğünü/işe alım yaptığını izleyen dar lead-research sistemi.

**Ticari sonuç:** Recruiter, sistemin **S: £3.600/ay araştırmacı maliyetini kaldırdığını** ve lead kalitesinin arttığını self-report ediyor.

**Kaynak:** Reddit r/recruiting, 24 Ocak 2026 “How is AI actually changing your recruiting process right now?” tartışmasındaki practitioner yorumu.

**Araç:** Yorumda `Boilr` adı veriliyor. Bunun yorumcuyla ticari ilişkisinin bağımsız doğrulaması yapılmadığı için sonuç temkinli tutulmalı.

**Ders:** Aynı yorumcu AI sourcing/phone screen/resume parsing'i kötü buluyor; AI'nın iyi olduğu alanı **araştırma + admin**, insanın alanını **assessment/judgment** olarak ayırıyor.

**Risk:** Self-report, potansiyel ürün tanıtımı, şirket büyüme sinyalinin yanlış yorumlanması.

**Senin için uygulama önizlemesi:** Türkiye'de recruiting yerine **“hangi fabrikalar yeni yatırım/işe alım/ihracat sinyali veriyor?”** araştırması, personel firmaları veya B2B tedarikçiler için satılabilir. AI karar verici seçmesin; açık kaynaklardan şirket fırsat listesi ve kaynak linki üretsin.

---

## C091 — Claude-Assisted SaaS, €100K ARR

**Ne yapılmış?** 10 yıllık software engineer bir geliştirici, yaklaşık bir yıl boyunca Claude Code desteğiyle kendi SaaS'ını geliştirip pazarlamayı öğreniyor.

**Ticari kanıt:** **R: €100K ARR**, yaklaşık **%80 profit margin** self-report.

**Kaynak:** Reddit r/ClaudeAI, 17 Şubat 2026 — “Claude changed my life”.

**Source durumu:** Kaynak post ürünün adını ve exact source kodunu açıklamıyor. Dolayısıyla gelir iddiası güçlü olsa da iş modelinin ne olduğuna dair uygulanabilir ayrıntı sınırlı. C kalır ve “fikir kataloğu” açısından düşük önceliklidir.

**Risk:** Survivor bias ve deneyimli geliştirici etkisi. Claude'un katkısı ile ürün/pazarlama/uzmanlık katkısı ayrıştırılamaz.

**Senin için uygulama önizlemesi:** Bu vakayı “SaaS yap, €100K kazan” reçetesi olarak kullanma. Değerli ders: AI geliştirme maliyetini düşürebilir ama **1 yıl ürün + dağıtım + pazarlama** çalışması hâlâ gerekiyor. Bizim ansiklopedide hizmet/operasyon vakaları sana daha doğrudan uygulanabilir.

---

## C092 — Photographer-Specific Tools, >$150K ARR self-report

**Ne yapılmış?** Profesyonel fotoğrafçı, kendi ihtiyacı için geliştirdiği araçları daha sonra diğer fotoğrafçılara satıyor.

**Ticari kanıt:** Aynı Claude success thread'indeki farklı bir yorumcu bu dikey araçların **R: $150K ARR üzerinde** gelir ürettiğini self-report ediyor.

**Müşteri stratejisi:** Ürün fikri dışarıdan tahmin edilmiyor; geliştirici kendi mesleğinde yaşadığı probleme araç yapıyor ve aynı problemi yaşayan meslektaşlara sunuyor.

**Source durumu:** Ürün isimleri ve exact source yorumda açıklanmıyor. C kalır.

**Risk:** Ayrıntı az, bağımsız doğrulama yok.

**Senin için uygulama önizlemesi:** En değerli desen **“önce bir mesleğin içine gir, tekrarlanan problemi gör, sonra aracı çıkar”**. Yerel servis, kurye/lojistik, eğitim veya küçük işletme operasyonlarında dışarıdan generic SaaS fikri aramaktan daha sağlam yöntem.

---

## Cilt 8'den çıkan ortak desen

Özel yazılım tarafında en güçlü satış kanalı çoğu zaman reklam değil:

- mevcut müşteri/iş ilişkisi,
- aynı sektörde bizzat yaşanan problem,
- küçük çalışan demo,
- dar meslek/inspection/management workflow'u,
- müşterinin bugün ödediği insan/yazılım maliyetini açıkça görmek.

AI kodu hızlandırıyor; **müşteriyi ödeme yapmaya ikna eden şey problem bilgisi ve dağıtım** olmaya devam ediyor.
