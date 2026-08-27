# Build Shortlist — Türkiye'de İlk Kurulacak 10 İş

Bu liste, katalogdaki ticari vakaları **Türkiye'de müşteri bulma kolaylığı + demo üretme hızı + tekrar satılabilirlik + teknik risk** açısından sıralar. Gelir garantisi değildir. Amaç tek seferlik oyuncak demolar değil, aynı çekirdeği birden fazla müşteriye uyarlayabileceğimiz ürünleşmiş hizmetler çıkarmaktır.

> Bu build dalgası şu anda duraklatılmıştır; repo araştırma aşamasındadır. Anılan vaka kodlarının tam anlatımı için [`ENCYCLOPEDIA.md`](ENCYCLOPEDIA.md) niş indeksine veya filtrelenebilir [atlas sayfasına](docs/index.html) bakın.

## Dalga 1 — Önce bunları kur

### 1. E-ticaret katalog doktoru
**Kaynak:** C003 — 50K+ Product Catalog Overhaul

**Hedef müşteri:** oto yedek parça, hırdavat, elektrik malzemesi, yapı malzemesi, mobilya ve geniş SKU'lu pazaryeri satıcıları.

**İlk MVP:** CSV/XLSX yükle → başlık/spec/kategori/duplicate analizi → düşük güvenli satırları insan onayına ayır → temiz CSV indir.

**Neden #1:** müşteri problemi çok görünür; demo için dış API şart değil; yüzlerce/binlerce SKU olduğunda değer kolay ölçülür.

**İlk satış metriği:** 100 ürünlük ücretsiz/ucuz audit ile kaç bozuk veya eksik kayıt bulunduğu.

### 2. B2B lead araştırma ve zenginleştirme motoru
**Kaynak:** A002, A003, A005 ve C001

**Hedef müşteri:** sanayi tedarikçisi, ihracatçı, personel ajansı, makine üreticisi, B2B yazılım/ajans, emlak proje satışı.

**İlk MVP:** sektör + şehir → hedef şirketler → karar verici rolü → kamuya açık şirket/iletişim bilgisi → kısa satış araştırma notu → Sheet/CRM.

**Kaynak avantajı:** üç A-seviye workflow çekirdeği var; A005'in `$1,800` gerçek müşteri vakası ve exact JSON'u doğrulandı.

**Kritik:** KVKK, platform ToS ve ticari elektronik ileti kuralları ayrı ele alınmalı. Scraping'i kör spam sistemine çevirmeyiz.

### 3. Muhasebe/fatura ön işleme
**Kaynak:** C002, C005 ve C015

**Hedef müşteri:** mali müşavir, dijital ajans, e-ticaret firması, çok şubeli işletme.

**İlk MVP:** e-posta/PDF → firma/tarih/tutar/vergi/proje → kurallı validasyon → düşük güvenli alan için insan onayı → Sheet/ERP ön kayıt.

**Neden güçlü:** ROI; harcanan idari saat veya bulunan tahsilat doğrudan ölçülebilir.

**Kritik:** finansal kayıtları LLM'e kör bırakma; deterministik kontroller + insan onayı zorunlu.

### 4. Yerel işletme WhatsApp sipariş/asistan sistemi
**Kaynak:** C008 ve C027

**Hedef müşteri:** kitapçı, pet shop, çiçekçi, butik mağaza, teknik servis, yedek parça satıcısı.

**İlk MVP:** müşteri mesajı → ürün/işlem niyeti → katalog/stock sorgusu → sipariş veya servis talebi → insan devri → yönetim paneli/Sheet.

**Ticari sinyal:** kitapçı vakasında ilk ücretli proje `$500`; teknik servis vakasında 80+ saat/ay tekrarlı destek yükünün kaldırıldığı bildiriliyor.

**Kritik:** prod müşteride resmi/izinli WhatsApp Business entegrasyonu tercih et. Unofficial session emülatörünü kritik müşteri altyapısına bağımlılık yapma.

### 5. Kahveci/restoran QR sipariş mikro-uygulaması
**Kaynak:** C019

**Hedef müşteri:** kafe, kahveci, küçük restoran, beach/camp işletmesi, otel havuz/oda servisi.

**İlk MVP:** QR → masa tanıma → menü → sipariş → mutfak/kasa ekranı veya Telegram/WhatsApp bildirimi → basit yönetim paneli.

**Ticari sinyal:** kaynak vakada ilk kahveci `$700` tek seferlik satın alma yapmış.

**Neden iyi:** işletme sahibine yüz yüze 30 saniyede gösterilebilen ürün; aynı kod tabanı farklı markalara uyarlanabilir.

## Dalga 2 — İlk satışlardan sonra

### 6. Emlak/site yönetimi bakım ve mesaj triyajı
**Kaynak:** C004 ve C017

Kiracı/sakin taleplerini sınıflandır; aciliyet/usta kategorisi çıkar; iş emri oluştur; durum takibi yap; yöneticiye özetle. Emlak lead tarafında hızlı geri dönüş eklenebilir fakat sesli/otomatik aramada açık izin ve makul tekrar politikası gerekir.

### 7. Klinik/ofis intake otomasyonu
**Kaynak:** C011

Form/e-posta/WhatsApp'tan gelen bilgiyi tek forma normalize et; belge klasörü oluştur; personele özet ve takip görevi üret. Tıbbi karar verme yok; yalnız idari süreç.

### 8. Eğitim işletmesi scheduling + ödeme bildirim sistemi
**Kaynak:** C018

Öğretmen uygunluğu + takvim + öğrenci/veli hatırlatmaları + ödeme bildirimi. Kaynak vaka `$5,000` ücret bildiriyor. Türkiye'de özel ders merkezi, dil kursu ve online öğretmen ekipleri hedeflenebilir.

### 9. E-ticaret görsel/içerik üretim pipeline'ı
**Kaynak:** C010 ve A001

Ürün fotoğrafı/brief → görsel varyasyonları → açıklama/metadata → insan onayı → Drive/WooCommerce/Shopify. Önce gerçek müşteri markası üzerinde kontrollü demo; telif/marka tutarlılığı denetimi şart.

### 10. Automation maintenance / monitoring aboneliği
**Kaynak:** C006

Kurulum satıldıktan sonra aylık bakım ürünü: workflow health-check, başarısız run alarmı, API/model maliyet raporu, örnek çıktı kalite denetimi, credentials/expiry kontrolü. Kaynak vaka 11 müşteri ve 115+ workflow yönetildiğini bildiriyor.

## Uygulama sırası

1. `catalog-doctor` demosu — dış servis bağımlılığı minimum.
2. A005 hukuk lead-gen workflow'unu incele; Türkiye için sektör-genel lead motoruna temiz biçimde uyarlama planı çıkar.
3. `invoice-intake` demosu — test faturaları ve insan-onay kuyruğu.
4. `local-commerce-assistant` — resmi mesajlaşma API'si kullanan sürüm.
5. `qr-ordering` — yeniden markalanabilir tek kod tabanı.

İlk beş ürün için ortak kural: müşteriye “AI” satma. Tek cümlelik ölçülebilir çıktı sat: **katalog temizle, lead bul, faturayı işle, siparişi kaydet, masadan sipariş al.**
