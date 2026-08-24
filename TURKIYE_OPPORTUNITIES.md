# Türkiye'de Satılabilir İlk Nişler

Bu dosya, katalogdaki gerçek ticari vakaları Türkiye'deki küçük/orta işletmelere uyarlamak için hazırlanmış çalışma görünümüdür. Gelir garantisi değildir; hangi demo ve tekliflerin önce denenmeye değer olduğunu gösterir.

## 1. E-ticaret katalog doktorluğu

**Kaynak vaka:** 50K+ ürün sayfasının AI ile açıklama/spec/SEO açısından yenilenmesi, rakiplerin taranması ve kategorilerin yeniden eşlenmesi.

**Türkiye'de hedef:** yapı malzemesi, hırdavat, elektrik malzemesi, oto yedek parça, mobilya, endüstriyel ürün, pazaryeri satıcıları.

**Satılacak çıktı:**
- bozuk/eksik başlıkları normalize etme,
- eksik açıklama oluşturma,
- teknik özellikleri kolonlara ayırma,
- kategori eşleme,
- duplicate/bozuk ürün tespiti,
- insan kontrolü için düşük güvenli satırları işaretleme.

**Demo:** 100 satırlık dağınık CSV alıp temizlenmiş CSV + before/after raporu üret.

**Neden güçlü:** binlerce üründe ürün başına düşük ücret bile anlamlı proje büyüklüğüne dönüşür.

## 2. Muhasebe / reklam faturası veri çıkarma

**Kaynak vaka:** Japon Google Ads faturalarının hibrit kod + Claude + structured output ile işlenmesi; yaklaşık `$2k/month` değer bildirimi.

**Türkiye'de hedef:** dijital ajanslar, mali müşavirler, çok şubeli işletmeler, e-ticaret şirketleri.

**Satılacak çıktı:**
- PDF/e-posta faturalarını alma,
- firma/tarih/tutar/vergi/proje bilgisini çıkarma,
- reklam platformu veya gider türüne göre sınıflandırma,
- Google Sheets/ERP/muhasebe ön kayıt tablosuna aktarma,
- güven düşükse insan onayına gönderme.

**Demo:** 10 örnek fatura üzerinde otomatik çıkarım + kontrol ekranı.

**Kritik:** finansal veride AI tek başına karar vermemeli; doğrulama ve insan onayı şart.

## 3. Emlak / site yönetimi bakım talebi otomasyonu

**Kaynak vaka:** Alman property-management otomasyon şirketinin 2025 içinde 20 müşteri edinmesi ve yalnız bu dikeyde n8n geliştiricileri çalıştırması.

**Türkiye'de hedef:** site yönetimleri, profesyonel apartman yönetim şirketleri, emlak portföy yöneticileri.

**Satılacak çıktı:**
- kiracı/sakin e-posta veya formunu sınıflandırma,
- arıza türü + aciliyet çıkarma,
- uygun usta/tedarikçiye yönlendirme,
- yanıt gelmezse takip,
- yönetici için haftalık sorun özeti.

**Demo:** su kaçağı / elektrik / asansör / temizlik / aidat kategorilerinde 30 sahte talebi işleyen workflow.

## 4. B2B lead araştırma motoru

**Kaynak vakalar:** LinkedIn Jobs + Decision Maker Research ve B2B Lead Search Engine; ikisi de ticari müşteri/ödeme sinyali taşıyor ve exact repo açık.

**Türkiye'de hedef:** personel danışmanlığı, endüstriyel tedarikçi, yazılım ajansı, makine üreticisi, ihracatçı, kurumsal eğitim firması.

**Satılacak çıktı:**
- hedef şirketleri bulma,
- karar verici rolünü belirleme,
- kamuya açık iletişim verisini zenginleştirme,
- CRM/Sheet'e yazma,
- satış temsilcisine kısa araştırma notu hazırlama.

**Demo:** Eskişehir veya İstanbul'da tek bir B2B dikey için 50 şirketlik temiz lead listesi.

**Kritik:** KVKK, platform kullanım koşulları ve ticari ileti izinleri ayrı kontrol edilmelidir.

## 5. İşe alım ajansları için yeni ilan radar sistemi

**Kaynak vaka:** Texas'taki inşaat staffing ajansı için LinkedIn ilanlarını sürekli izleyen ve hiring manager bulan workflow; geliştirici daha sonra birden fazla müşterinin aynı sistemi istediğini bildiriyor.

**Türkiye'de hedef:** insan kaynakları danışmanlıkları, mavi yaka personel firmaları, teknik işe alım ajansları.

**Satılacak çıktı:** yeni ilanı erken yakala → şirketi/karar vericiyi araştır → CRM'e yaz → satış ekibine bildir.

## Öncelik sırası

Sıfırdan demo üretme kolaylığı + yerel satış ihtimali birlikte düşünülünce:

1. E-ticaret katalog doktorluğu
2. B2B lead araştırması
3. Emlak/site yönetimi talepleri
4. Muhasebe/fatura ön işleme
5. İşe alım ilan radarı

İlk hedef, tek bir dikeyde çalışan küçük demo ve ölçülebilir önce/sonra çıktısı üretmektir; genel amaçlı “AI otomasyonu yapıyoruz” teklifi hazırlamak değildir.
