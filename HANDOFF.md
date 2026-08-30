# HANDOFF

**Nerede kaldık** dosyası. Turdan tura değişmeyen kurallar için [`CLAUDE.md`](CLAUDE.md)'ye bak — bu dosya her turda güncellenir.

Son güncelleme: **2026-08-30**. Wiki turu kapandı; **sıradaki iş araştırmanın kendisi.**

## Şu anki durum

| | |
|---|---|
| Dal | **`main`**, çalışma ağacı temiz · açık PR yok · açık issue yok |
| Vaka sayısı | **124 kayıt** — A 6 · B 25 · C 92 · X 1 · **arşivde 122** (X001 ve A006'ya devredilen C027 hariç) |
| İş kolu | 16 gerçek niş + `tartismali` |
| Doğrulayıcılar | `validate_catalog.py` 42 kayıt · `validate_cases.py` 124 kayıt + 3 çapraz kontrol — **ikisi de geçiyor** |
| `docs/` | **22 sayfalık Wiki**, veriyle taze |
| Canlı site | **Yayında ve doğrulandı** — `verify-live-site` iş akışı kök adreste Wiki'yi, alt sayfalarını ve varlıklarını buldu. https://paradoksix.github.io/ai-money-workflows/ |

---

# Sıradaki iş: araştırma

Kullanıcının kararı: **araştırmanın ucu açık, sabit hedef sayı yok.** Ölçütler gevşemiyor — A/B/C/X eşikleri ve lisans kuralı aynen duruyor; değişen tek şey arşivin bir bitiş sayısına doğru yürümemesi.

Yeni vaka aramak kadar **eldeki 124 kaydın boşluklarını kapatmak** da iş:

| Boşluk | Sayı | Anlamı |
|---|---|---|
| `status = encyclopedia_only` | **82 / 124** | Hiç araştırma kuyruğundan geçmemiş |
| `research_queue.csv`'de olmayan C vakası | **50 / 92** | Kuyruk 42 satır |
| `source_url` boş | **74 / 124** | En ağır nişler: video-görsel **18** · müşteri iletişimi **11** · içerik-sosyal medya **10** · B2B lead **7** |
| `revenue_type` boş | **33 / 124** | 2 A + 24 B + 7 C |
| `reported_amount` boş | **39 / 124** | |

## Buradan başla: 25 pazar yeri vakası

**En verimli yol bu ve erişilebilirliği sınandı.** Kaynağı olmayan 74 vakanın **25'i** Fiverr/Upwork tipi ilanlardan geliyor — metinlerinde `38 review`, `$30/saat`, `$50–100` gibi pazar yeri sinyalleri var. Örnekler: **C036 · C038 · C041 · C043 · C044 · C046 · C047 · C050**.

Neden umut verici:

- **`fiverr.com` ve `upwork.com` doğrudan çekilemiyor** (`curl` → `000`), **ama `WebSearch` bu alan adlarını reddetmiyor ve gerçek ilan adresleri döndürüyor** — 2026-08-30'da sınandı. Reddit'ten farkı bu: Reddit'te arama motorunun kendisi alan adını reddediyor (`400`).
- İlan adresi tam olarak `source_url`'ün ihtiyacı olan şey.
- Bu 25 vaka **hiç denenmedi** — altın vakalar gibi iki tur harcanmış değil.

Şunu bulmaya çalış: ilanın kendi adresi · satıcının profili · review sayısı ve fiyatın metinle tutup tutmadığı. **Kod bulunursa** derece C'den yukarı çıkabilir; bulunmazsa kaynak adresi bile tek başına kazanç, çünkü `source_url` doluyor.

## Denenmiş ve tükenmiş: tekrarlama

- **C076–C084 (dokuz vaka).** Hepsi tek bir Reddit başlığından geliyor ama adresi hiç kaydedilmemiş. Üç ayrı açıdan arandı (CRM ara katmanı `$3.500/ay` · D365 IOM `~$240K/yıl` · tıbbi cihaz son kullanma `$36K/çeyrek`) — hiçbiri bulmadı. Dokuzu da dürüst kayıtla kuyrukta. **Aynı aramaları yapma.**
- **11 altın vaka** (C004 Powerprozesse · C003 50K katalog · C002 Japon fatura · C006 AigencyTracker · C005 muhasebe · C001 gemi yöneticisi · C007 Shopify stok · C008 kitapçı WhatsApp · C018 `$5K` özel ders · C029 üniversite RAG · C076 tıbbi cihaz). **İki tur denendi, hiçbiri A/B'ye yükselmedi.** Çoğu engelli alan adlarına bağlı. Düşük verim; pazar yeri vakaları bitmeden buraya dönme.
- **C003 için `conor-is-my-name` adayı reddedildi** — teknik olarak uyumlu ama doğrulanmamış. Yeniden aday gösterme.

## Nasıl kaydedilir

**Asıl takip yeri `research_queue.csv`'nin `next_action` sütunudur** — issue checklist'i değil. Mevcut 42 satır *gerçek bulgular* taşıyor ("powerprozesse.de aktif bir şirket, GitHub varlığı yok" gibi), dolgu değil. Aynı seviyeyi koru: **tarihli, ne denendi, ne bulundu, sıradaki adım ne.** Mekanik satır eklemek kuyruğu dolu gösterir ama hiçbir şey katmaz — dahası takip ediliyormuş yanılsaması yaratır.

Üç kural, arşivin bütün değeri bunlara bağlı:

1. **Bulunamadıysa uydurma.** "bulunamadı" diye, ne denendiğiyle birlikte kaydet.
2. **Çıkarım yapma.** 33 boş `revenue_type` ve 39 boş `reported_amount` ansiklopedi metnine karşı kontrol edildi — **hiçbirinde açık gelir etiketi ya da rakam yok.** Doldurmak, arşivin sahip olmadığı kanıtı üretmek olur. Boş bırak.
3. **Gelir etiketleri karışmaz** — F (işi yapana ödenen ücret) · R (üründen gelir) · S (müşterinin tasarrufu) · V (başka ticari sonuç). Ayrıntı `CLAUDE.md`'de.

**Bir vaka üç yerde birden yaşıyor:** `data/cases.csv` · `encyclopedia/nis-*.md` · gerekiyorsa `research_queue.csv`. `validate_cases.py` üçü arasında çapraz kontrol yapıyor, yani biri değişince diğerleri de tutmalı. `catalog.csv`'de karşılığı olan bir vakanın `title`, `evidence_grade`, `status`, `work_model`, `reported_result`, `source_url`, `repo_url`, `pinned_commit` alanları **birebir aynı olmak zorunda**.

Veri değişince `docs/` yeniden üretilip **aynı commit'e** konur, yoksa CI tazelik kontrolünde kırılır.

---

## Gelecek fikri: repo gönderim ve tarama hattı

Araştırmanın ucu açık olmasının kullanıcının tarif ettiği yolu. **Tasarlanmadı** — burada yalnız fikir ve kısıtlar kayıtlı; uygulamadan önce ayrı bir tasarım turu gerekiyor.

1. **Wiki'de bir gönderim sayfası.** Ziyaretçi para kazandırdığını düşündüğü bir reponun linkini bırakır.
2. **Modele gitmeden ücretsiz elemeler.** Link gerçekten GitHub reposu mu · `cases.csv`'de zaten var mı · kök dizinde açık lisans var mı · depo boş/arşivlenmiş mi. Çoğu gönderim burada elenir, **modele hiç ulaşmaz**.
3. **Elemeyi geçen için tek ve küçük model çağrısı.** Yalnız repo üstverisi: ad, açıklama, konu etiketleri, README'nin ilk birkaç bin karakteri. **Kod indirilmez, dosya ağacı taranmaz.** Haiku sınıfı yeter.
4. **Karar kullanıcıda.** Ayrı bir yönetim paneli sayfasında bildirim düşer; ekle/ekleme kararını yalnız kullanıcı verir. Otomatik ekleme yok.
5. **Onaylananlar için derin araştırma** — repo incelenir, vaka araştırılır, mevcut kayıtlarla çakışma kontrol edilir, uygun nişe ve dereceye yerleştirilir.

**Token maliyeti bu tasarımın ana kısıtı** (kullanıcı iki kez vurguladı): ücretsiz elemeler her zaman modelden önce koşar, model çağrısı gönderim başına bir tane ve küçük.

**Çözülmemiş sorular:** GitHub Pages statik — formu alacak ve taramayı koşturacak bir yer yok, depo dışında bir şey gerekiyor (en büyük açık uç) · yönetim paneli kimlik doğrulaması · onaylanan adayın yukarıdaki üç dosyaya nasıl bağlanacağı · `docs/` üretilen çıktı olduğu için hat oraya doğrudan yazamaz.

## Kapanmış turlar — yeniden açma

Ayrıntı git geçmişinde ve [PR #5](https://github.com/paradoksix/ai-money-workflows/pull/5)'te. Buraya yalnız sonraki işi kısıtlayanlar:

- **Wiki (PR #5, 7 commit).** `docs/` artık 22 sayfa, `data/cases.csv` ve `encyclopedia/*.md`'den üretiliyor. 123 vaka bloğunun tamamı sitede, her vakada 19 kolonluk künye — **boş alanlar gizlenmiyor**, "kaynağın tam adresi kaydedilmemiş" diye yazıyor. Yani araştırma ilerledikçe site kendiliğinden doluyor.
- **Dil kuralı `RESEARCH_POLICY.md` ve `CLAUDE.md`'ye de uygulandı.** Kullanılacak karşılıklar `CLAUDE.md` → Dil kuralı bölümünde tablo hâlinde. **Dört derecenin adı üç yerde birebir aynı** olmalı: `RESEARCH_POLICY.md` başlıkları, `CLAUDE.md` özeti, `build_site.py`'deki `GRADES`.
- **Bilerek yapılmadı:** İngilizce vaka adları Türkçeleştirilmedi (ör. "Faceless Editing / Content Service"). Melez jargon değil, vakanın kaynağındaki adı; çevirmek kaynağa geri izlenebilirliği zorlaştırır. `research/GOLDEN-CASES-DEEP-DIVE-*.md` hâlâ eski dili taşıyor ama iç not, yayınlanan metin değil — kapsam dışı.
- **Pages dersi.** Site turlarca "canlı" sanıldı çünkü "pages build and deployment" yeşili öyle okundu. Yeşil derleme bir derlemenin *bittiğini* söyler, *neyin yayınlandığını* söylemez. Kaynak kök dizindeydi, Jekyll README'yi yayınlıyordu. `verify-live-site.yml` artık bunu makineye sorduruyor; **"canlı" iddiası yalnız o iş akışının yeşiline ya da kullanıcının teyidine dayanabilir.**

## Kullanıcıya kalan manuel iş

Tek şey: `claude/handoff-wiki-conversion-xemu2b` dalı hâlâ duruyor. **Tamamen merge edilmiş** — `main`'de olmayan commit'i yok, PR #5 ile girdi, silinse hiçbir şey kaybolmaz. Kullanıcı kendisi silecek. Diğer iki bayat dal silindi.

Dal silme buradan yapılamıyor: GitHub MCP'sinde araç yok. `git push origin --delete` git protokolü üzerinden gittiği için çalışabilir ama denenmedi. **Acil değil**, oturum sonunda hatırlatmak yeterli.

## Yeni oturum için ilk adımlar

1. `CLAUDE.md`'yi oku — kanıt dereceleri, lisans kuralı, dil kuralı (karşılık tablosuyla), veri sözleşmesi, ortam kısıtları.
2. Yeşil zemini teyit et:
   ```bash
   python3 scripts/validate_catalog.py
   python3 scripts/validate_cases.py
   python3 scripts/build_site.py && git diff --exit-code docs
   grep -hc '^## [ABCX][0-9]' encyclopedia/nis-*.md | paste -sd+ | bc   # 123 olmalı
   ```
3. **Açık karar ve bekleyen düzeltme yok.** Doğrudan araştırmaya geç: yukarıdaki **25 pazar yeri vakası**. Denenmiş ve tükenmiş listesini önce oku, o aramaları tekrarlama.
4. Turu kapatan commit bu dosyayı da güncellesin: yeni bulgular, derece değişiklikleri, tazelenmiş boşluk tablosu.
