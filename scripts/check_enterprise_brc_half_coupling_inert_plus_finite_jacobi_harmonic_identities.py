#!/usr/bin/env python3
"""Exact regression for the inert-plus finite Jacobi-jet reduction.

This checker is deliberately finite evidence only.  The theorem-level content
is the algebraic identification of F0,F1,F2,J0,J1 with one terminating
hypergeometric x-jet; the all-prime congruence remains unproved here.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, factorial, gcd, isqrt


def primes_below(limit: int):
    for n in range(2, limit):
        if all(n % d for d in range(2, isqrt(n) + 1)):
            yield n


def frac_mod(x: Fraction, modulus: int) -> int:
    den = x.denominator % modulus
    if gcd(den, modulus) != 1:
        raise AssertionError(f"nonunit denominator modulo {modulus}: {x.denominator}")
    return (x.numerator % modulus) * pow(den, -1, modulus) % modulus


def jet_coefficients(m: int):
    """Return Phi, Phi_x, Phi_xx, Psi, Psi_x at x=m, z=1/2.

    Phi_m(x,z)=sum_{k=0}^{6m} (-x)_k(-2x)_k z^k/(k!)^2.
    Psi_m=(1+12 z d/dz)Phi_m.

    The recurrence for a term f_k(x) at z=1/2 is
      f_{k+1}=f_k * (k-x)(k-2x)/(2(k+1)^2).
    We propagate its value and first two x-derivatives exactly.
    """
    f = Fraction(1)
    fx = Fraction(0)
    fxx = Fraction(0)
    phi = phix = phixx = psi = psix = Fraction(0)

    for k in range(0, 6 * m + 1):
        phi += f
        phix += fx
        phixx += fxx
        weight = 12 * k + 1
        psi += weight * f
        psix += weight * fx

        if k == 6 * m:
            break

        den = 2 * (k + 1) ** 2
        r = Fraction((k - m) * (k - 2 * m), den)
        rx = Fraction(-3 * k + 4 * m, den)
        rxx = Fraction(4, den)
        f, fx, fxx = (
            f * r,
            fx * r + f * rx,
            fxx * r + 2 * fx * rx + f * rxx,
        )

    return phi, phix, phixx, psi, psix


def harmonic_arrays(n: int):
    h = [Fraction(0)] * (n + 1)
    h2 = [Fraction(0)] * (n + 1)
    for j in range(1, n + 1):
        h[j] = h[j - 1] + Fraction(1, j)
        h2[j] = h2[j - 1] + Fraction(1, j * j)
    return h, h2


def frozen_block_coefficients(m: int):
    """Frozen parent F0,F1,F2,J0,J1 formulas, independently replayed."""
    h, h2 = harmonic_arrays(2 * m)
    f0 = f1 = f2 = j0 = j1 = Fraction(0)

    for k in range(m + 1):
        w = Fraction(comb(m, k) * comb(2 * m, k), 2**k)
        ell = (
            -Fraction(1, 6) * (h[m] - h[m - k])
            - Fraction(1, 3) * (h[2 * m] - h[2 * m - k])
        )
        q = Fraction(1, 2) * (
            ell * ell
            - Fraction(1, 36) * (h2[m] - h2[m - k])
            - Fraction(1, 9) * (h2[2 * m] - h2[2 * m - k])
        )
        f0 += w
        f1 += w * ell
        f2 += w * q
        j0 += (12 * k + 1) * w
        j1 += (12 * k + 1) * w * ell

    for k in range(m + 1, 2 * m + 1):
        d = Fraction(
            (-1) ** (m + k)
            * factorial(m)
            * factorial(k - m - 1)
            * factorial(2 * m),
            6 * factorial(2 * m - k) * factorial(k) ** 2 * 2**k,
        )
        corr = (
            Fraction(1, 6) * (h[k - m - 1] - h[m])
            - Fraction(1, 3) * (h[2 * m] - h[2 * m - k])
        )
        f1 += d
        f2 += d * corr
        j1 += (12 * k + 1) * d

    for k in range(2 * m + 1, 6 * m + 1):
        v = Fraction(
            (-1) ** m
            * factorial(m)
            * factorial(2 * m)
            * factorial(k - m - 1)
            * factorial(k - 2 * m - 1),
            18 * factorial(k) ** 2 * 2**k,
        )
        f2 += v

    return f0, f1, f2, j0, j1


def direct_Bs(p: int):
    out = [Fraction(1)]
    for k in range(p - 1):
        out.append(
            out[-1]
            * Fraction((6 * k + 1) * (3 * k + 1), 36 * (k + 1) ** 2)
        )
    return out


def reflected_Cs(m: int):
    if m == 0:
        return [None]
    out = [None, Fraction(1, 10)]
    for r in range(1, m):
        out.append(
            out[-1] * Fraction(36 * r * r, (6 * r + 5) * (3 * r + 2))
        )
    return out


def reflected_R(p: int, bs):
    m = (p - 1) // 6
    cs = reflected_Cs(m)
    sum_c = Fraction(0)
    sum_rc = Fraction(0)
    total = Fraction(0)
    for i in range(1, m + 1):
        sum_c += cs[i]
        sum_rc += i * cs[i]
        inner = (1 + 6 * i) * sum_c - 6 * sum_rc
        total += 2 * bs[i] * inner
    return total


def weighted_ramanujan_sum(p: int):
    # t_n = binom(2n,n)^2 binom(3n,n)/216^n
    t = Fraction(1)
    total = Fraction(1)
    for n in range(p - 1):
        t *= Fraction(
            (2 * n + 1) * (2 * n + 2)
            * (3 * n + 1) * (3 * n + 2) * (3 * n + 3),
            (n + 1) ** 5 * 216,
        )
        total += (6 * (n + 1) + 1) * t
    return total


def check_prime(p: int):
    if p % 24 not in (13, 19):
        raise ValueError("scoped to p == 13 or 19 (mod 24)")
    m = (p - 1) // 6

    phi, phix, phixx, psi, psix = jet_coefficients(m)
    f0, f1, f2, j0, j1 = frozen_block_coefficients(m)

    # Exact theorem-level jet identification.
    assert phi == f0
    assert -phix / 6 == f1
    assert phixx / 72 == f2
    assert psi == j0
    assert -psix / 6 == j1

    bs = direct_Bs(p)
    g = sum(bs, Fraction(0))
    h = sum(((12 * k + 1) * b for k, b in enumerate(bs)), Fraction(0))
    rp = reflected_R(p, bs)

    assert frac_mod(g - (phi - p * phix / 6 + p * p * phixx / 72), p**3) == 0
    assert frac_mod(h - (psi - p * psix / 6), p**2) == 0

    a = phi / p - phix / 6
    r0_residue = frac_mod(a * psi - 1, p)
    r1_residue = frac_mod(
        (a * psi - 1) / p
        - a * psix / 6
        + phixx * psi / 72
        - rp,
        p,
    )
    assert r0_residue == 0
    assert r1_residue == 0

    # Prior-art interface regression: R0 is exactly the mod-p^2 first digit
    # of Z.-W. Sun A14(ii) in the plus classes; R0+R1 is the mod-p^3 digit
    # after the frozen reflected-tail correction.
    sp = weighted_ramanujan_sum(p)
    assert frac_mod(sp - p, p**2) == 0
    assert frac_mod(sp - p, p**3) == 0

    return {"p": p, "m": m, "class_mod_24": p % 24}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=1000)
    args = parser.parse_args()

    rows = []
    for p in primes_below(args.limit):
        if p % 24 in (13, 19):
            rows.append(check_prime(p))

    print(json.dumps({
        "status": "PASS",
        "finite_regression_only": True,
        "prime_limit_exclusive": args.limit,
        "plus_inert_primes_checked": len(rows),
        "class_13_count": sum(r["class_mod_24"] == 13 for r in rows),
        "class_19_count": sum(r["class_mod_24"] == 19 for r in rows),
        "exact_jet_identification_failures": 0,
        "r0_failures": 0,
        "r1_failures": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
