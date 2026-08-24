# Cilt 4 — Marketplace otomasyon, RAG ve voice vakaları

Bu cilt **C034–C049** arasındaki marketplace vakalarını içerir. Buradaki kanıt çoğunlukla Fiverr benzeri pazarlarda görülen ücretli review/order sinyalidir. Bu sinyal “yüksek gelir” kanıtı değildir; müşterilerin hangi küçük işleri gerçekten satın aldığını gösterir.

---

## C034 — Form → Sheet → e-mail notification automation

**Ne satılmış?** Basit bir formdan gelen veriyi Google Sheets'e yazıp ilgili kişilere e-mail bildirim gönderen otomasyon.

**Ticari sinyal:** **F: $50 order**, yaklaşık 6 günlük teslim ve ücretli review'lar.

**Önemli ders:** AI şart değil. Müşteri sonucu satın alıyor.

**Senin için uygulama önizlemesi:** Türkiye'de **servis talebi, kurs başvurusu, teklif formu, site yönetimi arıza talebi** gibi alanlarda en kolay gösterilebilir örneklerden. Google Forms/Tally + Sheets + n8n ile sıfıra yakın maliyetli demo hazırlanabilir.

---

## C035 — Agentic n8n workflow build

**Ne satılmış?** Claude/Gemini/LangChain/Vapi gibi bileşenlerle daha karmaşık agentic n8n workflow geliştirme.

**Ticari sinyal:** **9 ücretli review**, yaklaşık `$50` order örnekleri.

**Risk:** “AI agent yaparım” teklifi aşırı geniş; scope hızla büyür.

**Senin için uygulama önizlemesi:** Genel agent satma. Marketplace talebinin arkasındaki atomu seç: **e-mail sınıflandırma, lead qualification, randevu, veri enrichment**. Böylece teknik öğrenme ve müşteri teklifi daha net olur.

---

## C036 — n8n API Integration

**Ne satılmış?** İki veya daha fazla SaaS/API'yi n8n ile birbirine bağlama.

**Ticari sinyal:** **12 review**, görünür yaklaşık `$50–100` siparişler.

**Değer:** AI'dan bağımsız olarak API entegrasyon becerisinin satıldığını gösteriyor.

**Senin için uygulama önizlemesi:** Öğrenme açısından en değerli alanlardan. **Webhook → API → transform → Sheet/database → notification** zincirini birkaç public API ile kurmak, ileride neredeyse tüm diğer vakaların temelini oluşturur.

---

## C037 — AI chatbot + e-mail reply + lead workflow

**Ne satılmış?** KOBİ için chatbot, e-mail yanıt ve lead workflow kombinasyonu.

**Ticari sinyal:** Marketplace'te görünür yaklaşık **$100–200** order örneği.

**Risk:** Generic chatbot metalaşmış durumda; yanlış yanıt ve otomatik gönderim.

**Senin için uygulama önizlemesi:** Chatbot'u merkezden çıkar. Örneğin **“gelen lead'i sınıflandır → eksik bilgiyi sor → satışçıya temiz özet bırak”** şeklinde ölçülebilir süreç satmak daha mantıklı.

---

## C038 — Production n8n / AI automation

**Ne satılmış?** n8n/Make/Zapier ve AI entegrasyonlarını production'a hazırlama.

**Ticari sinyal:** **38 review**, `$30/saat` ve `$50` başlangıç siparişi gibi görünür fiyat sinyalleri.

**Risk:** “Production-ready” iddiası hata, retry, logging, secrets ve bakım sorumluluğu getirir.

**Senin için uygulama önizlemesi:** Bu kategoriye ileride girmek için her demoda **error handling + retry + log + manuel fallback** göstermeyi alışkanlık haline getir. Repo-tabanlı test/checklist çalışma biçimin burada avantajlı.

---

## C039 — AI Voice Receptionist / Cold Caller

**Ne satılmış?** Vapi/ElevenLabs/Twilio/n8n tabanlı telefon karşılayan veya arama yapan voice agent.

