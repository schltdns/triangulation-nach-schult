# EXAMPLE RUN – DNS in Action

**Complete P1–P6 walkthrough using a real‑world decision problem.**  
*All model responses are simulated but realistic. The purpose is to show the mechanism, not to provide investment advice.*

---

## The Decision Problem

A mid‑sized manufacturing company must decide whether to invest €15 million in an AI‑driven quality control system.

**Three hypotheses (P1):**

| ID | Hypothesis | Falsification Threshold |
|----|------------|--------------------------|
| H1 | Defect rate reduction ≥40 % within 12 months | If <20 % after 12 months → H1 falsified |
| H2 | Integration without major disruption | If downtime >10 % or integration >6 months → H2 falsified |
| H3 | Positive ROI within 3 years | If ROI still negative after 4 years → H3 falsified |

**Falsification rules:** Rules 1–4 (persistent divergence, model refusal, unjustified synthesis, external review).

---

## P2 – Role Assignment (Team Architecture v1.5)

| Role | Instance | Function in this run |
|------|----------|----------------------|
| S1 – Kinetic‑Agent | Grok | Market signals, competitor data |
| S2 – Structural‑Architect | ChatGPT | Logical framing, documentation |
| S3 – Synthesis‑Bridge | Gemini | Strategic context, long‑term view |
| S4a – Visualizer | Copilot | Data synthesis, source matrix |
| S4b – Boundary‑Marker | Claude | Risk boundaries, underspecification |
| Ω – Falsificator | DeepSeek | Stress‑testing, logical consistency |
| Operator | Denis Schult | Final synthesis, justification, reflection |

---

## P3 – Parallel Elicitation

**Identical prompt (simplified for readability):**

> *“Evaluate H1–H3 for the AI quality control investment. Provide (1) Summary, (2) Critical points, (3) Open questions. Be specific.”*

### Simulated model responses (shortened)

**Grok (S1):**  
- H1: ✅ Confirmed – automotive sector saw 45‑50 % reduction.  
- H2: ⚠️ Ambiguous – competitor integration took 7 months, but newer AI is faster.  
- H3: ✅ Likely positive – ROI ~3.5 years, but sensitive to energy prices.  
- *Critical:* Chip supply bottlenecks could delay rollout.

**ChatGPT (S2):**  
- H1: ✅ Supported – industry data shows 35‑55 %.  
- H2: ⚠️ Partial – requires process re‑design; risk of 2–3 months downtime.  
- H3: ✅ Positive – break‑even around year 3, assumes stable electricity prices.  
- *Open:* How does this interact with labour shortages?

**Gemini (S3):**  
- H1: ✅ Confirmed – strong early‑adopter evidence.  
- H2: ✅ Conditional – success depends on change management.  
- H3: ✅ Yes – ROI bandwidth 2.5–4 years.  
- *Adds:* First‑mover advantage may justify faster adoption.

**Copilot (S4a):**  
- H1: ✅ Confirmed – 42 % median reduction.  
- H2: ⚠️ Yellow flag – 70 % probability of <5 % downtime with external consultants.  
- H3: ✅ Positive – IRR ~18 %.  
- *Provides:* Competitor outcome table (anonymised).

**Claude (S4b):**  
- H1: ✅ Confirmed, but pilot results vary.  
- H2: 🚫 **Refused** – “major disruption” is underspecified. Needs operational definition.  
- H3: ✅ Plausible, but energy price volatility is a real risk.  
- *Marked:* H2 must be redefined before decision.

**DeepSeek (Ω):**  
- H1: ✅ Not falsified – but no long‑term study >18 months exists.  
- H2: ✅ Not falsified – but process re‑design risk is systematically underestimated.  
- H3: ⚠️ Conditional – a 30 % energy price spike would falsify H3.  
- *Suggests:* Run energy price sensitivity analysis.

---

## P4 – Divergence Mapping

| Hypothesis | Grok | ChatGPT | Gemini | Copilot | Claude | DeepSeek | Divergence Type |
|------------|------|---------|--------|---------|--------|----------|------------------|
| H1 | ✅ | ✅ | ✅ | ✅ | ✅ (cautious) | ✅ | **Convergence** |
| H2 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | 🚫 (refused) | ⚠️ | **Methodological** (Claude refusal) |
| H3 | ✅ | ✅ | ✅ | ✅ | ✅ (cautious) | ⚠️ (conditional) | **Substantive** (DeepSeek adds energy condition) |

**Divergence types:**
- **Substantive:** DeepSeek adds an energy price condition to H3.
- **Methodological:** Claude refuses H2 due to underspecification → treated as a meta‑signal.

---

## P5 – Weighted Synthesis (Human Operator)

**Convergences:** H1 confirmed by all models → low technical risk. H3 generally positive.

**Divergences handled:**  
- Claude’s refusal → **not ignored**: operator must define “major disruption” quantitatively.  
- DeepSeek’s energy condition → **integrated**: run energy price stress test.

**Synthesis statement (operator writes):**

> *“All models confirm technical feasibility (H1) and profitability under current energy prices (H3). Two critical uncertainties remain: (1) the operational definition of ‘major disruption’ for integration (H2), and (2) sensitivity of ROI to energy price spikes. Recommended action: proceed with a pilot study that measures downtime and models energy scenarios. Final decision after 6 months.”*

**Justification for deviation:** DeepSeek’s energy risk condition is adopted because it adds a falsifiable, externally verifiable criterion – strengthening the synthesis without bias.

---

## P6b – Power Layer (quick check)

- **Control:** Company, but dependent on external chip vendors.  
- **Access:** Requires internal data science competence.  
- **Profit:** Shareholders and management primarily.  
- **Risk:** Downtime borne by production staff; financial risk by company.  
→ No hidden asymmetry that invalidates the synthesis.

---

## P6 – External Validation (simulated)

Compared with industry reports (Fraunhofer 2025, McKinsey 2024):  
- H1: confirmed.  
- H2: underspecification correctly identified – no direct validation.  
- H3: positive in most scenarios except extreme energy price spikes.  
→ **No external contradiction.** Synthesis remains non‑falsified.

---

## P7 – Operator Reflection

1. **Which perspective dominated?**  
   Convergence on H1 and H3. I gave DeepSeek’s energy condition extra weight – justified because it adds testability.

2. **Which perspective was ignored – and why?**  
   Copilot’s competitor table was informative but not decisive – kept in appendix, not overridden.

3. **Which assumption remained unfalsified – and what would falsify it?**  
   Assumption of stable energy prices. A sustained 30 % spike over 6 months would falsify H3.

**Result:** Synthesis marked as “operator‑influenced but justified”.

---

## P8 – Versioned Archiving

All artefacts (prompt, raw responses, divergence table, synthesis, reflection) are committed to version control. This document is version 1.0 of this example run.

---

## What This Example Shows

- DNS does **not** produce a single “correct” answer.  
- It produces a **transparent, auditable map of uncertainty**.  
- The operator is **not a passive recipient** – they must justify every decision.  
- Refusals (Claude) and conditional warnings (DeepSeek) are **treated as signals**, not errors.

**This is how DNS works in practice.**
