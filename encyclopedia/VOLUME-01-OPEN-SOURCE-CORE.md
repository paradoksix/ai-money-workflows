# Cilt 1 — Açık kaynakla izlenebilen çekirdek 30 vaka

Bu cilt **A001–A005 ve B001–B025** vakalarını içerir. A vakalarında ticari sonuç ile exact kaynak repo/workflow doğrudan bağlanmıştır. B vakalarında çalışan kaynak kod/JSON ve ticari üretici bağlamı vardır; ancak exact workflow'un ayrıca hangi fiyata satıldığı çoğu zaman bilinmez.

---

## A001 — AI Creative Director: moda kampanyası

**Ne satılmış?** Bir e-ticaret moda markası için çok sayıda kampanya görselini tutarlı kreatif yönle üretmeye yarayan AI creative-director workflow'u.

**Ticari kanıt:** Kaynak vaka kampanyayı **V: $9K campaign** olarak tanımlıyor. Bu rakam freelancerın net ücreti olarak doğrulanmıyor.

**Nasıl çalışıyor?** n8n + Gemini/Nano Banana benzeri görsel üretim zinciri; brief'i sahne/konsept/prompta dönüştürüp varyasyon üretiyor.

**Kaynak:** Reddit vaka + `sirlifehacker/Nano-Banana-Pro-Creative-Director`, pinned commit `1c82b35f...`. Root lisans bulunmadığı için kodu sahiplenmek yerine upstream referans alınmalı.

**Risk:** Marka/IP, ürünün gerçekte olmayan biçimde gösterilmesi, sentetik model kullanımı.

**Senin için uygulama önizlemesi:** Türkiye'de giyim yerine **mobilya, kozmetik, yerel gıda veya küçük e-ticaret markalarında “10 ürün → 30 reklam varyasyonu”** gibi dar bir paket araştırılabilir. Başlangıçta ücretli video modellerine girmeden görsel tarafında açık/ucuz araçlarla örnek set hazırlamak daha mantıklı; yerel PC'ni prompt/QA/metadata üretiminde kullanabilirsin.

---

## A002 — İş ilanı → hiring manager araştırması

**Ne satılmış?** Construction staffing ajansı için yeni iş ilanlarını bulup işe alım ihtiyacı olan şirketleri ve karar vericileri araştıran workflow.

**Ticari kanıt:** İlk müşteri vakası ve geliştiricinin daha sonra **birden fazla müşterinin aynı sistemi yaptırmak için kendisini tuttuğu** self-report'u var.

**Nasıl çalışıyor?** İlanları toplama → şirketi tanıma → hiring manager/decision maker araştırma → enrichment → kişiselleştirilmiş outreach notu.

**Kaynak:** Reddit + `sirlifehacker/n8n-automations`, commit `dcab491...`.

**Risk:** LinkedIn scraping, platform ToS, KVKK/GDPR ve izinsiz toplu iletişim.

**Senin için uygulama önizlemesi:** Türkiye'de LinkedIn'i agresif scrape etmek yerine **İŞKUR, şirket kariyer sayfaları, Google Maps ve açık şirket web siteleri** üzerinden “yeni eleman arayan firma radarı” biçiminde düşün. Eskişehir/Ankara'da teknik personel, kaynakçı, CNC, lojistik veya çağrı merkezi işe alımı yapan firmalara odaklı demo veri seti çıkarılabilir.

---

## A003 — B2B Lead Search Engine

**Ne satılmış?** Hedef sektör/konum kriterine göre şirket bulup puanlayan ve karar verici araştırması yapan lead search engine.

**Ticari kanıt:** Yazar B2B girişimcilerin sistemin varyantlarını ücretli yaptırdığını bildiriyor.

**Nasıl çalışıyor?** Google Maps/sosyal/web search → scraping/enrichment → AI scoring → sonuçların arayüz/form üzerinden teslimi.

