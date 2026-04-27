
---

### 4. `01_governance/en/minimal_safety_layer.md`

```markdown
# minimal_safety_layer.py – Explanation

This script implements the **DNS Safety Layer** logic for frAIme V1.0.0.

## Core Functions

- **`create_log_entry()`** – Creates a tamper‑proof log entry from the four‑questions answers.  
  Automatically maps to EU AI Act: Art. 13 (transparency), Art. 14 (human oversight), Art. 9 (risk management).
- **`hash_entry()`** – Computes a SHA256 hash of the entire log entry. Any change afterwards invalidates the hash.
- **`build_merkle_root()`** – Condenses a list of hashes into a single Merkle root (e.g., for daily integrity proofs).
- **Cross‑Language Integrity Check** – Checks whether LaTeX formulas in German and English Markdown files are identical.  
  Run with `python minimal_safety_layer.py --all`

## Usage in the frAIme Workflow

1. **AI generates** a statement / prediction.
2. **Human** answers the four questions (by clicking).
3. **Safety Layer** creates log, hash, and optionally a Merkle root.
4. **System** stores log and hash in a database.

The human does not write long protocols – they only validate. The rest happens automatically.

## Example Calls

```bash
python minimal_safety_layer.py --all                     # Checks all case study files
python minimal_safety_layer.py de/file.md en/file.md     # Checks a single pair
