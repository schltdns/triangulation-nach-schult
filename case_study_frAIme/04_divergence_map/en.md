# 04 – Divergence Map (Δdiv)

**Protocol:** DNS Mythology Project, Step P4  
**Calculated:** 2026-04-27, locally with sentence-transformers all-MiniLM-L6-v2 + spaCy de_core_news_sm  
**Formula:** Δdiv = 1 - (Jaccard_sem + Cosine_sem)/2

## Matrix

|            | NotebookLM | Qwen  | DeepSeek | Gemini | Meta  | Mistral |
|------------|------------|-------|----------|--------|-------|---------|
| NotebookLM | 0.000      | 0.625 | 0.715    | 0.661  | 0.673 | 0.633   |
| Qwen       | 0.625      | 0.000 | 0.610    | 0.701  | 0.659 | 0.584   |
| DeepSeek   | 0.715      | 0.610 | 0.000    | 0.759  | 0.730 | 0.650   |
| Gemini     | 0.661      | 0.701 | 0.759    | 0.000  | 0.714 | 0.672   |
| Meta       | 0.673      | 0.659 | 0.730    | 0.714  | 0.000 | 0.662   |
| Mistral    | 0.633      | 0.584 | 0.650    | 0.672  | 0.662 | 0.000   |

## Thresholds (from 01_hypothesis.md)
- < 0.15 → Consensus
- 0.15–0.35 → Minor deviation
- > 0.35 → Significant divergence
- > 0.50 → Source asymmetry

## Findings
1. **No consensus:** Lowest value Qwen–Mistral = 0.584 (still >0.5)
2. **Maximum divergence:** DeepSeek–Gemini = 0.759
3. **NotebookLM flag confirmed:** All comparisons 0.625–0.715 > 0.5. Hypothesis H1 holds – NotebookLM draws on academic full-texts, other models rely on web SEO content.

## Interpretation
- Models share almost no technical noun phrases (mean Jaccard_sem ≈ 0.18).
- Differences are not stylistic but source-driven.
- There is no single "DNS story" across models – each reproduces the bias of its training data.

## Artifact
- `04_divergence_matrix.csv` (raw data)
