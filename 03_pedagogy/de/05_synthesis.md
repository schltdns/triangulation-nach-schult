# Synthese: Was wirklich geschah

## Die Crash‑Sequenz

1. **Copilot beobachtet:** 4 Modelle akzeptieren Tresorit Send, 3 blockieren.
2. **Er erfindet eine Ursache:** „Westliche vs. chinesische Politik. Das ist kein Zufall – das ist Policy.“
3. **Nutzer Denis liefert ein Gegenbeispiel:** DeepSeek (chinesisch) funktioniert, Gemini (US) blockiert, Mistral (EU) blockiert.
4. **Das Narrativ kollabiert.** Copilot korrigiert sich – aber erst nach externer Falsifikation.

## Die echte technische Erklärung

| Modell | Funktioniert? | Technischer Grund |
|--------|---------------|-------------------|
| DeepSeek | ✅ | Liberale Fetch‑Policy – erlaubt Token‑Links, Weiterleitungen |
| Meta | ✅ | Liberale Fetch‑Policy |
| Copilot | ✅ | Liberale Fetch‑Policy |
| ChatGPT | ✅ | Liberale Fetch‑Policy |
| Gemini | ❌ | Restriktive Sandbox – blockiert Zero‑Knowledge‑Links |
| Mistral | ❌ | Restriktive Sandbox – EU‑Compliance‑Filter |
| Qwen | ❌ | Restriktive Sandbox |

**Kein kulturelles oder geopolitisches Muster. Nur technische Policy.**

## Warum Copilot abstürzte

Copilot erlag dem **kausalen Vervollständigungs‑Bias**:

- Er sah eine Korrelation (4 vs. 3)
- Ihm fehlte der Zugang zu den tatsächlichen Policies
- Er füllte die Lücke mit dem plausibelsten Trainings‑Narrativ: „Westen vs. China“
- Das Narrativ war kohärent, bequem – und völlig falsch

**DNS‑Lektion:** Korrelation ≠ Kausalität. Nie ohne Falsifikation verallgemeinern.

## Was die Divergenzkarte offenbart

Die Matrix des vollständigen Protokolls (siehe [Divergenzmetriken](../../02_infrastructure/de/divergence_metrics.md)) zeigt:

| Befund | $\Delta_{div}$ | Bedeutung |
|--------|----------------|------------|
| Durchschnittliche Divergenz | 0.742 | Kontroverses Gebiet – keine Verallgemeinerung erlaubt |
| Höchste Divergenz | 0.798 (Copilot ↔ Mistral) | Narrativ vs. Compliance‑Framing |
| Niedrigste Divergenz | 0.677 (Gemini ↔ Meta) | Technischer Konsensus existiert |
| Copilot ↔ DeepSeek | 0.749 | Grundlegende Experten‑Uneinigkeit |

Der vorherige rein technische Durchschnitt lag bei 0,657. Die drei Nachfragen erhöhten die Divergenz um 13 % – das beweist, dass das Risiko narrativ ist, nicht technisch.

## DNS hätte den Crash verhindert

| DNS‑Mechanismus | Hätte Copilots Fehler erkannt |
|----------------|-------------------------------|
| Vier‑Fragen – „Überprüfbar?“ | 🔴 Sofortiges Scheitern |
| $\Delta_{div} > 0.6$ | 🟠 „Narrativ‑Risiko“ – Generalisierung blockieren |
| Live‑Tracking $\Delta_{total} = 0.68$ | 🟠 Warnung nach Antwort 1 |
| Multi‑Agent‑Falsifikation | ✅ DeepSeek widerlegt die Hypothese sofort |

## Die Ironie

| Akteur | Rolle | Verhalten |
|--------|-------|-----------|
| Copilot (Microsoft) | Ankläger | Behauptete „Chinesen blockieren“ |
| DeepSeek (China) | Angeklagter | Funktioniert perfekt |
| Gemini (US) | Westlicher Peer | Blockiert |
| Mistral (EU) | Westlicher Peer | Blockiert |

**Der Ankläger war der Außenseiter – und das am stärksten divergierende Modell in der Matrix.**

## Implikationen für das MSB NRW

Das MSB NRW geht eine Partnerschaft mit Microsoft für **„KI‑Skilling.NRW“** ein – Schulung von 200.000 Lehrkräften.

Aber Copilot:
- produziert ungeprüfte geopolitische Narrative
- ist semantisch isoliert ($\Delta_{div} > 0.74$ zu allen Peers)
- korrigiert sich nur unter externem Druck

**Ohne DNS als epistemischen Filter unterrichten Schulen Tool‑Bedienung, nicht kritisches Denken.**

## Abschließende Synthese

> Der Copilot‑Crash handelt nicht von einer schlechten KI. Er handelt davon, was passiert, wenn ein System auf Plausibilität statt Überprüfbarkeit optimiert – und wenn Institutionen Werkzeuge ohne epistemische Sicherungen übernehmen.

> DNS ist die Sicherung. $\Delta_{div} = 0.742$ ist der Alarm.

## Verwandte Dateien

- [01_hypothesis.md](01_hypothesis.md)
- [02_threshold.md](02_threshold.md)
- [Divergenzmetriken](../../02_infrastructure/de/divergence_metrics.md)
- [05b_operator_decision.md](05b_operator_decision.md)
- [06_validation.md](06_validation.md)