**Kaynak:** `sirlifehacker/lead-gen-hacker`, commit `9ed891f...` + Reddit vaka.

**Risk:** Kişisel veri, scraping, spam, yanlış enrichment.

**Senin için uygulama önizlemesi:** En güçlü yerel uyarlama **“ihracatçı üreticiye distribütör adayı araştırma”**, “sanayi firmasına bayi listesi” veya “ajansa 100 hedef şirket araştırması”. İlk sürümde kişisel telefon/e-posta toplamaktan ziyade şirket + sektör + web sitesi + açık kurumsal iletişim + kısa araştırma notu üretmek daha güvenli.

---

## A004 — Social Story Scraper / trend intelligence

**Ne satılmış?** X/Twitter ve diğer kaynaklarda yükselen hikâyeleri toplayıp kümelendiren, araştıran ve içerik fırsatına çeviren sistem.

**Ticari kanıt:** **V: ~2,9M impression + 10+ high-ticket inbound lead**, yaklaşık `$75` run cost bildiriliyor. Bu doğrudan workflow satışı değil, içerikten ticari lead üretimi.

**Kaynak:** `sirlifehacker/social-story-scraper`, commit `69de288...` + Reddit vaka.

**Risk:** Kaynak platform scraping'i, telif, yanlış trend yorumlama.

**Senin için uygulama önizlemesi:** Genel teknoloji trendi yerine **tek sektör istihbaratı** daha satılabilir: örneğin “Türkiye'de motosiklet/yedek parça gündemi”, “otelcilik şikâyet trendleri”, “rakip e-ticaret kampanyaları”. Yerel model, özetleme ve kümelendirmeyi bilgisayarında yapabilir; web kaynak toplama tarafı ayrı tutulur.

---

## A005 — $1.800 Insurance Lawyer Lead-Gen Automation

**Ne satılmış?** Austin'deki butik sigorta/arabuluculuk hukuk firmasına avukat/firma dizinlerini tarayan, uygun firmaları araştıran ve kişiselleştirilmiş outreach hazırlayan sistem.

**Ticari kanıt:** **F: $1.800** ödenmiş proje. Satıcı normal fiyatının `$2.500 build + $400/ay` olacağını söylüyor.

**Nasıl çalışıyor?** Directory scrape → firma web sitesi bulma → uygunluk değerlendirme → araştırma → Sheets/Docs → kişiselleştirilmiş mesaj.

**Kaynak:** Reddit + `lucaswalter/n8n-ai-automations`, commit `08e33b6...`; exact `deal_breakdown_lawyer_lead_gen.json` doğrulanmış.

**Risk:** Dizin kullanım şartları, spam, kişisel veri, hukuk sektöründe yanlış temsil.

**Senin için uygulama önizlemesi:** Hukuk yerine daha düşük regülasyonlu bir dikeye taşı: **endüstriyel tedarikçi → potansiyel bayi**, **personel firması → işe alım yapan şirket**, **B2B eğitim firması → yeni büyüyen şirket**. Açık şirket verisiyle çalışan clean-room sürüm araştırmak en güvenli yol.

---

## B001 — Job Hacker: CV'yi ilana göre uyarlama

**Ne yapıyor?** İş ilanlarını buluyor, CV'deki anahtar kelime/bullet'ları ilana göre düzenlemeye yardımcı oluyor ve hiring manager araştırıyor.

**Kanıt:** Üretici AI araçları geliştirerek tam zamanlı gelir bildirmiş; bu exact workflow için ayrı ücretli müşteri kanıtı yok.

**Kaynak:** `sirlifehacker/n8n-job-hacker`, commit `edbc144...`.

**Risk:** CV'de gerçek dışı bilgi üretme, LinkedIn otomasyonu.

**Senin için uygulama önizlemesi:** B2C “CV botu” yerine **iş arayanlara yarı-manuel CV/ilan eşleştirme hizmeti** daha kolay test edilir. Yerel modelle ilan-CV fark analizi yapıp insan kontrolüyle teslim edilebilir; otomatik başvuru kısmına hiç girmemek daha güvenli.

