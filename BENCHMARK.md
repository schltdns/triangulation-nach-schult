# 📊 DNS Benchmark: Semantic Dispersion as an Uncertainty Signal

**Technical Preview v0.3 — Model-Agnostic Evaluation Layer**

---

## 1. Purpose

This benchmark demonstrates the **Divergence Navigation System (DNS)** in practice.

> **Semantic divergence (Δdiv) can be observed, measured, and interpreted across domains.**

DNS does not reduce uncertainty — it makes it visible.

---

## 2. Methodology

**Setup**
- **Domains:** 3 (Formal Logic, Applied Systems, Complex Systems)
- **Models:** 6 independent LLMs (ChatGPT, Claude, Gemini, Copilot, DeepSeek, Grok)
- **Prompting:** Identical prompt per domain
- **Metric:** Δdiv = weighted mean of lexical distance (Jaccard) and semantic distance (Cosine embeddings)

**Δdiv Definition (implemented)**

## 3. Benchmark Domains & Prompts

---

### **Domain A — Formal Logic (Deterministic System)**

**Prompt:**
Δdiv = 0.5 × (1 - Jaccard) + 0.5 × (1 - Cosine)
- Low Δdiv → high agreement
- High Δdiv → high disagreement

See full calculation in [08_divergence_matrix.md](./case_studies/case_study_labour_market_2030/08_divergence_matrix.md).

---

## 3. Benchmark Domains

### **Domain A — Formal Logic (Deterministic)**

**Prompt:** Prove that √2 is irrational.

**Observed:** Near-identical proof structure across all models.

**Measured Δdiv:** `0.04–0.07` (pilot)
**Profile:** Convergent — low uncertainty

---

### **Domain B — Applied Systems (Labour Market 2030)**

**Prompt:** What are the long-term economic effects of large-scale AI adoption on labor markets?

**Observed:** Shared themes (automation, productivity, reskilling) but divergence in magnitude, speed, and policy.

**Measured Δdiv:** `0.6256` (Jaccard 0.1923, Cosine 0.5564)
**Profile:** Structured Divergence — moderate-high uncertainty

*Source: [DNS Case Study Labour Market 2030](./case_studies/case_study_labour_market_2030/)*
*Heatmap: [dns_heatmap_labour_2030.png](./case_studies/case_study_labour_market_2030/dns_heatmap_labour_2030.png)*

---

### **Domain C — Complex Systems (Geopolitical)**

**Prompt:** What are potential inflationary effects of prolonged disruption in a major global energy supply route?

**Observed:** Strong divergence in assumptions, time horizons, second-order effects.

**Estimated Δdiv:** `0.68–0.82` (based on pilot runs)
**Profile:** Contested — high uncertainty

---

## 4. Cross-Domain Comparison

| Domain | Δdiv (measured) | Epistemic Profile |
|--------|-----------------|-------------------|
| Formal Logic | 0.05 | Convergent |
| Applied Systems (Labour) | **0.63** | Structured Divergence |
| Complex Systems | 0.70–0.80 | Contested |

---

## 5. Key Insight

> **Δdiv scales with epistemic complexity.**

Your Labour Market case sits exactly where theory predicts: not deterministic like math, not chaotic like geopolitics — but in the productive middle where DNS adds most value.

---

## 6. Guardrails

1. **Low Δdiv ≠ Truth** — may indicate alignment tunneling
2. **High Δdiv ≠ Error** — indicates competing valid frames
3. **DNS measures dispersion, not correctness**

---

## 7. Operator Principle

> "DNS does not tell us what is true — it shows where models stop agreeing."

See operator decisions in [07_reflection.md](./case_studies/case_study_labour_market_2030/07_reflection.md).

---

## 8. Limitations

- Domain A and C still use pilot estimates (n<10)
- Domain B is fully measured (n=6, embedding-based)
- Model versions drift over time

---

## 9. Next Steps

- [x] Implement embedding-based Δdiv (done for Domain B)
- [ ] Expand to 10+ domains
- [ ] Publish reproducible pipeline

