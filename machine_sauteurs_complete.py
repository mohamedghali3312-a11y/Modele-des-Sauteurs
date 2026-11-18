#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Le Modèle des Sauteurs — Visualisation Graphique (Ramanujan & Sauts)
Auteur : Mohamed Ghali (2026)
"""

import math
import matplotlib.pyplot as plt
from machine_sauteurs_complete import (
    generer_roue_primorielle,
    est_premier,
    pgcd,
)


def mesurer_onde_ramanujan(debut: int = 10000, fin: int = 10200):
    valeurs_N = list()
    nb_paires = list()

    for N in range(debut, fin + 1, 2):
        compteur = 0
        for q in range(3, N // 2 + 1, 2):
            if est_premier(q) and est_premier(N - q):
                compteur += 1
        valeurs_N.append(N)
        nb_paires.append(compteur)

    return valeurs_N, nb_paires


def mesurer_distribution_sauts(depart: int = 10**12, nb_blocs: int = 40):
    base_roue = 2310
    a_base = (depart // base_roue) * base_roue
    couloirs = list(r for r in range(1, base_roue, 2) if pgcd(r, base_roue) == 1)
    premiers = list()

    for bloc in range(nb_blocs):
        base = a_base + bloc * base_roue
        for r in couloirs:
            candidat = base + r
            if est_premier(candidat):
                premiers.append(candidat)

    sauts = list(premiers[i + 1] - premiers[i] for i in range(len(premiers) - 1))
    return sauts


def generer_planche_graphique(fichier_sortie: str = "analyse_sauteurs.png"):
    valeurs_N, nb_paires = mesurer_onde_ramanujan(10000, 10240)
    sauts = mesurer_distribution_sauts(10**12, nb_blocs=50)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), dpi=150)
    fig.patch.set_facecolor("white")

    # Graphique 1 : Onde de Ramanujan
    ax1.plot(valeurs_N, nb_paires, color="#1a365d", linewidth=1.4, marker="o", markersize=3)
    ax1.set_title("Onde de Résonance de Ramanujan — Paires de Goldbach (N ∈ [10 000 ; 10 240])", fontsize=11, fontweight="bold")
    ax1.set_xlabel("Entier pair N")
    ax1.set_ylabel("Nombre de décompositions (P + Q = N)")
    ax1.grid(True, linestyle="--", alpha=0.4)

    # Graphique 2 : Histogramme des sauts sur Roue +2310
    ax2.hist(sauts, bins=25, color="#2b6cb0", edgecolor="white", alpha=0.85)
    moyenne = sum(sauts) / len(sauts) if sauts else 0
    ax2.axvline(moyenne, color="#c53030", linestyle="--", linewidth=1.8, label=f"Saut moyen observé : {moyenne:.2f}")
    ax2.set_title("Distribution des Sauts sur la Roue +2310 (Altitude 10^12)", fontsize=11, fontweight="bold")
    ax2.set_xlabel("Amplitude du saut (écart entre deux premiers consécutifs)")
    ax2.set_ylabel("Fréquence")
    ax2.legend()
    ax2.grid(True, linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.savefig(fichier_sortie)
    print(f"Planche graphique enregistrée : {fichier_sortie}")


if __name__ == "__main__":
    generer_planche_graphique()
