"""Exact finite checks for the X6 stability derivation, not a theorem proof.

The array helpers below are local evidence code. Positive BRC accumulation reuses
the existing public implementation. No recovery or feasibility solver is added.
"""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, product
import json
from math import comb
from pathlib import Path
import random
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from enterprise_math.brc_weighted import cwm_from_positive_weights, effective_multiplicity


def l1(f):
    return sum(map(abs, f.values()), Q(0))


def marginal(f, selected):
    out = defaultdict(Q)
    for point, weight in f.items():
        out[tuple(point[i] for i in selected)] += weight
    return dict(out)


def discrepancy(f, n, k):
    return sum((l1(marginal(f, axes)) for axes in combinations(range(n), k)), Q(0))


def difference(a, b):
    return {x: a.get(x, Q(0)) - b.get(x, Q(0)) for x in a.keys() | b.keys()}


@lru_cache(None)
def constant(n, k):
    if k == 0 or k == n:
        return Q(1)
    return ((n-k) * constant(n-1, k) + 2*k * constant(n-1, k-1)) / n


def check_slice_ledger(f, n, k, j):
    slices = defaultdict(dict)
    for x, w in f.items():
        slices[x[j]][x[:j] + x[j+1:]] = w
    heavy = [b for b, g in slices.items() if sum(w > 0 for w in g.values()) >= 2**(k-1)]
    assert len(heavy) <= 1
    light = [g for b, g in slices.items() if b not in heavy]
    light_norm = sum(map(l1, light), Q(0))
    d_j = sum((l1(marginal(f, I)) for I in combinations(range(n), k) if j in I), Q(0))
    d_not_j = discrepancy(f, n, k) - d_j
    assert light_norm <= constant(n-1, k-1) * d_j
    aggregate = marginal(f, tuple(i for i in range(n) if i != j))
    assert sum(w > 0 for w in aggregate.values()) <= sum(w > 0 for w in f.values())
    assert discrepancy(aggregate, n-1, k) == d_not_j
    assert l1(aggregate) <= constant(n-1, k) * d_not_j
    if heavy:
        assert l1(f) <= l1(aggregate) + 2 * light_norm
    else:
        assert l1(f) == light_norm
    assert l1(f) <= constant(n-1, k) * d_not_j + 2 * constant(n-1, k-1) * d_j


assert constant(6, 3) == Q(111, 20)
integer_rows = [[int(comb(n, k) * constant(n, k)) for k in range(n+1)] for n in range(1, 7)]
assert integer_rows[-1] == [1, 11, 49, 111, 129, 63, 1]

# All binary chart points are the declared finite population. Signs and weights
# vary, without deleting competing points from the population before measuring.
rng = random.Random(20260907)
sample_count = ledger_count = 0
for n in range(1, 7):
    carrier = tuple(product((0, 1), repeat=n))
    for k in range(n+1):
        for trial in range(20):
            count = rng.randrange(min(2**k, len(carrier)+1))
            positives = set(rng.sample(carrier, count))
            f = {x: (Q(rng.randint(1, 7), rng.randint(1, 5)) if x in positives
                     else -Q(rng.randint(0, 7), rng.randint(1, 5))) for x in carrier}
            assert sum(w > 0 for w in f.values()) < 2**k
            assert l1(f) <= constant(n, k) * discrepancy(f, n, k)
            sample_count += 1
            if 0 < k < n:
                for j in range(n):
                    check_slice_ledger(f, n, k, j)
                    ledger_count += 1

zero = (0,) * 6
unit = (1, 0, 0, 0, 0, 0)
rectangle = tuple(x + (0, 0) for x in product((0, 1), repeat=4))
even = {x: Q(1) for x in rectangle if sum(x) % 2 == 0}
odd = {x: Q(1) for x in rectangle if sum(x) % 2 == 1}
seven = {x: w for x, w in even.items() if x != zero}
clipped = difference(seven, odd)
assert len(seven) == 7 and len(odd) == 8
assert l1(clipped) == 15 and discrepancy(clipped, 6, 3) == 20
assert all(l1(marginal(clipped, I)) == 1 for I in combinations(range(6), 3))
assert l1(difference(even, odd)) == 16
assert discrepancy(difference(even, odd), 6, 3) == 0

# This simpler one-axis case saturates its own general recurrence constant;
# it is not asserted to establish sharpness for the X6 three-axis case.
star = {zero: Q(5)}
star.update({tuple(int(i == j) for i in range(6)): Q(-1) for j in range(6)})
assert l1(star) == 11 and discrepancy(star, 6, 1) == 6
assert l1(star) == constant(6, 1) * discrepancy(star, 6, 1)

brc_witnesses = []
for t in (Q(1, 10), Q(1, 100), Q(1, 1000)):
    mu, nu = {zero: Q(1)}, {zero: Q(1), unit: t}
    a, b = (cwm_from_positive_weights(x.values()) for x in (mu, nu))
    assert (a.count, a.total, a.dominant) == (1, Q(1), Q(1))
    assert (b.count, b.total, b.dominant) == (2, Q(1)+t, Q(1))
    assert discrepancy(difference(mu, nu), 6, 3) == 20*t
    a = cwm_from_positive_weights([t])
    b = cwm_from_positive_weights([t/2, t/2])
    assert effective_multiplicity(a) == 1 and effective_multiplicity(b) == 2
    brc_witnesses.append({"t": str(t), "count_jump": [1, 2], "E_at_vanishing_mass": [1, 2]})

moment_witnesses = []
for radius in (2, 10, 100):
    t = Q(1, radius**4)
    remote = (radius, radius, radius, radius, 0, 0)
    mu, nu = {zero: Q(1)}, {zero: 1-t, remote: t}
    f = difference(mu, nu)
    assert l1(f) == 2*t and discrepancy(f, 6, 3) == 40*t
    assert abs(sum(w*x[0]*x[1]*x[2]*x[3] for x, w in f.items())) == 1
    moment_witnesses.append({"radius": radius, "stacked_error": str(40*t), "joint_moment_error": "1"})

result = {
    "status": "PASS",
    "evidence_type": "EXACT_FINITE_CHECKS_NOT_GENERAL_THEOREM_PROOF",
    "seed": 20260907,
    "rational_array_samples": sample_count,
    "per_axis_slice_ledger_checks": ledger_count,
    "constant_6_3": str(constant(6, 3)),
    "binomially_scaled_constant_rows": integer_rows,
    "seven_vs_eight_witness": {"positive_support": 7, "negative_support": 8,
                               "l1_error": 15, "stacked_l1_residual": 20,
                               "lower_bound_on_universal_constant": "3/4"},
    "eight_vs_eight_zero_noise_failure": True,
    "one_axis_constant_saturating_witness": "11/6",
    "brc_executable_reused": "enterprise_math.brc_weighted.cwm_from_positive_weights",
    "brc_boundaries": brc_witnesses,
    "unbounded_joint_moment_boundaries": moment_witnesses,
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(result, ensure_ascii=False, indent=2))