---

## B002 — Otel yüksek-harcayan müşteri reward e-mail

**Ne satılmış?** Salesforce/CRM'deki yüksek harcayan otel müşterilerini belirleyip kişiselleştirilmiş teşekkür/ödül e-maili gönderen workflow.

**Ticari kanıt:** **F: $200**; yazar yaklaşık 40 dakikada yaptığını söylüyor. GitHub'daki kaynak author repo değil, resmi n8n template'in mirror'u.

**Risk:** CRM verisi ve yanlış kampanya koşulları.

**Senin için uygulama önizlemesi:** Türkiye'de otel/pansiyon yerine **kuaför, servis, restoran, özel ders veya küçük e-ticaret** için “son 90 günde en çok harcayan müşteriler → insan onaylı geri-kazanım listesi” olarak uyarlanabilir. İlk versiyonda otomatik mesaj göndermek yerine öneri listesi üretmek düşük riskli.

---

## B003 — Dental Practice Voice Agent

**Ne yapıyor?** Diş kliniğinde telefondan gelen talepleri karşılayıp müsaitlik kontrolü, randevu ve Sheets log işlemleri yapıyor.

**Kanıt:** Çalışan JSON açık; exact müşteri/ücret bilinmiyor.

**Stack:** n8n + voice provider + Calendar + Sheets.

**Risk:** Sağlık verisi, yanlış randevu, çağrı kaydı/rıza.

**Senin için uygulama önizlemesi:** Sağlıkla başlamaktansa aynı sistemi **oto servis, kuaför, pet kuaförü, teknik servis veya restoran rezervasyonu** gibi daha düşük regülasyonlu alanlarda araştır. Voice maliyetli olduğu için önce WhatsApp/form tabanlı prototip daha ekonomik.

---

## B004 — Hotel WhatsApp Guest Assistant

**Ne yapıyor?** Misafirlerin sık sorularını yanıtlayıp otel bilgisi/öneri sunan WhatsApp agent.

**Kanıt:** Açık workflow var; exact ücret yok.

**Risk:** Meta policy, yanlış tesis bilgisi, kişisel veriler.

**Senin için uygulama önizlemesi:** Türkiye turizminde güçlü aday. Küçük oteller için ilk aşamada **check-in saati, kahvaltı, Wi-Fi, otopark, konum, transfer, oda kuralları** gibi yalnızca doğrulanmış bilgi tabanından cevap veren agent araştırılabilir. Sipariş/ödeme gibi aksiyonları sonraya bırak.

---

## B005 — AI Gmail Agent

**Ne yapıyor?** Gelen e-postayı sınıflandırıyor, önceliklendiriyor ve taslak yanıt oluşturuyor.

**Kanıt:** Açık JSON workflow; exact ücret yok.

**Risk:** Yanlış otomatik gönderim, gizli e-posta içeriği.

**Senin için uygulama önizlemesi:** En iyi yerel kullanım **“gelen maili cevaplamak” değil, “gelen maili klasörle + kısa özet + cevap taslağı hazırla”**. İnsan gönderim onayı korunursa düşük maliyetli ve birçok KOBİ'ye uygulanabilir.

---

## B006 — Auto Repair Shop Gmail Agent

**Ne yapıyor?** Oto servise gelen quote talebinde marka/model/araç bilgileri eksikse takip sorusu soruyor; yeterliyse ilgili kişiye SMS/iş akışı başlatıyor.

**Kanıt:** Exact workflow açık; ücret yok.

**Risk:** Yanlış sınıflandırma ve müşteriye yanlış fiyat/vaat.

**Senin için uygulama önizlemesi:** Türkiye için çok güçlü. İlk pilot **“WhatsApp/e-mail talebi → plaka/marka/model/şikâyet bilgisini tamamla → servis danışmanına temiz fiş bırak”** olmalı. Fiyatı AI vermesin; yalnız veri toplasın.

