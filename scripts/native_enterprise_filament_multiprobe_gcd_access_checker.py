#!/usr/bin/env python3
"""Exhaust the finite-quotient multiprobe gcd access law."""

from __future__ import annotations

import math
from itertools import combinations


def epsilon(j: int) -> int:
    return j & 1


def eta(j: int, chi: int) -> int:
    return (3 * j * j + chi * epsilon(j)) // 2


def word(M: int, k: int, R: int, c: int) -> tuple[int, ...]:
    chi = 1 if R % 2 == 0 else -1
    return tuple((c + 3 * R * j + eta(j, chi)) % M for j in range(k))


def code(M: int, k: int) -> set[tuple[int, ...]]:
    return {word(M, k, R, c) for R in range(2 * M) for c in range(M)}


def step_gcd(S: tuple[int, ...]) -> int:
    base = S[0]
    g = 0
    for j in S[1:]:
        g = math.gcd(g, abs(j - base))
    return g


def predicted_fiber(M: int, S: tuple[int, ...]) -> int:
    assert M % 6 == 0 and len(S) >= 2
    U = M // 6
    g = step_gcd(S)
    same_parity = all((j - S[0]) % 2 == 0 for j in S)
    return math.gcd(g, 2 * U if same_parity else U)


def observed_fibers(words: set[tuple[int, ...]], S: tuple[int, ...]) -> set[int]:
    counts: dict[tuple[int, ...], int] = {}
    for w in words:
        p = tuple(w[j] for j in S)
        counts[p] = counts.get(p, 0) + 1
    return set(counts.values())


def main() -> None:
    # Full subset replay over representative finite quotient channels.
    for M in (6, 12, 18, 30, 42, 60, 70, 90, 210):
        for k in range(3, 9):
            words = code(M, k)
            for size in range(2, k + 1):
                for S in combinations(range(k), size):
                    got = observed_fibers(words, S)
                    expected = predicted_fiber(M, S)
                    assert got == {expected}, (M, k, S, got, expected)

    # Exact M=210 examples.
    examples = {
        (0, 1): 1,
        (0, 3, 6): 1,
        (0, 5): 5,
        (0, 7): 7,
        (0, 2, 6): 2,
        (1, 3, 5, 7): 2,
    }
    for S, expected in examples.items():
        assert predicted_fiber(210, S) == expected

    # A new off-period probe repairs a q-periodic ambiguity.
    assert predicted_fiber(210, (0, 5)) == 5
    assert predicted_fiber(210, (0, 1, 5)) == 1
    assert predicted_fiber(210, (0, 7)) == 7
    assert predicted_fiber(210, (0, 3, 7)) == 1

    # Infinite-channel protected geometry, tested for every subset of 0..15.
    U = math.prod(
        q for q in range(5, 101)
        if all(q % p for p in range(2, math.isqrt(q) + 1))
    )
    for size in range(2, 8):
        for S in combinations(range(16), size):
            mixed = any(j % 2 == 0 for j in S) and any(j % 2 == 1 for j in S)
            g = step_gcd(S)
            protected = mixed and math.gcd(g, U) == 1
            # Since all prime factors <=15 occur in U except 2,3, this is
            # equivalent here to g being a power of3.
            z = g
            while z % 3 == 0:
                z //= 3
            expected = mixed and z == 1
            assert protected == expected

    print("MULTIPROBE_FIBER_GCD_FORMULA=PASS")
    print("ONE_PARITY_LAYER_NEVER_INJECTIVE=PASS")
    print("MIXED_PARITY_INJECTIVE_IFF_GCD_STEP_COPRIME_TO_M_OVER_6")
    print("BAD_PERIOD_REPAIR_BY_ONE_OFF_PERIOD_PROBE=PASS")
    print("ALL_CHANNEL_PROTECTED_STEP_GCD=POWER_OF_3")


if __name__ == "__main__":
    main()
