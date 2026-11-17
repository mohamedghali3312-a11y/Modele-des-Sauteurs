# Le Modèle des Sauteurs (*The Jumper Model*)

![Vérification CI](https://github.com)

**Auteur :** Mohamed Ghali (2026)  
**Licence :** MIT

Ce dépôt présente une implémentation algorithmique et une vérification formelle dédiées à l'arithmétique des roues primorielles, à la recherche paramétrique de paires de Goldbach et à la génération de nombres premiers de Proth compatibles avec les transformations NTT (*Number Theoretic Transform*).

---

## 1. Architecture du projet

* **`jumper_model.py`** : Moteur principal en Python (compatible `gmpy2` pour l'arithmétique multiprécision rapide).
* **`test_jumper_model.py`** : Suite de tests unitaires automatisés (`pytest`).
* **`proofs.lean`** : Vérification formelle sous **Lean 4** (avec `Mathlib`) des identités algébriques sous-jacentes au paramétrage des candidats.
* **`docs/Livre_Blanc_Modele_des_Sauteurs.pdf`** : Livre blanc technique et mathématique consolidé.
* **`LICENSE`** : Licence libre MIT.

---

## 2. Fondements mathématiques et méthodologie

### A. Filtrage par roue primorielle en mémoire auxiliaire $O(1)$
Au lieu de stocker un tableau de cribles en mémoire vive (comme le crible d'Ératosthène classique), l'algorithme génère des sauts arithmétiques basés sur les primorielles $V_k = \prod_{i=1}^k p_i$ (notamment $V_4 = 2310$ et $V_{12}$). Le filtrage préalable par PGCD ($\gcd(x, V_{12}) = 1$) élimine la majorité des entiers composés avant tout test de primalité.

### B. Paramétrage de Goldbach et certification de Pocklington
Pour un entier pair $N = 2C + 2$, le modèle explore les progressions arithmétiques de pas $S$ (un produit de petits premiers impairs) selon l'identité algébrique :

$$P_m + Q_m = \big(2S(K - m) + 1\big) + \big(2(r + mS) + 1\big) = N$$

Lorsqu'un couple $(P, Q)$ passe les tests de primalité (Miller-Rabin déterministe 12 bases sous $3.18 \times 10^{23}$, ou Baillie-PSW via `gmpy2` au-delà), un témoin $a$ de **Pocklington** est calculé pour $P = 2Sp + 1$ en vérifiant la condition théorique $F = \prod q_i > \sqrt{P}$.

### C. Génération de nombres premiers de Proth pour NTT
Le module `generer_module_ntt_rang_n` recherche des nombres premiers de la forme $q_n = 2^n \cdot p_k + 1$ et calcule une racine primitive $2^n$-ième de l'unité $\zeta_n \pmod{q_n}$. Ces paramètres sont adaptés aux transformations rapides sur corps fini (NTT) utilisées dans les algorithmes sur réseaux euclidiens (tels que ML-KEM ou Falcon-1024).

---

## 3. Vérification formelle (Lean 4)

Le fichier `proofs.lean` prouve formellement deux lemmes structurels :
1. **`goldbach_parametric_identity`** : Invariance de la somme $P_m + Q_m = N$ le long des sauts de pas $S$.
2. **`cunningham_link_formula`** : Relation de récurrence algébrique $2x_m + 1 = x_{m+1}$ générant les candidats des chaînes de Cunningham de première espèce.

---

## 4. Installation et exécution

```bash
# Exécution avec Python standard
python3 jumper_model.py

# Recommandé pour les grands entiers (10^100 et plus) : installation de gmpy2
pip install gmpy2
python3 jumper_model.py
```