**Ticari sinyal:** **8 ücretli review**.

**Risk:** Çağrı rızası, ticari ileti mevzuatı, yanlış konuşma, yüksek kullanım maliyeti. Cold-calling en riskli varyant.

**Senin için uygulama önizlemesi:** Türkiye'de outbound cold-caller yerine **inbound receptionist** araştır: müşteri zaten işletmeyi aradığında çalışma saatleri, adres, randevu talebi gibi sınırlı işler. Başlangıçta voice yerine yazılı demo ekonomik olarak daha mantıklı.

---

## C040 — AI UGC sosyal reklam videoları

**Ne satılmış?** TikTok/Instagram/Facebook için AI UGC tarzı reklam videoları.

**Ticari sinyal:** **31 ücretli review**.

**Risk:** Sentetik testimonial, marka güveni, platform reklam politikaları.

**Senin için uygulama önizlemesi:** İçerik/video tecrüben burada avantaj. “Sahte müşteri yorumu” yerine **ürün demonstrasyonu + 3 hook + 3 dikey varyasyon + insan edit** paketi araştırılabilir.

---

## C041 — AI Product Photography + lifestyle/model scene

**Ne satılmış?** Ürün fotoğrafını farklı lifestyle sahnelerine veya AI model görsellerine yerleştirme.

**Ticari sinyal:** **74 review**, görünür yaklaşık `$50–100` order örneği.

**Risk:** Ürünün gerçekte olmayan özelliklerini göstermek; insan/model kullanımında yanıltıcılık.

**Senin için uygulama önizlemesi:** Türkiye'deki Trendyol/Hepsiburada satıcılarına **“5 gerçek ürün fotoğrafından 10 sosyal medya lifestyle görseli”** gibi dar paket düşünülebilir. Ürünün şekli/renk/etiketini değiştirmeyen QA şartı ekle.

---

## C042 — Custom RAG Chatbot

**Ne satılmış?** GPT/Claude/Gemini + LangChain/vector DB/FastAPI ile müşterinin belgelerine özel RAG chatbot.

**Ticari sinyal:** **4 ücretli review**.

**Risk:** Halüsinasyon, gizli belge, erişim kontrolü.

**Senin için uygulama önizlemesi:** Generic chatbot'tan daha ilginç. Mevcut PC'nde küçük yerel RAG prototipi çalıştırıp **teknik ürün kataloğu veya eğitim dökümanı** üzerinde kaynak-citation doğruluğunu test edebilirsin.

---

## C043 — Enterprise RAG Agent

**Ne satılmış?** Daha büyük müşteriler için Pinecone/Qdrant, GPT/Claude ve web arayüzüyle enterprise bilgi agent'ı.

**Ticari sinyal:** **5 review**.

**Risk:** Yetkilendirme, veri izolasyonu, prompt injection, SLA beklentisi.

**Senin için uygulama önizlemesi:** Enterprise hedefleme kısa vadede gereksiz. Aynı problemin **“10–100 PDF'lik private knowledge base”** küçük versiyonunu araştır; privacy ve kaynak gösterme özelliği temel değer olsun.

---

## C044 — PDF/makale → iki-host AI podcast

**Ne satılmış?** PDF veya makaleyi iki konuşmacılı AI podcast formatına çevirme.

**Ticari sinyal:** **18 review**, `$5` basic giriş paketi.

**Risk:** Düşük fiyat, kaynak telifi, sentetik ses kalitesi.

**Senin için uygulama önizlemesi:** Tek başına düşük ticket. Fakat **eğitim materyali → sesli çalışma özeti**, **şirket raporu → yönetici audio brief** gibi daha niş ve kurumsal biçime çevrilirse değer artabilir. Yerel TTS/Whisper araçları maliyeti azaltabilir.

---

## C045 — Private / Self-hosted RAG

