#!/usr/bin/env python3
"""Exact checker for RS-PERFECT-PRIME-AP-FIXED-POINT-COMPOUND-NO-RECROSSING.

Standard-library only. Finite computations are regression/discovery evidence only.
The all-m adjacent-Cauchy-layer theorem is proved algebraically in the research return.
"""
from __future__ import annotations

import json
from fractions import Fraction as F
from math import comb, factorial


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


def transpose(a):
    return [list(row) for row in zip(*a)]


def mv(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def laplacian_from_h(m, h):
    n = m - 1
    w = [F((-1) ** i * comb(n, i)) for i in range(m)]
    e = mv(h, w)
    d = mv(transpose(h), w)
    L = [[F(0) for _ in range(2 * m)] for _ in range(2 * m)]
    for i in range(m):
        L[i][i] = w[i] * e[i]
        for j in range(m):
            c = w[i] * h[i][j] * w[j]
            L[i][m + j] = -c
            L[m + j][i] = -c
    for j in range(m):
        L[m + j][m + j] = w[j] * d[j]
    return L


def cofactor_tau(m, h):
    L = laplacian_from_h(m, h)
    return det([row[:-1] for row in L[:-1]])


def layer_h(m, s, b=None):
    if b is None:
        b = m * m
    return [[F(1, i + 1 + m * j + b * s) for j in range(m)] for i in range(m)]


def adjacent_tau(m, s, t, b=None):
    if b is None:
        b = m * m
    h0 = layer_h(m, s, b)
    h1 = layer_h(m, s + 1, b)
    h = [[h0[i][j] - t * h1[i][j] for j in range(m)] for i in range(m)]
    return cofactor_tau(m, h)


def actual_h(m, t):
    n = m - 1
    b = m * m
    out = []
    for i in range(m):
        row = []
        for j in range(m):
            base = i + 1 + m * j
            row.append(sum(
                F((-1) ** s * comb(n, s)) * (t ** s) / F(base + b * s)
                for s in range(n + 1)
            ))
        out.append(row)
    return out


def actual_tau(m, t):
    return cofactor_tau(m, actual_h(m, t))


def trim(p):
    p = [F(x) for x in p]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def interpolate_integer_grid(values):
    """Power coefficients of the unique polynomial through f(0),...,f(D)."""
    diffs = [F(x) for x in values]
    deltas = []
    while diffs:
        deltas.append(diffs[0])
        diffs = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]
    out = [F(0)]
    fall = [F(1)]
    for k, delta in enumerate(deltas):
        if k:
            nxt = [F(0)] * (len(fall) + 1)
            for i, c in enumerate(fall):
                nxt[i] -= F(k - 1) * c
                nxt[i + 1] += c
            fall = nxt
        if len(out) < len(fall):
            out += [F(0)] * (len(fall) - len(out))
        den = F(factorial(k))
        for i, c in enumerate(fall):
            out[i] += delta * c / den
    return trim(out)


def peval(p, x):
    z = F(0)
    for c in reversed(p):
        z = z * x + c
    return z


def mobius_positive_coefficients(q, d):
    """Coefficients of (1+x)^d q(x/(1+x))."""
    out = [F(0)] * (d + 1)
    for k, c in enumerate(q):
        for j in range(d - k + 1):
            out[k + j] += c * comb(d - k, j)
    return out


def frac(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def check_adjacent_layers():
    rows = []
    for m in range(2, 9):
        b = m * m
        for s in range(3):
            base = F(m * m + 1, 2) + b * s
            root = (base + b) / base
            at_root = adjacent_tau(m, s, root, b)
            at_one = adjacent_tau(m, s, F(1), b)
            assert root > 1
            assert at_root == 0
            assert at_one != 0
            rows.append({
                "m": m,
                "s": s,
                "b": b,
                "predicted_unique_nongauge_candidate_root": frac(root),
                "root_gt_1": True,
                "cofactor_at_predicted_root_zero": True,
                "cofactor_at_t_1_nonzero": True,
            })
    return rows


def check_actual_bernstein():
    rows = []
    for m in range(2, 6):
        n = m - 1
        # A (2m-1)x(2m-1) cofactor of a degree-n matrix polynomial has
        # degree at most n(2m-1); interpolate at the full safe bound.
        max_degree = n * (2 * m - 1)
        p = interpolate_integer_grid([actual_tau(m, F(k)) for k in range(max_degree + 1)])
        assert peval(p, F(1, 2)) == actual_tau(m, F(1, 2))
        assert all(p[k] == 0 for k in range(n))
        q = trim(p[n:])
        observed_d = len(q) - 1
        expected_d = n * (2 * m - 3)
        assert observed_d == expected_d
        bhat = mobius_positive_coefficients(q, observed_d)
        assert all(c > 0 for c in bhat)
        tau1 = actual_tau(m, F(1))
        assert tau1 > 0
        rows.append({
            "m": m,
            "forced_t_order": n,
            "tau_total_degree": len(p) - 1,
            "q_degree_after_forced_factor": observed_d,
            "mobius_coefficient_count": len(bhat),
            "all_mobius_coefficients_strictly_positive": True,
            "minimum_mobius_coefficient": frac(min(bhat)),
            "tau_at_1": frac(tau1),
        })
    return rows


def main():
    adjacent = check_adjacent_layers()
    actual = check_actual_bernstein()
    payload = {
        "schema": "PERFECT_PRIME_AP_FIXED_POINT_COMPOUND_NO_RECROSSING_CERT_V1",
        "arithmetic": "exact Python Fraction",
        "all_m_proof_location": "research return; adjacent-layer theorem is symbolic, not inferred from this finite regression",
        "adjacent_layer_regression": {
            "m_range": [2, 8],
            "s_range": [0, 2],
            "rows": adjacent,
        },
        "actual_ap_finite_discovery": {
            "m_range": [2, 5],
            "interpretation": "finite discovery/regression only; not an all-m proof",
            "rows": actual,
        },
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
