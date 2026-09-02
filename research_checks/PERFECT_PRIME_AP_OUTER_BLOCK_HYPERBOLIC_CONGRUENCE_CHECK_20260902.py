#!/usr/bin/env python3
"""Exact checker for the Perfect Prime AP outer block-hyperbolic task.

This checker certifies two narrow facts:
1. a fixed t-independent simultaneous 1+2 congruence decomposition already
   fails for m=4 at t=1/3,2/3,1;
2. the accepted m=15,t=4/5 adjacent scalar-pivot exchange is reproduced.

The symbolic theorem that arbitrary adaptive 1x1/2x2 principal block LDL
existence is equivalent to nonsingularity for a real symmetric matrix is
proved in the research return; finite computation is not used for that theorem.
"""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as F
from functools import reduce
from math import comb, factorial, gcd

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def det(a):
    a = [[F(x) for x in row] for row in a]
    n = len(a)
    if n == 0:
        return F(1)
    out = F(1)
    for c in range(n):
        pivot = next((r for r in range(c, n) if a[r][c]), None)
        if pivot is None:
            return F(0)
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            out = -out
        q = a[c][c]
        out *= q
        for j in range(c, n):
            a[c][j] /= q
        for r in range(c + 1, n):
            q = a[r][c]
            if q:
                for j in range(c, n):
                    a[r][j] -= q * a[c][j]
    return out


def c_js(m, j, s):
    n = m - 1
    z = m * j + m * m * s
    den = 1
    for r in range(1, m + 1):
        den *= z + r
    return F(factorial(n), den)


def inner_covariance(m, j, t):
    n = m - 1
    b = m * m
    y = m * j
    lam = [
        F((-1) ** s * comb(n, s)) * t**s * c_js(m, j, s)
        for s in range(n + 1)
    ]
    D = sum(lam)
    assert D > 0
    moments = [
        sum(lam[s] * F((y + b * s) ** r) for s in range(n + 1))
        for r in range(2 * n + 1)
    ]
    return [
        [
            moments[r + q] - moments[r] * moments[q] / D
            for q in range(1, n + 1)
        ]
        for r in range(1, n + 1)
    ]


def outer_covariance(m, t):
    n = m - 1
    S = [[F(0) for _ in range(n)] for __ in range(n)]
    for j in range(n + 1):
        C = inner_covariance(m, j, t)
        w = F((-1) ** j * comb(n, j))
        for r in range(n):
            for q in range(n):
                S[r][q] += w * C[r][q]
    return S


