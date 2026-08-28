# AI Gelir Vakaları Ansiklopedisi

Bu ansiklopedi, insanların ve işletmelerin yapay zekâ/otomasyon kullanarak hangi küçük problemlere **gerçekten para ödediğini** izler.

Amaç “AI ile para kazanmanın 122 yolu” demek değildir. Amaç, gerçek bir insanın veya işletmenin para ödediği ya da ölçülebilir ekonomik değer bildirdiği **122 küçük problemi** ne kadar güvenilir olduğu işaretlenmiş hâlde arşivlemek; güvenilirlik sorunu olanları da ayrı bir ek altında kaybetmemektir.

## Nereden başlamalı?

| Ne istiyorsun | Nereye git |
|---|---|
| Gezinmek, filtrelemek, bir iş kolu seçmek | **[Wiki](https://paradoksix.github.io/ai-money-workflows/)** — sol menüden gezilen sayfalar; [bütün örnekler](https://paradoksix.github.io/ai-money-workflows/tum-vakalar.html) sayfasında arama + iş kolu, güvenilirlik ve gelir türü filtreleri |
| Bir iş kolunu derinlemesine okumak | Aşağıdaki **iş kolları listesi** |
| Örnek gruplarından çıkan ortak dersler | [`encyclopedia/DESENLER.md`](encyclopedia/DESENLER.md) |
| Neyin nasıl doğrulandığını anlamak | [`RESEARCH_POLICY.md`](RESEARCH_POLICY.md) |
| Veriyi kendin analiz etmek | [`data/cases.csv`](data/cases.csv) — 124 kaydın tamamı |
| Kaynağı hâlâ aranan örnekler | [`research_queue.csv`](research_queue.csv) + [`research/`](research/) |

## Yanlarındaki harf ne demek?

- **A — Müşteri kanıtı + kodu açık.** İşin gerçek bir müşteriye satıldığı ve tam olarak hangi kodla yapıldığı, ikisi birden doğrulandı.
- **B — Kodu açık, kazancı belirsiz.** Kod gerçek ve çalışıyor; ama tam olarak bu işin para kazandırdığı ayrıca gösterilmedi.
- **C — Para kazandırmış, kodu yok.** Ödeme yapan müşteri, gelir ya da tasarruf anlatımı güçlü; ama işin kodu paylaşılmamış veya bulunamadı.
- **X — Şüpheli.** Kazanç iddiasında gizli reklam ya da çıkar çatışması şüphesi var; ana 122 sayımına katılmıyor.

Rakamlarda birbirine benzeyen ama aynı olmayan dört şey ayrı tutulur:

- **F:** işi yapana ödenen ücret
- **R:** satılan üründen veya abonelikten gelen gelir
- **S:** müşterinin kazandığı tasarruf
- **V:** kampanya değeri, alınan randevu, görüntülenme, tahsil edilen alacak gibi başka ticari sonuçlar

Bu rakamların neredeyse tamamı işi yapan kişilerin kendi beyanıdır; bağımsız denetlenmiş gerçekler gibi sunulmaz.

## İş kolları

Örnekler, satılan işin türüne göre 16 gruba ayrıldı. Her dosyada o grubun tanımı, Türkiye'de kimin satın aldığı, örneklerin tam anlatımı ve gruptan çıkan ortak ders var.

| # | İş kolu | Örnek | Güvenilirlik |
|---|---|---|---|
| 1 | [Video ve görsel üretimi](encyclopedia/nis-01-video-gorsel-produksiyon.md) | 20 | A1 · B4 · C15 |
| 2 | [Şirketlere satış: müşteri adayı bulma](encyclopedia/nis-02-b2b-satis-lead.md) | 12 | **A3** · B6 · C3 |
| 3 | [Müşteri iletişimi ve destek](encyclopedia/nis-03-musteri-iletisim-destek.md) | 12 | B6 · C6 |
| 4 | [Sipariş üzerine yazılım ve küçük ürünler](encyclopedia/nis-04-ozel-yazilim-mikro-saas.md) | 14 | C14 |
| 5 | [İçerik, sosyal medya ve bülten](encyclopedia/nis-05-icerik-sosyal-medya.md) | 11 | A1 · B5 · C5 |
| 6 | [E-ticaret ve ürün kataloğu](encyclopedia/nis-06-eticaret-katalog.md) | 7 | C7 |
| 7 | [Büyük şirketlerde maliyet düşürme](encyclopedia/nis-07-kurumsal-operasyon-maliyet.md) | 6 | C6 |
| 8 | [Ofis ve evrak işleri](encyclopedia/nis-08-ofis-belge-operasyonu.md) | 7 | B1 · C6 |
| 9 | [Yapay zekâ çıktısını temize çekme](encyclopedia/nis-09-veri-cikti-temizligi.md) | 6 | C6 |
| 10 | [Nasıl satılıyor: fiyat, kapsam, süreklilik](encyclopedia/nis-10-ajans-freelance-model.md) | 6 | C6 |
| 11 | [Mahalle esnafı ve saha servisi](encyclopedia/nis-11-yerel-isletme-saha-servisi.md) | 5 | **A1** · B1 · C3 |
| 12 | [Kendi belgelerinden cevap veren sistemler](encyclopedia/nis-12-rag-bilgi-sistemleri.md) | 5 | B1 · C4 |
| 13 | [Emlak ve site yönetimi](encyclopedia/nis-13-emlak-site-yonetimi.md) | 4 | C4 |
| 14 | [Muhasebe ve fatura işleri](encyclopedia/nis-14-muhasebe-finans-belge.md) | 3 | C3 |
| 15 | [İnsan kaynakları ve işe alım](encyclopedia/nis-15-ik-ise-alim.md) | 3 | B1 · C2 |
| 16 | [Kurs ve eğitim işletmeciliği](encyclopedia/nis-16-egitim-kurs-operasyonu.md) | 2 | C2 |

Ayrıca:

- [**A006 — Jacobo Device Repair**](encyclopedia/A006-JACOBO-DEVICE-REPAIR.md) — arşivin en sağlam tek örneği, kendi ayrıntılı kartıyla.
- [**Ek X — Şüpheli iddialar**](encyclopedia/APPENDIX-X-DISPUTED.md) — güvenilirlik ölçütlerini geçemeyen ama iz olarak saklanan örnekler.

## Sana göre uygulama önizlemeleri

Her örneğin sonunda kısa bir **“Senin için uygulama önizlemesi”** bölümü bulunur. Bu önizleme şu çalışma profilini esas alır:

- Türkiye'den satış veya hizmet verme,
- mümkün olduğunca düşük maliyetli/açık kaynak araç kullanma,
- n8n/Sheets/yerel LLM gibi basit ve değiştirilebilir bileşenleri tercih etme,
- mevcut RTX 3060 12 GB sınıfı bilgisayarda küçük yerel modellerden yararlanabilme,
- “AI uzmanlığı” satmak yerine ölçülebilir bir işletme problemini satma,
- önce dar kapsamlı demo/pilot, sonra gerekiyorsa aylık bakım anlaşmasına geçme.

Bu önizlemeler uygulama garantisi veya gelir tahmini değildir; hangi yönden araştırılabileceğini gösteren kısa yönlendirmelerdir.

## Altın vakalar derin araştırması

👉 [2026-08-26 İkinci Tur Raporu](research/GOLDEN-CASES-DEEP-DIVE-2026-08-26.md) · [2026-08-24 İlk Tur Raporu](research/GOLDEN-CASES-DEEP-DIVE-2026-08-24.md)

İlk turda:

- **C027 → A006:** canlı ortamdaki kaynak kodu bulundu; artık kendi A006 kaydına sahip.
- **C004 Powerprozesse:** 20→23 müşteri ve somut iş akışı örnekleriyle ticari kanıt güçlendi; şirketin resmî kaynak kodu bulunamadı.
- **C008 Bookstore WhatsApp:** `$500` birincil Reddit vakası korunuyor; aynı hikâyenin başka bir hesapta `$1,500` olarak kopyalanması kaynak kirliliği olarak kaydedildi.
- **C018 Tutoring:** `$5K` iddiası ikincil arşivce destekleniyor fakat birincil kaynak yeniden doğrulanmalı.
- **C029 Offline University RAG:** teknik kurgu ilginç; herkese açık kaynak kodu yok, seller/promo bağlamı nedeniyle temkinli.

İkinci turda 9 açık ipucu (C001–C008, C018) yeniden kovalandı. Hiçbiri A/B'ye yükselmedi; en güçlü yeni sinyal C003 için `conor-is-my-name` GitHub hesabı (teknik olarak uyumlu, yazar eşleşmesi doğrulanmamış), C008 için ise `anassy1` hesabının boş çıkması oldu. O turda ortamın Reddit'e doğrudan erişimi yoktu.

## Özellikle araştırılmaya devam edilecek altın vakalar

1. C004 — Property-management vertical / Powerprozesse
2. C003 — 50K ürün katalog overhaul (`conor-is-my-name` doğrulanmamış aday)
3. C002 — Japon Google Ads invoice processor
4. C006 — 115+ iş akışını izleyen panel / AigencyTracker
5. C005 — Bookkeeping process automation
6. C001 — Ship manager lead capture
7. C007 — 50K Shopify inventory shock absorber
8. C008 — Bookstore WhatsApp order assistant
9. C018 — $5K tutoring operations system
10. C029 — Offline university RAG
11. C076 — Medical-device expiry/spoilage automation

## Ana araştırma ilkesi

> Çok spesifik müşteri + çok spesifik tekrar eden problem + AI yalnız gerektiği yerde + ölçülebilir çıktı.
