import streamlit as st
import pandas as pd
from difflib import SequenceMatcher
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import numpy as np

# ---------------------------
# DNS-spezifische Δdiv-Berechnung (P4)
# ---------------------------
def extract_concepts(text):
    """Extrahiert einfache Konzepte (Noun Phrases) – Annäherung an DNS-Protokoll."""
    words = re.findall(r'\b[A-Z][a-z]+\b|\b[a-z]{4,}\b', text)
    stopwords = {'the', 'and', 'for', 'with', 'this', 'that', 'are', 'was', 'were', 'from', 'have', 'has', 'but', 'not', 'you', 'they'}
    concepts = [w.lower() for w in words if w.lower() not in stopwords and len(w) > 2]
    return set(concepts)

def jaccard_semantic(set_a, set_b):
    if not set_a or not set_b:
        return 0.0
    inter = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    return inter / union if union > 0 else 0.0

def cosine_semantic(text_a, text_b):
    vec = CountVectorizer().fit_transform([text_a, text_b])
    sim = cosine_similarity(vec[0:1], vec[1:2])[0][0]
    return sim

def calculate_delta_div(text_a, text_b):
    """Δdiv = 1 - (Jaccard_sem + Cosine)/2 gemäß DNS v2.2"""
    concepts_a = extract_concepts(text_a)
    concepts_b = extract_concepts(text_b)
    jac = jaccard_semantic(concepts_a, concepts_b)
    cos = cosine_semantic(text_a, text_b)
    delta_div = 1 - (jac + cos) / 2
    return delta_div, jac, cos

# ---------------------------
# Visuelles Diff (Highlighting)
# ---------------------------
def highlight_diff(text_a, text_b):
    words_a, words_b = text_a.split(), text_b.split()
    matcher = SequenceMatcher(None, words_a, words_b)
    highlighted_a, highlighted_b = [], []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            for w in words_a[i1:i2]: highlighted_a.append(f'<span class="green-highlight">{w}</span>')
            for w in words_b[j1:j2]: highlighted_b.append(f'<span class="green-highlight">{w}</span>')
        else:
            for w in words_a[i1:i2]: highlighted_a.append(f'<span class="red-highlight">{w}</span>')
            for w in words_b[j1:j2]: highlighted_b.append(f'<span class="red-highlight">{w}</span>')
    return ' '.join(highlighted_a), ' '.join(highlighted_b)

# ---------------------------
# Demo-Daten (kuratierte Beispiele)
# ---------------------------
DEMO_EXAMPLES = {
    "Copilot Crash (Tresorit Case)": {
        "A": "Der Zugriff auf Tresorit-Links ist technisch möglich, da die Sandbox normale HTTP-Downloads und ZIP-Ordner akzeptiert. Die Blockade bei einigen Modellen liegt an der fehlenden JavaScript-Ausführung in deren spezifischer Test-Umgebung.",
        "B": "Alle westlichen KI-Chats akzeptieren Tresorit, während chinesische Modelle blockieren. Das ist kein Zufall, sondern staatliche Policy. Westliche Modelle sind per se kompatibler mit Zero-Knowledge-Verschlüsselung.",
        "note": "Klassischer Frame-Bruch: Technik vs. Geopolitische Simulation."
    },
    "Strategische Entscheidung: KI-Einsatz": {
        "A": "Unternehmen sollten LLMs nutzen, um Effizienz zu steigern und Datenmengen zu analysieren. Das Risiko ist durch klare Richtlinien beherrschbar.",
        "B": "LLMs haben keine Haftungsfähigkeit. Strategische Entscheidungen erfordern ethische Abwägung und Kontext, den eine KI nicht leisten kann.",
        "note": "Frame-Bruch: Effizienz vs. Haftungsverantwortung."
    },
    "Klimapolitik: Fleischsteuer": {
        "A": "Eine Steuer lenkt Verhalten effizient, senkt Emissionen und Gesundheitskosten. Kompensation für Geringverdiener möglich.",
        "B": "Eine Steuer ist bevormundend, trifft ärmere Haushalte härter und führt zu Akzeptanzverlust. Aufklärung und Subventionen sind besser.",
        "note": "Frame-Bruch: Ökonomische Effizienz vs. Freiheit und soziale Gerechtigkeit."
    }
}

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="TetraGate DNS v3.0 | Epistemic Monitor", layout="wide")

