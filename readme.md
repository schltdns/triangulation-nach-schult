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

**frAIme macht Unsicherheit sichtbar – es schafft den Rahmen für verlässliche KI-Nutzung.**
frAIme ist Governance by Design, nicht Ethik per Deklaration.

Für Klassenzimmer: vier Fragen, Ampel, fertig.  
Für Forschung: messbare Divergenz (drift), auditierbar.

**Version:** V1.0.0 (2026-04-26) – Stable Release

---

## Start in 2 Minuten
**Die Vier-Fragen-Methode**
Prüfe jede LLM-Antwort:

1. On topic? 🟢 / 🔴
2. Neue Idee? 🟢 / 🟡 / 🔴
3. Verifizierbar? (Zahl, Datum, Ort, wenn-dann) 🟢 / 🔴
4. Verständlich? 👍 / 👎

Gute Antwort = 🟢 + 👍

Kein Account. Keine API. Funktioniert auf Papier.

## Was ist neu in V1.0.0
1. **Rebranding:** früher DNS – jetzt frAIme (Epistemic Governance Framework)
2. **Validiert:** case_study_frAIme zeigt drift 0,584–0,759 trotz scheinbarem Konsens
3. **Reichweite:** 6.946 Clones / 1.914 Unique Cloner in 14 Tagen

## Case Study: KI-Lernen vs Frontalunterricht

- **6 Modelle, gleiche Frage:** „Ist KI-Lernen effizienter?“
- **Vier Fragen:** alle 🟢 bei „On topic“, alle 👍 bei „Verständlich“ – scheinbarer Konsens
- **drift-Matrix:** 0,584–0,759 – hohe Divergenz trotz Einigkeit
    - DeepSeek–Gemini: 0,759
    - DeepSeek–Meta: 0,730
    - NotebookLM–DeepSeek: 0,715
    - Qwen–Mistral: 0,584 (niedrigster Wert)
- **Triangulation:**
        - Harvard RCT 2025 (n=194): Median 4,5 vs 3,5, Zeit 49 vs 60 Min – BESTÄTIGT
        - Türkei UPenn 2024 (n=1.000): +48 % Übungen / −17 % Test – BESTÄTIGT
        - Kulik & Fletcher 2016: +0,66 SD – BESTÄTIGT
- **Erkenntnis:** Hoher drift zeigte nicht „falsch“, sondern „quellenarm“. Nur ein Cluster lieferte Primärdaten.

**frAIme-Lektion:** Plausibilität ≠ Evidenz. drift lokalisiert Prüfbedarf.

## Technik
**drift = Δdiv = 1 - (Jaccard_sem + Cosine) / 2**
= 0,5·(1−Jaccard_sem) + 0,5·(1−Cosine)

Grenzwerte (aus P2):
- <0,15 = Konsens
- 0,15–0,35 = leichte Abweichung
- >0,35 = signifikante Divergenz
- >0,50 = Quellenasymmetrie
- >0,70 = blinder Fleck

case_study_frAIme: alle 15 Paare >0,50 → 100 % Quellenasymmetrie

Zwei Ebenen: Frontend (Vier Fragen) + Backend (Safety Layer, Hash-Anker, Multi-Agent-Log)

## Methode: frAIme Protocol (P1–P8)

frAIme adaptiert und erweitert etablierte Verfahren zur Analyse epistemischer Unsicherheit:

- **P1 Hypothesize** → `01_hypothesis.md`
- **P2 Thresholds** → `02_thresholds.md`
- **P3 Outputs** → `03_outputs/S1.md … S6.md`, `03_outputs/graph.png` (X/Y-MDS-Plot)
- **P4 Map Divergence** → `04_divergence_map.md`, `heatmap.png`
- **P5 Synthesis** → `05_synthesis.md`
- **P5b Operator Decision** → `05b_operator_decision.md`
- **P6 Validation** → `06_validation.md`
- **P6b Power Layer** → `06b_power_layer.md`
- **P7 Reflection** → `07_reflection.md`
- **P8 Versioning** → `08_manifest_de.json` / `08_manifest_en.json`

- Wie Delphi strukturiert frAIme Multi-Agenten-Input über isolierte Prompts (P3) und Synthese (P5).
- Wie MCDA nutzt frAIme gewichtete Aggregation, Gewichte kommen aber aus Divergenz-Metriken.
- Wie Structured Expert Judgment kalibriert frAIme Beiträge, nutzt aber semantischen Drift und externe Validierung.
- Anders als Konsensmethoden kartiert frAIme Divergenz als Signal (P4).
- Neu sind: (1) graphbasierte Informationsfluss-Analyse (X/Y-Plot), (2) Power Layer Check (P6b).
- Reproduzierbarkeit durch versionierte Artefakte (P8).
