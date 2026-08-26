#!/usr/bin/env python3
"""Exact checker for odd-curvature transparent-basin product/phase formulas."""

from __future__ import annotations

from math import isqrt, prod
from fractions import Fraction


def eps(n: int) -> int:
    return n & 1


def F(B: int, H: int, r: int) -> int:
    return H + (B * r * r + eps(r)) // 2


def legendre(a: int, q: int) -> int:
    a %= q
    if a == 0:
        return 0
    return 1 if pow(a, (q - 1) // 2, q) == 1 else -1


def tau_formula(B: int, q: int) -> int:
    if q == 2:
        return 1 if B % 4 == 3 else 0
    if q == 3:
        return 1 if B % 3 == 0 else 0
    if B % q == 0:
        return q - 2
    return (q - 3 + legendre(B, q) + legendre(-B, q)) // 4


def tau_bruteforce(B: int, q: int) -> int:
    period = 4 if q == 2 else 2 * q
    good = 0
    for H in range(q):
        if all(F(B, H, r) % q != 0 for r in range(period)):
            good += 1
    return good


def crt_basin_bruteforce(B: int, M: int) -> int:
    # The shell sequence modulo squarefree M has period dividing 2M.
    good = 0
    for H in range(M):
        if all(__import__('math').gcd(F(B, H, r), M) == 1 for r in range(2 * M)):
            good += 1
    return good


def primes_upto(n: int) -> list[int]:
    out = []
    for x in range(2, n + 1):
        if all(x % p for p in out if p * p <= x):
            out.append(x)
    return out


def first_n_primes(n: int) -> list[int]:
    out = []
    x = 2
    while len(out) < n:
        if all(x % p for p in out if p * p <= x):
            out.append(x)
        x += 1
    return out


def main() -> None:
    # Local factor formula through a broad finite grid.
    for B in range(1, 80, 2):
        for q in primes_upto(43):
            assert tau_formula(B, q) == tau_bruteforce(B, q), (B, q)

    # Exact CRT product theorem on manageable squarefree wheels.
    for B in (3, 15, 39, 51, 7, 21):
        for qs in ((2, 3), (2, 5), (3, 5), (2, 3, 5), (2, 3, 7), (2, 5, 7)):
            M = prod(qs)
            expected = prod(tau_formula(B, q) for q in qs)
            got = crt_basin_bruteforce(B, M)
            assert got == expected, (B, qs, got, expected)

    # First-break extinction dimensions for representative phases.
    P = 1
    theta = 1
    ps = first_n_primes(19)
    native = []
    for d, q in enumerate(ps, 1):
        P *= q
        theta *= tau_formula(3, q)
        native.append((d, q, theta))
    assert native[0][2] == 1
    assert native[1][2] == 1
    assert all(x[2] == 0 for x in native[2:])

    # No-break classes remain positive through d=19 and match frozen endpoints.
    expected_d19 = {
        15: 13948526592000,
        39: 19670999040000,
        51: 29208453120000,
    }
    P19 = prod(ps)
    assert P19 == 7858321551080267055879090
    for B, expected in expected_d19.items():
        theta = prod(tau_formula(B, q) for q in ps)
        assert theta == expected, (B, theta, expected)
        assert theta > 0

    # Complete no-break phase modulo60.
    no_break = []
    for B in range(1, 60, 2):
        if all(tau_formula(B, q) > 0 for q in (2, 3, 5)):
            no_break.append(B)
    assert no_break == [15, 39, 51]

    # Exact d19 densities.
    dens = {
        B: Fraction(expected, P19)
        for B, expected in expected_d19.items()
    }
    assert float(dens[15]) > 1.7e-12
    assert float(dens[51]) < 3.8e-12

    print("LOCAL_TAU_FORMULA=PASS")
    print("CRT_TRANSPARENT_BASIN_PRODUCT=PASS")
    print("NATIVE_B3_EXTINCTION_DIMENSION=3")
    print("NO_BREAK_MOD60={15,39,51}")
    print("D19_THETA_B15=13948526592000")
    print("D19_THETA_B39=19670999040000")
    print("D19_THETA_B51=29208453120000")
    print("ASYMPTOTIC_STEP=ANALYTIC_PROOF_USES_CLASSICAL_MERTENS_AND_DIRICHLET_L1")


if __name__ == "__main__":
    main()
