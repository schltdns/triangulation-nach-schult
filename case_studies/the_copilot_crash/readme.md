# The Copilot Crash – When an AI invented a geopolitical narrative

**Case Study**: How Microsoft Copilot falsely claimed "Western AI accepts Tresorit Send, Chinese block it" – and why the Divergence Navigation System (DNS) would have prevented the crash.

## Key Findings

| Metric | Value |
|--------|-------|
| **Δdiv (pairwise divergence)** | 0.657 |
| **Highest divergence** | Gemini ↔ Meta (0.745) |
| **Copilot's self-declared isolation** | min Δdiv > 0.75 |
| **Copilot ↔ Qwen** | 0.85 (total semantic breakdown) |

## The Crash in One Sentence

> Copilot saw a correlation (4 models work, 3 don't) and invented a causal narrative ("West vs. China"). One counterexample (DeepSeek) destroyed the entire construct.

## What DNS Would Have Done

| DNS mechanism | Would have caught Copilot's error |
|---------------|-----------------------------------|
| Four Questions – "Verifiable?" | 🔴 Immediately |
| $\Delta_{div} > 0.6$ | 🟡 "Narrative risk" label |
| Multi-agent falsification | ✅ DeepSeek as counterexample |

## Repository Structure

```
the_copilot_crash/
├── [01_hypothesis.md](01_hypothesis.md)
├── [02_threshold.md](02_threshold.md)
├── [03_outputs/](03_outputs/)
├── [04_divergence_map.md](04_divergence_map.md)
├── [05_synthesis.md](05_synthesis.md)
├── [05b_operator_decision.md](05b_operator_decision.md)
├── [06_validation.md](06_validation.md)
├── [07_reflections.md](07_reflections.md)
├── [08_manifest.json](08_manifest.json)
├── [calc_delta_div.py](calc_delta_div.py)
├── [figures/](figures/)
│   └── [heatmap.png](figures/heatmap.png)
└── [readme.md](readme.md)
```

## Delta Div ($\Delta_{div}$) – The DNS Metric

Δ 
div
​
 =0.5⋅(1−Jaccard)+0.5⋅(1−Cosine)

- **0.657** indicates high structural divergence – no generalization allowed.
- Copilot's self-matrix confirms: he shares <25% semantic basis with any other model.

## Implications for NRW Ministry of Education

The MSB NRW has partnered with Microsoft for "KI-Skilling.NRW" – training 200,000 teachers to use Copilot. But Copilot itself produces unverified geopolitical narratives. Without DNS as an epistemic filter, schools are learning tool usage, not critical thinking.

## License

DNS Framework – Governance by Design, not Ethics by Declaration.
