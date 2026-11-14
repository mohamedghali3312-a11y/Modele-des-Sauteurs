# Modele-des-Sauteurs# 🔢 Le Modèle des Sauteurs & Exploration Cryptographique (1024D)

**De l'intuition arithmétique sur feuille de brouillon à l'implémentation d'algorithmes haute performance pour les grands nombres premiers et la cryptographie post-quantique.**

---

## 🎯 À propos du projet

Ce dépôt rassemble mes recherches personnelles et mes expérimentations algorithmiques en **Python** autour de deux grands piliers des mathématiques appliquées et de la cybersécurité :

1. **Volet I — Le Modèle des Sauteurs & La Machine v4.0 (Nombres Premiers) :**
   Modélisation cinématique du crible d'Ératosthène permettant d'explorer la distribution des nombres premiers en mémoire constante $O(1)$ jusqu'à l'échelle cryptographique ($10^{500}$), d'analyser leurs fréquences cachées (FFT) et de certifier des nombres de Mersenne.
2. **Volet II — Cryptographie Post-Quantique & Optimisation sur Réseaux Euclidiens ($512 = 2^9$ et $1024 = 2^{10}$) :**
   Implémentation d'une Transformée Théorique des Nombres (**NTT** modulo $3329$) et conception de stratégies géométriques pour accélérer la réduction de réseaux (**Tri croissant + Effet Domino**, **Effet Miroir bidirectionnel**, **Tournoi par blocs** et **Indexation par Bibliothèque Numérotée**).

---

## 🚀 Résultats & Performances Mesurées

### 1. Exploration des Grands Nombres Premiers (Machine v4.0)
* **Filtrage géométrique par Roues Primorielles :** Élimination de **79,2 %** des composés avec la *Roue +2310* ($V_5$) et **80,82 %** avec la *Roue +30030* ($V_6$) avant tout test de primalité.
* **Validation statistique à $10^{20}$ :** Extraction de **9 982 nombres premiers** (saut moyen mesuré : `46,28` contre `46,05` théorique, soit **99,5 % d'adéquation**) et vérification empirique du biais de répulsion modulaire (*Lemke Oliver–Soundararajan*).
* **Haute altitude & Constellations :** Capture de **33 chaînes de Cunningham** (longueur 3) à $10^{50}$ en `7,82 s`, extraction d'un nombre premier certifié de **501 chiffres** ($10^{500}$) en `1,53 s`, et certification déterministe de nombres de Mersenne jusqu'à **6 533 chiffres** ($M_{21701}$) via le test de **Lucas-Lehmer**.

### 2. Cryptographie Post-Quantique & Réduction de Réseaux ($1024 = 2^{10}$)
* **Moteur NTT rapide ($p = 3329$) :** Multiplication polynomiale en **1024 dimensions** ($4 \times 256$) exécutée en **7,35 ms** sans erreur d'arrondi.
* **Optimisation LLL Bidirectionnelle (Domino + Miroir) :** Réduction de **44,7 %** du temps de calcul en 30D par rapport à LLL classique.
* **Indexation par Bibliothèque Numérotée & Triée (1024D) :** Regroupement spatial par composante dominante (`argmax`) et tri local permettant de traiter une matrice de **1 048 576 coefficients** en **18,4 ms** (72× plus rapide qu'un découpage par blocs fixes).

---

## 📂 Contenu du Dépôt

* `Modele_des_Sauteurs_Machine_v4_Edition_Integrale.pdf` : Dossier technique complet (Introduction, théorie, graphiques expérimentaux et codes sources).
* `machine_v4_sauteurs.py` : Extraction haute altitude (Roue +30030, PGCD primoriel, Miller-Rabin) et analyse spectrale FFT.
* `ntt_post_quantique_1024d.py` : Implémentation de la Transformée Théorique des Nombres rapide modulo $3329$.
* `bibliotheque_numerotee_1024d.py` : Algorithme de réduction hiérarchique par indexation spatiale et effet domino/miroir.

---

## 🛠️ Installation & Exécution

Les scripts utilisent uniquement **Python 3** et les bibliothèques scientifiques standards :

```bash
pip install numpy matplotlib
python bibliotheque_numerotee_1024d.py
```

---

## 💡 Démarche



Projet réalisé en **autodidacte** par passion pour l'algorithmique, la théorie des nombres et la cybersécurité. Chaque algorithme a été pensé visuellement avant d'être codé et mesuré expérimentalement.
