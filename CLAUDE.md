# CLAUDE.md

Bu depoda çalışan her Claude Code oturumu için **değişmeyen kurallar**. "Nerede kaldık, sırada ne var" sorusunun cevabı burada değil — önce [`HANDOFF.md`](HANDOFF.md) oku. Bu dosya nadiren değişir; `HANDOFF.md` her turda değişir.

## Bu depo nedir

Yapay zekâ ve otomasyonla **gerçekten para kazanıldığı bildirilen** işlerin, her birinin ne kadar kanıtlı olduğu işaretlenmiş arşivi. Amaç mümkün olduğunca çok "AI projesi" biriktirmek değil; şu zinciri izlenebilir tutmak:

> ticari vaka → kaynak → tam olarak hangi kod → sabitlenmiş sürüm → lisans durumu → Türkiye'de satılabilirlik

Tek bir ürün geliştirmeye odaklanan yapım dalgası (`BUILD_SHORTLIST.md`) **duraklatılmış** durumda. Şu anki aşama saf araştırma ve kataloglama.

## Kanıt dereceleri

Tam kural [`RESEARCH_POLICY.md`](RESEARCH_POLICY.md)'de. Özet:

- **A — Müşteri kanıtı + kodu açık.** İşin gerçek bir müşteriye satıldığı *ve* tam olarak hangi kodla yapıldığı, ikisi birden doğrulandı.
- **B — Kodu açık, kazancı belirsiz.** Kod gerçek ve çalışıyor; ama tam olarak bu işin para kazandırdığı ayrıca gösterilmedi.
- **C — Para kazandırmış, kodu yok.** Ödeme yapan müşteri anlatımı güçlü; kod paylaşılmamış veya bulunamadı. Kodu ortaya çıkana kadar, indirilecek kaynak kod listesine girmez.
- **X — Şüpheli.** Gizli reklam, komisyonlu tanıtımdan doğan çıkar çatışması veya kopya içerik şüphesi. Ana sayıma katılmaz, varsayılan indirme listesine de alınmaz.

**Gelir etiketleri asla birbirine karıştırılmaz:**

| | |
|---|---|
| **F** | işi yapana ödenen ücret |
| **R** | satılan üründen veya abonelikten gelen gelir |
| **S** | müşterinin kazandığı tasarruf |
| **V** | kampanya değeri, alınan randevu, tahsil edilen alacak gibi başka ticari sonuçlar |

Bu rakamların neredeyse tamamı **işi yapanın kendi beyanıdır**; bağımsız denetlenmiş gerçek gibi sunulmaz. Metinde de öyle yazılır ("bildiriyor", "iddia ediyor" — "kazandı" değil).

## Lisans kuralı

Herkese açık bir GitHub deposu, o kodu yeniden dağıtma veya yeniden lisanslama izni **vermez**. Kök dizininde açık lisansı olmayan hiçbir projenin kodu bu depoya kopyalanmaz. Saklanan tek şey:

- özgün deponun adresi,
- doğrulanmış 40 karakterlik sürüm kimliği (commit SHA — bir kodun tam olarak hangi hâline bakıldığını sabitleyen numara),
- vakanın anlatıldığı sayfanın adresi.

İndirme scriptleri (`clone_originals.sh/.ps1`, `clone_disputed.sh/.ps1`) özgün depoyu doğrudan o sürümden indirir.

Deponun **kendi** araştırma metni, veri dosyaları ve scriptleri [CC BY 4.0](LICENSE) altındadır. Atıf verilen, başkalarına ait kod bu lisansın dışındadır.

## Dil kuralı

Okur sıradan bir insan; jargon bilen bir mühendis değil.

- "exact kaynak", "ground truth", "verified repo" gibi **melez terimler kullanılmaz.** Herhangi birinin ne kastedildiğini anladığı kelime tercih edilir.
- Bir terim gerçekten şartsa **ilk geçtiği yerde açıklanır**, sonra serbestçe kullanılır.
- Kural yalnız gövde metnini değil **başlıkları, arayüz etiketlerini, filtre adlarını ve kart özetlerini** de kapsar.
- Kanıt derecesi hiçbir yerde yalnız renkle anlatılmaz — **harf her zaman görünür** (A/B/C/X), renk yalnız destektir.

Sık düşülen tuzaklar ve arşivin yerleşmiş karşılıkları — yeni metinde bunlar kullanılır:

| Kullanma | Bunu kullan |
|---|---|
| exact repo / exact kaynak | işin tam olarak hangi kodla yapıldığı · doğrulanmış kaynak kodu |
| workflow | iş akışı |
| upstream | özgün depo · kodun asıl sahibi |
| clone listesi | indirilecek kaynak kod listesi |
| affiliate | komisyonlu tanıtım |
| public repo | herkese açık depo |
| root lisans | deponun kök dizinindeki lisansı |
| pinlenmiş commit | sabitlenmiş sürüm |
| renderer | markdown çeviricisi |
| thread | tartışma başlığı |

