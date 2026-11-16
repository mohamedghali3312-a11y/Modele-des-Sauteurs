# Le Modèle des Sauteurs — La Machine (v16.0)
### *The Jumpers Model — La Machine (v16.0)*

**Architecture algébrique en mémoire constante $O(1)$ pour le filtrage primoriel double étage, la certification déterministe Lucas-Pocklington et la génération de paramètres NTT post-quantiques (ML-KEM / Falcon-1024 / FHE / ZK-STARKs).**

*(Constant $O(1)$ memory algebraic architecture for two-stage primorial filtering, deterministic Lucas-Pocklington certification, and post-quantum NTT parameter generation.)*

---

## 📄 Documents & Code Source / *Repository Contents*

* **[`Le_Modele_des_Sauteurs_La_Machine_v16_Complet.pdf`](./Le_Modele_des_Sauteurs_La_Machine_v16_Complet.pdf)** — Article scientifique complet en français (Théorèmes, preuves, benchmarks et connexion avec Goldbach & Riemann).
* **[`The_Jumpers_Model_La_Machine_v16_English.pdf`](./The_Jumpers_Model_La_Machine_v16_English.pdf)** — Full English version of the paper.
* **[`la_machine_v16.py`](./la_machine_v16.py)** — Implémentation Python autonome (Roue miroir $V_4$ en cache L1, filtre $W_{5..12}$, certification Lucas-Pocklington, générateur RNS/NTT et benchmarks).
* **[`la_machine_v16_proofs.lean`](./la_machine_v16_proofs.lean)** — Module de vérification formelle sous **Lean 4** certifiant les identités algébriques clés.

> **Statut académique / *Academic Status* :** Pré-publication déposée sur l'archive ouverte **HAL** (`hal.science`, en cours de validation technique).

---

## 🚀 Points clés de l'architecture / *Key Highlights*

### 1. Filtrage Double Étage en Mémoire Constante $O(1)$
* **Étage 1 (Cache L1 — Symétrie miroir $r \leftrightarrow V_4 - r$) :** Table circulaire pré-calculée de $\varphi(2\,310) = 480$ sauts occupant **$< 2\text{ Ko}$** en cache L1, éliminant $79{,}22\,\%$ des entiers par simple addition entière sans calcul de PGCD.
* **Étage 2 (Filtre PGCD $O(1)$) :** Filtrage par le cofacteur $W_{5..12} = V_{12}/V_4 = 131\,710\,070\,791$, portant le taux d'élimination global à **$85{,}49\,\%$** tout en réduisant d'un facteur **$4{,}81\times$** les appels `gcd`.
* **Certification déterministe instantanée :** Chaque candidat structuré $P = 2A + 1$ fournit *a priori* la factorisation de $P - 1$, permettant une certification déterministe directe via le théorème de **Lucas-Pocklington**.

### 2. Benchmarks Expérimentaux ($O(1)$ RAM)

| Taille cible | Appels Miller-Rabin (Naïf vs $V_{12}$) | Accélération temps | Pic mémoire dynamique |
| :--- | :---: | :---: | :---: |
| **512 bits** | $3\,542 \to 1\,024$ ($-71{,}1\,\%$) | **$2{,}85\times$** | $< 1\text{ Ko}$ ($O(1)$) |
| **1 024 bits** | $7\,118 \to 2\,058$ ($-71{,}1\,\%$) | **$3{,}21\times$** | $< 1\text{ Ko}$ ($O(1)$) |
| **2 048 bits** | $14\,290 \to 4\,132$ ($-71{,}1\,\%$) | **$3{,}44\times$** | $< 1\text{ Ko}$ ($O(1)$) |

### 3. Cryptographie Post-Quantique & Preuves ZK
L'équation génératrice au rang $n$, $q_n = 2^n \cdot K + 1$, produit directement les corps finis premiers et racines primitives de l'unité pour les transformées rapides **NTT** :
* **ML-KEM (NIST PQC) :** $n = 8 \implies q_8 = 3\,329$, racine primitive $\zeta_8 = 17$
* **Falcon-1024 :** $n = 12 \implies q_{12} = 12\,289$, racine primitive $\zeta_{12} = 1\,331$
* **FHE (RNS 60 bits) :** Génération déterministe de chaînes de modules premiers négacycliques ($d = 2^{15} = 32\,768$)
* **ZK-STARKs (BabyBear) :** $K = 15, n = 27 \implies p = 15 \cdot 2^{27} + 1 = 2\,013\,265\,921$

### 4. Théorie Analytique des Nombres (Goldbach & Riemann)
* **Réduction Paramétrique de Goldbach :** Reformulation de $N = P + Q$ autour du centre décalé $(N - 2)/2$ et analyse du terme d'erreur $E_k(N)$ face à l'obstacle de parité de Selberg.
* **Critère de Guy Robin :** Vérification numérique et asymptotique distinguant les roues sans facteur carré $V_k$ (limite $\frac{6}{\pi^2} e^\gamma \approx 1{,}08276$) des roues pondérées $\widetilde{V}_k$ (approchant le plafond critique $e^\gamma \approx 1{,}78107$).

---

## 💻 Exécution rapide / *Quick Start*

Aucune dépendance externe n'est requise (Python 3.8+ standard uniquement) :

```bash
python3 la_machine_v16.py
```

Pour vérifier les preuves formelles avec **Lean 4** :

```bash
lean la_machine_v16_proofs.lean
```

---

## ✒️ Citation & Auteur / *Author*

**Mohamed Ghali** — Novembre 2026  
Licence : **CC BY 4.0** (Documentation) / **MIT** (Code source)
