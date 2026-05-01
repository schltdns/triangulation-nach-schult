# frAIme Protocol (P1–P8)

**Reproducible workflow for argumentation drift**

frAIme maps where and why models diverge — not whether they agree.

---

## P1 — Hypothesize → `01_hypothesis/`
Define a falsifiable question.

## P2 — Thresholds → `02_thresholds/`
Set falsification criteria.

## P3 — Collect
Run identical prompt across S1–Ω.

## P4 — Map Divergence → `04_divergence_map/`

**Semantic Divergence (Δdiv)** — auditable metric  
**drift** — simplified term for practice

Δdiv = 1 - (Jaccard_sem + Cosine) / 2

where:
- Jaccard_sem = |concepts(A) ∩ concepts(B)| / |concepts(A) ∪ concepts(B)|
- Cosine = sentence-transformer similarity

Interpretation:
- Δdiv < 0.3 (low drift) → convergence
- 0.3–0.6 (medium drift) → productive friction
- >0.7 (high drift) → blind spot

*Reference: case_study_frAIme – Δdiv 0.584–0.759 (high drift despite surface consensus)*

## P5 — Synthesis → `05_synthesis/`
## P5b — Operator Decision → `05b_operator_decision/`
## P6 — Validation → `06_validation/`
## P6b — Power Layer → `06b_power_layer/`
## P7 — Reflection → `07_reflection/`
## P8 — Versioning → `08_manifest_en.json`