**Ne satılmış?** Flask/Django/Express + vector DB ile müşterinin kendi altyapısında çalışan private RAG sistemi.

**Ticari sinyal:** Görünür yaklaşık **$50 order**.

**Değer:** “Verimiz OpenAI'a gitmesin” problemi.

**Senin için uygulama önizlemesi:** Senin yerel AI ilgine en uyumlu vakalardan. RTX 3060 12 GB üzerinde küçük model + local embeddings + basit web UI ile **offline demo** yapılabilir; satıştan önce retrieval doğruluğu benchmark'ı önemli.

---

## C046 — Website AI Chatbot + CRM

**Ne satılmış?** Web sitesine chatbot kurup CRM'e lead kaydı yapan sistem.

**Ticari sinyal:** **24 review**, yaklaşık `$60` başlangıç.

**Risk:** Generic chatbot fiyat baskısı; yanlış cevap.

**Senin için uygulama önizlemesi:** Chat ekranını değil **lead capture + CRM'e temiz kayıt + insan devri** kısmını öne çıkar. “Sitenize bot” yerine “kaçan iletişim taleplerini yapılandırıyoruz” teklifi daha anlaşılır.

---

## C047 — WhatsApp/RAG Lead Qualification

**Ne satılmış?** WhatsApp'tan gelen lead'i RAG/kurallarla cevaplayan, qualify eden ve sonraki aksiyona taşıyan sistem.

**Ticari sinyal:** **8 review**.

**Risk:** Meta/KVKK, otomatik ticari ileti, yanlış qualification.

**Senin için uygulama önizlemesi:** Türkiye açısından yüksek uyum. İlk sürüm **müşteri kendisi yazınca** çalışsın; hizmet türü, lokasyon, bütçe veya ürün kodu gibi 3–5 bilgiyi toplayıp satışçıya iletsin.

---

## C048 — Omnichannel Concierge

**Ne satılmış?** Web, SMS, voice ve sosyal kanalları birlikte yöneten concierge/assistant.

**Ticari sinyal:** Görünür yaklaşık **$100–200 / 3 gün** order.

**Risk:** Her kanal yeni failure mode demek; credential ve mesaj senkronizasyonu zor.

**Senin için uygulama önizlemesi:** Bunu tek seferde kopyalama. **Bir kanal + bir amaç** kuralını kullan. Örneğin yalnız WhatsApp randevu intake veya yalnız web lead capture. Omnichannel ancak tek kanalda değer kanıtlandıktan sonra.

---

## C049 — WhatsApp/Web Customer Support Chatbot

**Ne satılmış?** ChatGPT/Dialogflow/CRM/APIs ile WhatsApp ve web müşteri destek chatbot'u.

**Ticari sinyal:** **130+ review**; kategoriye gerçek talep olduğunu gösteriyor.

**Risk:** Aynı yüksek review sayısı güçlü rekabet/metalaşma sinyali de.

**Senin için uygulama önizlemesi:** Generic destek botu olarak rekabet etmek yerine **tek sektöre özel bilgi toplama + human escalation** düşün: oto servis, otel, yedek parça, kurs, site yönetimi. Sektör dili ve gerçek operasyon entegrasyonu savunma hattı olur.

---

## Cilt 4'ten çıkan ortak desen

Marketplace bize iki şeyi aynı anda gösteriyor:

1. n8n, RAG, WhatsApp ve voice için gerçekten ödeme yapan müşteriler var.
2. Generic “AI chatbot / AI agent” teklifleri hızla metalaşıyor.

Bu yüzden senin için en mantıklı araştırma yönü araç adıyla değil müşteri problemiyle nişleşmek:

**“WhatsApp bot” değil → “oto serviste eksik araç bilgilerini tamamlayan intake.”**

**“RAG chatbot” değil → “teknik ürün kataloğunu dışarı göndermeden kaynaklı cevaplayan asistan.”**

**“n8n automation” değil → “formdan gelen teklif talebini CRM'e temiz kaydeden süreç.”**
