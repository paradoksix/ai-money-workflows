# Sabitlenmiş sürüm doğrulaması — 2026-09-03

Arşivde depo adresi **ve** 40 karakterlik sürüm kimliği taşıyan her kaydın
hâlâ gerçek olup olmadığı `scripts/verify_pins.py` ile denetlendi. Üç soru
soruldu: özgün depo hâlâ cevap veriyor mu · sabitlenen sürüme hâlâ
ulaşılabiliyor mu · deponun kök dizinindeki lisans durumu kayıtla uyuşuyor mu.

Kod indirilmedi, kopyalanmadı. Yalnız sabitlenen sürümün kök dizin listesi okundu.

## Sonuç

- Denetlenen kayıt: **9**
- Ulaşılamayan: **0**
- Lisans kaydı gerçekle uyuşmayan: **0**
- Özgün deposu sabitlenen sürümün ilerisine geçmiş: **3** (beklenen durum — sabitlemenin varlık sebebi bu)

| Vaka | Özgün depo | Sabitlenen sürüm | Ulaşılıyor mu | Depo şu an | Kök lisans | Sonuç |
|---|---|---|---|---|---|---|
| A001 | [sirlifehacker/Nano-Banana-Pro-Creative-Director](https://github.com/sirlifehacker/Nano-Banana-Pro-Creative-Director) | `1c82b35f1db2` | evet | sabitlenen sürüm hâlâ en güncel | yok | doğrulandı |
| A002 | [sirlifehacker/n8n-automations](https://github.com/sirlifehacker/n8n-automations) | `dcab49176024` | evet | sabitlenen sürüm hâlâ en güncel | yok | doğrulandı |
| A003 | [sirlifehacker/lead-gen-hacker](https://github.com/sirlifehacker/lead-gen-hacker) | `9ed891f4bc26` | evet | sabitlenen sürüm hâlâ en güncel | yok | doğrulandı |
| A004 | [sirlifehacker/social-story-scraper](https://github.com/sirlifehacker/social-story-scraper) | `69de2889cbe8` | evet | sabitlenen sürüm hâlâ en güncel | yok | doğrulandı |
| A005 | [lucaswalter/n8n-ai-automations](https://github.com/lucaswalter/n8n-ai-automations) | `08e33b6d5897` | evet | `57e1527902b8` (ilerlemiş) | yok | doğrulandı |
| A006 | [santifer/jacobo-workflows](https://github.com/santifer/jacobo-workflows) | `b26601dde3f3` | evet | `0ae8c642a67c` (ilerlemiş) | yok | doğrulandı |
| B001 | [sirlifehacker/n8n-job-hacker](https://github.com/sirlifehacker/n8n-job-hacker) | `edbc14455b17` | evet | sabitlenen sürüm hâlâ en güncel | yok | doğrulandı |
| B002 | [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz) | `93e196919aff` | evet | `a4ce217f284e` (ilerlemiş) | yok | doğrulandı |
| X001 | [YonkoSam/whatsapp-python-chatbot](https://github.com/YonkoSam/whatsapp-python-chatbot) | `8a1ae4680541` | evet | sabitlenen sürüm hâlâ en güncel | yok | doğrulandı |

## Dikkat edilecek kayıtlar

Yok. 9 kaydın hepsinde özgün depo cevap verdi, sabitlenen
sürüme ulaşıldı ve lisans kaydı gerçekle uyuştu.

## Nasıl tekrarlanır

```bash
python3 scripts/verify_pins.py
```

Ağ gerektirdiği ve başkalarının depolarına gittiği için CI üçlüsüne dâhil
değildir; araştırma turu açarken elle çalıştırılır.
