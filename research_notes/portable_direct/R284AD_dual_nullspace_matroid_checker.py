#!/usr/bin/env python3
"""R284AD exact rational checks: nullity-order certificate and positive Port witness.

Python 3 and SymPy 1.14. Fixed-seed finite experiments are not universal proofs.
"""
from itertools import combinations
from pathlib import Path
from random import Random
import json
import sympy as S

SEED = 284019
rng = Random(SEED)


def select_pivot(A, r):
    n = A.rows
    for rows in combinations(range(n), r):
        for cols in combinations(range(n), r):
            if A.extract(rows, cols).det() != 0:
                return tuple(rows), tuple(cols)
    raise ValueError("rank certificate not found")


def basis_certificate(A):
    n = A.rows
    r = A.rank()
    s = n - r
    assert 1 <= s < n
    row_p, col_p = select_pivot(A, r)
    rows = row_p + tuple(i for i in range(n) if i not in row_p)
    cols = col_p + tuple(j for j in range(n) if j not in col_p)
    P = S.eye(n).extract(rows, tuple(range(n)))
    Q = S.eye(n).extract(tuple(range(n)), cols)
    T = P * A * Q
    B = T[:r, :r]
    D, E = T[r:, :r], T[:r, r:]
    assert T[r:, r:] == D * B.inv() * E
    left = S.Matrix.hstack(-D * B.inv(), S.eye(s)) * P
    right = Q * S.Matrix.vstack(-B.inv() * E, S.eye(s))
    assert left * A == S.zeros(s, n)
    assert A * right == S.zeros(n, s)
    gamma = P.det() * Q.det() * B.det()
    return left, right, gamma


def coefficient_table(A, edges):
    """Complete squarefree coefficients by independent Boolean evaluations."""
    m = len(edges)
    dets = []
    for mask in range(1 << m):
        C = A.copy()
        for e, (i, j) in enumerate(edges):
            if mask >> e & 1:
                C[i, j] += 1
        dets.append(C.det(method="bareiss"))
    coeff = dets.copy()
    for e in range(m):
        for mask in range(1 << m):
            if mask >> e & 1:
                coeff[mask] -= coeff[mask ^ (1 << e)]
    return coeff


def leading_products(left, right, gamma, edges, inds):
    L = S.Matrix.hstack(*(left[:, edges[i][0]] for i in inds))
    R = S.Matrix.vstack(*(right[edges[i][1], :] for i in inds))
    return S.expand(gamma * L.det() * R.det())


def max_common_independence(left, right, edges):
    m = len(edges)
    out = 0
    witness = None
    s = left.rows
    for mask in range(1 << m):
        ids = [i for i in range(m) if mask >> i & 1]
        k = len(ids)
        if k <= out or k > s:
            continue
        LL = S.Matrix.hstack(*(left[:, edges[i][0]] for i in ids))
        RR = S.Matrix.vstack(*(right[edges[i][1], :] for i in ids))
        if LL.rank() == k and RR.rank() == k:
            out, witness = k, ids
    return out, witness


def dual_min(left, right, edges):
    m = len(edges)
    vals = []
    for mask in range(1 << m):
        sel = [i for i in range(m) if mask >> i & 1]
        comp = [i for i in range(m) if not (mask >> i & 1)]
        a = S.Matrix.hstack(*(left[:, edges[i][0]] for i in sel)).rank() if sel else 0
        b = S.Matrix.vstack(*(right[edges[i][1], :] for i in comp)).rank() if comp else 0
        vals.append((a + b, mask, a, b))
    return min(vals)


def port_matrix(C, g=S.Rational(1, 16)):
    k = C.rows
    delta = S.Rational(1, 256 * k)
    L = delta * S.ones(k)
    D = delta * S.ones(k)
    U = delta * S.ones(k)
    G = S.BlockMatrix([[S.eye(k) - L, -C], [-D, S.eye(k) - U]]).as_explicit()
    WSQ = S.Matrix.vstack(S.zeros(k), g * S.eye(k))
    WPS = S.Matrix.hstack(g * S.eye(k), S.zeros(k))
    return S.Matrix.vstack(
        S.Matrix.hstack(G, -WSQ),
        S.Matrix.hstack(-WPS, S.zeros(k))
    )


