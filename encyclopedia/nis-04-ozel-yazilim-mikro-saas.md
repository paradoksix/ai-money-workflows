# Sipariş üzerine yazılım ve küçük ürünler

Hazır bir sistem değil, uygulama satılan işler. Ortak yön şu: kimse "parlak bir fikir bulup kullanıcı beklemiyor". Müşteri; mevcut bir tanıdıklıktan, bizzat yaşanmış bir sektör derdinden ve gösterilen küçük çalışan bir örnekten geliyor. Yapay zekâ kod yazmayı hızlandırıyor; **müşteriyi ödemeye ikna eden şey hâlâ problemi bilmek ve ürünü ulaştırabilmek**.

**Türkiye'de kim satın alır?** Dar sektör işletmeleri, meslek grupları, hâlihazırda tanıdığın müşteriler

**Bu grupta 14 örnek var.** Ne kadar güvenilir oldukları — C: 14.

Harflerin ne anlama geldiği için `../RESEARCH_POLICY.md`, gruplar arası ortak dersler için `DESENLER.md`, hepsini birden filtrelemek için `../docs/index.html`.

---

## C020 — Caffeine Curfew Apple Watch App

**Ne yapılmış?** Kafein tüketimi ve uyku zamanlamasına yardımcı olan Apple Watch/iOS uygulaması; Claude SwiftUI/SwiftData/Watch/widget/Health/Siri geliştirmesinde pair-programmer olarak kullanılmış.

**Ticari kanıt:** **R: 2.500 indirme ve yaklaşık $700 gelir** kendi beyanı.

**Kaynak notu:** Aynı geliştiricinin GitHub'ında `CaffeineCurfew` isimli repo bulundu ancak yalnız landing page içeriyor; uygulamanın gerçek Swift kaynak kodu olmadığı için doğrulanmış kaynak sayılmadı.

**Risk:** Sağlık iddiaları ve App Store ekonomisi; gelir düşük olabilir.

**Senin için uygulama önizlemesi:** Bu vaka “Apple Watch app yap”tan çok **AI ile bilmediğin platformda üretim hızını artırabilirsin ama dağıtım/ürün-pazar uyumu hâlâ zor** dersini veriyor. Türkiye'de B2C app yerine küçük işletmeye özel basit mobil/web yardımcı araçları daha öngörülebilir.

---

## C021 — Claude-Built Social Reseller SaaS

**Ne yapılmış?** Sosyal medya hizmeti satan reseller/ajanslara yönelik küçük SaaS; kodun yaklaşık %95'inin Claude ile yazıldığı bildiriliyor.

**Ticari kanıt:** **R: yaklaşık $40**, ilk ödeme yapan müşteri lansmandan 3 gün sonra.

**Stack:** Next.js + Supabase + Vercel + Claude.

**Ders:** İlk ödeme ürün doğrulamasıdır ama iyi ekonomik model kanıtı değildir.

**Senin için uygulama önizlemesi:** Kendi SaaS'ını sıfırdan kurmaya atlamadan, ansiklopedide bu deseni **“önce hizmette gördüğün tekrar eden problemi sonra küçük araca çevir”** olarak tut. Repo-tabanlı çalışma biçimin bu yönde avantaj sağlar.

---

## C022 — Conversational Survey Forms

**Ne yapılmış?** Klasik statik anket yerine önceki cevap bağlamını kullanan conversational form uygulaması.

**Ticari kanıt:** **R: ilk dış müşteri $25**.

**Köken problem:** Akademik/iş araştırmasında çok sayıda yanıt toplarken form deneyiminin yetersiz kalması.

**Risk:** Survey bias, kişisel veri, düşük ticket.

**Senin için uygulama önizlemesi:** Genel form SaaS'ı yerine **“müşteri brief toplama formu”, “servis arıza ön-teşhis formu”, “özel ders seviye/uygunluk formu”** gibi tek kullanım alanına uyarlama daha mantıklı. Tally/Forms + n8n ile önce no-code sürüm test edilebilir.

---

## C023 — GLP-1 Nutrition App

**Ne yapılmış?** Bir diyetisyenin Claude Code ile geliştirdiği beslenme uygulaması.

