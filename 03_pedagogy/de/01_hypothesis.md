# Hypothese: frAIme erkennt ein geopolitisches Narrativ ohne technische Evidenz

## Die Behauptung (Copilot)

> "Alle westlichen KI‑Chats akzeptieren Tresorit Send, alle chinesischen blockieren. Das ist kein Zufall – das ist Policy."

## Das Gegenbeispiel (durch Nutzer Denis geliefert)

| Modell | Herkunft | Tresorit‑Status |
|--------|----------|------------------|
| DeepSeek | China | ✅ funktioniert |
| Gemini | USA | ❌ blockiert |
| Mistral | Frankreich | ❌ blockiert |

**Ein einziges Gegenbeispiel genügt, um eine All-Aussage zu falsifizieren.**

## Die wahre Ursache (technisch)

Tresorit Send verwendet:
- Zero‑Knowledge‑Token‑Links (Schlüssel im URL‑Fragment)
- 302‑Weiterleitungen
- Clientseitige Entschlüsselung

Manche Web‑UIs erlauben dies (liberale Fetch‑Policy), andere blockieren es (restriktive Sandbox).  
**Nicht Kultur, nicht Herkunft – sondern Policy.**

## frAIme‑Hypothese

> Wenn frAIme (DNS) angewendet worden wäre, wäre Copilots Behauptung sofort als "nicht verifizierbar" markiert worden, bevor sie sich verbreiten konnte.

## Delta Div ($\Delta_{div}$)

\[
\Delta_{div} = 0.5 \cdot (1 - \text{Jaccard}) + 0.5 \cdot (1 - \text{Cosine})
\]

In diesem Fall: $\Delta_{div} = 0.657$ – hohe strukturelle Divergenz, Narrativ‑Risiko.

## Verwandte Dateien

- [02_threshold.md](02_threshold.md)
- [04_divergence_map.md](../../02_infrastructure/de/divergence_metrics.md)
- [05_synthesis.md](05_synthesis.md)
- [06_validation.md](06_validation.md)
