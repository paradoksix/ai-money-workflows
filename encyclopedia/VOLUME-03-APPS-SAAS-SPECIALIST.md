# Cilt 3 — App, mikro-SaaS ve uzmanlık işleri

Bu cilt **C020–C033** vakalarını içerir. Buradaki örneklerin ortak yönü, yalnız workflow değil; özel uygulama, mikro-SaaS, migration, RAG veya uzmanlık hizmetinin AI ile daha hızlı üretilmesidir.

---

## C020 — Caffeine Curfew Apple Watch App

**Ne yapılmış?** Kafein tüketimi ve uyku zamanlamasına yardımcı olan Apple Watch/iOS uygulaması; Claude SwiftUI/SwiftData/Watch/widget/Health/Siri geliştirmesinde pair-programmer olarak kullanılmış.

**Ticari kanıt:** **R: 2.500 indirme ve yaklaşık $700 gelir** self-report.

**Kaynak notu:** Aynı geliştiricinin GitHub'ında `CaffeineCurfew` isimli repo bulundu ancak yalnız landing page içeriyor; uygulamanın gerçek Swift kaynak kodu olmadığı için exact repo sayılmadı.

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

## C024 — İlk Upwork n8n Gig

**Ne satılmış?** Upwork üzerinden özel n8n otomasyon işi.

**Ticari kanıt:** **F: $1.000+**, yaklaşık `$28/saat × 40 saat`; sonrasında bakım aşaması.

**Değer:** Marketplace'te gerçekten automation engineering için dört haneli proje çıkabildiğini gösteriyor.

**Risk:** Upwork rekabeti, scope creep, platform kuralları.

**Senin için uygulama önizlemesi:** “n8n expert” profili yerine portföyde **3 dar vaka: Sheets/CRM, e-mail triage, belge extraction** göstermek daha iyi. İlk hedef yüksek saat ücreti değil, işi küçük parçalara bölen temiz teklif ve doğrulanabilir demo.

---

## C025 — UK Agency: Make → n8n Migration + 15 Workflow

**Ne satılmış?** Bir UK ajans için 15 basit workflow ve 9 Make→n8n migration.

**Ticari kanıt:** **F: £1.000 ilk ay**, sonra **£1.000/ay extension** teklifi.

**Ders:** Yeni agent kurmaktan ziyade **migration, bakım ve mevcut sistem temizliği** de para ediyor.

**Risk:** Müşterinin production credential'ları, migration sırasında kesinti.

**Senin için uygulama önizlemesi:** Türkiye'de veya globalde “Make/Zapier faturanız yüksek, n8n'e geçelim” teklifi ileride güçlü olabilir. Şimdilik farklı platformlardan aynı basit akışı kurmayı öğrenmek ve migration checklist'i hazırlamak değerli araştırma yatırımı.

---

## C026 — AI Video Content Production Agent

**Ne satılmış?** Marketing ekibinin haftalık 20+ saatlik içerik üretimini azaltmayı hedefleyen AI video/content agent.

**Ticari kanıt:** **F: $2.530** satış iddiası.

**Stack:** Flux + Gemini + text/image-to-video + Telegram/n8n.

**Güven notu:** Satıcı/promosyon bağlamı nedeniyle bağımsız doğrulama gerekli.

**Senin için uygulama önizlemesi:** Senin içerik/video deneyimin nedeniyle teknik olarak erişilebilir, ancak “tam otomatik içerik agent” yerine **aylık içerik üretim hattı: brief → storyboard → draft → insan edit → teslim klasörü** daha güvenli ve satılabilir.

---

## C027 — Device Repair WhatsApp + Voice Agent

**Ne yapılmış?** Tamir dükkânında randevu, teklif, stok, iç sipariş, FAQ ve insan devrini WhatsApp + voice üzerinden yöneten sistem.

**Ticari sonuç:** **S: 80+ saat/ay** tekrar eden destek işinin kaldırıldığı; sistemin **1 yıldan uzun** çalıştığı ve işletme satıldığında yeni sahibin kullanmaya devam ettiği; run cost'un `<€200/ay` olduğu bildiriliyor.

**Stack:** n8n + WhatsApp + ElevenLabs + operasyon entegrasyonları.

**Risk:** Voice/WhatsApp maliyeti, yanlış teklif, müşteri verisi.

**Senin için uygulama önizlemesi:** Türkiye'de **telefon/tablet/PC servisi, motosiklet servisi, beyaz eşya tamiri** için çok doğal. İlk atom: “mesajdan cihaz/marka/model/arıza/servis türünü çıkar → eksik bilgiyi sor → personele özet bırak.” Voice ve stok entegrasyonu daha sonra.

