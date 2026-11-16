import math

def build_mirror_wheel_V4():
    V4 = 2310
    first_half = [r for r in range(1, V4 // 2, 2) if math.gcd(r, V4) == 1]
    residues = first_half + [V4 - r for r in reversed(first_half)]
    steps = [residues[i + 1] - residues[i] for i in range(len(residues) - 1)]
    steps.append(V4 + residues[0] - residues[-1])
    return V4, residues, steps

def is_prime_deterministic(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
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

def certify_pocklington(P, prime_factors_P_minus_1):
    if not all(is_prime_deterministic(q) for q in prime_factors_P_minus_1):
        return None
    for a in range(2, 500):
        if pow(a, P - 1, P) == 1 and all(
            math.gcd(pow(a, (P - 1) // q, P) - 1, P) == 1
            for q in prime_factors_P_minus_1
        ):
            return a
    return None

def next_prime_mirror_machine(start):
    V4, residues, steps = build_mirror_wheel_V4()
    W_5_12 = 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41
    rem = start % V4
    idx = next((i for i, r in enumerate(residues) if r >= rem), len(residues))
    x = start + (V4 - rem + residues[0] if idx == len(residues) else residues[idx] - rem)
    idx %= len(steps)
    while True:
        if math.gcd(x, W_5_12) == 1 and is_prime_deterministic(x):
            return x
        x += steps[idx]
        idx = (idx + 1) % len(steps)

if __name__ == "__main__":
    assert next_prime_mirror_machine(10**12) == 1000000000039
    assert is_prime_deterministic((1 << 8) * 13 + 1)
    assert is_prime_deterministic((1 << 27) * 15 + 1)
    print("Tests unitaires v16.0 valides.")
