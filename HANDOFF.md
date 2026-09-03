# HANDOFF

**Nerede kaldık** dosyası. Turdan tura değişmeyen kurallar için [`CLAUDE.md`](CLAUDE.md)'ye bak — bu dosya her turda güncellenir.

Son güncelleme: **2026-09-03**. Bu tur **arşiv doğrulaması**ydı: sabitlenmiş sürümler ilk kez denetlendi, iki araştırma yolu kapandı, bir tanesi de arşivin kendi kuralıyla çelişiyor çıktı.

## Şu anki durum

| | |
|---|---|
| Dal | `claude/proje-arsiv-revizyon-yzwtvq` |
| Vaka sayısı | **124 kayıt** — A 6 · B 25 · C 92 · X 1 · **arşivde 122** (X001 ve A006'ya devredilen C027 hariç) |
| İş kolu | 16 gerçek niş + `tartismali` |
| Doğrulayıcılar | `validate_catalog.py` 42 kayıt · `validate_cases.py` 124 kayıt + 3 çapraz kontrol — **ikisi de geçiyor** |
| Sabitlenmiş sürümler | **9/9 doğrulandı** — [2026-09-03 raporu](research/PIN-DOGRULAMA-2026-09-03.md) |
| `docs/` | 22 sayfalık Wiki, veriyle taze · ayrıca elle tutulan `docs/repo-discovery/` |
| Canlı site | Yayında ve doğrulandı — https://paradoksix.github.io/ai-money-workflows/ |

---

# Bu turda ne oldu

## 1. Sabitlenmiş sürümler ilk kez denetlendi — dokuzu da sağlam

Arşivin bütün iddiası "işin tam olarak hangi kodla yapıldığını biliyoruz"a dayanıyor, ama o bağ **yazıldığı günden beri bir kez bile yeniden sınanmamıştı.** Özgün depo silinse, adı değişse ya da geçmişi yeniden yazılsa arşiv var olmayan bir sürümü göstermeye devam edecekti.

`scripts/verify_pins.py` bunu tekrarlanabilir hale getiriyor. Depo adresi **ve** 40 karakterlik sürüm kimliği taşıyan 9 kaydın her biri için üç soru soruyor: özgün depo hâlâ cevap veriyor mu · sabitlenen sürüme hâlâ ulaşılabiliyor mu · `license_status` gerçekle uyuşuyor mu.

**Sonuç: 9/9 doğrulandı.** Dokuzunun da kök dizininde lisans yok (kayıt doğru). Üçünde özgün depo sabitlenen sürümün ilerisine geçmiş (A005 · A006 · B002) — bu beklenen durum, sabitlemenin varlık sebebi zaten bu.

Bu denetim **bayatlar**: sabitlenmiş sürüm eklendiğinde ve derece değiştiğinde tekrar çalıştır.

```bash
python3 scripts/verify_pins.py
python3 scripts/verify_pins.py --report research/PIN-DOGRULAMA-<tarih>.md
```

Bunu mümkün kılan şey yeni keşfedildi ve `CLAUDE.md`'ye yazıldı: GitHub API'sinin `repos/*` yolları proxy'de kapalı olsa da **`git ls-remote` ve sabitlenen sürümü tek tek çekmek çalışıyor.**

## 2. Pazar yeri yolu kapandı — önceki HANDOFF'un "buradan başla" önerisi yanlıştı

Önceki tur şunu öneriyordu: kaynağı olmayan vakaların büyük kısmı Fiverr/Upwork ilanlarından geliyor, `WebSearch` bu alan adlarını reddetmiyor, öyleyse ilan adresleri bulunabilir. **Sınandı, yürümüyor.** Üç ayrı sebep üst üste biniyor:

1. `WebSearch` gerçekten çalışıyor ve **gerçek ilan adresleri döndürüyor** — o kısım doğruydu.
2. Ama `fiverr.com` ve `upwork.com` sayfalarının kendisi ağ katmanında kapalı (`EGRESS_BLOCKED`). Bulunan ilanın yorum sayısı ya da fiyatı **açılıp doğrulanamıyor.**
3. Asıl engel bu: arşivin bu vakalarda tuttuğu alanlar **kimlik belirtmiyor.** `38 müşteri yorumu` + `$30/saat` ile binlerce neredeyse aynı ilan arasından bir tanesi seçilemez; arama motoru yorum sayısına göre indekslemiyor ve yorum sayısı zaten sürekli değişiyor.

Yani bulunan bir ilanı `source_url` diye yazmak, **arşivin sahip olmadığı kanıtı üretmek** olurdu. Kaynağı olmayan 74 vakanın **42'si** bu sınıfta (`N müşteri yorumu` / `görünür sipariş` sinyali taşıyanlar). Kuyruğa 42 mekanik satır eklemedim — bulgu sınıfın tamamı için geçerli ve burada duruyor. **Aynı aramayı tekrarlama.**

## 3. Açık bulgu: 23 B vakası kendi derecesinin tanımını karşılamıyor

**Bu turda karara bağlanmadı — kullanıcının kararı gerekiyor.**

`B` derecesinin tanımı `RESEARCH_POLICY.md`'de net: *"Kod açıkta duruyor ve ticari bağlam güçlü; fakat tam olarak bu iş akışının para kazandırdığı gösterilmemiş."* Yani B'nin tek şartı **kodun açık olması**.

25 B vakasının **23'ünde ne depo adresi ne kaynak adresi var:**

| Durum | Sayı |
|---|---|
| "Açık JSON" / "çalışan iş akışı açık" diyor, ama adresi hiçbir yerde yazmıyor | **9** |
| Ansiklopedi metninde **hiç kanıt satırı yok** | **14** |
| Adresi gerçekten kayıtlı olan (B001, B002) | 2 |

Yirmi üçünde de `reported_amount` ve `revenue_type` boş. Yani bu kayıtlar ne para kanıtı ne kod adresi taşıyor; B derecesi fiilen "kulağa makul gelen bir otomasyon fikri" anlamına gelmiş.

**`C`'ye indirmek de yanlış olur:** C'nin tanımı "para kazandırmış, kodu yok" — bu 23 kayıtta para kanıtı da yok, yani C onları para ekseninde *yükseltmiş* olur.

Seçenekler ve etkileri sonraki oturumda kullanıcıya sunulacak. Hangisi seçilirse seçilsin dört derecenin adı üç yerde birebir aynı kalmalı (`RESEARCH_POLICY.md` · `CLAUDE.md` özeti · `build_site.py`'deki `GRADES`) ve README'nin 12 rakamı veriden yeniden üretilmeli.

## 4. Kayda geçmemiş bir yapım dalgası var: Repo Discovery Engine

2-3 Eylül'de `main`'e altı commit girmiş (`9a249f4` → `909ba0b`) ve `builds/repo-discovery-demo/` + `docs/repo-discovery/` altında çalışan bir keşif motoru kurulmuş. **Önceki HANDOFF'ta tek satır yok.** Ne olduğu:

`data/cases.csv`'yi tarayıcıda okuyup önce arşivdeki vakaları tek tek kart olarak gösteriyor; arşiv tükenince `cases.csv`'den türettiği desenlerle GitHub'da arşivde olmayan depoları arıyor ve her adayın hangi vakalardan türediğini gösteriyor. **Model çağrısı yok, ücretsiz, tamamen tarayıcı tarafında.** Arşive veri yazmıyor.

Bakım borcu olarak not edilenler — hiçbiri bu turda ellenmedi:

- `app.js` **ölü kod**: hiçbir HTML yüklemiyor, kaldırılmış `#minStars`/`#deepWikiLink` alanlarını arıyor, ama hâlâ `docs/`'a yayınlanıyor ve `repo-discovery-demo.yml` tarafından denetleniyor. Deponun DeepWiki yasağını delen tek dosya da bu (yasak yalnız `index.html` ve `archive-app.js`'i tarıyor).
- `builds/repo-discovery-demo/README.md` **silinmiş uygulamayı** anlatıyor ve var olmayan bir mimari dosyasına atıf yapıyor.
- Sayfaya **hiçbir yerden link yok** — Wiki'de, README'de, hiçbir yerde. Adresi bilmeyen bulamaz.
- İki iş akışı (`repo-discovery-demo.yml` ve `archive-discovery.yml`) aynı klasör üzerinde **birbiriyle çelişen** mimariler doğruluyor.
- `builds/` ↔ `docs/` kopyası **elle** tutuluyor; CI eşitliği sonradan denetliyor ama `app.js` iki denetimin de dışında, sessizce ayrışabilir.

---

# Sıradaki iş

Araştırmanın ucu açık, sabit hedef sayı yok. Ölçütler gevşemiyor.

## Kalan boşluklar

| Boşluk | Sayı | Anlamı |
|---|---|---|
| `status = encyclopedia_only` | **82 / 124** | Hiç araştırma kuyruğundan geçmemiş |
| `research_queue.csv`'de olmayan C vakası | **50 / 92** | Kuyruk 42 satır |
| `source_url` boş | **74 / 124** | Bunun **42'si** pazar yeri sınıfı — yukarıda kapandı |
| `revenue_type` boş | **33 / 124** | |
| `reported_amount` boş | **39 / 124** | |
| Depo adresi olan kayıt | **9 / 124** | Doğrulanmış kaynak kodun tamamı bu |

## Denenmiş ve tükenmiş: tekrarlama

- **42 pazar yeri vakası.** Yukarıda 2. maddede. Sebebiyle birlikte kapandı.
- **C076–C084 (dokuz vaka).** Hepsi tek bir Reddit başlığından geliyor ama adresi hiç kaydedilmemiş. Üç ayrı açıdan arandı (CRM ara katmanı `$3.500/ay` · D365 IOM `~$240K/yıl` · tıbbi cihaz son kullanma `$36K/çeyrek`) — hiçbiri bulmadı.
- **11 altın vaka** (C004 · C003 · C002 · C006 · C005 · C001 · C007 · C008 · C018 · C029 · C076). **İki tur denendi, hiçbiri A/B'ye yükselmedi.** Çoğu engelli alan adlarına bağlı.
- **C003 için `conor-is-my-name` adayı reddedildi** — teknik olarak uyumlu ama doğrulanmamış. Yeniden aday gösterme.

## Nasıl kaydedilir

**Asıl takip yeri `research_queue.csv`'nin `next_action` sütunudur.** Mevcut 42 satır *gerçek bulgular* taşıyor, dolgu değil. Aynı seviyeyi koru: **tarihli, ne denendi, ne bulundu, sıradaki adım ne.** Bir bulgu bütün bir sınıf için geçerliyse HANDOFF'a yaz — kuyruğa aynı cümleden 42 tane ekleme; kuyruğu dolu gösterir ama takip ediliyormuş yanılsaması yaratır.

Üç kural, arşivin bütün değeri bunlara bağlı:

1. **Bulunamadıysa uydurma.** "bulunamadı" diye, ne denendiğiyle birlikte kaydet.
2. **Çıkarım yapma.** 33 boş `revenue_type` ve 39 boş `reported_amount` ansiklopedi metnine karşı kontrol edildi — **hiçbirinde açık gelir etiketi ya da rakam yok.** Doldurmak, arşivin sahip olmadığı kanıtı üretmek olur. Boş bırak.
3. **Gelir etiketleri karışmaz** — F (işi yapana ödenen ücret) · R (üründen gelir) · S (müşterinin tasarrufu) · V (başka ticari sonuç).

**Bir vaka üç yerde birden yaşıyor:** `data/cases.csv` · `encyclopedia/nis-*.md` · gerekiyorsa `research_queue.csv`. `catalog.csv`'de karşılığı olan bir vakanın `title`, `evidence_grade`, `status`, `work_model`, `reported_result`, `source_url`, `repo_url`, `pinned_commit` alanları **birebir aynı olmak zorunda**.

Veri değişince `docs/` yeniden üretilip **aynı commit'e** konur.

---

## Gelecek fikri: repo gönderim ve tarama hattı

**Tasarlanmadı** — burada yalnız fikir ve kısıtlar kayıtlı. Not: yukarıdaki keşif motoru bu fikrin *okuma* tarafını zaten kısmen yapıyor (aday bulma, arşivle karşılaştırma), ama gönderim ve onay tarafı hâlâ yok.

1. **Wiki'de bir gönderim sayfası.** Ziyaretçi para kazandırdığını düşündüğü bir reponun linkini bırakır.
2. **Modele gitmeden ücretsiz elemeler.** Link gerçekten GitHub reposu mu · `cases.csv`'de zaten var mı · kök dizinde açık lisans var mı · depo boş/arşivlenmiş mi. Çoğu gönderim burada elenir, **modele hiç ulaşmaz**.
3. **Elemeyi geçen için tek ve küçük model çağrısı.** Yalnız repo üstverisi: ad, açıklama, konu etiketleri, README'nin ilk birkaç bin karakteri. **Kod indirilmez, dosya ağacı taranmaz.**
4. **Karar kullanıcıda.** Otomatik ekleme yok.
5. **Onaylananlar için derin araştırma.**

**Token maliyeti bu tasarımın ana kısıtı.** **Çözülmemiş sorular:** GitHub Pages statik — formu alacak ve taramayı koşturacak bir yer yok (en büyük açık uç) · yönetim paneli kimlik doğrulaması · onaylanan adayın üç dosyaya nasıl bağlanacağı.

## Kapanmış turlar — yeniden açma

- **Wiki (PR #5, 7 commit).** `docs/` artık 22 sayfa, veriden üretiliyor. 123 vaka bloğunun tamamı sitede, her vakada 19 kolonluk künye — **boş alanlar gizlenmiyor**, "kaynağın tam adresi kaydedilmemiş" diye yazıyor. Araştırma ilerledikçe site kendiliğinden doluyor.
- **Dil kuralı** `RESEARCH_POLICY.md` ve `CLAUDE.md`'ye de uygulandı; karşılık tablosu `CLAUDE.md` → Dil kuralı bölümünde.
- **Bilerek yapılmadı:** İngilizce vaka adları Türkçeleştirilmedi — melez jargon değil, vakanın kaynağındaki adı; çevirmek kaynağa geri izlenebilirliği zorlaştırır.
- **Pages dersi.** Yeşil derleme bir derlemenin *bittiğini* söyler, *neyin yayınlandığını* söylemez. "Canlı" iddiası yalnız `verify-live-site` yeşiline ya da kullanıcının teyidine dayanabilir.

## Kullanıcıya kalan manuel iş

- `claude/handoff-wiki-conversion-xemu2b` dalı hâlâ duruyor. **Tamamen merge edilmiş** — `main`'de olmayan commit'i yok, silinse hiçbir şey kaybolmaz. Dal silme buradan yapılamıyor (proxy yazma yollarını kapatıyor). **Acil değil.**
- Bu turun dalı: `claude/proje-arsiv-revizyon-yzwtvq` — PR açılmadı, dalda bekliyor.

## Yeni oturum için ilk adımlar

1. `CLAUDE.md`'yi oku — kanıt dereceleri, lisans kuralı, dil kuralı, veri sözleşmesi, ortam kısıtları.
2. Yeşil zemini teyit et:
   ```bash
   python3 scripts/validate_catalog.py
   python3 scripts/validate_cases.py
   python3 scripts/build_site.py && git diff --exit-code docs
   grep -hc '^## [ABCX][0-9]' encyclopedia/nis-*.md | paste -sd+ | bc   # 123 olmalı
   ```
3. **Açık karar var:** yukarıdaki 3. madde — 23 B vakasının derecesi. Araştırmaya devam etmeden önce bu karara bağlanmalı, çünkü A/B/C sayıları README'nin 12 rakamını ve Wiki'yi etkiliyor.
4. Turu kapatan commit bu dosyayı da güncellesin.