---

## C028 — Custom E-commerce Integration Projects

**Ne satılmış?** Online mağazalara özel API ve operasyon entegrasyonları.

**Ticari kanıt:** Geliştirici **F: $3K–$5K/proje**, 10–20 saat/hafta manuel işi azaltma ve `$300–$1K+` retainer önerisi bildiriyor.

**Güven:** Reddit thread'inde AI-benzeri yazım/promosyon şüphesi bulunduğu için orta.

**Senin için uygulama önizlemesi:** Büyük “e-commerce integration” yerine **tek akış** ara: stok CSV import, sipariş export, kargo durumu eşleme, iade nedenleri raporu, katalog normalizasyonu. Türkiye'de Shopify kadar WooCommerce/yerel ERP/pazaryeri CSV akışları da önemli.

---

## C029 — Offline University RAG Chatbot

**Ne satılmış?** Güney Afrika'daki üniversite için internete veri göndermeden local/open-source modelle çalışan RAG bilgi sistemi.

**Ticari kanıt:** **F/V: $5.500 deal**, 2.000+ öğrenci hedefi.

**Teknik:** Yerel GPU + önceden vectorize edilmiş seçilebilir kaynaklar; geliştirici native-code çözümünün n8n'e tercih edildiğini söylüyor. Kod ücretli/private library'de.

**Risk:** Kaynak doğruluğu, kullanıcı yetkisi, öğrenci verisi.

**Senin için uygulama önizlemesi:** RTX 3060 12 GB bu alanı deneysel olarak anlaman için yeterli. Büyük üniversite yerine **küçük eğitim kurumu, teknik servis dokümanı, ürün kataloğu veya şirket prosedürü** ile local RAG benchmark'ı araştırabilirsin. Bu alanda privacy satış argümanı güçlü.

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

**Ticari kanıt:** **F/R: $5.000 bounty** self-report; bağımsız doğrulama ve teknik detay yok.

**Risk:** Çok yüksek uzmanlık, authorization sınırları; yanlış yerde güvenlik testi yasadışı olabilir.

**Senin için uygulama önizlemesi:** Şimdilik uygulama adayı değil. Ansiklopedide **“AI uzmanlığı yükseltir ama temel güvenlik bilgisi yerine geçmez”** örneği olarak tut. Yalnızca açıkça yetkilendirilmiş programlarda ve ciddi eğitim sonrası düşünülmeli.

---

## C032 — Adversarial ML Script Contracting

**Ne satılmış?** AI/ML müşterisine adversarial/evaluation script geliştirme hizmeti.

**Ticari kanıt:** **F: $3.600/hafta** self-report.

**Teknik eşik:** Python, ML ve değerlendirme metodolojisi; yüksek.

**Risk:** Uzmanlık gereksinimi ve doğrulanmamış self-report.

**Senin için uygulama önizlemesi:** Kısa vadeli gelir adayı değil. Fakat yerel model/benchmark projelerine ilgin olduğu için uzun vadede **model evaluation, prompt regression test, output QA** gibi daha erişilebilir alt parçaları inceleyebilirsin.

---

## C033 — Claude-Built SaaS/App: 24 saatte ilk ödeme

**Ne yapılmış?** Claude yardımıyla hızla SaaS/app geliştirip ilk ödeme yapan kullanıcıyı kısa sürede edinme.

**Ticari kanıt:** İlk paying customer **24 saat içinde**; tutar açıklanmamış.

**Risk:** Survivor bias; ilk ödeme sürdürülebilir talep değildir.

**Senin için uygulama önizlemesi:** Bu vaka hızın mümkün olduğunu gösteriyor ama bizim araştırma hedefimizde **“24 saatte app yap” sinyali değil, “hangi spesifik problem birisini 24 saatte ödeme yapmaya ikna etti?”** sorusu daha değerli. Yeni benzer vakalarda problem tanımını özellikle çıkar.

---

## Cilt 3'ten çıkan ortak desen

AI-assisted coding gerçekten teslim süresini azaltabiliyor; fakat **ürün geliştirme hızı ile müşteri edinme kolaylığı aynı şey değil.**

Bu ciltte sana en uygulanabilir desenler:

- C025 — migration/bakım hizmeti,
- C027 — yerel tamir/servis operasyonu,
- C029 — private/local RAG,
- C030 — müşteriye özel katalog/configurator.

B2C app ve SaaS örnekleri ise gelir kanıtı açısından daha oynak; hizmet modelinden daha yüksek pazar riski taşıyor.
