#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Le Modèle des Sauteurs — Moteur d'arithmétique primorielle
Auteur : Mohamed Ghali (2026)
"""

import json
import time
import math
import hashlib
from datetime import datetime, timezone

try:
    import gmpy2
    HAS_GMPY2 = True
except ImportError:
    HAS_GMPY2 = False


def pgcd(a: int, b: int) -> int:
    return int(gmpy2.gcd(a, b)) if HAS_GMPY2 else math.gcd(a, b)


def est_premier_probable(n: int) -> bool:
    if HAS_GMPY2:
        return bool(gmpy2.is_prime(n))
    if n < 2:
        return False
    petits_premiers = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in petits_premiers:
        if n == p:
            return True
        if n % p == 0:
            return False
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in petits_premiers:
        if a >= n:
            break
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generer_roue_primorielle(rang_max: int = 12):
    V = list((2,))
    premiers = list((2,))
    pk = 2
    for _ in range(rang_max):
        pk = next(x for x in range(pk + 1, V[-1] + 2) if pgcd(x, V[-1]) == 1)
        premiers.append(pk)
        V.append(V[-1] * pk)
    return V, premiers


def generer_temoin_pocklington(P: int, facteurs_certifies: list) -> int | None:
    P_m1 = P - 1
    F = math.prod(facteurs_certifies)
    if F * F <= P:
        return None

    facteurs_uniques = set(facteurs_certifies)
    for a in range(2, 1000):
        if pow(a, P_m1, P) != 1:
            continue
        if all(pgcd(pow(a, P_m1 // q, P) - 1, P) == 1 for q in facteurs_uniques):
            return a
    return None


def isoler_et_certifier_goldbach(
    N: int,
    socle_facteurs: list,
    V12: int,
    fichier_json: str | None = None,
    max_iter: int = 5_000_000,
) -> dict | None:
    if N % 2 != 0 or N < 8:
        raise ValueError("N doit être un entier pair supérieur ou égal à 8.")

    centre = (N - 2) // 2
    S = math.prod(socle_facteurs)
    B = centre % S or S

    t0 = time.perf_counter()
    iterations = 0
    tests_primalite = 0

    while B < centre and iterations < max_iter:
        iterations += 1
        Q = 2 * B + 1

        if pgcd(Q, V12) == 1:
            p = (centre - B) // S
            P = 2 * (S * p) + 1

            if p > 1 and pgcd(p, V12) == 1 and pgcd(P, V12) == 1:
                tests_primalite += 1
                if est_premier_probable(Q) and est_premier_probable(p) and est_premier_probable(P):
                    duree_ms = round((time.perf_counter() - t0) * 1000, 3)
                    facteurs_P_m1 = sorted(list(set(list((2,)) + socle_facteurs + list((p,)))))
                    temoin_a = generer_temoin_pocklington(P, facteurs_P_m1)

                    certificat = {
                        "meta": {
                            "systeme": "Le Modèle des Sauteurs (v13.1)",
                            "auteur": "Mohamed Ghali",
                            "moteur_test": "Baillie-PSW (gmpy2)" if HAS_GMPY2 else "Miller-Rabin (12 bases)",
                            "horodatage_utc": datetime.now(timezone.utc).isoformat(),
                            "temps_ms": duree_ms,
                            "iterations_saut": iterations,
                            "candidats_testes": tests_primalite,
                        },
                        "goldbach": {
                            "N": str(N),
                            "nb_chiffres": len(str(N)),
                            "P": str(P),
                            "Q": str(Q),
                            "somme_verifiee": (P + Q == N),
                        },
                        "parametres": {
                            "socle_S": str(S),
                            "facteurs_socle": socle_facteurs,
                            "bloc_B": str(B),
                            "quotient_p": str(p),
                        },
                        "certification_pocklington": {
                            "temoin_a": temoin_a,
                            "facteurs_P_moins_1": list(str(q) for q in facteurs_P_m1),
                            "note": "Certificat strict si p est prouvé premier (conditionnel à BPSW sinon).",
                        },
                    }

                    brut = json.dumps(certificat, sort_keys=True).encode("utf-8")
                    certificat["integrite_sha256"] = hashlib.sha256(brut).hexdigest()

                    if fichier_json:
                        with open(fichier_json, "w", encoding="utf-8") as f:
                            json.dump(certificat, f, indent=2, ensure_ascii=False)

                    return certificat
        B += S

    return None


def generer_module_ntt_rang_n(n: int, premiers: list) -> dict:
    dim = 1 << n
    for pk in premiers[1:]:
        q_n = dim * pk + 1
        if est_premier_probable(q_n):
            facteurs_qn_m1 = list((2,)) * n + list((pk,))
            temoin_a = generer_temoin_pocklington(q_n, facteurs_qn_m1)
            if temoin_a is not None:
                zeta_n = pow(temoin_a, pk, q_n)
                if pow(zeta_n, dim // 2, q_n) == q_n - 1 and pow(zeta_n, dim, q_n) == 1:
                    return {
                        "rang_n": n,
                        "dimension_2_n": dim,
                        "generateur_pk": pk,
                        "module_premier_qn": q_n,
                        "temoin_a": temoin_a,
                        "racine_ntt_zeta": zeta_n,
                    }
    raise RuntimeError(f"Aucun module premier trouvé pour n={n} dans la liste fournie.")


if __name__ == "__main__":
    V, premiers = generer_roue_primorielle(25)
    V12 = V[12]

    print("=" * 72)
    print(f"MODÈLE DES SAUTEURS — EXÉCUTION ({'gmpy2/BPSW' if HAS_GMPY2 else 'Python/Miller-Rabin'})")
    print("=" * 72)
    print(f"Primorielle V_12 : {V12}\n")

    print("1. Décomposition de Goldbach + Témoin de Pocklington (N = 1 000 000)")
    cert_1 = isoler_et_certifier_goldbach(1000002, list((3, 7, 11)), V12)
    if cert_1:
        print(f"  -> {cert_1['goldbach']['N']} = {cert_1['goldbach']['P']} + {cert_1['goldbach']['Q']} "
              f"(p = {cert_1['parametres']['quotient_p']}, Témoin a = {cert_1['certification_pocklington']['temoin_a']})")

    print("\n2. Test à grande échelle (N = 10^100 + 2)")
    cert_100 = isoler_et_certifier_goldbach(10**100 + 2, premiers[1:13], V12)
    if cert_100:
        print(f"  -> Trouvé en {cert_100['meta']['temps_ms']} ms "
              f"({cert_100['meta']['candidats_testes']} candidats testés, Témoin a = {cert_100['certification_pocklington']['temoin_a']})")

    print("\n3. Génération de modules premiers de Proth compatibles NTT (q_n = 2^n * p_k + 1)")
    for rang in (8, 12, 32, 64):
        mod = generer_module_ntt_rang_n(rang, premiers)
        print(f"  -> n={mod['rang_n']:<2} | q_n = {mod['module_premier_qn']} | "
              f"zeta_n = {mod['racine_ntt_zeta']}")
