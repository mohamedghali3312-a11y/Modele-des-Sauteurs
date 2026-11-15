# Le Modèle des Sauteurs — La Machine (v7.0 à v13.0)
**The Jumper Model — The Machine (v7.0 to v13.0)**

**Auteur / Author :** Mohamed Ghali | **Année / Year :** 2026  
**Domaines / Fields :** Théorie algorithmique des nombres • Conjecture de Goldbach • Chaînes de Cunningham • Cryptographie Post-Quantique (ML-KEM) • Chiffrement Homomorphe (FHE)

---

## 🇫🇷 Présentation Générale (Français)

**« Le Modèle des Sauteurs — La Machine »** est une architecture mathématique et algorithmique conçue pour explorer les grands nombres premiers à très haute altitude ($10^{300}$ à $10^{2000}$) et auditer la sécurité des protocoles cryptographiques financiers sur un ordinateur personnel.

En combinant les **roues primorielles** ($V_k = \prod p_i$), la **symétrie miroir** ($r \leftrightarrow V_k - r$) et la **réduction télescopique** des quotients primoriels ($p_k = V_k / V_{k-1}$), ce système remplace le stockage de lourdes tables de crible par un filtrage algébrique en **mémoire constante $O(1)$**.

### Contributions et Résultats Clés (v13.0)
* **Filtrage Primoriel $O(1)$ & Certification Déterministe :** Utilisation d'un unique entier de 15 chiffres ($V_{12} = 304\,250\,263\,527\,210$) éliminant **85,49 %** des composés par PGCD avant le test Baillie-PSW, couplé à des preuves déterministes de **Lucas-Pocklington** exportées en certificats JSON signés (SHA-256).
* **Approche Algébrique de la Conjecture de Goldbach :**
  * Équation d'équilibre autour du centre décalé $\frac{N-2}{2} = A + B$ permettant l'isolation directe du facteur manquant : $p = \frac{\frac{N-2}{2} - B}{S}$.
  * Démonstration de la non-vacuité structurelle des couloirs miroirs ($C_k(N) \ge 1$) et vérification numérique de l'onde de résonance de Ramanujan ($905$ paires certifiées sur la crête $V_5 = 30\,030$ contre $244$ sur le plancher $2^{15}$).
* **Chaînes de Cunningham & Spirale d'Ulam :** Loi d'arrêt modulaire ($m \le q - 2$) permettant de construire des chaînes de Cunningham à 5 maillons par troncature haute au-dessus de $V_4$, et filtrage des diagonales quadratiques d'Euler.
* **Unification Post-Quantique (ML-KEM & FHE) au rang $n$ :** Généralisation $q_n = 2^n \left(\frac{V_k}{V_{k-1}}\right) + 1$ reliant le générateur $p_5 = V_5 / V_4 = 13$ au module premier **$q = 3\,329$** et à la racine primitive NTT **$\zeta = 17$** de ML-KEM-768, avec calcul du seuil de déclenchement du *Bootstrapping* FHE.

---

## 🇬🇧 Project Overview (English)

**"The Jumper Model — The Machine"** is a mathematical and software framework engineered to explore large prime numbers at extreme altitudes ($10^{300}$ to $10^{2000}$) and audit financial cryptographic shields on a standard personal computer.

By uniting **primorial wheels** ($V_k = \prod p_i$), **mirror symmetry** ($r \leftrightarrow V_k - r$), and the **telescoping reduction** of primorial quotients ($p_k = V_k / V_{k-1}$), this model eliminates memory-heavy sieve tables in favor of **constant $O(1)$ memory** algebraic filtering.

### Key Contributions & Verified Results (v13.0)
* **$O(1)$ Primorial Filtering & Deterministic Certification:** Uses a single 15-digit integer ($V_{12} = 304,250,263,527,210$) to filter out **85.49%** of composites via GCD prior to Baillie-PSW testing, paired with deterministic **Lucas-Pocklington** proofs exported as SHA-256 signed JSON certificates.
* **Algebraic Isolation for the Goldbach Conjecture:** Derives the shifted-center balance equation $\frac{N-2}{2} = A + B$ for direct factor isolation $p = \frac{\frac{N-2}{2} - B}{S}$, proving structural corridor non-emptiness ($C_k(N) \ge 1$) and verifying the Ramanujan resonance wave ($905$ pairs on $V_5 = 30,030$ vs. $244$ on $2^{15}$).
* **Post-Quantum Unification (ML-KEM & FHE) at Rank $n$:** Generalizes the generator equation to $q_n = 2^n \left(\frac{V_k}{V_{k-1}}\right) + 1$, proving that $p_5 = V_5 / V_4 = 13$ directly structures the prime modulus **$q = 3,329$** and primitive NTT root **$\zeta = 17$** of ML-KEM-768, alongside FHE *Bootstrapping* noise-budget modeling.

---

## 📂 Contenu du Dépôt / Repository Structure

* `Compte_Rendu_Complet_Modele_des_Sauteurs_2026.pdf` — Compte rendu technique intégral (FR) : théorie, démonstrations, graphiques et code.
* `The_Jumper_Model_Complete_Report_2026_EN.pdf` — Complete technical report (EN) : equations, numerical audits, and plots.
* `Recueil_Calculs_Detailles_Modele_des_Sauteurs_2026.pdf` — Recueil des démonstrations pas à pas et tableaux de vérification (FR).
* `la_machine_sauteurs_v13.py` — Moteur Python autonome (filtrage $V_{12}$, isolation Goldbach, certification JSON Lucas-Pocklington et NTT rang $n$).
* `requirements.txt` & `LICENSE` — Dépendances et licence libre MIT (Mohamed Ghali, 2026).

---

## 🚀 Démarrage Rapide / Quick Start

```bash
pip install -r requirements.txt
python la_machine_sauteurs_v13.py
```
