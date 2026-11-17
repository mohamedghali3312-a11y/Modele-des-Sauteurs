# Le Modèle des Sauteurs (*The Jumper Model*)

Ce dépôt présente une approche algorithmique dédiée à l'optimisation de la recherche de nombres premiers et à l'étude de structures arithmétiques spécifiques (paires de Goldbach et chaînes de Cunningham).

## 🎯 Objectif du projet

Le **Modèle des Sauteurs** repose sur le principe de la factorisation par roue primorielle (*Primorial Wheel Factorization*). Plutôt que de tester tous les entiers un par un, l'algorithme utilise des « sauts » prédéfinis basés sur les produits de petits nombres premiers (les primorielles) afin d'ignorer directement les multiples évidents.

## 🔬 Axes de recherche et fonctionnalités

* **Filtrage par crible primoriel :** Réduction de l'espace de recherche grâce aux résidus modulaires autour d'une base primorielle $P_k\#$.
* **Exploration de Goldbach :** Repérage et analyse de la distribution des paires de nombres premiers $(p, q)$ telles que $p + q = 2n$.
* **Détection des chaînes de Cunningham :** Recherche optimisée de suites de nombres premiers de première et seconde espèce ($p_{i+1} = 2p_i \pm 1$).
* **Tests de performance et benchmarks :** Mesure des temps d'exécution et comparaison avec les cribles classiques (crible d'Ératosthène segmenté).

## 📁 Structure du dépôt

* `/src` : Code source de l'algorithme et scripts de test.
* `/docs` : Livre blanc, notes mathématiques et démonstrations détaillées.
* `/benchmarks` : Résultats des tests de vitesse et consommation mémoire.

## 🚀 Utilisation rapide

*(Ajoutez ici la commande permettant de lancer votre script, par exemple :)*

```bash
python src/jumper_model.py --limit 1000000
```

## ⚠️ Note méthodologique et limites

Ce projet constitue un travail de recherche exploratoire en théorie computationnelle des nombres. Les optimisations proposées réduisent le facteur constant du temps de calcul, mais restent soumises aux limites théoriques de complexité liées à la taille des entiers traités.

## 📄 Licence

Ce projet est distribué sous licence MIT. Voir le fichier `LICENSE` pour plus d'informations.
