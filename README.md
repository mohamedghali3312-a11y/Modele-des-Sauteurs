# Le Modèle des Sauteurs — La Machine

**Statut :** `CI : PASSING` | **Preuves Formelles :** `Lean 4 (Mathlib)` | **Moteur :** `Python 3.11+ / gmpy2` | **Licence :** `MIT (2026)`

**Auteur :** Mohamed Ghali (2026)  
**Domaine :** Arithmétique primorielle, crible cinématique, conjecture de Goldbach, certification déterministe Lucas-Pocklington et modules post-quantiques NTT.

---

## 1. Vue d'ensemble du projet

**Le Modèle des Sauteurs** remplace le balayage séquentiel traditionnel par une **téléportation algébrique en mémoire O(1)** sur les roues primorielles \(V_k = \prod_{i=1}^k p_i\) :

* **Filtrage primoriel V₁₂ :** Élimination déterministe de **85,49 %** des entiers composés dès l'initialisation (V₁₂ = 7 420 738 134 810).
* **Isolation directe de Goldbach (N = P + Q) :** Paramétrisation symétrique autour du centre décalé C = (N - 2)/2 exploitant la résonance modulaire de Ramanujan.
* **Certification déterministe & SHA-256 :** Génération de témoins de primalité de **Lucas-Pocklington** (\(F > \sqrt{P}\)) et signature cryptographique des certificats JSON.
* **Modules Post-Quantiques NTT :** Génération directe des nombres premiers de Proth \(q_n = 2^n \cdot p_k + 1\) compatibles avec les transformées numériques rapides (incluant le module standard **ML-KEM** q₈ = 3 329 pour p₅ = 13).

**Documentation complète :** [Télécharger le Rapport Certifié (PDF)](Rapport_Certifie_Modele_des_Sauteurs.pdf)

---

## 2. Architecture du dépôt

```text
Modele-des-Sauteurs/
├── .github/workflows/ci.yml                # Pipeline CI automatique (Python + Lean 4)
├── jumper_model.py                         # Moteur principal en mémoire O(1)
├── machine_sauteurs_complete.py            # Moteur unifié (Goldbach, Machine v4.0, NTT)
├── visualisation_sauteurs.py               # Tracés graphiques (Onde de Ramanujan & sauts)
├── test_jumper_model.py                    # Suite de tests unitaires (pytest)
├── proofs.lean                             # Preuves formelles vérifiées sous Lean 4
├── lakefile.toml                           # Configuration du projet Lean 4 / Mathlib
├── lean-toolchain                          # Version du compilateur Lean (v4.12.0)
├── requirements.txt                        # Dépendances Python (pytest, gmpy2, matplotlib)
├── Rapport_Certifie_Modele_des_Sauteurs.pdf # Rapport scientifique et technique consolidé
└── LICENSE                                 # Licence MIT (Mohamed Ghali, 2026)
```

---

## 3. Démarrage rapide

### Installation et exécution Python
```bash
pip install -r requirements.txt
pytest -v
python jumper_model.py
python machine_sauteurs_complete.py
```

### Vérification formelle sous Lean 4
```bash
lake exe cache get
lake build
```
