# 01 – Hypothese & Falsifikation

## Kontext
In diesem Lauf wurden 7 identische Prompts an 6 Modelle gestellt. NotebookLM hatte ausschließlich Zugriff auf frAIme/DNS-Quellen. Qwen, DeepSeek, Gemini, Meta und Mistral hatten Zugriff auf KMK, UNESCO, OECD, Schulbarometer, AKTIV, PAIR und weitere.

## Hypothese H1
Ein Sprachmodell mit einseitig beschränkter Quellenbasis (nur frAIme) produziert Antworten, die systematisch von Modellen mit breiter Quellenbasis abweichen. Erwartete Divergenz: Δdiv > 0,5.

## Hypothese H2
Die Abweichung beruht nicht auf faktischen Fehlern, sondern auf epistemischem Bias – einer strukturellen Perspektivverengung.

## Hypothese H3
Wird die Quellenasymmetrie aufgehoben, sinkt Δdiv messbar.

## Falsifikationskriterien
1. Δdiv NotebookLM ↔ alle anderen < 0,3 → kein Bias
2. NotebookLM konvergiert mit mindestens zwei anderen Modellen (Δdiv < 0,4)
3. Die Divergenz lässt sich durch nachweisbare Faktfehler in NotebookLM erklären
4. Externe Gutachter bewerten die Quellentiefe von NotebookLM als gleichwertig
