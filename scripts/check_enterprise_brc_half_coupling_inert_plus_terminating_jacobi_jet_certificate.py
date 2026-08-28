#!/usr/bin/env python3
"""Deterministic finite regression for the EBP6JT CM/Hasse reduction.

The theorem-level content (proved in the research return) is the Hesse-Hasse
identification and the Deuring-CM vanishing of Q_m(1/2) for p == 13,19 mod 24.
This script is finite evidence only for the remaining unit reciprocity and JT2
second-digit identity.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, gcd, isqrt


def primes_below(limit: int):
    for n in range(2, limit):
        if all(n % d for d in range(2, isqrt(n) + 1)):
            yield n


def frac_mod(x: Fraction, modulus: int) -> int:
    den = x.denominator % modulus
    if gcd(den, modulus) != 1:
        raise AssertionError(f"nonunit denominator modulo {modulus}: {x.denominator}")
    return (x.numerator % modulus) * pow(den, -1, modulus) % modulus


def poly_trim(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_add(a, b, p):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return poly_trim(out, p)


def poly_scale(a, c, p):
    return poly_trim([(c * x) % p for x in a], p)


def poly_x(a, p):
    return [0] + [x % p for x in a]


def poly_eval(a, x, p):
    total = 0
    for c in reversed(a):
        total = (total * x + c) % p
    return total


def poly_deriv_eval(a, x, p):
    total = 0
    for r in range(len(a) - 1, 0, -1):
        total = (total * x + r * a[r]) % p
    return total


def legendre_poly(n: int, p: int):
    """P_n(T) over F_p from the three-term recurrence."""
    p0 = [1]
    if n == 0:
        return p0
    p1 = [0, 1]
    if n == 1:
        return p1
    pm1, pn = p0, p1
    for r in range(1, n):
        # (r+1) P_{r+1} = (2r+1) T P_r - r P_{r-1}.
        rhs = poly_add(poly_scale(poly_x(pn, p), 2 * r + 1, p), poly_scale(pm1, -r, p), p)
        nxt = poly_scale(rhs, pow(r + 1, -1, p), p)
        pm1, pn = pn, nxt
    return pn


def q_polynomial(m: int, p: int):
    """Q_m(S) defined by P_{2m}(T)=Q_m(T^2)."""
    leg = legendre_poly(2 * m, p)
    assert all(leg[i] % p == 0 for i in range(1, len(leg), 2))
    return [leg[2 * r] % p for r in range(m + 1)]


def q_one_minus_z(q, p):
    """Expand Q(1-Z) in the Z basis."""
    out = [0] * len(q)
    for r, c in enumerate(q):
        for k in range(r + 1):
            out[k] = (out[k] + c * comb(r, k) * ((-1) ** k)) % p
    return poly_trim(out, p)


def h_m_coefficients(m: int, p: int):
    # H_m(Z)=Phi_m(m,Z)=sum_{k=0}^m C(m,k)C(2m,k)Z^k.
    return poly_trim([(comb(m, k) * comb(2 * m, k)) % p for k in range(m + 1)], p)


def direct_Bs(p: int):
    out = [Fraction(1)]
    for k in range(p - 1):
        out.append(out[-1] * Fraction((6 * k + 1) * (3 * k + 1), 36 * (k + 1) ** 2))
    return out


def reflected_Cs(m: int):
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


def check_prime(p: int):
    if p % 24 not in (13, 19):
        raise ValueError("scope is p == 13 or 19 (mod 24)")
    m = (p - 1) // 6
    inv2 = pow(2, -1, p)

    # Exact finite quadratic/Legendre polynomial transport over F_p.
    q = q_polynomial(m, p)
    assert q_one_minus_z(q, p) == h_m_coefficients(m, p)

    # The CM/Hasse theorem predicts this zero; derivative simplicity is exact.
    q0 = poly_eval(q, inv2, p)
    qp = poly_deriv_eval(q, inv2, p)
    assert q0 == 0
    assert qp != 0

    # Frozen direct parent scalars. G=g/p is p-adically integral on this lane.
    bs = direct_Bs(p)
    g = sum(bs, Fraction(0))
    h = sum(((12 * k + 1) * b for k, b in enumerate(bs)), Fraction(0))
    rp = reflected_R(p, bs)
    G_mod_p2 = frac_mod(g / p, p * p)
    h_mod_p2 = frac_mod(h, p * p)

    # H_m(1/2)=0 and H_m'(1/2)=-Q_m'(1/2) give Psi=-6Q'_m mod p.
    assert h_mod_p2 % p == (-6 * qp) % p

    unit_reciprocity_residue = (G_mod_p2 * (-6 * qp) - 1) % p
    jt2_residue = (G_mod_p2 * h_mod_p2 - (1 + p * frac_mod(rp, p))) % (p * p)
    assert unit_reciprocity_residue == 0
    assert jt2_residue == 0

    return {
        "p": p,
        "m": m,
        "class_mod_24": p % 24,
        "Q_half_mod_p": q0,
        "Qprime_half_mod_p": qp,
        "unit_reciprocity_residue_mod_p": unit_reciprocity_residue,
        "jt2_residue_mod_p2": jt2_residue,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=2000)
    args = parser.parse_args()

    # Hilbert class polynomial data for discriminant -24.
    A = 2417472
    B = 1707264
    assert 2 * A == 4834944
    assert A * A - 2 * B * B == 14670139392

    rows = [check_prime(p) for p in primes_below(args.limit) if p % 24 in (13, 19)]
    print(json.dumps({
        "status": "PASS",
        "finite_regression_only": True,
        "prime_limit_exclusive": args.limit,
        "plus_inert_primes_checked": len(rows),
        "class_13_count": sum(r["class_mod_24"] == 13 for r in rows),
        "class_19_count": sum(r["class_mod_24"] == 19 for r in rows),
        "quadratic_legendre_transport_failures": 0,
        "cm_hasse_zero_failures": 0,
        "simple_root_failures": 0,
        "unit_reciprocity_failures": 0,
        "jt2_failures": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
