# Catalog Doctor — Clean-room MVP

İlk build dalgasının ürün #1'i. Geniş SKU'lu ürün kataloglarını kaynak dosyayı değiştirmeden audit eder; temizlenmiş çıktı ve insan-kontrol kuyruğu üretir.

## Ne yapıyor?

- CSV ayırıcısını otomatik algılar: `,`, `;`, tab veya `|`.
- Hücrelerde whitespace/Unicode temizliği yapar.
- Ürün adı, açıklama, kategori ve SKU kolonlarını yaygın Türkçe/İngilizce adlardan otomatik bulmaya çalışır.
- Eksik alan, eksik başlık/kategori, duplicate başlık ve duplicate SKU işaretler.
- Orijinal CSV'ye dokunmaz.
- `cleaned.csv`, `audit.csv` ve `summary.json` üretir.
- İsteğe bağlı olarak yerel **Ollama** modeli ile sorunlu satırlara temiz başlık ve kategori önerisi ekler.
- AI düşük güven verirse veya hata olursa satırı otomatik onaylamaz; `review_required=yes` bırakır.

## Neden yerel Ollama?

İlk MVP'de ücretli API zorunlu olmasın ve müşteri kataloğunu gereksiz yere üçüncü tarafa göndermeyelim. AI kapalıyken de deterministik audit çalışır.

Örnek uygun modeller:

```text
qwen2.5:7b
qwen3:8b
llama3.1:8b
```

Donanıma göre daha küçük model seçilebilir.

## Kullanım

AI olmadan:

```bash
python catalog_doctor.py sample_catalog.csv --out demo-output
```

Ollama ile yalnız sorunlu satırlara AI önerisi:

```bash
ollama pull qwen2.5:7b
python catalog_doctor.py sample_catalog.csv --out demo-output --ollama-model qwen2.5:7b
```

Her satıra AI önerisi:

```bash
python catalog_doctor.py sample_catalog.csv --out demo-output --ollama-model qwen2.5:7b --ai-all
```

## Çıktılar

### `audit.csv`
Her problemli satır için:
- CSV satırı,
- SKU,
- ürün adı,
- problem türleri,
- eksik alanlar,
- insan kontrolü gerekip gerekmediği,
- varsa AI başlık/kategori önerisi ve confidence.

### `cleaned.csv`
Temizlenmiş orijinal kolonlar + AI öneri kolonları. AI önerisi mevcut alanın üzerine yazılmaz; ayrı kolonda tutulur.

### `summary.json`
Demo/satış görüşmesinde kullanılabilecek before/after metriklerini verir.

## Satılabilir ilk paket

Müşteriye “AI katalog sistemi” değil şu çıktı satılır:

> Kataloğunuzdan 100 ürünü ücretsiz/ucuz audit edelim; eksik, duplicate ve kategori sorunu sayısını çıkaralım. Sorun anlamlıysa tüm kataloğu temizleyip insan-onaylı CSV olarak teslim edelim.

İlk hedef sektörler: oto yedek parça, hırdavat, elektrik/yapı malzemesi, mobilya ve geniş kataloglu pazaryeri satıcıları.

## MVP sınırları

- Excel `.xlsx` henüz doğrudan okunmuyor; CSV export gerekli.
- Kategori taksonomisi müşteriye özel değil; AI yalnız öneri verir.
- Ürün özellikleri henüz kolonlara otomatik parse edilmiyor.
- E-ticaret API'lerine otomatik push yok.
- Üretim kullanımında müşterinin veri şeması ve kategori sözlüğü için ayrı mapping katmanı eklenmeli.

## Sonraki sürüm

1. `.xlsx` desteği.
2. Müşteri kategori sözlüğüne constrained mapping.
3. Teknik özellik extraction.
4. Confidence threshold + review web UI.
5. Shopify/WooCommerce/Trendyol export adaptörleri.
6. Satır başına değişiklik günlüğü ve geri alma.
