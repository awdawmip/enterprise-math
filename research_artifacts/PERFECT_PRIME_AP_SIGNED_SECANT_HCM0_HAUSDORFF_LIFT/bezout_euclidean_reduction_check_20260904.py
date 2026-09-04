#!/usr/bin/env python3
"""Exact regression for the all-m Bezout/Euclidean reduction used by HCM0.

The symbolic proof is in the paired checkpoint.  This script uses only
fractions.Fraction and verifies the identities for a finite exact regression
set; finite verification is not the all-m proof.
"""
from __future__ import annotations

import json
from fractions import Fraction as F
from math import comb, factorial


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def psub(a, b):
    n = max(len(a), len(b))
    out = [F(0)] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pprod_linear(roots):
    p = [F(1)]
    for r in roots:
        p = pmul(p, [F(-r), F(1)])
    return p


def pdivmod(a, b):
    a = [F(x) for x in a]
    b = [F(x) for x in b]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    while len(b) > 1 and b[-1] == 0:
        b.pop()
    if b == [0]:
        raise ZeroDivisionError
    q = [F(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        k = len(a) - len(b)
        c = a[-1] / b[-1]
        q[k] += c
        for j in range(len(b)):
            a[k + j] -= c * b[j]
        while len(a) > 1 and a[-1] == 0:
            a.pop()
    return q, a


def bezout(f, g, N):
    """B for (f(y)g(x)-f(x)g(y))/(x-y), powers 0..N-1."""
    B = [[F(0) for _ in range(N)] for __ in range(N)]
    for a, fa in enumerate(f):
        if not fa:
            continue
        for b, gb in enumerate(g):
            if not gb or a == b:
                continue
            c = fa * gb
            if b > a:
                for k in range(b - a):
                    i, j = b - 1 - k, a + k
                    if i < N and j < N:
                        B[i][j] += c
            else:
                for k in range(a - b):
                    i, j = a - 1 - k, b + k
                    if i < N and j < N:
                        B[i][j] -= c
    return B


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def inverse(A):
    n = len(A)
    M = [[F(A[i][j]) for j in range(n)] + [F(int(i == j)) for j in range(n)]
         for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c]), None)
        if p is None:
            raise ZeroDivisionError("singular")
        if p != c:
            M[c], M[p] = M[p], M[c]
        z = M[c][c]
        M[c] = [x / z for x in M[c]]
        for r in range(n):
            if r == c:
                continue
            z = M[r][c]
            if z:
                M[r] = [M[r][j] - z * M[c][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def scale(A, c):
    return [[F(c) * x for x in row] for row in A]


def submat(A, rows, cols):
    return [[A[i][j] for j in cols] for i in rows]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def outer(a, b):
    return [[x * y for y in b] for x in a]


def case(m, c):
    n = m - 1
    X = [F(-c - i - 1) for i in range(m)]
    Y = [F(m * j) for j in range(m)]
    p = pprod_linear(Y)
    q = pprod_linear(X)
    r = psub(q, p)
    quotient, t = pdivmod(p, r)

    # A_c and full monomial moment matrix, powers 0..n.
    adiag = []
    for i in range(m):
        den = 1
        for j in range(m):
            den *= i + 1 + c + m * j
        E = F(m ** n * factorial(n), den)
        adiag.append(F((-1) ** i * comb(n, i)) * E)
    V = [[X[i] ** k for k in range(m)] for i in range(m)]
    M = matmul(transpose(V), matmul([[adiag[i] if i == j else F(0) for j in range(m)] for i in range(m)], V))

    B = bezout(p, q, m)
    Binv = inverse(B)
    kappa = F((-1) ** m * m ** n * factorial(n) ** 2)
    assert M == scale(Binv, kappa)

    # Highest-power scalar and Schur complement.
    a = r[-1]
    expected_a = F(m) * (F(c) + F(m * m + 1, 2))
    assert a == expected_a > 0
    assert B[-1][-1] == -a
    top = submat(B, range(n), range(n))
    edge = [B[i][-1] for i in range(n)]
    schur = msub(top, scale(outer(edge, edge), F(1, 1) / B[-1][-1]))
    Bt = bezout(r, t, n)
    assert schur == scale(Bt, -1)

    # First Euclidean quotient is linear with slope 1/a; remainder is lower degree.
    assert len(quotient) == 2 and quotient[1] == F(1, 1) / a
    assert len(t) <= n

    # Quotient Gram identity G_c = -kappa Bez(r,t)^(-1).
    G = submat(M, range(n), range(n))
    assert G == scale(inverse(Bt), -kappa)

    return {
        "m": m,
        "c": c,
        "a_c": f"{a.numerator}/{a.denominator}",
        "full_moment_equals_kappa_bezout_inverse": True,
        "schur_equals_minus_next_bezout": True,
        "quotient_gram_equals_minus_kappa_next_bezout_inverse": True,
    }


def main():
    rows = []
    for m in range(2, 7):
        for c in (0, m * m, 2 * m * m):
            rows.append(case(m, c))
    print(json.dumps({
        "schema": "PERFECT_PRIME_HCM0_BEZOUT_EUCLIDEAN_REDUCTION_REGRESSION_V1",
        "arithmetic": "exact fractions.Fraction",
        "finite_regression": rows,
        "symbolic_proof_location": "paired checkpoint markdown",
        "scope_boundary": "finite replay verifies formulas only; all-m force comes from the symbolic Vandermonde/Euclidean proof",
    }, indent=2))


if __name__ == "__main__":
    main()
