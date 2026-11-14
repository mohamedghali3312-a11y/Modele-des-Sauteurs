import math
import random
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt


def test_miller_rabin(n, tours=20):
    """Test probabiliste de primalite de Miller-Rabin."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(tours):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def extraire_premiers_roue(depart_A=10**300, nb_blocs=20):
    """Teleportation sans pilotes : Roue +2310 et filtrage par PGCD primoriel."""
    ROUE = 2310  # V_5 = 2 * 3 * 5 * 7 * 11 (480 couloirs vierges, elimine 79,2 %)
    A = (depart_A // ROUE) * ROUE
    couloirs = [r for r in range(1, ROUE) if math.gcd(r, ROUE) == 1]

    # Produit des petits sauteurs (13 a 10 000) pour filtrage rapide par PGCD unique
    petits_premiers = [
        p for p in range(13, 10000)
        if all(p % d != 0 for d in range(2, int(p**0.5) + 1))
    ]
    produit_sauteurs = math.prod(petits_premiers)

    premiers = []
    for bloc in range(nb_blocs):
        base = A + bloc * ROUE
        for r in couloirs:
            candidat = base + r
            if math.gcd(candidat, produit_sauteurs) > 1:
                continue
            if test_miller_rabin(candidat):
                premiers.append(candidat)
    return premiers


def analyse_spectrale_et_modulaire(premiers, titre_altitude="10^20"):
    """Analyse des biais modulaires (mod 6 / mod 30) et spectre de Fourier (FFT)."""
    sauts = np.diff(premiers)
    N = len(sauts)

    # 1. Distribution Modulo 6 et Modulo 30
    mod6 = Counter(int(g % 6) for g in sauts)
    mod30 = Counter(int(g % 30) for g in sauts)

    print(f"=== Machine v4.0 — Rapport Complet (Altitude {titre_altitude}) ===")
    print(f"Sauts analyses           : {N}")
    print(f"Saut moyen / Maximum     : {np.mean(sauts):.2f} / +{np.max(sauts)}")
    print(f"Taux de sauts mult. de 6 : {(mod6[0]/N)*100:.2f} %")
    print(f"Top 3 residus mod 30     : {[(k, f'{(v/N)*100:.1f}%') for k, v in mod30.most_common(3)]}")

    # 2. Analyse Spectrale FFT (Verrou n°3)
    sauts_float = sauts.astype(float)
    signal_centre = sauts_float - np.mean(sauts_float)
    amplitudes = np.abs(np.fft.rfft(signal_centre)) / N
    frequences = np.fft.rfftfreq(N, d=1.0)

    # 3. Visualisation graphique (Mod 6, Mod 30 et Spectre FFT)
    fig = plt.figure(figsize=(11, 8))
    fig.suptitle(f"Machine v4.0 — Analyse Spectrale & Modulaire ({titre_altitude})", fontweight="bold")

    ax1 = plt.subplot(2, 2, 1)
    vals_6 = [0, 2, 4]
    ax1.bar(
        [f"≡ {r} (mod 6)" for r in vals_6],
        [(mod6[r] / N) * 100 for r in vals_6],
        color=["#2ca02c", "#1f77b4", "#ff7f0e"]
    )
    ax1.set_title("Sauts Modulo 6 (%)")

    ax2 = plt.subplot(2, 2, 2)
    vals_30 = list(range(0, 30, 2))
    ax2.bar(
        [str(r) for r in vals_30],
        [(mod30[r] / N) * 100 for r in vals_30],
        color=["#2ca02c" if r % 6 == 0 else "#4c72b0" for r in vals_30]
    )
    ax2.set_title("Sauts Modulo 30 (Vert = Mult. de 6)")

    ax3 = plt.subplot(2, 1, 2)
    ax3.plot(frequences[1:], amplitudes[1:], color="#8c564b", linewidth=1.2)
    ax3.set_title("Spectre de Fourier (FFT) — Signature frequentielle des sauts")
    ax3.set_xlabel("Frequence (cycles par saut)")
    ax3.set_ylabel("Amplitude spectrale")
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Exemple 1 : Teleportation a l'horizon 10^300
    geants_300 = extraire_premiers_roue(depart_A=10**300, nb_blocs=5)
    print(f"Horizon 10^300 : {len(geants_300)} premiers de 301 chiffres extraits.")

    # Exemple 2 : Analyse spectrale & modulaire autour de 10^20
    echantillon = extraire_premiers_roue(depart_A=10**20, nb_blocs=300)
    analyse_spectrale_et_modulaire(echantillon, titre_altitude="10^20")
