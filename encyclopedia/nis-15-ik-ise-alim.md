# İnsan kaynakları ve işe alım

Aday ve çalışan süreçleri ile işe alım tarafındaki araştırma işleri. C090'daki saha notu grubun özeti: yapay zekânın iyi olduğu yer **araştırma ve evrak**, insanın yeri **değerlendirme ve karar**. İşe alım kararını makineye bırakmak hem etik hem hukuki risk.

**Türkiye'de kim satın alır?** İK danışmanlığı, personel firması, teknik işe alım ajansı

**Bu grupta 3 örnek var.** Ne kadar güvenilir oldukları — B: 1 · C: 2.

Harflerin ne anlama geldiği için `../RESEARCH_POLICY.md`, gruplar arası ortak dersler için `DESENLER.md`, hepsini birden filtrelemek için [atlas sayfası](https://paradoksix.github.io/ai-money-workflows/).

---

## B001 — Job Hacker: CV'yi ilana göre uyarlama

**Ne yapıyor?** İş ilanlarını buluyor, CV'deki anahtar kelime/bullet'ları ilana göre düzenlemeye yardımcı oluyor ve hiring manager araştırıyor.

**Kanıt:** Üretici AI araçları geliştirerek tam zamanlı gelir bildirmiş; tam olarak bu iş akışı için ayrı ücretli müşteri kanıtı yok.

**Kaynak:** `sirlifehacker/n8n-job-hacker`, commit `edbc144...`.

**Risk:** CV'de gerçek dışı bilgi üretme, LinkedIn otomasyonu.

**Senin için uygulama önizlemesi:** B2C “CV botu” yerine **iş arayanlara yarı-manuel CV/ilan eşleştirme hizmeti** daha kolay test edilir. Yerel modelle ilan-CV fark analizi yapıp insan kontrolüyle teslim edilebilir; otomatik başvuru kısmına hiç girmemek daha güvenli.

---

## C009 — HR Automation Packaged MVP

**Ne satılmış?** HR sürecini haritalayıp AI prompt logic + Sheets + Slack/Railway gibi araçlarla paketlenmiş operasyon MVP'si.

**Ticari kanıt:** **F: €3.000** kendi beyanı.

**Problem:** Dağınık aday/çalışan süreçleri ve manuel koordinasyon.

**Risk:** Çalışan/aday verisi, ayrımcılık, AI skorunun işe alım kararına dönüşmesi.

**Senin için uygulama önizlemesi:** İşe alım kararını AI'ya bırakma. **CV dosyalarını adlandırma, görüşme notunu özetleme, eksik belge takibi, aday durum panosu** gibi nötr idari süreçleri hedefle. Türkiye'de küçük işe alım danışmanlıkları bunun için uygun araştırma alanı.

---

## C090 — Manufacturing Recruiting Lead Research, £3.600/ay Araştırmacı İkamesi

**Ne yapılmış?** Manufacturing recruiting nişinde hangi şirketlerin büyüdüğünü/işe alım yaptığını izleyen dar lead-research sistemi.

**Ticari sonuç:** Recruiter, sistemin **S: £3.600/ay araştırmacı maliyetini kaldırdığını** ve lead kalitesinin arttığını kendisi bildiriyor.

**Kaynak:** Reddit r/recruiting, 24 Ocak 2026 “How is AI actually changing your recruiting process right now?” tartışmasındaki practitioner yorumu.

**Araç:** Yorumda `Boilr` adı veriliyor. Bunun yorumcuyla ticari ilişkisinin bağımsız doğrulaması yapılmadığı için sonuç temkinli tutulmalı.

**Ders:** Aynı yorumcu AI sourcing/phone screen/resume parsing'i kötü buluyor; AI'nın iyi olduğu alanı **araştırma + admin**, insanın alanını **assessment/judgment** olarak ayırıyor.

**Risk:** kendi beyanı, potansiyel ürün tanıtımı, şirket büyüme sinyalinin yanlış yorumlanması.

**Senin için uygulama önizlemesi:** Türkiye'de recruiting yerine **“hangi fabrikalar yeni yatırım/işe alım/ihracat sinyali veriyor?”** araştırması, personel firmaları veya B2B tedarikçiler için satılabilir. AI karar verici seçmesin; açık kaynaklardan şirket fırsat listesi ve kaynak linki üretsin.

---
