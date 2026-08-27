# Müşteri iletişimi & destek

Gelen mesajı, çağrıyı veya formu karşılayıp sınıflandıran, eksik bilgiyi tamamlayan ve gerektiğinde insana devreden sistemler. Marketplace'te en çok review alan kategorilerden biri — yani hem gerçek talep hem güçlü metalaşma var. Ayrışma yolu generic bot değil, **tek sektörün diline ve gerçek operasyonuna bağlanmak**.

**Türkiye'de kim satın alır?** Otel, klinik, oto servis, e-ticaret, kurs, site yönetimi

**Bu nişte 12 vaka var.** Kanıt dağılımı — B: 6 · C: 6.

Kanıt dereceleri için `../RESEARCH_POLICY.md`, nişler arası kesişen dersler için `DESENLER.md`, tüm vakaların filtrelenebilir listesi için `../docs/index.html`.

---

## B002 — Otel yüksek-harcayan müşteri reward e-mail

**Ne satılmış?** Salesforce/CRM'deki yüksek harcayan otel müşterilerini belirleyip kişiselleştirilmiş teşekkür/ödül e-maili gönderen workflow.

**Ticari kanıt:** **F: $200**; yazar yaklaşık 40 dakikada yaptığını söylüyor. GitHub'daki kaynak author repo değil, resmi n8n template'in mirror'u.

**Risk:** CRM verisi ve yanlış kampanya koşulları.

**Senin için uygulama önizlemesi:** Türkiye'de otel/pansiyon yerine **kuaför, servis, restoran, özel ders veya küçük e-ticaret** için “son 90 günde en çok harcayan müşteriler → insan onaylı geri-kazanım listesi” olarak uyarlanabilir. İlk versiyonda otomatik mesaj göndermek yerine öneri listesi üretmek düşük riskli.

---

## B003 — Dental Practice Voice Agent

**Ne yapıyor?** Diş kliniğinde telefondan gelen talepleri karşılayıp müsaitlik kontrolü, randevu ve Sheets log işlemleri yapıyor.

**Kanıt:** Çalışan JSON açık; exact müşteri/ücret bilinmiyor.

**Stack:** n8n + voice provider + Calendar + Sheets.

**Risk:** Sağlık verisi, yanlış randevu, çağrı kaydı/rıza.

**Senin için uygulama önizlemesi:** Sağlıkla başlamaktansa aynı sistemi **oto servis, kuaför, pet kuaförü, teknik servis veya restoran rezervasyonu** gibi daha düşük regülasyonlu alanlarda araştır. Voice maliyetli olduğu için önce WhatsApp/form tabanlı prototip daha ekonomik.

---

## B004 — Hotel WhatsApp Guest Assistant

**Ne yapıyor?** Misafirlerin sık sorularını yanıtlayıp otel bilgisi/öneri sunan WhatsApp agent.

**Kanıt:** Açık workflow var; exact ücret yok.

**Risk:** Meta policy, yanlış tesis bilgisi, kişisel veriler.

**Senin için uygulama önizlemesi:** Türkiye turizminde güçlü aday. Küçük oteller için ilk aşamada **check-in saati, kahvaltı, Wi-Fi, otopark, konum, transfer, oda kuralları** gibi yalnızca doğrulanmış bilgi tabanından cevap veren agent araştırılabilir. Sipariş/ödeme gibi aksiyonları sonraya bırak.

---

## B021 — Support ticket classifier

**Ne yapıyor?** Gelen destek taleplerini intent/priority kategorilerine ayırıyor.

**Risk:** Acil talebin yanlış düşük önceliğe düşmesi.

**Senin için uygulama önizlemesi:** İlk sürüm yalnız **etiketlesin ve özetlesin**, otomatik kapatmasın. Teknik servis, e-ticaret, site yönetimi veya küçük SaaS'ta uygulanabilir.

---

## B023 — WhatsApp Business RAG Agent

**Ne yapıyor?** WhatsApp mesajını bilgi tabanıyla yanıtlıyor ve konuşmayı logluyor.

**Risk:** Meta policy, KVKK, yanlış cevap.

**Senin için uygulama önizlemesi:** Türkiye için güçlü fakat ilk ürün “serbest konuşan agent” değil, **5–10 doğrulanmış FAQ + insan devri + kayıt** olmalı. Satın alma/ödeme gibi kritik aksiyonlar insan onayında kalmalı.

---

## B025 — Appointment Scheduling Assistant

**Ne yapıyor?** Randevu talebini aciliyet, süre, uygun slot ve mesaj haline getiriyor.

**Risk:** Özellikle sağlık sektöründe yanlış aciliyet yorumu.

**Senin için uygulama önizlemesi:** Kuaför, teknik servis, danışmanlık, özel ders gibi alanlarda **“talebi yapılandır + uygun slot öner + insan onayıyla gönder”** biçiminde uygulanabilir. Takvim entegrasyonu basit ve ölçülebilir olduğu için iyi araştırma adayı.

---

## C037 — AI chatbot + e-mail reply + lead workflow

**Ne satılmış?** KOBİ için chatbot, e-mail yanıt ve lead workflow kombinasyonu.

**Ticari sinyal:** Marketplace'te görünür yaklaşık **$100–200** order örneği.

**Risk:** Generic chatbot metalaşmış durumda; yanlış yanıt ve otomatik gönderim.

**Senin için uygulama önizlemesi:** Chatbot'u merkezden çıkar. Örneğin **“gelen lead'i sınıflandır → eksik bilgiyi sor → satışçıya temiz özet bırak”** şeklinde ölçülebilir süreç satmak daha mantıklı.

---

## C039 — AI Voice Receptionist / Cold Caller

**Ne satılmış?** Vapi/ElevenLabs/Twilio/n8n tabanlı telefon karşılayan veya arama yapan voice agent.

**Ticari sinyal:** **8 ücretli review**.

**Risk:** Çağrı rızası, ticari ileti mevzuatı, yanlış konuşma, yüksek kullanım maliyeti. Cold-calling en riskli varyant.

**Senin için uygulama önizlemesi:** Türkiye'de outbound cold-caller yerine **inbound receptionist** araştır: müşteri zaten işletmeyi aradığında çalışma saatleri, adres, randevu talebi gibi sınırlı işler. Başlangıçta voice yerine yazılı demo ekonomik olarak daha mantıklı.

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
