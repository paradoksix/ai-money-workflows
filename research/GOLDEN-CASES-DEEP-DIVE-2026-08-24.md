# Altın Vakalar Derin Araştırma — 2026-08-24

Bu rapor, ansiklopedide özellikle kovalanacak 10 C-vakasını yeniden inceler. Hedef: exact repo/Gist/template, ikinci ticari kanıt, vaka sahibi–repo ilişkisi, gelir semantiği, teknik mimari ve güvenilirlik kırmızı bayrakları.

## Sonuç özeti

- **C027 → A006'ya yükselmeye hazır:** exact production repo, 7 sanitised n8n workflow, aynı vaka sahibiyle doğrudan bağlantı ve pinned commit bulundu.
- **C004 güçlendi:** Powerprozesse için 2025 boyunca 20 → 23 müşteri, birden fazla işe alım ilanı ve n8n Community'de somut tenant-damage workflow örneği bulundu. Exact resmi workflow reposu bulunmadı.
- **C008 dikkat gerektiriyor:** Reddit'teki orijinal self-report `$500`; aynı hikâyenin daha sonra başka bir LinkedIn hesabında neredeyse kelimesi kelimesine `$1,500` olarak tekrarlandığı görüldü. Bu ikinci kaynak doğrulama değildir; tam tersine kaynak kirliliği/rakam tutarsızlığıdır.
- **C018 kısmen geri doğrulandı:** orijinal Reddit kaynağı bu turda doğrudan alınamadı; bağımsız bir Reddit günlük arşivi u/marc00099'ın ilk yerel müşteri olarak tutoring business'a `$5K` WhatsApp bot sattığını ve 2 günde teslim ettiğini kaydetmiş. Exact code yok.
- **C029 güven notu düşürüldü:** $5,500 offline university RAG anlatısı teknik olarak ayrıntılı olsa da kod paid/private; 2,000+ öğrenci / tek GPU concurrency sorusuna kaynak sahibi cevap vermeyip promosyon bağlantısına yöneliyor.
- C001, C002, C003, C005, C006 için ticari/teknik ayrıntı arttı ancak exact source bulunmadı.

---

## A006 (eski C027) — Jacobo: Device Repair WhatsApp + Voice AI Agent

**Karar:** A seviyesine yükselt.

**Birincil vaka:**
https://www.reddit.com/r/n8n/comments/1sc3i30/i_built_a_whatsapp_voice_ai_agent_in_n8n_that/

**Exact repo:**
https://github.com/santifer/jacobo-workflows

**Pinned commit:**
`b26601dde3f35edddf3690bd2f5a6656420df073`

**Repo ile vaka bağlantısı:** Reddit yazarı workflow'ları açıkça bu repoya bağlar. Repo README'si aynı Jacobo sistemini ve Santifer iRepair üretim ortamını anlatır.

**Exact workflow dosyaları:**
- `jacobo-chatbot-v2.json` — merkezi router, intent classification, shared memory
- `subagente-citas.json` — randevu
- `presupuesto-modelo.json` — gerçek Airtable fiyat/stock verisinden teklif
- `hacer-pedido.json` — parça yoksa internal order
- `calculadora-santifer.json` — deterministik fiyat/indirim hesabı
- `contactar-agente-humano.json` — Slack üzerinden human handoff
- `enviar-mensaje-wati.json` — WhatsApp sender/cross-channel bridge

