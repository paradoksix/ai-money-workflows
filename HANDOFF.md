# HANDOFF

**Nerede kaldık** dosyası. Turdan tura değişmeyen kurallar için [`CLAUDE.md`](CLAUDE.md)'ye bak — bu dosya her turda güncellenir.

Son güncelleme: **2026-08-28**, "yeniden düzenleme turu"nun kapanışında.

## Şu anki durum

| | |
|---|---|
| Dal | `main` — bu handoff'tan önceki son içerik commit'i `031c47f`; çalışma ağacı temiz, 49 dosya |
| Vaka sayısı | **124 kayıt** — A 6 · B 25 · C 92 · X 1 · **arşivde 122** (X001 ve A006'ya devredilen C027 hariç) |
| İş kolu | 16 gerçek niş + `tartismali` |
| `validate_catalog.py` | 42 kayıt — **geçiyor** |
| `validate_cases.py` | 124 kayıt + 3 çapraz kontrol — **geçiyor** |
| `docs/index.html` | veriyle **taze**, 153 KB |
| GitHub Pages | **canlı** — https://paradoksix.github.io/ai-money-workflows/ |
| Repo About kutusu | **dolu** — açıklama + website + 10 konu etiketi |
| Issue | **açık issue yok** — #1 ve #3 tamamlandı olarak, #2 (duraklatılmış build dalgası) "planlanmadı" olarak kapalı |
| PR | #4 merge edildi (2026-08-27) — **açık PR yok** |

## Bu turda ne yapıldı

Bu tur **yeni vaka eklemedi**; arşivi gezilebilir ve doğrulanabilir hâle getirdi.

- **`data/cases.csv` sıfırdan kuruldu** (124 kayıt, 19 kolon). Öncesinde 124 vakanın **82'si yalnız düzyazı olarak vardı** — hiçbir yapılandırılmış tabloda görünmüyordu.
- **8 cilt 16 nişe bölündü.** `VOLUME-01..08-*.md` yerine `nis-01..16-*.md`. Gezinme artık kanıt derecesiyle konuyu karıştırmıyor. **123 vaka bloğunun tamamı bayt-bayt korundu** (git HEAD ile karşılaştırılarak doğrulandı). Ciltlerin sentez bölümleri `encyclopedia/DESENLER.md`'ye taşındı.
- **`scripts/build_site.py`** yazıldı — `data/cases.csv`'den arama + üç filtreli atlas sayfası üretir, saf stdlib, deterministik.
- **`scripts/validate_cases.py`** yazıldı — şema + 3 çapraz kontrol: katalog ↔ `cases.csv` alan uyumu, ansiklopedi başlıkları ↔ kayıtlar, **README rakamları ↔ veri**.
- **Sade Türkçe geçişi.** Arayüz metinleri, başlıklar ve kart özetlerindeki melez jargon ("exact kaynak" vb.) sıradan okurun anladığı ifadelerle değiştirildi. Kural artık `CLAUDE.md`'de kalıcı.
- **README yeniden yazıldı**, ekran görüntüsü ve rozetler eklendi; **CC BY 4.0 `LICENSE`** kapsam notuyla eklendi (deponun kendi içeriğini kapsar, atıf verilen upstream kodu kapsamaz).
- **Pages açıldı**, depodaki tüm atlas linkleri canlı adrese çevrildi (GitHub `.html`'i render etmiyor, ham kaynak gösteriyordu).
- **Veri yarası düzeltildi:** C076–C084 (9 vaka) yanlışlıkla C005'in Reddit URL'ini taşıyordu. Temizlendi; her birine "kaynak thread ansiklopedide adıyla anılıyor ama tam adresi hiç kaydedilmemiş, bulunamadı" notu düşüldü. README'deki kaynaklı vaka sayısı 59 → 50 düzeltildi.
- **Issue #1 ve #3 dürüst gerekçeyle kapatıldı** — "tamamlandı" diye işaretlenmedi; #1'in takibi `research_queue.csv`'ye, #3'ün hedefi README'nin "Proje durumu" bölümüne taşındı.

## Sıradaki iş: araştırmayı tamamlama

Kullanıcının bir sonraki oturum için tarifi: **"araştırmaların son noktasına kadar genişletilip, eksiklerin giderilip araştırmanın tamamlanma evresinden devam edeceğiz."**

Bunun sayısal karşılığı ölçüldü. Aşağıdaki tablo bir sonraki turun malzemesi:

| Boşluk | Sayı | Anlamı |
|---|---|---|
| `status = encyclopedia_only` | **82 / 124** | Hiç araştırma kuyruğundan geçmemiş; yalnız ansiklopedi metninde var |
| `research_queue.csv`'de olmayan C vakası | **59 / 92** | Kuyruk yalnız 33 satır — C vakalarının üçte ikisi takip edilmiyor |
| `source_url` boş | **74 / 124** | 23 B + 51 C. En ağır nişler: video-görsel **18**, müşteri iletişimi **11**, içerik-sosyal medya **10**, B2B lead **7** |
| `revenue_type` boş | **33 / 124** | 2 A + 24 B + 7 C |
| `reported_amount` boş | **39 / 124** | |

`research_queue.csv`'nin şu anki 33 satırı: 28 `repo_missing`, 3 `needs_verification`, 1 `resolved_see_A006`, 1 `source_private`. **Asıl takip yeri bu dosyanın `next_action` sütunudur** — issue checklist'i değil.

**Kaynağı hâlâ aranan 11 altın vaka** (öncelik sırasıyla): C004 Powerprozesse · C003 50K katalog (`conor-is-my-name` adayı **reddedildi**, yeniden kullanma) · C002 Japon fatura işleyici · C006 AigencyTracker · C005 muhasebe otomasyonu · C001 gemi yöneticisi lead · C007 Shopify stok · C008 kitapçı WhatsApp · C018 `$5K` özel ders · C029 çevrimdışı üniversite RAG · C076 tıbbi cihaz son kullanma takibi.

Bunların çoğu **engelli alan adlarına** (Reddit, Linktree) ihtiyaç duyuyor — `CLAUDE.md`'deki ortam kısıtlarına bak. İki tur denendi, hiçbiri A/B'ye yükselmedi. Yeni turda daha verimli olabilecek yön: yukarıdaki tablodaki **82 `encyclopedia_only` vakası**, çünkü bunlar hiç denenmedi.

## Açıkta bırakılan iki karar

Kullanıcı ikisini de bilerek **bu handoff'tan sonraya** erteledi. Yeni oturum bunları kendi başına seçmemeli — sorup karar almalı.

**1. Araştırma nerede biter?** Adaylar:
- README'deki mevcut hedef: **150–200 vaka** bandına ölçütleri gevşetmeden çıkmak;
- ya da yeni vaka eklemeden **derinleşmek**: her C vakasını kuyruğa sokmak, her vakaya `source_url` kazandırmak, boş `revenue_type`/`reported_amount` alanlarını kapatmak.
İkisi çok farklı işler. Yukarıdaki tablo hangisinin ne kadar iş olduğunu gösteriyor.

**2. Wiki derinliği:** her vaka **kendi sayfasını** mı alacak (~145 sayfa), yoksa vakalar niş sayfasında kalıp oraya **derin bağlantı** mı verilecek (~21 sayfa)?

## Hedef: arayüzü Wiki'ye çevirmek

Kullanıcının tarifi, birebir:

> web arayüzünü bir Wiki haline getireceğiz, sol menüde rahatça ve sadelik içinde dolaşılabilecek, tıklanan menü elemanları kendilerinin ilgili sayfasına yönlenecek, o sayfada da çok iyi dizayn edilmiş detaylı içerikleri bulunacak.

Şu anki `docs/index.html` **tek sayfa**: arama + üç filtre + kart ızgarası. Wiki bunu sol menü + ayrı sayfalar hâline getirecek.

**En büyük teknik risk ölçüldü ve ortadan kalktı.** Wiki'nin sayfalarını doldurmak için ansiklopedi metnini HTML'e çevirmek gerekiyor. 16 niş dosyasının tamamı (95.710 bayt, 123 vaka bloğu) tarandı — kullanılan markdown **çok dar bir alt küme**:

| Var | Yok |
|---|---|
| `**kalın**` 826 · `` `kod` `` 78 · link 17 · `##` başlık 123 · `---` 139 | liste **0** · sıralı liste **0** · alıntı **0** · kod bloğu **0** · tablo **0** · görsel **0** · `###` **0** · `_italik_` **0** |

Yani **~40 satırlık bir renderer yeter; markdown kütüphanesi gerekmez.** `build_site.py`'nin saf-stdlib ve deterministik olma kuralı Wiki'de de korunabilir. Sayfa sayısı tahmini: 1 ana + 16 niş + 124 vaka + ~4 meta ≈ **145** (yukarıdaki 2. karara bağlı).

Wiki yazılırken korunacaklar: üretilen çıktının elle düzenlenmemesi, CI'nın `git diff --exit-code` ile tazelik ölçebilmesi, üç durumlu tema (açık / koyu / sistem), harfin renkten bağımsız her zaman görünmesi.

## Kullanıcıya kalan tek manuel iş

`claude/golden-cases-deep-dive-2-c1m4ov` dalı merge edilmemiş ve terk edilmiş durumda — içeriği (eski `VOLUME-*` yapısı, `data/cases.csv` öncesi dünya) tamamen bayat, kurtarılacak bir şeyi yok. **Buradan silinemiyor**: agent proxy GitHub API'sinin yazma yollarını reddediyor. GitHub arayüzünden `Branches` ekranından silinmeli.

Repo About kutusu için ayrıca bir şey yapılmasına **gerek yok** — kullanıcı tamamladı.

## Yeni oturum için ilk adımlar

1. `CLAUDE.md`'yi oku (kurallar, veri sözleşmesi, ortam kısıtları).
2. Yeşil zemini teyit et:
   ```bash
   python3 scripts/validate_catalog.py
   python3 scripts/validate_cases.py
   python3 scripts/build_site.py && git diff --exit-code docs/index.html
   ```
3. Yukarıdaki **iki açık kararı** kullanıcıya sor — araştırmanın bitiş çizgisi ve Wiki derinliği. İkisi de sonraki tüm işi belirliyor.
4. Araştırma turunu kapatan commit bu dosyayı da güncellesin.