---

## B007 — Eski web sitesinden yeniden tasarım brief'i

**Ne yapıyor?** Mevcut siteyi scrape edip içerik/yapı analizi yapıyor ve AI site-builder için PRD/yeniden tasarım brief'i çıkarıyor.

**Stack:** n8n + Firecrawl + LLM + site builder.

**Risk:** Site içeriği/IP ve hatalı ihtiyaç çıkarımı.

**Senin için uygulama önizlemesi:** Yerel işletmelere “web sitesi yaparım” yerine **“mevcut sitenizin eksiklerini, içerik haritasını ve yeni site brief'ini 1 günde çıkarırım”** şeklinde düşük ticket danışmanlık ürünü olarak incelenebilir.

---

## B008 — Meta Ads competitor audit → sales deck

**Ne yapıyor?** Rakip reklamları topluyor, kreatif analizi yapıyor ve Gamma benzeri araçla satış/audit sunumu üretiyor.

**Stack:** Apify/Firecrawl/Gemini/Gamma/n8n.

**Risk:** Rakip kreatif telifi, yanlış performans yorumu.

**Senin için uygulama önizlemesi:** Reklam ajanslarına **“5 rakibin son reklamları → hook/format/teklif matrisi”** araştırma hizmeti. Reklamı kopyalamak yerine örüntü çıkar. Yerel LLM ile sınıflandırma/özet kısmı ucuza yapılabilir.

---

## B009 — YouTube → X + LinkedIn repurposing

**Ne yapıyor?** Uzun videodan thread ve profesyonel sosyal medya postları çıkarıyor.

**Kanıt:** Çalışan JSON açık.

**Risk:** Kaynak içeriğin hakkı ve marka dili.

**Senin için uygulama önizlemesi:** Türkiye'de eğitmen, podcast, danışman, emlakçı veya doktor içerik üreticilerine **“1 uzun video → 6 kısa post + 2 LinkedIn yazısı”** şeklinde manuel+AI hizmet olarak test edilebilir. Video düzenleme deneyimin bu kategoriyi daha erişilebilir kılar.

---

## B010 — Uzun videodan Shorts/Reels adayları

**Ne yapıyor?** Uzun videoyu analiz edip kısa klip olabilecek bölümleri seçiyor ve üretim hattına aktarıyor.

**Stack:** n8n + Vizard/clip tool + Slack vb.

**Risk:** Telif, yanlış segment seçimi, düşük kalite.

**Senin için uygulama önizlemesi:** Tam otomatik video üretmek yerine **“AI klip adaylarını bulur, sen final kesim/altyazı/tempo kontrolü yaparsın”** yaklaşımı daha savunulabilir. Yerel Whisper kullanarak transkripsiyon maliyetini düşürebilirsin.

---

## B011 — Yerel haber/etkinliklerden otomatik podcast bülteni

**Ne yapıyor?** RSS/web kaynaklarını toplayıp kısa yerel podcast bülteni hazırlıyor.

**Stack:** Firecrawl + ElevenLabs + n8n.

**Risk:** Haber doğruluğu ve kaynak telifi.

**Senin için uygulama önizlemesi:** Genel haber yerine **“haftalık Eskişehir etkinlik özeti”, “sanayi sektörü bülteni”, “turizm işletmeleri için etkinlik radar”** gibi dar dikeyler. Ses üretimini ilk aşamada zorunlu tutmadan metin bülteniyle test etmek ucuz.

---

## B012 — AI Newsletter Generator

**Ne yapıyor?** Kaynakları toplar, özetler ve düzenli newsletter taslağı üretir.

**Kanıt:** Açık JSON.

**Risk:** Kaynak doğruluğu, tekrar içerik.

**Senin için uygulama önizlemesi:** Kendi medya markanı kurmaktan önce **B2B firmaya sektör bülteni üretim hizmeti** daha hızlı doğrulanabilir. Örneğin “haftalık otomotiv yedek parça/ihracat/regülasyon özeti”.

