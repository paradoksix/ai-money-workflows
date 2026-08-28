# CLAUDE.md

Bu depoda çalışan her Claude Code oturumu için **değişmeyen kurallar**. "Nerede kaldık, sırada ne var" sorusunun cevabı burada değil — önce [`HANDOFF.md`](HANDOFF.md) oku. Bu dosya nadiren değişir; `HANDOFF.md` her turda değişir.

## Bu depo nedir

Yapay zekâ ve otomasyonla **gerçekten para kazanıldığı bildirilen** işlerin, her birinin ne kadar kanıtlı olduğu işaretlenmiş arşivi. Amaç mümkün olduğunca çok "AI projesi" biriktirmek değil; şu zinciri izlenebilir tutmak:

> ticari vaka → kaynak → tam olarak hangi kod → pinlenmiş commit → lisans durumu → Türkiye'de satılabilirlik

Tek bir ürün geliştirmeye odaklanan build dalgası (`BUILD_SHORTLIST.md`) **duraklatılmış** durumda. Şu anki aşama saf araştırma ve kataloglama.

## Kanıt dereceleri

Tam kural [`RESEARCH_POLICY.md`](RESEARCH_POLICY.md)'de. Özet:

- **A — Müşteri kanıtı + kodu açık.** İşin gerçek bir müşteriye satıldığı *ve* tam olarak hangi kodla yapıldığı, ikisi birden doğrulandı.
- **B — Kodu açık, kazancı belirsiz.** Kod gerçek ve çalışıyor; ama tam olarak bu işin para kazandırdığı ayrıca gösterilmedi.
- **C — Para kazandırmış, kodu yok.** Ödeme yapan müşteri anlatımı güçlü; kod paylaşılmamış veya bulunamadı. Repo çıkana kadar upstream clone listesine girmez.
- **X — Şüpheli.** Gizli reklam, affiliate çıkar çatışması veya kopya içerik şüphesi. Ana sayıma katılmaz, varsayılan clone listesine alınmaz.

**Gelir etiketleri asla birbirine karıştırılmaz:**

| | |
|---|---|
| **F** | işi yapana ödenen ücret |
| **R** | satılan üründen veya abonelikten gelen gelir |
| **S** | müşterinin kazandığı tasarruf |
| **V** | kampanya değeri, alınan randevu, tahsil edilen alacak gibi başka ticari sonuçlar |

Bu rakamların neredeyse tamamı **işi yapanın kendi beyanıdır**; bağımsız denetlenmiş gerçek gibi sunulmaz. Metinde de öyle yazılır ("bildiriyor", "iddia ediyor" — "kazandı" değil).

## Lisans kuralı

Public bir GitHub reposu, yeniden dağıtım veya yeniden lisanslama izni **vermez**. Root seviyede açık lisansı olmayan hiçbir projenin kodu bu depoya kopyalanmaz. Saklanan tek şey:

- upstream URL,
- doğrulanmış 40 karakterlik commit SHA,
- kaynak vaka URL'i.

Clone scriptleri (`clone_originals.sh/.ps1`, `clone_disputed.sh/.ps1`) orijinal repoyu doğrudan o commit'ten çeker.

Deponun **kendi** araştırma metni, veri dosyaları ve scriptleri [CC BY 4.0](LICENSE) altındadır. Atıf verilen upstream kod bu lisansın dışındadır.

## Dil kuralı

Okur sıradan bir insan; jargon bilen bir mühendis değil.

- "exact kaynak", "ground truth", "verified repo" gibi **melez terimler kullanılmaz.** Herhangi birinin ne kastedildiğini anladığı kelime tercih edilir.
- Bir terim gerçekten şartsa **ilk geçtiği yerde açıklanır**, sonra serbestçe kullanılır.
- Kural yalnız gövde metnini değil **başlıkları, arayüz etiketlerini, filtre adlarını ve kart özetlerini** de kapsar.
- Kanıt derecesi hiçbir yerde yalnız renkle anlatılmaz — **harf her zaman görünür** (A/B/C/X), renk yalnız destektir.

## Veri sözleşmesi

- **`data/cases.csv` tek doğruluk kaynağıdır.** 124 kaydın tamamı burada. Bir vakayla ilgili herhangi bir sayı değişecekse önce burası değişir.
- **`docs/index.html` üretilir — elle düzenlenmez.** `scripts/build_site.py` onu `data/cases.csv`'den yeniden yazar.
- **`catalog.csv`**, A/B/X çekirdeğinin pinlenmiş alt kümesidir (42 satır) ve `validate_cases.py`'deki `SHARED_WITH_CATALOG` alanlarında `cases.csv` ile **birebir uyuşmak zorundadır**.
- **README'deki rakamlar veriden yeniden hesaplanır.** `validate_cases.py`'nin `check_readme` kontrolü 15 rakamı veriden üretip README ile karşılaştırır; tutmayanı adıyla söyleyip başarısız olur. README'de sayı değiştirirken veriyi de değiştir, yoksa CI kırılır.
- **`build_site.py` deterministiktir** — aynı veriden bayt-aynı çıktı üretir. CI tazeliği `git diff --exit-code` ile ölçtüğü için bu özellik korunmalı: sözlük sırasına güvenme, zaman damgası veya rastgelelik ekleme.
- Scriptler **saf stdlib** Python'dır (`csv`, `html`, `json`, `argparse`, `pathlib`, `re`). Dış bağımlılık eklenmez.
- CSV'ler **RFC4180**'e uyar: içinde virgül geçen her serbest metin alanı tırnaklanır. (`$1,800` gibi tutarlar tırnaksız yazılırsa kolonlar kayar — bu hata bir kez yaşandı.)

