#!/usr/bin/env python3
"""Exact sparse-symbolic checker for the m=6 all-parameter M6 certificate.

The script reconstructs the synchronized quotient reduction from the frozen
Pascal/Hausdorff data, uses the exact rank-one inverse numerator, and verifies
that the oriented primitive numerator of

    tr(Hcal_(a+c)^(-1) Hcal_a) - 5

has 6214/6214 positive coefficients. No floating-point arithmetic is used.
"""
from __future__ import annotations

import hashlib
import math
from math import comb, factorial
import sympy as sp

EXPECTED_TERMS = 6214
EXPECTED_DEGREE = 36
EXPECTED_MIN = 4579782756145393414891192920000000
EXPECTED_MAX = 6306341609694513654383029565571237172427478203022182449152000
EXPECTED_SHA256 = "7e1b1042aba54c874bae3b57fbff13cd6d3c22fafc455331390c2fa24918f13a"
EXPECTED_DEN_LCM = 5
EXPECTED_CONTENT = 51998697814228992


def main():
    a, c, S = sp.symbols("a c S")
    variables = (a, c, S)
    QQ = sp.QQ
    m, n = 6, 5

    def poly(expr=0):
        return sp.Poly(expr, *variables, domain=QQ)

    zero, one = poly(0), poly(1)

    def matmul(A, B):
        rows, inner, cols = len(A), len(B), len(B[0])
        out = [[zero for _ in range(cols)] for __ in range(rows)]
        for i in range(rows):
            for k in range(inner):
                if A[i][k].is_zero:
                    continue
                for j in range(cols):
                    if not B[k][j].is_zero:
                        out[i][j] = out[i][j] + A[i][k] * B[k][j]
        return out

    def trans(A):
        return [list(row) for row in zip(*A)]

    def trace(A):
        out = zero
        for i in range(len(A)):
            out = out + A[i][i]
        return out

    def binom_over_M(M, h):
        # binom(M,h)/M, h>=1; polynomial because the factor M cancels.
        expr = sp.Rational(1, factorial(h))
        for t in range(1, h):
            expr *= M - t
        return poly(expr)

    def tbar(M):
        return [[binom_over_M(M, col - row) if row < col else zero
                 for col in range(1, n + 1)]
                for row in range(n)]

    def inv_unit_upper(A):
        size = len(A)
        B = [[zero for _ in range(size)] for __ in range(size)]
        for i in range(size):
            B[i][i] = one
        for j in range(size):
            for i in range(j - 1, -1, -1):
                acc = zero
                for k in range(i + 1, j + 1):
                    acc = acc + A[i][k] * B[k][j]
                B[i][j] = -acc
        return B

    # F=mu^{-1} and its n-th finite difference.
    x = sp.symbols("x")
    Fexpr = sp.prod(m * x + k for k in range(1, m + 1)) / factorial(m - 1)
    delta = sp.Poly(Fexpr, x, domain=QQ)
    for _ in range(n):
        delta = sp.Poly(delta.as_expr().subs(x, x + 1) - delta.as_expr(), x, domain=QQ)
    assert sp.factor(delta.as_expr()) == 23328 * (12 * x + 37)

    # Normalized transition V=Tbar_(6a) Tbar_(6(a+c))^{-1}.
    V = matmul(tbar(6 * a), inv_unit_upper(tbar(6 * (a + c))))

    # Fixed leading Pascal matrix and inverse.
    P = sp.Matrix([[sp.binomial(i, k) if k <= i else 0
                    for k in range(n)] for i in range(n)])
    Pinv = P.inv()
    PinvP = [[poly(Pinv[i, j]) for j in range(n)] for i in range(n)]

    # Common-denominator numerator H_r = Hn/Lr at r=6(S+a).
    r = 6 * (S + a)
    factors = [poly(6 * r + k) for k in range(1, m * m + 1)]
    Lr = one
    for factor in factors:
        Lr = Lr * factor

    Hn = [[zero for _ in range(n)] for __ in range(n)]
    for j in range(m):
        complement = one
        lo = j * m
        for idx, factor in enumerate(factors):
            if not (lo <= idx < lo + m):
                complement = complement * factor
        complement = complement.mul_ground(((-1) ** j) * comb(n, j) * factorial(n))
        for u in range(n):
            if u > j:
                continue
            for v in range(n):
                if v <= j:
                    Hn[u][v] = Hn[u][v] + complement.mul_ground(comb(j, u) * comb(j, v))

    # Exact rank-one inverse numerator at s=6(S+a+c).
    s = 6 * (S + a + c)
    Sden = poly(((-1) ** n) * delta.as_expr().subs(x, s))
    assert sp.factor(Sden.as_expr()) == -23328 * (72 * (S + a + c) + 37)

    Fi = [poly(Fexpr.subs(x, s + i)) for i in range(n)]
    Kinv = [[zero for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            value = -(Fi[i] * Fi[j])
            if i == j:
                value = value + (Fi[i] * Sden).mul_ground(sp.Rational((-1) ** i, comb(n, i)))
            Kinv[i][j] = value
    Hinv = matmul(PinvP, matmul(Kinv, trans(PinvP)))

    pulled = matmul(trans(V), matmul(Hn, V))
    trace_num = trace(matmul(Hinv, pulled))
    raw = trace_num - (Sden * Lr).mul_ground(n)

    # raw is exactly divisible by c. Since Sden<0 for the target region,
    # orient by -1 before freezing the positive primitive polynomial.
    raw_dict = raw.as_dict()
    assert raw_dict and all(exp[1] >= 1 for exp in raw_dict)
    q = sp.Poly.from_dict(
        {(exp[0], exp[1] - 1, exp[2]): coeff for exp, coeff in raw_dict.items()},
        variables,
        domain=QQ,
    )
    q = -q
    assert all(coeff > 0 for coeff in q.coeffs())

    den_lcm = 1
    for coeff in q.coeffs():
        den_lcm = sp.ilcm(den_lcm, int(coeff.q))
    integer_coeffs = [int(coeff * den_lcm) for coeff in q.coeffs()]
    content = 0
    for value in integer_coeffs:
        content = math.gcd(content, abs(value))
    primitive = [value // content for value in integer_coeffs]

    rows = []
    for (monomial, _), value in zip(q.terms(), primitive):
        rows.append(f"{monomial[0]},{monomial[1]},{monomial[2]}|{value}")
    digest = hashlib.sha256("\n".join(rows).encode()).hexdigest()

    assert len(primitive) == EXPECTED_TERMS
    assert q.total_degree() == EXPECTED_DEGREE
    assert min(primitive) == EXPECTED_MIN
    assert max(primitive) == EXPECTED_MAX
    assert digest == EXPECTED_SHA256
    assert den_lcm == EXPECTED_DEN_LCM
    assert content == EXPECTED_CONTENT
    assert sp.factor(sp.Rational(content, den_lcm) / 23328) == sp.Rational(2229025112064, 5)

    print("PASS m=6 all-parameter normalized trace certificate")
    print("terms:", len(primitive))
    print("total degree:", q.total_degree())
    print("min coefficient:", min(primitive))
    print("max coefficient:", max(primitive))
    print("sha256:", digest)
    print("identity: trace(H_later^-1 H_earlier)-5 =")
    print("  (2229025112064/5)*c*P6 / [(72*(S+a+c)+37)*prod_{k=1}^36(36*(S+a)+k)]")


if __name__ == "__main__":
    main()
