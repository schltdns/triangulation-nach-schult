<p align="center">
  <img src="docs/assets/frAIme_final.png" alt="frAIme – just before decision" width="650"/>
</p>

<h1 align="center">frAIme</h1>

<p align="center">
🟢 Topic consistency • 🟡 Idea emergence • 🔴 Verifiability • 🔵 Understandability
</p>

<p align="center">
<a href="https://doi.org/10.5281/zenodo.19793185">https://doi.org/10.5281/zenodo.19793185</a>
</p>

**frAIme makes uncertainty visible – it creates the framework for reliable AI use.**
frAIme is Governance by Design, not ethics by declaration.

For classrooms: four questions, traffic light, done.  
For research: measurable divergence (drift), auditable.

**Version:** V1.0.0 (2026-04-26) – Stable Release

---

## Start in 2 Minutes
**The Four Questions Method**
Check every LLM answer:

1. On topic? 🟢 / 🔴
2. New idea? 🟢 / 🟡 / 🔴
3. Verifiable? (number, date, place, if-then) 🟢 / 🔴
4. Understandable? 👍 / 👎

Good answer = 🟢 + 👍

No account. No API. Works on paper.

## What's New in V1.0.0
1. **Rebranding:** formerly DNS – now frAIme (Epistemic Governance Framework)
2. **Validated:** case_study_frAIme shows drift 0.584–0.759 despite apparent consensus
3. **Reach:** 6,946 clones / 1,914 unique cloners in 14 days

## Case Study: AI Learning vs Frontal Teaching

- **6 models, same question:** "Is AI learning more efficient?"
- **Four Questions:** all 🟢 on "On topic", all 👍 on "Understandable" – apparent consensus
- **drift matrix:** 0.584–0.759 – high divergence despite agreement
    - DeepSeek–Gemini: 0.759
    - DeepSeek–Meta: 0.730
    - NotebookLM–DeepSeek: 0.715
    - Qwen–Mistral: 0.584 (lowest)
- **Triangulation:**
        - Harvard RCT 2025 (n=194): Median 4.5 vs 3.5, Time 49 vs 60 min – CONFIRMED
        - Turkey UPenn 2024 (n=1,000): +48% exercises / −17% test – CONFIRMED
        - Kulik & Fletcher 2016: +0.66 SD – CONFIRMED
- **Insight:** High drift did not mean "wrong", but "source-poor". Only one cluster provided primary data.

**frAIme lesson:** Plausibility ≠ Evidence. drift localizes verification need.

## Technology
**drift = Δdiv = 1 - (Jaccard_sem + Cosine) / 2**
= 0.5·(1−Jaccard_sem) + 0.5·(1−Cosine)

Thresholds (from P2):
- <0.15 = Consensus
- 0.15–0.35 = slight deviation
- >0.35 = significant divergence
- >0.50 = source asymmetry
- >0.70 = blind spot

case_study_frAIme: all 15 pairs >0.50 → 100% source asymmetry

Two layers: Frontend (Four Questions) + Backend (Safety Layer, Hash Anchor, Multi-Agent Log)

## Method: frAIme Protocol (P1–P8)

frAIme adapts and extends established methods for analyzing epistemic uncertainty:

- **P1 Hypothesize** → `01_hypothesis.md`
- **P2 Thresholds** → `02_thresholds.md`
- **P3 Outputs** → `03_outputs/S1.md … S6.md`, `03_outputs/graph.png` (X/Y MDS plot)
- **P4 Map Divergence** → `04_divergence_map.md`, `heatmap.png`
- **P5 Synthesis** → `05_synthesis.md`
- **P5b Operator Decision** → `05b_operator_decision.md`
- **P6 Validation** → `06_validation.md`
- **P6b Power Layer** → `06b_power_layer.md`
- **P7 Reflection** → `07_reflection.md`
- **P8 Versioning** → `08_manifest_en.json` / `08_manifest_de.json`

- Like Delphi, frAIme structures multi-agent input via isolated prompts (P3) and synthesis (P5).
- Like MCDA, frAIme uses weighted aggregation, but weights come from divergence metrics.
- Like Structured Expert Judgment, frAIme calibrates contributions, but uses semantic drift and external validation.
- Unlike consensus methods, frAIme maps divergence as signal (P4).
- New: (1) graph-based information flow analysis (X/Y plot), (2) Power Layer check (P6b).
- Reproducibility through versioned artifacts (P8).
