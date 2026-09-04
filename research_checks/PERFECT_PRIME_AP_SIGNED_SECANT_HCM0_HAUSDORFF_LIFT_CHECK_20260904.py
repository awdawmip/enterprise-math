#!/usr/bin/env python3
"""Exact checkpoint checker for RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT.

Claims checked here are finite/exact only:
  * full shifted finite-Hausdorff complete monotonicity for m=11 and m=12,
    using the accepted predecessor's exact fractions.Fraction reconstruction;
  * an exact m=2 moment-matrix counterexample showing that strict total
    positivity plus positive binomial contractions alone does NOT imply the
    signed bipartite tree-cofactor sign;
  * the pure Cauchy-shift Lagrange/Schur factorization on finite regression
    cases m=2..6 and several rational shifts.

No finite regression is promoted to an all-m HCM0 proof.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE / "PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_CHECK_20260903.py"

EXPECTED = {
    11: {
        "degree": 190,
        "cells": 18336,
        "sha256": "abd4f6a5e6bc97161b151edb28e3017a8d96a03cf1273091860d1c427f8f9d93",
    },
    12: {
        "degree": 231,
        "cells": 27028,
        "sha256": "e44d1cb01420a206200158046b366e5d6ac953551ebcb580f8f84b6d0c64af40",
    },
}


def load_parent():
    spec = importlib.util.spec_from_file_location("perfect_prime_parent_checker", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PARENT}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def exact_hcm_row(parent, m: int):
    q = parent.q_coefficients(m)
    d = len(q) - 1
    h = [F((-1) ** a) * q[a] / F(comb(d, a)) for a in range(d + 1)]
    current = h
    k = 0
    cells = 0
    canonical = []
    full_strict = True
    initial_strict = True
    first_bad = None
    while current:
        signed = [F((-1) ** k) * v for v in current]
        if signed[0] <= 0:
            initial_strict = False
        for r, v in enumerate(signed):
            cells += 1
            canonical.append(f"{k}:{r}:{v.numerator}/{v.denominator}")
            if v <= 0 and first_bad is None:
                first_bad = [k, r, f"{v.numerator}/{v.denominator}"]
                full_strict = False
            elif v <= 0:
                full_strict = False
        current = [current[i + 1] - current[i] for i in range(len(current) - 1)]
        k += 1
    digest = hashlib.sha256("\n".join(canonical).encode()).hexdigest()
    out = {
        "m": m,
        "degree": d,
        "cells": cells,
        "hcm0_initial_row_strict": initial_strict,
        "full_shifted_hcm_strict": full_strict,
        "first_bad": first_bad,
        "sha256": digest,
    }
    exp = EXPECTED[m]
    assert d == exp["degree"]
    assert cells == exp["cells"]
    assert digest == exp["sha256"]
    assert initial_strict and full_strict and first_bad is None
    return out


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


def moment_counterexample():
    pts = [F(1, 10), F(4, 5)]
    mu = [sum(x ** k for x in pts) for k in range(4)]
    H = [[mu[0], mu[2]], [mu[1], mu[3]]]
    w = [F(1), F(-1)]
    det_h = H[0][0] * H[1][1] - H[0][1] * H[1][0]
    row_contractions = [sum(H[i][j] * w[j] for j in range(2)) for i in range(2)]
    col_contractions = [sum(H[i][j] * w[i] for i in range(2)) for j in range(2)]
    a, b = H[0]
    c, d = H[1]
    tree = a * b * c + b * c * d - a * c * d - a * b * d
    assert mu == [F(2), F(9, 10), F(13, 20), F(513, 1000)]
    assert det_h == F(441, 1000) > 0
    assert row_contractions == [F(27, 20), F(387, 1000)]
    assert col_contractions == [F(11, 10), F(137, 1000)]
    assert tree == F(-24039, 200000) < 0
    return {
        "measure": ["delta_1/10", "delta_4/5"],
        "moments_0_to_3": [str(v) for v in mu],
        "H": [[str(v) for v in row] for row in H],
        "det_H": str(det_h),
        "row_binomial_contractions": [str(v) for v in row_contractions],
        "col_binomial_contractions": [str(v) for v in col_contractions],
        "signed_tree_cofactor": str(tree),
        "interpretation": (
            "strict TP moment-matrix structure plus positive row/column binomial "
            "contractions is insufficient by itself to force the target tree-cofactor sign"
        ),
    }


def lagrange_values(nodes, x):
    out = []
    for j, yj in enumerate(nodes):
        num = F(1)
        den = F(1)
        for k, yk in enumerate(nodes):
            if k != j:
                num *= x - yk
                den *= yj - yk
        out.append(num / den)
    return out


def pure_cauchy_shift_regression():
    rows = []
    for m in range(2, 7):
        n = m - 1
        w = [F((-1) ** i * comb(n, i)) for i in range(m)]
        y = [F(m * j) for j in range(m)]
        for c in [F(0), F(1), F(7, 3)]:
            H = [[F(1) / F(i + 1 + m * j + c) for j in range(m)] for i in range(m)]
            E = [sum(H[i][j] * w[j] for j in range(m)) for i in range(m)]
            Fcol = [sum(H[i][j] * w[i] for i in range(m)) for j in range(m)]
            A = [w[i] * E[i] for i in range(m)]
            P = [[w[j] * H[i][j] / E[i] for j in range(m)] for i in range(m)]
            for i in range(m):
                expected = lagrange_values(y, -c - i - 1)
                assert P[i] == expected
            for j in range(m):
                for k in range(m):
                    lhs = sum(P[i][j] * A[i] * P[i][k] for i in range(m))
                    rhs = w[j] * Fcol[j] if j == k else F(0)
                    assert lhs == rhs
            L = [[F(0) for _ in range(2 * m)] for __ in range(2 * m)]
            for i in range(m):
                L[i][i] = w[i] * E[i]
                for j in range(m):
                    cc = w[i] * H[i][j] * w[j]
                    L[i][m + j] = -cc
                    L[m + j][i] = -cc
            for j in range(m):
                L[m + j][m + j] = w[j] * Fcol[j]
            assert det([row[:-1] for row in L[:-1]]) == 0
            rows.append({"m": m, "c": str(c), "lagrange_schur_identity": True})
    return rows


def pure_shift_laplacian(m, c):
    n = m - 1
    w = [F((-1) ** i * comb(n, i)) for i in range(m)]
    H = [[F(1) / F(i + 1 + m * j + c) for j in range(m)] for i in range(m)]
    E = [sum(H[i][j] * w[j] for j in range(m)) for i in range(m)]
    Fcol = [sum(H[i][j] * w[i] for i in range(m)) for j in range(m)]
    L = [[F(0) for _ in range(2 * m)] for __ in range(2 * m)]
    for i in range(m):
        L[i][i] = w[i] * E[i]
        for j in range(m):
            cc = w[i] * H[i][j] * w[j]
            L[i][m + j] = -cc
            L[m + j][i] = -cc
    for j in range(m):
        L[m + j][m + j] = w[j] * Fcol[j]
    return L


def two_shift_sign_regression():
    rows = []
    for m in range(2, 7):
        n = m - 1
        Lc = pure_shift_laplacian(m, F(0))
        Ld = pure_shift_laplacian(m, F(2))
        def tau(z, w):
            M = [[F(z) * Lc[i][j] + F(w) * Ld[i][j]
                  for j in range(2 * m)] for i in range(2 * m)]
            return det([row[:-1] for row in M[:-1]])
        t11 = tau(1, 1)
        t21 = tau(2, 1)
        alpha = (t21 - F(2 ** n) * t11) / F(2 ** m - 2 ** n)
        beta = t11 - alpha
        assert F((-1) ** n) * alpha > 0
        assert F((-1) ** n) * beta > 0
        assert tau(3, 2) == alpha * F(3 ** m) * F(2 ** n) + beta * F(3 ** n) * F(2 ** m)
        rows.append({
            "m": m,
            "c": "0",
            "d": "2",
            "two_shift_support": [[m, n], [n, m]],
            "both_coefficients_have_sign": f"(-1)^{n}",
        })
    return rows


def symbolic_small_multivariate():
    try:
        import sympy as sp
    except Exception as exc:
        raise RuntimeError("--symbolic-small requires sympy") from exc

    def tree_poly(m, basis):
        n = m - 1
        b = m * m
        vars_ = sp.symbols("z0:" + str(m))
        H = []
        for i in range(m):
            row = []
            for j in range(m):
                A0 = i + m * j
                if basis == "density":
                    val = 0
                    for r in range(m):
                        num = 1
                        for q in range(1, r + 1):
                            num *= q
                        num *= b ** r
                        den = 1
                        for s in range(r + 1):
                            den *= A0 + 1 + b * s
                        val += sp.Rational(num, den) * vars_[r]
                elif basis == "layers":
                    val = sum(
                        sp.Rational(((-1) ** s) * comb(n, s), A0 + 1 + b * s) * vars_[s]
                        for s in range(m)
                    )
                else:
                    raise ValueError(basis)
                row.append(val)
            H.append(row)
        w = [(-1) ** i * comb(n, i) for i in range(m)]
        L = sp.zeros(2 * m)
        for i in range(m):
            E = sum(H[i][j] * w[j] for j in range(m))
            L[i, i] = w[i] * E
            for j in range(m):
                cc = w[i] * H[i][j] * w[j]
                L[i, m + j] = -cc
                L[m + j, i] = -cc
        for j in range(m):
            Fv = sum(H[i][j] * w[i] for i in range(m))
            L[m + j, m + j] = w[j] * Fv
        return sp.Poly(sp.expand(L[:-1, :-1].det(method="domain-ge")), *vars_)

    expected_density_terms = {2: 3, 3: 18, 4: 110}
    expected_layer_terms = {2: 2, 3: 12, 4: 80}
    rows = []
    for m in range(2, 5):
        n = m - 1
        D = 2 * m - 1
        pd = tree_poly(m, "density")
        assert len(pd.terms()) == expected_density_terms[m]
        assert all(c > 0 for _, c in pd.terms())
        assert all(mon[0] <= D - n for mon, _ in pd.terms())
        pl = tree_poly(m, "layers")
        assert len(pl.terms()) == expected_layer_terms[m]
        for mon, c in pl.terms():
            weighted = sum(s * mon[s] for s in range(m))
            assert (1 if c > 0 else -1) == (-1) ** (weighted + n)
            assert max(mon) <= m
        rows.append({
            "m": m,
            "density_basis_terms": len(pd.terms()),
            "density_basis_all_coefficients_positive": True,
            "layer_basis_terms": len(pl.terms()),
            "layer_basis_sign": "sign(coeff)=(-1)^(weighted_layer_degree+n)",
        })
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m", type=int, choices=[11, 12], action="append",
                    help="exact HCM case to recompute; repeat to run both")
    ap.add_argument("--skip-hcm", action="store_true",
                    help="run only the fast structural exact checks")
    ap.add_argument("--symbolic-small", action="store_true",
                    help="also verify exact m=2..4 multivariate symbolic sign patterns")
    args = ap.parse_args()

    payload = {
        "schema": "PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT_CHECKPOINT_V1",
        "arithmetic": "exact fractions.Fraction",
        "proof_boundary": (
            "m=11,12 are finite exact regressions only. The all-m statements proved "
            "symbolically in the paired checkpoint are the coefficientwise-total-positivity "
            "moment-kernel lemma, the pure Cauchy-shift Lagrange/Schur factorization, and "
            "two-shift mixed-cell sign regularity. HCM0 remains open."
        ),
        "moment_tp_mechanism_obstruction": moment_counterexample(),
        "pure_cauchy_shift_regression": pure_cauchy_shift_regression(),
        "two_shift_sign_regression": two_shift_sign_regression(),
    }
    if args.symbolic_small:
        payload["small_multivariate_symbolic"] = symbolic_small_multivariate()
    if not args.skip_hcm:
        parent = load_parent()
        ms = args.m or [11]
        payload["hcm_exact_extension"] = [exact_hcm_row(parent, m) for m in ms]
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
