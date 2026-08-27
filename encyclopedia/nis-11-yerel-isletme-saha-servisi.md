# Yerel işletme & saha servisi

Mahalledeki işletmeye yüz yüze satılabilen sistemler: teknik servis, kitapçı, kafe, oto servis. Ansiklopedinin **en güçlü tek vakası (A006)** burada — 7 workflow'luk, iki yıl production'da çalışmış, exact kaynağı doğrulanmış bir sistem. Ortak desen: AI fiyat uydurmasın, gerçek tablodan okusun.

**Türkiye'de kim satın alır?** Teknik servis, kitapçı, kafe, oto servis, pet shop, çiçekçi

**Bu nişte 5 vaka var.** Kanıt dağılımı — A: 1 · B: 1 · C: 3.

Kanıt dereceleri için `../RESEARCH_POLICY.md`, nişler arası kesişen dersler için `DESENLER.md`, tüm vakaların filtrelenebilir listesi için `../docs/index.html`.

---

## A006 — Jacobo Device Repair WhatsApp + Voice AI Agent

**Kanıt seviyesi:** A — ticari vaka + exact kaynak

16 yıllık cihaz tamir işletmesinde randevu, gerçek fiyat tablosundan teklif, stok/iç sipariş ve insan devrini yöneten 7 workflow'luk çok-ajanlı production sistemi. Ayrı freelance satış ücreti yok; işletmeyle birlikte devredilen operasyonel varlık.

👉 Tam vaka kartı: [`A006-JACOBO-DEVICE-REPAIR.md`](A006-JACOBO-DEVICE-REPAIR.md)

---

## B006 — Auto Repair Shop Gmail Agent

**Ne yapıyor?** Oto servise gelen quote talebinde marka/model/araç bilgileri eksikse takip sorusu soruyor; yeterliyse ilgili kişiye SMS/iş akışı başlatıyor.

**Kanıt:** Exact workflow açık; ücret yok.

**Risk:** Yanlış sınıflandırma ve müşteriye yanlış fiyat/vaat.

**Senin için uygulama önizlemesi:** Türkiye için çok güçlü. İlk pilot **“WhatsApp/e-mail talebi → plaka/marka/model/şikâyet bilgisini tamamla → servis danışmanına temiz fiş bırak”** olmalı. Fiyatı AI vermesin; yalnız veri toplasın.

---

## C008 — Bookstore WhatsApp AI Order Assistant

**Ne satılmış?** Yerel kitapçıya WhatsApp'tan metin, ses, görsel/fiş alıp sipariş oluşturan ve sipariş durumunu yöneten asistan.

**Ticari kanıt:** **F: $500 ilk ücretli n8n projesi**. İşletme sahibinin saatler süren manuel destek yükünü azalttığı bildiriliyor.

**Stack:** Supabase + OpenAI + n8n + WhatsApp; voice/image/receipt handling.

**Risk:** Meta policy, sipariş hatası, ödeme/kişisel veri.

**Senin için uygulama önizlemesi:** Türkiye için çok doğal. Kitapçı yerine **oto yedek parça, çiçekçi, pet shop, teknik servis, butik gıda** düşünülebilir. İlk pilotta sipariş tamamlamasın: ürün adı/adet/teslimat bilgilerini toplayıp personele “hazır sipariş taslağı” bıraksın.

---

## C019 — Coffee Shop QR Ordering Web App

**Ne satılmış?** Masadaki QR'dan sipariş verilen, yeniden markalanabilir küçük web uygulaması.

**Ticari kanıt:** **F: $700 tek sefer satış**; geliştirici üç dükkâna gittiğini ve ilk işletmenin kabul ettiğini söylüyor. Claude Code engineering'in büyük bölümünde kullanılmış.

**Risk:** POS/ödeme entegrasyonu eklenirse kapsam hızla büyür; bakım garantisi maliyet doğurur.

**Senin için uygulama önizlemesi:** Buradaki ders “QR app yap” değil, **hazır küçük bir yazılımı yüz yüze yerel işletmeye göstermek**. Türkiye'de kafe dışında küçük lokanta, çay evi, oyun salonu, beach club gibi yerlerde yalnız menü + masa kodu + sipariş taslağı seviyesinde değerlendirilebilir.

---

## C027 — Device Repair WhatsApp + Voice Agent

**Ne yapılmış?** Tamir dükkânında randevu, teklif, stok, iç sipariş, FAQ ve insan devrini WhatsApp + voice üzerinden yöneten sistem.

**Ticari sonuç:** **S: 80+ saat/ay** tekrar eden destek işinin kaldırıldığı; sistemin **1 yıldan uzun** çalıştığı ve işletme satıldığında yeni sahibin kullanmaya devam ettiği; run cost'un `<€200/ay` olduğu bildiriliyor.

**Stack:** n8n + WhatsApp + ElevenLabs + operasyon entegrasyonları.

**Risk:** Voice/WhatsApp maliyeti, yanlış teklif, müşteri verisi.

**Senin için uygulama önizlemesi:** Türkiye'de **telefon/tablet/PC servisi, motosiklet servisi, beyaz eşya tamiri** için çok doğal. İlk atom: “mesajdan cihaz/marka/model/arıza/servis türünü çıkar → eksik bilgiyi sor → personele özet bırak.” Voice ve stok entegrasyonu daha sonra.

---
