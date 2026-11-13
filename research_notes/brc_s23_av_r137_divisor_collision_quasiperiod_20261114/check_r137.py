#!/usr/bin/env python3
"""R137 exact collision, affine quasiperiod and independent event checks."""
from fractions import Fraction
from math import lcm

def totients(limit):
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for n in range(p, limit + 1, p):
                phi[n] -= phi[n] // p
    return phi

def j_divisor(K, m, phi):
    L, N = K - 1, K - 1 + m
    return sum(phi[q] for q in range(2, N + 1)
               if N // q - (max(L, 1) - 1) // q >= 1)

def j_collision(K, m, phi):
    assert K >= 2 and m >= 1
    L = K - 1
    raw = (m + 1) * (K - 2) + m * (m + 1) // 2
    duplicate = sum(
        phi[q] * ((L + m) // q - (L - 1) // q - 1)
        for q in range(2, m + 1)
    )
    return raw - duplicate

def j_fraction_union(K, m):
    L = K - 1
    return len({
        Fraction(p, n)
        for n in range(max(1, L), L + m + 1)
        for p in range(1, n)
    })

def classical_count(m, phi):
    return 1 + sum((m + 1 - q) * phi[q] for q in range(1, m + 1))

def run():
    phi = totients(1200)
    pairs = 0
    for m in range(1, 31):
        for K in range(2, 81):
            assert j_divisor(K, m, phi) == j_collision(K, m, phi)
            pairs += 1
    assert pairs == 2370
    # Independent exact rational fractions, including K=1.
    direct = 0
    for m in range(1, 13):
        for K in range(1, 35):
            assert j_divisor(K, m, phi) == j_fraction_union(K, m)
            direct += 1
    assert direct == 408
    periods = 0
    for m in range(1, 9):
        P = lcm(*range(1, m + 1))
        for K in range(2, 30):
            assert j_collision(K + P, m, phi) - j_collision(K, m, phi) == (m + 1) * P
            periods += 1
    assert periods == 224
    for m in range(1, 7):
        P = lcm(*range(1, m + 1))
        down = [K for K in range(2, 2 + P)
                if j_collision(K + 1, m, phi) < j_collision(K, m, phi)]
        if m <= 5:
            assert not down, (m, down)
        else:
            assert down == [24, 54], down
    assert (j_collision(24, 6, phi), j_collision(25, 6, phi)) == (169, 167)
    expected_first = {1:2,2:2,3:3,4:4,5:7,6:9,7:11,8:16,9:22,
        10:25,11:29,12:41,13:46,14:51,15:67,16:73,17:79,18:99,
        19:106,20:113}
    necessary = {}
    for m in range(1, 21):
        count = classical_count(m, phi)
        k = next(K for K in range(2, m * m + m + 3)
                 if j_collision(K, m, phi) + 1 >= count)
        assert k <= expected_first[m]
        necessary[m] = k
    assert necessary[10] == 12 and necessary[20] == 42
    print("R137_COLLISION_QUASIPERIOD_PASS")
    print({"divisor_pairs": pairs, "exact_fraction_pairs": direct,
           "quasiperiod_pairs": periods,
           "example": [j_collision(24, 6, phi), j_collision(25, 6, phi)],
           "necessary_thresholds": necessary})
if __name__ == "__main__":
    run()
