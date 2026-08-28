# HANDOFF

**Nerede kaldık** dosyası. Turdan tura değişmeyen kurallar için [`CLAUDE.md`](CLAUDE.md)'ye bak — bu dosya her turda güncellenir.

Son güncelleme: **2026-08-28**, "Wiki'ye geçiş turu"nun kapanışında.

## Şu anki durum

| | |
|---|---|
| Dal | `claude/handoff-wiki-conversion-xemu2b` — `main`'den (`1914dfc`) ayrıldı, Wiki commit'ini taşıyor |
| Vaka sayısı | **124 kayıt** — A 6 · B 25 · C 92 · X 1 · **arşivde 122** (X001 ve A006'ya devredilen C027 hariç) — *bu turda değişmedi* |
| İş kolu | 16 gerçek niş + `tartismali` |
| `validate_catalog.py` | 42 kayıt — **geçiyor** |
| `validate_cases.py` | 124 kayıt + 3 çapraz kontrol — **geçiyor** |
| `docs/` | **22 sayfalık Wiki**, veriyle taze |
| GitHub Pages | `main`'e merge edilince canlıya çıkar — https://paradoksix.github.io/ai-money-workflows/ |
| Issue | **açık issue yok** |
| PR | Bu dalın PR'ı **henüz açılmadı** — kullanıcı istemedi |

## Bu turda ne yapıldı: web arayüzü Wiki oldu

Kullanıcının tarifi buydu:

> web arayüzünü bir Wiki haline getireceğiz, sol menüde rahatça ve sadelik içinde dolaşılabilecek, tıklanan menü elemanları kendilerinin ilgili sayfasına yönlenecek, o sayfada da çok iyi dizayn edilmiş detaylı içerikleri bulunacak.

Öncesinde `docs/index.html` **tek sayfaydı**: arama + üç filtre + kart ızgarası. Şimdi:

- **22 sayfa.** Giriş · bütün örnekler · 16 iş kolu · şüpheli iddialar · ortak dersler · A006 · ölçütler.
- **Her sayfada aynı sol menü**, bulunulan sayfa işaretli (`aria-current`). Dar ekranda menü "Menü ▾" açılırına dönüşüyor.
- **Ansiklopedi metni artık sitede.** 123 vaka bloğunun tamamı kendi iş kolu sayfasında, tam anlatımıyla. Öncesinde site yalnız tek cümlelik özetleri gösteriyor, tam metin için GitHub'a gönderiyordu.
- **Her vakanın kalıcı adresi var:** `nis-05-icerik-sosyal-medya.html#C060`. "Bütün örnekler" sayfasındaki her başlık oraya gider.
- **Her vakaya künye eklendi** — `cases.csv`'deki 19 kolonun tamamı, açılır bir bölümde: paranın nereden geldiği, tutar, müşteri, araçlar, zorluk, kaynak, kod, sabitlenmiş sürüm, lisans ve **araştırmanın hangi aşamada olduğu**. Boş alanlar gizlenmiyor, "kaynağın tam adresi kaydedilmemiş" gibi açıkça yazılıyor.

### Derinlik kararı (açıktaki iki karardan biri kapandı)

Kullanıcıya soruldu, **"niş sayfası + derin bağlantı (~21 sayfa)"** seçildi. Gerekçesi ölçüldü: vaka bloklarının medyanı **71 kelime** (en kısa 41, en uzun 188, 31 blok 60 kelimenin altında). Her vakaya ayrı sayfa verilseydi 92 C sayfası ~70 kelime + tablodan ibaret kalacak, sol menü 145 maddeye çıkacaktı.

### Teknik notlar

- **Markdown renderer saf stdlib**, `build_site.py` içinde. Başlık, kalın, satır içi kod, bağlantı, madde/numaralı liste, yatay çizgi ve alıntı destekli. **Tanımadığı bir yapıyla karşılaşırsa sessizce atlamıyor, hata verip duruyor** — ansiklopediye tablo veya kod bloğu eklenirse CI bunu yakalar.
- **Ortak `wiki.css` / `wiki.js`** ayrı dosyada; CSS 22 sayfaya kopyalanmıyor.
- **Determinizm korundu** — aynı veriden bayt-aynı çıktı. İki kez üretilip `diff -r` ile doğrulandı.
- **CI genişletildi:** artık `docs/index.html` değil `docs/` klasörünün tamamı kontrol ediliyor; ayrıca üretilip commit edilmemiş bir sayfa kalırsa `git status --porcelain` ile yakalanıyor (`git diff` untracked dosyayı görmez).
- **Üç durumlu tema ve "harf her zaman görünür" kuralı korundu.** Açık/koyu/sistem üç durumda da A/B/C/X harfi renkten bağımsız okunuyor.

### Yerelde doğrulananlar

`*.github.io` engelli olduğu için her şey yerelde Chromium ile bakıldı:

- 500 / 820 / 1440 piksel genişlikte **yatay taşma yok** (`scrollWidth == viewport`, taşan öğe listesi boş).
- **922 iç bağlantının tamamı çözülüyor**, kırık yok. 124 vakanın tamamının tam olarak bir çapası var.
- Üretilen HTML'de **kalıntı markdown yok** (`**`, backtick, `](` taraması temiz).
- `docs/wiki-onizleme.png` yeni giriş sayfasından üretildi; eski `atlas-onizleme.png` silindi.

### Ansiklopedi metnine dokunulan tek yer

16 niş dosyasının **9. satırındaki** "hepsini birden filtrelemek için [atlas sayfası]" bağlantısı, artık doğru sayfayı göstermek için `tum-vakalar.html`'e çevrildi. `ENCYCLOPEDIA.md` de aynı şekilde güncellendi. **123 vaka bloğunun hiçbirine dokunulmadı** (sayım korunuyor).

Wiki, her niş sayfasında iki satırı **görüntülemiyor**: "Bu grupta N örnek var" (artık sayfa başlığında) ve "Harflerin ne anlama geldiği için…" (artık sol menüde, her sayfada). Kaynak markdown'da ikisi de duruyor; GitHub'dan okuyanlar için hâlâ gerekli.

## Sıradaki iş: araştırmayı tamamlama

Bu tur **bilerek yeni vaka eklemedi** — kullanıcı "araştırmayı sonraya bırakıyoruz" dedi. Aşağıdaki tablo bir önceki turda ölçüldü ve **hâlâ geçerli**:

| Boşluk | Sayı | Anlamı |
|---|---|---|
| `status = encyclopedia_only` | **82 / 124** | Hiç araştırma kuyruğundan geçmemiş |
| `research_queue.csv`'de olmayan C vakası | **59 / 92** | Kuyruk yalnız 33 satır |
| `source_url` boş | **74 / 124** | 23 B + 51 C. En ağır nişler: video-görsel **18**, müşteri iletişimi **11**, içerik-sosyal medya **10**, B2B lead **7** |
| `revenue_type` boş | **33 / 124** | 2 A + 24 B + 7 C |
| `reported_amount` boş | **39 / 124** | |

**Asıl takip yeri `research_queue.csv`'nin `next_action` sütunudur** — issue checklist'i değil.

**Kaynağı hâlâ aranan 11 altın vaka** (öncelik sırasıyla): C004 Powerprozesse · C003 50K katalog (`conor-is-my-name` adayı **reddedildi**, yeniden kullanma) · C002 Japon fatura işleyici · C006 AigencyTracker · C005 muhasebe otomasyonu · C001 gemi yöneticisi lead · C007 Shopify stok · C008 kitapçı WhatsApp · C018 `$5K` özel ders · C029 çevrimdışı üniversite RAG · C076 tıbbi cihaz son kullanma takibi.

Çoğu **engelli alan adlarına** (Reddit, Linktree) ihtiyaç duyuyor. İki tur denendi, hiçbiri A/B'ye yükselmedi. Daha verimli yön: yukarıdaki **82 `encyclopedia_only` vakası** — bunlar hiç denenmedi.

Wiki'nin künye bölümü artık bu boşlukları **sayfada görünür kılıyor**: kaynağı olmayan her vaka "kaynağın tam adresi kaydedilmemiş" yazıyor. Araştırma ilerledikçe bu satırlar kendiliğinden dolar.

## Açıkta kalan tek karar

**Araştırma nerede biter?** (Derinlik kararı bu turda kapandı, bu duruyor.) Adaylar:

- README'deki mevcut hedef: **150–200 vaka** bandına ölçütleri gevşetmeden çıkmak;
- ya da yeni vaka eklemeden **derinleşmek**: her C vakasını kuyruğa sokmak, her vakaya `source_url` kazandırmak, boş `revenue_type`/`reported_amount` alanlarını kapatmak.

İkisi çok farklı işler. Yukarıdaki tablo hangisinin ne kadar iş olduğunu gösteriyor. **Yeni oturum bunu kendi başına seçmemeli — sorup karar almalı.**

## Kullanıcıya kalan manuel işler

Agent proxy'si GitHub API'sinin yazma yollarını reddettiği için **dal silme buradan yapılamıyor**. GitHub arayüzünden `Branches` ekranından silinecek **iki bayat dal** var:

- `claude/golden-cases-deep-dive-2-c1m4ov` — **merge edilmemiş**, `main`'de olmayan 2 commit taşıyor ama içeriği tamamen bayat (eski `VOLUME-*` yapısı, `data/cases.csv` öncesi dünya). Kurtarılacak bir şeyi yok;
- `claude/continue-from-where-left-y8utux` — **tamamen merge edilmiş** (`main`'de olmayan commit'i yok), yalnız artık gereksiz.

Ayrıca: bu dalın **PR'ı açılmadı**. İstenirse açılabilir; Wiki `main`'e merge edilene kadar canlı sitede eski tek sayfa duruyor.

## Yeni oturum için ilk adımlar

1. `CLAUDE.md`'yi oku (kurallar, veri sözleşmesi, ortam kısıtları).
2. Yeşil zemini teyit et:
   ```bash
   python3 scripts/validate_catalog.py
   python3 scripts/validate_cases.py
   python3 scripts/build_site.py && git diff --exit-code docs
   grep -hc '^## [ABCX][0-9]' encyclopedia/nis-*.md | paste -sd+ | bc   # 123 olmalı
   ```
3. Yukarıdaki **açık kararı** kullanıcıya sor — araştırmanın bitiş çizgisi.
4. Araştırma turunu kapatan commit bu dosyayı da güncellesin.
