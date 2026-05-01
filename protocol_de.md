frAIme Protokoll (P1–P8)
Ein reproduzierbarer, auditierbarer Workflow für Argumentations-Drift

frAIme strukturiert, wie heterogene Modelle (S1–Ω) und der Mensch zusammenarbeiten, um epistemische Unsicherheit sichtbar zu machen. Domänen-agnostisch.

frAIme sucht keinen Konsens — es kartiert wo und warum Modelle divergieren.

🧭 Übersicht
P1 – Hypothese

P2 – Schwellenwerte

P3 – Sammeln

P4 – Divergenz-Karte

P5 – Synthese

P5b – Operator-Entscheidung

P6 – Validierung

P6b – Power Layer

P7 – Reflexion

P8 – Versionierung

P1 – Hypothese
Falsifizierbare Frage definieren.

Scope, Annahmen, Domäne

Output: 01_hypothesis.md

P2 – Schwellenwerte
Falsifikationskriterien festlegen.

Δdiv-Grenzwerte, Widerspruchs-Flags

Output: 02_thresholds.md

P3 – Sammeln
Identischen Prompt über S1–Ω laufen lassen.

keine Cross-Kontamination, Single-Turn

Output: 03_outputs/S1.md … 03_outputs/Omega.md

optional: 03_outputs/graph.png (bei Bedarf)

P4 – Divergenz-Karte
frAIme berechnet Divergenz:

4.1 Semantische Divergenz (Δdiv) / drift
Δdiv = 1 − (Jaccard_sem + Cosine) / 2
*(entspricht der gemittelten Jaccard- und Kosinus-Distanz: 0,5·(1−Jaccard_sem) + 0,5·(1−Cosine), was mathematisch identisch ist)*

wobei:

Jaccard_sem = |Konzepte(A) ∩ Konzepte(B)| / |Konzepte(A) ∪ Konzepte(B)|

Cosine = Embedding-Ähnlichkeit

Interpretation:

Δdiv < 0,3 → niedriger drift

0,3–0,6 → mittlerer drift

0,7 → hoher drift

case_study_frAIme: Δdiv 0,584–0,759

Output: 04_divergence_map.md, heatmap.png

P5 – Synthese
Integration mit Vier Fragen.

Output: 05_synthesis.md

P5b – Operator-Entscheidung
Mensch gewichtet und begründet.

Output: 05b_operator_decision.md

P6 – Validierung
Abgleich mit Literatur.

Output: 06_validation.md

P6b – Power Layer
Wer profitiert / trägt Risiko.

Output: 06b_power_layer.md

P7 – Reflexion
Bias dokumentieren.

Output: 07_reflection.md

P8 – Versionierung
Archivierung mit Versionstag.

Output: 08_manifest_de.json, 08_manifest_en.json

Die neue Hauptformel Δdiv = 1 − (Jaccard_sem + Cosine) / 2 ist kompakter und zeigt sofort, dass Divergenz der Abstand zur maximal möglichen Ähnlichkeit ist. Der Klammerzusatz bewahrt die didaktisch wertvolle Erklärung, dass beide Metriken gleichgewichtet als Distanzen eingehen. So ist die Definition sowohl für schnelle Leser als auch für tiefere Analyse klar.
