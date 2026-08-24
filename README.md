# AI Money Workflows

Bu repo, 2025–2026 döneminde **gerçek müşteri / gelir / ticari lead sonucu bildirilen** ve doğrudan kaynak GitHub reposu doğrulanabilen AI otomasyon örneklerini izlemek için hazırlanmıştır.

Amaç, başkalarının kodunu bizimmiş gibi yeniden yayımlamak değil; **orijinal upstream repo + doğrulanmış commit + gelir/müşteri kanıtı** bağını koruyarak araştırılabilir ve tekrar kurulabilir bir koleksiyon oluşturmaktır.

## A — Güçlü müşteri / para sinyali + doğrudan orijinal GitHub

### 1. AI Creative Director — $9K e-ticaret moda kampanyası
- Kaynak repo: https://github.com/sirlifehacker/Nano-Banana-Pro-Creative-Director
- Sabitlenen commit: `1c82b35f1db29e9f0ed35f5e0680148241a371b5`
- Reddit: https://www.reddit.com/r/n8n/comments/1p9uvtq/i_automated_a_9k_ecom_fashion_campaign_using_n8n/
- Kanıt: müşteri işi açık; kampanya `$9K` olarak tanımlanmış; bunun freelancerın net ücreti olduğu kanıtlanmıyor.
- Lisans: root `LICENSE` bulunamadı.

### 2. LinkedIn Jobs + Decision Maker Research
- Kaynak repo: https://github.com/sirlifehacker/n8n-automations
- Sabitlenen commit: `dcab49176024e410a1cc555ea8bda3f21f4c6f1f`
- Reddit: https://www.reddit.com/r/n8n/comments/1ocnoyj/ive_had_multiple_clients_hire_me_to_build_this/
- Kanıt: yazar, birden fazla müşterinin bu sistemi yaptırmak için kendisini tuttuğunu söylüyor.
- Lisans: root `LICENSE` bulunamadı.

### 3. B2B Lead Search Engine
- Kaynak repo: https://github.com/sirlifehacker/lead-gen-hacker
- Sabitlenen commit: `9ed891f4bc2666f19941ea8c03841555c4812b66`
- Reddit: https://www.reddit.com/r/n8n/comments/1t21mnr/i_created_a_leads_search_engine_in_n8n_b2b/
- Kanıt: B2B girişimcilerin varyantlarını yaptırmak için yazarı tuttuğu belirtiliyor.
- Lisans: root `LICENSE` bulunamadı.

### 4. Social Story Scraper — içerikten high-ticket lead üretimi
- Kaynak repo: https://github.com/sirlifehacker/social-story-scraper
- Sabitlenen commit: `69de2889cbe8a80124581d5f5b2abede4d221b3f`
- Reddit: https://www.reddit.com/r/n8n/comments/1oncgwf/3m_views_in_3_months_all_from_this_automation/
- Kanıt: ~2.9M impression, 10+ high-ticket inbound lead ve yaklaşık `$75` çalışma maliyeti bildiriliyor.
- Lisans: root `LICENSE` bulunamadı.

## X — Tartışmalı gelir iddiası

### WhatsApp Gemini chatbot — $275 iddiası
- Repo: https://github.com/YonkoSam/whatsapp-python-chatbot
- Commit: `8a1ae46805410b11d43eebf023ab23df41f9d116`
- Reddit: https://www.reddit.com/r/AI_Agents/comments/1l4gojr/i_made_275_in_a_1_day_building_a_whatsapp_ai/
- Not: yorumlarda API hizmetiyle gizli ilişki / reklam şüphesi bulunduğu için varsayılan clone listesine alınmadı.

## Kullanım

Windows:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\clone_originals.ps1
```

Linux / macOS / WSL:

```bash
chmod +x clone_originals.sh
./clone_originals.sh
```

Scriptler repoları `upstreams/` altında clone eder ve araştırmada doğrulanan commit'e checkout yapar.

## Lisans notu

Public GitHub reposu otomatik olarak yeniden dağıtım / yeniden lisanslama izni vermez. Açık lisansı olmayan upstream kodları bu repoya kopyalanmamıştır; bunun yerine orijinal repo ve Git geçmişi korunur.
