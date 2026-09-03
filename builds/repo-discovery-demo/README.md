# Keşif motoru — sıfır maliyetli demo

Arşivi tek tek kart olarak gezdiren, arşiv tükenince GitHub'da arşivde **olmayan** benzer depoları öneren statik bir sayfa. Sunucusu yok, ücretli servis kullanmıyor ve **hiçbir yapay zekâ modeline istek atmıyor** — bütün eşleştirme tarayıcıda, sabit kurallarla yapılıyor.

Arşive veri **yazmaz**. Yeni vaka üretmez. Ne göstereceğine `data/cases.csv` karar verir.

## İki aşama

**1. Arşiv aşaması (açılıştaki hâli).** `data/cases.csv`'yi okur ve kayıtları teker teker kart olarak gösterir. Kartta vakanın adı, özeti, bildirilen sonucu ve altı ölçüsü var: kanıt derecesi, gelir türü, Türkiye'de satılabilirlik, zorluk, iş modeli, müşteri tipi. Üstteki "Arşiv odağı" listesiyle daraltılabilir (yalnız A dereceliler, yalnız depo adresi olanlar, yalnız yerel işletmeye satılabilirler gibi).

**2. Sınır aşaması.** Seçilen odaktaki bütün vakalar görüldükten sonra kendiliğinden devreye girer. `cases.csv`'den çıkardığı desenlerle GitHub'da arama yapar ve **arşivde kaydı olmayan** depoları gösterir. Bu kartlar açıkça "arşivde kayıtlı değil; gelir kanıtı değil" diye işaretlenir — bir aday, kanıtlanmış bir vaka değildir.

## İki düğme

- **Wiki** — vakanın ansiklopedi metnini sayfadan ayrılmadan açar. Komşu Wiki sayfasını çeker, ilgili vaka bölümünü ayıklar, script/iframe/form gibi her şeyi temizler ve gömer.
- **Derin analiz** — arşiv kartında künyenin düzenli hâlini; sınır kartında "bu neden bulundu" izini gösterir: hangi sorgu, hangi desen, hangi vaka kimliklerinden türedi ve arşivdeki en yakın örnekler hangileri.

## Çalıştırma

**`docs/` kökünden servis et, bu klasörden değil:**

```bash
python3 -m http.server 8080 --directory docs
# http://localhost:8080/repo-discovery/
```

Wiki düğmesi ansiklopedi sayfalarını `../nis-02-b2b-satis-lead.html` gibi göreli adreslerle çeker. Bu klasörün içinden servis edilirse o adresler boşa çıkar ve **Wiki düğmesi çalışmaz**; sayfanın geri kalanı çalışıyor göründüğü için hata da fark edilmez.

## Ağa çıktığı yerler — hepsi bu

| Nereye | Ne zaman |
|---|---|
| `raw.githubusercontent.com/.../data/cases.csv` | Açılışta, arşivi okumak için |
| `api.github.com/search/repositories` | Yalnız sınır aşamasında, aday aramak için |
| `api.github.com/repos/{depo}/readme` | Yalnız sınır aşamasında ve yalnız derin analiz istenirse |
| Aynı sunucudaki `../nis-*.html` | Wiki düğmesine basılırsa |

Arşivi her zaman `main` dalından okur. Yani yerelde çalıştırsan bile **yayındaki veriyi** gösterir; yerel `cases.csv` değişikliğin sayfaya yansımaz.

## Saklama ve gizlilik

- Görülen vakalar `localStorage`'daki `amw_seen` anahtarında tutulur; dışa aktarılıp geri yüklenebilir (JSON).
- GitHub erişim anahtarı **isteğe bağlıdır** ve yalnız sekme ömrü boyunca `sessionStorage`'da durur. Hiçbir dosyaya, adrese ya da kalıcı depoya yazılmaz. Anahtarın tek etkisi GitHub'ın saatlik istek sınırını yükseltmektir; onsuz da çalışır.
- Dışarıdan gelen her metin ekrana basılmadan önce kaçırılır; çekilen Wiki bölümü temizlenmeden gömülmez; dış bağlantılar `rel=noreferrer` ile açılır.

## `docs/repo-discovery/` ile ilişkisi

`docs/repo-discovery/` bu klasörün **birebir kopyasıdır** (`README.md` hariç) ve **elle** güncellenir — üreten bir script yok. Burada bir dosyayı değiştirirsen aynısını oraya da kopyala; `archive-discovery.yml` ve `card-metric-ui.yml` iş akışları iki kopyanın eşitliğini denetler ve ayrışırsa CI kırılır.

`scripts/build_site.py` bu klasörü **bilmez**. Wiki'yi üretirken `docs/` içindeki başka hiçbir şeyi silmediği için kopya hayatta kalıyor — bu artık bir gereklilik, ayrıntısı `CLAUDE.md`'nin veri sözleşmesinde.

## Bilerek yapılmayanlar

- **Model çağrısı yok.** Fırsat metni de, benzerlik sıralaması da sabit kurallarla üretiliyor. Maliyet şartı bu.
- **Kod indirilmiyor.** Sınır aşaması yalnız depo üstverisine ve istenirse README'ye bakar; dosya ağacı taranmaz. Lisans kuralı bunu gerektiriyor.
- **Sayfa yenilenince kaldığın vakaya dönmüyor.** Adres çubuğuna `#/case/A002` yazılıyor ama okunmuyor; yenileme baştan başlatır.
