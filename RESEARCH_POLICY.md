# Araştırma ve kanıt standardı

Bu koleksiyonun amacı mümkün olduğunca çok repo biriktirmek değil; **ticari kullanım iddiası ile kaynak kod arasındaki bağı izlenebilir tutmaktır.**

## Kanıt dereceleri

### A — Doğrulanmış ticari vaka + exact repo
Aşağıdakilerin tamamı gerekir:
1. Belirli bir müşteri, gelir, ticari sonuç veya ücretli kullanım açıkça anlatılmış olmalı.
2. Aynı vaka ile doğrudan ilişkilendirilen GitHub/Gist/workflow kaynağı bulunmalı.
3. Repo sahibinin veya vaka yazarının bağlantısı makul biçimde kurulabilmeli.
4. Gelir rakamı varsa neyi ifade ettiği ayrıştırılmalı: freelancer ücreti, kampanya bütçesi, müşteriye sağlanan değer veya tasarruf aynı şey değildir.

### B — Ticari üretici + exact repo, fakat workflow bazında gelir kanıtı eksik
Kod açık ve ticari bağlam güçlüdür; fakat bu belirli workflow için ücretli müşteri veya gelir doğrudan gösterilmemiştir.

### C — Güçlü ücretli müşteri vakası, fakat kaynak repo yok
İş modeli gerçektir ve araştırmaya değerdir. Orijinal kod bulunana kadar upstream koleksiyonuna girmez.

### X — Tartışmalı / promosyon riski
Gelir veya müşteri iddiası vardır ancak gizli reklam, affiliate çıkar çatışması, kopya içerik veya başka ciddi şüphe bulunur. Varsayılan clone listesine alınmaz.

## Lisans kuralı
Public GitHub reposu, yeniden dağıtım veya yeniden lisanslama iznini otomatik olarak vermez. Root seviyede açık lisans bulunmayan projelerin kodunu bu repoya kopyalamıyoruz. Bunun yerine:
- upstream URL,
- doğrulanmış commit SHA,
- kaynak vaka URL'si
saklanır ve clone scripti orijinal repoyu doğrudan çeker.

## Türkiye'de satılabilirlik alanı
`tr_sellability` kaba bir araştırma önceliğidir:
- `high`: Türkiye'de çok sayıda benzer işletmeye doğrudan satılabilir.
- `medium`: müşteri var ama entegrasyon/pazar koşulları daha niş.
- `low`: yerel talep veya platform erişimi sınırlı.

Bu alan gelir garantisi değildir.

## Araştırma ilkesi
Tek bir Reddit gelir ekran görüntüsü yeterli kanıt değildir. Tercih sırası:
1. belirli müşteri problemi,
2. çalışan sistem açıklaması,
3. ticari sonuç,
4. exact kaynak kod,
5. repo geçmişi ve lisans,
6. mümkünse ikinci bağımsız sinyal.
