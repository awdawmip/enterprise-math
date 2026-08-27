#!/usr/bin/env python3
"""Finite checker for the c515 low-pair canonical hard-suffix split."""

from itertools import combinations
from math import prod

K = 116_009_280_740_973_308
W = K + 1
N0 = 18_455  # floor(W^(1/4))
HARD_PRIMES = (41, 43, 47, 53, 59, 61, 67, 71, 73, 79)


def qcrit(primes_desc: tuple[int, ...]) -> int:
    if not primes_desc:
        return 1
    running = 1
    out = 1
    for j, q in enumerate(primes_desc, start=1):
        if j % 2 == 1:
            out = max(out, running * q**3)
        running *= q
    return out


def split(primes_desc: tuple[int, ...]) -> tuple[int, int, int]:
    if not primes_desc:
        return 1, 1, 0
    qs = primes_desc[-1]
    b = prod(primes_desc)
    if qs > N0:
        return b, 1, 0
    if len(primes_desc) == 1 or primes_desc[-2] * qs > N0:
        return b // qs, qs, 1
    qprev = primes_desc[-2]
    return b // (qprev * qs), qprev * qs, 2


def main() -> None:
    assert 23**12 < W < 29**12
    assert 41**12 > W  # 41^3 > W^(1/4)

    # Algebraic regression across finite hard-prime packets and several D1 scales.
    d1_values = (2, 10, 100, 1_000, 10_000, 1_000_000, 10**9, 10**12)
    checked = 0
    for s in range(0, 8):
        for subset in combinations(HARD_PRIMES, s):
            desc = tuple(sorted(subset, reverse=True))
            qc = qcrit(desc)
            for d1 in d1_values:
                if qc >= d1 * N0:
                    continue
                b1, b2, typ = split(desc)
                assert typ in (0, 1, 2)
                assert b2 <= N0
                assert b1 < d1
                assert b1 * b2 == prod(desc) if desc else b1 * b2 == 1
                checked += 1

    print("P017 c515 low-pair canonical suffix factorization checker: PASS")
    print("N0 =", N0)
    print("finite supported packets checked =", checked)
    print("unique suffix types = 0,1,2 hard primes")


if __name__ == "__main__":
    main()
