# Muhasebe & finans belgeleri

Fatura, tahsilat ve ön-muhasebe süreçleri. Bu nişin değişmez kuralı her vakada tekrarlanıyor: **LLM rakam hesabı yapmasın.** AI yalnız alan çıkarır; matematiği, vergi kontrolünü ve format doğrulamasını deterministik kod yapar, düşük güvenli satır insana gider.

**Türkiye'de kim satın alır?** Mali müşavir, dijital ajans, çok şubeli işletme, e-ticaret firması

**Bu nişte 3 vaka var.** Kanıt dağılımı — C: 3.

Kanıt dereceleri için `../RESEARCH_POLICY.md`, nişler arası kesişen dersler için `DESENLER.md`, tüm vakaların filtrelenebilir listesi için `../docs/index.html`.

---

## C002 — Japanese Google Ads Invoice Processor

**Ne satılmış?** Japon Google Ads faturalarındaki karmaşık/negatif satırları kurallı biçimde parse edip muhasebe sürecine hazırlayan sistem.

**Ticari kanıt:** **V/S: yaklaşık $2K/ay sistem değeri** bildiriliyor. Bunun freelancer ücreti mi yoksa müşteriye sağlanan değer mi olduğu net değil; bu yüzden rakam gelir diye yazılmıyor.

**Nasıl çalışıyor?** Deterministik parser + Claude structured output + Board API/Sheets benzeri iş akışı.

**Risk:** Finansal doğruluk; AI'nın rakam/vergi alanlarını yanlış okuması.

**Senin için uygulama önizlemesi:** Türkiye'de doğrudan muhasebe kaydı yazdırmak yerine **“PDF/e-posta faturası → firma/tarih/tutar/vergi/proje alanları → doğrulama kuyruğu → Excel”** olarak düşün. OCR/LLM yalnız veri çıkarır, matematik ve format kontrollerini normal kod yapar. Bu senin düşük maliyet tercihinle uyumlu.

---

## C005 — Bookkeeping Process Automation

**Ne satılmış?** Muhasebe firmasının belge/toplama/ön-muhasebe süreçlerini otomatikleştirme.

**Ticari sonuç:** **S: yaklaşık 600 saat/yıl doğrudan tasarruf**; ölçek etkisiyle 2.400 saat/~$30K ücret tasarrufu tahmini. Sonuç yalnız n8n'e değil yeni pre-accounting yazılımına da bağlı.

**Risk:** Vergi/muhasebe doğruluğu, yanlış sınıflandırma.

**Senin için uygulama önizlemesi:** Türkiye'de mali müşavirin resmi muhasebe kararını otomatikleştirmek yerine **belge toplama, dosya adlandırma, eksik evrak kontrolü, fatura alanlarını Excel'e çıkarma, müşteri hatırlatma** gibi ön süreçlere odaklan. Finansal kararı insanda bırak.

---

## C015 — Stripe Overdue Invoice Chaser

**Ne yapılmış?** Gecikmiş Stripe faturalarını belirli günlerde farklı tonlarda e-mail ile takip eden sistem.

**Ticari sonuç:** **V: $4.200 alacağın 6 haftada geri kazanıldığı** bildiriliyor.

**Risk:** Yanlış müşteriye agresif hatırlatma, ödeme uyuşmazlığı.

**Senin için uygulama önizlemesi:** Türkiye'de Stripe yerine müşterinin kullandığı fatura/CRM/Sheet sisteminden **“vadesi geçenleri listeler + hazır hatırlatma taslağı üretir + insan onayı”** versiyonu araştırılabilir. Tahsilatı otomatik yapma.

---
