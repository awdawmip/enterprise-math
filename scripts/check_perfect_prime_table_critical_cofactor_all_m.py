#!/usr/bin/env python3
"""Exact checker for RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF.

Standard-library only. It reconstructs:
  * the critical mixed-difference matrix M_m;
  * the shifted-Newton transfer minor T_m[J,I];
  * the reciprocal-kernel signed bipartite Laplacian cofactor.

Default range is m=2..6. All arithmetic is exact.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction


def bareiss_det(a):
    a = [list(map(int, row)) for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if a[r][k] != 0), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                if k:
                    assert num % prev == 0
                    num //= prev
                a[i][j] = num
        for i in range(k + 1, n):
            a[i][k] = 0
        prev = pivot
    return sign * a[n - 1][n - 1]


def fraction_det(a):
    a = [[Fraction(x) for x in row] for row in a]
    n = len(a)
    det = Fraction(1)
    sign = 1
    for k in range(n):
        pivot = next((r for r in range(k, n) if a[r][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        p = a[k][k]
        det *= p
        for j in range(k, n):
            a[k][j] /= p
        for i in range(k + 1, n):
            f = a[i][k]
            if not f:
                continue
            for j in range(k, n):
                a[i][j] -= f * a[k][j]
    return det * sign


def A(m, i, j):
    out = 1
    for k in range(m):
        out *= 1 + i + m * j + k * m * m
    return out


def critical_matrix(m):
    rows = [(i, j) for i in range(2, m + 1) for j in range(2, m + 1)]
    cols = [(a, b) for a in range(m - 1) for b in range(m - 1)]
    out = []
    for i, j in rows:
        row = []
        for a, b in cols:
            row.append(
                A(m, i, j) * (i ** a) * (j ** b)
                - A(m, i, 1) * (i ** a)
                - A(m, 1, j) * (j ** b)
                + A(m, 1, 1)
            )
        out.append(row)
    return out


def matmul(a, b):
    nr, nk, nc = len(a), len(b), len(b[0])
    assert nk == len(b)
    return [[sum(a[i][k] * b[k][j] for k in range(nk))
             for j in range(nc)] for i in range(nr)]


def transfer_target(m):
    states = [(r, s) for r in range(m) for s in range(m)]
    idx = {st: n for n, st in enumerate(states)}
    N = m * m
    Z = [[0] * N for _ in range(N)]
    for r, s in states:
        c = idx[(r, s)]
        Z[c][c] = r + 1 + m * (s + 1)
        if r + 1 < m:
            Z[idx[(r + 1, s)]][c] = 1
        if s + 1 < m:
            Z[idx[(r, s + 1)]][c] = m

    T = [[int(i == j) for j in range(N)] for i in range(N)]
    for k in range(m):
        beta = 1 + k * m * m
        L = [row[:] for row in Z]
        for d in range(N):
            L[d][d] += beta
        T = matmul(L, T)

    rows = [idx[(p, q)] for p in range(1, m) for q in range(1, m)]
    cols = [idx[(r, s)] for r in range(m - 1) for s in range(m - 1)]
    return [[T[r][c] for c in cols] for r in rows]


def barycentric_weights(m):
    return [
        Fraction((-1) ** (m - i), math.factorial(i - 1) * math.factorial(m - i))
        for i in range(1, m + 1)
    ]


def laplacian_cofactor(m):
    w = barycentric_weights(m)
    K = [[Fraction(1, A(m, i, j)) for j in range(1, m + 1)]
         for i in range(1, m + 1)]
    Q = [[w[i] * K[i][j] * w[j] for j in range(m)] for i in range(m)]
    row_sum = [sum(Q[i][j] for j in range(m)) for i in range(m)]
    col_sum = [sum(Q[i][j] for i in range(m)) for j in range(m)]
    L = [[Fraction(0) for _ in range(2 * m)] for _ in range(2 * m)]
    for i in range(m):
        L[i][i] = row_sum[i]
        for j in range(m):
            L[i][m + j] = -Q[i][j]
            L[m + j][i] = -Q[i][j]
    for j in range(m):
        L[m + j][m + j] = col_sum[j]
    cofactor = [row[:-1] for row in L[:-1]]
    return fraction_det(cofactor)


def scale_factor(m):
    vdet = math.prod(math.factorial(p) for p in range(1, m))
    return vdet ** (2 * (m - 1))


def check_one(m):
    Mdet = bareiss_det(critical_matrix(m))
    Tdet = bareiss_det(transfer_target(m))
    scale = scale_factor(m)
    assert Mdet == scale * Tdet
    cof = laplacian_cofactor(m)
    assert cof != 0
    return {
        "m": m,
        "critical_size": (m - 1) ** 2,
        "M_det": str(Mdet),
        "M_det_sign": 1 if Mdet > 0 else -1 if Mdet < 0 else 0,
        "transfer_target_det": str(Tdet),
        "transfer_target_det_sign": 1 if Tdet > 0 else -1 if Tdet < 0 else 0,
        "monomial_to_newton_output_scale": str(scale),
        "scale_identity_verified": Mdet == scale * Tdet,
        "signed_laplacian_cofactor_num": str(cof.numerator),
        "signed_laplacian_cofactor_den": str(cof.denominator),
        "signed_laplacian_cofactor_sign": 1 if cof > 0 else -1 if cof < 0 else 0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-m", type=int, default=6)
    args = ap.parse_args()
    results = [check_one(m) for m in range(2, args.max_m + 1)]
    print(json.dumps({
        "schema": "PERFECT_PRIME_TABLE_CRITICAL_COFACTOR_EXACT_CERT_V1",
        "arithmetic": "exact integer/Fraction",
        "range": [2, args.max_m],
        "results": results,
    }, indent=2))


if __name__ == "__main__":
    main()
