# The Jumper Model — La Machine (v7.0 to v13.0)

**Author:** Mohamed Ghali | **Year:** 2026  
**Fields:** Computational Number Theory, Post-Quantum Cryptography (ML-KEM), Fully Homomorphic Encryption (FHE)

---

## Project Overview

**"The Jumper Model — The Machine"** is a mathematical and software architecture designed to explore large prime numbers at extreme altitudes ($10^{300}$ to $10^{2000}$) and audit the resilience of modern cryptographic protocols on a standard personal computer.

By combining the arithmetic of **primorial wheels** ($V_k = \prod p_i$), **mirror symmetry** ($r \leftrightarrow V_k - r$), and the **telescoping reduction** of primorial quotients ($p_k = V_k / V_{k-1}$), this framework replaces memory-intensive sieve tables with algebraic filtering in **constant $O(1)$ memory**.

---

## Key Contributions & Verified Results

1. **$O(1)$ Primorial Filtering and Deterministic Certification:**
   * Leverages a single 15-digit integer ($V_{12} = 304,250,263,527,210$) to eliminate **85.49%** of composite numbers via a single GCD operation prior to running Baillie-PSW primality tests (reduced Fermat + strong Lucas).
   * Generates deterministic primality proofs via the **Lucas-Pocklington theorem**, exported as timestamped, SHA-256 signed JSON certificates verifiable offline.

2. **Algebraic Approach to the Goldbach Conjecture and Cunningham Chains:**
   * Formulates a balance equation around the shifted center $\frac{N-2}{2}$, enabling direct algebraic isolation of missing prime factors through exact integer division and GCD filtering.
   * Demonstrates the **structural non-emptiness of mirror corridors** ($C_k(N) \ge 1$) and numerically verifies the Ramanujan resonance wave ($905$ certified prime pairs on the $V_5 = 30,030$ peak versus $244$ on the $2^{15}$ floor).
   * Establishes a modular truncation law to construct uninterrupted **Cunningham chains** from high-altitude primorial quotients.

3. **Unification with Post-Quantum Cryptography (ML-KEM) and FHE:**
   * Generalizes the primorial generator equation to rank $n$ ($q_n = 2^n \frac{V_k}{V_{k-1}} + 1$), proving that the generator $p_5 = V_5 / V_4 = 13$ directly structures the prime modulus **$q = 3,329$** and the primitive NTT root **$\zeta = 17$** of the **ML-KEM** post-quantum standard.
   * Conducts a quantitative security audit against lattice attacks ($10^9$ transactions), confirming the security margin of **ML-KEM-768** ($2^{198.2}$ operations, mean vector angle $87.91^\circ$) in alignment with ANSSI/NIST guidelines, coupled with an **FHE engine (v13.0)** featuring automated noise-clearing via *Bootstrapping*.

---

## Repository Structure

```text
├── README.md
├── LICENSE
├── requirements.txt
├── src/
│   └── la_machine_sauteurs_v13.py
└── docs/
    ├── Compte_Rendu_Complet_Modele_des_Sauteurs_2026.pdf
    ├── Recueil_Calculs_Detailles_Modele_des_Sauteurs_2026.pdf
    └── The_Jumper_Model_Complete_Report_2026_EN.pdf
```

## Quick Start

```bash
# Run directly with standard Python 3 (zero external dependencies required)
python src/la_machine_sauteurs_v13.py

# Optional: install gmpy2 for C/GMP hardware acceleration at 10^300+
pip install -r requirements.txt
```
