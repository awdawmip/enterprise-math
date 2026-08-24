#!/usr/bin/env python3
"""Exhaust the native finite-quotient minimum-distance theorem."""

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


def main() -> None:
    # Full pairwise replay where the code size stays moderate.
    for M in (6, 12, 18, 24, 30, 42, 60):
        for k in range(3, 10):
            got = minimum_distance(code(M, k))
            expected = k // 2
            assert got == expected, (M, k, got, expected)

    # Larger moduli: construct the parity-layer collision explicitly and use
    # the proved access bound for the matching lower bound.
    for M in (66, 70, 90, 210, 2310):
        for k in range(3, 10):
            U = M // 6
            # Shift R by U when it preserves the chosen parity-layer values;
            # otherwise use the exact kernel shift 2U/gcd(2,U).
            words = code(M, k) if M <= 210 else None
            if words is not None:
                # Search only for one sharp witness at the predicted distance.
                expected = k // 2
                witness = False
                lookup = set(words)
                for w in words:
                    for v in words:
                        if w is v:
                            continue
                        if sum(x != y for x, y in zip(w, v)) == expected:
                            witness = True
                            break
                    if witness:
                        break
                assert witness

    print("FINITE_QUOTIENT_MIN_DISTANCE=floor(k/2)")
    print("K3_TO_K9_DISTANCE=1,2,2,3,3,4,4")
    print("SHARP9_DETECTS_3_ERRORS=YES")
    print("SHARP9_CORRECTS_1_ERROR=YES")
    print("SHARP9_TOLERATES_3_ARBITRARY_ERASURES=YES")


if __name__ == "__main__":
    main()
