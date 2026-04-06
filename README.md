# Triangulation nach Schult (v1.1‑Open)
**"Divergence is a signal, not noise."**  
A formal multi‑agent protocol for structured decision‑making and uncertainty mapping using Large Language Models (LLMs).  
**Divergence > Consensus.**

---

## 🎯 The Problem
Traditional AI consensus methods (voting, averaging, multi‑agent debate) aim for a single “correct” answer.  
But because LLMs share training data and alignment biases, **consensus often hides systemic errors**.

When multiple models confidently agree on a falsehood, the risk becomes invisible.

---

# 🚀 The Solution: Triangulation nach Schult (TNS)
The framework treats **dissonance, disagreement, drift, and even model refusal** as primary data points.  
It provides a **6‑phase operational protocol** to transform conflicting AI outputs into a structured, non‑falsified (within defined thresholds) human synthesis.

The method is:
- model‑agnostic  
- falsifiable  
- recursive  
- didactically applicable  
- open‑source  

---

# 🔬 Novelty Claim
Unlike classical triangulation, Delphi methods, or ensemble approaches,  
this framework does **not** aim to reduce disagreement.

Instead, it operationalizes divergence as a primary analytical signal through:
- role‑based multi‑agent decomposition  
- explicit falsification thresholds  
- structured divergence mapping  
- mandatory human synthesis with justification  

This combination does not exist in current AI evaluation or decision frameworks.

---

# 📊 Methodology Workflow (STM Integration)

The following diagram illustrates the iterative flow of the **Schult’s Triangulation Method (STM)**,  
highlighting the parallel processing layer and the central role of human synthesis.

```mermaid
graph TD
    %% Styling
    classDef stage fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef human fill:#e1f5fe,stroke:#01579b,stroke-width:2px,font-weight:bold;
    classDef models fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    %% Workflow
    Start((Start)) --> S1[Stage 1: Initialization]
    S1 --> S2[Stage 2: Role Assignment]
    
    subgraph Parallel_Processing [Multi-Agent Layer]
        S3[Stage 3: Parallel Multi-Agent Prompting]
        M1(Model A: Falsifier) -.-> S3
        M2(Model B: Historicator) -.-> S3
        M3(Model C: Structuralist) -.-> S3
    end

    S3 --> S4[Stage 4: Divergence Mapping]
    
    S4 --> S5[Stage 5: Human-in-the-Loop Synthesis]
    
    S5 --> S6[Stage 6: Epistemic Reflection]
    S6 --> End((Validated Insight))

    %% Assigning Classes
    class S1,S2,S4,S6 stage;
    class S5 human;
    class S3,M1,M2,M3 models;
