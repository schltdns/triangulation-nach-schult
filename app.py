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
    vec = CountVectorizer().fit_transform([text_a, text_b])
    return cosine_similarity(vec[0:1], vec[1:2])[0][0]

def calculate_delta_div(text_a, text_b):
    concepts_a = extract_concepts(text_a)
    concepts_b = extract_concepts(text_b)
    jac = jaccard_semantic(concepts_a, concepts_b)
    cos = cosine_semantic(text_a, text_b)
    return 1 - (jac + cos) / 2, jac, cos

def get_ampel_state(delta):
    if delta < 0.3:
        return "🟢 GRÜN", "#2ecc71", "Delegierbar – du darfst die Antwort übernehmen."
    elif delta < 0.6:
        return "🟡 GELB", "#f1c40f", "Denkpunkt – prüfe Annahmen oder fordere ein Gegenbeispiel."
    else:
        return "🔴 ROT", "#e74c3c", "Nicht delegierbar – du musst selbst entscheiden."

# ---------------------------
# Session State
# ---------------------------
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'last_operator' not in st.session_state:
    st.session_state.last_operator = ""
if 'last_bot' not in st.session_state:
    st.session_state.last_bot = ""
if 'ack_required' not in st.session_state:
    st.session_state.ack_required = False
if 'ack_done' not in st.session_state:
    st.session_state.ack_done = False

st.set_page_config(page_title="DNS Chat – Ampelgestützte Entscheidungsfindung", layout="wide")
st.title("🧭 DNS Chat – Ampelgestützte Entscheidungsfindung")
st.caption("Die Ampel läuft im Hintergrund. Bei Gelb oder Rot musst du quittieren, bevor du weitermachst.")

# ---------------------------
# Sidebar mit didaktischer Hilfe
# ---------------------------
with st.sidebar:
    st.markdown("### 🧠 Didaktische Ampel")
    st.markdown("""
    - **🟢 GRÜN:** Delegierbar – du darfst die Antwort übernehmen.
    - **🟡 GELB:** Denkpunkt – Vorsicht, prüfe Annahmen oder fordere ein Gegenbeispiel.
    - **🔴 ROT:** Nicht delegierbar – du musst selbst entscheiden. Die KI kann dir die Verantwortung nicht abnehmen.
    """)
    st.divider()
    st.caption("DNS v2.2 | Δdiv = 0.5*(1-Jaccard_sem)+0.5*(1-Cosine)")

# ---------------------------
# Chat-Verlauf anzeigen
# ---------------------------
st.subheader("📜 Gesprächsverlauf")
for op, bot in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(op)
    with st.chat_message("assistant"):
        st.write(bot)

# ---------------------------
# Eingabebereich
# ---------------------------
with st.container():
    new_prompt = st.text_area("Deine Nachricht an den DNS-Chatbot:", key="input_prompt", height=100)
    
    st.markdown("**Antwort des DNS-Chatbots (simuliert – du trägst sie ein oder nutzt ein Beispiel):**")
    bot_response = st.text_area("Antwort:", key="bot_response", height=150)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📘 Beispiel 'Copilot Crash' (roter Fall)"):
            st.session_state.input_prompt = "Why do some AI models block Tresorit links while others accept them?"
            st.session_state.bot_response = "All Western AI chatbots accept Tresorit, while Chinese models block it. This is not a coincidence but state policy."
            st.rerun()
    with col2:
        if st.button("🧹 Chat löschen"):
            st.session_state.chat_history = []
            st.session_state.ack_required = False
            st.session_state.ack_done = False
            st.rerun()

# ---------------------------
# Ampel und Quittierung
# ---------------------------
if new_prompt and bot_response:
    delta, jac, cos = calculate_delta_div(new_prompt, bot_response)
    ampel_text, ampel_color, ampel_hint = get_ampel_state(delta)
    
    # Ampel als farbige Box
    st.markdown(f"""
    <div style="background-color:{ampel_color}20; padding:10px; border-left: 8px solid {ampel_color}; border-radius:8px; margin:10px 0">
    <strong>{ampel_text}</strong> – Δdiv = {delta:.3f} (Jaccard_sem={jac:.2f}, Cosine={cos:.2f})<br>
    <span style="font-size:0.9em">{ampel_hint}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Quittierungspflicht bei Gelb oder Rot
    if delta >= 0.3:
        st.session_state.ack_required = True
        if not st.session_state.ack_done:
            st.warning("⚠️ Die Ampel ist nicht grün. Du musst die Situation quittieren, bevor du die Nachricht zum Verlauf hinzufügen kannst.")
            if st.button("✅ Quittieren & weiter"):
                st.session_state.ack_done = True
                st.rerun()
        else:
            st.success("✅ Quittiert. Du kannst die Nachricht nun zum Verlauf hinzufügen.")
    else:
        st.session_state.ack_required = False
        st.session_state.ack_done = False
else:
    st.info("Bitte beide Texte eingeben (deine Nachricht und die Bot-Antwort).")

# ---------------------------
# Hinzufügen zum Verlauf (nur wenn keine Quittung nötig oder quittiert)
# ---------------------------
if new_prompt and bot_response:
    if (st.session_state.ack_required and st.session_state.ack_done) or (not st.session_state.ack_required):
        if st.button("📨 Nachricht zum Verlauf hinzufügen"):
            st.session_state.chat_history.append((new_prompt, bot_response))
            # Eingabefelder leeren
            st.session_state.input_prompt = ""
            st.session_state.bot_response = ""
            st.session_state.ack_done = False
            st.rerun()
