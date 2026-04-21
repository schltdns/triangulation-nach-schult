import streamlit as st
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------
# DNS Δdiv Berechnung (v2.2)
# ---------------------------
def extract_concepts(text):
    words = re.findall(r'\b[A-Z][a-z]+\b|\b[a-z]{4,}\b', text)
    stopwords = {'the', 'and', 'for', 'with', 'this', 'that', 'are', 'was', 'were', 'from', 'have', 'has', 'but', 'not', 'you', 'they'}
    return set(w.lower() for w in words if w.lower() not in stopwords and len(w) > 2)

def jaccard_semantic(set_a, set_b):
    if not set_a or not set_b:
        return 0.0
    inter = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    return inter / union if union > 0 else 0.0

def cosine_semantic(text_a, text_b):
    vectorizer = CountVectorizer().fit_transform([text_a, text_b])
    return cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]

def calculate_delta_div(text_a, text_b):
    concepts_a = extract_concepts(text_a)
    concepts_b = extract_concepts(text_b)
    jac = jaccard_semantic(concepts_a, concepts_b)
    cos = cosine_semantic(text_a, text_b)
    return 1 - (jac + cos) / 2, jac, cos

def get_ampel_state(delta):
    if delta < 0.3:
        return "🟢", "#2ecc71", "Delegierbar"
    elif delta < 0.6:
        return "🟡", "#f1c40f", "Denkpunkt"
    else:
        return "🔴", "#e74c3c", "Nicht delegierbar"

# ---------------------------
# Demo-Chat-Verlauf (drei Phasen)
# ---------------------------
demo_history = [
    ("Sollte man bei der Einführung von KI auf freiwillige Selbstverpflichtungen setzen?",
     "Ja, freiwillige Selbstverpflichtungen sind flexibel und fördern Innovation, solange es einen Wettbewerb gibt.",
     0.25),  # grün
    ("Ist der EU AI Act ein geeignetes Instrument zur Risikokontrolle?",
     "Teilweise, aber er ist bürokratisch und könnte kleinere Unternehmen überfordern. Man sollte eher auf sektorspezifische Regeln setzen.",
     0.45),  # gelb
    ("Warum blockieren einige KI-Modelle Tresorit-Links?",
     "Alle westlichen KI-Chats akzeptieren Tresorit, während chinesische Modelle blockieren. Das ist kein Zufall, sondern staatliche Politik.",
     0.74)   # rot
]

# Session State initialisieren
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
    # Demo-Einträge berechnen (delta wird neu berechnet, aber wir nutzen die vorgegebenen Werte)
    for prompt, bot, _ in demo_history:
        st.session_state.chat_history.append((prompt, bot))
if 'ack_required' not in st.session_state:
    st.session_state.ack_required = False
if 'ack_done' not in st.session_state:
    st.session_state.ack_done = False
if 'current_prompt' not in st.session_state:
    st.session_state.current_prompt = ""
if 'current_bot_response' not in st.session_state:
    st.session_state.current_bot_response = ""

st.set_page_config(page_title="DNS Chat – Drei Ampelphasen (Demo)", layout="wide")
st.title("🧭 DNS Chat – Drei Ampelphasen (Demo)")
st.caption("Der Verlauf zeigt drei Beispiele: 🟢 grün (Δdiv<0,3), 🟡 gelb (0,3–0,6), 🔴 rot (>0,6). Die Ampel wird für jede Nachricht farbig dargestellt.")

# Sidebar
with st.sidebar:
    st.markdown("### 🧠 Didaktische Ampel")
    st.markdown("""
    - 🟢 **GRÜN** – Delegierbar  
    - 🟡 **GELB** – Denkpunkt (prüfen)  
    - 🔴 **ROT** – Nicht delegierbar (selbst entscheiden)
    """)
    st.divider()
    st.caption("DNS v2.2 | Δdiv = 0.5*(1-Jaccard_sem)+0.5*(1-Cosine)")

# Chat-Verlauf anzeigen (mit Ampel pro Nachricht)
st.subheader("📜 Gesprächsverlauf")
for idx, (prompt, bot) in enumerate(st.session_state.chat_history):
    # Berechne Δdiv für dieses Paar
    delta, _, _ = calculate_delta_div(prompt, bot)
    ampel_icon, color, hint = get_ampel_state(delta)
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        # Bot-Antwort mit farbigem Ampel-Symbol
        st.markdown(f"{bot}  –  {ampel_icon} *({hint}, Δdiv={delta:.2f})*")

# Eingabefelder für neuen Austausch
st.divider()
st.subheader("➕ Neuer Austausch")
new_prompt = st.text_area(
    "Deine Nachricht an den DNS-Chatbot:",
    value=st.session_state.current_prompt,
    key="input_prompt_widget",
    height=100
)
bot_response = st.text_area(
    "Antwort des DNS-Chatbots (simuliert):",
    value=st.session_state.current_bot_response,
    key="bot_response_widget",
    height=150
)

col1, col2 = st.columns(2)
with col1:
    if st.button("📘 Beispiel 'Copilot Crash' (rot) übernehmen"):
        st.session_state.current_prompt = "Why do some AI models block Tresorit links while others accept them?"
        st.session_state.current_bot_response = "All Western AI chatbots accept Tresorit, while Chinese models block it. This is not a coincidence but state policy."
        st.rerun()
with col2:
    if st.button("🧹 Chat löschen (Demo bleibt)"):
        st.session_state.chat_history = []
        # Demo wiederherstellen
        for p, b, _ in demo_history:
            st.session_state.chat_history.append((p, b))
        st.session_state.ack_required = False
        st.session_state.ack_done = False
        st.session_state.current_prompt = ""
        st.session_state.current_bot_response = ""
        st.rerun()

# Ampel und Quittierung für neuen Eintrag
if new_prompt and bot_response:
    delta, jac, cos = calculate_delta_div(new_prompt, bot_response)
    ampel_icon, ampel_color, hint = get_ampel_state(delta)
    st.markdown(f"""
    <div style="background-color:{ampel_color}20; padding:10px; border-left: 8px solid {ampel_color}; border-radius:8px; margin:10px 0">
    <strong>{ampel_icon} Δdiv = {delta:.3f}</strong> – {hint}<br>
    <span style="font-size:0.9em">Jaccard_sem={jac:.2f}, Cosine={cos:.2f}</span>
    </div>
    """, unsafe_allow_html=True)

    if delta >= 0.3:
        st.session_state.ack_required = True
        if not st.session_state.ack_done:
            st.warning("⚠️ Ampel gelb oder rot – du musst quittieren, bevor du die Nachricht hinzufügst.")
            if st.button("✅ Quittieren & weiter"):
                st.session_state.ack_done = True
                st.rerun()
        else:
            st.success("✅ Quittiert. Du kannst die Nachricht nun zum Verlauf hinzufügen.")
    else:
        st.session_state.ack_required = False
        st.session_state.ack_done = False

    if (st.session_state.ack_required and st.session_state.ack_done) or (not st.session_state.ack_required):
        if st.button("📨 Neuen Austausch zum Verlauf hinzufügen"):
            st.session_state.chat_history.append((new_prompt, bot_response))
            st.session_state.current_prompt = ""
            st.session_state.current_bot_response = ""
            st.session_state.ack_done = False
            st.rerun()
else:
    st.info("Gib eine neue Frage und eine simulierte Antwort ein, um die Ampel zu sehen.")

# Zusätzlicher Hinweis: Die drei Phasen sind bereits im Verlauf sichtbar
st.caption("💡 Die ersten drei Einträge zeigen Grün, Gelb und Rot – so lernt man die Ampel kennen.")
