#!/usr/bin/env python3
"""Exact certificate for the three-shift auxiliary-conjecture obstruction.

This does NOT test or refute HCM0.  It tests the stronger auxiliary conjecture
that every mixed coefficient of arbitrary nonnegative pure Cauchy shifts L(c)
has the two-shift sign (-1)^(m-1).

All arithmetic is fractions.Fraction.  The m=7 coefficient for shifts (0,2,5)
and multiplicities (1,5,7) is computed two independent ways:

  1. multivariate finite-difference coefficient extraction;
  2. coefficient-of-z derivative at z=0 followed by exact univariate Lagrange
     interpolation in t.

The same multiplicity cell is also checked at the actual Perfect-Prime spacing
(0,m^2,2m^2), where its sign is positive.  A small exact AP-spacing scan is
included only as finite structural evidence.
"""
from __future__ import annotations

import json
from fractions import Fraction as F
from itertools import product
from math import comb, factorial

EXPECTED = F(
    -9124563710159060296133331257733323921803,
    214894420165177617520129597749664857553591871024974545851844728742741899728650240000,
)
EXPECTED_ACTUAL = F(
    2020508893605078901068867942380512448517816669066168908718740610593813,
    1705478180555715554493070132258456452246159299927111039765299907113833208874517899074841695344312605748184696287356534903432480176558433107968000000,
)


def det(a):
    a = [[F(x) for x in row] for row in a]
    n = len(a)
    out = F(1)
    for c in range(n):
        pivot = next((r for r in range(c, n) if a[r][c]), None)
        if pivot is None:
            return F(0)
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            out = -out
        p = a[c][c]
        out *= p
        for j in range(c, n):
            a[c][j] /= p
        for r in range(c + 1, n):
            q = a[r][c]
            if q:
                for j in range(c, n):
                    a[r][j] -= q * a[c][j]
    return out


def pure_shift_reduced_laplacian(m: int, c: F):
    n = m - 1
    w = [F((-1) ** i * comb(n, i)) for i in range(m)]
    H = [[F(1, i + 1 + m * j + c) for j in range(m)] for i in range(m)]
    E = [sum(H[i][j] * w[j] for j in range(m)) for i in range(m)]
    Fc = [sum(H[i][j] * w[i] for i in range(m)) for j in range(m)]
    L = [[F(0) for _ in range(2 * m)] for __ in range(2 * m)]
    for i in range(m):
        L[i][i] = w[i] * E[i]
        for j in range(m):
            cc = w[i] * H[i][j] * w[j]
            L[i][m + j] = -cc
            L[m + j][i] = -cc
    for j in range(m):
        L[m + j][m + j] = w[j] * Fc[j]
    return [row[:-1] for row in L[:-1]]


def mixed_value(layers, ks):
    N = len(layers[0])
    M = [[sum(F(ks[s]) * layers[s][i][j] for s in range(len(layers)))
          for j in range(N)] for i in range(N)]
    return det(M)


def mixed_coefficient(m: int, shifts, alpha):
    """Coefficient of prod z_s^alpha_s in det'(sum z_s L(c_s))."""
    assert sum(alpha) == 2 * m - 1
    layers = [pure_shift_reduced_laplacian(m, F(c)) for c in shifts]
    total = F(0)
    for ks in product(*[range(a + 1) for a in alpha]):
        val = mixed_value(layers, ks) if any(ks) else F(0)
        sign = (-1) ** sum(a - k for a, k in zip(alpha, ks))
        weight = 1
        for a, k in zip(alpha, ks):
            weight *= comb(a, k)
        total += F(sign * weight) * val
    den = 1
    for a in alpha:
        den *= factorial(a)
    return total / F(den)


