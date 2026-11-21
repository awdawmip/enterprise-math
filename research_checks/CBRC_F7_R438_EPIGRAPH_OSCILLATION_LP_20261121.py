#!/usr/bin/env python3
"""F7 finite-cube oscillation LP, exact formulation / numerical feasibility experiment.

Every constraint here follows algebraically from the rank-one involution in
r437. HiGHS floating-point feasibility is exploratory, not an exact proof.
Usage: OPENBLAS_NUM_THREADS=1 python this_file.py [B=12] [q_upper=1]
"""
import sys
import time
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

B = int(sys.argv[1]) if len(sys.argv) > 1 else 12
q_upper = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
start = time.monotonic()


def scalar(x, y):
    a = abs(x)
    if a == 0 and y == 0:
        return None, 0.0
    if y == 0:
        return None, 1.0
    if (a, y) in ((2, 1), (1, -1)):
        return None, 0.5
    return (a, y), 0.0


def form(a, b, w):
    p, p0 = scalar(w + a - b, w - b)
    q, q0 = scalar(w + b - a, w - a)
    terms = {}
    if p is not None:
        terms[p] = terms.get(p, 0) + 1
    if q is not None:
        terms[q] = terms.get(q, 0) - 1
    return terms, p0 - q0


# R=I_a+b and S=I_b+a. F(r) and F(s) are linear in the q pair classes.
# One auxiliary c ensures F(s)<=c and F(r)>=c-eps.
# Another auxiliary d ensures F(r)<=d and F(s)>=d-eps.
# F_{b,a}=-F_{a,b}, with R and S swapped, so a<b suffices.
constraints = []
keys = set()
pairs = []
for a in range(-2 * B, 2 * B + 1):
    I_a = range(max(-B, -B - a), min(B, B - a) + 1)
    for b in range(a + 1, 2 * B + 1):
        I_b = range(max(-B, -B - b), min(B, B - b) + 1)
        pair_id = len(pairs)
        pairs.append((a, b))
        for m in I_a:
            terms, const = form(a, b, m + b)
            keys.update(terms)
            constraints.append((pair_id, 0, -1, terms, const, 0.5))  # c-F(r)<=1/2
            constraints.append((pair_id, 1, +1, terms, const, 0.0))  # F(r)-d<=0
        for ell in I_b:
            terms, const = form(a, b, ell + a)
            keys.update(terms)
            constraints.append((pair_id, 0, +1, terms, const, 0.0))  # F(s)-c<=0
            constraints.append((pair_id, 1, -1, terms, const, 0.5))  # d-F(s)<=1/2

q_keys = sorted(keys)
q_index = {key: i for i, key in enumerate(q_keys)}
nq = len(q_keys)
row, col, coef, rhs = [], [], [], []
for k, (pid, aux, sign, terms, const, limit) in enumerate(constraints):
    row.append(k)
    col.append(nq + 2 * pid + aux)
    coef.append(-sign)
    for key, value in terms.items():
        if value:
            row.append(k)
            col.append(q_index[key])
            coef.append(sign * value)
    rhs.append(limit - sign * const)

M = coo_matrix(
    (np.asarray(coef, dtype=np.int8),
     (np.asarray(row, dtype=np.int32), np.asarray(col, dtype=np.int32))),
    shape=(len(rhs), nq + 2 * len(pairs)),
).tocsr()
print(
    f"B={B} q_variables={nq} unordered_pairs={len(pairs)} "
    f"auxiliary_variables={2*len(pairs)} inequalities={len(rhs)} "
    f"nonzero_coefficients={M.nnz} seconds_to_build={time.monotonic()-start:.3f}",
    flush=True,
)
assert len(rhs) == 8 * B * (2 * B + 1) ** 2

res = linprog(
    np.zeros(M.shape[1]),
    A_ub=M,
    b_ub=np.asarray(rhs),
    bounds=[(0.5, q_upper)] * nq + [(-2, 2)] * (2 * len(pairs)),
    method="highs",
    options={"presolve": True, "time_limit": 110},
)
print(
    f"HiGHS_status={res.status} message={res.message} "
    f"seconds_total={time.monotonic()-start:.3f}",
    flush=True,
)
if res.x is not None:
    print(
        f"numerical_max_row_residual={np.max(M@res.x - np.asarray(rhs)):.4g} "
        f"q_range=[{min(res.x[:nq]):.12g},{max(res.x[:nq]):.12g}]",
        flush=True,
    )
