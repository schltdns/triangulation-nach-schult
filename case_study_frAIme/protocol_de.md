# frAIme Protokoll (P1–P8) – case_study_frAIme

**Reproduzierbarer Workflow für Argumentations-Drift**

frAIme sucht keinen Konsens — es kartiert wo und warum Modelle divergieren.

## P1 – Hypothese
**Datei:** `01_hypothesis.md`

Frage: Wie divergieren sechs heterogene LLMs (NotebookLM, Qwen, DeepSeek, Gemini, Meta, Mistral) beim identischen frAIme-Prompt?

## P2 – Schwellenwerte
**Datei:** `02_thresholds.md`

Aus Hypothese:
## Δdiv / drift Interpretation (canonical)

| Wertebereich | Label | Handlungsempfehlung |
|-------------|-------|-------------------|
| < 0,15 | Konsens | Keine weitere Prüfung nötig |
| 0,15–0,35 | Leichte Abweichung | Kontext prüfen, dokumentieren |
| 0,35–0,50 | Signifikante Divergenz | Externe Validierung (P6) anstoßen |
| 0,50–0,70 | Quellenasymmetrie | Power Layer Check (P6b) aktivieren |
| > 0,70 | Epistemischer blinder Fleck | F1-Trigger: DeepSeek-Intervention + Operator-Eskalation |

## P3 – Outputs
**Ordner:** `03_outputs/`

Sechs Single-Turn-Outputs ohne Cross-Kontamination:
- S1.md … S6.md
- `graph.png` → X/Y-MDS-Plot der Δdiv-Matrix

## P4 – Divergenz-Karte
**Dateien:** `04_divergence_map.md`, `heatmap.png`

Δdiv = 1 − (Jaccard_sem + Cosine)/2 = 0,5·(1−Jaccard_sem)+0,5·(1−Cosine)
drift = Δdiv

**Ergebnisse case_study_frAIme:**
- DeepSeek–Gemini: 0,759
- DeepSeek–Meta: 0,730
- NotebookLM–DeepSeek: 0,715
- Qwen–Mistral: 0,584 (niedrigster Wert)
- Alle 15 Paare >0,50 → 100% Quellenasymmetrie

## P5 – Synthese
**Datei:** `05_synthesis.md`

## P5b – Operator-Entscheidung
**Datei:** `05b_operator_decision.md`

## P6 – Validierung
**Datei:** `06_validation.md`

## P6b – Power Layer
**Datei:** `06b_power_layer.md`

## P7 – Reflexion
**Datei:** `07_reflection.md`

## P8 – Versionierung
**Dateien:** `08_manifest_de.json`, `08_manifest_en.json`
