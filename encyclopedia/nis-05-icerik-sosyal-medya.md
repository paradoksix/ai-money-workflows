# İçerik, sosyal medya ve bülten

Uzun içeriği parçalara ayırmak, bülten hazırlamak, kaynak taramak ve yüz göstermeyen kanallar için üretim yapmak. Buradaki en önemli ders C059'da net görünüyor: bu örnekler yüz göstermeyen kanalın para kazandığını değil, **kanal sahiplerinin video üretimine para ödediğini** kanıtlıyor.

**Türkiye'de kim satın alır?** Eğitmen, danışman, podcast yapan, B2B firma, kanal sahibi

**Bu grupta 11 örnek var.** Ne kadar güvenilir oldukları — A: 1 · B: 5 · C: 5.

Harflerin ne anlama geldiği için `../RESEARCH_POLICY.md`, gruplar arası ortak dersler için `DESENLER.md`, hepsini birden filtrelemek için [atlas sayfası](https://paradoksix.github.io/ai-money-workflows/).

---

## A004 — Social Story Scraper / trend intelligence

**Ne satılmış?** X/Twitter ve diğer kaynaklarda yükselen hikâyeleri toplayıp kümelendiren, araştıran ve içerik fırsatına çeviren sistem.

**Ticari kanıt:** **V: ~2,9M impression + 10+ high-ticket inbound lead**, yaklaşık `$75` run cost bildiriliyor. Bu doğrudan workflow satışı değil, içerikten ticari lead üretimi.

**Kaynak:** `sirlifehacker/social-story-scraper`, commit `69de288...` + Reddit vaka.

**Risk:** Kaynak platform scraping'i, telif, yanlış trend yorumlama.

**Senin için uygulama önizlemesi:** Genel teknoloji trendi yerine **tek sektör istihbaratı** daha satılabilir: örneğin “Türkiye'de motosiklet/yedek parça gündemi”, “otelcilik şikâyet trendleri”, “rakip e-ticaret kampanyaları”. Yerel model, özetleme ve kümelendirmeyi bilgisayarında yapabilir; web kaynak toplama tarafı ayrı tutulur.

---

## B007 — Eski web sitesinden yeniden tasarım brief'i

**Ne yapıyor?** Mevcut siteyi scrape edip içerik/yapı analizi yapıyor ve AI site-builder için PRD/yeniden tasarım brief'i çıkarıyor.

**Stack:** n8n + Firecrawl + LLM + site builder.

**Risk:** Site içeriği/IP ve hatalı ihtiyaç çıkarımı.

**Senin için uygulama önizlemesi:** Yerel işletmelere “web sitesi yaparım” yerine **“mevcut sitenizin eksiklerini, içerik haritasını ve yeni site brief'ini 1 günde çıkarırım”** şeklinde düşük ticket danışmanlık ürünü olarak incelenebilir.

---

## B009 — YouTube → X + LinkedIn repurposing

**Ne yapıyor?** Uzun videodan thread ve profesyonel sosyal medya postları çıkarıyor.

**Kanıt:** Çalışan JSON açık.

**Risk:** Kaynak içeriğin hakkı ve marka dili.

**Senin için uygulama önizlemesi:** Türkiye'de eğitmen, podcast, danışman, emlakçı veya doktor içerik üreticilerine **“1 uzun video → 6 kısa post + 2 LinkedIn yazısı”** şeklinde manuel+AI hizmet olarak test edilebilir. Video düzenleme deneyimin bu kategoriyi daha erişilebilir kılar.

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

## C044 — PDF/makale → iki-host AI podcast

**Ne satılmış?** PDF veya makaleyi iki konuşmacılı AI podcast formatına çevirme.

**Ticari sinyal:** **18 review**, `$5` basic giriş paketi.

**Risk:** Düşük fiyat, kaynak telifi, sentetik ses kalitesi.

**Senin için uygulama önizlemesi:** Tek başına düşük ticket. Fakat **eğitim materyali → sesli çalışma özeti**, **şirket raporu → yönetici audio brief** gibi daha niş ve kurumsal biçime çevrilirse değer artabilir. Yerel TTS/Whisper araçları maliyeti azaltabilir.

---

## C059 — Faceless YouTube Full Production

**Ne satılmış?** Script, voice, edit, görsel ve thumbnail dahil faceless YouTube video üretimi.

**Ticari sinyal:** **143 review, 11 aktif queue**, `$20` basic.

**Önemli ders:** Bu, faceless kanalın para kazandığını değil **kanal sahiplerinin prodüksiyona para ödediğini** kanıtlıyor.

**Senin için uygulama önizlemesi:** Kendi kanalını büyütme riskini almadan, **belirli bir nişte video prodüksiyon hizmeti** araştırılabilir. Türkçe/İngilizce eğitim, tarih, teknoloji veya şirket içi açıklayıcı video tarafı daha savunulabilir.

---

## C060 — Faceless Editing / Content Service

**Ne satılmış?** Faceless kanal sahiplerine düzenli editing/content üretimi.

**Ticari sinyal:** **173 review, 21 queue**.

**Senin için uygulama önizlemesi:** Aylık retainer'a en uygun yaratıcı işlerden. AI ile script/rough-cut hızlanabilir; sen kalite kontrol, ritim, görsel seçim ve final export kısmını sahiplenirsin.

---

## C061 — 8 Dakika Niche Faceless Video + Thumbnail

**Ne satılmış?** Belirli nişte yaklaşık 8 dakikalık faceless video ve thumbnail.

**Ticari sinyal:** **48 review**, `$20` giriş.

**Risk:** Düşük fiyatlı global rekabet.

**Senin için uygulama önizlemesi:** Fiyat rekabetine girmek yerine **Türkçe niş uzmanlığı veya iki dilli içerik** üzerinden ayrışmak daha mantıklı. Örneğin teknik eğitim/yerel sektör videosu.

---

## C084 — 44-Country Newsletter Localisation

**Ne yapılmış?** 44 ülkeye ayrı marka/dil varyasyonlu newsletter üretimi; product feed + template + brand voice + insan review.

**Ticari kanıt:** Yaklaşık **1.500 newsletter/yıl**. Manuelde ~4 saat/newsletter ≈ 6.000 saat; yeni akış 5–15 dakika/newsletter, **S: ~5.600 saat/yıl** tahmini tasarruf.

**Kaynak:** Reddit r/n8n real-business-problem thread'i.

**Risk:** Localization hatası, regülasyon/promosyon metni, marka tonu.

**Senin için uygulama önizlemesi:** 44 ülke değil; **Türkçe + İngilizce + bir ihracat pazarı** için ürün bülteni/teklif maili. Yerel LLM ilk taslak/translation yapabilir; final insan review şart.

---
