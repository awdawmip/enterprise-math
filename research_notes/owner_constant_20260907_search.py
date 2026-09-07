"""Bounded numeric candidate search, followed by exact rational verification.

HiGHS values are only hints. Every reported lower bound is recomputed from a
finite rational signed array on all 64 binary X6 chart Cells and all 20 raw
marginal tables. No optimality/global-exhaustion claim is emitted.
"""
from fractions import Fraction as Q
from functools import reduce
from itertools import combinations, product
import json
from math import gcd, lcm
from pathlib import Path
import random

import numpy as np
from scipy.optimize import linprog

POINTS = tuple(product((0, 1), repeat=6))
AXES = tuple(combinations(range(6), 3))
ROWS = tuple((I, a) for I in AXES for a in product((0, 1), repeat=3))
A = np.array([[int(tuple(x[i] for i in I) == a) for x in POINTS] for I, a in ROWS], dtype=float)
I = np.eye(len(ROWS))
rng = random.Random(2026090719)


def exact_candidate(positive):
    sign = np.array([1 if i in positive else -1 for i in range(64)])
    signed = A * sign
    result = linprog(np.r_[np.zeros(64), np.ones(len(ROWS))],
                     A_ub=np.block([[signed, -I], [-signed, -I]]),
                     b_ub=np.zeros(2*len(ROWS)),
                     A_eq=np.array([np.r_[np.ones(64), np.zeros(len(ROWS))]]),
                     b_eq=np.array([1.0]), bounds=(0, None), method="highs")
    if not result.success:
        return None
    values = [Q(str(max(0.0, x))).limit_denominator(1000000) * int(s)
              for x, s in zip(result.x[:64], sign)]
    denominator = lcm(*(v.denominator for v in values))
    integers = [int(v * denominator) for v in values]
    divisor = reduce(gcd, (abs(v) for v in integers if v), 0)
    if not divisor:
        return None
    integers = [v//divisor for v in integers]
    positive_count = sum(v > 0 for v in integers)
    assert 1 <= positive_count <= 7
    tables = []
    for axes in AXES:
        table = {}
        for point, value in zip(POINTS, integers):
            address = tuple(point[i] for i in axes)
            table[address] = table.get(address, 0) + value
        tables.append(table)
    norm = sum(map(abs, integers))
    residual = sum(abs(v) for table in tables for v in table.values())
    assert residual > 0
    return Q(norm, residual), integers, norm, residual


initial = frozenset(i for i, x in enumerate(POINTS) if x[4:] == (0, 0) and sum(x[:4]) % 2 == 0 and any(x))
best_support, best = initial, exact_candidate(initial)
assert best is not None
seen = {initial}
tested = 1
for attempt in range(600):
    if attempt % 3 == 0:
        support = frozenset(rng.sample(range(64), 7))
    else:
        source = best_support if attempt % 7 else initial
        removed = rng.choice(tuple(source))
        added = rng.choice(tuple(set(range(64))-source))
        support = frozenset((source - {removed}) | {added})
    if support in seen:
        continue
    seen.add(support)
    result = exact_candidate(support)
    tested += 1
    if result is not None and result[0] > best[0]:
        best_support, best = support, result
        print("IMPROVED", tested, str(best[0]), flush=True)

ratio, values, norm, residual = best
payload = {
    "status": "EXACT_WITNESS_AFTER_BOUNDED_NUMERIC_DISCOVERY",
    "scope": "64 binary chart Cells; 600 attempted support mutations; no global optimization assertion",
    "supports_tested": tested,
    "positive_support": sum(v > 0 for v in values),
    "negative_support": sum(v < 0 for v in values),
    "l1": norm, "stacked_residual": residual, "ratio": str(ratio),
    "signed_integer_array": [[list(x), v] for x, v in zip(POINTS, values) if v],
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
