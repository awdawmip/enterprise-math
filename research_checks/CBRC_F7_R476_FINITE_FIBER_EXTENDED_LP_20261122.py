#!/usr/bin/env python3
"""Exact extended LP for the original CBRC F7 finite-box half-error question.

The matrix uses quarter-units (4*q), so epsilon=1/2 is RHS 2.
Matrix construction is exact-integer; HiGHS is only a numerical exploration
and is NOT a rational feasibility certificate.
"""
import argparse
import itertools
import time
import numpy as np
from scipy import sparse
from scipy.optimize import linprog


def fiber_grid(B):
    R = list(range(-2 * B, 2 * B + 1))
    T = {
        r: list(range(2 * r - min(B, r + B),
                      2 * r - max(-B, r - B) + 1))
        for r in R
    }
    assert sum(map(len, T.values())) == (2 * B + 1) ** 2
    return R, T


def finite_q_key(r, v):
    x, y = 2 * r - v, r - v
    key = (abs(x), y)
    if y == 0:
        return ("fixed", 0 if x == 0 else 4)
    if key in ((2, 1), (1, -1)):
        return ("fixed", 2)
    return ("variable", key)


def build_matrix(B, eps4=2):
    R, T = fiber_grid(B)
    qindex = {}
    for i, r in enumerate(R):
        for u in R[i + 1:]:
            for v in itertools.chain(T[r], T[u]):
                for rr in (r, u):
                    typ, value = finite_q_key(rr, v)
                    if typ == "variable" and value not in qindex:
                        qindex[value] = len(qindex)

    nq = len(qindex)
    npairs = len(R) * (len(R) - 1) // 2
    n = nq + 2 * npairs
    row, col, data, rhs = [], [], [], []

    def append_constraint(sign, r, u, v, auxiliary, bound):
        terms = {}
        fixed_part = 0
        for rr, coefficient in ((r, sign), (u, -sign)):
            typ, value = finite_q_key(rr, v)
            if typ == "fixed":
                fixed_part += coefficient * value
            else:
                j = qindex[value]
                terms[j] = terms.get(j, 0) + coefficient
        for j, coefficient in auxiliary:
            terms[j] = terms.get(j, 0) + coefficient
        i = len(rhs)
        for j, coefficient in terms.items():
            if coefficient:
                row.append(i)
                col.append(j)
                data.append(coefficient)
        rhs.append(bound - fixed_part)

    k = 0
    for i, r in enumerate(R):
        for u in R[i + 1:]:
            L, U = nq + 2 * k, nq + 2 * k + 1
            for t in T[r]:
                append_constraint(-1, r, u, t, [(L, 1)], 0)    # L <= F(t)
                append_constraint(+1, r, u, t, [(U, -1)], 0)   # F(t) <= U
            for s in T[u]:
                append_constraint(-1, r, u, s, [(U, 1)], eps4) # F(s) >= U-eps
                append_constraint(+1, r, u, s, [(L, -1)], eps4)# F(s) <= L+eps
            k += 1

    assert len(rhs) == 8 * B * (2 * B + 1) ** 2
    A = sparse.coo_matrix(
        (np.array(data, dtype=np.int8),
         (np.array(row, dtype=np.int32), np.array(col, dtype=np.int32))),
        shape=(len(rhs), n)
    ).tocsr()
    bounds = [(2, None)] * nq + [(None, None)] * (2 * npairs)
    return A, np.array(rhs, dtype=np.float64), bounds, qindex, npairs


def exact_oracle(B):
    """Compare direct 4D maximum and pair-fiber formula on one fixed integer q."""
    R, T = fiber_grid(B)

    def q4(x, y):
        if y == 0:
            return 0 if x == 0 else 4
        if (abs(x), y) in ((2, 1), (1, -1)):
            return 2
        return 2 + ((abs(x) * 113 + y * 19 + 7) % 3)

    def h(r, v):
        return q4(2 * r - v, r - v)

    direct = 0
    for a, b, c, d in itertools.product(range(-B, B + 1), repeat=4):
        k = a - 2 * b - c + 2 * d
        v = q4(a + k, b + k) + q4(c - k, d - k) - q4(a, b) - q4(c, d)
        direct = max(direct, abs(v))

    fiber = 0
    for i, r in enumerate(R):
        for u in R[i + 1:]:
            vals_r = [h(r, v) - h(u, v) for v in T[r]]
            vals_u = [h(r, v) - h(u, v) for v in T[u]]
            fiber = max(fiber, max(vals_u) - min(vals_r),
                        max(vals_r) - min(vals_u))
    assert direct == fiber
    return direct


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--B", type=int, default=15)
    parser.add_argument("--solve", action="store_true")
    parser.add_argument("--time-limit", type=int, default=20)
    args = parser.parse_args()
    if args.B < 1:
        parser.error("B must be >=1")
    started = time.time()
    A, rhs, bounds, qindex, npairs = build_matrix(args.B)
    print("B", args.B, "q_variables", len(qindex),
          "pair_variables", 2 * npairs, "inequalities", A.shape[0],
          "nonzeros", A.nnz, "build_seconds", round(time.time()-started, 3))
    if args.B <= 4:
        print("exact_oracle_max_quarter_units", exact_oracle(args.B))
    if args.solve:
        res = linprog(np.zeros(A.shape[1]), A_ub=A, b_ub=rhs,
                      bounds=bounds, method="highs",
                      options={"time_limit": args.time_limit})
        print("numerical_status", res.status, res.message)
        if res.x is not None:
            print("largest_inequality_residual",
                  float(np.max(A.dot(res.x) - rhs)))
            print("min_off_axis_q4", float(np.min(res.x[:len(qindex)])))
        # A successful floating-point solve is evidence of a candidate,
        # not exact rational certification; convert and check all rows exactly.


if __name__ == "__main__":
    main()