**Dört derecenin adı üç yerde birebir aynıdır** ve öyle kalmalı: `RESEARCH_POLICY.md` başlıkları, `CLAUDE.md`'nin yukarıdaki özeti ve `build_site.py`'deki `GRADES` sabiti.

## Veri sözleşmesi

- **`data/cases.csv` tek doğruluk kaynağıdır.** 124 kaydın tamamı burada. Bir vakayla ilgili herhangi bir sayı değişecekse önce burası değişir.
- **`docs/` klasörünün tamamı üretilir — elle düzenlenmez.** `scripts/build_site.py` 22 Wiki sayfasını + `wiki.css`, `wiki.js`, `vakalar.js` dosyalarını `data/cases.csv` ve `encyclopedia/*.md`'den yeniden yazar. (Elle konmuş tek iki dosya: `.nojekyll` ve `wiki-onizleme.png`.)
- **`catalog.csv`**, A/B/X çekirdeğinin sürümü sabitlenmiş alt kümesidir (42 satır) ve `validate_cases.py`'deki `SHARED_WITH_CATALOG` alanlarında `cases.csv` ile **birebir uyuşmak zorundadır**.
- **README'deki rakamlar veriden yeniden hesaplanır.** `validate_cases.py`'nin `check_readme` kontrolü 12 rakamı veriden üretip README ile karşılaştırır; tutmayanı adıyla söyleyip başarısız olur. README'de sayı değiştirirken veriyi de değiştir, yoksa CI kırılır — CI, her push'ta GitHub'ın kendiliğinden çalıştırdığı denetim.
- **`build_site.py` deterministiktir** — aynı veriden bayt-aynı çıktı üretir. CI tazeliği `git diff --exit-code` ile ölçtüğü için bu özellik korunmalı: sözlük sırasına güvenme, zaman damgası veya rastgelelik ekleme.
- **Ansiklopedi markdown'ı dar bir alt kümedir.** `build_site.py` içindeki markdown çeviricisi başlık, kalın, satır içi kod, bağlantı, madde ve numaralı liste, yatay çizgi ve alıntıyı tanır. Tablo, kod bloğu veya görsel eklenirse **derleme sessizce atlamaz, hata verip durur**. Yeni bir yapı gerekiyorsa önce `md_blocks`'a desteğini ekle.
- Scriptler yalnız **Python'ın kendi kütüphaneleriyle** yazılır (`csv`, `html`, `json`, `argparse`, `pathlib`, `re`). Dışarıdan paket eklenmez.
- CSV'ler **RFC4180**'e uyar: içinde virgül geçen her serbest metin alanı tırnaklanır. (`$1,800` gibi tutarlar tırnaksız yazılırsa sütunlar kayar — bu hata bir kez yaşandı.)

## Değişiklikten sonra çalıştırılacak üçlü

CI de birebir aynısını çalıştırır (`.github/workflows/validate-catalog.yml`):

```bash
python3 scripts/validate_catalog.py                                    # 42 kayıt, sabitlenmiş çekirdek
python3 scripts/validate_cases.py                                      # 124 kayıt + 3 çapraz kontrol
python3 scripts/build_site.py && git diff --exit-code docs             # Wiki taze mi
```

Ansiklopedi metnine dokunan her değişiklikten sonra ayrıca vaka bloğu sayısı korunmalı:

```bash
grep -hc '^## [ABCX][0-9]' encyclopedia/nis-*.md | paste -sd+ | bc     # 123 olmalı
```

## Depo haritası

| Yol | Ne |
|---|---|
| `data/cases.csv` | **Tek doğruluk kaynağı** — 124 vaka, 19 kolon |
| `catalog.csv` | A/B/X çekirdeğinin sürümü sabitlenmiş alt kümesi (42 satır) |
| `research_queue.csv` | Kaynağı hâlâ aranan vakalar + `next_action` sütunu |
| `sources.csv` | Kaynak platform kayıtları |
| `encyclopedia/nis-01..16-*.md` | 16 iş koluna göre vaka metinleri (123 blok) |
| `encyclopedia/DESENLER.md` | Örnek gruplarından çıkan ortak dersler |
| `encyclopedia/A006-JACOBO-DEVICE-REPAIR.md` | Arşivin en sağlam tek vakası, kendi kartıyla |
| `encyclopedia/APPENDIX-X-DISPUTED.md` | Şüpheli iddialar |
| `ENCYCLOPEDIA.md` | Ansiklopedi girişi ve iş kolu indeksi |
| `docs/` | **Üretilen Wiki** — 22 sayfa: giriş, bütün örnekler, 16 iş kolu, şüpheli iddialar, ortak dersler, A006, ölçütler · `wiki.css` · `wiki.js` · `vakalar.js` · elle konan `.nojekyll` ve `wiki-onizleme.png` |
| `scripts/build_site.py` | Wiki üreticisi — sol menü, vaka çapaları, ansiklopedi çeviricisi (`--fragment PATH` ile giriş sayfasının başlıksız kopyasını da yazar) |
| `scripts/validate_cases.py` | Şema + 3 çapraz kontrol (katalog ↔ ansiklopedi ↔ README) |
| `scripts/validate_catalog.py` | `catalog.csv` şeması, A/B/X için depo adresi + 40 karakterlik sürüm kimliği zorunlu |
| `.github/workflows/verify-live-site.yml` | Canlı sitenin **Wiki'yi** sunduğunu doğrular (README'yi değil) — bu ortamdan yapılamayan tek kontrol |
| `research/GOLDEN-CASES-DEEP-DIVE-*.md` | Tarihli derin araştırma turları |
| `RESEARCH_POLICY.md` | Kanıt ve lisans kural kitabı |
| `TURKIYE_OPPORTUNITIES.md` · `BUILD_SHORTLIST.md` | Türkiye uyarlaması ve duraklatılmış yapım listesi |
| `builds/catalog-doctor/` | Tek çalışan örnek araç (duraklatılmış yapım dalgasından kalan) |

