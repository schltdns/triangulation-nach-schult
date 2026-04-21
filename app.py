import streamlit as st
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# NLTK Daten einmalig herunterladen
@st.cache_resource
def download_nltk_data():
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('punkt_tab', quiet=True)
    return stopwords.words('english'), WordNetLemmatizer()

stop_words, lemmatizer = download_nltk_data()

def preprocess(text):
    # Kleinschreibung, Tokenisierung, Stoppwort-Entfernung, Lemmatisierung
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return ' '.join(words)

def semantic_similarity(text_a, text_b):
    # TF-IDF + Cosine auf vorverarbeiteten Texten
    pre_a = preprocess(text_a)
    pre_b = preprocess(text_b)
    if not pre_a or not pre_b:
        return 0.0
    vectorizer = TfidfVectorizer().fit_transform([pre_a, pre_b])
    return cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]

def calculate_delta_div(text_a, text_b):
    cos = semantic_similarity(text_a, text_b)
    return 1 - cos, 0.0, cos

def get_ampel_state(delta):
    if delta < 0.3:
        return "🟢", "#2ecc71", "Delegierbar"
    elif delta < 0.6:
        return "🟡", "#f1c40f", "Denkpunkt"
    else:
        return "🔴", "#e74c3c", "Nicht delegierbar"
