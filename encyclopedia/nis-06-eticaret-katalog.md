# E-ticaret ve ürün kataloğu

Ürün bilgisi, katalog kalitesi, stok akışı ve satış sonrası işler. Türkiye için en uygun gruplardan biri: oto yedek parça, hırdavat, elektrik malzemesi, mobilya ve sanayi ekipmanı kataloglarında aynı dertler açıkça duruyor. C003'ün notu grubun özeti: **asıl değer otomasyon aracında değil, dağınık veriyi toparlamakta.**

**Türkiye'de kim satın alır?** Oto yedek parça, hırdavat, mobilya, sanayi ekipmanı, pazaryeri satıcısı

**Bu grupta 7 örnek var.** Ne kadar güvenilir oldukları — C: 7.

Harflerin ne anlama geldiği için `../RESEARCH_POLICY.md`, gruplar arası ortak dersler için `DESENLER.md`, hepsini birden filtrelemek için [bütün örnekler sayfası](https://paradoksix.github.io/ai-money-workflows/tum-vakalar.html).

---

## C003 — 50K Product Catalog Overhaul

**Ne satılmış?** 50.000+ ürün sayfasının açıklama, teknik özellik, SEO, kategori ve rakip eşlemesini topluca yenileme.

**Müşteri:** Büyük e-ticaret mağazası.

**Ticari kanıt:** Ücretli müşteri işi ve **50K+ SKU** ölçeği bildirilmiş; ücret açıklanmamış.

**Stack:** n8n + LLM + scraping + tablo/veri işleme.

**Risk:** Yanlış teknik özellik, yanlış kategori, SEO spam'i, yanlış rakip eşlemesi.

**Senin için uygulama önizlemesi:** Türkiye'de çok güçlü. Özellikle **oto yedek parça, hırdavat, elektrik malzemesi, mobilya, sanayi ekipmanı** katalogları. İlk araştırma demosu 100 satırlık dağınık CSV: eksik kolon, duplicate, kategori, teknik özellik ve düşük güvenli satırları işaretle. RTX 3060 üzerinde küçük yerel modelle metin normalizasyonu yapılabilir.

---

## C007 — Shopify Inventory Shock Absorber

**Ne yapılmış?** Çok yüksek hacimli inventory update/webhook akışını buffer/queue/rate-limit ederek Shopify tarafındaki yükü azaltan sistem.

**Ticari sonuç:** **S: $25K tasarruf iddiası**, ancak güvenilirlik ve kaynak kodu hâlâ doğrulama bekliyor.

**Risk:** Envanter yanlışlığı doğrudan satış kaybı doğurur; güçlü engineering gerekir.

**Senin için uygulama önizlemesi:** Şimdilik kopyalanacak iş değil, **yüksek hacim entegrasyon problemlerinin yüksek ticket olabileceğinin sinyali**. Senin için daha küçük versiyon: “stok feed'inde duplicate/update burst tespiti ve raporu”; otomatik stok yazma değil.

---

## C010 — E-commerce Product Image Pipeline

**Ne satılmış?** Ürün mockup'larını AI ile üretip Drive/Sheets/WooCommerce zincirine aktaran içerik otomasyonu.

**Ticari kanıt:** **F iddiası: $3.000/ay** ve yaklaşık **25 saat/ay tasarruf**; iddia mentor üzerinden aktarıldığı için güven orta.

**Risk:** Ürün gerçeğine aykırı görsel, telif/marka.

**Senin için uygulama önizlemesi:** Tam otomatik WooCommerce publish yerine **ürün görsel seti üret → klasörle → insan onayı → upload-ready paket** modeli. Yerel PC'ni batch resize/background/metadata gibi işlerde kullanarak API maliyetini düşürebilirsin.

---

## C016 — E-commerce Background AI Agents

**Ne yapılmış?** 20+ D2C markada abandoned cart, WISMO (“siparişim nerede?”), returns, descriptions, inventory alerts ve review handling gibi arka-ofis agent'ları.

**Ticari kanıt:** Geliştirici 20+ marka ile çalıştığını, markaların aylık yaklaşık `$12K–$250K` gelir ölçeğinde olduğunu bildiriyor.

**Risk:** Çok kapsamlı agent'lar hata zinciri yaratabilir.

**Senin için uygulama önizlemesi:** “E-ticaret agent paketi” diye başlamamak gerek. Tek atom seç: **WISMO taleplerini sipariş numarasına göre sınıflandırma**, **iade nedenlerini haftalık raporlama**, **stok uyarılarını temizleme**. Türkiye'de pazaryeri satıcıları için ölçülebilir.

---

## C028 — Custom E-commerce Integration Projects

**Ne satılmış?** Online mağazalara özel API ve operasyon entegrasyonları.

**Ticari kanıt:** Geliştirici **F: $3K–$5K/proje**, 10–20 saat/hafta manuel işi azaltma ve `$300–$1K+` retainer önerisi bildiriyor.

**Güven:** Reddit thread'inde AI-benzeri yazım/promosyon şüphesi bulunduğu için orta.

**Senin için uygulama önizlemesi:** Büyük “e-commerce integration” yerine **tek akış** ara: stok CSV import, sipariş export, kargo durumu eşleme, iade nedenleri raporu, katalog normalizasyonu. Türkiye'de Shopify kadar WooCommerce/yerel ERP/pazaryeri CSV akışları da önemli.

---

## C041 — AI Product Photography + lifestyle/model scene

**Ne satılmış?** Ürün fotoğrafını farklı lifestyle sahnelerine veya AI model görsellerine yerleştirme.

**Ticari sinyal:** **74 review**, görünür yaklaşık `$50–100` order örneği.

**Risk:** Ürünün gerçekte olmayan özelliklerini göstermek; insan/model kullanımında yanıltıcılık.

**Senin için uygulama önizlemesi:** Türkiye'deki Trendyol/Hepsiburada satıcılarına **“5 gerçek ürün fotoğrafından 10 sosyal medya lifestyle görseli”** gibi dar paket düşünülebilir. Ürünün şekli/renk/etiketini değiştirmeyen QA şartı ekle.

---

## C080 — Shopify Dropship Backorder Detection + Self-Service

**Ne yapılmış?** Tedarikçi confirmation e-mail'lerinden backorder ve ship date çıkarılıyor, Google Sheet'e yazılıyor; mağazaya gömülü küçük app müşterinin siparişini sorguluyor; daha sonra AI agent aynı API'yi kullanarak durum cevabı veriyor.

**Ticari kanıt:** İşletme sahibi **S: yüzlerce saat/ay** tasarruf bildirmiş. AI-agent katmanı yeni olduğu için onun ayrı etkisi henüz ölçülmemiş.

**Kaynak:** Reddit r/n8n real-business-problem thread'i.

**Risk:** Yanlış shipment date müşteri güvenini etkiler. E-mail parsing fallback ve source timestamp saklanmalı.

**Senin için uygulama önizlemesi:** Türkiye'de distribütör/e-ticaret için **tedarikçi e-mail/PDF → geciken ürünler tablosu → müşteriye insan-onaylı durum ekranı**. AI chatbot zorunlu değil; önce temiz status data yarat.

---