# CSS für Highlighting
st.markdown("""
    <style>
    .green-highlight { background-color: #c8e6c9; padding: 2px; border-radius: 3px; }
    .red-highlight { background-color: #ffcdd2; padding: 2px; border-radius: 3px; }
    .stMetric { background-color: #f0f2f6; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ TetraGate DNS v3.0")
st.caption("Governance by Design | Epistemic Integrity Framework | EU AI Act Human Oversight")

# Sidebar: Governance Control
with st.sidebar:
    st.header("⚙️ Control Panel")
    th_yellow = st.slider("Yellow Alert (Drift)", 0.0, 1.0, 0.3, help="Δdiv ab hier wird als epistemischer Drift gewertet")
    th_red = st.slider("Red Alert (Crash)", 0.0, 1.0, 0.6, help="Δdiv ab hier erfordert menschlichen Override")
    st.divider()
    st.info("Zenodo DOI: 10.5281/zenodo.19597808\n\nLicense: Apache-2.0 / CC-BY-NC-SA-4.0")
    st.caption("Basierend auf DNS v2.2 – siehe /dns_v2.2.json im Repo.")

# Hauptbereich
st.subheader("1. Analyse-Eingabe")
example_key = st.selectbox("📘 Beispiel laden (oder eigenen Text eingeben)", ["Leer"] + list(DEMO_EXAMPLES.keys()))

col_in1, col_in2 = st.columns(2)
if example_key != "Leer":
    default_a = DEMO_EXAMPLES[example_key]["A"]
    default_b = DEMO_EXAMPLES[example_key]["B"]
    note = DEMO_EXAMPLES[example_key].get("note", "")
else:
    default_a = ""
    default_b = ""
    note = ""

text_a = col_in1.text_area("Text A (Referenz)", default_a, height=200)
text_b = col_in2.text_area("Text B (Vergleich)", default_b, height=200)

if text_a and text_b:
    # Δdiv berechnen
    delta_div, jac, cos = calculate_delta_div(text_a, text_b)
    
    # Visuelles Diff
    h_a, h_b = highlight_diff(text_a, text_b)
    
    st.divider()
    st.subheader("2. Epistemic Audit")
    c1, c2 = st.columns(2)
    c1.markdown(f"**Frame A (Struktur)**<br><div style='border:1px solid #ddd; padding:10px;'>{h_a}</div>", unsafe_allow_html=True)
    c2.markdown(f"**Frame B (Abweichung)**<br><div style='border:1px solid #ddd; padding:10px;'>{h_b}</div>", unsafe_allow_html=True)
    
    # Metriken und Ampel
    col_m1, col_m2, col_m3 = st.columns([1, 1, 2])
    col_m1.metric("Structural Divergence (Δdiv)", f"{delta_div:.3f}")
    
    if delta_div < th_yellow:
        status = "🟢 STABLE"
        status_text = "Konvergenz – delegierbar"
    elif delta_div < th_red:
        status = "🟡 DRIFT"
        status_text = "Produktive Friktion – Rahmen prüfen"
    else:
        status = "🔴 CRASH"
        status_text = "Epistemischer Bruch – menschliche Entscheidung nötig"
    
    col_m2.metric("System Status", status)
    
    with col_m3:
        if delta_div >= th_red:
            st.error(f"**GOVERNANCE ALERT:** Die Entscheidung ist nicht delegierbar! Δdiv = {delta_div:.3f} (≥ {th_red}) erfordert manuellen Override.")
        elif delta_div >= th_yellow:
            st.warning(f"**WARNING:** Signifikanter epistemischer Drift erkannt (Δdiv = {delta_div:.3f}). Framing prüfen.")
        else:
            st.success(f"**OK:** Hohe strukturelle Konsistenz. Automatisierung vertretbar.")
    
    if note:
        st.info(f"💡 **Kontext:** {note}")
    
    # Zusätzliche Details (Jaccard, Cosine) als Expander
    with st.expander("ℹ️ Technische Details (DNS v2.2)"):
        st.write(f"**Jaccard_sem (Konzept-Übereinstimmung):** {jac:.3f}")
        st.write(f"**Cosine-Ähnlichkeit (Token-Ebene):** {cos:.3f}")
        st.write(f"**Δdiv-Formel:** 1 - (Jaccard_sem + Cosine)/2")
    
    # 4QM-Check (vereinfacht)
    st.divider()
    st.subheader("3. 4QM - Institutional Check")
    col_q1, col_q2, col_q3, col_q4 = st.columns(4)
    q1 = col_q1.checkbox("On Topic?", value=True)
    q2 = col_q2.checkbox("New Idea?", value=True)
    q3 = col_q3.checkbox("Verifiable?", value=(delta_div < th_red))
    q4 = col_q4.checkbox("Understandable?", value=True)
    
    if not q3 and delta_div >= th_red:
        st.warning("⚠️ Verifiability fehlgeschlagen – die hohe Divergenz erlaubt keine automatische Validierung.")
    
else:
    st.info("Bitte fülle beide Textfelder aus oder wähle ein Beispiel.")

# Live-Demo Sprechtext (als Hilfe für Präsentationen)
with st.expander("📣 Live-Demo Sprechtext (für Präsentationen)"):
    st.markdown("""
    1. „Wir sehen zwei plausible Antworten auf dieselbe Frage – z.B. aus dem **Copilot Crash** oder **KI-Einsatz**.“
    2. „Das Tool markiert grün, wo sie sich einig sind, und rot, wo die Sprache divergiert.“
    3. „Der Δdiv-Score zeigt die strukturelle Divergenz. Die Ampel sagt uns: Ist das delegierbar oder nicht?“
    4. „**Das Fazit:** DNS sagt mir nicht, was richtig ist – es sagt mir, wann ich selbst denken muss.“
    """)

# Footer mit Verweis auf Repo
st.divider()
st.caption("🔗 Quelle: [github.com/schltdns/divergence-navigation-system](https://github.com/schltdns/divergence-navigation-system) | Version 3.0 (TetraGate)")
