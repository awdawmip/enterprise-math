#!/usr/bin/env python3
"""Exact full three-distinct-layer pure-shift exhaustions for m=3..7.

All arithmetic is fractions.Fraction. For each requested m, this checks every
3-element support among the actual shifts c_s=m^2*s and every positive
multiplicity triple alpha with entries <=m and total degree 2m-1.

The finite exhaustions do not constitute an all-m HCM0 proof.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, factorial

EXPECTED = {
    3: (6, "bd54f9ea62075c4b013d01ed7e3497657d4ae137129e666ed8b42126633cdbdc"),
    4: (48, "d475a2621eb89d2db91c45301ce611847b1a9a6647cfa0db594d7f4177cb43c5"),
    5: (190, "638992a2e805c29ef85a188c96a4114f160bccf0e98599f6a776d979d8ed61c2"),
    6: (540, "6b026c5b13785f82872752bdcea676ff8f074b016e8e43133e1523272d3f76bd"),
    7: (1260, "3db78536c9254be76b0ae9791245ec4e8cace248d5b8d3396270ffeff651a854"),
}


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
        for j in range(c + 1, n):
            a[c][j] /= p
        for r in range(c + 1, n):
            q = a[r][c]
            if q:
                for j in range(c + 1, n):
                    a[r][j] -= q * a[c][j]
    return out


def pure_shift_reduced_laplacian(m, c):
    n = m - 1
    w = [F((-1) ** i * comb(n, i)) for i in range(m)]
    H = [[F(1, i + 1 + m * j + c) for j in range(m)] for i in range(m)]
    E = [sum(H[i][j] * w[j] for j in range(m)) for i in range(m)]
    Fc = [sum(H[i][j] * w[i] for i in range(m)) for j in range(m)]
    L = [[F(0) for _ in range(2 * m)] for __ in range(2 * m)]
    for i in range(m):
        L[i][i] = w[i] * E[i]
        for j in range(m):
            edge = w[i] * H[i][j] * w[j]
            L[i][m + j] = -edge
            L[m + j][i] = -edge
    for j in range(m):
        L[m + j][m + j] = w[j] * Fc[j]
    return [row[:-1] for row in L[:-1]]


def mixed_value(layers, ks):
    N = len(layers[0])
    M = [[sum(F(ks[s]) * layers[s][i][j] for s in range(3))
          for j in range(N)] for i in range(N)]
    return det(M)


def coefficient(grid, alpha):
    total = F(0)
    for ks in product(*[range(a + 1) for a in alpha]):
        sign = (-1) ** sum(a - k for a, k in zip(alpha, ks))
        weight = 1
        for a, k in zip(alpha, ks):
            weight *= comb(a, k)
        total += F(sign * weight) * grid[ks]
    den = 1
    for a in alpha:
        den *= factorial(a)
    return total / F(den)


def run_m(m):
    n = m - 1
    D = 2 * m - 1
    b = m * m
    target_sign = (-1) ** n
    layers_all = [pure_shift_reduced_laplacian(m, b * s) for s in range(m)]
    multiplicities = [
        alpha for alpha in product(range(1, m + 1), repeat=3)
        if sum(alpha) == D
    ]

    canonical = []
    bad = []
    supports = 0
    for support in combinations(range(m), 3):
        supports += 1
        layers = [layers_all[s] for s in support]
        grid = {}
        for ks in product(range(m + 1), repeat=3):
            grid[ks] = mixed_value(layers, ks) if any(ks) else F(0)
        for alpha in multiplicities:
            value = coefficient(grid, alpha)
            sign = 1 if value > 0 else -1 if value < 0 else 0
            canonical.append(
                f"{','.join(map(str, support))}|{','.join(map(str, alpha))}|"
                f"{value.numerator}/{value.denominator}"
            )
            if sign != target_sign:
                bad.append((support, alpha, value))

    digest = hashlib.sha256("\n".join(canonical).encode()).hexdigest()
    expected_count, expected_digest = EXPECTED[m]
    assert len(canonical) == expected_count
    assert digest == expected_digest
    assert not bad
    return {
        "m": m,
        "n": n,
        "target_pure_shift_sign": target_sign,
        "three_layer_support_count": supports,
        "multiplicity_patterns_per_support": len(multiplicities),
        "cells_checked": len(canonical),
        "wrong_sign_or_zero_cells": 0,
        "canonical_table_sha256": "sha256:" + digest,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m", type=int, choices=range(3, 8), help="run one m (3..7)")
    ap.add_argument("--all", action="store_true", help="run all m=3..7")
    args = ap.parse_args()
    if args.all:
        values = list(range(3, 8))
    else:
        values = [args.m if args.m is not None else 5]

    rows = [run_m(m) for m in values]
    payload = {
        "schema": "PERFECT_PRIME_HCM0_ACTUAL_TRIPLE_SUPPORT_M3_M7_EXACT_V1",
        "arithmetic": "exact fractions.Fraction",
        "rows": rows,
        "total_cells_checked": sum(row["cells_checked"] for row in rows),
        "all_cells_strict_target_sign": all(row["wrong_sign_or_zero_cells"] == 0 for row in rows),
        "scope_boundary": (
            "Each listed m is a complete finite exact three-distinct-layer pure-shift exhaustion. "
            "The union is not an all-m theorem, not HCM0, and not parent determinant nonvanishing."
        ),
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
