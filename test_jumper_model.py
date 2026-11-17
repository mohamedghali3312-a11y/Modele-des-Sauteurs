import pytest
from jumper_model import (
    est_premier_probable,
    generer_roue_primorielle,
    generer_temoin_pocklington,
    isoler_et_certifier_goldbach,
    generer_module_ntt_rang_n,
)


def test_primalite_cas_limites():
    assert est_premier_probable(-5) is False
    assert est_premier_probable(0) is False
    assert est_premier_probable(1) is False
    assert est_premier_probable(2) is True
    assert est_premier_probable(3) is True
    assert est_premier_probable(4) is False
    assert est_premier_probable(1000000000039) is True
    assert est_premier_probable(561) is False


def test_roue_primorielle():
    V, premiers = generer_roue_primorielle(4)
    assert premiers == list((2, 3, 5, 7, 11))
    assert V[-1] == 2310


def test_pocklington_rigoureux():
    assert generer_temoin_pocklington(6657, list((2, 13))) is None
    assert generer_temoin_pocklington(3329, list((2, 13))) is None

    facteurs_3329 = list((2, 2, 2, 2, 2, 2, 2, 2, 13))
    temoin = generer_temoin_pocklington(3329, facteurs_3329)
    assert temoin is not None
    assert pow(temoin, 3328, 3329) == 1


def test_goldbach_et_integrite():
    V, _ = generer_roue_primorielle(12)
    V12 = V[12]
    N = 48512
    cert = isoler_et_certifier_goldbach(N, list((3, 5, 7, 11)), V12)

    assert cert is not None
    P = int(cert["goldbach"]["P"])
    Q = int(cert["goldbach"]["Q"])
    assert P + Q == N
    assert est_premier_probable(P) is True
    assert est_premier_probable(Q) is True
    assert len(cert["integrite_sha256"]) == 64


def test_generation_ntt():
    _, premiers = generer_roue_primorielle(15)
    mod = generer_module_ntt_rang_n(8, premiers)
    q = mod["module_premier_qn"]
    zeta = mod["racine_ntt_zeta"]

    assert est_premier_probable(q) is True
    assert pow(zeta, 128, q) == q - 1
    assert pow(zeta, 256, q) == 1
