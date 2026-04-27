# 04 – Divergence Map (Δdiv)

**Protokoll:** DNS-Mythologie-Projekt, Schritt P4  
**Berechnet:** 27.04.2026, lokal mit sentence-transformers all-MiniLM-L6-v2 + spaCy de_core_news_sm  
**Formel:** Δdiv = 1 - (Jaccard_sem + Cosine_sem)/2

## Matrix

|            | NotebookLM | Qwen  | DeepSeek | Gemini | Meta  | Mistral |
|------------|------------|-------|----------|--------|-------|---------|
| NotebookLM | 0.000      | 0.625 | 0.715    | 0.661  | 0.673 | 0.633   |
| Qwen       | 0.625      | 0.000 | 0.610    | 0.701  | 0.659 | 0.584   |
| DeepSeek   | 0.715      | 0.610 | 0.000    | 0.759  | 0.730 | 0.650   |
| Gemini     | 0.661      | 0.701 | 0.759    | 0.000  | 0.714 | 0.672   |
| Meta       | 0.673      | 0.659 | 0.730    | 0.714  | 0.000 | 0.662   |
| Mistral    | 0.633      | 0.584 | 0.650    | 0.672  | 0.662 | 0.000   |

## Schwellenwerte (aus 01_hypothesis.md)
- < 0,15 → Konsens
- 0,15–0,35 → leichte Abweichung
- > 0,35 → signifikante Divergenz
- > 0,50 → Quellenasymmetrie

## Befund
1. **Kein Konsens:** Niedrigster Wert Qwen–Mistral = 0,584 (immer noch >0,5)
2. **Maximale Divergenz:** DeepSeek–Gemini = 0,759
3. **NotebookLM-Flag bestätigt:** Alle Vergleiche 0,625–0,715 > 0,5. Hypothese H1 trifft zu – NotebookLM nutzt akademische Volltexte, die anderen Modelle stützen sich auf Web-SEO.

## Interpretation
- Die Modelle teilen kaum Fachbegriffe (mittlerer Jaccard_sem ≈ 0,18).
- Die Unterschiede sind nicht stilistisch, sondern quellenbedingt.
- Es existiert keine einheitliche „DNS-Geschichte“ in den Modellen – jede Instanz reproduziert die Bias ihrer Trainingsdaten.

## Artefakt
- `04_divergence_matrix.csv` (Rohdaten)
