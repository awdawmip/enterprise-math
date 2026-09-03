#!/usr/bin/env python3
"""Exact checker for the Perfect Prime AP residual Mobius-Bernstein coefficient task.

All arithmetic is fractions.Fraction.  The symbolic all-m statements belong in
the paired research return.  This checker verifies:
  * the signed squared-secant Cauchy-Binet coefficient formula for m <= 4;
  * the row-minor/secant factorization on all basis candidates for m <= 3;
  * strict alternating signs of q_m and strict finite Hausdorff complete
    monotonicity of h_{m,a}=(-1)^a q_{m,a}/binom(d,a) through m <= 8
    by default, with single exact extension cases selected by --m.

Finite checks are regression/discovery only and are not an all-m proof.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from itertools import combinations
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


def actual_h(m, t):
    n = m - 1
    b = m * m
    return [[sum(
        F((-1) ** s * comb(n, s)) * t ** s
        / F(i + 1 + m * j + b * s)
        for s in range(n + 1)
    ) for j in range(m)] for i in range(m)]


def actual_tau(m, t):
    L = laplacian_from_h(m, actual_h(m, t))
    return det([row[:-1] for row in L[:-1]])


def trim(p):
    p = [F(x) for x in p]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def interpolate_integer_grid(values):
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


def q_coefficients(m):
    n = m - 1
    max_degree = n * (2 * m - 1)
    p = interpolate_integer_grid(
        [actual_tau(m, F(k)) for k in range(max_degree + 1)]
    )
    assert len(p) - 1 == 2 * n * n
    assert all(p[k] == 0 for k in range(n))
    q = trim(p[n:])
    d = n * (2 * m - 3)
    assert len(q) - 1 == d
    return q


def c_js(m, j, s):
    n = m - 1
    z = m * j + m * m * s
    den = 1
    for r in range(1, m + 1):
        den *= z + r
    return F(factorial(n), den)


def secant_delta(m, groups):
    n = m - 1
    b = m * m
    rows = []
    for j, S in enumerate(groups):
        if not S:
            raise ValueError("secant_delta requires every j-group active")
        r0 = min(S)
        y = m * j
        z0 = y + b * r0
        for s in sorted(S):
            if s == r0:
                continue
            z = y + b * s
            rows.append([F(z ** p - z0 ** p) for p in range(1, n + 1)])
    assert len(rows) == n
    return rows


def cb_q_coefficients(m):
    """The exact signed squared-secant formula, enumerated for small m."""
    n = m - 1
    D = 2 * m - 1
    d = n * (2 * m - 3)
    atoms = [(j, s) for j in range(m) for s in range(m)]
    out = [F(0)] * (d + 1)
    vx = 1
    for k in range(1, n + 1):
        vx *= factorial(k)

    for I in combinations(atoms, D):
        groups = [[] for _ in range(m)]
        for j, s in I:
            groups[j].append(s)
        if any(not S for S in groups):
            continue
        Delta = secant_delta(m, groups)
        dd = det(Delta)
        if dd == 0:
            continue
        A = sum(s for _, s in I)
        a = A - n
        assert 0 <= a <= d
        eps = -1 if (sum(j + s for j, s in I) % 2) else 1
        gamma = F(dd * dd)
        for j, s in I:
            gamma *= F(comb(n, j) * comb(n, s)) * c_js(m, j, s)
        out[a] += F(eps) * gamma / F(vx * vx)
    return out


def full_atom_row(m, j, s):
    n = m - 1
    y = m * j
    z = y + m * m * s
    return [F(z ** r) for r in range(n + 1)] + [
        F(-y ** r) for r in range(1, n + 1)
    ]


def vy_abs(m):
    n = m - 1
    out = m ** (n * (n + 1) // 2)
    for k in range(1, n + 1):
        out *= factorial(k)
    return out


def check_row_minor_factorization(m_max=3):
    checked = 0
    zero_when_group_missing = 0
    factored = 0
    for m in range(2, m_max + 1):
        D = 2 * m - 1
        atoms = [(j, s) for j in range(m) for s in range(m)]
        vy2 = F(vy_abs(m) ** 2)
        for I in combinations(atoms, D):
            R = [full_atom_row(m, j, s) for j, s in I]
            rd = det(R)
            groups = [[] for _ in range(m)]
            for j, s in I:
                groups[j].append(s)
            checked += 1
            if any(not S for S in groups):
                assert rd == 0
                zero_when_group_missing += 1
                continue
            Delta = secant_delta(m, groups)
            dd = det(Delta)
            assert rd * rd == vy2 * dd * dd
            factored += 1
    return {
        "m_range": [2, m_max],
        "candidate_minors_checked": checked,
        "missing_group_zero_minors": zero_when_group_missing,
        "all_group_active_factorizations_checked": factored,
    }


def finite_hcm(q):
    d = len(q) - 1
    h = [F((-1) ** a) * q[a] / F(comb(d, a)) for a in range(d + 1)]
    q_alternating = all(F((-1) ** a) * q[a] > 0 for a in range(d + 1))
    current = h
    k = 0
    all_strict = True
    cells = 0
    canonical = []
    initial = []
    while current:
        signed = [F((-1) ** k) * value for value in current]
        for r, value in enumerate(signed):
            cells += 1
            if value <= 0:
                all_strict = False
            canonical.append(f"{k}:{r}:{value.numerator}/{value.denominator}")
        initial.append(signed[0])
        current = [current[i + 1] - current[i] for i in range(len(current) - 1)]
        k += 1
    digest = hashlib.sha256("\n".join(canonical).encode("utf-8")).hexdigest()

    # [x^k] Bhat / binom(d,k) = (-1)^k Delta^k h_0.
    assert all(v > 0 for v in initial)
    return {
        "degree": d,
        "q_coefficients_strictly_alternating": q_alternating,
        "all_shifted_finite_differences_strictly_positive": all_strict,
        "finite_difference_cells": cells,
        "finite_difference_table_sha256": "sha256:" + digest,
        "target_initial_difference_row_strictly_positive": True,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--m",
        type=int,
        help="run one exact q/Hausdorff case m>=2 (default runs m=2..8)",
    )
    args = ap.parse_args()
    if args.m is not None:
        if args.m < 2:
            raise SystemExit("--m must be >=2")
        m_values = [args.m]
    else:
        m_values = list(range(2, 9))

    q_cache = {}
    hausdorff = []
    for m in m_values:
        q = q_coefficients(m)
        q_cache[m] = q
        row = {"m": m}
        row.update(finite_hcm(q))
        hausdorff.append(row)

    cb = []
    for m in range(2, 5):
        q = q_cache.get(m) or q_coefficients(m)
        via_secants = cb_q_coefficients(m)
        assert via_secants == q
        cb.append({
            "m": m,
            "degree": len(q) - 1,
            "signed_squared_secant_formula_matches_direct_q": True,
        })

    payload = {
        "schema": "PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_CERT_V1",
        "arithmetic": "exact Python fractions.Fraction",
        "proof_boundary": (
            "finite checks certify only the listed finite identities/regressions; "
            "the all-m Cauchy-Binet/secant formula and endpoint exponent bounds "
            "are proved symbolically in the paired research return"
        ),
        "row_minor_factorization": check_row_minor_factorization(3),
        "cauchy_binet_secant_q_regression": cb,
        "hausdorff_complete_monotonicity_regression": {
            "m_values": m_values,
            "rows": hausdorff,
            "interpretation": (
                "strict full finite Hausdorff complete monotonicity is exact "
                "regression only, not an all-m theorem"
            ),
        },
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
