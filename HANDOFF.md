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
| PR | **Açılmadı, açılmayacak da** — kullanıcı kararı: PR'lar biriktirilip önemli bir aşamada değerlendirilecek. Kendi başına açma, hatırlat (`CLAUDE.md` → PR ve dal politikası) |

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

## Karar: araştırmanın ucu açık, hedef yok

Önceki turdan kalan "araştırma nerede biter?" sorusu **kapandı**. Kullanıcının kararı: **sabit bir bitiş çizgisi yok.** Arşiv sürekli büyümeye açık; 150–200 vaka gibi bir hedef bandı artık geçerli değil.

**Bu bir çelişki bıraktı — sonraki turun somut işi:** `README.md` satır 188 hâlâ şunu diyor:

> Arşiv **122 örnekte**; hedef, aynı ölçütleri gevşetmeden 150–200 bandına kontrollü biçimde ilerlemek.

Bu cümlenin ikinci yarısı artık yanlış. Düzeltilirken `validate_cases.py`'nin `check_readme` kontrolüne dikkat: **"122" rakamı veriden doğrulanıyor**, ona dokunma; yalnız hedef bandı ifadesi değişecek.

Ucu açıklık, ölçütlerin gevşediği anlamına **gelmiyor** — A/B/C/X eşikleri ve lisans kuralı aynen duruyor. Değişen tek şey, arşivin bir bitiş sayısına doğru yürümemesi.

## Açık boşluklar: neyin araştırılacağı

Arşivin ucu açık olması, **eldeki 124 kaydın da eksiksiz olduğu anlamına gelmiyor.** Yeni vaka aramak kadar mevcutların boşluklarını kapatmak da iş. Bu tur bilerek yeni vaka eklemedi; aşağıdaki tablo bir önceki turda ölçüldü ve **hâlâ geçerli**:

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

## Gelecek fikri: repo gönderim ve tarama hattı

Araştırmanın ucu açık olmasının **kullanıcının tarif ettiği yolu** bu. Henüz **tasarlanmadı** — burada yalnız fikir ve kısıtları kayıtlı. Uygulanmadan önce ayrı bir tasarım turu gerekiyor.

Akış:

1. **Wiki'de bir gönderim sayfası.** Ziyaretçi, para kazandırdığını düşündüğü bir reponun linkini bir alana yazıp gönderir.
2. **Modele gitmeden önce ücretsiz elemeler.** Token harcamadan yapılabilecek kontroller önce koşar: link gerçekten bir GitHub reposu mu · `data/cases.csv`'de `repo_url` olarak zaten var mı · kök dizinde açık lisans var mı · depo boş ya da arşivlenmiş mi. Gönderimlerin çoğu burada elenir ve **modele hiç ulaşmaz**.
3. **Elemeyi geçen için tek ve küçük bir model çağrısı.** Yalnız repo üstverisi gönderilir: ad, açıklama, konu etiketleri ve README'nin ilk birkaç bin karakteri. **Kod indirilmez, dosya ağacı taranmaz.** Ucuz/küçük bir model yeter (Haiku sınıfı). Tek soru: *bu, para kazandırdığı iddia edilen bir iş akışı mı; arşivin ölçütlerine aday olur mu?*
4. **Karar kullanıcıda.** Aday çıkarsa ayrı bir yönetim paneli sayfasında kullanıcıya bildirim düşer; ekle/ekleme kararını **yalnız kullanıcı** verir. Otomatik ekleme yok.
5. **Onaylananlar için derin araştırma.** Repo derinlemesine incelenir, vaka hakkında internette araştırma yapılır, mevcut kayıtlarla benzerlik ve çakışma kontrol edilir, sonra uygun nişe ve kanıt derecesine yerleştirilir.

**Token maliyeti bu tasarımın ana kısıtı** — kullanıcı bunu iki kez vurguladı. Kural: ücretsiz elemeler her zaman modelden önce koşar; model çağrısı gönderim başına bir tane ve küçük tutulur.