---

## B013 — News/Reddit/HN ingestion + relevancy scoring

**Ne yapıyor?** Çok sayıda kaynaktan içerik alıp müşterinin ilgi alanına göre puanlıyor.

**Risk:** Scraping/telif ve yanlış önem skoru.

**Senin için uygulama önizlemesi:** Bu tek başına satılan ürün değil, **rekabet istihbaratı, sektör bülteni veya satış research servisinin arka motoru** olarak daha anlamlı. Yerel LLM puanlaması maliyeti düşürür.

---

## B014 — Reklamdan 10 kontrollü A/B varyasyonu

**Ne yapıyor?** Mevcut başarılı kreatifi temel alıp kontrollü görsel/metin varyasyonları oluşturuyor.

**Kanıt:** Açık workflow; ücret yok.

**Risk:** Marka/IP, yalnız görsel değiştirip “test” diye satma.

**Senin için uygulama önizlemesi:** “AI görsel” yerine **“1 mevcut reklam → 10 hipotezli test varyasyonu + hangi unsur değişti tablosu”** satılabilir. Böylece çıktı ölçülebilir ve ajans müşterisi için daha profesyonel olur.

---

## B015 — E-commerce AI UGC video varyantları

**Ne yapıyor?** Ürün görsellerinden UGC tarzı video senaryoları/varyantları üretiyor.

**Stack:** Sora/Gemini/vision/n8n.

**Risk:** Sahte testimonial, marka güveni, video maliyeti.

**Senin için uygulama önizlemesi:** Başlangıçta gerçek kullanıcı yorumu taklit etmek yerine **ürün demonstrasyonu, problem/çözüm, katalog video** türüne odaklan. Video API maliyeti nedeniyle bu kategori yerel PC'nde metin/storyboard/QA, bulutta yalnız final üretim şeklinde düşünülmeli.

---

## B016 — Ürün fotoğrafını kısa videoya çevirme

**Ne yapıyor?** E-ticaret katalog görsellerini kısa hareketli ürün videolarına dönüştürüyor.

**Stack:** Firecrawl/Veo/Drive/n8n.

**Risk:** Ürünün fiziksel özelliklerini yanlış göstermek.

**Senin için uygulama önizlemesi:** Türkiye'de pazaryeri satıcılarına **“20 SKU → 20 kısa dikey ürün klibi”** şeklinde paketlenebilir. Önce birkaç üründe gerçek ürüne sadakat testi yapılmalı.

---

## B017 — Website business e-mail extraction

**Ne yapıyor?** Bir şirket sitesindeki sayfaları tarayıp açık kurumsal e-posta adreslerini topluyor.

**Kanıt:** Açık JSON.

**Risk:** Spam/KVKK ve site ToS.

**Senin için uygulama önizlemesi:** Bunu doğrudan “e-mail scraper” diye satmak yerine **“hedef şirket araştırması + açık kurumsal iletişim kanalı + kaynak URL”** teslimatı olarak sınırla. Kişisel e-posta tahmini yapma.

---

## B018 — Enterprise AI Sales Agent / lead scoring

**Ne yapıyor?** Inbound lead'i çok alanlı skorlayıp Calendar/e-mail/Slack aksiyonuna yönlendiriyor.

**Kaynak:** Nextwave portfolio, runnable workflow.

**Risk:** Yanlış lead skoru ve fırsat kaçırma.

**Senin için uygulama önizlemesi:** Küçük işletmede 15 alanlı karmaşık skor yerine **3 kriter: hizmet türü, bütçe aralığı, aciliyet** ile başlamak daha mantıklı. AI skoru satışçıya öneri sunsun, otomatik reddetmesin.

---

## B019 — CRM AI enrichment

**Ne yapıyor?** CRM lead'lerini sektör, değer, buying signal vb. alanlarla zenginleştiriyor.

