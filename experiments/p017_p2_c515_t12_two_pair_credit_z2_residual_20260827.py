#!/usr/bin/env python3
"""Supersession checker for the former c515 two-pair / z^2 claim.

The z^2 finite censuses are retained as conditional diagnostics, while the
least-shell budget obstruction is asserted explicitly.  The actual residual
ceiling is D^(1/2); see the correction checker.
"""

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


def active_z2(vals: tuple[int, ...]) -> bool:
    return qcrit(vals) ** 27 < W**10


def census(primes: tuple[int, ...], depth: int) -> dict[int, int]:
    out: dict[int, int] = {}
    for r in range(depth + 1):
        n = sum(1 for sub in combinations(primes, r) if active_z2(sub))
        if n:
            out[r] = n
    return out


def main() -> None:
    # Explicit obstruction: full base-T3=1 at u=1/6, but least shell costs 1/2.
    u = Q(1, 6)
    base = 12 * u - 1
    least = Q(1, 2)
    pair_max = Q(1, 2)
    assert base == 1
    assert base - least == pair_max < 2 * pair_max

    # Conditional z^2 diagnostics remain arithmetically correct.
    all_odd = tuple(p for p in primes_upto(127) if p % 2)
    hard = tuple(p for p in all_odd if p >= 29)
    hard_counts = census(hard, 3)
    full_counts = census(all_odd, 6)
    assert hard_counts == {0: 1, 1: 22, 2: 231}
    assert full_counts == {0: 1, 1: 30, 2: 435, 3: 1153, 4: 1234, 5: 288}

    print("P017 former two-pair/z2 checker: SUPERSEDED AS EXPECTED")
    print("two-pair premise fails after least-shell charge")
    print("conditional z2 censuses retained: 254 hard / 3141 anchor-free")


if __name__ == "__main__":
    main()