**Çözülmemiş mimari sorular** (tasarım turunun cevaplaması gerekenler):

- **GitHub Pages statiktir.** Form gönderimini alacak ve arka planda tarama koşturacak bir yer yok. Depo dışında bir şey gerekiyor: GitHub Actions, harici bir servis ya da başka bir çözüm. Bu, tasarımın en büyük açık ucu.
- **Yönetim paneli kimlik doğrulaması** nasıl yapılacak — panel herkese açık bir sayfa olamaz.
- **Onaylanan aday veriye nasıl bağlanacak?** Bir vaka üç yerde birden yaşıyor: `data/cases.csv`, `encyclopedia/nis-*.md` ve gerekiyorsa `research_queue.csv`. `validate_cases.py` üçü arasında çapraz kontrol yapıyor; hat bu üçünü tutarlı bırakmak zorunda.
- **`docs/` üretilen çıktıdır.** Gönderim hattı oraya doğrudan yazamaz — veri değişir, Wiki `build_site.py` ile yeniden üretilir.

## Sonraki iş: dil kuralını iki dosyaya uygula

`CLAUDE.md`'deki **dil kuralı** melez terimleri yasaklıyor ("exact kaynak", "ground truth", "verified repo" örnek olarak veriliyor) ama **kuralın kendi kural kitabı ve kendi anayasası hâlâ o terimleri kullanıyor.** Kullanıcı ikisinin de temizlenmesini onayladı; yalnız zamanlamayı sonraya bıraktı.

Aşağıdaki tarama **yapıldı** — sonraki turun yeniden taramasına gerek yok.

### `RESEARCH_POLICY.md` (45 satır) — ihlaller

| Satır | İfade |
|---|---|
| 7 (başlık) | `### A — Doğrulanmış ticari vaka + exact repo` |
| 10 | "GitHub/Gist/**workflow** kaynağı" |
| 14 (başlık) | `### B — Ticari üretici + exact repo, fakat workflow bazında gelir kanıtı eksik` |
| 15 | "bu belirli **workflow** için" |
| 18 | "**upstream** koleksiyonuna girmez" |
| 21 | "**affiliate** çıkar çatışması… **clone** listesine alınmaz" |
| 24 | "**Public** GitHub **reposu**… bu **repo**ya kopyalamıyoruz" |
| 25 | "**upstream** URL" |
| 43 | "**exact kaynak** kod" — kuralın birebir yasakladığı örnek ifadenin aynısı |
| 44 | "**repo** geçmişi ve lisans" |

### `CLAUDE.md` — aynı jargon

Satır 19 ("Repo çıkana kadar **upstream clone** listesine girmez") · satır 20 ("**affiliate** çıkar çatışması", "varsayılan **clone** listesi") · satır 35 ("**Public** bir GitHub **reposu**", "**Root** seviyede") · satır 37 ("**upstream** URL") · satır 41 ("**Clone** scriptleri") · satır 43 ("atıf verilen **upstream** kod").

### Kullanılabilecek karşılıklar

| Şimdi | Sade karşılığı |
|---|---|
| exact repo | işin tam olarak hangi kodla yapıldığı · doğrulanmış kaynak kodu |
| workflow | iş akışı |
| upstream | özgün depo · kodun asıl sahibi |
| clone listesi | indirilecek kaynak kod listesi |
| affiliate | komisyonlu tanıtım |
| public repo | herkese açık depo |
| root lisans | deponun kök dizinindeki lisans |

### Güvenlik ve kısıt notları (taranarak doğrulandı)

