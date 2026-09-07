"""Bounded exact exploration of symmetric seven-positive-point candidates.

Uses existing Phase I for feasibility at declared residual levels. This is
candidate discovery, not an optimization or exhaustive global certificate.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "experiments" / "owner_joint_observer_20260907"))
from exact_feasibility import solve_nonnegative, verify_certificate


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def symmetric_candidate(positive_layers, residual_budget):
    n, k = 6, 3
    signs = [1 if w in positive_layers else -1 for w in range(n+1)]
    # Magnitudes g_0,...,g_6, four pairs of residuals, then slack.
    rows = [[choose(n, w) for w in range(n+1)] + [0]*9]
    rhs = [Q(1)]
    for r in range(k+1):
        row = [signs[w]*choose(n-k, w-r) for w in range(n+1)]
        row += [int(j == r) for j in range(k+1)]
        row += [-int(j == r) for j in range(k+1)] + [0]
        rows.append(row)
        rhs.append(Q(0))
    rows.append([0]*7 + [choose(n, k)*choose(k, r) for r in range(k+1)]*2 + [1])
    rhs.append(residual_budget)
    certificate = solve_nonnegative(rows, rhs)
    assert verify_certificate(rows, rhs, certificate)
    if certificate.status == "INFEASIBLE":
        return None
    masses = [signs[w]*certificate.primal[w] for w in range(n+1)]
    f = {x: masses[sum(x)] for x in product((0, 1), repeat=6)}
    norm = sum(map(abs, f.values()), Q(0))
    residual = Q(0)
    for axes in combinations(range(6), 3):
        table = {}
        for x, weight in f.items():
            y = tuple(x[i] for i in axes)
            table[y] = table.get(y, Q(0)) + weight
        residual += sum(map(abs, table.values()), Q(0))
    assert norm == 1 and residual <= residual_budget
    assert sum(value > 0 for value in f.values()) <= 7
    return masses, residual, norm/residual


if __name__ == "__main__":
    for layers in ((0, 1), (0, 5), (0, 6), (1,), (5,)):
        for budget in (Q(1), Q(4, 3), Q(2)):
            answer = symmetric_candidate(layers, budget)
            print(layers, str(budget), None if answer is None else [list(map(str, answer[0])), str(answer[1]), str(answer[2])])
