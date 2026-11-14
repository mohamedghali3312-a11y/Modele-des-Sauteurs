# 🔢 Le Modèle des Sauteurs & La Machine v4.0 (Horizon $10^{300}$)

**De l'intuition arithmétique sur feuille de brouillon à l'implémentation d'algorithmes haute performance pour les grands nombres premiers, l'analyse spectrale et la cryptographie.**

---

## 🎯 À propos du projet

Ce dépôt rassemble mes recherches personnelles et mes expérimentations algorithmiques en **Python** autour de la structure des nombres premiers :

1. **Fondements Cinématiques & Primorielle ($V_k$) :** Modélisation du crible sur une piste infinie où chaque sauteur bondit selon sa vitesse propre $v_k = p_k$, combinée à la correction additive/multiplicative et à la projection par produit scindé.
2. **Campagnes Expérimentales ($10^{13}$ et $10^{14}$) :** Exploration à haute altitude via les roues $+210$ et $+2310$ (éliminant jusqu'à $79,2\%$ des composés), vérification de la conjecture de Legendre ($99,99\%$) et détection de constellations rares (jumeaux, triplets, quadruplets, chaînes de Cunningham).
3. **Mutations de la Machine v4.0 (Horizon $10^{300}$) :**
   * **Téléportation sans pilotes en mémoire $O(1)$ :** Couplage de la Roue $+2310$, du PGCD groupé et du radar probabiliste de Miller-Rabin.
   * **Crible pondéré lisse (Maynard-Tao) :** Dépassement du problème de la parité.
   * **Analyseur spectral FFT & Modulaire :** Étude fréquentielle des écarts et des biais modulo $6$ et modulo $30$.

---

## 📂 Contenu du Dépôt

| Fichier | Description |
| :--- | :--- |
| **`Modele_des_Sauteurs_Machine_v4_Smartphone.pdf`** | Édition finale illustrée regroupant la théorie complète, les tableaux de résultats ($10^{13}$ / $10^{14}$) et le code commenté. |
| **`machine_v4_10300.py`** | Script Python exécutable intégrant la Roue $+2310$, le filtrage par PGCD primoriel, le test de Miller-Rabin et les graphiques FFT / Mod 6 & 30. |
| **`README.md`** | Documentation principale du projet. |

---

## 🛠️ Installation & Exécution

Le script nécessite **Python 3** ainsi que les bibliothèques `numpy` et `matplotlib` :

```bash
pip install numpy matplotlib
python machine_v4_10300.py
```

---

## 👤 Auteur

* **Mohamed Ghali** — [@mohamedghali3312-a11y](https://github.com)
