# HANDOFF

**Nerede kaldık** dosyası. Turdan tura değişmeyen kurallar için [`CLAUDE.md`](CLAUDE.md)'ye bak — bu dosya her turda güncellenir.

Son güncelleme: **2026-09-03**. Bu tur **arşiv doğrulamasıydı**: sabitlenmiş sürümler ilk kez denetlendi, bir araştırma yolu sebebiyle birlikte kapandı, 23 kaydın kendi derecesiyle çelişkisi işaretlendi ve kayda geçmemiş keşif motoru hem yazıldı hem ölü kodundan arındırıldı.

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

## 3. Kapandı: 23 B vakası artık ne olduğunu söylüyor

`B` derecesinin tanımı `RESEARCH_POLICY.md`'de net: *"Kod açıkta duruyor ve ticari bağlam güçlü; fakat tam olarak bu iş akışının para kazandırdığı gösterilmemiş."* Yani B'nin tek şartı **kodun açık olması**.

25 B vakasının **23'ünde ne depo adresi ne kaynak adresi vardı** — üstelik hepsinde `reported_amount` ve `revenue_type` de boş. Dört derecenin mantığı şu: A = para✓ kod✓ · B = para✗ kod✓ · C = para✓ kod✗. "para✗ kod✗" için arşivde karşılık yok, o yüzden bu 23 kayıt B'ye park edilmişti.

**Karar: derece duruyor, durum işaretlendi.** `status` alanı `encyclopedia_only`'den ikiye ayrıldı:

| Yeni durum | Sayı | Wiki'de görünen |
|---|---|---|
| `open_code_claimed_unlocated` | **8** | "Kodun açık olduğu söyleniyor, ama adresi kayıtlı değil" |
| `no_recorded_evidence` | **15** | "Derecesini destekleyen hiçbir kanıt kaydedilmemiş" |

İlk grup (B003 · B004 · B005 · B006 · B009 · B012 · B014 · B017) ansiklopedi metninde "Açık JSON" / "çalışan iş akışı açık" diyor ama o dosyanın adresi hiçbir yerde yazmıyor. İkinci grup (B007 · B008 · B010 · B011 · B013 · B015 · B016 · B018–B025) **hiç kanıt satırı taşımıyor.**

Yirmi üçü de `research_queue.csv`'ye girdi (kuyruk 42 → 65 satır). İlk grubun `next_action`'ı dayandığı iddiayı **birebir alıntılıyor**, yani sonraki oturum tam olarak neyi arayacağını biliyor.

**`C`'ye indirilmedi, bilerek:** C'nin tanımı "para kazandırmış, kodu yok" — bu 23 kayıtta para kanıtı da yok, yani C onları para ekseninde *yükseltmiş* olurdu.

Derece sayıları değişmedi (A6 · B25 · C92 · X1), dolayısıyla README'nin 12 rakamı ve dört derecenin üç yerdeki adı da aynı kaldı. Adres bulunursa kayıt gerçek B olur — karar geri alınabilir.

## 4. Keşif motoru kayda geçti ve ölü kodu temizlendi

2-3 Eylül'de `main`'e altı commit girmiş (`9a249f4` → `909ba0b`) ve `builds/repo-discovery-demo/` + `docs/repo-discovery/` altında çalışan bir keşif motoru kurulmuş. **Önceki HANDOFF'ta tek satır yoktu.**

Ne yaptığı: `data/cases.csv`'yi tarayıcıda okuyup arşivdeki vakaları tek tek kart olarak gösteriyor; seçilen odaktaki vakalar tükenince `cases.csv`'den türettiği desenlerle GitHub'da **arşivde olmayan** depoları arıyor ve her adayın hangi vakalardan türediğini gösteriyor. **Model çağrısı yok, ücretsiz, tamamen tarayıcı tarafında.** Arşive veri yazmıyor.

Bu turda temizlenenler:

- **`app.js` silindi** (iki kopyadan da). Hiçbir HTML yüklemiyordu, kaldırılmış alanları arıyordu ve deponun DeepWiki yasağını delen tek dosyaydı — yasak yalnız iki dosyayı tarıyordu, o ise üçüncüsüydü.
- **DeepWiki yasağı klasörün tamamına genişletildi** (`grep -rqi`). Artık hiçbir şeyin yüklemediği bir dosya bile yasağı delemiyor.
- **`repo-discovery-demo.yml` kaldırıldı.** İçindeki denetimlerin tamamı ya ölü `app.js` hakkındaydı ya da diğer iki iş akışında zaten vardı. Yalnız araç çubuğu alanlarının denetimi (`repoCard` · `wikiBtn` · `tokenInput` · `importInput`) tek başınaydı; **kaybolmasın diye `card-metric-ui.yml`'e taşındı.** Çelişen iki mimari doğrulaması böylece bitti.
- **README yeniden yazıldı.** Eskisi silinmiş uygulamayı anlatıyordu, var olmayan bir mimari dosyasına atıf yapıyordu ve verdiği çalıştırma komutu **Wiki düğmesini bozuyordu** (bu klasörden servis edilince `../nis-*.html` adresleri boşa çıkıyor, üstelik sayfanın geri kalanı çalıştığı için fark edilmiyor). Yenisi `docs/` kökünden servis etmeyi, ağa çıktığı dört yeri ve iki kopyanın elle tutulduğunu yazıyor.

**Yapılmadı, duruyor:** sayfaya hâlâ hiçbir yerden link yok — Wiki'de, README'de, hiçbir yerde. Adresini bilmeyen bulamaz. Bağlamak Wiki üreticisine dokunmayı gerektiriyor, ayrı bir tur.

**Küçük not:** üç iş akışının canlı sayfa dumanı testi sunucuyu `sleep 1` ile bekliyor. Yerelde bu yarışı bir kez yakaladım (sunucu geç açılınca ilk kontroller düşüyor). Şimdiye kadar CI'da patlamamış ama hazır bir tökezleme; hazır dokunulmuşken hazır olana kadar bekleyen bir döngüye çevrilebilir.

---

# Sıradaki iş

Araştırmanın ucu açık, sabit hedef sayı yok. Ölçütler gevşemiyor.

## Kalan boşluklar

| Boşluk | Sayı | Anlamı |
|---|---|---|
| `status = encyclopedia_only` | **59 / 124** | Hiç araştırma kuyruğundan geçmemiş (23'ü bu turda çıktı) |
| `research_queue.csv`'de olmayan C vakası | **50 / 92** | Kuyruk 65 satır |
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
