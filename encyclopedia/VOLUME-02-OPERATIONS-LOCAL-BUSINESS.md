# Cilt 2 — Operasyon, back-office ve yerel işletme vakaları

Bu cilt **C001–C019** vakalarını içerir. Bunlarda ücretli müşteri, gelir, tasarruf veya gerçek production kullanımı yönünde güçlü ticari sinyal vardır; fakat exact kaynak repo/workflow çoğunlukla bulunamamıştır.

---

## C001 — Ship Manager Lead Capture

**Ne satılmış?** IMO numarasından gemi/ship manager bilgisi bulup şirket, domain ve iletişim enrichment'i yapan denizcilik lead araştırma sistemi.

**Müşteri problemi:** Denizcilikte doğru ship-management şirketini ve karar vericiyi elle bulmak çok zaman alıyor.

**Ticari kanıt:** Geliştirici bunun **ilk ücretli müşterisi** olduğunu bildiriyor.

**Stack:** Puppeteer + Equasis/WSD + Apify + n8n + AI enrichment.

**Risk:** Veri kaynaklarının kullanım şartları, scraping, güncel olmayan denizcilik verisi.

**Senin için uygulama önizlemesi:** Denizcilik Türkiye'de niş ama ihracatçı sanayi açısından desen çok değerli. Aynısını **“ürün kodu → üretici/distribütör → ülke → açık iletişim”** araştırmasına çevir. Örneğin Eskişehir'deki makine/metal üreticilerine belirli ülkelerde distribütör adayı listesi hazırlamak, aynı mantığın daha erişilebilir versiyonu.

---

## C002 — Japanese Google Ads Invoice Processor

**Ne satılmış?** Japon Google Ads faturalarındaki karmaşık/negatif satırları kurallı biçimde parse edip muhasebe sürecine hazırlayan sistem.

**Ticari kanıt:** **V/S: yaklaşık $2K/ay sistem değeri** bildiriliyor. Bunun freelancer ücreti mi yoksa müşteriye sağlanan değer mi olduğu net değil; bu yüzden rakam gelir diye yazılmıyor.

**Nasıl çalışıyor?** Deterministik parser + Claude structured output + Board API/Sheets benzeri iş akışı.

**Risk:** Finansal doğruluk; AI'nın rakam/vergi alanlarını yanlış okuması.

**Senin için uygulama önizlemesi:** Türkiye'de doğrudan muhasebe kaydı yazdırmak yerine **“PDF/e-posta faturası → firma/tarih/tutar/vergi/proje alanları → doğrulama kuyruğu → Excel”** olarak düşün. OCR/LLM yalnız veri çıkarır, matematik ve format kontrollerini normal kod yapar. Bu senin düşük maliyet tercihinle uyumlu.

---

## C003 — 50K Product Catalog Overhaul

**Ne satılmış?** 50.000+ ürün sayfasının açıklama, teknik özellik, SEO, kategori ve rakip eşlemesini topluca yenileme.

**Müşteri:** Büyük e-ticaret mağazası.

**Ticari kanıt:** Ücretli müşteri işi ve **50K+ SKU** ölçeği bildirilmiş; ücret açıklanmamış.

**Stack:** n8n + LLM + scraping + tablo/veri işleme.

**Risk:** Yanlış teknik özellik, yanlış kategori, SEO spam'i, yanlış rakip eşlemesi.

**Senin için uygulama önizlemesi:** Türkiye'de çok güçlü. Özellikle **oto yedek parça, hırdavat, elektrik malzemesi, mobilya, sanayi ekipmanı** katalogları. İlk araştırma demosu 100 satırlık dağınık CSV: eksik kolon, duplicate, kategori, teknik özellik ve düşük güvenli satırları işaretle. RTX 3060 üzerinde küçük yerel modelle metin normalizasyonu yapılabilir.

---

## C004 — Property Management Automation Vertical

**Ne satılmış?** Yalnız Alman property-management/Hausverwaltung şirketlerine yönelik bakım, kiracı talebi ve operasyon workflow'ları.

**Ticari kanıt:** 2025'te **20 müşteri**, daha sonra yaklaşık 23 müşteri seviyesinde büyüme ve özel n8n geliştiricisi işe alımı bildiriliyor.

**Problem:** Kiracı talepleri, bakım/arıza, tedarikçi koordinasyonu, durum takibi.

**Risk:** Kiracı kişisel verileri, yanlış aciliyet, otomatik tedarikçi yönlendirme.