## Değişiklikten sonra çalıştırılacak üçlü

CI de birebir aynısını çalıştırır (`.github/workflows/validate-catalog.yml`):

```bash
python3 scripts/validate_catalog.py                                    # 42 kayıt, pinlenmiş çekirdek
python3 scripts/validate_cases.py                                      # 124 kayıt + 3 çapraz kontrol
python3 scripts/build_site.py && git diff --exit-code docs/index.html  # sayfa taze mi
```

Ansiklopedi metnine dokunan her değişiklikten sonra ayrıca vaka bloğu sayısı korunmalı:

```bash
grep -hc '^## [ABCX][0-9]' encyclopedia/nis-*.md | paste -sd+ | bc     # 123 olmalı
```

## Depo haritası

| Yol | Ne |
|---|---|
| `data/cases.csv` | **Tek doğruluk kaynağı** — 124 vaka, 19 kolon |
| `catalog.csv` | A/B/X çekirdeğinin pinlenmiş alt kümesi (42 satır) |
| `research_queue.csv` | Kaynağı hâlâ aranan vakalar + `next_action` sütunu |
| `sources.csv` | Kaynak platform kayıtları |
| `encyclopedia/nis-01..16-*.md` | 16 iş koluna göre vaka metinleri (123 blok) |
| `encyclopedia/DESENLER.md` | Örnek gruplarından çıkan ortak dersler |
| `encyclopedia/A006-JACOBO-DEVICE-REPAIR.md` | Arşivin en sağlam tek vakası, kendi kartıyla |
| `encyclopedia/APPENDIX-X-DISPUTED.md` | Şüpheli iddialar |
| `ENCYCLOPEDIA.md` | Ansiklopedi girişi ve iş kolu indeksi |
| `docs/index.html` | **Üretilen** atlas sayfası · `docs/.nojekyll` · `docs/atlas-onizleme.png` |
| `scripts/build_site.py` | Atlas üreticisi (`--fragment PATH` ile başlıksız kopya da yazar) |
| `scripts/validate_cases.py` | Şema + 3 çapraz kontrol (katalog ↔ ansiklopedi ↔ README) |
| `scripts/validate_catalog.py` | `catalog.csv` şeması, A/B/X için repo + 40 karakterlik SHA zorunlu |
| `research/GOLDEN-CASES-DEEP-DIVE-*.md` | Tarihli derin araştırma turları |
| `RESEARCH_POLICY.md` | Kanıt ve lisans kural kitabı |
| `TURKIYE_OPPORTUNITIES.md` · `BUILD_SHORTLIST.md` | Türkiye uyarlaması ve duraklatılmış build listesi |
| `builds/catalog-doctor/` | Tek çalışan demo (duraklatılmış build dalgasından kalan) |

Canlı site: **https://paradoksix.github.io/ai-money-workflows/** (GitHub Pages, `/docs` kaynağı, `main` dalı).

Depoda `.md` linkleri **canlı adrese** gider, `docs/index.html`'e değil — GitHub `.html` dosyalarını render etmez, ham kaynak olarak gösterir.

## Ortam kısıtları

Bu sandbox'ta doğrulanmış, kalıcı kısıtlar. **Her oturumda yeniden test etme** — kullanıcı düzeldiğini söylemedikçe doğru kabul et:

- **Engelli alan adları:** `reddit.com`, `old.reddit.com`, `linktr.ee`, çoğu şirket sitesi ve **tüm `*.github.io` adresleri** — kendi canlı sitemiz dâhil. Yani sayfayı buradan açıp göremezsin; doğrulamayı yerelde `docs/index.html` üzerinden (Chromium `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`) veya GitHub API ile yap.
- **GitHub API yazma yolları proxy tarafından kapalı:** `"Write access to this GitHub API path is not permitted through this proxy."` Yani **dal silme, repo ayarı, Pages ayarı buradan yapılamaz** — bunlar kullanıcıya bırakılır. Okuma, issue/PR yorumu ve `git push` çalışır.
- Reddit metni gerektiren araştırmalarda tek yol `WebSearch`'ün dolaylı özetleridir; thread'in tam metnine ulaşılamaz. Kaynak bulunamadıysa **uydurma — "bulunamadı" diye kaydet.**

## Senkron kuralı

- **Kural değişti mi** → `CLAUDE.md`.
- **Durum değişti mi** → `HANDOFF.md`.

Bir araştırma turunu kapatan commit, `HANDOFF.md`'yi de aynı commit içinde günceller: yeni rapor dosyası işaretçisi, derece değişiklikleri, tazelenmiş açık iş kuyruğu.