**Ticari kanıt:** **R: 4 ödeme yapan kullanıcı**, fakat geliştirici AI abonelikleri nedeniyle hâlâ net zararda olduğunu açıkça söylüyor.

**Önemli ders:** İlk müşteriler = sürdürülebilir iş modeli değildir.

**Risk:** Tıbbi/sağlık iddiaları ve düzenleyici sorumluluk.

**Senin için uygulama önizlemesi:** Sağlık uygulaması üretmek yerine bu vakayı **unit economics filtresi** olarak kullan. Her fikirde aylık API/hosting/ödeme maliyetini müşteri başına gelirle karşılaştır; düşük maliyet/açık kaynak tercihin bu riski azaltabilir.

---

## C030 — Client Catalog + Configurator Apps

**Ne satılmış?** Bir müşteriye ücretli katalog uygulaması, başka müşteriye ücretsiz MVP sonrası online configurator.

**Ticari kanıt:** İki gerçek müşteri “evet”; tutarlar açıklanmamış.

**Üretim:** Claude Code destekli custom web app development.

**Risk:** Müşteri özel yazılımında bakım/scope büyümesi.

**Senin için uygulama önizlemesi:** Türkiye'deki **mobilya, makine, alüminyum, tabela, mutfak, kapı/pencere** firmalarında katalog+konfigüratör sık karşılaşılan ihtiyaç. Buradaki araştırma sorusu: “müşteri Excel/PDF kataloğunda hangi seçimleri müşterisine sürekli elle açıklıyor?”

---

## C031 — Claude-Assisted Bug Bounty

**Ne yapılmış?** AI'dan güvenlik araştırmasında destek alarak bug bounty programında açık bulma.

**Ticari kanıt:** **F/R: $5.000 bounty** kendi beyanı; bağımsız doğrulama ve teknik detay yok.

**Risk:** Çok yüksek uzmanlık, authorization sınırları; yanlış yerde güvenlik testi yasadışı olabilir.

**Senin için uygulama önizlemesi:** Şimdilik uygulama adayı değil. Ansiklopedide **“AI uzmanlığı yükseltir ama temel güvenlik bilgisi yerine geçmez”** örneği olarak tut. Yalnızca açıkça yetkilendirilmiş programlarda ve ciddi eğitim sonrası düşünülmeli.

---

## C032 — Adversarial ML Script Contracting

**Ne satılmış?** AI/ML müşterisine adversarial/evaluation script geliştirme hizmeti.

**Ticari kanıt:** **F: $3.600/hafta** kendi beyanı.

**Teknik eşik:** Python, ML ve değerlendirme metodolojisi; yüksek.

**Risk:** Uzmanlık gereksinimi ve doğrulanmamış kendi beyanı.

**Senin için uygulama önizlemesi:** Kısa vadeli gelir adayı değil. Fakat yerel model/benchmark projelerine ilgin olduğu için uzun vadede **model evaluation, prompt regression test, output QA** gibi daha erişilebilir alt parçaları inceleyebilirsin.

---

## C033 — Claude-Built SaaS/App: 24 saatte ilk ödeme

**Ne yapılmış?** Claude yardımıyla hızla SaaS/app geliştirip ilk ödeme yapan kullanıcıyı kısa sürede edinme.

**Ticari kanıt:** İlk paying customer **24 saat içinde**; tutar açıklanmamış.

**Risk:** Survivor bias; ilk ödeme sürdürülebilir talep değildir.

**Senin için uygulama önizlemesi:** Bu vaka hızın mümkün olduğunu gösteriyor ama bizim araştırma hedefimizde **“24 saatte app yap” sinyali değil, “hangi spesifik problem birisini 24 saatte ödeme yapmaya ikna etti?”** sorusu daha değerli. Yeni benzer vakalarda problem tanımını özellikle çıkar.

---

## C086 — $5K Grant-Funded Sales Analysis App

**Ne satılmış?** Bir işletmeye uygun `$5.000` grant bulunuyor; grant kapsamında satış verisini accounting software'den export edip statik uygulamada OpenAI API ile satış analizi/prediction yapan küçük custom app geliştiriliyor.

**Ticari kanıt:** Geliştirici **F: $5.000 collected** kendisi bildiriyor; app'i yaklaşık bir günde hazırladığını söylüyor. İşletme kendi OpenAI API key'ini ödüyor.