**Senin için uygulama önizlemesi:** Türkiye'de **profesyonel site/apartman yönetim şirketleri** hedeflenebilir. İlk versiyon: WhatsApp/form/e-mail talebi → kategori (su, elektrik, asansör, temizlik, aidat) → yöneticiye temiz görev kartı. Usta atamasını insan yapsın.

---

## C005 — Bookkeeping Process Automation

**Ne satılmış?** Muhasebe firmasının belge/toplama/ön-muhasebe süreçlerini otomatikleştirme.

**Ticari sonuç:** **S: yaklaşık 600 saat/yıl doğrudan tasarruf**; ölçek etkisiyle 2.400 saat/~$30K ücret tasarrufu tahmini. Sonuç yalnız n8n'e değil yeni pre-accounting yazılımına da bağlı.

**Risk:** Vergi/muhasebe doğruluğu, yanlış sınıflandırma.

**Senin için uygulama önizlemesi:** Türkiye'de mali müşavirin resmi muhasebe kararını otomatikleştirmek yerine **belge toplama, dosya adlandırma, eksik evrak kontrolü, fatura alanlarını Excel'e çıkarma, müşteri hatırlatma** gibi ön süreçlere odaklan. Finansal kararı insanda bırak.

---

## C006 — Automation Monitoring Dashboard

**Ne satılmış/yapılmış?** Bir ajansın çok müşterili n8n workflow'larını tek panelden izleyen dashboard: execution error, anomaly, raporlama, bakım.

**Ticari kanıt:** **11 müşteri / 115+ workflow** yöneten ajans.

**Değer:** Yeni otomasyon satmaktan ziyade mevcut otomasyonların bozulmasını erken yakalamak.

**Risk:** Müşteri credential'ları, loglarda kişisel veri, tek noktadan erişim riski.

**Senin için uygulama önizlemesi:** Bu hemen ilk müşteriye satılacak iş değil; fakat ansiklopedide önemli çünkü **retainer gelirinin nereden çıktığını** gösteriyor. İleride 3–5 müşteriye workflow kurulduğunda “aylık sağlık kontrolü + hata raporu + API değişikliği kontrolü” şeklinde doğal bakım ürünü olur.

---

## C007 — Shopify Inventory Shock Absorber

**Ne yapılmış?** Çok yüksek hacimli inventory update/webhook akışını buffer/queue/rate-limit ederek Shopify tarafındaki yükü azaltan sistem.

**Ticari sonuç:** **S: $25K tasarruf iddiası**, ancak güvenilirlik ve exact source hâlâ doğrulama bekliyor.

**Risk:** Envanter yanlışlığı doğrudan satış kaybı doğurur; güçlü engineering gerekir.

**Senin için uygulama önizlemesi:** Şimdilik kopyalanacak iş değil, **yüksek hacim entegrasyon problemlerinin yüksek ticket olabileceğinin sinyali**. Senin için daha küçük versiyon: “stok feed'inde duplicate/update burst tespiti ve raporu”; otomatik stok yazma değil.

---

## C008 — Bookstore WhatsApp AI Order Assistant

**Ne satılmış?** Yerel kitapçıya WhatsApp'tan metin, ses, görsel/fiş alıp sipariş oluşturan ve sipariş durumunu yöneten asistan.

**Ticari kanıt:** **F: $500 ilk ücretli n8n projesi**. İşletme sahibinin saatler süren manuel destek yükünü azalttığı bildiriliyor.

**Stack:** Supabase + OpenAI + n8n + WhatsApp; voice/image/receipt handling.

**Risk:** Meta policy, sipariş hatası, ödeme/kişisel veri.

**Senin için uygulama önizlemesi:** Türkiye için çok doğal. Kitapçı yerine **oto yedek parça, çiçekçi, pet shop, teknik servis, butik gıda** düşünülebilir. İlk pilotta sipariş tamamlamasın: ürün adı/adet/teslimat bilgilerini toplayıp personele “hazır sipariş taslağı” bıraksın.

---

## C009 — HR Automation Packaged MVP

**Ne satılmış?** HR sürecini haritalayıp AI prompt logic + Sheets + Slack/Railway gibi araçlarla paketlenmiş operasyon MVP'si.

**Ticari kanıt:** **F: €3.000** self-report.

**Problem:** Dağınık aday/çalışan süreçleri ve manuel koordinasyon.

**Risk:** Çalışan/aday verisi, ayrımcılık, AI skorunun işe alım kararına dönüşmesi.

**Senin için uygulama önizlemesi:** İşe alım kararını AI'ya bırakma. **CV dosyalarını adlandırma, görüşme notunu özetleme, eksik belge takibi, aday durum panosu** gibi nötr idari süreçleri hedefle. Türkiye'de küçük işe alım danışmanlıkları bunun için uygun araştırma alanı.

