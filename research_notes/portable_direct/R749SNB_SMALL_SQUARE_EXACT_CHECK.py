#!/usr/bin/env python3
"""R749SNB exact certificate: small-square signed Walsh minimax theorem.

Only Python standard library integer arithmetic and fractions.Fraction.
Reproduction: python R749SNB_SMALL_SQUARE_EXACT_CHECK.py
This exhaustively enumerates all possible vertices of the full 7D
(t,s,h,u,v,w,z) rational polytope in 0 <= s <= t <= 1/5.
"""
import collections
import itertools
import json
from fractions import Fraction as Q


def chi(mask, x):
    return 1 - 2 * ((mask & x).bit_count() % 2)


SOURCE_ROWS = []
for x in range(16):
    a, d, p, q = (chi(mask, x) for mask in (3, 12, 1, 4))
    SOURCE_ROWS.append((a, d, a * d, p, a * p, q, d * q))

# Each inequality is M[i] dot z >= rhs[i].
M = SOURCE_ROWS + [
    (0, 1, 0, 0, 0, 0, 0),       # s >= 0
    (1, -1, 0, 0, 0, 0, 0),      # t >= s
    (-5, 0, 0, 0, 0, 0, 0),      # t <= 1/5
]
RHS = [-1] * 16 + [0, 0, -1]


def solve_exact(indices):
    """Integer Bareiss elimination and exact rational back substitution."""
    n = 7
    m = [list(M[i]) + [RHS[i]] for i in indices]
    previous_pivot = 1
    for j in range(n - 1):
        pivot_row = next((i for i in range(j, n) if m[i][j]), None)
        if pivot_row is None:
            return None
        if pivot_row != j:
            m[j], m[pivot_row] = m[pivot_row], m[j]
        pivot = m[j][j]
        for i in range(j + 1, n):
            below = m[i][j]
            for k in range(j + 1, n + 1):
                numerator = m[i][k] * pivot - below * m[j][k]
                assert numerator % previous_pivot == 0
                m[i][k] = numerator // previous_pivot
            m[i][j] = 0
        previous_pivot = pivot
    if m[n - 1][n - 1] == 0:
        return None
    z = [None] * n
    for j in range(n - 1, -1, -1):
        z[j] = (
            Q(m[j][-1])
            - sum((m[j][k] * z[k] for k in range(j + 1, n)), Q(0))
        ) / m[j][j]
    return tuple(z)


def certify():
    count = collections.Counter()
    vertices = set()
    for active_set in itertools.combinations(range(19), 7):
        count["active_subsets"] += 1
        z = solve_exact(active_set)
        if z is None:
            continue
        count["nonsingular_subsets"] += 1
        if any(
            sum(a * b for a, b in zip(row, z)) < lower
            for row, lower in zip(M, RHS)
        ):
            continue
        count["feasible_bases"] += 1
        vertices.add(z)

    count["vertices"] = len(vertices)
    for z in vertices:
        t, s, h, u, v, w, zz = z
        if (t, s) == (0, 0):
            count["origin_vertices"] += 1
        elif (t, s) == (Q(1, 5), 0):
            count["axis_tip_vertices"] += 1
        elif (t, s) == (Q(1, 5), Q(1, 5)):
            count["diagonal_tip_vertices"] += 1
        else:
            raise AssertionError(("unexpected vertex parameter", (t, s)))
        # TV(mu,q) = sum(abs(difference_numerator))/32.
        # Target TV <= (1-s)/2.
        absolute_sum = sum(
            abs((h - s) * r[2] + u * r[3] + v * r[4]
                + w * r[5] + zz * r[6])
            for r in SOURCE_ROWS
        )
        slack = 16 * (1 - s) - absolute_sum
        assert slack >= 0, ("upper-bound counterexample", z, slack)
        if slack == 0:
            count["tight_vertices"] += 1
        count["slack_" + str(slack)] += 1

    assert (
        count["active_subsets"],
        count["nonsingular_subsets"],
        count["feasible_bases"],
        count["vertices"],
        count["origin_vertices"],
        count["axis_tip_vertices"],
        count["diagonal_tip_vertices"],
        count["tight_vertices"],
    ) == (50388, 24992, 1088, 123, 26, 44, 53, 59)
    assert sum(
        n for key, n in count.items() if key.startswith("slack_")
    ) == 123
    return dict(sorted(count.items()))


if __name__ == "__main__":
    result = {"research_unit": "R749SNB", "arithmetic": "exact_integer_and_Fraction",
              "status": "PASS", "certificate": certify()}
    print(json.dumps(result, indent=2, ensure_ascii=False))
