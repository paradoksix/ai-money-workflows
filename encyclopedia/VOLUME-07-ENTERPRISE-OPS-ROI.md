# Cilt 7 — Enterprise operasyon, maliyet düşürme ve yüksek-ROI vakaları

Bu cilt araştırmanın genişletme dalgasında bulunan **C076–C086** vakalarını içerir. Ortak özellikleri: çoğunda “AI ürünü” satılmıyor; mevcut lisans, insan zamanı, belge akışı veya operasyon kaybı ölçülebilir biçimde azaltılıyor.

---

## C076 — Medical Device Expiry / Spoilage Automation

**Ne satılmış?** Medikal cihaz distribütöründe son kullanma tarihi 45 günden az kalan stokların haftalık raporlanması; ürünlerin first-to-pick yapılması veya üreticiye %60 refund için geri gönderilmesi.

**Ticari kanıt:** Müşteri hesaplamasına göre **S: $36K ilk çeyrek tasarruf**. Hizmet sağlayıcıya **F/R: $1.000/ay** ödenmeye devam edildiği ve müşteri başka otomasyonlar istediği bildiriliyor.

**Kaynak:** Reddit r/n8n, “What automations are you guys actually selling?” thread'i.

**Risk:** Medikal cihaz stok/expiry yanlışlığı ciddi sonuç doğurabilir; AI karar vermemeli, kaynak inventory sistemi ve deterministik tarihler esas alınmalı.

**Senin için uygulama önizlemesi:** Sağlıkla başlamadan aynı deseni **gıda distribütörü, kozmetik, boya/kimya, yedek parça shelf-life, garanti süresi** gibi daha düşük regülasyonlu stoklarda araştır. “45 gün içinde riskli stok → rapor + aksiyon önerisi” basit ama ROI'si çok görünür.

---

## C077 — D365 Status Update / IOM Replacement

**Ne yapılmış?** Dynamics 365 status update sürecinde pahalı IOM/lisans + developer bakım katmanını n8n tabanlı daha basit entegrasyonla değiştirme.

**Ticari kanıt:** **S: up to $240K/year** self-report; yaklaşık `$160K/yıl licensing + $50–80K/yıl developer/maintenance` maliyeti. Geliştirme süresi 2,5 gün olarak bildiriliyor.

**Kaynak:** Reddit r/n8n real-business-problem thread'i.

**Risk:** Enterprise sistemlerde 2,5 günlük geliştirme süresi genellenemez. Regression, permissions, audit ve rollback gerekir.

**Senin için uygulama önizlemesi:** D365 seviyesine hemen girmek yerine Türkiye KOBİ'lerinde **“iki sistem arasında yalnızca durum/sipariş/stok alanı taşıyan pahalı ara yazılım var mı?”** diye bak. En küçük entegrasyon bile aylık yazılım aboneliğini kaldırabiliyorsa teklif çok netleşir.

---

## C078 — UK Private School / Exam Centre Data Workflow Retainer

**Ne satılmış?** Özel okul/sınav merkezinde farklı formatlarda gelen öğrenci/sınav verilerini temizleyip master spreadsheet üretme ve sezonluk veri toplama workflow'ları.

**Ticari kanıt:** Büyük tek seferlik ücret değil; geliştirici **yıllık retainer'ın biriktiğini** ve workflow'u kendisinin host ettiğini bildiriyor.

**Müşteri edinme:** Süreci elle yapan yönetici problemden bıkmış; demo sonrası kabul etmiş.

**Kaynak:** Reddit r/n8n real-business-problem thread'i.

**Senin için uygulama önizlemesi:** Türkiye'de kurs/özel okul/sınav merkezi için **farklı öğretmenlerden gelen Excel/form verisini tek master tabloya normalize etme**. AI yalnız serbest metin/kolon eşlemede yardımcı olabilir; öğrenci notu/karar üretmemeli.

---

## C079 — Warehouse Scan Latency Optimisation

**Ne yapılmış?** Depoda bir ürün scan edildiğinde kaydın yüklenme süresini **24 saniyeden 4 saniyeye** indiren teknik optimizasyon.

**Ticari kanıt:** Çalışan, fulfillment adedi × 20 saniye × işçilik maliyeti hesabıyla **S: ~$47K/yıl** iş gücü değeri çıkardığını bildiriyor.

