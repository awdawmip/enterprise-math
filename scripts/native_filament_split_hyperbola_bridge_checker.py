#!/usr/bin/env python3
"""Exact checker for the split-hyperbola tangent/cover bridge."""

from __future__ import annotations

from itertools import combinations
from math import isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def legendre(a: int, q: int) -> int:
    a %= q
    if a == 0:
        return 0
    return 1 if pow(a, (q - 1) // 2, q) == 1 else -1


def inv(a: int, q: int) -> int:
    return pow(a % q, -1, q)


def orbit_key(x: int, y: int, q: int) -> frozenset[tuple[int, int]]:
    return frozenset(
        ((sx * x) % q, (sy * y) % q)
        for sx in (1, -1)
        for sy in (1, -1)
    )


def check_field_bridge(q: int, B: int, chirality: int) -> None:
    assert q % 2 == 1 and is_prime(q)
    B %= q
    assert B != 0
    inv2 = inv(2, q)

    # Q_0^(chi)=x^2/(2B), Q_1^(chi)=x^2/(2B)-chi/2.
    d = [0, (chirality * inv2) % q]

    for i in (0, 1):
        j = 1 - i
        C = (2 * (d[i] - d[j])) % q
        assert C != 0

        reps = {
            (x, y)
            for x in range(q)
            for y in range(q)
            if (B * (y * y - x * x) - C) % q == 0
        }
        hyp = {
            (a, b)
            for a in range(q)
            for b in range(q)
            if (B * a * b - C) % q == 0
        }

        # Linear bridge Phi(x,y)=(y-x,y+x).
        phi = {((y - x) % q, (y + x) % q) for x, y in reps}
        assert phi == hyp
        assert len(reps) == q - 1
        assert len(hyp) == q - 1

        # Negative Legendre-dual images.
        I_i = {(-B * x * x * inv2 - d[i]) % q for x in range(q)}
        I_j = {(-B * y * y * inv2 - d[j]) % q for y in range(q)}
        overlap = I_i & I_j

        # Common dual values are exactly independent-sign orbits.
        orbits = {orbit_key(x, y, q) for x, y in reps}
        assert len(orbits) == len(overlap)

        formula = (
            q
            + 1
            + legendre(B * C, q)
            + legendre(-B * C, q)
        ) // 4
        assert len(overlap) == formula

        # Native chirality sign only swaps the two character terms.
        native_formula = (q + 1 + legendre(B, q) + legendre(-B, q)) // 4
        assert len(overlap) == native_formula


def mixed_difference_sample(k: int) -> set[tuple[int, int, int, int, int]]:
    """Return (u,v,w,e,a*b) over mixed-parity triples in [0,k)."""
    out = set()
    for e in (0, 1):
        same = [j for j in range(k) if j % 2 == e]
        opp = [j for j in range(k) if j % 2 != e]
        for u, v in combinations(same, 2):
            for w in opp:
                out.add((u, v, w, e, (w - u) * (w - v)))
    return out


def main() -> None:
    # General bridge and orbit theorem on a broad exact grid.
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for q in primes:
        for B in range(1, q):
            for chi in (1, -1):
                check_field_bridge(q, B, chi)

    # Native B=3, q=5: complete hyperbola collapses to one sign orbit.
    q = 5
    B = 3
    overlap_5 = (q + 1 + legendre(B, q) + legendre(-B, q)) // 4
    assert overlap_5 == 1
    tau_5 = overlap_5 - 1
    assert tau_5 == 0

    # Native B=3, q=53: local k=9 sample hits, but global orbit quotient is 13.
    q = 53
    overlap_53 = (q + 1 + legendre(B, q) + legendre(-B, q)) // 4
    assert overlap_53 == 13
    assert overlap_53 - 1 == 12

    sample = mixed_difference_sample(9)
    extremal = [row for row in sample if abs(row[4]) == 35]
    assert extremal
    assert any((B * prod + 1) % 53 == 0 for *_, prod in extremal)

    # Exact finite-window cutoff M_J=35 for k=9.
    M = max(abs(prod) for *_, prod in sample)
    assert M == 35
    assert (B * M + 1) // 2 == 53

    # The explicit terminal witness triple is present.
    assert (0, 2, 7, 0, 35) in sample
    assert 3 * 35 + 1 == 2 * 53

    print("GENERAL_LINEAR_HYPERBOLA_BRIDGE=PASS")
    print("SIGN_ORBIT_OVERLAP_THEOREM=PASS")
    print("NATIVE_Q5_ORBIT_COLLAPSE=PASS overlap=1 tau=0")
    print("NATIVE_Q53_SAMPLE_HIT_NONBREAKER=PASS overlap=13 tau=12")
    print("NATIVE_K9_SAMPLE_MAX_PRODUCT=35")
    print("NATIVE_TERMINAL_EXCEPTION=3*35+1=106=2*53")


if __name__ == "__main__":
    main()
