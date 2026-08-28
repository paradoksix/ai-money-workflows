# Kendi belgelerinden cevap veren sistemler

Şirketin kendi belgelerine dayanarak cevap üreten yardımcılar. Satış gerekçesi çoğu zaman zekâ değil **gizlilik**: "verimiz dışarı çıkmasın". Ölçülecek şey de "bot var mı" değil; doğru belgeyi bulabiliyor mu, kaynağı doğru gösteriyor mu, ne kadar sürede cevaplıyor ve aynı anda kaç kişiye yetiyor.

**Türkiye'de kim satın alır?** Teknik belgesi olan üretici, eğitim kurumu, gizliliğe önem veren şirket

**Bu grupta 5 örnek var.** Ne kadar güvenilir oldukları — B: 1 · C: 4.

Harflerin ne anlama geldiği için `../RESEARCH_POLICY.md`, gruplar arası ortak dersler için `DESENLER.md`, hepsini birden filtrelemek için [bütün örnekler sayfası](https://paradoksix.github.io/ai-money-workflows/tum-vakalar.html).

---

## B022 — Şirket içi RAG knowledge agent

**Ne yapıyor?** Şirket dokümanlarından kaynaklı cevap üretip gerektiğinde Calendar/Slack aksiyonu başlatıyor.

**Risk:** Gizli belge, prompt injection, yanlış kaynak.

**Senin için uygulama önizlemesi:** RTX 3060 12 GB sayesinde küçük bir yerel model + embeddings ile **private RAG demo** araştırabilirsin. İlk hedef sağlık/finans değil; teknik ürün dokümanı, şirket prosedürü veya eğitim materyali daha güvenli.

---

## C029 — Offline University RAG Chatbot

**Ne satılmış?** Güney Afrika'daki üniversite için internete veri göndermeden local/open-source modelle çalışan RAG bilgi sistemi.

**Ticari kanıt:** **F/V: $5.500 deal**, 2.000+ öğrenci hedefi.

**Teknik:** Yerel GPU + önceden vectorize edilmiş seçilebilir kaynaklar; geliştirici native-code çözümünün n8n'e tercih edildiğini söylüyor. Kod ücretli/private library'de.

**Risk:** Kaynak doğruluğu, kullanıcı yetkisi, öğrenci verisi.

**Senin için uygulama önizlemesi:** RTX 3060 12 GB bu alanı deneysel olarak anlaman için yeterli. Büyük üniversite yerine **küçük eğitim kurumu, teknik servis dokümanı, ürün kataloğu veya şirket prosedürü** ile local RAG benchmark'ı araştırabilirsin. Bu alanda privacy satış argümanı güçlü.

---

## C042 — Custom RAG Chatbot

**Ne satılmış?** GPT/Claude/Gemini + LangChain/vector DB/FastAPI ile müşterinin belgelerine özel RAG chatbot.

**Ticari sinyal:** **4 ücretli review**.

**Risk:** Halüsinasyon, gizli belge, erişim kontrolü.

**Senin için uygulama önizlemesi:** Generic chatbot'tan daha ilginç. Mevcut PC'nde küçük yerel RAG prototipi çalıştırıp **teknik ürün kataloğu veya eğitim dökümanı** üzerinde kaynak-citation doğruluğunu test edebilirsin.

---

## C043 — Enterprise RAG Agent

**Ne satılmış?** Daha büyük müşteriler için Pinecone/Qdrant, GPT/Claude ve web arayüzüyle enterprise bilgi agent'ı.

**Ticari sinyal:** **5 review**.

**Risk:** Yetkilendirme, veri izolasyonu, prompt injection, SLA beklentisi.

**Senin için uygulama önizlemesi:** Enterprise hedefleme kısa vadede gereksiz. Aynı problemin **“10–100 PDF'lik private knowledge base”** küçük versiyonunu araştır; privacy ve kaynak gösterme özelliği temel değer olsun.

---

## C045 — Private / Self-hosted RAG

**Ne satılmış?** Flask/Django/Express + vector DB ile müşterinin kendi altyapısında çalışan private RAG sistemi.

**Ticari sinyal:** Görünür yaklaşık **$50 order**.

**Değer:** “Verimiz OpenAI'a gitmesin” problemi.

**Senin için uygulama önizlemesi:** Senin yerel AI ilgine en uyumlu vakalardan. RTX 3060 12 GB üzerinde küçük model + local embeddings + basit web UI ile **offline demo** yapılabilir; satıştan önce retrieval doğruluğu benchmark'ı önemli.

---
