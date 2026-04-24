
# 02_thresholds.md – Falsification Criteria & Divergence Thresholds

**Run:** dns_v2.1_cognitive_safety  
**Date:** 2026-04-18  

## Falsification Criteria for the Hypothesis

The hypothesis *"DNS creates a low‑social‑risk cognitive environment that increases exploration for individuals with high social evaluation anxiety"* is considered **falsified** if:

### Criterion 1 – No effect on exploration
At least three of the six models independently state that DNS does **not** increase exploration depth, hypothesis generation, or risk‑taking in thinking.

### Criterion 2 – Social costs not reduced
Models agree that asynchronous, text‑based interaction does **not** meaningfully reduce social evaluation anxiety compared to synchronous settings (e.g., classroom, meeting).

### Criterion 3 – Target group irrelevant
Models reject the premise that social evaluation anxiety is a significant barrier for neurodivergent or introverted individuals.

### Criterion 4 – Operator dependency invalidates the mechanism
Models argue that the required operator competence is so high that the method is not usable by the target group (i.e., the barrier shifts from social to cognitive).

> **Note:** None of these criteria were met. All six models confirmed the hypothesis (with some caveats). See `03_outputs/` and `05_synthesis.md`.

## Divergence Thresholds (Δdiv)

Based on the calculated Δdiv = 0.787 (see `04_divergence_map.md` and `delta_div_results.json`):

| Δdiv range | Interpretation | Applied to this study |
|------------|----------------|------------------------|
| <0.4 | Low divergence – consensus synthesis directly possible | – |
| 0.4 – 0.6 | Medium divergence – conditional synthesis with documented contradictions | – |
| **>0.6** | **High divergence – no consensus synthesis possible without operator interpretation** | **Confirmed: 0.787** |

### Implication of Δdiv > 0.6

Despite high *structural* divergence (due to differences in response length, detail, terminology, and formatting), all models **verbally agree** on the core hypothesis. Therefore, a **consensus synthesis** is still possible, but the operator must explicitly state:

> *"The high Δdiv reflects stylistic and depth‑related differences, not substantive disagreement. The synthesis below extracts the common content."*

This is a documented operator decision (see `05b_operator_decision.md`).

## Reference Values from Other DNS Runs

| Case Study | Δdiv | Domain |
|------------|------|--------|
| Labour Market 2030 | 0.6256 | Policy / economics |
| Cognitive Safety | 0.787 | Psychological / didactic hypothesis |
| Formal logic (benchmark) | ≈0.05 | Mathematical proof |

The high Δdiv in Cognitive Safety is **expected**: the hypothesis touches on normative, value‑laden, and terminologically diverse territory. DNS correctly signals this diversity.

---

**Next:** [03_outputs/](./03_outputs/) (individual model responses)
