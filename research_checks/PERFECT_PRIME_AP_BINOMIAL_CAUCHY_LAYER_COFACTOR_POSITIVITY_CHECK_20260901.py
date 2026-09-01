#!/usr/bin/env python3
"""Exact finite checker for the Perfect Prime AP binomial Cauchy-layer cofactor task.

All arithmetic is fractions.Fraction. Finite ranges are regression/discovery only.
The all-m covariance reduction and inner-inertia obstruction are proved symbolically
in the paired research return.
"""
from __future__ import annotations

import argparse
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
    return [[sum(
        F((-1) ** s * comb(n, s)) * t ** s / F(i + 1 + m * j + b * s)
        for s in range(n + 1)
    ) for j in range(m)] for i in range(m)]


def actual_tau(m, t):
    return cofactor_tau(m, actual_h(m, t))


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


def peval(p, x):
    z = F(0)
    for c in reversed(p):
        z = z * x + c
    return z


def mobius_coefficients(q, d):
    # coefficients of (1+x)^d q(x/(1+x))
    out = [F(0)] * (d + 1)
    for k, c in enumerate(q):
        for j in range(d - k + 1):
            out[k + j] += c * comb(d - k, j)
    return out


def frac(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


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
    lam = [F((-1) ** s * comb(n, s)) * t ** s * c_js(m, j, s)
           for s in range(n + 1)]
    D = sum(lam)
    moments = [
        sum(lam[s] * F((y + b * s) ** r) for s in range(n + 1))
        for r in range(2 * n + 1)
    ]
    C = [[moments[r + q] - moments[r] * moments[q] / D
          for q in range(1, n + 1)] for r in range(1, n + 1)]
    return C, D, lam


def outer_covariance(m, t):
    n = m - 1
    S = [[F(0) for _ in range(n)] for _ in range(n)]
    Ds = []
    for j in range(n + 1):
        C, D, _ = inner_covariance(m, j, t)
        Ds.append(D)
        wj = F((-1) ** j * comb(n, j))
        for r in range(n):
            for q in range(n):
                S[r][q] += wj * C[r][q]
    return S, Ds


def tau_from_outer_covariance(m, t):
    n = m - 1
    S, Ds = outer_covariance(m, t)
    prod_w = F(1)
    prod_D = F(1)
    for j in range(n + 1):
        prod_w *= F((-1) ** j * comb(n, j))
        prod_D *= Ds[j]
    vand = F(1)
    for k in range(1, n + 1):
        vand *= factorial(k)
    return prod_w * prod_D * det(S) / (vand * vand)


def signed_cov_det_formula(m, j, t):
    n = m - 1
    b = m * m
    C, D, lam = inner_covariance(m, j, t)
    vand = F(1)
    zs = [m * j + b * s for s in range(n + 1)]
    for a in range(n + 1):
        for bidx in range(a + 1, n + 1):
            vand *= zs[bidx] - zs[a]
    rhs = vand * vand
    for x in lam:
        rhs *= x
    rhs /= D
    return det(C), rhs


def leading_minor_signs(a):
    signs = []
    for k in range(1, len(a) + 1):
        d = det([row[:k] for row in a[:k]])
        signs.append(1 if d > 0 else -1 if d < 0 else 0)
    return signs


def check_adjacent():
    rows = []
    for m in range(2, 8):
        b = m * m
        for s in range(3):
            base = F(m * m + 1, 2) + b * s
            root = (base + b) / base
            assert root > 1
            assert adjacent_tau(m, s, root, b) == 0
            assert adjacent_tau(m, s, F(1), b) != 0
            rows.append({"m": m, "s": s, "candidate": frac(root)})
    return rows


def check_covariance_reduction():
    rows = []
    for m in range(2, 7):
        for t in (F(1, 2), F(1)):
            direct = actual_tau(m, t)
            reduced = tau_from_outer_covariance(m, t)
            assert direct == reduced
            S, Ds = outer_covariance(m, t)
            assert all(D > 0 for D in Ds)
            for j in range(m):
                lhs, rhs = signed_cov_det_formula(m, j, t)
                assert lhs == rhs != 0
            rows.append({
                "m": m, "t": frac(t), "tau": frac(direct),
                "outer_det_sign": 1 if det(S) > 0 else -1,
                "outer_leading_minor_signs": leading_minor_signs(S),
            })
    # exact explicit witness: inner covariance is indefinite already at m=3
    C, D, _ = inner_covariance(3, 0, F(1))
    assert C == [
        [F(-2673, 16120), F(-12231, 16120)],
        [F(-12231, 16120), F(102303, 16120)],
    ]
    assert det(C) == F(-6561, 4030)
    return rows


def first_order_outer(m):
    # coefficient of t in each C_j: -n*c_1*delta(z^r)*delta(z^q)
    n = m - 1
    b = m * m
    S = [[F(0) for _ in range(n)] for __ in range(n)]
    for j in range(n + 1):
        y = m * j
        w = F((-1) ** j * comb(n, j))
        c1 = c_js(m, j, 1)
        for r in range(1, n + 1):
            dr = F((y + b) ** r - y ** r)
            for q in range(1, n + 1):
                dq = F((y + b) ** q - y ** q)
                S[r - 1][q - 1] += w * (-n * c1 * dr * dq)
    return S


def check_forced_order():
    rows = []
    for m in range(2, 8):
        n = m - 1
        S1 = first_order_outer(m)
        assert det(S1) != 0
        rows.append({
            "m": m,
            "forced_order": n,
            "first_order_outer_det_sign": 1 if det(S1) > 0 else -1,
        })
    return rows


def check_mobius(m_max):
    rows = []
    for m in range(2, m_max + 1):
        n = m - 1
        max_degree = n * (2 * m - 1)
        p = interpolate_integer_grid([actual_tau(m, F(k)) for k in range(max_degree + 1)])
        assert all(p[k] == 0 for k in range(n))
        assert peval(p, F(1, 2)) == actual_tau(m, F(1, 2))
        q = trim(p[n:])
        d = len(q) - 1
        assert d == n * (2 * m - 3)
        # total tau degree = n + d = 2 n^2
        assert len(p) - 1 == 2 * n * n
        bhat = mobius_coefficients(q, d)
        assert all(c > 0 for c in bhat)
        # The scaled cofactor of H~_x=(1+x)^n H_{x/(1+x)}
        # equals x^n (1+x)^n * Bhat_m(x).
        rows.append({
            "m": m,
            "tau_degree": len(p) - 1,
            "forced_t_order": n,
            "postfactor_degree": d,
            "mobius_coeff_count": len(bhat),
            "min_mobius_coeff": frac(min(bhat)),
            "tau_at_1": frac(actual_tau(m, F(1))),
            "double_endpoint_factor": f"x^{n}(1+x)^{n}",
        })
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--extended", action="store_true",
                    help="extend exact Mobius/Bernstein finite regression from m<=8 to m<=10")
    args = ap.parse_args()
    m_max = 10 if args.extended else 8
    payload = {
        "schema": "PERFECT_PRIME_AP_BINOMIAL_CAUCHY_LAYER_COFACTOR_POSITIVITY_CERT_V1",
        "arithmetic": "exact Python Fraction",
        "proof_boundary": "finite checks are regression/discovery only; all-m reduction and inertia obstruction are proved in the research return",
        "adjacent_layer_regression": check_adjacent(),
        "outer_covariance_reduction": check_covariance_reduction(),
        "forced_order_regression": check_forced_order(),
        "mobius_double_endpoint_regression": {
            "m_range": [2, m_max],
            "all_transformed_coefficients_positive": True,
            "interpretation": "finite evidence only; not an all-m proof",
            "rows": check_mobius(m_max),
        },
        "exact_obstruction_witness": {
            "m": 3, "j": 0, "t": "1",
            "inner_covariance": [["-2673/16120", "-12231/16120"],
                                 ["-12231/16120", "102303/16120"]],
            "determinant": "-6561/4030",
            "classification": "indefinite conditional covariance block",
        },
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
