# Şirketlere satış: müşteri adayı bulma

Hedef şirketi bul, kararı veren kişiyi çıkar, herkese açık bilgiyle zenginleştir ve satışçıya temiz bir not bırak. Arşivin **kaynak koduyla en iyi doğrulanmış** grubu: üç A örneği burada. Ortak hassas nokta kişisel veri, platform kuralları ve izinsiz toplu mesaj — bu işi kör bir spam makinesine çevirmemek grubun tek gerçek savunması.

**Türkiye'de kim satın alır?** Sanayi tedarikçisi, ihracatçı, personel ajansı, makine üreticisi, B2B ajans

**Bu grupta 12 örnek var.** Ne kadar güvenilir oldukları — A: 3 · B: 6 · C: 3.

Harflerin ne anlama geldiği için `../RESEARCH_POLICY.md`, gruplar arası ortak dersler için `DESENLER.md`, hepsini birden filtrelemek için [atlas sayfası](https://paradoksix.github.io/ai-money-workflows/).

---

## A002 — İş ilanı → hiring manager araştırması

**Ne satılmış?** Construction staffing ajansı için yeni iş ilanlarını bulup işe alım ihtiyacı olan şirketleri ve karar vericileri araştıran workflow.

**Ticari kanıt:** İlk müşteri vakası ve geliştiricinin daha sonra **birden fazla müşterinin aynı sistemi yaptırmak için kendisini tuttuğu** kendi beyanı var.

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

## A005 — $1.800 Insurance Lawyer Lead-Gen Automation

**Ne satılmış?** Austin'deki butik sigorta/arabuluculuk hukuk firmasına avukat/firma dizinlerini tarayan, uygun firmaları araştıran ve kişiselleştirilmiş outreach hazırlayan sistem.

**Ticari kanıt:** **F: $1.800** ödenmiş proje. Satıcı normal fiyatının `$2.500 build + $400/ay` olacağını söylüyor.

**Nasıl çalışıyor?** Directory scrape → firma web sitesi bulma → uygunluk değerlendirme → araştırma → Sheets/Docs → kişiselleştirilmiş mesaj.

**Kaynak:** Reddit + `lucaswalter/n8n-ai-automations`, commit `08e33b6...`; birebir `deal_breakdown_lawyer_lead_gen.json` dosyası doğrulanmış.

**Risk:** Dizin kullanım şartları, spam, kişisel veri, hukuk sektöründe yanlış temsil.

**Senin için uygulama önizlemesi:** Hukuk yerine daha düşük regülasyonlu bir dikeye taşı: **endüstriyel tedarikçi → potansiyel bayi**, **personel firması → işe alım yapan şirket**, **B2B eğitim firması → yeni büyüyen şirket**. Açık şirket verisiyle çalışan clean-room sürüm araştırmak en güvenli yol.

---

## B008 — Meta Ads competitor audit → sales deck

**Ne yapıyor?** Rakip reklamları topluyor, kreatif analizi yapıyor ve Gamma benzeri araçla satış/audit sunumu üretiyor.

**Stack:** Apify/Firecrawl/Gemini/Gamma/n8n.

**Risk:** Rakip kreatif telifi, yanlış performans yorumu.

**Senin için uygulama önizlemesi:** Reklam ajanslarına **“5 rakibin son reklamları → hook/format/teklif matrisi”** araştırma hizmeti. Reklamı kopyalamak yerine örüntü çıkar. Yerel LLM ile sınıflandırma/özet kısmı ucuza yapılabilir.

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

## B024 — GoHighLevel lead qualifier

**Ne yapıyor?** Form lead'ini AI ile qualify/tag/follow-up ediyor.

**Risk:** CRM erişimi ve spam.

**Senin için uygulama önizlemesi:** GoHighLevel Türkiye'de şart değil; aynı deseni **Tally/Google Form → Sheets → n8n → satışçı bildirimi** ile daha düşük maliyetle test etmek mümkün.

---

## C001 — Ship Manager Lead Capture

**Ne satılmış?** IMO numarasından gemi/ship manager bilgisi bulup şirket, domain ve iletişim enrichment'i yapan denizcilik lead araştırma sistemi.

**Müşteri problemi:** Denizcilikte doğru ship-management şirketini ve karar vericiyi elle bulmak çok zaman alıyor.

**Ticari kanıt:** Geliştirici bunun **ilk ücretli müşterisi** olduğunu bildiriyor.

**Stack:** Puppeteer + Equasis/WSD + Apify + n8n + AI enrichment.

**Risk:** Veri kaynaklarının kullanım şartları, scraping, güncel olmayan denizcilik verisi.

**Senin için uygulama önizlemesi:** Denizcilik Türkiye'de niş ama ihracatçı sanayi açısından desen çok değerli. Aynısını **“ürün kodu → üretici/distribütör → ülke → açık iletişim”** araştırmasına çevir. Örneğin Eskişehir'deki makine/metal üreticilerine belirli ülkelerde distribütör adayı listesi hazırlamak, aynı mantığın daha erişilebilir versiyonu.

---

## C014 — Daily Lead Finder + Personalized Outreach

**Ne yapılmış?** Her gün yeni lead bulup GPT ile kişiselleştirilmiş outreach hazırlayan sistem.

**Ticari sonuç:** **V: 40+ booked sales call/ay, 8 ay** kendi beyanı.

**Stack:** n8n + GPT + Google Sheets.

**Risk:** Attribution belirsizliği, spam, platform/ileti mevzuatı.

**Senin için uygulama önizlemesi:** Otomatik mesaj yollamayı değil **“haftalık 30 nitelikli şirket + neden uygun oldukları + kaynak link”** hizmetini araştır. Satış temsilcisi iletişimi kendisi yapsın; hukuki risk azalır.

---

## C083 — B2B Manufacturing Tender Research Agent

**Ne yapılmış?** Üretici firma için tender/ihale araştırmasını bulma → temizleme → filtreleme → qualification zinciriyle otomatikleştirme.

**Ticari kanıt:** Kaynak, bu işin önceden satış müdürünün **neredeyse tam zamanlı işini** aldığını bildiriyor. Parasal rakam yok.

**Kaynak:** Reddit r/n8n real-business-problem thread'i.

**Risk:** İhale koşulunu yanlış yorumlama, deadline kaçırma, kaynak kapsamı.

**Senin için uygulama önizlemesi:** Eskişehir sanayisiyle çok uyumlu. İlk hizmet: **haftalık açık ihale/fırsat radarı + neden uygun olduğuna dair 3 maddelik özet + kaynak URL**. Başvuru yapma; yalnız research/triage.

---
