# Eğitim & kurs operasyonu

Ders programı, öğrenci/veli iletişimi, ödeme takibi ve sınav/öğrenci verisi normalizasyonu. Türkiye'de dil kursu, özel ders merkezi ve etüt merkezi yoğunluğu düşünülünce vaka sayısına göre orantısız biçimde uygulanabilir bir niş. AI öğrenci değerlendirmesi yapmamalı.

**Türkiye'de kim satın alır?** Dil kursu, özel ders merkezi, etüt merkezi, sınav merkezi

**Bu nişte 2 vaka var.** Kanıt dağılımı — C: 2.

Kanıt dereceleri için `../RESEARCH_POLICY.md`, nişler arası kesişen dersler için `DESENLER.md`, tüm vakaların filtrelenebilir listesi için `../docs/index.html`.

---

## C018 — Tutoring Business Scheduling Agent

**Ne satılmış?** Öğretmen programlarını yöneten, Calendar'a yazan, WhatsApp reminder ve payment notification üreten eğitim operasyon sistemi.

**Ticari kanıt:** **F: $5.000**, geliştirici 2 günde kurduğunu ve production'da çalıştığını bildiriyor. 2 gün süresi yeni başlayan için referans değildir.

**Risk:** Öğrenci/veli verisi, ödeme bildirimi hatası.

**Senin için uygulama önizlemesi:** Türkiye'de **özel ders veren öğretmenler, dil kursları, küçük eğitim merkezleri** çok uygun. İlk araştırma ürünü: öğretmen müsaitliği + ders takvimi + hatırlatma + “ödendi/ödenmedi” takip tablosu. AI yalnız doğal dil talebini yapılandırsın.

---

## C078 — UK Private School / Exam Centre Data Workflow Retainer

**Ne satılmış?** Özel okul/sınav merkezinde farklı formatlarda gelen öğrenci/sınav verilerini temizleyip master spreadsheet üretme ve sezonluk veri toplama workflow'ları.

**Ticari kanıt:** Büyük tek seferlik ücret değil; geliştirici **yıllık retainer'ın biriktiğini** ve workflow'u kendisinin host ettiğini bildiriyor.

**Müşteri edinme:** Süreci elle yapan yönetici problemden bıkmış; demo sonrası kabul etmiş.

**Kaynak:** Reddit r/n8n real-business-problem thread'i.

**Senin için uygulama önizlemesi:** Türkiye'de kurs/özel okul/sınav merkezi için **farklı öğretmenlerden gelen Excel/form verisini tek master tabloya normalize etme**. AI yalnız serbest metin/kolon eşlemede yardımcı olabilir; öğrenci notu/karar üretmemeli.

---
