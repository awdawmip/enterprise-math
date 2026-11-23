#!/usr/bin/env python3
"""Independent SciPy/HiGHS finite-disjunct real-LP crosscheck for R284GC.
Not the exact universal proof: use R284GC_uniform_twoheavy_unsat_checker.py.
"""
from itertools import combinations, product
from scipy.optimize import linprog

PAIRS = list(combinations(range(4), 2))
ADJ = {(0, 1), (0, 3), (1, 2), (2, 3)}
BITS = {p: (0, p & 1, (p >> 1) & 1, (p >> 2) & 1) for p in range(1, 8)}
LAST = {(p, i): next(e for e in ((i - 1 - t) % 4 for t in range(4))
                      if BITS[p][e] != BITS[p][(e + 1) % 4])
        for p in range(1, 8) for i in range(4)}


def differing(i, j):
    return [p for p in range(1, 8) if BITS[p][i] != BITS[p][j]]


def cuts(i, j):
    edges = [(p, LAST[p, i], 4 + LAST[p, j]) for p in differing(i, j)]
    masks = {}
    for vertices in range(1, 256):
        mask = tuple(p for p, left, right in edges
                     if vertices >> left & 1 and vertices >> right & 1)
        if mask:
            masks[mask] = min(masks.get(mask, 9), vertices.bit_count())
    return list(masks.items())


def constraint(types, qcoef, minimum):
    """sum(x_p) - qcoef*q >= minimum, converted to A_ub*x <= b_ub."""
    row = [0.0] * 8
    row[0] = float(qcoef)
    for p in types:
        row[p] = -1.0
    return row, -float(minimum)


STAR = [cuts(0, j) for j in (1, 2, 3)]
for k in (8, 9):
    count = 0
    for chosen_cuts in product(*STAR):
        for light in combinations((3, 5, 6), 2):
            A = []
            b = []
            for i, j in ((1, 2), (1, 3), (2, 3)):
                a, rhs = constraint(differing(i, j), 2,
                                    5 if (i, j) in ADJ else 3)
                A.append(a)
                b.append(rhs)
            for mask, size in chosen_cuts:
                a, rhs = constraint(mask, size, 3)
                A.append(a)
                b.append(rhs)
            for p in light:
                a = [0.0] * 8
                a[0] = -2.0
                a[p] = 1.0
                A.append(a)
                b.append(1.0)
            result = linprog([0.0] * 8, A_ub=A, b_ub=b,
                             A_eq=[[-4.0] + [1.0] * 7],
                             b_eq=[float(k)],
                             bounds=[(5, None)] + [(0, None)] * 7,
                             method='highs')
            count += 1
            assert result.status == 2, (k, chosen_cuts, light, result.message)
    assert count == 1323
    print(f'k={k}: {count} real-LP branches: none feasible')
print('PASS: 2646 independently reconstructed floating-point LP checks')
