# Ofis ve evrak işleri

Form, e-posta, dosya ve tablo trafiğini düzene sokan işler. C011'in gösterdiği gibi burada **yapay zekâ çoğu zaman şart bile değil** — müşteri sadece kopyala-yapıştırdan kurtulmak istiyor. Bu grup, sıradan bir otomasyonun bazen yapay zekâdan daha doğru çözüm olduğunu hatırlatıyor.

**Türkiye'de kim satın alır?** Klinik, kurs, emlak ofisi, küçük ajans, tek başına yürüyen işletmeci

**Bu grupta 7 örnek var.** Ne kadar güvenilir oldukları — B: 1 · C: 6.

Harflerin ne anlama geldiği için `../RESEARCH_POLICY.md`, gruplar arası ortak dersler için `DESENLER.md`, hepsini birden filtrelemek için [atlas sayfası](https://paradoksix.github.io/ai-money-workflows/).

---

## B005 — AI Gmail Agent

**Ne yapıyor?** Gelen e-postayı sınıflandırıyor, önceliklendiriyor ve taslak yanıt oluşturuyor.

**Kanıt:** Açık JSON workflow; ne kadar kazandırdığı bilinmiyor.

**Risk:** Yanlış otomatik gönderim, gizli e-posta içeriği.

**Senin için uygulama önizlemesi:** En iyi yerel kullanım **“gelen maili cevaplamak” değil, “gelen maili klasörle + kısa özet + cevap taslağı hazırla”**. İnsan gönderim onayı korunursa düşük maliyetli ve birçok KOBİ'ye uygulanabilir.

---

## C011 — Clinic Intake Copy-Paste Automation

**Ne yapılmış?** Form → spreadsheet → özet e-mail → shared folder gibi basit intake otomasyonu.

**Ticari sonuç:** **S: 10–12 saat/hafta** iddiası; geliştirici bunu yaklaşık `$30K/yıl` tasarrufa extrapole ediyor.

**Önemli nokta:** AI şart değil. Müşteri yalnız manuel kopyala-yapıştır işinden kurtulmak istiyor.

**Risk:** Sağlık verisi.

**Senin için uygulama önizlemesi:** Sağlık yerine **kurs kayıtları, servis talepleri, emlak müşteri formu, iş başvurusu evrak toplama** gibi düşük regülasyonlu süreçlerde aynı deseni ara. Bu vaka, bazen normal otomasyonun AI'dan daha doğru ürün olduğunu gösteriyor.

---

## C034 — Form → Sheet → e-mail notification automation

**Ne satılmış?** Basit bir formdan gelen veriyi Google Sheets'e yazıp ilgili kişilere e-mail bildirim gönderen otomasyon.

**Ticari sinyal:** **F: $50 order**, yaklaşık 6 günlük teslim ve ücretli review'lar.

**Önemli ders:** AI şart değil. Müşteri sonucu satın alıyor.

**Senin için uygulama önizlemesi:** Türkiye'de **servis talebi, kurs başvurusu, teklif formu, site yönetimi arıza talebi** gibi alanlarda en kolay gösterilebilir örneklerden. Google Forms/Tally + Sheets + n8n ile sıfıra yakın maliyetli demo hazırlanabilir.

---

## C071 — AI-Assisted Executive / Content VA

**Ne satılmış?** Founder/KOBİ için araştırma, içerik, planlama, doküman ve asistanlık işlerini ChatGPT/Claude/Office/Canva ile hızlandıran VA hizmeti.

**Ticari sinyal:** **20 review**, yaklaşık **$30 / 6 saat** paket sinyali.

**Risk:** Düşük fiyat baskısı, credential/confidentiality.

**Senin için uygulama önizlemesi:** Generic VA yerine **AI destekli B2B araştırma/operasyon asistanı** daha uyumlu: şirket listesi temizleme, araştırma özeti, Sheets düzenleme, takip tablosu ve haftalık rapor. Sonradan tekrar eden parçalar n8n'e taşınabilir.

---

## C072 — AI-Boosted VA: research + Sheets + outreach + Notion

**Ne satılmış?** Araştırma, Sheets, özetleme, outreach hazırlığı, Notion ve genel operasyon işlerini AI ile hızlandıran sanal asistanlık.

**Ticari sinyal:** **65 completed order / 44 review**, yaklaşık `$5 / 1 saat` giriş paketi.

**Ders:** Talep var ama global marketplace'te fiyat çok düşük olabilir.

**Senin için uygulama önizlemesi:** Saat satma yarışına girme. **“50 şirketlik temiz araştırma listesi”, “haftalık rakip radar raporu”, “300 satırlık katalog QA”** gibi fixed-output hizmete dönüştür. AI verimliliği marjını artırır.

---

## C074 — AI-Assisted General VA

**Ne satılmış?** Genel sanal asistanlık; araştırma, veri girişi, admin ve içerik işleri AI ile hızlandırılıyor.

**Ticari sinyal:** **492 completed order** sinyali, yaklaşık `$20 / 2 saat` giriş paketi.

**Risk:** Düşük fiyat/yoğun rekabet ve müşteri hesaplarına erişim.

**Senin için uygulama önizlemesi:** Bunu son hedef değil **müşteri problemlerini içeriden gözlemleme yolu** olarak gör. Bir sektörde VA işi yaparken en sık tekrarlanan 2–3 işi tespit edip otomasyon fırsatına çevirmek daha değerli olabilir.

---

## C075 — Jarvis / Voice Virtual-Assistant Build

**Ne satılmış?** Voice/AI/automation kullanan kişisel veya iş amaçlı sanal asistan sistemi.

**Ticari sinyal:** Görünür yaklaşık **$200–400** AI-chatbot/assistant siparişi.

**Risk:** Scope çok kolay patlar; “Jarvis gibi her şeyi yapsın” beklentisi teknik ve güvenlik açısından tehlikeli.

**Senin için uygulama önizlemesi:** Genel Jarvis yapma. **Tek rol + tek veri kaynağı + 2–3 aksiyon** sınırı koy: örneğin “servis yöneticisinin günlük iş emirlerini özetleyen sesli asistan”. Voice son katman olsun; önce text workflow doğru çalışsın.

---
