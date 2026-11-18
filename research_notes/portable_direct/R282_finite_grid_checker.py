#!/usr/bin/env python3
"""R282 exact finite grids: rational multiaffine quotients and modular interpolation."""
from fractions import Fraction as Q
from itertools import product
import json


def inverse(a):
    n = len(a)
    z = [[Q(a[i][j]) for j in range(n)] + [Q(i == j) for j in range(n)] for i in range(n)]
    for k in range(n):
        p = next(i for i in range(k, n) if z[i][k])
        z[p], z[k] = z[k], z[p]
        piv = z[k][k]
        z[k] = [x/piv for x in z[k]]
        for i in range(n):
            if i != k:
                t = z[i][k]
                z[i] = [x-t*y for x, y in zip(z[i], z[k])]
    return [r[n:] for r in z]


def observe(w, edits, weights, a, b):
    z = [[Q(v) for v in row] for row in w]
    for (i, j), q in zip(edits, weights):
        z[i][j] += q
    assert all(sum(row) < 1 and all(v >= 0 for v in row) for row in z)
    n = len(z)
    return inverse([[Q(i == j)-z[i][j] for j in range(n)] for i in range(n)])[a][b]


def model(a, b, gamma):
    return [[Q(0), Q(a), Q(0)],
            [Q(0), Q(0), Q(0)],
            [Q(b), Q(gamma), Q(0)]]


w1 = model(Q(1, 4), Q(1, 4), Q(0))
w2 = model(Q(1, 4), Q(15, 64), Q(1, 4))
e = [(1, 2)]
read1 = [str(observe(w1, e, [x], 0, 0)) for x in [Q(0), Q(1, 4), Q(1, 2)]]
read2 = [str(observe(w2, e, [x], 0, 0)) for x in [Q(0), Q(1, 4), Q(1, 2)]]
assert read1 == ["1", "64/63", "32/31"]
assert read2 == ["1", "64/63", "448/433"]

# Scoped Port output equivalence can erase only edges irrelevant to that readout.
def isolated(z):
    w = [[Q(0) for _ in range(4)] for _ in range(4)]
    w[0][1] = w[2][0] = Q(1, 4)
    w[3][3] = Q(z)
    return w


edges = [(1, 2), (3, 3)]
grid = (Q(0), Q(1, 16), Q(1, 8))
assert all(
    observe(isolated(Q(0)), edges, x, 0, 0) ==
    observe(isolated(Q(1, 4)), edges, x, 0, 0)
    for x in product(grid, repeat=2)
)
assert observe(isolated(Q(0)), edges, (Q(0), Q(0)), 3, 3) == 1
assert observe(isolated(Q(1, 4)), edges, (Q(0), Q(0)), 3, 3) == Q(4, 3)

# Exhaustive degree<=2 interpolation over F_13 at 0, 1/16, 1/8.
p = 13
pts = [0, pow(16, -1, p), (2*pow(16, -1, p)) % p]
assert pts == [0, 9, 5]


def qeval(c, x):
    return (c[0] + c[1]*x + c[2]*x*x) % p


nullspace = [(a, b, c) for a, b, c in product(range(p), repeat=3)
             if all(qeval((a, b, c), x) == 0 for x in pts)]
assert nullspace == [(0, 0, 0)]


def mod(q):
    q = Q(q)
    assert q.denominator % 13 != 0
    return q.numerator * pow(q.denominator, -1, 13) % 13


assert [mod(Q(s)) for s in read1[:2]] == [mod(Q(s)) for s in read2[:2]]
assert mod(Q(read1[2])) != mod(Q(read2[2]))

result = {
    "status": "PASS",
    "models": 4,
    "counterexample_two_point_values": read1[:2],
    "model1_three_values": read1,
    "model2_three_values": read2,
    "distinguishing_third_value": str(Q(1, 2)),
    "two_edit_cartesian_grid_points_checked": 9,
    "single_variable_finite_field_polynomials_exhausted": 13**3,
    "finite_field_interpolation_kernel": [list(v) for v in nullspace],
    "finite_field_grid_residues": pts,
    "scope": "one-label explicit stable Port witness; two-label readout-scope witness; exhaustive F13 quadratic kernel; universal theorem by multiquadratic polynomial identity",
    "source": "R281@a957ac339577bf794b46d25221f9e38a43c2128d",
    "frozen_pin": "43ec6098b1330ae86d0a7863be336c5d97f6ef34"
}
print(json.dumps(result, indent=2, ensure_ascii=False))
