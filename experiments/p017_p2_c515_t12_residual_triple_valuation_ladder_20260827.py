#!/usr/bin/env python3
"""Exact checker for the corrected residual triple valuation ladder."""

from fractions import Fraction as Q
from itertools import combinations

K = 116_009_280_740_973_308
W = K + 1


def primes_upto(n: int) -> tuple[int, ...]:
    ps: list[int] = []
    for x in range(2, n + 1):
        ok = True
        for p in ps:
            if p * p > x:
                break
            if x % p == 0:
                ok = False
                break
        if ok:
            ps.append(x)
    return tuple(ps)


def qcrit(vals: tuple[int, ...]) -> int:
    qs = tuple(sorted(vals, reverse=True))
    running = 1
    out = 1
    for j, q in enumerate(qs, start=1):
        if j % 2 == 1:
            out = max(out, running * q**3)
        running *= q
    return out


def main() -> None:
    # Basin exponent forces j<=8.
    assert Q(10, 6) < Q(9, 5)
    assert Q(11, 6) > Q(9, 5)

    # Level ladder exponents 1-(j+2)/6.
    assert 1 - Q(3, 6) == Q(1, 2)
    assert 1 - Q(4, 6) == Q(1, 3)
    assert 1 - Q(5, 6) == Q(1, 6)
    assert 1 - Q(6, 6) == 0

    # Tier-A z cutoff.
    assert 1439**27 < W**5 < 1447**27

    # j=2: Q<=z^2=W^(10/27); hard alphabet after P23 is 29..127.
    hard_z2 = tuple(p for p in primes_upto(127) if p >= 29)
    counts = {}
    for depth in range(4):
        n = sum(
            1
            for sub in combinations(hard_z2, depth)
            if qcrit(sub) ** 27 < W**10
        )
        if n:
            counts[depth] = n
    assert counts == {0: 1, 1: 22, 2: 231}
    assert sum(counts.values()) == 254

    # j=3: Q<=z<1447; any hard prime q>=29 violates q^3<Q.
    assert 29**3 > 1447

    print("P017 corrected residual triple valuation ladder checker: PASS")
    print("j=1: Q<=D^(1/2), 74025-state census certified separately")
    print("j=2: Q<=z^2, hard states=254")
    print("j>=3: no nontrivial P23-hard inner Rosser modulus")


if __name__ == "__main__":
    main()
