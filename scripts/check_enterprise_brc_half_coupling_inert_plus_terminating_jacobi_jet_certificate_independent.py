#!/usr/bin/env python3
"""Independent finite regression for the recovered EBP6JT strict reduction.

This checker is deliberately structurally distinct from the predecessor checker:
it evaluates P_{2m}(t) and P'_{2m}(t) by the differentiated Legendre three-term
recurrence in F_p[t]/(t^2-1/2), rather than building the full coefficient array.
Finite success is regression/falsification evidence only for UR and JT2/LIFT.
"""
from __future__ import annotations

import json
from fractions import Fraction
from math import gcd, isqrt


def primes_below(limit: int):
    for n in range(2, limit):
        if all(n % d for d in range(2, isqrt(n) + 1)):
            yield n


def frac_mod(x: Fraction, modulus: int) -> int:
    den = x.denominator % modulus
    if gcd(den, modulus) != 1:
        raise AssertionError(f"nonunit denominator modulo {modulus}: {x.denominator}")
    return (x.numerator % modulus) * pow(den, -1, modulus) % modulus


def add(x, y, p):
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def scale(x, c, p):
    return (x[0] * c % p, x[1] * c % p)


def mul_t(x, inv2, p):
    # (a + b t)t = b/2 + a t because t^2 = 1/2.
    return (x[1] * inv2 % p, x[0] % p)


def legendre_value_derivative(n: int, p: int):
    """Return P_n(t), P'_n(t) in F_p[t]/(t^2-1/2)."""
    inv2 = pow(2, -1, p)
    if n == 0:
        return (1, 0), (0, 0)
    pm1, pn = (1, 0), (0, 1)
    dm1, dn = (0, 0), (1, 0)
    for r in range(1, n):
        inv = pow(r + 1, -1, p)
        nxt = scale(add(scale(mul_t(pn, inv2, p), 2 * r + 1, p),
                        scale(pm1, -r, p), p), inv, p)
        # (r+1)P'_{r+1}=(2r+1)(P_r+tP'_r)-rP'_{r-1}.
        dnext = scale(add(
            scale(add(pn, mul_t(dn, inv2, p), p), 2 * r + 1, p),
            scale(dm1, -r, p), p
        ), inv, p)
        pm1, pn = pn, nxt
        dm1, dn = dn, dnext
    return pn, dn


def q_value_and_derivative(m: int, p: int):
    value, deriv = legendre_value_derivative(2 * m, p)
    # P_{2m}(t)=Q_m(t^2), so at t^2=1/2 value is scalar and
    # P'_{2m}(t)=2t Q'_m(1/2) is pure t.
    assert value[1] % p == 0
    assert deriv[0] % p == 0
    q0 = value[0] % p
    # deriv[1]*t = 2*t*Q', hence Q'=deriv[1]/2.
    qp = deriv[1] * pow(2, -1, p) % p
    return q0, qp


def direct_Bs(p: int):
    out = [Fraction(1)]
    for k in range(p - 1):
        out.append(
            out[-1]
            * Fraction((6 * k + 1) * (3 * k + 1), 36 * (k + 1) ** 2)
        )
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
    q0, qp = q_value_and_derivative(m, p)
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
    classes = [check_prime(p) for p in primes_below(2000) if p % 24 in (13, 19)]
    assert len(classes) == 77
    assert classes.count(13) == 40
    assert classes.count(19) == 37
    print(json.dumps({
        "status": "PASS",
        "independent_legendre_evaluator": "DIFFERENTIATED_RECURRENCE_IN_FP_T_MOD_T2_MINUS_HALF",
        "finite_regression_only": True,
        "prime_limit_exclusive": 2000,
        "target_primes_checked": 77,
        "class_13_count": 40,
        "class_19_count": 37,
        "cm0_failures": 0,
        "simple_failures": 0,
        "unit_reciprocity_failures": 0,
        "jt2_lift_failures": 0
    }, sort_keys=True))


if __name__ == "__main__":
    main()
