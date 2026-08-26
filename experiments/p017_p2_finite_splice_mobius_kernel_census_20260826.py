#!/usr/bin/env python3
"""Exact finite-splice census for the P017 a6 terminal Mobius kernel.

The program enlarges the physical collision domain by dropping primality,
hyperbola/product, accepted-assignment and z-smoothness constraints.  It then
checks the exact divisor-threshold cover formula over every odd squarefree
ell allowed by the Tier-A a6 splice envelope.

This certifies only the finite-splice exact-Mobius kernel constant.  It does
not provide an all-K constant or extend the cancellation to arbitrary
Rosser/well-factorable coefficients.
"""

from math import gcd


K0 = 116_009_280_740_973_308
W0 = K0 + 1


def floor_nth_root(n: int, k: int) -> int:
    if n < 0 or k <= 0:
        raise ValueError("need n>=0 and k>=1")
    lo, hi = 0, 1
    while hi**k <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**k <= n:
            lo = mid
        else:
            hi = mid
    return lo


def ceil_nth_root(n: int, k: int) -> int:
    r = floor_nth_root(n, k)
    return r if r**k == n else r + 1


P0 = ceil_nth_root(K0**22, 27)
Q0 = (K0 * K0 + 2 * K0) // (P0 * P0)
L0 = Q0 // 3

assert P0 == 80_241_952_393_051
assert Q0 == 2_090_174
assert L0 == 696_724
assert P0**27 >= K0**22
assert (P0 - 1) ** 27 < K0**22
assert Q0 * P0 * P0 <= K0 * K0 + 2 * K0
assert (Q0 + 1) * P0 * P0 > K0 * K0 + 2 * K0
assert W0 < 1446 * P0


def linear_sieve(limit: int):
    lp = [0] * (limit + 1)
    mu = [0] * (limit + 1)
    omega = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []

    for i in range(2, limit + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            mu[i] = -1
            omega[i] = 1
        for p in primes:
            value = i * p
            if value > limit:
                break
            lp[value] = p
            if i % p == 0:
                mu[value] = 0
                omega[value] = omega[i]
                break
            mu[value] = -mu[i]
            omega[value] = omega[i] + 1

    return lp, mu, omega


def squarefree_factors(n: int, lp: list[int]) -> tuple[int, ...]:
    out: list[int] = []
    while n > 1:
        p = lp[n]
        out.append(p)
        n //= p
    return tuple(out)


def divisors_from_factors(factors: tuple[int, ...]) -> list[int]:
    divisors = [1]
    for p in factors:
        divisors += [d * p for d in tuple(divisors)]
    divisors.sort()
    return divisors


def local_envelope(
    ell: int,
    divisors: list[int],
    mu: list[int],
) -> tuple[int, tuple[int, int, int]]:
    """Max |-mu(ell)+cover prefix| over 3<R1,R2<=W0/P0."""

    size = len(divisors)
    prefix = [[0] * size for _ in range(size)]

    for i, f1 in enumerate(divisors):
        row_sum = 0
        for j, f2 in enumerate(divisors):
            weight = (
                mu[f1] * mu[f2]
                if f1 * f2 // gcd(f1, f2) == ell
                else 0
            )
            row_sum += weight
            prefix[i][j] = row_sum + (prefix[i - 1][j] if i else 0)

    # R>3 strictly.  Hence every divisor <=3 is present already in the
    # minimal cutoff state.  A divisor d can be included below some allowed
    # R<=W0/P0 iff d < W0/P0, checked exactly as d*P0<W0.
    min_index = 0
    max_index = -1
    for i, d in enumerate(divisors):
        if d <= 3:
            min_index = i
        if d * P0 < W0:
            max_index = i

    assert max_index >= min_index

    best_abs = -1
    best = (0, divisors[min_index], divisors[min_index])
    baseline = -mu[ell]

    for i in range(min_index, max_index + 1):
        for j in range(min_index, max_index + 1):
            coefficient = baseline + prefix[i][j]
            magnitude = abs(coefficient)
            if magnitude > best_abs:
                best_abs = magnitude
                best = (coefficient, divisors[i], divisors[j])

    return best_abs, best


def main() -> None:
    lp, mu, omega = linear_sieve(L0)

    squarefree_count = 0
    maximum = -1
    maximum_example = None
    maximum_by_omega: dict[int, int] = {}

    for ell in range(3, L0 + 1, 2):
        if mu[ell] == 0:
            continue

        squarefree_count += 1
        factors = squarefree_factors(ell, lp)
        divisors = divisors_from_factors(factors)
        local_max, local_example = local_envelope(ell, divisors, mu)

        w = omega[ell]
        maximum_by_omega[w] = max(maximum_by_omega.get(w, 0), local_max)

        if local_max > maximum:
            maximum = local_max
            maximum_example = (ell, factors, local_example)

    assert squarefree_count == 282_366
    assert max(maximum_by_omega) == 6
    assert maximum_by_omega == {
        1: 1,
        2: 1,
        3: 2,
        4: 5,
        5: 11,
        6: 13,
    }
    assert maximum == 13
    assert maximum_example == (
        255_255,
        (3, 5, 7, 11, 13, 17),
        (13, 1001, 1309),
    )

    print("P017 finite-splice Mobius kernel census: PASS")
    print("K0 =", K0)
    print("P0 = ceil(K0^(22/27)) =", P0)
    print("Q0 =", Q0)
    print("L0 = floor(Q0/3) =", L0)
    print("odd squarefree ell scanned =", squarefree_count)
    print("max by omega =", maximum_by_omega)
    print("global max |C| =", maximum)
    print("example =", maximum_example)


if __name__ == "__main__":
    main()
