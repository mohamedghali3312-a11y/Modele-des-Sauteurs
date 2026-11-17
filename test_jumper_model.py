def test_goldbach_et_integrite():
    V, _ = generer_roue_primorielle(12)
    V12 = V[-1]
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
    _, premiers = generer_roue_primorielle(25)
    mod = generer_module_ntt_rang_n(8, premiers)
    q = mod["module_premier_qn"]
    zeta = mod["racine_ntt_zeta"]

    assert est_premier_probable(q) is True
    assert pow(zeta, 128, q) == q - 1
    assert pow(zeta, 256, q) == 1
