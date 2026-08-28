# A006 — Jacobo Device Repair WhatsApp + Voice AI Agent

**Kanıt seviyesi:** A — gerçek production vaka + vaka sahibine doğrudan bağlı doğrulanmış GitHub iş akışı deposu.

## Ne yapılmış?

16 yıldır telefon/cihaz tamiri yapan Santifer iRepair işletmesinde WhatsApp ve telefon üzerinden gelen müşteri trafiğini yöneten çok ajanlı bir n8n sistemi kurulmuş.

Merkez router müşterinin niyetini sınıflandırıyor ve ilgili alt ajana yönlendiriyor. Sistem randevu, gerçek fiyat/veritabanından teklif, stok/part order, insan devri ve WhatsApp/voice köprüsü gibi görevleri ayırıyor.

## Ticari/operasyonel sonuç

Kaynak sahibi ve repo dokümantasyonunda bildirilen sonuçlar:

- yaklaşık **%90 self-service**,
- yaklaşık **80 saat/ay** tekrar eden müşteri iletişiminin otomasyonu,
- **<30 saniye** yanıt süresi,
- **<€200/ay** toplam altyapı maliyeti,
- 12+ ay / repo anlatımında yaklaşık 2 yıl production kullanımı,
- işletme satıldığında sistemin yeni işletme sahibine devredilip kullanılmaya devam edilmesi.

Bu vaka için ayrı bir `$X freelance satış ücreti` kanıtlanmıyor. Kaynak sahibi sistemi tek başına satmadığını; tüm işletmeyi, içindeki AI/otomasyon sistemleriyle birlikte sattığını açıklıyor. Bu nedenle ekonomik kanıt türü **operational value / business asset**, freelancer fee değildir.

## doğrulanmış kaynak kodu

- Reddit vaka: https://www.reddit.com/r/n8n/comments/1sc3i30/i_built_a_whatsapp_voice_ai_agent_in_n8n_that/
- Repo: https://github.com/santifer/jacobo-workflows
- Pinned commit: `b26601dde3f35edddf3690bd2f5a6656420df073`

## birebir iş akışı dosyaları

- `jacobo-chatbot-v2.json` — merkezi router, intent classification ve kısa konuşma hafızası
- `subagente-citas.json` — doğal dil randevu talebini uygun slotlara çevirir
- `presupuesto-modelo.json` — Airtable'daki gerçek model + onarım + stok verisinden teklif üretir
- `hacer-pedido.json` — parça yoksa iç sipariş oluşturur
- `calculadora-santifer.json` — kombinasyon/indirim hesabını normal business logic ile yapar
- `contactar-agente-humano.json` — Slack üzerinden insan devri + konuşma özeti/deep-link
- `enviar-mensaje-wati.json` — voice agent'ın WhatsApp mesajı göndermesi için köprü

## Mimari ders

Bu vaka “her şeyi LLM'e yaptır” modelinin tersini gösteriyor. Bazı görevler LLM, bazıları saf business logic:

- niyet/routing ve doğal dil → LLM,
- gerçek fiyat/stock → Airtable source-of-truth,
- indirim hesabı → deterministik kod,
- kritik/istisna durum → insan devri,
- iletişim → WATI/WhatsApp ve ElevenLabs voice.

Bu ayrım, güvenilir ticari otomasyon için çok önemli.

## Riskler

- WhatsApp Business/Meta politika uyumu,
- müşteri kişisel verileri,
- voice-call rıza ve kayıt yükümlülükleri,
- yanlış fiyat veya stok bilgisi,
- LLM/API provider değişiklikleri,
- işletmenin source-of-truth tablosu bozulursa yanlış çıktı üretme.

## Lisans

GitHub repository metadata'sında açık bir root lisans görünmüyor. Public repo olması yeniden dağıtım veya yeniden lisanslama izni anlamına gelmez. Bu ansiklopedide özgün deponun adresi + sabitlenmiş sürüm olarak tutulur; kod sahiplenilmez.

## Senin için uygulama önizlemesi

Türkiye'de aynı sistemi komple kurmaya çalışma. En küçük satılabilir problem:

**“Servise gelen WhatsApp mesajından cihaz/marka/model/arıza/randevu bilgisini tamamla ve personele temiz iş talebi bırak.”**

İlk sürümde:

1. müşteri kendisi mesaj başlatır,
2. eksik marka/model/arıza bilgisi sorulur,
3. AI fiyat uydurmaz,
4. varsa fiyat yalnız doğrulanmış servis tablosundan okunur,
5. personel tek özet kart görür,
6. müşteri isterse insana devredilir.

Telefon tamiri dışında motosiklet servisi, beyaz eşya servisi, bilgisayar servisi ve küçük teknik bakım şirketleri aynı desene uyabilir. Voice katmanı ancak yazılı intake gerçekten çalıştıktan sonra eklenmeli.