---

## C010 — E-commerce Product Image Pipeline

**Ne satılmış?** Ürün mockup'larını AI ile üretip Drive/Sheets/WooCommerce zincirine aktaran içerik otomasyonu.

**Ticari kanıt:** **F iddiası: $3.000/ay** ve yaklaşık **25 saat/ay tasarruf**; iddia mentor üzerinden aktarıldığı için güven orta.

**Risk:** Ürün gerçeğine aykırı görsel, telif/marka.

**Senin için uygulama önizlemesi:** Tam otomatik WooCommerce publish yerine **ürün görsel seti üret → klasörle → insan onayı → upload-ready paket** modeli. Yerel PC'ni batch resize/background/metadata gibi işlerde kullanarak API maliyetini düşürebilirsin.

---

## C011 — Clinic Intake Copy-Paste Automation

**Ne yapılmış?** Form → spreadsheet → özet e-mail → shared folder gibi basit intake otomasyonu.

**Ticari sonuç:** **S: 10–12 saat/hafta** iddiası; geliştirici bunu yaklaşık `$30K/yıl` tasarrufa extrapole ediyor.

**Önemli nokta:** AI şart değil. Müşteri yalnız manuel kopyala-yapıştır işinden kurtulmak istiyor.

**Risk:** Sağlık verisi.

**Senin için uygulama önizlemesi:** Sağlık yerine **kurs kayıtları, servis talepleri, emlak müşteri formu, iş başvurusu evrak toplama** gibi düşük regülasyonlu süreçlerde aynı deseni ara. Bu vaka, bazen normal otomasyonun AI'dan daha doğru ürün olduğunu gösteriyor.

---

## C012 — Housing Association Self-Service Forms

**Ne yapılmış?** 3.000 kiracılı housing association'da self-service formlar ve website routing ile telefon/manuel işlem yükünü azaltma.

**Ticari sonuç:** Reddit yorumunda **S: ~£160K** tasarruf bildiriliyor; ikincil kanıt olduğu için temkinli.

**Risk:** Kamu/housing işlemlerinde erişilebilirlik ve doğru yönlendirme.

**Senin için uygulama önizlemesi:** Türkiye'de site yönetimi, belediye iştiraki veya büyük kooperatif gibi kurumlara direkt girmek yerine **küçük yönetim şirketlerinde sık sorulan talebi doğru forma yönlendiren portal** desenini araştır.

---

## C013 — 18 SMB Client AI Automation Portfolio

**Ne satılmış?** Çeşitli KOBİ'lere CRM, lead follow-up, Zapier/GPT ve operasyon otomasyonları.

**Ticari kanıt:** Yaklaşık **R/F: $75K / ~1 yıl**, ortalama proje ~$4.200, **8 retainer** self-report.

**Örnek değer:** Bir SaaS lead follow-up sisteminde yanıt süresinin yaklaşık 14 saatten 3 dakikanın altına indiği iddia ediliyor.

**Risk:** Self-report; tüm gelirin tek teknolojiye atfedilememesi.

**Senin için uygulama önizlemesi:** Bu vaka “AI agency kur” demiyor; **müşteride önce tek tekrar eden problem bul, sonra aynı müşteride ikinci/üçüncü süreci keşfet** modelini gösteriyor. Senin repo-temelli çalışma tarzın için her müşteri tipini case template olarak belgelemek yararlı olur.

---

## C014 — Daily Lead Finder + Personalized Outreach

**Ne yapılmış?** Her gün yeni lead bulup GPT ile kişiselleştirilmiş outreach hazırlayan sistem.

**Ticari sonuç:** **V: 40+ booked sales call/ay, 8 ay** self-report.

**Stack:** n8n + GPT + Google Sheets.

**Risk:** Attribution belirsizliği, spam, platform/ileti mevzuatı.

**Senin için uygulama önizlemesi:** Otomatik mesaj yollamayı değil **“haftalık 30 nitelikli şirket + neden uygun oldukları + kaynak link”** hizmetini araştır. Satış temsilcisi iletişimi kendisi yapsın; hukuki risk azalır.

---

## C015 — Stripe Overdue Invoice Chaser

**Ne yapılmış?** Gecikmiş Stripe faturalarını belirli günlerde farklı tonlarda e-mail ile takip eden sistem.

**Ticari sonuç:** **V: $4.200 alacağın 6 haftada geri kazanıldığı** bildiriliyor.

**Risk:** Yanlış müşteriye agresif hatırlatma, ödeme uyuşmazlığı.

