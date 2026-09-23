#!/usr/bin/env python3
"""
Exact falsification for base-branch dominance criteria.

Portable research checker only. It does not confer Source authority,
mathematical acceptance, CLAIM, OPEN, Result, review, or Working Truth.

Theorems under test:
1. For p == 13 (mod 24), p>13, branch 13 dominates branch p on every
   monomial whose occupied ports avoid both p-divisibility and the
   13-cancellation progression j == 3 (mod 6).
2. For p == 19 (mod 72), p>19, branch 19 dominates branch p on every
   monomial whose occupied ports avoid p-divisibility.
"""

from __future__ import annotations

import random


SEED = 20260924
CLASS13_P_MAX = 2000
CLASS19_P_MAX = 3000
J_MAX = 320
M_MAX = 180
SAMPLES_PER_PRIME = 1000


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def vp_int(n: int, p: int) -> int:
    if n == 0:
        raise ValueError
    n = abs(n)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def vp_factorial(n: int, p: int) -> int:
    e = 0
    q = p
    while q <= n:
        e += n // q
        q *= p
    return e


def vp_one_plus_four_power(j: int, p: int) -> int:
    e = 0
    modulus = p
    while (pow(4, j, modulus) + 1) % modulus == 0:
        e += 1
        modulus *= p
        if e > 12:
            raise RuntimeError("unexpectedly high valuation")
    return e


def endpoint(p: int, j: int) -> int:
    return int((2 * j) % (p - 1) == 0)


def gamma(p: int, m: dict[int, int]) -> int:
    E = sum(a * endpoint(p, j) for j, a in m.items())
    D = sum(a * vp_int(j, p) for j, a in m.items())
    C = sum(a * vp_one_plus_four_power(j, p) for j, a in m.items())
    F = sum(vp_factorial(a, p) for a in m.values())
    return E + D - C + F


def cancellation13(j: int) -> bool:
    # ord_13(4)=6, so s_13=3 and cancellation is j=3*(odd).
    return j % 6 == 3


def main() -> None:
    rng = random.Random(SEED)

    ps13 = [
        p
        for p in range(37, CLASS13_P_MAX + 1)
        if is_prime(p) and p % 24 == 13
    ]
    ps19 = [
        p
        for p in range(91, CLASS19_P_MAX + 1)
        if is_prime(p) and p % 72 == 19
    ]

    # Structural endpoint dominance and factorial monotonicity.
    endpoint_checks = 0
    factorial_checks = 0
    for p in ps13:
        for j in range(1, J_MAX + 1):
            assert endpoint(13, j) >= endpoint(p, j)
            endpoint_checks += 1
        for n in range(0, M_MAX + 1):
            assert vp_factorial(n, 13) >= vp_factorial(n, p)
            factorial_checks += 1

    for p in ps19:
        for j in range(1, J_MAX + 1):
            assert endpoint(19, j) >= endpoint(p, j)
            endpoint_checks += 1
        for n in range(0, M_MAX + 1):
            assert vp_factorial(n, 19) >= vp_factorial(n, p)
            factorial_checks += 1

    class13_vectors = 0
    for p in ps13:
        allowed = [
            j
            for j in range(1, J_MAX + 1)
            if j % p != 0 and not cancellation13(j)
        ]
        for _ in range(SAMPLES_PER_PRIME):
            js = rng.sample(allowed, rng.randint(1, 6))
            m = {j: rng.randint(1, M_MAX) for j in js}
            assert gamma(13, m) >= gamma(p, m), (
                p,
                m,
                gamma(13, m),
                gamma(p, m),
            )
            class13_vectors += 1

    class19_vectors = 0
    for p in ps19:
        allowed = [
            j
            for j in range(1, J_MAX + 1)
            if j % p != 0
        ]
        for _ in range(SAMPLES_PER_PRIME):
            js = rng.sample(allowed, rng.randint(1, 6))
            m = {j: rng.randint(1, M_MAX) for j in js}
            assert gamma(19, m) >= gamma(p, m), (
                p,
                m,
                gamma(19, m),
                gamma(p, m),
            )
            class19_vectors += 1

    # Restrictions are genuinely needed.
    assert gamma(37, {37: 1}) > gamma(13, {37: 1})  # own denominator
    assert gamma(37, {3: 1}) > gamma(13, {3: 1})    # base-13 cancellation
    assert gamma(163, {163: 1}) > gamma(19, {163: 1})  # own denominator

    print("status=PASS")
    print(f"class13_primes={len(ps13)}")
    print(f"class19mod72_primes={len(ps19)}")
    print(f"endpoint_checks={endpoint_checks}")
    print(f"factorial_checks={factorial_checks}")
    print(f"class13_vectors={class13_vectors}")
    print(f"class19_vectors={class19_vectors}")
    print("restriction_witnesses=37:e37,37:e3,163:e163")


if __name__ == "__main__":
    main()