- **CI güvenli:** `validate_cases.py` ve `validate_catalog.py` `RESEARCH_POLICY.md`'yi **hiç okumuyor**. Düzyazı değişikliği doğrulamayı kırmaz.
- **Ama `docs/` tazelenmeli:** `build_site.py` bu dosyayı `docs/arastirma-politikasi.html`'e render ediyor. Değişiklikten sonra `python3 scripts/build_site.py` çalıştırılıp `docs/` aynı commit'e konmalı, yoksa tazelik kontrolü kırılır.
- **Markdown alt kümesinin dışına çıkma:** başlık, kalın, satır içi kod, bağlantı, madde/numaralı liste, yatay çizgi, alıntı serbest. **Tablo, kod bloğu veya görsel derlemeyi durdurur** (renderer bilerek hata veriyor).
- **Başlıklar serbestçe değiştirilebilir:** dosyaya bağlanan hiçbir yer bölüm çapası kullanmıyor — hepsi dosyanın kendisine bağlanıyor (`CLAUDE.md`, `README.md`×3, `ENCYCLOPEDIA.md`, 16 `encyclopedia/nis-*.md`, `build_site.py`).
- **Anlam değişmemeli, yalnız kelimeler.** A/B/C/X tanımları `validate_*.py` tarafından zorlanıyor ve `build_site.py`'nin `GRADES` sabitinde tekrar ediliyor. Kural aynı kalacak, sadece sadeleşecek.
- **Wiki'de iş yok:** `build_site.py`'deki `GRADES` ve `REVENUE` metinleri zaten sade Türkçe. Geride kalan yalnız bu iki markdown dosyası.
- **Düşük öncelikli yayılma:** aynı jargon (`workflow`, `upstream` ağırlıklı) `encyclopedia/*.md`, `TURKIYE_OPPORTUNITIES.md` ve `BUILD_SHORTLIST.md`'de de var. `research/GOLDEN-CASES-DEEP-DIVE-*.md` en yoğunu ama bunlar **iç araştırma notu**, yayınlanan metin değil — kapsam dışı bırakılabilir.

## Kullanıcıya kalan manuel işler

**Acil değil.** Kullanıcı bunları müsait olduğunda kendisi yapacak; oturum sonlarında hatırlatılması yeterli. Agent proxy'si GitHub API'sinin yazma yollarını reddettiği için dal silme buradan zaten yapılamıyor — GitHub arayüzünde `Branches` ekranından siliniyor.

Silinecek **iki bayat dal**:

- `claude/golden-cases-deep-dive-2-c1m4ov` — **merge edilmemiş**, `main`'de olmayan 2 commit taşıyor ama içeriği tamamen bayat (eski `VOLUME-*` yapısı, `data/cases.csv` öncesi dünya). Kurtarılacak bir şeyi yok;
- `claude/continue-from-where-left-y8utux` — **tamamen merge edilmiş** (`main`'de olmayan commit'i yok), yalnız artık gereksiz.

Wiki dalı (`claude/handoff-wiki-conversion-xemu2b`) `main`'e girene kadar canlı sitede **eski tek sayfa** duruyor. PR politikası gereği bu dalın PR'ı kendi başına açılmaz — önemli bir aşamada kullanıcıya sorulur.

## Yeni oturum için ilk adımlar

1. `CLAUDE.md`'yi oku (kurallar, veri sözleşmesi, ortam kısıtları).
2. Yeşil zemini teyit et:
   ```bash
   python3 scripts/validate_catalog.py
   python3 scripts/validate_cases.py
   python3 scripts/build_site.py && git diff --exit-code docs
   grep -hc '^## [ABCX][0-9]' encyclopedia/nis-*.md | paste -sd+ | bc   # 123 olmalı
   ```
3. **Açık karar kalmadı** — sorulacak bir şey yok, iş var. Sıradaki iki somut iş:
   - **Dil kuralı temizliği** — `RESEARCH_POLICY.md` ve `CLAUDE.md`. Tarama yapıldı, ihlal listesi ve karşılıklar yukarıda; yeniden taramaya gerek yok. Bitince `docs/` yeniden üretilmeli.
   - **`README.md` satır 188** — artık geçerli olmayan 150–200 hedef bandı ifadesi.
4. Araştırma turunu kapatan commit bu dosyayı da güncellesin.
