#!/usr/bin/env python3
"""
calc_delta_div.py – Δdiv Berechnung für frAIme V1.0.0

Berechnet die paarweise Divergenz zwischen Modell-Antworten.
Δdiv = 0.5 * (1 - Jaccard) + 0.5 * (1 - Cosine)

Usage:
    python calc_delta_div.py --file responses.json
"""

import json
import argparse
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def jaccard_similarity(text1, text2):
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())
    if not set1 or not set2:
        return 0.0
    return len(set1 & set2) / len(set1 | set2)

def calculate_delta_div(responses):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(responses)
    n = len(responses)
    if n < 2:
        return 0.0
    total = 0.0
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            cos_sim = cosine_similarity([embeddings[i]], [embeddings[j]])[0][0]
            jac_sim = jaccard_similarity(responses[i], responses[j])
            delta = 0.5 * (1 - jac_sim) + 0.5 * (1 - cos_sim)
            total += delta
            pairs += 1
    return total / pairs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='JSON file with "responses" array')
    args = parser.parse_args()
    with open(args.file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    texts = [item['text'] for item in data['responses']]
    delta = calculate_delta_div(texts)
    print(f"Δdiv = {delta:.4f}")

if __name__ == '__main__':
    main()
