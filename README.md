DNS — Divergence Navigation System
![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19597808.svg)
DNS does not reduce uncertainty — it makes it visible.
A divergence-based evaluation layer for epistemic uncertainty in multi-model systems.
DNS transforms model disagreement into structured epistemic insight — not to find truth,
but to reveal systemic weaknesses in AI reasoning, safety, and governance.
It is a domain-agnostic evaluation layer that:
detects epistemic friction
reveals blind spots
supports transparent human-in-the-loop synthesis
DNS is not a truth machine — it is a systemic weakness detector for AI safety, governance, and research.
Versioning and Open Data Proof
Current version: v2.1 (published 2026-04-15)  
DOI: 10.5281/zenodo.19597808
Previous version: v2.0  
DOI: 10.5281/zenodo.19513073
IPFS anchor: `bafkreiblue2cs6e4xmpbpklkswimpzgnoumszgkvcm5csukdiqhqkf7wyy`  
See `dns_open_data_proof.json` for CID + SHA256
Attribution & License
DNS uses dual licensing to protect both code and method:
Code components (JSON schema, Python reference implementation): Apache License 2.0 — see LICENSE-CODE.txt
Documentation, method, teaching materials (whitepaper, PDFs, teaching): CC BY-NC-SA 4.0 — see LICENSE-DOCS.txt
You are free to use, modify and integrate the code commercially under Apache-2.0.  
For any public use of the method, derivative work, product integration, research paper or commercial application, please include clear attribution:
> "Divergence Navigation System (DNS)" by Denis Schult  
> GitHub: https://github.com/schltdns/divergence-navigation-system  
> Whitepaper: https://doi.org/10.5281/zenodo.19597808
Thank you for respecting the origin of the framework.
🧭 What DNS Is (Overview)
DNS is a divergence-sensitive epistemic protocol that uses multi-model disagreement as a navigational signal.
It enables:
structured analysis under uncertainty
adversarial triangulation across heterogeneous models
detection of bias, drift, and alignment tunneling
quantifiable uncertainty signals (Δdiv)
psychologically safe exploration (low-social-risk environments)
transparent human synthesis (operator-in-the-loop)
Full conceptual description: 👉 HOW_IT_WORKS.md
🎯 Why DNS matters for AI safety & governance
DNS is Governance by Design, not just Ethics by Declaration.
Modern LLMs often exhibit false consensus due to shared training data and alignment. DNS exposes this by measuring semantic dispersion across models.
DNS provides:
Δdiv (Semantic Dispersion) — proxy for epistemic uncertainty
Friction mapping — identifies contested domains
Human-in-the-loop synthesis — the operator decides, not the system
Auditability — relevant for safety, compliance, and regulated industries (EU AI Act Art. 9, 13, 14, 15)
Use cases:
AI safety & interpretability
Model comparison & evaluation
Governance & risk documentation
Research on epistemic uncertainty
📊 Core Metric: Divergence Delta (Δdiv)
DNS measures epistemic friction, not correctness.
Domain Type	Δdiv (observed)	Epistemic Profile
Formal Logic	~0.05	Convergent
Applied Systems	~0.40–0.55	Structured Divergence
Complex Systems	~0.65–0.80	Contested / High Uncertainty
Full benchmark: 👉 BENCHMARK.md
📖 DNS Standard Glossary & Methodological Provenance
To ensure methodological clarity and provenance, DNS uses a specific terminology:
Δdiv (Delta Divergence): The mathematical quantification of semantic disagreement between n model outputs. Δdiv = 1 - (Jaccard + Cosine Similarity)/2 (simplified example)
Epistemic Navigation Layer: The operative space where a human operator interacts with model divergence to produce validated insight.
P1–P8 Protocol: The standardized 8-step sequence that transforms divergence into a verified synthesis.
Four Questions Method: The operational frontend for learners (topic, novelty, verifiability, understandability).
Safety Layer: EU AI Act-compliant backend with bias detection, formal dissent, and hash-anchored audit trail.
Full glossary: 👉 MATH_AND_GLOSSARY.md
⚠️ Guardrails
Low Δdiv ≠ Truth — may indicate alignment tunneling
High Δdiv ≠ Error — indicates competing valid perspectives
DNS measures dispersion, not correctness — it is an uncertainty signal
🧠 Operator Principle
"DNS does not tell us what is true — it shows where models stop agreeing."
DNS is a human-centered protocol. The operator remains the final synthesizer.
📜 DNS Protocol
Reproducible 8-phase workflow (P1–P8): 👉 protocol.md
🧮 Mathematical Foundations
Formal definitions and glossary: 👉 MATH_AND_GLOSSARY.md
Example full run (P1–P8): 👉 EXAMPLE_RUN.md
📦 Case Studies
Cognitive Safety & Neurodiversity 👉 case_study_cognitive_safety.md
Labor Market 2030 👉 case_study_labour_market_2030.md
Energy Market Dynamics 👉 case_study_energy.md
🔧 Operationalization (v2.1)
New in v2.1:
Four Questions Method – learner flyer: `vier_fragen_methode.pdf`
AI Act mapping – legal mapping: `mapping_ai_act.pdf`
Safety Layer schema v2 – `safety_layer_schema_v2.json`
Reference implementation – `minimal_safety_layer.py`
Operationalization Report – OPERATIONALIZATION_REPORT.md
🔗 Related Work
Detailed positioning: 👉 related_works.md
DNS is an evaluation layer, not a replacement.
📂 Repository Structure
```
divergence-navigation-system/
├── README.md
├── BENCHMARK.md
├── OPERATIONALIZATION_REPORT.md
├── LICENSE-CODE.txt
├── LICENSE-DOCS.txt
├── dns_open_data_proof.json
├── safety_layer_schema_v2.json
├── minimal_safety_layer.py
├── docs/
│   ├── EXAMPLE_RUN.md
│   ├── HOW_IT_WORKS.md
│   └── MATH_AND_GLOSSARY.md
├── protocol/
│   └── protocol.md
├── case_studies/
│   ├── case_study_cognitive_safety.md
│   ├── case_study_labour_market_2030.md
│   └── case_study_energy.md
├── teaching/
│   ├── vier_fragen_methode.pdf
│   └── mapping_ai_act.pdf
└── whitepaper/
```
🚀 Quick Start
Read BENCHMARK.md (Δdiv logic)
Read HOW_IT_WORKS.md for the workflow
Read OPERATIONALIZATION_REPORT.md for the practical method
Run your own mini-benchmarks with your models
DNS requires no installation — it is a human-centered protocol.
✍️ Author & Citation
Denis Schult  
Independent Researcher, Germany  
GitHub: https://github.com/schltdns
Please cite as:
> Schult, D. (2026). DNS — Divergence Navigation System (v2.1). Zenodo. https://doi.org/10.5281/zenodo.19597808
