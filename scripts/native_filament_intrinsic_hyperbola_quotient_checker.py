#!/usr/bin/env python3
"""Exact checker for the intrinsic tangent-hyperbola quotient theorem."""

from __future__ import annotations

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


def K4_orbit(a: int, b: int, q: int) -> frozenset[tuple[int, int]]:
    return frozenset({
        (a % q, b % q),
        (b % q, a % q),
        ((-a) % q, (-b) % q),
        ((-b) % q, (-a) % q),
    })


def check(q: int, B: int, chirality: int, branch: int) -> None:
    assert q % 2 == 1 and is_prime(q)
    B %= q
    assert B != 0
    inv2 = pow(2, -1, q)
    inv8 = pow(8, -1, q)

    d = [0, (chirality * inv2) % q]
    i = branch
    j = 1 - i
    C = (2 * (d[i] - d[j])) % q
    assert C != 0

    H = {
        (a, b)
        for a in range(q)
        for b in range(q)
        if (B * a * b - C) % q == 0
    }
    assert len(H) == q - 1

    # Intrinsic quotient map pi_i(a,b) = -B(b-a)^2/8 - d_i.
    pi = {
        (a, b): (-B * (b - a) * (b - a) * inv8 - d[i]) % q
        for a, b in H
    }

    # Every K4 orbit is a pi fiber and conversely.
    fibers: dict[int, set[tuple[int, int]]] = {}
    for p, val in pi.items():
        fibers.setdefault(val, set()).add(p)

    orbits = {K4_orbit(a, b, q) for a, b in H}
    fiber_sets = {frozenset(v) for v in fibers.values()}
    assert orbits == fiber_sets

    # Compare directly with dual-image overlap.
    Ii = {(-B * x * x * inv2 - d[i]) % q for x in range(q)}
    Ij = {(-B * y * y * inv2 - d[j]) % q for y in range(q)}
    assert set(fibers.keys()) == Ii & Ij

    # Orbit-capacity lower bound.
    assert len(orbits) >= (len(H) + 3) // 4

    # Exact Burnside/cyclotomic count.
    expected = (q + 1 + legendre(B * C, q) + legendre(-B * C, q)) // 4
    assert len(orbits) == expected


def main() -> None:
    for q in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        for B in range(1, q):
            for chi in (1, -1):
                for branch in (0, 1):
                    check(q, B, chi, branch)

    # Native q=5 is one regular K4 orbit.
    q = 5
    B = 3
    chi = 1
    inv2 = pow(2, -1, q)
    d = [0, inv2]
    C = (2 * (d[0] - d[1])) % q
    H5 = {(a, b) for a in range(q) for b in range(q) if (B * a * b - C) % q == 0}
    orbits5 = {K4_orbit(a, b, q) for a, b in H5}
    assert len(H5) == 4
    assert len(orbits5) == 1
    assert all(len(o) == 4 for o in orbits5)

    # Native q=53 has 52 points and exactly 13 symmetry classes.
    q = 53
    inv2 = pow(2, -1, q)
    d = [0, inv2]
    C = (2 * (d[0] - d[1])) % q
    H53 = {(a, b) for a in range(q) for b in range(q) if (B * a * b - C) % q == 0}
    orbits53 = {K4_orbit(a, b, q) for a, b in H53}
    assert len(H53) == 52
    assert len(orbits53) == 13

    print("INTRINSIC_K4_QUOTIENT=PASS")
    print("DUAL_OVERLAP_EQUALS_TANGENT_QUOTIENT=PASS")
    print("ORBIT_CAPACITY_BREAKER_BOUND_Q_LE_5=PASS")
    print("NATIVE_Q5_ONE_REGULAR_K4_ORBIT=PASS")
    print("NATIVE_Q53_THIRTEEN_K4_ORBITS=PASS")


if __name__ == "__main__":
    main()
