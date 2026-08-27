# Büyük şirketlerde maliyet düşürme

Bu grubun ortak özelliği çoğunda yapay zekâ satılmaması: ödenen yazılım lisansı, harcanan insan saati veya sessizce sızan kayıp ölçülebilir biçimde azaltılıyor. En yüksek getiri çoğu zaman en akıllı sistemde değil; **her ay ödenen yazılım faturasını kaldırmakta, tarihi yaklaşan stoğu önceden görmekte ve günde yüzlerce kez tekrarlanan 20 saniyelik beklemeyi yok etmekte.**

**Türkiye'de kim satın alır?** Distribütör, üretici, depo, birden çok yazılım kullanan orta ölçekli şirket

**Bu grupta 6 örnek var.** Ne kadar güvenilir oldukları — C: 6.

Harflerin ne anlama geldiği için `../RESEARCH_POLICY.md`, gruplar arası ortak dersler için `DESENLER.md`, hepsini birden filtrelemek için [atlas sayfası](https://paradoksix.github.io/ai-money-workflows/).

---

## C006 — Automation Monitoring Dashboard

**Ne satılmış/yapılmış?** Bir ajansın çok müşterili n8n workflow'larını tek panelden izleyen dashboard: execution error, anomaly, raporlama, bakım.

**Ticari kanıt:** **11 müşteri / 115+ workflow** yöneten ajans.

**Değer:** Yeni otomasyon satmaktan ziyade mevcut otomasyonların bozulmasını erken yakalamak.

**Risk:** Müşteri credential'ları, loglarda kişisel veri, tek noktadan erişim riski.

**Senin için uygulama önizlemesi:** Bu hemen ilk müşteriye satılacak iş değil; fakat ansiklopedide önemli çünkü **retainer gelirinin nereden çıktığını** gösteriyor. İleride 3–5 müşteriye workflow kurulduğunda “aylık sağlık kontrolü + hata raporu + API değişikliği kontrolü” şeklinde doğal bakım ürünü olur.

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

**Ticari kanıt:** **S: up to $240K/year** kendi beyanı; yaklaşık `$160K/yıl licensing + $50–80K/yıl developer/maintenance` maliyeti. Geliştirme süresi 2,5 gün olarak bildiriliyor.

**Kaynak:** Reddit r/n8n real-business-problem thread'i.

**Risk:** Enterprise sistemlerde 2,5 günlük geliştirme süresi genellenemez. Regression, permissions, audit ve rollback gerekir.

**Senin için uygulama önizlemesi:** D365 seviyesine hemen girmek yerine Türkiye KOBİ'lerinde **“iki sistem arasında yalnızca durum/sipariş/stok alanı taşıyan pahalı ara yazılım var mı?”** diye bak. En küçük entegrasyon bile aylık yazılım aboneliğini kaldırabiliyorsa teklif çok netleşir.

---

## C079 — Warehouse Scan Latency Optimisation

**Ne yapılmış?** Depoda bir ürün scan edildiğinde kaydın yüklenme süresini **24 saniyeden 4 saniyeye** indiren teknik optimizasyon.

**Ticari kanıt:** Çalışan, fulfillment adedi × 20 saniye × işçilik maliyeti hesabıyla **S: ~$47K/yıl** iş gücü değeri çıkardığını bildiriyor.

**Önemli ders:** AI yok. “20 saniye” küçük görünür; yüksek frekansta ciddi para eder.

**Senin için uygulama önizlemesi:** İşletmede tek seferde büyük otomasyon aramak yerine **çok sık tekrarlanan 10–60 saniyelik beklemeleri** ölç. Barkod, CSV import, sipariş ekranı, dosya arama gibi gecikmeler yüksek hacimde iyi ROI vakalarına dönüşebilir.

---

## C081 — CRM Sync Replaces $3,500/month Middleware

**Ne yapılmış?** İki CRM/platform arasında veri taşıyan eski Windows Server + özel uygulama yerine birkaç API connection ve küçük data transform ile n8n sync.

**Ticari kanıt:** Eski tedarikçiye **S: $3.500/ay** bakım/bug-fix ücreti ödendiği bildiriliyor; yeni akış bunu ikame ediyor.

**Kaynak:** Reddit r/n8n real-business-problem thread'i.

**Risk:** Data loss, duplicate, conflict resolution ve rollback.

**Senin için uygulama önizlemesi:** Türkiye'de “eski yazılımdan yeni CRM/ERP'ye veri akıtmak için her ay para ödenen küçük bridge” vakalarını ara. İlk demo **read-only compare/report** olmalı; iki sisteme yazmaya sonra geç.

---

## C085 — Renewable-Energy SMB: Claude as Business Automation Layer

**Ne yapılmış?** Yenilenebilir enerji şirketi sahibi; eski database ile HubSpot'u webhooks/scripts/Python ile birleştirme, Google Ads weekly reports, HTML proposals, P&L analysis ve business reporting gibi işleri Claude yardımıyla geliştirmiş.

**Ticari kanıt:** İşletme sahibi 2026 başından Ağustos'a kadar **S: $50K+ tasarruf** ettiğini kendisi bildiriyor; kullandığı plan `$200/ay`.

**Kaynak:** Reddit r/ClaudeAI, 5 Ağustos 2026 “Claude from a small business perspective”.

**Risk:** Tek kişinin kendi tahmini; tasarruf kalemleri bağımsız audit edilmemiş.

**Senin için uygulama önizlemesi:** Bu vaka tek ürün değil, **AI-assisted internal ops** modeli. Türkiye KOBİ'sinde 3 küçük iş seç: haftalık reklam raporu, teklif PDF/HTML hazırlama, CRM veri senkronu. Her birinin önce/sonra süresini ölçerek gerçek ROI üret.

---
