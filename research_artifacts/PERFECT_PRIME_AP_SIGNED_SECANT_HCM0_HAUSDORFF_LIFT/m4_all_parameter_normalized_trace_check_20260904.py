#!/usr/bin/env python3
"""Exact symbolic checker for the m=4 all-parameter normalized trace certificate.

This checker reconstructs the reduced numerator from the frozen quotient family,
uses the explicit rank-one inverse formula, clears rational coefficient content,
and verifies that the primitive numerator polynomial has 804/804 positive
coefficients with the frozen SHA-256 digest.
"""
from __future__ import annotations

import hashlib
import math
import sympy as sp

EXPECTED_SHA256 = "d3f4ab2e04dc270de37880c853a6a9454f5a534e6da8b767c4ee42c26c7b50ae"
EXPECTED_TERMS = 804
EXPECTED_DEGREE = 16
EXPECTED_MIN = 163214609191200
EXPECTED_MAX = 15223190061789668997857280


def main():
    a, c, S = sp.symbols("a c S")
    m, n = 4, 3

    def F(x):
        return sp.prod(m * x + k for k in range(1, m + 1)) / sp.factorial(m - 1)

    x = sp.symbols("x")
    delta = sp.expand(F(x))
    for _ in range(n):
        delta = sp.expand(delta.subs(x, x + 1) - delta)
    assert sp.factor(delta) == 128 * (8 * x + 17)

    def tbar(M):
        return sp.Matrix([
            [sp.binomial(M, col - row) if row < col else 0
             for col in range(1, n + 1)]
            for row in range(n)
        ]) / M

    V = sp.simplify(tbar(4 * a) * tbar(4 * (a + c)).inv())
    expected_V = sp.Matrix([
        [1, -2 * c, c * (-4 * a + 4 * c + 3) / 3],
        [0, 1, -2 * c],
        [0, 0, 1],
    ])
    assert sp.simplify(V - expected_V) == sp.zeros(n)

    P = sp.Matrix([
        [sp.binomial(i, k) if k <= i else 0 for k in range(n)]
        for i in range(n)
    ])
    Pinv = P.inv()

    def h_num_common(r):
        L = sp.prod(m * r + k for k in range(1, m * m + 1))
        Hn = sp.zeros(n)
        for j in range(m):
            dj = sp.prod(m * (r + j) + k for k in range(1, m + 1))
            coeff = (-1) ** j * sp.binomial(n, j) * sp.factorial(n) * (L / dj)
            for u in range(n):
                for v in range(n):
                    Hn[u, v] += coeff * sp.binomial(j, u) * sp.binomial(j, v)
        return Hn.applyfunc(sp.expand), sp.expand(L)

    r = 4 * (S + a)
    s = 4 * (S + a + c)
    Hrn, Lr = h_num_common(r)

    Sden = (-1) ** n * sp.expand(delta.subs(x, s))
    assert sp.factor(Sden) == -128 * (32 * S + 32 * a + 32 * c + 17)

    Fi = [sp.expand(F(s + i)) for i in range(n)]
    Kinv_num = sp.Matrix(n, n, lambda i, j: sp.expand(
        -Fi[i] * Fi[j]
        + (sp.Rational((-1) ** i, sp.binomial(n, i)) * Fi[i] * Sden
           if i == j else 0)
    ))
    Hinv_num = (Pinv * Kinv_num * Pinv.T).applyfunc(sp.expand)

    trace_num = sp.expand(sp.trace(Hinv_num * (V.T * Hrn * V)))
    raw = sp.expand(trace_num - n * Sden * Lr)
    quot, rem = sp.div(raw, c, a, c, S, domain=sp.QQ)
    assert rem == 0

    # Sden<0, so orient numerator by -1.  Clear rational coefficient
    # denominators and divide content to freeze a primitive integer polynomial.
    poly = sp.Poly(-quot, a, c, S, domain=sp.QQ)
    assert all(co.is_positive is True for co in poly.coeffs())

    den_lcm = sp.ilcm(*[int(co.q) for co in poly.coeffs()])
    integer_coeffs = [int(co * den_lcm) for co in poly.coeffs()]
    content = 0
    for value in integer_coeffs:
        content = math.gcd(content, abs(value))
    primitive = [value // content for value in integer_coeffs]

    rows = []
    for (monomial, _), value in zip(poly.terms(), primitive):
        rows.append(f"{monomial[0]},{monomial[1]},{monomial[2]}|{value}")
    digest = hashlib.sha256("\n".join(rows).encode()).hexdigest()

    assert len(primitive) == EXPECTED_TERMS
    assert poly.total_degree() == EXPECTED_DEGREE
    assert min(primitive) == EXPECTED_MIN
    assert max(primitive) == EXPECTED_MAX
    assert digest == EXPECTED_SHA256

    # Ppos = content/den_lcm * P_primitive = 131072/9 * P_primitive.
    assert den_lcm == 9
    assert content == 131072
    assert content // 128 == 1024

    print("PASS m=4 all-parameter normalized trace certificate")
    print("terms:", len(primitive))
    print("total degree:", poly.total_degree())
    print("min coefficient:", min(primitive))
    print("max coefficient:", max(primitive))
    print("sha256:", digest)
    print("identity: trace(H_later^-1 H_earlier)-3 =")
    print("  1024*c*P4 / [9*(32*(S+a+c)+17)*prod_{k=1}^16(16*(S+a)+k)]")


if __name__ == "__main__":
    main()