def run():
    counts = {
        "generated_exact_rank_cases": 0,
        "sampled_boolean_determinants": 0,
        "checked_leading_coefficients": 0,
        "verified_lower_degree_zeros": 0,
        "matroid_max_min_equalities": 0,
        "leading_nonzero_witness_cases": 0,
        "leading_zero_cases": 0,
        "delayed_higher_degree_cases": 0,
    }
    delayed_examples = []
    for n in range(2, 6):
        for r in range(1, n):
            s = n - r
            for rep in range(12):
                # Positive low-rank baseline, with exact observed rank.
                while True:
                    X = S.Matrix(n, r, lambda i, j: rng.randint(1, 4))
                    Y = S.Matrix(r, n, lambda i, j: rng.randint(1, 4))
                    A = X * Y
                    if A.rank() == r:
                        break
                all_edges = [(i, j) for i in range(n) for j in range(n)]
                rng.shuffle(all_edges)
                edges = all_edges[:min(5, len(all_edges))]
                m = len(edges)
                left, right, gamma = basis_certificate(A)
                coeff = coefficient_table(A, edges)
                counts["generated_exact_rank_cases"] += 1
                counts["sampled_boolean_determinants"] += 1 << m
                for mask, value in enumerate(coeff):
                    deg = mask.bit_count()
                    if deg < s:
                        assert value == 0, (n, r, edges, mask, value)
                        counts["verified_lower_degree_zeros"] += 1
                    if deg == s:
                        ids = [i for i in range(m) if mask >> i & 1]
                        predicted = leading_products(left, right, gamma, edges, ids)
                        assert value == predicted, (n, r, edges, ids, value, predicted)
                        counts["checked_leading_coefficients"] += 1
                mx, witness = max_common_independence(left, right, edges)
                minsum, split, a, b = dual_min(left, right, edges)
                assert mx == minsum, ("matroid-minmax", n, r, edges, mx, minsum)
                counts["matroid_max_min_equalities"] += 1
                leading = any(value != 0 and mask.bit_count() == s
                              for mask, value in enumerate(coeff))
                assert leading == (mx == s)
                counts["leading_nonzero_witness_cases" if leading else "leading_zero_cases"] += 1
                if not leading and any(value != 0 and mask.bit_count() > s
                                       for mask, value in enumerate(coeff)):
                    counts["delayed_higher_degree_cases"] += 1
                    if len(delayed_examples) < 3:
                        delayed_examples.append({
                            "n": n, "base_rank": r,
                            "edges_1_based": [[u + 1, v + 1] for u, v in edges],
                            "dual_partition_mask": split,
                            "dual_partition_ranks": [a, b],
                            "first_nonzero_degree": min(
                                mask.bit_count() for mask, value in enumerate(coeff) if value != 0)
                        })

    # Independent exact stable-positive counterexample.
    c = S.Rational(1, 192)
    base = c * S.Matrix([[1, 1, 1], [1, 2, 1], [1, 1, 1]])
    assert base.rank() == 2
    edges = [(1, 0), (0, 1)]
    L, R, gamma = basis_certificate(base)
    assert all(leading_products(L, R, gamma, edges, [i]) == 0 for i in range(2))
    example = []
    for a in (0, c):
        for b in (0, c):
            C = base.copy()
            C[1, 0] += a
            C[0, 1] += b
            assert C.det() == -c * a * b
            A = port_matrix(C)
            assert A.det() == -S.Rational(1, 16) ** 6 * C.det()
            assert A.rank() == (9 if a and b else 8)
            delta = S.Rational(1, 768)
            for i in range(3):
                assert 3 * delta + sum(C[i, j] for j in range(3)) < 1
                assert 6 * delta + S.Rational(1, 16) < 1
            example.append({
                "t1": str(a), "t2": str(b),
                "core_det": str(C.det()), "port_det": str(A.det()),
                "port_rank": A.rank()
            })
    assert example[-1]["port_det"] == "1/118747255799808"
    return {
        "schema": "R284AD_EXACT_DUAL_NULLSPACE_LEADING_CERTIFICATE_V1",
        "status": "PASS",
        "seed": SEED,
        "arithmetic": "SymPy exact rational and integer Bareiss determinant, no floating point",
        "domain": "n=2..5, r=1..n-1, twelve fixed-seed positive full-rank factorizations per (n,r), m=min(5,n^2) distinct edited entries",
        "counts": counts,
        "delayed_random_examples": delayed_examples,
        "positive_stable_port_witness": example,
        "theorem_status": "Mathematical proof separate from finite tests; common-basis min-max invokes classical matroid-intersection theorem",
        "no_native_heartbeat_or_BRC_run_claimed": True,
    }


if __name__ == "__main__":
    out = run()
    evidence = Path(__file__).with_name("R284AD_dual_nullspace_matroid_verification.json")
    evidence.write_text(json.dumps(out, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
                        encoding="utf-8")
    print(json.dumps({"status": out["status"], "counts": out["counts"],
                      "positive_last": out["positive_stable_port_witness"][-1]},
                     ensure_ascii=False))