def det_and_inverse(A):
    A = [[F(x) for x in row] for row in A]
    n = len(A)
    M = [A[i] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    determinant = F(1)
    for c in range(n):
        pivot = next((r for r in range(c, n) if M[r][c]), None)
        if pivot is None:
            return F(0), None
        if pivot != c:
            M[c], M[pivot] = M[pivot], M[c]
            determinant = -determinant
        p = M[c][c]
        determinant *= p
        for j in range(2 * n):
            M[c][j] /= p
        for r in range(n):
            if r == c:
                continue
            q = M[r][c]
            if q:
                for j in range(2 * n):
                    M[r][j] -= q * M[c][j]
    return determinant, [row[n:] for row in M]


def determinant_derivative(A, B):
    determinant, inv = det_and_inverse(A)
    assert inv is not None
    n = len(A)
    trace = sum(inv[i][j] * B[j][i] for i in range(n) for j in range(n))
    return determinant * trace


def poly_mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def lagrange_interpolate(xs, ys):
    out = [F(0)] * len(xs)
    for i, (xi, yi) in enumerate(zip(xs, ys)):
        basis = [F(1)]
        den = F(1)
        for j, xj in enumerate(xs):
            if i == j:
                continue
            basis = poly_mul(basis, [F(-xj), F(1)])
            den *= xi - xj
        scale = yi / den
        for k, c in enumerate(basis):
            out[k] += scale * c
    return out


def independent_obstruction_coefficient():
    """[z^1 t^5] det'(z L(0)+t L(2)+L(5)); remaining L(5)-degree is 7."""
    m = 7
    L0 = pure_shift_reduced_laplacian(m, F(0))
    L2 = pure_shift_reduced_laplacian(m, F(2))
    L5 = pure_shift_reduced_laplacian(m, F(5))
    xs = [F(k) for k in range(1, 14)]
    ys = []
    for t in xs:
        A = [[t * L2[i][j] + L5[i][j] for j in range(13)] for i in range(13)]
        ys.append(determinant_derivative(A, L0))
    poly = lagrange_interpolate(xs, ys)
    return poly[5]


def main():
    m = 7
    alpha = (1, 5, 7)
    arbitrary = mixed_coefficient(m, (0, 2, 5), alpha)
    independent = independent_obstruction_coefficient()
    actual = mixed_coefficient(m, (0, 49, 98), alpha)
    assert arbitrary == EXPECTED
    assert independent == EXPECTED
    assert arbitrary < 0  # n=6, so auxiliary conjecture expected positive.
    assert actual == EXPECTED_ACTUAL > 0

    scan = {}
    for B in (1, 2, 5, 10, 20, 30, 40, 49):
        v = mixed_coefficient(m, (0, B, 2 * B), alpha)
        scan[str(B)] = "positive" if v > 0 else "negative" if v < 0 else "zero"
    assert scan == {
        "1": "negative", "2": "negative", "5": "negative", "10": "negative",
        "20": "positive", "30": "positive", "40": "positive", "49": "positive",
    }

    print(json.dumps({
        "schema": "PERFECT_PRIME_HCM0_THREE_SHIFT_AUXILIARY_OBSTRUCTION_V1",
        "arithmetic": "exact fractions.Fraction",
        "m": m,
        "n": m - 1,
        "multiplicity": list(alpha),
        "arbitrary_shifts": [0, 2, 5],
        "arbitrary_coefficient": f"{arbitrary.numerator}/{arbitrary.denominator}",
        "independent_jacobi_lagrange_match": independent == arbitrary,
        "auxiliary_expected_sign": "positive because (-1)^n=+1",
        "auxiliary_conjecture_refuted": True,
        "actual_spacing_shifts": [0, 49, 98],
        "actual_spacing_same_cell_sign": "positive",
        "actual_spacing_same_cell": f"{actual.numerator}/{actual.denominator}",
        "ap_spacing_scan_B_for_shifts_0_B_2B": scan,
        "scope_boundary": (
            "This refutes only the arbitrary-nonnegative-shift all-support sign extension. "
            "It does not refute HCM0, actual m^2-spaced layer signs, or parent determinant nonvanishing."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
