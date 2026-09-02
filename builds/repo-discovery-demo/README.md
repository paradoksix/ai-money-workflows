# Repo Discovery Engine — sıfır maliyetli demo

Bu klasör, `repo-discovery-engine-v2.md` mimarisinin **sunucusuz ve ücretli servis kullanmayan** çalışan demosudur. Amaç production altyapısını birebir taklit etmek değil; ürün deneyimini ve kritik algoritmaları gerçek GitHub verisiyle doğrulamaktır.

## Çalıştırma

```bash
cd builds/repo-discovery-demo
python -m http.server 8080
# http://localhost:8080
```

Node/Python zorunlu değildir; herhangi bir statik HTTP server yeterlidir. GitHub Pages veya ücretsiz statik hosting üzerinde de çalışır.

## Gerçekten çalışan parçalar

- Gerçek GitHub Repository Search API üzerinden aday keşfi.
- Exact `repository.id` ile kimliklendirme.
- IndexedDB metadata cache.
- Exact seen-set; Bloom filter yok.
- Seen state JSON export/import.
- Quality + relevance + freshness + novelty skoru.
- Son 10 repo üzerinden diversity penalty.
- Ağırlıklı, yer değiştirmesiz örnekleme.
- İstemci tarafında 20'lik kuyruk ve low-water refill.
- Kart odaktayken doğal Space/Enter aktivasyonu; global keyboard handler yok.
- Static canonical route: `#/r/{repository_id}/{slug}`.
- Repo ID üzerinden route restore (`GET /repositories/{id}`).
- README'nin yalnızca talep üzerine çekilmesi.
- Ücretli LLM olmadan deterministik “AI Money Workflow Opportunities” üretimi.
- DeepWiki çıkışı.
- GitHub rate-limit header'larının UI'da gösterilmesi.
- İsteğe bağlı token; sadece `sessionStorage` içinde tutulur.
- Havuz tükenince açıkça işaretli “seen fallback”.

## v2'den bilinçli sapmalar

Bu demo tamamen statiktir. Bu yüzden production v2'nin şu parçaları **taklit edilmez**:

1. Sunucu tarafı RoaringBitmap / tek doğruluk kaynağı: burada exact ID set IndexedDB'de tutulur. Safari storage eviction riski nedeniyle export/import eklendi. Production'da server-backed seen state kullanılmalı.
2. GH Archive ingest: tarayıcıdan saatlik gzip firehose işlemek demo için gereksiz ve kaba olur. Demo GitHub Search API ile sınırlı aday havuzu doldurur. Production keşif yakıtı yine GH Archive olmalıdır.
3. Supabase/Postgres queue + unique job index: ücretsiz statik demoda server job yok. Wiki deterministik olarak tarayıcıda üretilir.
4. Edge/origin ayrımı: static asset CDN + GitHub API çağrıları dışında origin yoktur.
5. Claude/API tabanlı opportunity generation: ücret şartını ihlal etmemek için yerini deterministic rules alır.

## Rate-limit

Demo token olmadan da çalışır. GitHub unauthenticated ve Search API limitleri daha düşüktür; UI kalan kotayı response header'lardan gösterir. Kendi token'ını girersen yalnızca sekme ömrü boyunca `sessionStorage`'da tutulur. Repo içine secret yazılmaz.

## Güvenlik

- Token hiçbir dosyaya, URL'ye veya localStorage'a yazılmaz.
- HTML'e basılan dış veri escape edilir.
- README ham HTML olarak render edilmez.
- `target=_blank` linklerinde `rel=noreferrer` kullanılır.
- README yalnızca özet/başlık/komut ipucu için analiz edilir; tüm içerik yeniden yayınlanmaz.

## Kabul kriteri

Demo başarılı sayılırsa:

1. İlk açılışta gerçek bir repo gösterir.
2. Kart odaktayken Space ile yeni repo gösterir.
3. Aynı oturum/IndexedDB içinde aynı repo, havuz tükenmedikçe tekrar gelmez.
4. Wiki düğmesi README'yi talep üzerine analiz eder.
5. Sayfa yenilenince `#/r/{id}` route'u aynı repo ID'sini geri yükler.
6. Token olmadan temel akış çalışır.
7. Rate-limit hatası kullanıcıya sessizce yutulmadan gösterilir.
