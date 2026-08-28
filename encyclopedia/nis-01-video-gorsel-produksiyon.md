# Video ve görsel üretimi

Reklam filmi, ürün videosu, müzik klibi, avatar ve video kapak görseli. Buradaki kanıt çoğunlukla pazaryerlerindeki müşteri yorumu sayısı: talep gerçek, ama rekabet de o kadar yüksek. Örneklerin gösterdiği şey şu: müşteri artık "yapay zekâya erişim" satın almıyor; **aynı ürün için birden çok deneme sürümü, marka tutarlılığı ve makinenin çıkardığı işi yayınlanabilir hâle getiren insan kurgusunu** satın alıyor.

**Türkiye'de kim satın alır?** E-ticaret markaları, reklam ajansları, müzisyenler, içerik kanalları

**Bu grupta 20 örnek var.** Ne kadar güvenilir oldukları — A: 1 · B: 4 · C: 15.

Harflerin ne anlama geldiği için `../RESEARCH_POLICY.md`, gruplar arası ortak dersler için `DESENLER.md`, hepsini birden filtrelemek için [bütün örnekler sayfası](https://paradoksix.github.io/ai-money-workflows/tum-vakalar.html).

---

## A001 — AI Creative Director: moda kampanyası

**Ne satılmış?** Bir e-ticaret moda markası için çok sayıda kampanya görselini tutarlı kreatif yönle üretmeye yarayan AI creative-director workflow'u.

**Ticari kanıt:** Kaynak vaka kampanyayı **V: $9K campaign** olarak tanımlıyor. Bu rakam freelancerın net ücreti olarak doğrulanmıyor.

**Nasıl çalışıyor?** n8n + Gemini/Nano Banana benzeri görsel üretim zinciri; brief'i sahne/konsept/prompta dönüştürüp varyasyon üretiyor.

**Kaynak:** Reddit vaka + `sirlifehacker/Nano-Banana-Pro-Creative-Director`, pinned commit `1c82b35f...`. Root lisans bulunmadığı için kodu sahiplenmek yerine upstream referans alınmalı.

**Risk:** Marka/IP, ürünün gerçekte olmayan biçimde gösterilmesi, sentetik model kullanımı.

**Senin için uygulama önizlemesi:** Türkiye'de giyim yerine **mobilya, kozmetik, yerel gıda veya küçük e-ticaret markalarında “10 ürün → 30 reklam varyasyonu”** gibi dar bir paket araştırılabilir. Başlangıçta ücretli video modellerine girmeden görsel tarafında açık/ucuz araçlarla örnek set hazırlamak daha mantıklı; yerel PC'ni prompt/QA/metadata üretiminde kullanabilirsin.

---

## B010 — Uzun videodan Shorts/Reels adayları

**Ne yapıyor?** Uzun videoyu analiz edip kısa klip olabilecek bölümleri seçiyor ve üretim hattına aktarıyor.

**Stack:** n8n + Vizard/clip tool + Slack vb.

**Risk:** Telif, yanlış segment seçimi, düşük kalite.

**Senin için uygulama önizlemesi:** Tam otomatik video üretmek yerine **“AI klip adaylarını bulur, sen final kesim/altyazı/tempo kontrolü yaparsın”** yaklaşımı daha savunulabilir. Yerel Whisper kullanarak transkripsiyon maliyetini düşürebilirsin.

---

## B014 — Reklamdan 10 kontrollü A/B varyasyonu

**Ne yapıyor?** Mevcut başarılı kreatifi temel alıp kontrollü görsel/metin varyasyonları oluşturuyor.

**Kanıt:** Açık workflow; ücret yok.

**Risk:** Marka/IP, yalnız görsel değiştirip “test” diye satma.

**Senin için uygulama önizlemesi:** “AI görsel” yerine **“1 mevcut reklam → 10 hipotezli test varyasyonu + hangi unsur değişti tablosu”** satılabilir. Böylece çıktı ölçülebilir ve ajans müşterisi için daha profesyonel olur.

---

## B015 — E-commerce AI UGC video varyantları

**Ne yapıyor?** Ürün görsellerinden UGC tarzı video senaryoları/varyantları üretiyor.

**Stack:** Sora/Gemini/vision/n8n.

**Risk:** Sahte testimonial, marka güveni, video maliyeti.

**Senin için uygulama önizlemesi:** Başlangıçta gerçek kullanıcı yorumu taklit etmek yerine **ürün demonstrasyonu, problem/çözüm, katalog video** türüne odaklan. Video API maliyeti nedeniyle bu kategori yerel PC'nde metin/storyboard/QA, bulutta yalnız final üretim şeklinde düşünülmeli.

---

## B016 — Ürün fotoğrafını kısa videoya çevirme

**Ne yapıyor?** E-ticaret katalog görsellerini kısa hareketli ürün videolarına dönüştürüyor.

**Stack:** Firecrawl/Veo/Drive/n8n.

**Risk:** Ürünün fiziksel özelliklerini yanlış göstermek.

**Senin için uygulama önizlemesi:** Türkiye'de pazaryeri satıcılarına **“20 SKU → 20 kısa dikey ürün klibi”** şeklinde paketlenebilir. Önce birkaç üründe gerçek ürüne sadakat testi yapılmalı.

---

## C026 — AI Video Content Production Agent

**Ne satılmış?** Marketing ekibinin haftalık 20+ saatlik içerik üretimini azaltmayı hedefleyen AI video/content agent.

**Ticari kanıt:** **F: $2.530** satış iddiası.

**Stack:** Flux + Gemini + text/image-to-video + Telegram/n8n.

**Güven notu:** Satıcı/promosyon bağlamı nedeniyle bağımsız doğrulama gerekli.

**Senin için uygulama önizlemesi:** Senin içerik/video deneyimin nedeniyle teknik olarak erişilebilir, ancak “tam otomatik içerik agent” yerine **aylık içerik üretim hattı: brief → storyboard → draft → insan edit → teslim klasörü** daha güvenli ve satılabilir.

---

## C040 — AI UGC sosyal reklam videoları

**Ne satılmış?** TikTok/Instagram/Facebook için AI UGC tarzı reklam videoları.

**Ticari sinyal:** **31 ücretli review**.

**Risk:** Sentetik testimonial, marka güveni, platform reklam politikaları.

**Senin için uygulama önizlemesi:** İçerik/video tecrüben burada avantaj. “Sahte müşteri yorumu” yerine **ürün demonstrasyonu + 3 hook + 3 dikey varyasyon + insan edit** paketi araştırılabilir.

---

## C050 — Veo/Sora UGC Product Ad

**Ne satılmış?** Ürün için UGC tarzı dikey reklam videosu.

**Ticari sinyal:** **23 review**, yaklaşık `$50–100` sipariş örnekleri.

**Risk:** Sahte testimonial ve marka güveni.

**Senin için uygulama önizlemesi:** “AI UGC” yerine **3 farklı hook + 1 ürün demonstrasyonu + 3 dikey varyasyon** gibi ölçülebilir paket düşün. Senin video düzenleme deneyimin, AI çıktısını insan edit ile kaliteye taşıma tarafında avantaj.

---

## C051 — Realistic AI UGC Ad Editing

**Ne satılmış?** AI ile üretilmiş UGC reklamlarını gerçekçi hale getirme ve final edit.

**Ticari sinyal:** Yaklaşık **2 × $50** görünür order.

**Stack:** Veo/Sora/Kling/HeyGen + human edit.

**Senin için uygulama önizlemesi:** Buradaki değer model değil, **AI çıktısındaki yapaylıkları temizlemek**. Color, pacing, subtitle, sound design ve cutaway ile “AI raw output → yayınlanabilir reklam” hizmeti Türkiye'de ajanslara satılabilir.

---

## C052 — Cinematic Product Commercial

**Ne satılmış?** Ürün için sinematik kısa reklam filmi.

**Ticari sinyal:** **11 review**, `$30` başlangıç.

**Risk:** Ürünü gerçekte olmayan biçimde göstermek.

**Senin için uygulama önizlemesi:** Düşük ticket tek video yerine **3 ürün → 3 kısa commercial + aynı görsel dil** gibi seri üretim paketi daha anlamlı. Storyboard ve ürün gerçekliği kontrolü senin insan katkın olmalı.

---

## C053 — AI-Generated Music Video

**Ne satılmış?** Müzisyenlere AI destekli klip üretimi.

**Ticari sinyal:** **54 review**, bazı seçeneklerde yaklaşık `$40/saat`.

**Stack:** Kling/Veo/Krea/Higgsfield + editing.

**Senin için uygulama önizlemesi:** Yerel müzisyenler için tam klipten önce **15–30 sn teaser, Spotify canvas, dikey reels paketi** daha erişilebilir. Müzik senkronu ve edit becerisi asıl savunma hattı.

---

## C054 — AI Music-Video Production

**Ne satılmış?** Baştan sona AI destekli müzik videosu.

**Ticari sinyal:** **116 review**.

**Ders:** Müzisyen nişi marketplace'te gerçek ödeme gösteriyor.

**Senin için uygulama önizlemesi:** Türkiye'de bağımsız sanatçı/rap/elektronik müzik tarafında **cover art + teaser + lyric visualizer + kısa klip** şeklinde paket düşünmek tek “AI video”dan daha satılabilir.

---

## C055 — AI Brand Video

**Ne satılmış?** Marka tanıtım veya sosyal medya videosu.

**Ticari sinyal:** **9 review + repeat buyer** sinyali.

**Risk:** Generic video üretimi hızla commodity oluyor.

**Senin için uygulama önizlemesi:** Savunma hattını **marka dili + tekrar eden aylık üretim** yap. “Ayda 4 video + 8 cutdown + altyazı + teslim klasörü” modeli recurring gelir açısından daha anlamlı.

---

## C056 — AI Music Video + Avatar

**Ne satılmış?** Müzik videosu ve avatar/karakter kullanımı.

**Ticari sinyal:** Görünür yaklaşık **$200–400** sipariş.

**Stack:** Veo/Seedance/Runway/Kling/Luma.

**Risk:** Karakter tutarlılığı, likeness/telif.

**Senin için uygulama önizlemesi:** Yüksek ticket mümkün ama üretim maliyeti de artar. İlk araştırma, aynı karakteri 5–10 sahnede tutarlı üretme benchmark'ı; satıştan önce teknoloji güvenilirliğini ölç.

---

## C057 — 3'lü AI UGC Ad Paketi

**Ne satılmış?** Tek ürün için üç UGC reklam varyasyonu.

**Ticari sinyal:** **28 review**, yaklaşık `$50–100` paketler.

**Ders:** Müşteri tek video değil, test varyasyonu satın alıyor.

**Senin için uygulama önizlemesi:** Türkiye'de küçük e-ticaret markalarına **3 hook × 1 ürün** paket mantığı uygulanabilir. AI generation maliyetini paket fiyatına göre baştan hesaplamak gerekir.

---

## C058 — AI Avatar / Commercial Video

**Ne satılmış?** Avatar ve sentetik video kullanarak reklam/tanıtım.

**Ticari sinyal:** **15 review**, yaklaşık `$50–100` order.

**Risk:** Sentetik sunucunun gerçek kişi gibi sunulması.

**Senin için uygulama önizlemesi:** Avatarı “müşteri testimonialı” yerine **ürün açıklayıcı sunucu, eğitim anlatıcısı veya çok-dilli kurumsal video** olarak konumlandırmak daha güvenli.

---

## C062 — AI Promotional Commercial

**Ne satılmış?** AI destekli kısa promotional commercial.

**Ticari sinyal:** **13 review**, **$85 başlangıç**.

**Senin için uygulama önizlemesi:** En iyi teklif “video üretirim” değil, **tek kampanya için 15s/30s/vertical üç format**. Aynı asset'ten farklı format üretmek marjı yükseltir.

---

## C063 — AI YouTube Thumbnail

**Ne satılmış?** AI destekli thumbnail tasarımı.

**Ticari sinyal:** **40 review**, yaklaşık `$10`.

**Risk:** Çok düşük ticket ve commodity.

**Senin için uygulama önizlemesi:** Tek thumbnail satmak yerine **aylık 12 thumbnail + 2 alternatif başlık/thumbnail konsepti** paketi daha mantıklı. AI yalnız konsept hızlandırıcı.

---

## C064 — AI-Enhanced Thumbnail

**Ne satılmış?** AI + insan tasarımıyla daha profesyonel thumbnail.

**Ticari sinyal:** **565 review**.

**Ders:** İnsan tasarım becerisi hâlâ değerli; AI yalnız üretim hızını artırıyor.

**Senin için uygulama önizlemesi:** Bu kategori, içerik üretimi geçmişinle en hızlı denenebileceklerden. Ancak rekabet yüksek olduğu için **tek niş kanal tipi** seçmek önemli: podcast, eğitim, teknoloji, emlak vb.

---

## C065 — Midjourney Thumbnail

**Ne satılmış?** Midjourney ile thumbnail üretip düzenleme.

**Ticari sinyal:** **36 review**, `$10` başlangıç.

**Risk:** Araç adı üzerinden satılan hizmetin kolay kopyalanması.

**Senin için uygulama önizlemesi:** “Midjourney thumbnail” yerine **CTR test mantığı, okunabilir tipografi, marka yüzü/renk tutarlılığı** sat. Araç değişse bile hizmet değeri kalır.

---