Canlı site: **https://paradoksix.github.io/ai-money-workflows/** (GitHub Pages, `/docs` kaynağı, `main` dalı).

Depoda `.md` linkleri **canlı adrese** gider, `docs/index.html`'e değil — GitHub `.html` dosyalarını sayfa olarak göstermez, ham kaynak kodunu gösterir.

## Ortam kısıtları

Bu çalışma ortamında doğrulanmış, kalıcı kısıtlar. **Her oturumda yeniden test etme** — kullanıcı düzeldiğini söylemedikçe doğru kabul et:

- **Engelli alan adları:** `reddit.com`, `old.reddit.com`, `linktr.ee`, çoğu şirket sitesi ve **tüm `*.github.io` adresleri** — kendi canlı sitemiz dâhil. Yani sayfayı buradan açıp göremezsin; doğrulamayı yerelde `docs/index.html` ve diğer Wiki sayfaları üzerinden (Chromium `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`) veya GitHub API ile yap.
- **GitHub API yazma yolları proxy tarafından kapalı:** `"Write access to this GitHub API path is not permitted through this proxy."` Yani **dal silme, depo ayarı, Pages ayarı buradan yapılamaz** — bunlar kullanıcıya bırakılır. Okuma, issue ve PR yorumu (PR = pull request, bir dalın `main`'e katılma önerisi) ve `git push` çalışır.
- Reddit metni gerektiren araştırmalarda tek yol `WebSearch`'ün dolaylı özetleridir; tartışma başlığının tam metnine ulaşılamaz. Kaynak bulunamadıysa **uydurma — "bulunamadı" diye kaydet.** (`reddit.com` yalnız doğrudan erişime değil, **web aramasına da kapalı** — arama motoru alan adını reddediyor.)
- **GitHub Pages kaynağı `main` + `/docs` olmak zorundadır.** Kök dizin seçilirse Jekyll `README.md`'yi site sanıp yayınlar; Wiki `/docs/` altına gömülür ve deponun bütün bağlantıları yanlış yere gider. Bu ayar buradan **değiştirilemez** (depo ayarı, GitHub MCP'sinde Pages aracı yok) — kullanıcıya bırakılır.
- **Sitenin yayında olduğu buradan doğrulanamaz.** `*.github.io` kapalı. "pages build and deployment" iş akışının yeşil bitmesi bir derlemenin *bittiğini* söyler, **neyin yayınlandığını söylemez** — bu ikisi bir kez karıştırıldı ve depo birkaç tur boyunca sitenin canlı olduğunu yanlış varsaydı. "Canlı" iddiası yalnız iki şeye dayanabilir: `verify-live-site` iş akışının yeşili ya da kullanıcının teyidi. **Derleme durumuna bakıp varsayma.**

## PR ve dal politikası

- **PR kendi başına açılmaz.** İş biten dala push edilir, orada bekler. Kullanıcı PR'ları biriktirip önemli bir aşamada topluca değerlendirmek istiyor.
- **Önemli bir gelişmeden sonra hatırlat** — "şu dal hazır, PR açmamı ister misin?" diye sor. Onay gelirse aç, gelmezse dalda bırak.
- **Silinecek bayat dal varsa oturum sonunda hatırlat.** Silmeyi kullanıcı, müsait olduğunda GitHub arayüzünden kendisi yapar (proxy zaten yazma yollarını kapatıyor). **Acil bir işmiş gibi sunma** — sadece listeyi hatırlat.

## Senkron kuralı

- **Kural değişti mi** → `CLAUDE.md`.
- **Durum değişti mi** → `HANDOFF.md`.

Bir araştırma turunu kapatan commit, `HANDOFF.md`'yi de aynı commit içinde günceller: yeni rapor dosyası işaretçisi, derece değişiklikleri, tazelenmiş açık iş kuyruğu.
