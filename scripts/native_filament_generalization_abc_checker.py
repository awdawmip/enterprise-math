#!/usr/bin/env python3
"""Independent finite checker for the native filament A/B/C generalization package.

Only the Python standard library is used.
The script does not prove the theorems, but exhaustively / pseudo-randomly replays
small instances of their exact formulas.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb, gcd, lcm
from random import Random


def line_points(t: int, c: int, modulus: int):
    return {((-t * y - c) % modulus, y) for y in range(modulus)}


def arrangement_stats(ts, cs, modulus):
    lines = [line_points(t, c, modulus) for t, c in zip(ts, cs)]
    point_mult = Counter()
    for line in lines:
        for point in line:
            point_mult[point] += 1
    n_m = Counter(m for m in point_mult.values() if m >= 2)
    union = set().union(*lines)
    delta = sum(n * comb(m - 1, 2) for m, n in n_m.items() if m >= 3)
    return len(union), n_m, delta


def triple_det(ti, ci, tj, cj, tk, ck):
    # det of rows (1,t,c)
    return ti * (cj - ck) + tj * (ck - ci) + tk * (ci - cj)


def vp(n: int, p: int):
    n = abs(n)
    if n == 0:
        return 10**9
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a


def check_A():
    rng = Random(20260824)
    checked = 0
    for p in (5, 7):
        for _ in range(80):
            k = 4
            ts = rng.sample(range(-8, 9), k)
            if any((ts[i] - ts[j]) % p == 0 for i in range(k) for j in range(i)):
                continue
            cs = [rng.randrange(-12, 13) for _ in range(k)]
            dets = [
                triple_det(ts[i], cs[i], ts[j], cs[j], ts[l], cs[l])
                for i, j, l in combinations(range(k), 3)
            ]
            if any(d == 0 for d in dets):
                continue  # theorem A is stated for simple-over-Q arrangements
            nu = max(vp(d, p) for d in dets)
            previous = None
            for a in (1, 2, 3):
                m = p**a
                union_size, n_m, delta = arrangement_stats(ts, cs, m)
                complement = m * m - union_size
                assert sum(n * comb(mult, 2) for mult, n in n_m.items()) == comb(k, 2)
                assert complement == m * m - k * m + comb(k, 2) - delta
                if previous is not None:
                    assert delta <= previous
                previous = delta
                if a > nu:
                    assert delta == 0
            checked += 1
    assert checked >= 40
    print(f"A_RANDOM_SIMPLE_ARRANGEMENTS_PASS={checked}")


def eta_int(j: int, chi: int):
    return (3 * j * j + chi * (j & 1)) // 2


def native_code(k: int, modulus: int):
    if modulus == 2:
        period = 2
    else:
        period = lcm(2, modulus // gcd(3, modulus))
    words = set()
    for c in range(modulus):
        for R in range(period):
            chi = 1 if R % 2 == 0 else -1
            words.add(
                tuple(
                    (c + 3 * R * j + eta_int(j, chi)) % modulus
                    for j in range(k)
                )
            )
    return words, period


def check_B():
    for k in range(3, 9):
        for M in range(2, 19):
            words, period = native_code(k, M)
            if M == 2:
                assert len(words) == 2
            else:
                expected_period = lcm(2, M // gcd(3, M))
                assert period == expected_period
                assert len(words) == M * expected_period
                equivalent = 2 * M * M
                if M % 2 == 0:
                    equivalent //= 2
                if M % 3 == 0:
                    equivalent //= 3
                assert len(words) == equivalent
    print("B_FINITE_QUOTIENT_CARDINALITY_PASS=M2..18,K3..8")


def legendre(a: int, p: int):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def transparency_bruteforce(p, alpha, beta, a, b):
    count = 0
    for h in range(p):
        f = alpha * (h - a) % p
        g = beta * (h - b) % p
        if f and g and legendre(f, p) == -1 and legendre(g, p) == -1:
            count += 1
    return count


def transparency_formula(p, alpha, beta, a, b):
    numerator = (
        p - 2
        + legendre(alpha * (b - a), p)
        + legendre(beta * (a - b), p)
        - legendre(alpha * beta, p)
    )
    assert numerator % 4 == 0
    return numerator // 4


def check_C():
    primes = (5, 7, 11, 13, 17, 19)
    checked = 0
    for p in primes:
        for alpha in range(1, min(p, 5)):
            for beta in range(1, min(p, 5)):
                for a, b in ((0, 1), (1, 3), (2, 4)):
                    a %= p
                    b %= p
                    if a == b:
                        continue
                    brute = transparency_bruteforce(p, alpha, beta, a, b)
                    formula = transparency_formula(p, alpha, beta, a, b)
                    assert brute == formula
                    if p >= 7:
                        assert brute > 0
                    checked += 1
    print(f"C_TRANSPARENCY_FORMULA_PASS={checked}")


def main():
    check_A()
    check_B()
    check_C()
    print("ABC_GENERALIZATION_CHECKER=PASS")


if __name__ == "__main__":
    main()