**Kaynak:** Reddit r/ClaudeAI, 13 Haziran 2026 “Anyone here actually making money with stuff they built using Claude?” thread'i.

**Önemli ders:** Geliri sağlayan yalnız coding değil; **grant discovery + müşteriye demo/PDF + küçük uygulanabilir scope** kombinasyonu.

**Risk:** Hibe koşulları, çıkar çatışması, uygun olmayan hibe kullanımını teşvik etmemek; programa göre kurallar ayrı kontrol edilmeli.

**Senin için uygulama önizlemesi:** Türkiye/EU hibe danışmanlığı uzmanıymış gibi davranmadan, **KOSGEB/AB/dijitalleşme programlarında teknoloji harcamasına izin verilen alanları araştırıp**, hibe uzmanıyla partnerlik modeli düşünülebilir. İlk değer: küçük, açıkça tanımlı veri analizi/raporlama aracı.

---

## C087 — $30K Business Management Web App

**Ne satılmış?** Bir işletmenin operasyonunu yönetmek için özel web tabanlı management system.

**Ticari kanıt:** Geliştirici **F: $30.000 sözleşmeyi tamamladığını** bildiriyor.

**Müşteri edinme:** Geliştirici öğretmenlik yaparken öğrencilerinden birinin arkadaşının büyük bir yazılım şirketinden ürün almak üzere olduğunu öğreniyor. Ders sırasında Replit ile müşterinin istediği şeye benzer basit frontend demo gösteriyor; bu demo karar vericiye ulaşıyor ve birkaç ay sonra özel yazılım sözleşmesi imzalanıyor.

**AI rolü:** İlk görsel demo Replit; asıl uygulama geliştirme Claude Code ağırlıklı. Kaynak sahibi temel yazılım tasarımı/pentest geçmişi olduğunu da belirtiyor; bu nedenle “sıfır teknik bilgiyle bir günde $30K” şeklinde yorumlanmamalı.

**Kaynak:** Reddit r/ClaudeAI, 10 Şubat 2026 — “I just delivered on a $30,000 contract thanks to Claude Code”.

**Source durumu:** Müşteri uygulamasının kaynak kodu herkese açık değil. C kalır.

**Risk:** Custom software'da bakım, güvenlik, authentication, veri migration, scope creep ve production support.

**Senin için uygulama önizlemesi:** Buradaki asıl ders `$30K app` değil, **önce müşterinin mevcut sürecini görüp küçük çalışan demo göstermek**. Türkiye'de teknik servis, küçük üretici, eğitim merkezi veya distribütör için Excel/WhatsApp ile yürüyen tek bir süreci basit web paneline çevirmek; tam ERP yapmaya çalışmamak daha doğru başlangıç.

---

## C088 — Fitness Coach Habit + Daily Check-In App

**Ne satılmış?** Fitness coach için müşterilerin alışkanlıklarını ve günlük check-in'lerini takip eden küçük özel uygulama.

**Ticari kanıt:** **F: $500**. Geliştirici uygulamayı teslim ettiğini ve live olduğunu bildiriyor.

**Müşteri edinme:** Önceden tanıdığı fitness coach'a kendi yaptığı siteyi gösteriyor; coach bunun üzerine özel uygulama istiyor. Fiyatı geliştirici değil müşteri, “bana ne kadar değer sağlar?” sorusuna cevap verirken `$500` olarak belirliyor.

**Stack:** Claude Code + Vercel + Supabase authentication/database.

**Kaynak:** Reddit r/vibecoding, 7 Nisan 2026 — “I made my first $500 coding with claude”.

**Source durumu:** doğrulanmış kaynak kodu public olarak doğrulanmadı. C kalır.

**Risk:** Kişisel/sağlık verisi, hosting ve bakım sorumluluğu. Kaynak yorumlarında tek seferlik ücret karşılığında sürekli hosting/bakımın nasıl karşılanacağı özellikle sorgulanıyor.

**Senin için uygulama önizlemesi:** B2C fitness app çıkarmak yerine **mevcut koç/eğitmen için müşteri takip mini-paneli** daha mantıklı. Özel ders, dil öğretmeni veya kişisel antrenörde “check-in + hedef + randevu + not” gibi basit kayıtları merkezileştirmek aynı desendir.

