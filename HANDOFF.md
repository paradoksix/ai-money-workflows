# HANDOFF

**Nerede kaldık** dosyası. Turdan tura değişmeyen kurallar için [`CLAUDE.md`](CLAUDE.md)'ye bak — bu dosya her turda güncellenir.

Son güncelleme: **2026-08-30**, Wiki turu `main`'e birleşip canlıda doğrulandıktan sonra.

## Şu anki durum

| | |
|---|---|
| Dal | **`main`** — Wiki dalı birleşti (merge commit `10dfc80`), çalışma ağacı temiz |
| Vaka sayısı | **124 kayıt** — A 6 · B 25 · C 92 · X 1 · **arşivde 122** (X001 ve A006'ya devredilen C027 hariç) — *bu turda değişmedi* |
| İş kolu | 16 gerçek niş + `tartismali` |
| `validate_catalog.py` | 42 kayıt — **geçiyor** |
| `validate_cases.py` | 124 kayıt + 3 çapraz kontrol — **geçiyor** |
| `docs/` | **22 sayfalık Wiki**, veriyle taze |
| GitHub Pages | **Wiki canlıda — doğrulandı.** `verify-live-site` iş akışı 2026-08-28'de kök adreste Wiki'yi buldu ([run #1](https://github.com/paradoksix/ai-money-workflows/actions/runs/33220250547)). Bu, oturum boyunca *kanıta* dayanan ilk "canlı" ifadesi — öncekiler derleme durumundan varsayılmıştı |
| Issue | **açık issue yok** |
| PR | **[#5](https://github.com/paradoksix/ai-money-workflows/pull/5) merge edildi** (7 commit, 57 dosya) — **açık PR yok**. Politika aynen geçerli: PR'ı kullanıcı açar, agent kendi başına açmaz — yalnız hatırlatır (`CLAUDE.md` → PR ve dal politikası) |

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

`README.md`'nin "Proje durumu" bölümü buna göre **düzeltildi** — eskiden "hedef, aynı ölçütleri gevşetmeden 150–200 bandına kontrollü biçimde ilerlemek" diyordu, artık ucu açıklığı anlatıyor. Doğrulayıcının kontrol ettiği "122" rakamına dokunulmadı.

Ucu açıklık, ölçütlerin gevşediği anlamına **gelmiyor** — A/B/C/X eşikleri ve lisans kuralı aynen duruyor. Değişen tek şey, arşivin bir bitiş sayısına doğru yürümemesi.

## Açık boşluklar: neyin araştırılacağı

Arşivin ucu açık olması, **eldeki 124 kaydın da eksiksiz olduğu anlamına gelmiyor.** Yeni vaka aramak kadar mevcutların boşluklarını kapatmak da iş. Bu tur bilerek yeni vaka eklemedi; aşağıdaki tablo bir önceki turda ölçüldü ve **hâlâ geçerli**:

| Boşluk | Sayı | Anlamı |
|---|---|---|
| `status = encyclopedia_only` | **82 / 124** | Hiç araştırma kuyruğundan geçmemiş |
| `research_queue.csv`'de olmayan C vakası | **50 / 92** | Kuyruk 42 satır (C076–C084 bu turda eklendi) |
| `source_url` boş | **74 / 124** | 23 B + 51 C. En ağır nişler: video-görsel **18**, müşteri iletişimi **11**, içerik-sosyal medya **10**, B2B lead **7** |
| `revenue_type` boş | **33 / 124** | 2 A + 24 B + 7 C |
| `reported_amount` boş | **39 / 124** | |

**Asıl takip yeri `research_queue.csv`'nin `next_action` sütunudur** — issue checklist'i değil.

**Bu turda denenen ve başarısız olan:** C076–C084'ün ortak kaynak başlığı arandı. Dokuzu da tek bir Reddit başlığından geliyor ama adresi hiç kaydedilmemiş. Üç ayrı açıdan arandı (CRM ara katmanı `$3.500/ay` · D365 IOM `~$240K/yıl` · tıbbi cihaz son kullanma `$36K/çeyrek`) — hiçbiri bulmadı. **`reddit.com` bu ortamda yalnız doğrudan erişime değil, web aramasına da kapalı** (arama motoru `400` döndürüyor). Dokuzu da dürüst kayıtla kuyruğa alındı; aynı aramaları tekrarlama.

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

## Yapıldı: dil kuralı kendi kural kitaplarına da uygulandı

`CLAUDE.md`'deki **dil kuralı** melez terimleri yasaklıyor ("exact kaynak", "ground truth", "verified repo" örnek olarak veriliyor) ama kuralı koyan iki dosyanın kendisi o terimleri kullanıyordu. İkisi de temizlendi.

- **`CLAUDE.md`** — 23 değişiklik. Ayrıca `CI`, `PR` ve `commit SHA` ilk geçtikleri yerde açıklandı. Okurken gerçek bir hata da çıktı: veri sözleşmesi `check_readme`'nin **15** rakam kontrol ettiğini söylüyordu, doğrusu **12** (doğrulayıcının kendi çıktısı bunu yazıyor). Düzeltildi.
- **`RESEARCH_POLICY.md`** — baştan sona yeniden yazıldı. Dört derecenin başlığı artık Wiki ve `CLAUDE.md` ile **birebir aynı** (`A — Müşteri kanıtı + kodu açık` vb.); önceden `A — Doğrulanmış ticari vaka + exact repo` diyordu. Eşikler, lisans kuralı ve `tr_sellability` tanımları **anlamca değişmedi**; yalnız kelimeler sadeleşti.

Kullanılan karşılıklar artık kalıcı kural olarak `CLAUDE.md`'nin **Dil kuralı** bölümünde bir tabloda duruyor — yeni metin yazarken oraya bakılır.

`docs/arastirma-politikasi.html` aynı commit'te yeniden üretildi. Doğrulayıcılar bu iki dosyayı okumadığı için CI etkilenmedi.

**Kuyruk da kapandı.** `encyclopedia/*.md` (26 yer), `TURKIYE_OPPORTUNITIES.md`, `BUILD_SHORTLIST.md` ve `README.md` temizlendi; 123 vaka bloğu sayımı korundu. İki vakanın başlığı da değişti — C035 ve C037 "workflow" taşıyordu — ve `data/cases.csv` ile senkronlandı, yoksa Wiki'nin iki sayfası aynı vakayı farklı isimle gösterirdi. (İkisi de `catalog.csv`'de olmadığı için orada karşılığı yok.)

**Bilerek yapılmayan:** İngilizce vaka adlarının tamamı Türkçeleştirilmedi (ör. "Faceless Editing / Content Service", "50K Product Catalog Overhaul"). Bunlar melez jargon değil, vakanın kaynağındaki adı; çevirmek kaynağa geri izlenebilirliği zorlaştırır. Ayrı bir editoryal karar gerektirir.

`research/GOLDEN-CASES-DEEP-DIVE-*.md` hâlâ yoğun jargon içeriyor ama bunlar **iç araştırma notu**, yayınlanan metin değil — kapsam dışı.

## Bu turun bulgusu: site Wiki'yi hiç yayınlamamış

Kullanıcı canlı siteyi açtı ve **README göründü** — Wiki'ye çevrilmiş hâli sayfada yalnızca gömülü bir ekran görüntüsü olarak duruyordu.

Sebep: **Pages kaynağı `main` + kök dizin.** Kök seçildiğinde Jekyll `README.md`'yi site sanıp temayla yayınlıyor; `docs/` altındaki 22 sayfa köke gelmiyor. `docs/.nojekyll` var ama kaynak kök olduğu için Jekyll'i durdurmuyor. Ek belirti: README'nin `<div align="center">` ile başlayan başlık/rozet bloğu **ham markdown** olarak çıkıyordu — kramdown HTML bloğu içindeki markdown'ı işlemez, GitHub'ın kendi render'ı işler.

**Asıl ders teknik değil.** Bu depo birkaç turdur sitenin canlı olduğunu *varsaydı*. Kaynak: "pages build and deployment" iş akışının yeşil bitmesi, "Wiki yayında" diye okundu. Oysa yeşil derleme bir derlemenin **bittiğini** söyler, **neyin yayınlandığını** söylemez. `*.github.io` bu ortama kapalı olduğu için hiçbir oturum farkı göremedi ve yanlış birikti — eski "atlas canlı" commit'i de aynı hatayı yapmıştı.

Kalıcı önlem iki parçalı:

- **`verify-live-site.yml`** eklendi. Actions runner'ları siteye erişebiliyor; iş akışı kök adresi çekip Wiki'nin sol menü işaretini (`class="nav" id="nav"` — README'de yok) arıyor. `page_build` sonrası ve elle çalışıyor, ayrı iş akışı olduğu için PR'ları bloklamıyor.
- **`CLAUDE.md`** artık şunu kural olarak taşıyor: Pages kaynağı `main` + `/docs` olmak zorunda, ve **derleme durumuna bakıp "canlı" varsayılmaz** — iddia ya bu iş akışının yeşiline ya da kullanıcının teyidine dayanır.

**Çözüldü.** Kullanıcı Pages kaynağını `/docs`'a çevirdi ve `verify-live-site` ilk çalışmasında kök adreste Wiki'yi buldu. Hiçbir bağlantının düzeltilmesi gerekmedi — README, ENCYCLOPEDIA, 16 niş dosyası ve rozetler zaten bu kökü gösteriyordu.

Kontrol sonradan güçlendirildi: yalnız giriş sayfasına bakmak yetmez, çünkü kök yanlış yapılandırılmışken bile giriş sayfası cevap verebilir ama içindeki bağlantılar 404 döner. İş akışı artık `tum-vakalar.html`, `wiki.css` ve `vakalar.js`'i de çekerek sitenin gerçekten **gezilebilir** olduğunu doğruluyor.

## Kullanıcıya kalan manuel işler

Kullanıcı bayat dalları temizledi. **İkisi silindi:** `claude/golden-cases-deep-dive-2-c1m4ov` ve `claude/continue-from-where-left-y8utux`.

Geriye **tek dal** kaldı: `claude/handoff-wiki-conversion-xemu2b` (`fe3535f`). Kullanıcı bunu da kendisi silecek. Sonraki oturum içinde bir şey kalıp kalmadığını araştırmasın diye: **tamamen merge edilmiş** — `main`'de olmayan commit'i yok, PR #5 ile girdi, silinse hiçbir şey kaybolmaz.

Dal silme buradan yapılamıyor: GitHub MCP'sinde dal silme aracı **yok** (arandı). `git push origin --delete` git protokolü üzerinden gittiği için çalışabilir ama denenmedi — kullanıcı silmeyi kendisi yapmayı tercih ediyor. **Acil bir iş değil**, oturum sonlarında hatırlatılması yeterli.

Wiki `main`'e girdi ve **canlı sitede yayında** — kaynak `/docs`'a çevrildikten sonra `verify-live-site` bunu doğruladı.

## Yeni oturum için ilk adımlar

1. `CLAUDE.md`'yi oku (kurallar, veri sözleşmesi, ortam kısıtları).
2. Yeşil zemini teyit et:
   ```bash
   python3 scripts/validate_catalog.py
   python3 scripts/validate_cases.py
   python3 scripts/build_site.py && git diff --exit-code docs
   grep -hc '^## [ABCX][0-9]' encyclopedia/nis-*.md | paste -sd+ | bc   # 123 olmalı
   ```
3. **Açık karar ve bekleyen düzeltme yok.** Dil kuralı temizliği ve README çelişkisi kapandı; sıradaki iş **araştırmanın kendisi** — yukarıdaki "Açık boşluklar" tablosu ve 11 altın vaka. Yeni metin yazarken `CLAUDE.md`'nin Dil kuralı bölümündeki karşılık tablosuna bak.
4. Araştırma turunu kapatan commit bu dosyayı da güncellesin.