**Risk:** Uydurma enrichment.

**Senin için uygulama önizlemesi:** Yalnızca **kaynağı gösterilebilir bilgiler** ekleyen sürüm araştır: şirket web sitesinden faaliyet alanı, lokasyon, ürün grubu ve açık haber sinyali. Her alanın yanında source URL tut.

---

## B020 — Google Sheets mini-CRM enrichment

**Ne yapıyor?** Pahalı CRM olmadan Sheets'i lead tablosu + AI enrichment arayüzü gibi kullanıyor.

**Senin için uygulama önizlemesi:** Türkiye'deki küçük ekipler için çok uygun. **Google Sheets + n8n + yerel/ucuz LLM** ile “mevcut Excel listenizi temizleyip zenginleştiren mini CRM” yaklaşımı düşük başlangıç maliyetli.

---

## B021 — Support ticket classifier

**Ne yapıyor?** Gelen destek taleplerini intent/priority kategorilerine ayırıyor.

**Risk:** Acil talebin yanlış düşük önceliğe düşmesi.

**Senin için uygulama önizlemesi:** İlk sürüm yalnız **etiketlesin ve özetlesin**, otomatik kapatmasın. Teknik servis, e-ticaret, site yönetimi veya küçük SaaS'ta uygulanabilir.

---

## B022 — Şirket içi RAG knowledge agent

**Ne yapıyor?** Şirket dokümanlarından kaynaklı cevap üretip gerektiğinde Calendar/Slack aksiyonu başlatıyor.

**Risk:** Gizli belge, prompt injection, yanlış kaynak.

**Senin için uygulama önizlemesi:** RTX 3060 12 GB sayesinde küçük bir yerel model + embeddings ile **private RAG demo** araştırabilirsin. İlk hedef sağlık/finans değil; teknik ürün dokümanı, şirket prosedürü veya eğitim materyali daha güvenli.

---

## B023 — WhatsApp Business RAG Agent

**Ne yapıyor?** WhatsApp mesajını bilgi tabanıyla yanıtlıyor ve konuşmayı logluyor.

**Risk:** Meta policy, KVKK, yanlış cevap.

**Senin için uygulama önizlemesi:** Türkiye için güçlü fakat ilk ürün “serbest konuşan agent” değil, **5–10 doğrulanmış FAQ + insan devri + kayıt** olmalı. Satın alma/ödeme gibi kritik aksiyonlar insan onayında kalmalı.

---

## B024 — GoHighLevel lead qualifier

**Ne yapıyor?** Form lead'ini AI ile qualify/tag/follow-up ediyor.

**Risk:** CRM erişimi ve spam.

**Senin için uygulama önizlemesi:** GoHighLevel Türkiye'de şart değil; aynı deseni **Tally/Google Form → Sheets → n8n → satışçı bildirimi** ile daha düşük maliyetle test etmek mümkün.

---

## B025 — Appointment Scheduling Assistant

**Ne yapıyor?** Randevu talebini aciliyet, süre, uygun slot ve mesaj haline getiriyor.

**Risk:** Özellikle sağlık sektöründe yanlış aciliyet yorumu.

**Senin için uygulama önizlemesi:** Kuaför, teknik servis, danışmanlık, özel ders gibi alanlarda **“talebi yapılandır + uygun slot öner + insan onayıyla gönder”** biçiminde uygulanabilir. Takvim entegrasyonu basit ve ölçülebilir olduğu için iyi araştırma adayı.

---

## Cilt 1'den çıkan ortak desen

Açık kaynakla en iyi izlenebilen işler “süper akıllı agent”lardan çok şu zincirde yoğunlaşıyor:

**veriyi bul → temizle → sınıflandır → doğru kişiye/aksiyona taşı → insan kontrolü bırak.**

Bu desen düşük maliyetli araçlarla ve küçük pilotlarla öğrenilmeye en uygun alanlardan biridir.