---

## C089 — Pest-Control Inspection App, $500/ay

**Ne satılmış?** Pest-control inspection sürecine özel, sahada test edilmiş dar sektör uygulaması.

**Ticari kanıt:** Reddit yorumcusu **R: $500/ay imzalı kontrat** ve ayrıca cold inbound lead aldığını bildiriyor. Uygulamanın yaklaşık iki ay sahada test edildiğini ve word-of-mouth ile yayıldığını söylüyor.

**Kaynak:** Reddit r/vibecoding, 11 Şubat 2026 “Real success stories” tartışmasındaki yorum.

**Source durumu:** Ürün adı/kaynak kodu yorumda görünmüyor. C kalır.

**Neden önemli?** Generic checklist/SaaS yerine **tek saha mesleğinin inspection workflow'u** için ödeme var. Recurring revenue kanıtı olan dar dikey app örneği.

**Risk:** Inspection raporu yasal/teknik kayıt olarak kullanılıyorsa doğruluk, audit trail ve offline saha kullanımı gerekir.

**Senin için uygulama önizlemesi:** Türkiye'de pest control yerine **motosiklet/oto ekspertiz checklist'i, klima/beyaz eşya servis formu, yangın tüpü/periyodik kontrol, bina bakım turu** gibi saha denetimlerini araştır. İlk sürüm fotoğraf + checklist + PDF rapor + imza taslağı olabilir; AI zorunlu değil.

---

## C091 — Claude-Assisted SaaS, €100K ARR

**Ne yapılmış?** 10 yıllık software engineer bir geliştirici, yaklaşık bir yıl boyunca Claude Code desteğiyle kendi SaaS'ını geliştirip pazarlamayı öğreniyor.

**Ticari kanıt:** **R: €100K ARR**, yaklaşık **%80 profit margin** kendi beyanı.

**Kaynak:** Reddit r/ClaudeAI, 17 Şubat 2026 — “Claude changed my life”.

**Source durumu:** Kaynak post ürünün adını ve kaynak kodunu açıklamıyor. Dolayısıyla gelir iddiası güçlü olsa da iş modelinin ne olduğuna dair uygulanabilir ayrıntı sınırlı. C kalır ve “fikir kataloğu” açısından düşük önceliklidir.

**Risk:** Survivor bias ve deneyimli geliştirici etkisi. Claude'un katkısı ile ürün/pazarlama/uzmanlık katkısı ayrıştırılamaz.

**Senin için uygulama önizlemesi:** Bu vakayı “SaaS yap, €100K kazan” reçetesi olarak kullanma. Değerli ders: AI geliştirme maliyetini düşürebilir ama **1 yıl ürün + dağıtım + pazarlama** çalışması hâlâ gerekiyor. Bizim ansiklopedide hizmet/operasyon vakaları sana daha doğrudan uygulanabilir.

---

## C092 — Photographer-Specific Tools, >$150K ARR, kendi beyanı

**Ne yapılmış?** Profesyonel fotoğrafçı, kendi ihtiyacı için geliştirdiği araçları daha sonra diğer fotoğrafçılara satıyor.

**Ticari kanıt:** Aynı Claude success thread'indeki farklı bir yorumcu bu dikey araçların **R: $150K ARR üzerinde** gelir ürettiğini kendisi bildiriyor.

**Müşteri stratejisi:** Ürün fikri dışarıdan tahmin edilmiyor; geliştirici kendi mesleğinde yaşadığı probleme araç yapıyor ve aynı problemi yaşayan meslektaşlara sunuyor.

**Source durumu:** Ürün isimleri ve kaynak kodu yorumda açıklanmıyor. C kalır.

**Risk:** Ayrıntı az, bağımsız doğrulama yok.

**Senin için uygulama önizlemesi:** En değerli desen **“önce bir mesleğin içine gir, tekrarlanan problemi gör, sonra aracı çıkar”**. Yerel servis, kurye/lojistik, eğitim veya küçük işletme operasyonlarında dışarıdan generic SaaS fikri aramaktan daha sağlam yöntem.

---
