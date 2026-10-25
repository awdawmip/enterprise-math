#!/usr/bin/env python3
"""EC19: exact, reproducible finite certificate for an infinite-n BRC theorem.
Uses only CPython integer arithmetic; no external libraries or network.
Scope: the auxiliary palindromic E(x,u), not native X6 dynamics.
"""
import hashlib
import json
import math
from pathlib import Path

JMAX = 512
MAX_N = 3 * JMAX + 6


def build_rows(max_n):
    """Extract E_n(u) from Delta(x,u) E(x,u) = 1-u*x**2."""
    rows = []
    for n in range(max_n + 1):
        cur = [0] * (n + 1)
        if n == 0:
            cur[0] = 1
        else:
            for j, a in enumerate(rows[n - 1]):
                cur[j] += a
                cur[j + 1] += a
            if n >= 4:
                for j, a in enumerate(rows[n - 4]):
                    cur[j + 2] -= 2 * a
            if n >= 6:
                for j, a in enumerate(rows[n - 6]):
                    cur[j + 3] += a
            if n == 2:
                cur[1] -= 1
        rows.append(cur)
    return rows


def shift_add(dst, src, shift, coefficient):
    for i, val in enumerate(src):
        dst[i + shift] += coefficient * val


def build_rational_numerators(max_j):
    """E_j(x)=A_j(x)/(1-x)**(j+1), degrees <=3j."""
    a = [[1], [0, 1, -1, 1]]
    for j in range(2, max_j + 1):
        dst = [0] * (3 * j + 1)
        shift_add(dst, a[j - 1], 1, 1)
        shift_add(dst, a[j - 2], 4, -2)
        shift_add(dst, a[j - 2], 5, 2)
        if j >= 3:
            shift_add(dst, a[j - 3], 6, 1)
            shift_add(dst, a[j - 3], 7, -2)
            shift_add(dst, a[j - 3], 8, 1)
        while dst and dst[-1] == 0:
            dst.pop()
        assert dst and len(dst) - 1 <= 3 * j
        a.append(dst)
    return a[: max_j + 1]


def rational_coefficient(num, j, n):
    # For n>=2j, n-d+j>=0 for every d<=3j, so this is a polynomial in n.
    assert n >= 2 * j
    return sum(c * math.comb(n - d + j, j)
               for d, c in enumerate(num) if c and n - d + j >= j)


def forward_difference_head(values):
    arr = list(values)
    while arr:
        yield arr[0]
        arr = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]


def main():
    rows = build_rows(MAX_N)
    a = build_rational_numerators(JMAX)
    assert rows[10][2] == rows[10][3] == 23
    assert rows[10][4] == 25
    assert rows[12][3] == rows[12][4] == 52

    # Independent fixed-grade rational expansion versus depth recurrence.
    # Every j is tested at three positions, including the far end of the
    # window used by the Newton certificate.
    independent_checks = 0
    for j in range(JMAX + 1):
        for n in sorted({2*j, 2*j+6, 3*j+6}):
            assert rational_coefficient(a[j], j, n) == rows[n][j], (j, n)
            independent_checks += 1

    positive_newton_count = 0
    minimum_newton = None
    newton_sha = hashlib.sha256()
    for j in range(1, JMAX + 1):
        base = 2*j + 6
        values = [rows[base+t][j] - rows[base+t][j-1]
                  for t in range(j+1)]
        differences = list(forward_difference_head(values))
        assert len(differences) == j+1
        for r, d in enumerate(differences):
            assert d > 0, ("NONPOSITIVE_NEWTON", j, r, d)
            newton_sha.update(f"{j}|{r}|{d}\n".encode("ascii"))
            positive_newton_count += 1
            minimum_newton = d if minimum_newton is None else min(minimum_newton,d)
        assert differences[-1] == 1, ("TOP_DIFFERENCE", j)
    assert positive_newton_count == 131840

    low_strip_count = 0
    exceptions = []
    strip_sha = hashlib.sha256()
    for j in range(1, JMAX + 1):
        for n in range(max(10, 2*j), 2*j+6):
            if 2*j > n:
                continue
            d = rows[n][j] - rows[n][j-1]
            assert d >= 0, ("LOW_STRIP_NEGATIVE", n, j, d)
            if d == 0:
                exceptions.append([n, j])
            strip_sha.update(f"{n}|{j}|{d}\n".encode("ascii"))
            low_strip_count += 1
    assert low_strip_count == 3054
    assert exceptions == [[10, 3], [12, 4]]

    report = {
        "schema": "EM_R4_EC19_EXACT_FINITE_WIDTH_CERTIFICATE_V1",
        "model": "auxiliary ordered positive binary affine BRC palindromic grade kernel",
        "generating_function": "(1-u*x^2)/(1-(1+u)*x+2*u^2*x^4-u^3*x^6)",
        "certified_theorem": "E[n,j]>=E[n,j-1] for all integers n>=10, 1<=j<=min(floor(n/2),512), with equality only at (n,j)=(10,3),(12,4)",
        "derived_corollary": "D[n,k]>=0 for all n>=max(13,2*k+1), 2<=k<=513, with equality only at (13,4),(15,5)",
        "j_max": JMAX,
        "recurrence_n_max": MAX_N,
        "recurrence_integer_cells": (MAX_N+1)*(MAX_N+2)//2,
        "independent_rational_evaluations": independent_checks,
        "positive_integer_newton_coefficients": positive_newton_count,
        "minimum_newton_coefficient": minimum_newton,
        "newton_coefficient_sha256": newton_sha.hexdigest(),
        "low_strip_integer_checks": low_strip_count,
        "low_strip_sha256": strip_sha.hexdigest(),
        "exact_equalities": exceptions,
        "arithmetic": "Python arbitrary precision exact integers and math.comb",
        "proof_logic": "degree <=j from A_j/(1-x)^(j+1); for n>=2j the fixed-grade coefficient is polynomial; strictly positive Newton coefficients at base 2j+6 extend to every n beyond; six finite n-cases per j close the strip",
        "coverage": "infinite n but finite grades j<=512; does not settle j>512 or formal native X6 dynamics",
        "mathematical_admission": "AUTHOR_SIDE_UNREVIEWED",
        "native_X6_experiment": "NOT_RUN"
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
