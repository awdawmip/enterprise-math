"""Exact lower-bound and route-obstruction witnesses, not a general proof."""
from fractions import Fraction as Q
from itertools import combinations, product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from enterprise_math.brc_weighted import cwm_from_positive_weights

AXES = tuple(combinations(range(6), 3))
ZERO = (0,) * 6


def marginal(f, axes):
    result = {}
    for point, weight in f.items():
        address = tuple(point[i] for i in axes)
        result[address] = result.get(address, Q(0)) + weight
    return result


def l1(f):
    return sum(map(abs, f.values()), Q(0))


three_axis_cases = []
for active in AXES:
    f = {}
    for bits in product((0, 1), repeat=3):
        point = [0]*6
        for axis, bit in zip(active, bits):
            point[axis] = bit
        f[tuple(point)] = Q((-1)**sum(bits))
    positive, negative = [w for w in f.values() if w > 0], [-w for w in f.values() if w < 0]
    summaries = [cwm_from_positive_weights(leg) for leg in (positive, negative)]
    assert all((state.count, state.total, state.dominant) == (4, 4, 1) for state in summaries)
    residuals = {axes: l1(marginal(f, axes)) for axes in AXES}
    assert residuals[active] == 8
    assert all(value == 0 for axes, value in residuals.items() if axes != active)
    assert l1(f) == sum(residuals.values()) == 8
    normalized = {point: w/4 for point, w in f.items()}
    assert l1(normalized) == sum(l1(marginal(normalized, axes)) for axes in AXES) == 2
    for values in (positive, negative):
        summary = cwm_from_positive_weights([w/4 for w in values])
        assert (summary.count, summary.total, summary.dominant) == (4, Q(1), Q(1, 4))
    three_axis_cases.append({"active": list(active), "l1": 8, "stacked_l1": 8, "ratio": "1"})

punctured_cases = 0
for active in combinations(range(6), 4):
    h = {}
    for bits in product((0, 1), repeat=4):
        point = [0]*6
        for axis, bit in zip(active, bits):
            point[axis] = bit
        h[tuple(point)] = Q((-1)**sum(bits))
    assert all(l1(marginal(h, axes)) == 0 for axes in AXES)
    h.pop(ZERO)
    assert l1(h) == 15
    assert all(l1(marginal(h, axes)) == 1 for axes in AXES)
    assert l1(h) / sum(l1(marginal(h, axes)) for axes in AXES) == Q(3, 4)
    punctured_cases += 1

one_sided_minimum_cases = []
for active_count in range(3, 7):
    top = (1,)*active_count + (0,)*(6-active_count)
    h = {ZERO: Q(active_count-1), top: Q(1)}
    for j in range(active_count):
        h[tuple(int(i == j) for i in range(6))] = Q(-1)
    assert sum(value > 0 for value in h.values()) == 2
    assert sum(value < 0 for value in h.values()) == active_count
    assert all(l1(marginal(h, (j,))) == 0 for j in range(6))
    assert h[ZERO] != h[top]
    one_sided_minimum_cases.append(active_count)

output = {
    "status": "PASS",
    "scope": "EXACT_FINITE_WITNESSES_NOT_OPTIMAL_CONSTANT_PROOF",
    "new_uniform_constant_interval": ["1", "111/20"],
    "all_three_activity_sets": three_axis_cases,
    "punctured_four_axis_examples": punctured_cases,
    "k1_minimal_positive_but_unequal_weight_examples": one_sided_minimum_cases,
    "minimal_total_support_equal_weight_lemma": "PROVED_IN_NOTE_NOT_BY_ENUMERATION",
    "brc_reuse": "enterprise_math.brc_weighted.cwm_from_positive_weights",
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
print(json.dumps({key: value for key, value in output.items() if key != "all_three_activity_sets"}, indent=2))
