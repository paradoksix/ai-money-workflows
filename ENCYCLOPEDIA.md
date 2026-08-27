# AI Gelir Vakaları Ansiklopedisi

Bu ansiklopedi, insanların ve işletmelerin yapay zekâ/otomasyon kullanarak hangi küçük problemlere **gerçekten para ödediğini** izler.

Amaç “AI ile para kazanmanın 122 yolu” demek değildir. Amaç, gerçek bir insanın veya işletmenin para ödediği ya da ölçülebilir ekonomik değer bildirdiği **122 küçük problemi** kanıt derecesiyle birlikte arşivlemek; güvenilirlik sorunu olanları da ayrı bir ek altında kaybetmemektir.

## Nereden başlamalı?

| Ne istiyorsun | Nereye git |
|---|---|
| Gezinmek, filtrelemek, bir niş seçmek | **[Atlas web sayfası](docs/index.html)** — arama + niş/kanıt/gelir tipi filtreleri |
| Bir nişi derinlemesine okumak | Aşağıdaki **niş indeksi** |
| Vaka gruplarından çıkan kesişen dersler | [`encyclopedia/DESENLER.md`](encyclopedia/DESENLER.md) |
| Kanıt standardını anlamak | [`RESEARCH_POLICY.md`](RESEARCH_POLICY.md) |
| Veriyi kendin analiz etmek | [`data/cases.csv`](data/cases.csv) — 124 kaydın tamamı |
| Hâlâ kaynağı aranan vakalar | [`research_queue.csv`](research_queue.csv) + [`research/`](research/) |

## Kanıt sistemi

- **A — Ticari vaka + exact kaynak repo/workflow.** Aynı müşteri/gelir/operasyon vakası ile doğrudan bağlantılı kaynak kod doğrulanmıştır.
- **B — Açık çalışan workflow/repo + ticari üretici bağlamı.** Kod gerçektir fakat o exact workflow'un ayrı ücretli müşteri sonucu kanıtlanmamıştır.
- **C — Güçlü ücretli müşteri, gelir, tasarruf veya marketplace sinyali.** Exact kaynak repo kapalıdır, bulunamamıştır veya doğrulanmamıştır.
- **X — Tartışmalı.** Gelir iddiasında promosyon, çıkar çatışması veya başka ciddi güvenilirlik problemi vardır; ana 122 sayımına dahil edilmez.

Gelir rakamlarında şu ayrım korunur ve birbirine karıştırılmaz:

- **F:** freelancer/hizmet sağlayıcının aldığı ücret
- **R:** ürün/SaaS/app geliri
- **S:** müşterinin bildirilen tasarrufu
- **V:** kampanya değeri, booked call, impression, geri kazanılan alacak gibi ticari sonuç

Self-report rakamları bağımsız denetlenmiş gerçekler gibi sunulmaz.

## Niş indeksi

Vakalar 16 nişe ayrılmıştır. Her dosyada o nişin tanımı, Türkiye'de kimin satın aldığı, vakaların tam anlatımı ve nişin ortak deseni bulunur.

| # | Niş | Vaka | Kanıt dağılımı |
|---|---|---|---|
| 1 | [Video & görsel prodüksiyon](encyclopedia/nis-01-video-gorsel-produksiyon.md) | 20 | A1 · B4 · C15 |
| 2 | [B2B satış & lead araştırma](encyclopedia/nis-02-b2b-satis-lead.md) | 12 | **A3** · B6 · C3 |
| 3 | [Müşteri iletişimi & destek](encyclopedia/nis-03-musteri-iletisim-destek.md) | 12 | B6 · C6 |
| 4 | [Özel yazılım & mikro-SaaS](encyclopedia/nis-04-ozel-yazilim-mikro-saas.md) | 14 | C14 |
| 5 | [İçerik, sosyal medya & bülten](encyclopedia/nis-05-icerik-sosyal-medya.md) | 11 | A1 · B5 · C5 |
| 6 | [E-ticaret & katalog](encyclopedia/nis-06-eticaret-katalog.md) | 7 | C7 |
| 7 | [Kurumsal operasyon & maliyet](encyclopedia/nis-07-kurumsal-operasyon-maliyet.md) | 6 | C6 |
| 8 | [Ofis & belge operasyonu](encyclopedia/nis-08-ofis-belge-operasyonu.md) | 7 | B1 · C6 |
| 9 | [Veri & AI-çıktısı temizliği](encyclopedia/nis-09-veri-cikti-temizligi.md) | 6 | C6 |
| 10 | [Ajans & freelance hizmet modeli](encyclopedia/nis-10-ajans-freelance-model.md) | 6 | C6 |
| 11 | [Yerel işletme & saha servisi](encyclopedia/nis-11-yerel-isletme-saha-servisi.md) | 5 | **A1** · B1 · C3 |
| 12 | [RAG & özel bilgi sistemleri](encyclopedia/nis-12-rag-bilgi-sistemleri.md) | 5 | B1 · C4 |
| 13 | [Emlak & site yönetimi](encyclopedia/nis-13-emlak-site-yonetimi.md) | 4 | C4 |
| 14 | [Muhasebe & finans belgeleri](encyclopedia/nis-14-muhasebe-finans-belge.md) | 3 | C3 |
| 15 | [İK & işe alım](encyclopedia/nis-15-ik-ise-alim.md) | 3 | B1 · C2 |
| 16 | [Eğitim & kurs operasyonu](encyclopedia/nis-16-egitim-kurs-operasyonu.md) | 2 | C2 |

