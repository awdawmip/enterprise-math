#!/usr/bin/env python3
"""Check the exact two-probe projection fibers of native quotient codes."""

from __future__ import annotations

import math


def epsilon(j: int) -> int:
    return j & 1


def eta(j: int, chi: int) -> int:
    return (3 * j * j + chi * epsilon(j)) // 2


def word(M: int, k: int, R: int, c: int) -> tuple[int, ...]:
    chi = 1 if R % 2 == 0 else -1
    return tuple((c + 3 * R * j + eta(j, chi)) % M for j in range(k))


def code(M: int, k: int) -> set[tuple[int, ...]]:
    return {word(M, k, R, c) for R in range(2 * M) for c in range(M)}


def predicted_fiber(M: int, ell: int) -> int:
    assert M % 6 == 0
    U = M // 6
    return math.gcd(ell, U) if ell % 2 else math.gcd(ell, 2 * U)


def projection_fibers(words: set[tuple[int, ...]], i: int, j: int) -> set[int]:
    counts: dict[tuple[int, int], int] = {}
    for w in words:
        p = (w[i], w[j])
        counts[p] = counts.get(p, 0) + 1
    return set(counts.values())


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % p for p in range(2, math.isqrt(n) + 1))


def main() -> None:
    # Exhaust several composite moduli, all island lengths and all baselines.
    for M in (6, 12, 18, 24, 30, 42, 60, 66, 70, 90, 210):
        for k in range(3, 10):
            words = code(M, k)
            for i in range(k):
                for j in range(i + 1, k):
                    ell = j - i
                    got = projection_fibers(words, i, j)
                    expected = predicted_fiber(M, ell)
                    assert got == {expected}, (M, k, i, j, got, expected)

    # Frozen nine-Cell primorial phase diagram.
    expected = {
        6: {1, 3, 5, 7},
        30: {1, 3, 7},
        210: {1, 3},
        2310: {1, 3},
        30030: {1, 3},
    }
    for M, protected in expected.items():
        got = {
            ell for ell in range(1, 9)
            if predicted_fiber(M, ell) == 1
        }
        assert got == protected

    # Through dimension19, the nine-Cell baseline set has already stabilized.
    primes_19 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67)
    P19 = math.prod(primes_19)
    assert {
        ell for ell in range(1, 9)
        if predicted_fiber(P19, ell) == 1
    } == {1, 3}

    # At larger baseline scales, dimension19 still protects numbers whose
    # prime factors all lie outside 5..67; do not confuse this finite stage
    # with the infinite-channel statement.
    stable_19 = {
        ell for ell in range(1, 1001)
        if predicted_fiber(P19, ell) == 1
    }
    assert 73 in stable_19 and 79 in stable_19 and 5 not in stable_19

    # Infinite characterization up to a finite cutoff: include every possible
    # prime factor of an ell<=1000, so only powers of3 remain.
    U = math.prod(q for q in range(5, 1001) if is_prime(q))
    stable_infinite_cutoff = {
        ell for ell in range(1, 1001)
        if ell % 2 and math.gcd(ell, U) == 1
    }
    powers3 = {1, 3, 9, 27, 81, 243, 729}
    assert stable_infinite_cutoff == powers3

    print("TWO_PROBE_FIBER_FORMULA=PASS")
    print("D2_BASELINES=1,3,5,7")
    print("D3_BASELINES=1,3,7")
    print("D4_TO_D19_NINECELL_BASELINES=1,3")
    print("ALL_CHANNEL_PROTECTED_BASELINES=POWERS_OF_3")


if __name__ == "__main__":
    main()
