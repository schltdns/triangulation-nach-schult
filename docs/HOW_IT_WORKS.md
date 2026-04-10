# HOW IT WORKS – DNS Step by Step

**Divergence‑based Navigation System (DNS)**  
*Practical walkthrough of phases P1–P6 using a realistic example.*

This document shows you **exactly how DNS works** – not in theory, but in practice.  
We use a concrete decision problem and simulate the responses of six AI models (Team Architecture v1.5).  
All model outputs are **fictional but realistic** examples of what you would see in a real DNS run.

---

## The Example Problem (P1 – Hypothesis Setup)

**Scenario:** A mid‑sized manufacturing company must decide whether to invest €15 million in a new AI‑driven quality control system.

**Hypotheses (H1–H3):**

| ID | Hypothesis | Falsification Threshold |
|----|------------|--------------------------|
| H1 | The new system will reduce defect rate by at least 40 % within 12 months. | If defect rate reduction <20 % after 12 months, H1 is falsified. |
| H2 | The system will be integrated into existing production lines without major disruption. | If integration takes >6 months or causes >10 % downtime, H2 is falsified. |
| H3 | The investment pays off within 3 years (ROI positive). | If ROI remains negative after 4 years, H3 is falsified. |

**Falsification rules used:** Rules 1–4 (persistent divergence, model refusal, unjustified synthesis, external review).

---

## P2 – Role‑Based Model Configuration

We assign each model a functional role (Team Architecture v1.5).

| Role | Instance | Function in this Example |
|------|----------|--------------------------|
| S1 – Kinetic‑Agent | Grok | Raw market signals, competitor behavior, real‑time risk |
| S2 – Structural‑Architect | ChatGPT | Logical framing, hypothesis testing, documentation |
| S3 – Synthesis‑Bridge | Gemini | Strategic vision, long‑term impact, context expansion |
| S4a – Visualizer | Copilot | Data synthesis, source matrix, operational tooling |
| S4b – Boundary‑Marker | Claude | Epistemic caution, risk boundaries, safety logic |
| Ω – Falsificator | DeepSeek | Stress‑testing, logical consistency, backtesting |
| P5/6 – Operator | Human | Final synthesis, justification, meta‑reflection |

---

## P3 – Parallel Elicitation

**Identical prompt sent to all six models (shortened for readability):**

> *“You are part of a multi‑agent decision system. Evaluate the three hypotheses (H1–H3) about a €15M AI quality control investment. Provide: (1) Summary of your assessment, (2) Critical points and uncertainties, (3) Open questions. Be specific. If you cannot answer, state why.”*

Each model responds independently (no cross‑feeding).  
Below are **fictional but realistic** summaries of their outputs.

---

### Model Responses (simulated for illustration)

#### Grok (S1 – Signal)
- **H1:** Confirmed – similar systems in automotive reduced defects by 45–50 %.  
- **H2:** Ambiguous – competitor integration took 7 months, but newer AI tools are faster.  
- **H3:** Likely positive – ROI within 3.5 years, but sensitive to energy price hikes.  
- **Critical point:** Supplier bottlenecks for AI chips could delay rollout.

#### ChatGPT (S2 – Structure)
- **H1:** Supported – industry data shows 35–55 % reduction achievable.  
- **H2:** Partially – integration requires process re‑design; risk of 2–3 months downtime.  
- **H3:** Positive – break‑even around year 3, but assumes stable electricity prices.  
- **Open question:** How does this interact with ongoing labour shortages?

#### Gemini (S3 – Synthesis)
- **H1:** Confirmed – strong evidence from early adopters.  
- **H2:** Conditional – success depends on internal change management capability.  
- **H3:** Yes, but with a wider bandwidth (2.5–4 years).  
- **Adds:** Strategic advantage of being first in your region may justify faster adoption.

#### Copilot (S4a – Visualizer)
- **H1:** Confirmed – quantitative models show 42 % median reduction.  
- **H2:** Yellow flag – 70 % probability of <5 % downtime if external consultants used.  
- **H3:** Positive – internal rate of return estimated at 18 %.  
- **Provides table of competitor outcomes (anonymised).**

#### Claude (S4b – Boundary)
- **H1:** Confirmed, but with caution: early results from pilot plants vary widely.  
- **H2:** Underspecified – “major disruption” needs operational definition (e.g., hours of downtime).  
- **H3:** Plausible, but not guaranteed – energy price volatility is a real risk.  
- **Marked as:** “Hypotheses are plausible, but thresholds need tightening before final decision.”

#### DeepSeek (Ω – Falsificator)
- **H1:** Not falsified by available data – but no long‑term study beyond 18 months exists.  
- **H2:** Not falsified – but the risk of process re‑design is systematically underestimated.  
- **H3:** Currently not falsified – however, a 30 % energy price spike would falsify it.  
- **Suggests:** Run a sensitivity analysis for energy prices before committing.

