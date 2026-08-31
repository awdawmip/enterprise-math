#!/usr/bin/env python3
"""Exact finite replay of native filament quotient-code cardinalities."""

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
    # 2M is always a safe R period for the finite replay.
    return {word(M, k, R, c) for R in range(2 * M) for c in range(M)}


def predicted_size(M: int) -> int:
    if M == 2:
        return 2
    divisor = (2 if M % 2 == 0 else 1) * (3 if M % 3 == 0 else 1)
    return 2 * M * M // divisor


def main() -> None:
    # Exhaust all small moduli and all realized island lengths.
    for M in range(2, 101):
        g = math.gcd(3, M)
        L = math.lcm(2, M // g)
        if M > 2:
            assert predicted_size(M) == M * L

        sizes = []
        for k in range(3, 10):
            got = len(code(M, k))
            assert got == predicted_size(M), (M, k, got, predicted_size(M))
            sizes.append(got)
        assert len(set(sizes)) == 1

    # Exact primorial tower through d=19 by closed cardinality arithmetic.
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67)
    P = 1
    sizes = []
    for d, q in enumerate(primes, start=1):
        P *= q
        size = 2 if d == 1 else P * P // 3
        sizes.append(size)
        if d == 1:
            assert size == 2
        elif d == 2:
            assert size // sizes[-2] == 6
        else:
            assert size // sizes[-2] == q * q

    assert P == 7858321551080267055879090
    assert sizes[-1] == 20584405866724191423702130398265558985510899742700

    # Full word-by-word reduction replay only where the state sets remain small.
    for M, q in ((6, 5), (30, 7)):
        N = M * q
        for k in (3, 5, 9):
            low = code(M, k)
            high = code(N, k)
            fibers = {w: 0 for w in low}
            for v in high:
                w = tuple(x % M for x in v)
                assert w in fibers
                fibers[w] += 1
            assert set(fibers.values()) == {q * q}

    # Larger tower steps use the proved parameter-period ratio rather than
    # materializing millions of long tuples.
    for M, q in ((210, 11), (2310, 13), (30030, 17)):
        assert predicted_size(M * q) // predicted_size(M) == q * q

    print("FINITE_QUOTIENT_SIZE_FORMULA=PASS M<=100 K=3..9")
    print("MOD2_EXCEPTION_SIZE=2")
    print("M_DIVISIBLE_BY_6_SIZE=M^2/3")
    print("GENERIC_NEW_CHANNEL_FIBER=q^2")
    print("WORD_LEVEL_FIBER_REPLAY=PASS 6->30->210")
    print("PRIMORIAL_D19_CODE_SIZE=20584405866724191423702130398265558985510899742700")


if __name__ == "__main__":
    main()
