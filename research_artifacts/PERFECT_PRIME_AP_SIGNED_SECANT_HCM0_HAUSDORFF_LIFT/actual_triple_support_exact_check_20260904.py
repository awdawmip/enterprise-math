#!/usr/bin/env python3
"""Exact exhaustive m=5 check of actual three-layer pure-shift mixed cells.

This checker uses only fractions.Fraction.  It tests every 3-element support
among the five actual Perfect-Prime shifts c_s=m^2 s and every positive
multiplicity alpha=(a,b,c) with a,b,c<=m and a+b+c=2m-1.

Finite exhaustions are discovery/certification only; they are NOT an all-m HCM0
proof and do not prove parent determinant nonvanishing.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, factorial


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


def pure_shift_reduced_laplacian(m: int, c: int):
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


def coefficient_from_grid(grid, alpha):
    """Exact coefficient of z^alpha in a polynomial of coordinate degrees <=alpha."""
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


def main():
    m = 5
    n = m - 1
    D = 2 * m - 1
    b = m * m
    expected_sign = (-1) ** n

    all_layers = [pure_shift_reduced_laplacian(m, b * s) for s in range(m)]
    multiplicities = [
        alpha for alpha in product(range(1, m + 1), repeat=3)
        if sum(alpha) == D
    ]
    assert len(multiplicities) == 19

    canonical = []
    bad = []
    sample = None
    support_rows = []

    for support in combinations(range(m), 3):
        layers = [all_layers[s] for s in support]
        grid = {}
        for ks in product(range(m + 1), repeat=3):
            grid[ks] = mixed_value(layers, ks) if any(ks) else F(0)

        support_count = 0
        for alpha in multiplicities:
            value = coefficient_from_grid(grid, alpha)
            sign = 1 if value > 0 else -1 if value < 0 else 0
            support_count += 1
            canonical.append(
                f"{','.join(map(str, support))}|{','.join(map(str, alpha))}|"
                f"{value.numerator}/{value.denominator}"
            )
            if sign != expected_sign:
                bad.append({
                    "support": list(support),
                    "multiplicity": list(alpha),
                    "value": f"{value.numerator}/{value.denominator}",
                })
            if support == (0, 1, 2) and alpha == (3, 3, 3):
                sample = value
        support_rows.append({
            "support_layers": list(support),
            "actual_shifts": [b * s for s in support],
            "cells_checked": support_count,
        })

    assert len(support_rows) == 10
    assert len(canonical) == 190
    assert not bad
    assert sample == F(
        606281913837168436546787482311248779296875,
        2130095297450584815801682840209259311560647444027632266554642894848,
    )

    digest = hashlib.sha256("\n".join(canonical).encode("utf-8")).hexdigest()
    assert digest == "638992a2e805c29ef85a188c96a4114f160bccf0e98599f6a776d979d8ed61c2"

    print(json.dumps({
        "schema": "PERFECT_PRIME_HCM0_ACTUAL_TRIPLE_SUPPORT_M5_EXACT_V1",
        "arithmetic": "exact fractions.Fraction",
        "m": m,
        "n": n,
        "tree_cofactor_degree": D,
        "actual_layer_shift_rule": "c_s=m^2*s",
        "three_layer_supports": len(support_rows),
        "positive_multiplicity_patterns_per_support": len(multiplicities),
        "total_triple_support_cells_checked": len(canonical),
        "expected_pure_shift_coefficient_sign": expected_sign,
        "wrong_sign_or_zero_cells": len(bad),
        "all_cells_strict_target_sign": True,
        "canonical_table_sha256": "sha256:" + digest,
        "balanced_sample": {
            "support_layers": [0, 1, 2],
            "actual_shifts": [0, 25, 50],
            "multiplicity": [3, 3, 3],
            "value": f"{sample.numerator}/{sample.denominator}",
            "sign": "positive",
        },
        "support_summary": support_rows,
        "scope_boundary": (
            "This is a finite exact m=5 exhaustion of all three-distinct-layer "
            "pure-shift cells. It is not an all-m sign theorem, not HCM0, and "
            "not parent determinant nonvanishing."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
