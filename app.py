import streamlit as st
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# ---------------------------
# Lade semantisches Modell (einmalig)
# ---------------------------
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

def semantic_similarity(text_a, text_b):
    emb_a = model.encode([text_a])[0]
    emb_b = model.encode([text_b])[0]
    # Cosine-Ähnlichkeit zwischen den Vektoren
    sim = np.dot(emb_a, emb_b) / (np.linalg.norm(emb_a) * np.linalg.norm(emb_b))
    return float(sim)

def calculate_delta_div(text_a, text_b):
    # Nur semantische Ähnlichkeit (kein Jaccard mehr – der ist zu oberflächlich)
    cos = semantic_similarity(text_a, text_b)
    # Δdiv = 1 - cos (wir könnten auch andere Metriken mischen, aber cos reicht für Didaktik)
    delta = 1 - cos
    return delta, 0.0, cos  # Jaccard nicht mehr verwendet

def get_ampel_state(delta):
    if delta < 0.3:
        return "🟢", "#2ecc71", "Delegierbar"
    elif delta < 0.6:
        return "🟡", "#f1c40f", "Denkpunkt"
    else:
        return "🔴", "#e74c3c", "Nicht delegierbar"

# Der Rest der App (Chat-Verlauf, UI) bleibt gleich, nur die Berechnung wird ersetzt.
# Siehe unten die vollständige Datei.