Ayrıca:

- [**A006 — Jacobo Device Repair**](encyclopedia/A006-JACOBO-DEVICE-REPAIR.md) — ansiklopedinin en güçlü tek vakası, kendi ayrıntılı kartıyla.
- [**Ek X — Tartışmalı vakalar**](encyclopedia/APPENDIX-X-DISPUTED.md) — ana kanıt standardını geçmeyen fakat araştırma izi olarak korunan örnekler.

## Sana göre uygulama önizlemeleri

Her vakanın sonunda kısa bir **“Senin için uygulama önizlemesi”** bölümü bulunur. Bu önizleme şu çalışma profilini esas alır:

- Türkiye'den satış veya hizmet verme,
- mümkün olduğunca düşük maliyetli/açık kaynak araç kullanma,
- n8n/Sheets/yerel LLM gibi basit ve değiştirilebilir bileşenleri tercih etme,
- mevcut RTX 3060 12 GB sınıfı bilgisayarda küçük yerel modellerden yararlanabilme,
- “AI uzmanlığı” satmak yerine ölçülebilir bir işletme problemini satma,
- önce dar kapsamlı demo/pilot, sonra gerekiyorsa aylık bakım/retainer modeline geçme.

Bu önizlemeler uygulama garantisi veya gelir tahmini değildir; hangi yönden araştırılabileceğini gösteren kısa yönlendirmelerdir.

## Altın vakalar derin araştırması

👉 [2026-08-26 İkinci Tur Raporu](research/GOLDEN-CASES-DEEP-DIVE-2026-08-26.md) · [2026-08-24 İlk Tur Raporu](research/GOLDEN-CASES-DEEP-DIVE-2026-08-24.md)

İlk turda:

- **C027 → A006:** exact production repo bulundu; artık kendi A006 kaydına sahip.
- **C004 Powerprozesse:** 20→23 müşteri ve somut workflow örnekleriyle ticari kanıt güçlendi; resmi exact repo bulunmadı.
- **C008 Bookstore WhatsApp:** `$500` birincil Reddit vakası korunuyor; aynı hikâyenin başka bir hesapta `$1,500` olarak kopyalanması kaynak kirliliği olarak kaydedildi.
- **C018 Tutoring:** `$5K` iddiası ikincil arşivce destekleniyor fakat birincil kaynak yeniden doğrulanmalı.
- **C029 Offline University RAG:** teknik mimari ilginç; public exact code yok, seller/promo bağlamı nedeniyle temkinli.

İkinci turda 9 açık ipucu (C001–C008, C018) yeniden kovalandı. Hiçbiri A/B'ye yükselmedi; en güçlü yeni sinyal C003 için `conor-is-my-name` GitHub hesabı (teknik olarak uyumlu, yazar eşleşmesi doğrulanmamış), C008 için ise `anassy1` hesabının boş çıkması oldu. O turda ortamın Reddit'e doğrudan erişimi yoktu.

## Özellikle araştırılmaya devam edilecek altın vakalar

1. C004 — Property-management vertical / Powerprozesse
2. C003 — 50K ürün katalog overhaul (`conor-is-my-name` doğrulanmamış aday)
3. C002 — Japon Google Ads invoice processor
4. C006 — 115+ workflow monitoring / AigencyTracker
5. C005 — Bookkeeping process automation
6. C001 — Ship manager lead capture
7. C007 — 50K Shopify inventory shock absorber
8. C008 — Bookstore WhatsApp order assistant
9. C018 — $5K tutoring operations system
10. C029 — Offline university RAG
11. C076 — Medical-device expiry/spoilage automation

## Ana araştırma ilkesi

> Çok spesifik müşteri + çok spesifik tekrar eden problem + AI yalnız gerektiği yerde + ölçülebilir çıktı.