**Bildirilen sonuç:**
- ~%90 self-service
- ~80 saat/ay insan işi azaltma
- <30 saniye response
- <€200/ay toplam altyapı
- 12+ ay (repo README'sinde 2 yıl) production kullanımı
- işletme 2025'te satıldı; teknik olmayan yeni sahibi sistemi çalıştırmaya devam etti

**Gelir semantiği:** Bu bir `$X freelance sale` değildir. Yazar sistemi ayrı fiyatla satmadığını, tüm işletmeyi going-concern olarak sattığını ve AI sistemlerinin işletmeyle beraber devredildiğini açıklar. Bu nedenle ekonomik kanıt türü **operational value/business asset**, bağımsız freelancer fee değil.

**Teknik ayrıntılar:** WATI WhatsApp BSP; ElevenLabs voice; Airtable source-of-truth; farklı görevler için farklı LLM; OpenRouter fallback; n8n self-hosted cloud; built-in execution logs + Slack HITL, manuel WATI conversation review.

**Lisans:** GitHub repository metadata'sında lisans görünmüyor. Public repo = yeniden dağıtım/relicense izni değildir. Upstream referans + pinned commit olarak tutulmalı.

**Türkiye önizlemesi:** Telefon/motosiklet/beyaz eşya servisi için ilk küçük sürüm yalnız mesajdan `cihaz/marka/model/arıza/randevu` alanlarını tamamlayıp personele temiz özet bıraksın. AI fiyat uydurmasın; teklif gerçek fiyat tablosundan gelsin. Voice en son eklenmeli.

---

## C001 — Ship Manager Lead Capture

**Birincil vaka:**
https://www.reddit.com/r/n8n/comments/1mzz8j9/got_my_first_paying_client_here_is_the_workflow_i/

**Yeni doğrulanan ayrıntılar:**
- İlk ücretli müşteri.
- IMO number → local Puppeteer `/scrape` → Equasis login → WSD Online navigation → ship-management company.
- Apify SERP ile company/domain'e ait açık e-mail araştırması.
- Results Google Sheets'e.
- WSD tarafında tab/meta-refresh/iframe ve missing-field sorunları; 3 retry + 10s bekleme.
- Müşteri edinme: sosyal medyada workflow yardımı isteyen birini görüp ilk yanıt veren kişi olmuş.
- Scope yalnız workflow değil: VPS, n8n, Node.js/Puppeteer ve backup kurulumu.
- Yazar setup fee + monthly recurring modeline geçtiğini anlatıyor.
- Kendi ifadesiyle ilk projeyi düşük fiyatlamış ve scope'u hafife almış.

**Source durumu:** Post flair'i `Code Not Included`. Exact public repo bulunamadı. C kalır.

**Türkiye önizlemesi:** Aynı araştırma mimarisini denizcilikten önce `ürün kodu → üretici/distribütör → ülke → açık kurumsal iletişim` için kullanmak daha erişilebilir. Eskişehir/Ankara sanayi firmalarına ihracat/distribütör araştırması doğal uyarlamadır.

---

## C002 — Japanese Google Ads Invoice Processor

**Birincil vaka:**
https://www.reddit.com/r/n8n/comments/1lm0y5y/i_built_a_2kmonth_automation_system_for_japanese/

**Yeni doğrulanan ayrıntılar:**
- Müşteri: Japon real-estate advertising agency.
- Pozitif/predictable satırlar normal kodla; karmaşık negatif invoice line'ları Claude 3.5 Sonnet structured output ile.
- Fuzzy project match Board API üzerinden.
- Sheets/HTTP → müşterinin invoice platformu.
- Rate limits için loop/batching.
- Negative-only faturalar için Telegram human-in-the-loop check.
- Sistem geliştirici tarafından hosted; Yahoo Ads, Meta Ads ve LINE Ads'e genişletiliyor; custom control panel planlanmış.
- Müşteri acquisition: Japonya'da önceden tanıdığı bir bağlantı; ilk işi overdeliver edip sonra daha fazla otomasyon almış.

**Gelir semantiği:** Kaynak `around $2,000/month in value` diyor. Bunu freelancerın aylık aldığı ücret diye yazmak yanlış. **V/S = client system value**.

**Source durumu:** Workflow paylaşma talepleri var ancak public GitHub/Gist yok. Aynı yazarın cross-postları bağımsız ikinci kanıt sayılmaz. C kalır.

**Türkiye önizlemesi:** `PDF/e-mail fatura → alan çıkarma → deterministik vergi/tutar kontrolleri → düşük-confidence kuyruğu → Excel/ön-muhasebe` şeklinde düşün. LLM rakam hesabı yapmamalı.

---

## C003 — 50K+ Product Catalog Overhaul

**Birincil vaka:**
https://www.reddit.com/r/n8n/comments/1kql6nm

**Yeni doğrulanan ayrıntılar:**
- Bir haftada 50K+ product page.
- Sparse listing → SEO description + specs/attributes.
- Rakip mağazaların scrape edilip aynı ürün bazında karşılaştırılması.
- Tüm product category'lerin remap edilmesi.
- Aynı hafta custom scrapes + invoice/quote generation.
- Yazarın kritik cümlesi: n8n tek başına işin küçük kısmı; gerçek değer `data wrangling and cleanup`, giderek Python + Postgres/SQL kullanıyor.

**Source durumu:** Exact repo bulunmadı. Önceki `conor-is-my-name` bağlantısı kesin doğrulanamadığı için resmi author/repo ilişkisi olarak kullanılmamalı. C kalır.

**Türkiye önizlemesi:** Oto yedek parça, hırdavat, elektrik malzemesi, sanayi ekipmanı gibi kataloglarda `duplicate + eksik teknik alan + kategori eşleme + low-confidence review queue`. Bu vaka ürün yazmaktan çok data engineering işidir.

---

## C004 — Powerprozesse Property-Management Vertical

**Birincil/tekrarlı kaynaklar:**
- https://www.reddit.com/r/n8n/comments/1oh9rpo/automation_developer_n8n_remote_3050k/
- https://www.reddit.com/r/n8n/comments/1obh937/looking_for_n8n_developers_100_remote_fulltime/
- n8n Community Powerprozesse job posts

**Yeni doğrulanan ayrıntılar:**
- Almanya'da yalnız property-management/Hausverwaltung şirketlerine odaklanıyor.
- Temmuz 2025'te Make.com'dan n8n'e geçtiklerini söylüyor.
- Ekim 2025: 20 yeni müşteri; founder + bir developer.
- Kasım 2025: 23 yeni müşteri.
- Reddit'ten bir n8n developer işe alıp en az 2 aydır çalıştırdıklarını söylüyor.
- n8n Community'deki somut workflow örneği: `tenant submits damage report → AI classifies → contractor assignment → tenant notification`.
- Daha sonraki company posts: e-mail'den Casavi ticket üretme, tenant/object otomatik eşleme, duplicate incident detection, processed e-mail archive, AI-drafted portal notice.
- Full-time n8n rollerinde €3K–€5K/month gross / €30K–€60K/year bandında ilanlar var; bu agency revenue değildir ama ticari ölçeğin hiring sinyalidir.

**GitHub:** `Powerprozesse` aramasında resmi company workflow repo bulunmadı. Bulunan `gagan114662/powerprozesse-property-n8n-proof` üçüncü taraf proof/aday reposudur; original kabul edilmez.

**Karar:** C'de kalır, fakat ticari süreklilik kanıtı güçlü.

**Türkiye önizlemesi:** Site/apartman yönetim şirketlerinde e-mail/WhatsApp arıza taleplerini `su/elektrik/asansör/temizlik/aidat` gibi kategorilere ayırıp yöneticiye görev kartı. Usta atama/harcama onayı insanda kalmalı.

---

## C005 — Bookkeeping Process Automation

**Birincil vaka:**
https://www.reddit.com/r/n8n/comments/1ncjqju/has_anyone_actually_automated_a_real_business/

**Doğrulanan sonuç:**
- 600 saat/yıl doğrudan tasarruf.
- Client list 4x büyürken yeni çalışan alınmadığı için effective 2,400 saat.
- Yaklaşık 30K wage saving.
- Kritik caveat: yalnız n8n değil; yeni pre-accounting software + n8n document management/client chasers birlikte.

**Source durumu:** Exact repo yok. C kalır.

**Türkiye önizlemesi:** Muhasebe kararını AI'ya vermek yerine evrak toplama, eksik belge hatırlatma, dosya adlandırma, PDF alan çıkarma, review queue.

**Bu thread'den çıkan yeni güçlü vakalar:** Volume 7'ye eklenmiştir: D365 licensing replacement, UK school retainer, warehouse scan optimisation, CRM sync replacement, real-estate document automation, manufacturing tender research, 44-country newsletter automation.

---

## C006 — 115+ Workflow Monitoring Dashboard / AigencyTracker

**Birincil vaka:**
https://www.reddit.com/r/AiAutomations/comments/1qrhf8c/how_i_manage_115_n8n_workflows_for_11_clients/

**Yeni doğrulanan ayrıntılar:**
- Agency yaklaşık 1 yılda 2 → 11 müşteri.
- n8n + Make + Power Automate enterprise.
- 115+ workflow.
- Önceden ~2h/day monitoring; merkezi panel sonrası ~10 min/day.
- Detection time günlerden dakikalara indiği bildiriliyor.
- n8n API execution data, abnormal pattern alerts, client reports.
- 4 ay internal kullanım sonrası `aigencytracker.com` olarak productize edilmiş.
- Agency vertical: industrial + cybersecurity.

**Source durumu:** AigencyTracker proprietary. Thread'deki `FlowMetr` GitHub projesi aynı probleme açık-source alternatif fakat vaka yazarının exact sistemi değil. B/A diye yanlış eşleştirilmemeli. C kalır.

**Türkiye önizlemesi:** İlk müşteri ürünü değil; 3–5 automation client sonrasında doğal retainer katmanı: execution health, failed credential/API change, monthly report, incident SLA.

---

## C008 — Bookstore WhatsApp AI Order Assistant

**Birincil Reddit vaka:**
https://www.reddit.com/r/n8n/comments/1rq486u/i_made_500_on_my_first_n8n_paid_project_building/

**Reddit'te doğrulanan:**
- Author: `anassy1`.
- `$500` first paid n8n gig.
- Local bookstore, manual WhatsApp support/orders.
- Supabase + OpenAI/LangChain.
- Audio transcription, vision for receipts/product images, intent routing, hybrid FTS + vector search, order state, COD/bank transfer, shipping-data collection.
- Supabase ~$25/mo + Hostinger VPS ~$100/year + OpenAI tokens.
- Cleaned template yalnız Linktree/profile üzerinden; GitHub değil.
- Evolution API (unofficial WhatsApp API) kullanmış ve Meta ban riskini bizzat uyarıyor.
- Benzer sistemleri başka işletmeler için de yaptığını söylüyor.

**Önemli güvenilirlik bulgusu:** Aynı hikâye daha sonra `Raghavendra J.` adlı farklı bir LinkedIn hesabında neredeyse aynı metinle **$1,500** proje olarak paylaşıldı. Bu, bağımsız doğrulama değildir ve rakam tutarsızlığı oluşturur. Ana vaka için Reddit'teki `$500` korunmalı; LinkedIn kopyası kanıt olarak kullanılmamalı.

**Karar:** C kalır; exact public repo yok, source contamination notu eklenmeli.

**Türkiye önizlemesi:** Resmi WhatsApp BSP/API tercih et; ilk sürüm siparişi otomatik finalize etmek yerine ürün/adet/adres bilgilerini toplayıp personele draft order bıraksın.

---

## C018 — Tutoring Business $5K WhatsApp Automation

**Önceki kaynak URL:**
https://www.reddit.com/r/NoCodeSaaS/comments/1sbzb0s/printing_with_claude_struere/

**Bu turdaki durum:** URL doğrudan fetch edilemedi ve web search'te indekslenmedi. Bu nedenle kaynak erişilebilirliği zayıf.

**İkincil arşiv desteği:** AI Pulse Daily 2026-04-14 özeti, Reddit user `u/marc00099` için şu vakayı kaydediyor: yerel işletmelere yüz yüze demo; ilk deal tutoring business'a **$5K WhatsApp bot**, **2 günde shipped**. Bu, önceki notun ana fiyat/sales kanalını destekliyor fakat exact source'un yerini tutmuyor.

**Karar:** C kalır; `source_revalidation_needed`. Exact workflow/repo yok.

**Türkiye önizlemesi:** Dil kursu/özel ders merkezinde ilk atom: inquiry → seviye/konu/uygun saat toplama → takvim önerisi → ödeme/hatırlatma. Öğrenci değerlendirmesini AI'ya bırakma.

---

## C029 — Offline University RAG Chatbot

**Birincil vaka:**
https://www.reddit.com/r/n8nbusinessautomation/comments/1qiryis/i_sold_a_rag_chatbot_for_5500_code_beat_nocode/

**Doğrulanan teknik gerekçeler:**
- `$5,500 deal` self-report.
- University client; hedef 2,000+ student.
- No recurring API; full offline/local GPU.
- Pre-vectorized selectable sources.
- Model swapping.
- Adjustable chunk retrieval.
- GPT-OSS / client-owned GPU.
- Native-code çözüm n8n versiyonuna tercih edilmiş.

**Kırmızı bayrak:** Kaynak sahibi aynı zamanda Augmented AI / eğitim-library promosyonu yapıyor. 2,000+ student için tek GPU concurrency sorusuna teknik cevap vermek yerine framework/library linki bırakıyor. Exact code public değil, paid/private library bağlamı var.

**Karar:** C kalır; teknik fikir güçlü, ticari claim orta güven. A/B'ye yükseltme yok.

**Türkiye önizlemesi:** Üniversite yerine 10–100 teknik PDF'li bir üretici/eğitim merkezi için local RAG. Ölçülecek şey “chatbot var” değil: retrieval hit-rate, citation accuracy, response latency, concurrent user sınırı.

---

# Araştırma sonucu: altın vakaların yeni sırası

1. **A006 Jacobo device repair** — exact production source bulundu, en güçlü sonuç.
2. **C004 Powerprozesse property management** — en güçlü tekrarlı ticari vertical kanıt.
3. **C003 50K catalog overhaul** — Türkiye için en güçlü data-operation paterni.
4. **C002 Ads invoice processor** — human-in-loop financial preprocessing modeli.
5. **C006 workflow monitoring** — recurring revenue için doğal ikinci katman.
6. **C005 bookkeeping document/client chaser** — boring ops, yüksek ROI.
7. **C001 maritime/company research** — acquisition + setup/retainer modeli ilginç.
8. **C008 bookstore WhatsApp** — gerçek paid claim ama kaynak kirliliği/unofficial API riski.
9. **C018 tutoring** — satış paterni güçlü; primary source tekrar doğrulanmalı.
10. **C029 offline university RAG** — yüksek ticket, fakat seller-promo/concurrency belirsizliği.

# Sonraki exact-source avı

- Powerprozesse resmi workflow/source repo veya müşteriye ait public case study.
- C003 50K katalog yorumunun kesin Reddit author kimliği ve public GitHub profili.
- C008 `anassy1` temiz template'in gerçek dosya kaynağı/lisansı; Linktree'den GitHub'a çıkış var mı.
- C018 orijinal Reddit thread / u/marc00099 profile / code artefact.
- C001 Puppeteer scraper public artefact var mı.
- C002 hosted control panel/repo izi.
