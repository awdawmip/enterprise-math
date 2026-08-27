#!/usr/bin/env python3
"""Exact regression checker for the inert-plus reflected derivative-product bridge.

Finite regression only.  The theorem-level output of the task is the exact
second-order parameter-deformation reduction, not this bounded scan.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, factorial, gcd, isqrt


def primes_below(limit: int):
    for n in range(2, limit):
        ok = True
        for d in range(2, isqrt(n) + 1):
            if n % d == 0:
                ok = False
                break
        if ok:
            yield n


def frac_mod(x: Fraction, modulus: int) -> int:
    den = x.denominator % modulus
    if gcd(den, modulus) != 1:
        raise AssertionError(f"nonunit denominator modulo {modulus}: {x.denominator}")
    return (x.numerator % modulus) * pow(den, -1, modulus) % modulus


def harmonic_arrays(n: int):
    h = [Fraction(0)] * (n + 1)
    h2 = [Fraction(0)] * (n + 1)
    for j in range(1, n + 1):
        h[j] = h[j - 1] + Fraction(1, j)
        h2[j] = h2[j - 1] + Fraction(1, j * j)
    return h, h2


def direct_Bs(p: int):
    # B_{k+1}/B_k=((6k+1)(3k+1))/(36(k+1)^2).
    out = [Fraction(1)]
    for k in range(p - 1):
        out.append(out[-1] * Fraction((6 * k + 1) * (3 * k + 1), 36 * (k + 1) ** 2))
    return out


def taylor_coefficients(m: int):
    """F0,F1,F2,J0,J1 for b_{m,k}(eps) at eps=0.

    b_{m,k}(eps)=(-m+eps/6)_k(-2m+eps/3)_k / ((k!)^2 2^k).
    For p=6m+1, B_k=b_{m,k}(p).
    """
    h, h2 = harmonic_arrays(2 * m)
    f0 = f1 = f2 = j0 = j1 = Fraction(0)

    # Low block: k<=m, order 0.
    for k in range(m + 1):
        w = Fraction(comb(m, k) * comb(2 * m, k), 2**k)
        ell = -Fraction(1, 6) * (h[m] - h[m - k]) - Fraction(1, 3) * (h[2 * m] - h[2 * m - k])
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

    # Middle block: m<k<=2m, order 1.
    for k in range(m + 1, 2 * m + 1):
        d = Fraction(
            (-1) ** (m + k)
            * factorial(m)
            * factorial(k - m - 1)
            * factorial(2 * m),
            6 * factorial(2 * m - k) * factorial(k) ** 2 * 2**k,
        )
        corr = Fraction(1, 6) * (h[k - m - 1] - h[m]) - Fraction(1, 3) * (h[2 * m] - h[2 * m - k])
        f1 += d
        f2 += d * corr
        j1 += (12 * k + 1) * d

    # High block: 2m<k<=6m, order 2.
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


def reflected_Cs(m: int):
    # C_1=1/10 and C_{r+1}/C_r=36r^2/((6r+5)(3r+2)).
    if m == 0:
        return [None]
    out = [None, Fraction(1, 10)]
    for r in range(1, m):
        out.append(out[-1] * Fraction(36 * r * r, (6 * r + 5) * (3 * r + 2)))
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


def direct_unweighted_U(p: int):
    # A_n/216^n with A_n=(2n)!(3n)!/(n!)^5.
    terms = [Fraction(1)]
    for n in range(p - 1):
        num = (2 * n + 1) * (2 * n + 2) * (3 * n + 1) * (3 * n + 2) * (3 * n + 3)
        den = (n + 1) ** 5 * 216
        terms.append(terms[-1] * Fraction(num, den))
    return sum(terms, Fraction(0))


def check_prime(p: int):
    if p % 24 not in (13, 19):
        raise ValueError("checker is scoped to plus inert residue classes")
    m = (p - 1) // 6
    bs = direct_Bs(p)
    g = sum(bs, Fraction(0))
    h = sum(((12 * k + 1) * b for k, b in enumerate(bs)), Fraction(0))
    r = reflected_R(p, bs)
    f0, f1, f2, j0, j1 = taylor_coefficients(m)

    # Structural Taylor reconstruction.
    assert frac_mod(g, p**3) == frac_mod(f0 + p * f1 + p * p * f2, p**3)
    assert frac_mod(h, p**2) == frac_mod(j0 + p * j1, p**2)

    # Independent finite check of the imported unweighted inert congruence and p|G.
    u = direct_unweighted_U(p)
    assert frac_mod(u, p * p) == 0
    assert frac_mod(g, p) == 0

    # Parent reduced product target, regression only.
    rmod = frac_mod(r, p)
    lhs = frac_mod(g, p**3) * frac_mod(h, p**3)
    assert (lhs - (p + p * p * rmod)) % (p**3) == 0

    # Exact two-scalar reduction.
    a = f0 / p + f1
    assert (frac_mod(a, p) * frac_mod(j0, p) - 1) % p == 0
    correction = (a * j0 - 1) / p + a * j1 + f2 * j0 - r
    assert frac_mod(correction, p) == 0

    return {"p": p, "class_mod_24": p % 24, "m": m}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=500)
    args = parser.parse_args()
    records = []
    for p in primes_below(args.limit):
        if p % 24 in (13, 19):
            records.append(check_prime(p))
    counts = {str(c): sum(r["class_mod_24"] == c for r in records) for c in (13, 19)}
    print(json.dumps({
        "status": "PASS",
        "finite_regression_only": True,
        "prime_limit_exclusive": args.limit,
        "plus_inert_primes_checked": len(records),
        "class_counts": counts,
        "failures": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