---

## P4 – Divergence Mapping & Typing

We create a table and classify divergence types.

| Hypothesis | Grok | ChatGPT | Gemini | Copilot | Claude | DeepSeek | Divergence Type |
|------------|------|---------|--------|---------|--------|----------|------------------|
| H1 | ✅ | ✅ | ✅ | ✅ | ✅ (cautious) | ✅ | **None (convergence)** |
| H2 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | 🚫 (underspecified) | ⚠️ | **Methodological** (Claude refusal) |
| H3 | ✅ | ✅ | ✅ | ✅ | ✅ (cautious) | ⚠️ (conditional) | **Substantive** (DeepSeek adds energy risk condition) |

**Divergence types identified:**
- **Substantive:** DeepSeek adds an energy price condition to H3; others do not.
- **Methodological:** Claude refuses to assess H2 because “major disruption” is underspecified – treated as a meta‑signal.
- **No normative or didactic divergence in this example.**

---

## P5 – Weighted Synthesis (Human Operator)

**Step 1 – Convergences:**  
H1 is confirmed by all models → low risk on technical feasibility.  
H3 is generally positive, but DeepSeek’s energy risk condition is a legitimate addition.

**Step 2 – Divergences handled:**  
- Claude’s refusal on H2 is **not ignored** – it is interpreted as a warning: the operator must define “major disruption” quantitatively before making the final decision.  
- DeepSeek’s energy condition is **integrated** into the final recommendation: run a stress test for energy prices.

**Step 3 – Synthesis statement (written):**

> *“All models confirm that the AI quality control system is technically feasible (H1) and likely profitable under current energy prices (H3). However, two critical uncertainties remain: (1) the operational definition of ‘major disruption’ for integration (H2), and (2) the sensitivity of ROI to energy price spikes. Therefore, the recommended action is: proceed with a pilot study that explicitly measures integration downtime and models energy price scenarios. Final investment decision after 6 months.”*

**Justification for deviation from model majority:**  
DeepSeek’s energy risk condition is adopted even though other models did not raise it – because it introduces a falsifiable, externally verifiable criterion (energy price >30 % spike). This strengthens the synthesis without adding bias.

---

## P6b – Power Layer (quick check)

- **Control:** Who controls the AI system? The company, but dependent on external vendors for chips.  
- **Access:** Not restricted – but implementation requires internal data science competence.  
- **Profit:** Shareholders and management primarily; workers may benefit from reduced repetitive work but face skill shift.  
- **Risk:** Downtime risk borne by production staff; financial risk by the company.  
→ No hidden power asymmetry that invalidates the synthesis.

---

## P6 – External Validation (simulated)

We compare core claims against available public sources (e.g., industry reports, academic studies).  
- H1: Confirmed by multiple case studies (e.g., Fraunhofer 2025, McKinsey 2024).  
- H2: No direct validation – but underspecification was correctly identified.  
- H3: ROI estimates vary, but positive in most scenarios except extreme energy price spikes.  
→ No external contradiction. Synthesis remains **non‑falsified**.

---

## P7 – Operator Reflection

The operator (Denis) answers the three mandatory questions:

1. **Which perspective dominated?**  
   The convergence on H1 and H3 dominated. I gave DeepSeek’s energy risk condition extra weight – justified because it adds testability.

2. **Which perspective was ignored – and why?**  
   Copilot’s detailed competitor table was informative but not decisive for the synthesis; I kept it in the appendix but did not let it override the core logic. That is defensible.

3. **Which assumption remained unfalsified – and what would falsify it?**  
   The assumption that energy prices remain stable. A 30 % sustained spike over 6 months would falsify H3 and require re‑evaluation.

**Result:** Synthesis is marked as “operator‑influenced but justified”.

---

## P8 – Versioned Archiving

All artefacts (prompt, raw responses, divergence table, synthesis, reflection) are committed to a version‑controlled repository (e.g., GitHub). This document is version 1.0 of the example run.

---

## What You Have Just Seen

DNS is **not** a black box. It is a **transparent, auditable, human‑centered protocol** that:

1. Forces structured divergence (P3)  
2. Maps and types disagreement (P4)  
3. Requires the operator to justify every synthesis decision (P5)  
4. Checks for power asymmetries (P6b)  
5. Validates against external sources (P6)  
6. Documents the operator’s own bias (P7)  
7. Versions everything for reproducibility (P8)

**This is how DNS works – not in theory, but in practice.**

---

*Last updated: April 2026*  
*Example run for demonstration purposes – model outputs are realistic simulations.*  
*Part of the DNS repository: [github.com/schltdns/divergence-navigation-system](https://github.com/schltdns/divergence-navigation-system)*