**Senin için uygulama önizlemesi:** Türkiye'de Stripe yerine müşterinin kullandığı fatura/CRM/Sheet sisteminden **“vadesi geçenleri listeler + hazır hatırlatma taslağı üretir + insan onayı”** versiyonu araştırılabilir. Tahsilatı otomatik yapma.

---

## C016 — E-commerce Background AI Agents

**Ne yapılmış?** 20+ D2C markada abandoned cart, WISMO (“siparişim nerede?”), returns, descriptions, inventory alerts ve review handling gibi arka-ofis agent'ları.

**Ticari kanıt:** Geliştirici 20+ marka ile çalıştığını, markaların aylık yaklaşık `$12K–$250K` gelir ölçeğinde olduğunu bildiriyor.

**Risk:** Çok kapsamlı agent'lar hata zinciri yaratabilir.

**Senin için uygulama önizlemesi:** “E-ticaret agent paketi” diye başlamamak gerek. Tek atom seç: **WISMO taleplerini sipariş numarasına göre sınıflandırma**, **iade nedenlerini haftalık raporlama**, **stok uyarılarını temizleme**. Türkiye'de pazaryeri satıcıları için ölçülebilir.

---

## C017 — Real Estate AI Voice Lead Follow-up

**Ne satılmış?** Emlak broker'ına yeni lead geldikten yaklaşık 1 dakika içinde arayıp qualify eden ve randevu alan voice agent.

**Ticari kanıt:** Gerçek broker müşterisi; fiyat açıklanmamış.

**Stack:** Vapi + n8n + CRM/Sheet.

**Risk:** Kaynak post agresif tekrar aramayı anlatıyor; bunu kopyalamak hukuki/etik açıdan uygun değil. Consent/İYS kritik.

**Senin için uygulama önizlemesi:** Voice yerine **lead geldi → danışmana anında WhatsApp/Telegram/CRM bildirimi → lead özeti → cevap taslağı** deseni çok daha güvenli. Emlak ofisinde “hızlı insan yanıtı” sat.

---

## C018 — Tutoring Business Scheduling Agent

**Ne satılmış?** Öğretmen programlarını yöneten, Calendar'a yazan, WhatsApp reminder ve payment notification üreten eğitim operasyon sistemi.

**Ticari kanıt:** **F: $5.000**, geliştirici 2 günde kurduğunu ve production'da çalıştığını bildiriyor. 2 gün süresi yeni başlayan için referans değildir.

**Risk:** Öğrenci/veli verisi, ödeme bildirimi hatası.

**Senin için uygulama önizlemesi:** Türkiye'de **özel ders veren öğretmenler, dil kursları, küçük eğitim merkezleri** çok uygun. İlk araştırma ürünü: öğretmen müsaitliği + ders takvimi + hatırlatma + “ödendi/ödenmedi” takip tablosu. AI yalnız doğal dil talebini yapılandırsın.

---

## C019 — Coffee Shop QR Ordering Web App

**Ne satılmış?** Masadaki QR'dan sipariş verilen, yeniden markalanabilir küçük web uygulaması.

**Ticari kanıt:** **F: $700 tek sefer satış**; geliştirici üç dükkâna gittiğini ve ilk işletmenin kabul ettiğini söylüyor. Claude Code engineering'in büyük bölümünde kullanılmış.

**Risk:** POS/ödeme entegrasyonu eklenirse kapsam hızla büyür; bakım garantisi maliyet doğurur.

**Senin için uygulama önizlemesi:** Buradaki ders “QR app yap” değil, **hazır küçük bir yazılımı yüz yüze yerel işletmeye göstermek**. Türkiye'de kafe dışında küçük lokanta, çay evi, oyun salonu, beach club gibi yerlerde yalnız menü + masa kodu + sipariş taslağı seviyesinde değerlendirilebilir.

---

## Cilt 2'den çıkan ortak desen

Bu vakaların çoğunda müşteri AI satın almıyor. Müşteri şunlardan birini satın alıyor:

- saatler süren araştırmanın kısalması,
- dağınık belge/verinin temizlenmesi,
- yanlış kişiye giden talebin doğru yere yönlenmesi,
- cevap/randevu/tahsilat gecikmesinin azalması,
- WhatsApp/e-mail trafiğinin yapılandırılması,
- tekrar eden operasyonun insan kontrolüyle otomatikleşmesi.

Türkiye uyumu en yüksek vakalar: **C003 katalog, C004 site yönetimi, C005 muhasebe ön-işleme, C008 WhatsApp sipariş, C011 intake, C015 alacak takibi, C018 eğitim operasyonu ve C019 yerel küçük app**.