**Önemli ders:** AI yok. “20 saniye” küçük görünür; yüksek frekansta ciddi para eder.

**Senin için uygulama önizlemesi:** İşletmede tek seferde büyük otomasyon aramak yerine **çok sık tekrarlanan 10–60 saniyelik beklemeleri** ölç. Barkod, CSV import, sipariş ekranı, dosya arama gibi gecikmeler yüksek hacimde iyi ROI vakalarına dönüşebilir.

---

## C080 — Shopify Dropship Backorder Detection + Self-Service

**Ne yapılmış?** Tedarikçi confirmation e-mail'lerinden backorder ve ship date çıkarılıyor, Google Sheet'e yazılıyor; mağazaya gömülü küçük app müşterinin siparişini sorguluyor; daha sonra AI agent aynı API'yi kullanarak durum cevabı veriyor.

**Ticari kanıt:** İşletme sahibi **S: yüzlerce saat/ay** tasarruf bildirmiş. AI-agent katmanı yeni olduğu için onun ayrı etkisi henüz ölçülmemiş.

**Kaynak:** Reddit r/n8n real-business-problem thread'i.

**Risk:** Yanlış shipment date müşteri güvenini etkiler. E-mail parsing fallback ve source timestamp saklanmalı.

**Senin için uygulama önizlemesi:** Türkiye'de distribütör/e-ticaret için **tedarikçi e-mail/PDF → geciken ürünler tablosu → müşteriye insan-onaylı durum ekranı**. AI chatbot zorunlu değil; önce temiz status data yarat.

---

## C081 — CRM Sync Replaces $3,500/month Middleware

**Ne yapılmış?** İki CRM/platform arasında veri taşıyan eski Windows Server + özel uygulama yerine birkaç API connection ve küçük data transform ile n8n sync.

**Ticari kanıt:** Eski tedarikçiye **S: $3.500/ay** bakım/bug-fix ücreti ödendiği bildiriliyor; yeni akış bunu ikame ediyor.

**Kaynak:** Reddit r/n8n real-business-problem thread'i.

**Risk:** Data loss, duplicate, conflict resolution ve rollback.

**Senin için uygulama önizlemesi:** Türkiye'de “eski yazılımdan yeni CRM/ERP'ye veri akıtmak için her ay para ödenen küçük bridge” vakalarını ara. İlk demo **read-only compare/report** olmalı; iki sisteme yazmaya sonra geç.

---

## C082 — Real-Estate Document Generation + E-Sign

**Ne yapılmış?** Online formlardan gayrimenkul belgeleri oluşturuluyor, validation uygulanıyor, e-sign platformuna gönderiliyor ve imza linki WhatsApp'a iletiliyor.

**Ticari kanıt:** Kaynak, şirketin **S: $4.000/ay hukuk ücreti** tasarruf ettiğini bildiriyor.

**Risk:** Çok yüksek. Hukuki belge üretiminde yanlış form/şart ciddi sonuç doğurabilir. Yerel hukukçu review ve şablon kilidi şart.

**Senin için uygulama önizlemesi:** Hukuki sözleşmeyle başlamamak gerek. Aynı teknik deseni **teklif, servis formu, teslim tutanağı, izin/onay formu, standart müşteri bilgi belgesi** gibi düşük-risk dokümanlarda uygula.

---

## C083 — B2B Manufacturing Tender Research Agent

**Ne yapılmış?** Üretici firma için tender/ihale araştırmasını bulma → temizleme → filtreleme → qualification zinciriyle otomatikleştirme.

**Ticari kanıt:** Kaynak, bu işin önceden satış müdürünün **neredeyse tam zamanlı işini** aldığını bildiriyor. Parasal rakam yok.

**Kaynak:** Reddit r/n8n real-business-problem thread'i.

**Risk:** İhale koşulunu yanlış yorumlama, deadline kaçırma, kaynak kapsamı.

**Senin için uygulama önizlemesi:** Eskişehir sanayisiyle çok uyumlu. İlk hizmet: **haftalık açık ihale/fırsat radarı + neden uygun olduğuna dair 3 maddelik özet + kaynak URL**. Başvuru yapma; yalnız research/triage.

