#!/usr/bin/env python3
"""Exact checker for RS-ADDMUL-FORMAL-GROUP-INTERPOLATION.

Standard-library only. It checks:
1. exact F_c associativity and shifted multiplicative transport over Z;
2. integer inverse-domain classification;
3. finite Z/N shifted-coordinate image/fiber/inverse classification;
4. the finite-depth integer-safety criterion for formal log/exp coefficients;
5. the sharp degree-4 associativity defect of a degree-3 truncation of the
   strict integral formal group transported by h(t)=t+t^2.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial, gcd
from typing import Dict, Tuple

Mon = Tuple[int, int, int]
Poly = Dict[Mon, int]


def F(c: int, x: int, y: int) -> int:
    return x + y + c * x * y


def shifted(c: int, x: int) -> int:
    return 1 + c * x


def primes_upto(n: int) -> list[int]:
    out: list[int] = []
    for k in range(2, n + 1):
        ok = True
        q = 2
        while q * q <= k:
            if k % q == 0:
                ok = False
                break
            q += 1
        if ok:
            out.append(k)
    return out


def primorial_upto(n: int) -> int:
    out = 1
    for p in primes_upto(n):
        out *= p
    return out


def log_jet_integral(c: int, d: int) -> bool:
    return all(
        Fraction(((-1) ** (n + 1)) * c ** (n - 1), n).denominator == 1
        for n in range(1, d + 1)
    )


def exp_jet_integral(c: int, d: int) -> bool:
    return all(
        Fraction(c ** (n - 1), factorial(n)).denominator == 1
        for n in range(1, d + 1)
    )


def p_add(a: Poly, b: Poly) -> Poly:
    out = dict(a)
    for m, coeff in b.items():
        out[m] = out.get(m, 0) + coeff
        if out[m] == 0:
            del out[m]
    return out


def p_neg(a: Poly) -> Poly:
    return {m: -coeff for m, coeff in a.items()}


def p_sub(a: Poly, b: Poly) -> Poly:
    return p_add(a, p_neg(b))


def p_mul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = (ma[0] + mb[0], ma[1] + mb[1], ma[2] + mb[2])
            out[m] = out.get(m, 0) + ca * cb
    return {m: coeff for m, coeff in out.items() if coeff}


def p_pow(a: Poly, n: int) -> Poly:
    out: Poly = {(0, 0, 0): 1}
    for _ in range(n):
        out = p_mul(out, a)
    return out


def p_scale(a: Poly, scale: int) -> Poly:
    return {m: scale * coeff for m, coeff in a.items() if scale * coeff}


def hom_part(a: Poly, degree: int) -> Poly:
    return {m: coeff for m, coeff in a.items() if sum(m) == degree and coeff}


def subst_bivar(
    coeffs: dict[tuple[int, int], int], u: Poly, v: Poly
) -> Poly:
    out: Poly = {}
    for (i, j), coeff in coeffs.items():
        out = p_add(out, p_scale(p_mul(p_pow(u, i), p_pow(v, j)), coeff))
    return out


def check_integer_law() -> int:
    checks = 0
    for c in range(-10, 11):
        for x in range(-8, 9):
            assert F(c, x, 0) == x
            for y in range(-8, 9):
                assert F(c, x, y) == F(c, y, x)
                assert shifted(c, F(c, x, y)) == shifted(c, x) * shifted(c, y)
                for z in range(-5, 6):
                    assert F(c, F(c, x, y), z) == F(c, x, F(c, y, z))
                    checks += 1
    return checks


def check_integer_inverses() -> int:
    checks = 0
    for c in range(-12, 13):
        for x in range(-60, 61):
            u = 1 + c * x
            if c == 0:
                y = -x
                assert F(c, x, y) == 0
                expected = True
            else:
                expected = u in (-1, 1)
                if expected:
                    assert (-x) % u == 0
                    y = (-x) // u
                    assert F(c, x, y) == 0
                    assert shifted(c, y) == u
            brute = any(F(c, x, y) == 0 for y in range(-80, 81))
            assert brute == expected
            checks += 1
    return checks


def check_finite_rings() -> int:
    checks = 0
    for n in range(2, 41):
        for c0 in range(-20, 21):
            c = c0 % n
            g = gcd(c, n)
            image = {(1 + c * x) % n for x in range(n)}
            assert len(image) == n // g
            fibers: dict[int, list[int]] = {}
            for x in range(n):
                fibers.setdefault((1 + c * x) % n, []).append(x)
            assert {len(v) for v in fibers.values()} == {g}
            for x in range(n):
                for y in range(n):
                    lhs = (1 + c * ((x + y + c * x * y) % n)) % n
                    rhs = ((1 + c * x) * (1 + c * y)) % n
                    assert lhs == rhs
                u = (1 + c * x) % n
                invertible = gcd(u, n) == 1
                inverses = [
                    y for y in range(n) if (x + y + c * x * y) % n == 0
                ]
                assert bool(inverses) == invertible
                if invertible:
                    y = (-x * pow(u, -1, n)) % n
                    assert y in inverses
                    assert ((1 + c * y) * u) % n == 1
                checks += 1
    return checks


def check_integral_jets() -> int:
    checks = 0
    for c in range(-210, 211):
        for d in range(1, 9):
            p = primorial_upto(d)
            expected = c % p == 0
            assert log_jet_integral(c, d) == expected
            assert exp_jet_integral(c, d) == expected
            checks += 1
    return checks


def check_truncation_defect() -> int:
    # h(t)=t+t^2, h^{-1}(s)=s-s^2+2s^3-5s^4+...
    # The exact transported formal law has:
    # F = x+y-2xy+4x^2y+4xy^2
    #     -8x^3y-20x^2y^2-8xy^3 + O(5).
    # G3 is the ordinary degree<=3 polynomial truncation.
    g3 = {
        (1, 0): 1,
        (0, 1): 1,
        (1, 1): -2,
        (2, 1): 4,
        (1, 2): 4,
    }
    h4 = {(3, 1): -8, (2, 2): -20, (1, 3): -8}

    X: Poly = {(1, 0, 0): 1}
    Y: Poly = {(0, 1, 0): 1}
    Z: Poly = {(0, 0, 1): 1}

    gxy = subst_bivar(g3, X, Y)
    left = subst_bivar(g3, gxy, Z)
    gyz = subst_bivar(g3, Y, Z)
    right = subst_bivar(g3, X, gyz)
    associator = p_sub(left, right)

    expected4: Poly = {
        (2, 1, 1): -16,
        (1, 1, 2): 16,
    }
    assert hom_part(associator, 1) == {}
    assert hom_part(associator, 2) == {}
    assert hom_part(associator, 3) == {}
    assert hom_part(associator, 4) == expected4

    hxy = subst_bivar(h4, X, Y)
    hxpy_z = subst_bivar(h4, p_add(X, Y), Z)
    hyz = subst_bivar(h4, Y, Z)
    hx_ypz = subst_bivar(h4, X, p_add(Y, Z))
    additive_coboundary = p_sub(
        p_add(hxy, hxpy_z), p_add(hyz, hx_ypz)
    )
    assert p_scale(hom_part(additive_coboundary, 4), -1) == expected4
    return len(associator)


def main() -> None:
    counts = {
        "integer_assoc_transport": check_integer_law(),
        "integer_inverse_domain": check_integer_inverses(),
        "finite_ring_states": check_finite_rings(),
        "integral_log_exp_jets": check_integral_jets(),
        "truncation_associator_terms": check_truncation_defect(),
    }
    print("PASS ADDMUL_FORMAL_GROUP_INTERPOLATION")
    for key, value in counts.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
