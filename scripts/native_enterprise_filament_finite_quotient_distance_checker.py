#!/usr/bin/env python3
"""Exhaust/check the native finite-quotient minimum-distance theorem."""

from __future__ import annotations


def epsilon(j: int) -> int:
    return j & 1


def eta(j: int, chi: int) -> int:
    return (3 * j * j + chi * epsilon(j)) // 2


def word(M: int, k: int, R: int, c: int) -> tuple[int, ...]:
    chi = 1 if R % 2 == 0 else -1
    return tuple((c + 3 * R * j + eta(j, chi)) % M for j in range(k))


def code(M: int, k: int) -> list[tuple[int, ...]]:
    return list({word(M, k, R, c) for R in range(2 * M) for c in range(M)})


def minimum_distance(words: list[tuple[int, ...]]) -> int:
    k = len(words[0])
    best = k + 1
    for i, u in enumerate(words):
        for v in words[:i]:
            d = sum(x != y for x, y in zip(u, v))
            if d < best:
                best = d
    return best


def explicit_sharp_pair(M: int, k: int):
    assert M % 6 == 0
    U = M // 6
    u = word(M, k, 0, 0)
    v = word(M, k, U, 0)
    assert u != v
    assert all(u[j] == v[j] for j in range(0, k, 2))
    assert all(u[j] != v[j] for j in range(1, k, 2))
    assert sum(x != y for x, y in zip(u, v)) == k // 2
    return u, v


def main() -> None:
    # Full pairwise replay where the code size stays moderate.
    for M in (6, 12, 18, 24, 30, 42):
        for k in range(3, 10):
            got = minimum_distance(code(M, k))
            expected = k // 2
            assert got == expected, (M, k, got, expected)

    # Arbitrarily large moduli use one explicit extremal pair; the matching
    # lower bound is supplied by the proved multiprobe access theorem.
    for M in (60, 66, 70, 90, 210, 2310, 30030, 510510):
        for k in range(3, 10):
            explicit_sharp_pair(M, k)

    print("FINITE_QUOTIENT_MIN_DISTANCE=floor(k/2)")
    print("EXPLICIT_EXTREMAL_SHIFT=R_TO_R_PLUS_M_OVER_6")
    print("K3_TO_K9_DISTANCE=1,2,2,3,3,4,4")
    print("SHARP9_DETECTS_3_ERRORS=YES")
    print("SHARP9_CORRECTS_1_ERROR=YES")
    print("SHARP9_TOLERATES_3_ARBITRARY_ERASURES=YES")


if __name__ == "__main__":
    main()
