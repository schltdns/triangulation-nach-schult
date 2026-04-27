#!/usr/bin/env python3
"""
minimal_safety_layer.py – frAIme V1.0.0 Safety Layer

Features:
- Four questions → AI Act mapping → hash chain
- Cross-language integrity check (LaTeX formulas in de/en .md files)
- Merkle root for daily batch integrity
"""

import hashlib
import json
import re
import os
from datetime import datetime, timezone
from typing import List, Tuple

# ---------- Core safety layer functions ----------

def create_log_entry(prognose_id, answers, dissent=None):
    """Create a log entry with AI Act mapping."""
    entry = {
        "prognose_id": prognose_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "session_hash": hashlib.sha256(b"frAIme_salt").hexdigest()[:16],
        "fragen": answers,
        "ai_act_mapping": {
            "art_13_transparenz": not answers.get("thema_getroffen", True),
            "art_14_human_oversight": dissent is not None,
            "art_9_risikomanagement": answers.get("ueberpruefbar", False)
        }
    }
    if dissent:
        entry["dissent_log"] = dissent
    return entry

def hash_entry(entry):
    """Create SHA256 hash of the JSON entry."""
    entry_str = json.dumps(entry, sort_keys=True)
    return hashlib.sha256(entry_str.encode()).hexdigest()

def build_merkle_root(hashes):
    """Build Merkle root from list of hashes (simplified)."""
    if not hashes:
        return None
    while len(hashes) > 1:
        if len(hashes) % 2:
            hashes.append(hashes[-1])
        hashes = [hashlib.sha256((h1 + h2).encode()).hexdigest()
                  for h1, h2 in zip(hashes[::2], hashes[1::2])]
    return hashes[0]

# ---------- Cross‑language integrity check ----------

def extract_latex_formulas(text: str) -> List[str]:
    """Extract all LaTeX formulas (inline $...$, display $$...$$, \[...\])."""
    formulas = []
    # Display math: $$ ... $$
    formulas.extend(re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL))
    # Display math: \[ ... \]
    formulas.extend(re.findall(r'\\\[(.*?)\\\]', text, re.DOTALL))
    # Inline math: $ ... $ (avoid $$)
    formulas.extend(re.findall(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', text, re.DOTALL))
    # Normalize whitespace
    return [re.sub(r'\s+', ' ', f.strip()) for f in formulas]

def check_language_integrity(de_path: str, en_path: str, verbose: bool = True) -> Tuple[bool, str]:
    """Compare LaTeX formulas between German and English markdown files."""
    if not os.path.exists(de_path):
        return False, f"German file not found: {de_path}"
    if not os.path.exists(en_path):
        return False, f"English file not found: {en_path}"
    with open(de_path, 'r', encoding='utf-8') as f:
        de_text = f.read()
    with open(en_path, 'r', encoding='utf-8') as f:
        en_text = f.read()
    de_formulas = extract_latex_formulas(de_text)
    en_formulas = extract_latex_formulas(en_text)
    if de_formulas == en_formulas:
        if verbose:
            print(f"✅ OK: {os.path.basename(de_path)} ↔ {os.path.basename(en_path)} ({len(de_formulas)} formulas)")
        return True, "Formulas match."
    else:
        if verbose:
            print(f"❌ MISMATCH: {os.path.basename(de_path)} ↔ {os.path.basename(en_path)}")
            print(f"   DE: {de_formulas}")
            print(f"   EN: {en_formulas}")
        return False, f"Formulas differ: DE {de_formulas} vs EN {en_formulas}"

def validate_all_case_study_files(base_path: str = "../03_pedagogy") -> bool:
    """Validate all .md files in de/ vs en/ under base_path."""
    de_dir = os.path.join(base_path, "de")
    en_dir = os.path.join(base_path, "en")
    if not os.path.exists(de_dir) or not os.path.exists(en_dir):
        print("❌ Could not find de/ and en/ subdirectories.")
        return False
    files = [f for f in os.listdir(de_dir) if f.endswith('.md') and f != 'README.md']
    all_ok = True
    for fname in files:
        de_file = os.path.join(de_dir, fname)
        en_file = os.path.join(en_dir, fname)
        if not os.path.exists(en_file):
            print(f"⚠️ Skipping {fname}: English version missing.")
            continue
        ok, _ = check_language_integrity(de_file, en_file, verbose=True)
        all_ok = all_ok and ok
    if all_ok:
        print("\n✅ All case study files passed cross‑language integrity test.")
    else:
        print("\n❌ Some files have formula mismatches. Review above.")
    return all_ok

# ---------- Example / CLI ----------
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        check_language_integrity(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2 and sys.argv[1] == "--all":
        validate_all_case_study_files("../03_pedagogy")
    else:
        print("Usage:")
        print("  python minimal_safety_layer.py <de_file> <en_file>")
        print("  python minimal_safety_layer.py --all")
        print("\nRunning original demo (log entry & merkle root):\n")
        answers = {
            "thema_getroffen": True,
            "neue_idee": "voll",
            "ueberpruefbar": True,
            "verstaendlich": True
        }
        dissent = {
            "kategorie": "fehlender_kontext",
            "begruendung": "Die KI kennt die lokalen Schulschließungen nicht." * 3
        }
        entry = create_log_entry("demo-001", answers, dissent)
        print("Log Entry:", json.dumps(entry, indent=2))
        h = hash_entry(entry)
        print("SHA256 Hash:", h)
        daily_hashes = [h, "abc123", "def456"]
        merkle_root = build_merkle_root(daily_hashes)
        print("Merkle Root (daily batch):", merkle_root)
