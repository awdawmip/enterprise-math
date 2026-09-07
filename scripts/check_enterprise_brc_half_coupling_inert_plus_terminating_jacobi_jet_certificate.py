#!/usr/bin/env python3
"""Exact finite regression for the EBP6JT CM-Hasse strict reduction.

Finite evidence only: theorem status of CM0/SIMPLE comes from the return proof.
UR and JT2/LIFT are checked for falsification/regression, never promoted by scan.
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


def trim(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return trim(out, p)


def scale(a, c, p):
    return trim([(c * x) % p for x in a], p)


def legendre_poly(n: int, p: int):
    if n == 0:
        return [1]
    pm1, pn = [1], [0, 1]
    for r in range(1, n):
        tpn = [0] + pn
        rhs = add(scale(tpn, 2 * r + 1, p), scale(pm1, -r, p), p)
        nxt = scale(rhs, pow(r + 1, -1, p), p)
        pm1, pn = pn, nxt
    return pn


def q_poly(m: int, p: int):
    P = legendre_poly(2 * m, p)
    assert all(P[i] % p == 0 for i in range(1, len(P), 2))
    return [P[2 * r] % p for r in range(m + 1)]


def eval_poly(a, x, p):
    y = 0
    for c in reversed(a):
        y = (y * x + c) % p
    return y


def eval_deriv(a, x, p):
    y = 0
    for r in range(len(a) - 1, 0, -1):
        y = (y * x + r * a[r]) % p
    return y


def q_one_minus_z(q, p):
    out = [0] * len(q)
    for r, c in enumerate(q):
        for k in range(r + 1):
            out[k] = (out[k] + c * comb(r, k) * ((-1) ** k)) % p
    return trim(out, p)


def h_coeffs(m, p):
    return trim([comb(m, k) * comb(2 * m, k) % p for k in range(m + 1)], p)


def direct_Bs(p: int):
    out = [Fraction(1)]
    for k in range(p - 1):
        out.append(out[-1] * Fraction((6 * k + 1) * (3 * k + 1), 36 * (k + 1) ** 2))
    return out


def reflected_Cs(m: int):
    out = [None, Fraction(1, 10)]
    for r in range(1, m):
        out.append(out[-1] * Fraction(36 * r * r, (6 * r + 5) * (3 * r + 2)))
    return out


def reflected_R(p: int, bs):
    m = (p - 1) // 6
    cs = reflected_Cs(m)
    sc = Fraction(0)
    src = Fraction(0)
    total = Fraction(0)
    for i in range(1, m + 1):
        sc += cs[i]
        src += i * cs[i]
        total += 2 * bs[i] * ((1 + 6 * i) * sc - 6 * src)
    return total


def check_prime(p: int):
    assert p % 24 in (13, 19)
    m = (p - 1) // 6
    inv2 = pow(2, -1, p)

    q = q_poly(m, p)
    assert q_one_minus_z(q, p) == h_coeffs(m, p)

    q0 = eval_poly(q, inv2, p)
    qp = eval_deriv(q, inv2, p)
    assert q0 == 0
    assert qp != 0

    bs = direct_Bs(p)
    g = sum(bs, Fraction(0))
    h = sum(((12 * k + 1) * b for k, b in enumerate(bs)), Fraction(0))
    rp = reflected_R(p, bs)

    G = frac_mod(g / p, p * p)
    h2 = frac_mod(h, p * p)
    assert h2 % p == (-6 * qp) % p

    ur = (G * (-6 * qp) - 1) % p
    jt2 = (G * h2 - (1 + p * frac_mod(rp, p))) % (p * p)
    assert ur == 0
    assert jt2 == 0

    return p % 24


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=2000)
    args = parser.parse_args()

    A = 2417472
    B = 1707264
    assert 2 * A == 4834944
    assert A * A - 2 * B * B == 14670139392

    classes = [check_prime(p) for p in primes_below(args.limit) if p % 24 in (13, 19)]
    print(json.dumps({
        "status": "PASS",
        "finite_regression_only": True,
        "prime_limit_exclusive": args.limit,
        "target_primes_checked": len(classes),
        "class_13_count": classes.count(13),
        "class_19_count": classes.count(19),
        "quadratic_legendre_transport_failures": 0,
        "cm_hasse_zero_failures": 0,
        "simple_root_failures": 0,
        "unit_reciprocity_failures": 0,
        "jt2_failures": 0
    }, sort_keys=True))


if __name__ == "__main__":
    main()