def inverse(a):
    n = len(a)
    M = [
        [F(a[i][j]) for j in range(n)]
        + [F(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for c in range(n):
        pivot = next((r for r in range(c, n) if M[r][c]), None)
        assert pivot is not None
        M[c], M[pivot] = M[pivot], M[c]
        q = M[c][c]
        M[c] = [x / q for x in M[c]]
        for r in range(n):
            if r != c and M[r][c]:
                q = M[r][c]
                M[r] = [M[r][j] - q * M[c][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def matmul(A, B):
    return [
        [
            sum(A[i][k] * B[k][j] for k in range(len(B)))
            for j in range(len(B[0]))
        ]
        for i in range(len(A))
    ]


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def matsub(A, B):
    return [
        [A[i][j] - B[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]


def rank(A):
    M = [[F(x) for x in row] for row in A]
    m = len(M)
    n = len(M[0]) if m else 0
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if M[i][c]), None)
        if pivot is None:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        q = M[r][c]
        M[r] = [x / q for x in M[r]]
        for i in range(m):
            if i != r and M[i][c]:
                q = M[i][c]
                M[i] = [M[i][j] - q * M[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def cross3(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]


def primitive_integer_vector(v):
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)

    L = 1
    for x in v:
        L = lcm(L, x.denominator)
    ints = [x.numerator * (L // x.denominator) for x in v]
    g = reduce(gcd, (abs(x) for x in ints if x), 0)
    ints = [x // g for x in ints]
    first = next(x for x in ints if x)
    if first < 0:
        ints = [-x for x in ints]
    return ints


def wedge3(a, b):
    return [
        a[0] * b[1] - a[1] * b[0],
        a[0] * b[2] - a[2] * b[0],
        a[1] * b[2] - a[2] * b[1],
    ]


def sign(q):
    return 1 if q > 0 else -1 if q < 0 else 0


def frac_sha256(q):
    text = f"{q.numerator}/{q.denominator}".encode("ascii")
    return "sha256:" + hashlib.sha256(text).hexdigest()


def vector_sha256(v):
    return "sha256:" + hashlib.sha256(",".join(map(str, v)).encode("ascii")).hexdigest()


def leading_minors(m, t):
    S = outer_covariance(m, t)
    return [det([row[:k] for row in S[:k]]) for k in range(1, m)]


def main():
    # Static simultaneous-block obstruction in the smallest useful odd quotient
    # dimension n=3 (m=4).
    t0, t1, t2 = F(1, 3), F(2, 3), F(1)
    A, B, C = [outer_covariance(4, t) for t in (t0, t1, t2)]
    dets = [det(M) for M in (A, B, C)]
    assert all(d != 0 for d in dets)

    Ainv = inverse(A)
    TB = matmul(Ainv, B)
    TC = matmul(Ainv, C)
    K = matsub(matmul(TB, TC), matmul(TC, TB))
    assert det(K) == 0
    assert rank(K) == 2

    # Since rank K=2, ker K is one-dimensional. This cross-product generator
    # spans it exactly.
    v = primitive_integer_vector(cross3(K[0], K[1]))
    vF = [F(x) for x in v]
    assert all(x == 0 for x in matvec(K, vF))
    TBv = matvec(TB, vF)
    wedge = wedge3(TBv, vF)
    assert any(x != 0 for x in wedge)

    # Therefore T_B and T_C have no common eigenline: any common eigenvector
    # must lie in ker[T_B,T_C], but the unique kernel line is not T_B-invariant.
    # A fixed 1+2 simultaneous congruence decomposition of A,B,C would force
    # such a common invariant line, hence is impossible.

    # Accepted m=15 paired-pivot regression.
    ds = leading_minors(15, F(4, 5))
    leading_signs = [sign(d) for d in ds]
    expected = [-1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1]
    assert leading_signs == [-1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1]
    assert [k + 1 for k, (a, b) in enumerate(zip(leading_signs, expected)) if a != b] == [12]
    pivots = [sign(ds[0])] + [sign(ds[k] / ds[k - 1]) for k in range(1, len(ds))]
    assert pivots == [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1]
    assert pivots.count(1) == 7 and pivots.count(-1) == 7

    d12_34 = leading_minors(15, F(3, 4))[11]
    d12_45 = ds[11]
    d12_1 = leading_minors(15, F(1))[11]
    assert d12_34 > 0 and d12_45 < 0 and d12_1 > 0

    payload = {
        "schema": "PERFECT_PRIME_AP_OUTER_BLOCK_HYPERBOLIC_CONGRUENCE_OBSTRUCTION_CERT_V1",
        "task_id": "RS-PERFECT-PRIME-AP-OUTER-BLOCK-HYPERBOLIC-CONGRUENCE",
        "publication_id": "TP2-E2EE65A96658AD50D37C",
        "claim_id": "CLM-43687A005470DE71A6DF",
        "researcher_id": "EM-PPTAPOBHC1-C58329",
        "arithmetic": "exact Python fractions.Fraction",
        "static_simultaneous_block_obstruction": {
            "m": 4,
            "quotient_dimension": 3,
            "t_values": ["1/3", "2/3", "1"],
            "base_matrix_determinant_signs": [sign(d) for d in dets],
            "base_matrix_determinant_sha256": [frac_sha256(d) for d in dets],
            "operators": ["T_B=S(1/3)^(-1)S(2/3)", "T_C=S(1/3)^(-1)S(1)"],
            "commutator_rank": rank(K),
            "commutator_determinant": "0",
            "commutator_kernel_dimension": 1,
            "primitive_kernel_vector_sha256": vector_sha256(v),
            "primitive_kernel_vector_bit_lengths": [abs(x).bit_length() for x in v],
            "T_B_v_wedge_v_signs": [sign(x) for x in wedge],
            "T_B_v_wedge_v_nonzero": [x != 0 for x in wedge],
            "conclusion": (
                "No single t-independent real congruence with one fixed block partition "
                "can simultaneously reduce S_4(t) to blocks of size at most 2 for all "
                "0<t<=1; already t=1/3,2/3,1 are incompatible."
            ),
        },
        "m15_regression": {
            "m": 15,
            "t": "4/5",
            "leading_minor_signs_k1_to_k14": leading_signs,
            "canonical_expected_flag_signs": expected,
            "mismatch_orders": [12],
            "ldl_pivot_signs_k1_to_k14": pivots,
            "inertia_from_nonzero_scalar_pivots": {"positive": 7, "negative": 7, "zero": 0},
            "delta_12_signs": {"3/4": sign(d12_34), "4/5": sign(d12_45), "1": sign(d12_1)},
            "delta_12_sha256": {
                "3/4": frac_sha256(d12_34),
                "4/5": frac_sha256(d12_45),
                "1": frac_sha256(d12_1),
            },
        },
        "classification": "EXACT_STATIC_BLOCK_CONGRUENCE_OBSTRUCTION",
        "scope": (
            "This certificate obstructs a fixed t-independent simultaneous block basis. "
            "It does not refute det S_m(t)!=0, does not refute all structured t-dependent "
            "block algorithms, and does not use finite checks as an all-m theorem."
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
