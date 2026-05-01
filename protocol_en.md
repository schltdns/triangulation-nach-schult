# frAIme Protocol (P1–P8)

**A reproducible, auditable workflow for argumentation drift**

frAIme structures how heterogeneous models and the human operator collaborate to reveal epistemic uncertainty. It is domain-agnostic.

frAIme does not seek consensus — it maps **where and why models diverge**.

---

## 🧭 Overview

1. **P1 — Hypothesize**
2. **P2 — Thresholds**
3. **P3 — Collect**
4. **P4 — Map Divergence**
5. **P5 — Synthesis**
6. **P5b — Operator Decision**
7. **P6 — Validation**
8. **P6b — Power Layer**
9. **P7 — Reflection**
10. **P8 — Versioning**

---

## P1 — Hypothesize

Define a falsifiable question.
- scope, assumptions, domain

**Output:** `01_hypothesis/`

## P2 — Thresholds

Define falsification criteria.
- drift thresholds, contradiction flags

**Output:** `02_thresholds/`

## P3 — Collect

Run identical prompt across different models.
- no cross-contamination, single-turn

## P4 — Map Divergence

frAIme calculates divergence on two layers:

### 4.1 Semantic Drift

drift = 1 - (Jaccard_sem + Cosine) / 2

where:
- Jaccard_sem = |concepts(A) ∩ concepts(B)| / |concepts(A) ∪ concepts(B)|
  (concepts extracted via noun-phrase chunking, not tokens)
- Cosine = embedding similarity (sentence-transformers)

Interpretation:
- drift < 0.3 → convergence
- 0.3–0.6 → productive friction
- >0.7 → epistemic blind spot

*Reference: case_study_frAIme "AI Learning vs Frontal Teaching" – drift 0.584–0.759 despite surface consensus; only one model provided primary sources.*

### 4.2 Graph Divergence

Models are nodes in directed graph G = (V,E). Edge weight w_ij = 1 - similarity(output_i, output_j). High-weight edges indicate friction points.

**Output:** `04_divergence_map/`

## P5 — Synthesis

Operator integrates using the Four Questions (Topic, Idea, Verifiable, Understandable).

**Output:** `05_synthesis/`

## P5b — Operator Decision

Human weighs, justifies, selects.

**Output:** `05b_operator_decision/`

## P6 — Validation

Compare with data, literature, experts.

**Output:** `06_validation/`

## P6b — Power Layer

Who controls, benefits, bears risk, is excluded.

**Output:** `06b_power_layer/`

## P7 — Reflection

Document bias, load, uncertainty.

**Output:** `07_reflection/`

## P8 — Versioning

Archive all artifacts with version tag.

**Output:** 
- `08_manifest_en.json` / `08_manifest_de.json`
- Zenodo DOI: 10.5281/zenodo.19793185