---

## C084 — 44-Country Newsletter Localisation

**Ne yapılmış?** 44 ülkeye ayrı marka/dil varyasyonlu newsletter üretimi; product feed + template + brand voice + insan review.

**Ticari kanıt:** Yaklaşık **1.500 newsletter/yıl**. Manuelde ~4 saat/newsletter ≈ 6.000 saat; yeni akış 5–15 dakika/newsletter, **S: ~5.600 saat/yıl** tahmini tasarruf.

**Kaynak:** Reddit r/n8n real-business-problem thread'i.

**Risk:** Localization hatası, regülasyon/promosyon metni, marka tonu.

**Senin için uygulama önizlemesi:** 44 ülke değil; **Türkçe + İngilizce + bir ihracat pazarı** için ürün bülteni/teklif maili. Yerel LLM ilk taslak/translation yapabilir; final insan review şart.

---

## C085 — Renewable-Energy SMB: Claude as Business Automation Layer

**Ne yapılmış?** Yenilenebilir enerji şirketi sahibi; eski database ile HubSpot'u webhooks/scripts/Python ile birleştirme, Google Ads weekly reports, HTML proposals, P&L analysis ve business reporting gibi işleri Claude yardımıyla geliştirmiş.

**Ticari kanıt:** İşletme sahibi 2026 başından Ağustos'a kadar **S: $50K+ tasarruf** ettiğini self-report ediyor; kullandığı plan `$200/ay`.

**Kaynak:** Reddit r/ClaudeAI, 5 Ağustos 2026 “Claude from a small business perspective”.

**Risk:** Tek kişinin kendi tahmini; tasarruf kalemleri bağımsız audit edilmemiş.

**Senin için uygulama önizlemesi:** Bu vaka tek ürün değil, **AI-assisted internal ops** modeli. Türkiye KOBİ'sinde 3 küçük iş seç: haftalık reklam raporu, teklif PDF/HTML hazırlama, CRM veri senkronu. Her birinin önce/sonra süresini ölçerek gerçek ROI üret.

---

## C086 — $5K Grant-Funded Sales Analysis App

**Ne satılmış?** Bir işletmeye uygun `$5.000` grant bulunuyor; grant kapsamında satış verisini accounting software'den export edip statik uygulamada OpenAI API ile satış analizi/prediction yapan küçük custom app geliştiriliyor.

**Ticari kanıt:** Geliştirici **F: $5.000 collected** self-report ediyor; app'i yaklaşık bir günde hazırladığını söylüyor. İşletme kendi OpenAI API key'ini ödüyor.

**Kaynak:** Reddit r/ClaudeAI, 13 Haziran 2026 “Anyone here actually making money with stuff they built using Claude?” thread'i.

**Önemli ders:** Geliri sağlayan yalnız coding değil; **grant discovery + müşteriye demo/PDF + küçük uygulanabilir scope** kombinasyonu.

**Risk:** Hibe koşulları, çıkar çatışması, uygun olmayan hibe kullanımını teşvik etmemek; programa göre kurallar ayrı kontrol edilmeli.

**Senin için uygulama önizlemesi:** Türkiye/EU hibe danışmanlığı uzmanıymış gibi davranmadan, **KOSGEB/AB/dijitalleşme programlarında teknoloji harcamasına izin verilen alanları araştırıp**, hibe uzmanıyla partnerlik modeli düşünülebilir. İlk değer: küçük, açıkça tanımlı veri analizi/raporlama aracı.

---

## Cilt 7'den çıkan ortak desen

En yüksek ROI çoğu zaman “en zeki AI agent”ta değil:

- lisans maliyetini kaldırmak,
- tarihi yaklaşan stoğu erken görmek,
- 20 saniyelik yüksek-frekans gecikmeyi yok etmek,
- aynı veriyi tekrar tekrar kopyalamayı kaldırmak,
- insanın araştırdığı fırsatları önce filtrelemek,
- binlerce lokalizasyonun ilk taslağını makineye yaptırıp insana review bırakmak.

Bu cilt, Türkiye'de özellikle **sanayi, distribütörlük, eğitim operasyonu, e-ticaret ve eski-yeni yazılım entegrasyonu** tarafını daha derin araştırmaya değer hale getiriyor.
