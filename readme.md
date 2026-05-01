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
- **Triangulation:**
    - Harvard RCT 2025 (n=194): Median 4,5 vs 3,5, Zeit 49 vs 60 Min – BESTÄTIGT
    - Türkei UPenn 2024 (n=1.000): +48 % Übungen / −17 % Test – BESTÄTIGT
    - Kulik & Fletcher 2016: +0,66 SD – BESTÄTIGT
- **Erkenntnis:** Hoher drift zeigte nicht „falsch“, sondern „quellenarm“. Nur ein Cluster lieferte Primärdaten.

**frAIme-Lektion:** Plausibilität ≠ Evidenz. drift lokalisiert Prüfbedarf.

## Technik
drift = 1 - (Jaccard_sem + Cosine) / 2

Grenzwerte:
- <0,3 = Konvergenz
- 0,3–0,6 = produktive Reibung
- >0,7 = blinder Fleck

Zwei Ebenen: Frontend (Vier Fragen) + Backend (Safety Layer, Hash-Anker, Multi-Agent-Log)

## Methode: frAIme

frAIme adaptiert und erweitert etablierte Verfahren zur Analyse epistemischer Unsicherheit:

- Wie Delphi strukturiert frAIme Multi-Agenten-Input über isolierte Prompts (P3) und Synthese (P5).
- Wie MCDA nutzt frAIme gewichtete Aggregation, Gewichte kommen aber aus Divergenz-Metriken.
- Wie Structured Expert Judgment kalibriert frAIme Beiträge, nutzt aber semantischen Drift und externe Validierung.
- Anders als Konsensmethoden kartiert frAIme Divergenz als Signal (P4).
- Neu sind: (1) graphbasierte Informationsfluss-Analyse, (2) Power Layer Check (P6b).
- Reproduzierbarkeit durch versionierte Artefakte (P8).
