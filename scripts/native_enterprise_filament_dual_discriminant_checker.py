#!/usr/bin/env python3
"""Check the dual-syndrome / arrangement-discriminant identity."""

from __future__ import annotations

import math
from itertools import combinations


def epsilon(j: int) -> int:
    return j & 1


def eta(j: int, chi: int) -> int:
    n = 3 * j * j + chi * epsilon(j)
    assert n % 2 == 0
    return n // 2


def packet(k: int, a: int, b: int, chi: int) -> list[int]:
    return [a + b * j + eta(j, chi) for j in range(k)]


def mixed_triples(k: int):
    for tri in combinations(range(k), 3):
        evens = [j for j in tri if j % 2 == 0]
        odds = [j for j in tri if j % 2 == 1]
        if len(evens) == 2:
            u, v = evens
            w = odds[0]
            e = 0
        elif len(odds) == 2:
            u, v = odds
            w = evens[0]
            e = 1
        else:
            continue
        yield tri, u, v, w, e


def triple_check(values: list[int], u: int, v: int, w: int) -> int:
    return (
        (v - u) * values[w]
        + (w - v) * values[u]
        - (w - u) * values[v]
    )


def factor(n: int) -> dict[int, int]:
    n = abs(n)
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def product_factorization(k: int, chi: int) -> dict[int, int]:
    prod = 1
    for _tri, u, v, w, e in mixed_triples(k):
        d = 3 * (w - u) * (w - v) + chi * ((-1) ** e)
        assert d != 0
        prod *= abs(d)
    return factor(prod)


def main() -> None:
    expected_mixed = {3: 1, 4: 4, 5: 9, 6: 18, 7: 30, 8: 48, 9: 70}
    expected = {
        (3, 1): {2: 1},
        (3, -1): {2: 2},
        (4, 1): {2: 7, 5: 1},
        (4, -1): {2: 7, 5: 1},
        (5, 1): {2: 18, 5: 2},
        (5, -1): {2: 15, 5: 4},
        (6, 1): {2: 34, 5: 5, 7: 1, 11: 1, 23: 1},
        (6, -1): {2: 34, 5: 5, 7: 1, 11: 1, 23: 1},
        (7, 1): {2: 56, 5: 6, 7: 4, 11: 2, 13: 1, 23: 2},
        (7, -1): {2: 60, 5: 8, 7: 3, 11: 2, 23: 2},
        (8, 1): {2: 96, 5: 10, 7: 6, 11: 4, 13: 2, 23: 3, 31: 1, 53: 1},
        (8, -1): {2: 96, 5: 10, 7: 6, 11: 4, 13: 2, 23: 3, 31: 1, 53: 1},
        (9, 1): {2: 140, 5: 14, 7: 9, 11: 8, 13: 4, 23: 4, 31: 2, 53: 2},
        (9, -1): {2: 140, 5: 14, 7: 8, 11: 8, 13: 3, 23: 6, 31: 2, 53: 2},
    }

    for k in range(3, 10):
        triples = list(mixed_triples(k))
        assert len(triples) == expected_mixed[k]
        e = (k + 1) // 2
        o = k // 2
        assert len(triples) == e * o * (k - 2) // 2

        for chi in (1, -1):
            values = packet(k, a=137, b=-19, chi=chi)
            y = [2 * values[j] - 3 * j * j for j in range(k)]
            for _tri, u, v, w, parity in triples:
                t = triple_check(values, u, v, w)
                d = 3 * (w - u) * (w - v) + chi * ((-1) ** parity)
                assert 2 * t == (v - u) * d

                mode_t = triple_check(y, u, v, w)
                assert mode_t == chi * (v - u) * ((-1) ** parity)

            assert product_factorization(k, chi) == expected[(k, chi)]

    # Sharp-nine radical and p-adic depth statement.
    radicals = []
    for chi in (1, -1):
        f = product_factorization(9, chi)
        radicals.append(math.prod(f))
        for q in (11, 13, 23, 31, 53):
            assert q in f
            # Every individual obstruction is smaller than q^2.
            for _tri, u, v, w, e in mixed_triples(9):
                d = abs(3 * (w - u) * (w - v) + chi * ((-1) ** e))
                assert d <= 106
                assert not (d and d % (q * q) == 0)
    assert radicals[0] == radicals[1] == 378267890

    print("MIXED_DUAL_CHECK_COUNTS=1,4,9,18,30,48,70")
    print("DUAL_SYNDROME_EQUALS_CONCURRENCE_OBSTRUCTION=PASS")
    print("CURVATURE_FLATTENED_MODE_SYNDROME=PASS")
    print("DISCRIMINANT_FACTORIZATION_STAIRCASE=PASS")
    print("K9_RADICAL=378267890")
    print("K9_POST_SMALL_PADIC_DEPTH=1")


if __name__ == "__main__":
    main()
