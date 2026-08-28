# Araştırma ve kanıt standardı

Bu arşivin amacı mümkün olduğunca çok depo biriktirmek değil; **bir işin para kazandırdığı iddiası ile o işin kaynak kodu arasındaki bağı izlenebilir tutmaktır.**

## Kanıt dereceleri

### A — Müşteri kanıtı + kodu açık
Aşağıdakilerin tamamı gerekir:

1. Belirli bir müşteri, gelir, ticari sonuç veya ücretli kullanım açıkça anlatılmış olmalı.
2. Aynı vakayla doğrudan ilişkilendirilebilen, açıkta duran bir kaynak kod bulunmalı — bir GitHub deposu ya da Gist (GitHub'ın küçük kod parçalarını paylaşmaya yarayan sayfası).
3. Kodu paylaşan kişi ile vakayı anlatan kişi arasındaki bağ makul biçimde kurulabilmeli.
4. Gelir rakamı varsa neyi ifade ettiği ayrıştırılmalı: **işi yapana ödenen ücret, kampanya bütçesi, müşteriye sağlanan değer ve müşterinin kazandığı tasarruf aynı şey değildir.**

### B — Kodu açık, kazancı belirsiz
Kod açıkta duruyor ve ticari bağlam güçlü; fakat **tam olarak bu iş akışının** para kazandırdığı, yani ödeme yapan bir müşteri ya da gelir, doğrudan gösterilmemiş.

### C — Para kazandırmış, kodu yok
İş modeli gerçek ve araştırmaya değer. Kodu ortaya çıkana kadar, indirilecek kaynak kod listesine girmez.

### X — Şüpheli
Gelir veya müşteri iddiası var; ama gizli reklam, komisyonlu tanıtımdan doğan çıkar çatışması, kopya içerik ya da başka ciddi bir şüphe de var. Varsayılan indirme listesine alınmaz.

## Lisans kuralı
Herkese açık bir GitHub deposu, o kodu yeniden dağıtma veya yeniden lisanslama iznini kendiliğinden **vermez**. Kök dizininde açık lisans bulunmayan projelerin kodunu bu depoya kopyalamıyoruz. Bunun yerine

- özgün deponun adresi,
- doğrulanmış sürüm kimliği (commit SHA — bir kodun tam olarak hangi hâline bakıldığını sabitleyen numara),
- vakanın anlatıldığı sayfanın adresi

saklanır; indirme scripti özgün depoyu doğrudan o sürümden çeker.

## Türkiye'de satılabilirlik alanı
`tr_sellability` kesin bir ölçüm değil, kaba bir araştırma önceliğidir:

- `high`: Türkiye'de çok sayıda benzer işletmeye doğrudan satılabilir.
- `medium`: müşterisi var, ama kurulum koşulları ya da pazarı daha dar.
- `low`: yerel talep veya platform erişimi sınırlı.

Bu alan bir gelir garantisi değildir.

## Araştırma ilkesi
Tek bir Reddit gelir ekran görüntüsü yeterli kanıt değildir. Aranan sıra:

1. belirli bir müşteri problemi,
2. çalışan sistemin anlatımı,
3. elde edilen ticari sonuç,
4. işin tam olarak hangi kodla yapıldığı,
5. o kodun geçmişi ve lisansı,
6. mümkünse ikinci bir bağımsız işaret.
