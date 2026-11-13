#!/usr/bin/env python3
"""R724: exact native X6 signed two-step Cell observer/path fibers.
Pure finite integer combinatorics; no force/BRC physics evolution."""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from pathlib import Path
import json

N = 6
TRIPLES = tuple(combinations(range(N), 3))
STEPS = tuple((a, s) for a in range(N) for s in (-1, 1))
ZERO = (0,) * N

def step(a, s):
    v = [0] * N
    v[a] = s
    return tuple(v)

def plus(x, y):
    return tuple(a + b for a, b in zip(x, y))

def can3(x, triple):
    vals = [x[a] for a in triple]
    return tuple(t - min(vals) for t in vals)

def mask(v):
    return sum(1 << i for i, t in enumerate(TRIPLES)
               if len({v[a] for a in t}) != 1)

def multiplicities(groups):
    return dict(sorted(Counter(map(len, groups)).items()))

def make_groups(entries, f):
    d = defaultdict(list)
    for p in entries:
        d[f(p)].append(p)
    return d

paths = []
for a, s in STEPS:
    for b, t in STEPS:
        x, y = step(a, s), step(b, t)
        v = plus(x, y)
        paths.append(((a, s), (b, t), x, v, mask(x), mask(v)))
assert len(paths) == 144

# Independently check the min-zero observation against mask formula.
for z in (ZERO, (-3, 2, 1, -4, 0, 5), (7, -6, 3, 8, -9, 4)):
    for p in paths:
        for v, claimed in ((p[2], p[4]), (p[3], p[5])):
            direct = sum(1 << j for j, triple in enumerate(TRIPLES)
                         if can3(z, triple) != can3(plus(z, v), triple))
            assert direct == claimed

end = make_groups(paths, lambda p: p[5])
trace = make_groups(paths, lambda p: (p[4], p[5]))
nets = sorted({p[3] for p in paths})
v_by_end = make_groups(nets, mask)
assert (len(end), len(trace), len(nets)) == (22, 42, 73)
assert multiplicities(end.values()) == {2: 6, 8: 15, 12: 1}
assert multiplicities(trace.values()) == {2: 12, 4: 30}
assert multiplicities(v_by_end.values()) == {1: 1, 2: 6, 4: 15}
assert Counter(mask_value.bit_count() for mask_value in end) == {0: 1, 10: 6, 16: 15}

future = {}
for h in range(3):
    Q = [ZERO]
    if h >= 1:
        Q += [step(a, s) for a, s in STEPS]
    if h >= 2:
        Q += [plus(step(a, s), step(b, t))
              for a, s in STEPS for b, t in STEPS]
    Q = list(dict.fromkeys(Q))
    groups = make_groups(nets, lambda v: tuple(mask(plus(v, q)) for q in Q))
    future[h] = {
        "continuation_displacements": len(Q),
        "signature_classes": len(groups),
        "fiber_multiplicities": multiplicities(groups.values()),
    }
assert [future[h]["signature_classes"] for h in range(3)] == [22, 67, 73]
assert future[0]["fiber_multiplicities"] == {1: 1, 2: 6, 4: 15}
assert future[1]["fiber_multiplicities"] == {1: 61, 2: 6}
assert future[2]["fiber_multiplicities"] == {1: 73}

# Axis-permutation covariance of 20-bit triple change masks.
triple_lookup = {t: i for i, t in enumerate(TRIPLES)}
for perm in permutations(range(N)):
    remapped_triples = [triple_lookup[tuple(sorted(perm[a] for a in t))]
                        for t in TRIPLES]
    for v in nets:
        remapped_v = [0] * N
        for a, x in enumerate(v):
            remapped_v[perm[a]] = x
        direct = mask(remapped_v)
        transported = sum(1 << remapped_triples[i] for i in range(len(TRIPLES))
                          if mask(v) & (1 << i))
        assert direct == transported

record = {
    "schema": "ENTERPRISE_MATH_R724_X6_TWO_STEP_OBSERVER_V1",
    "frozen_science_commit": "a72226e2430ffa4786321ac86e7f0c599d5f0389",
    "object_type": "signed_native_cell_coordinate_path_not_physical_triadic_closure",
    "axes": N, "signed_primitive_step_choices": len(STEPS),
    "ordered_length_two_paths": len(paths),
    "distinct_terminal_observer_masks": len(end),
    "terminal_fiber_multiplicity": multiplicities(end.values()),
    "distinct_midpoint_terminal_traces": len(trace),
    "trace_fiber_multiplicity": multiplicities(trace.values()),
    "distinct_net_displacements": len(nets),
    "net_fiber_multiplicity_by_terminal_mask": multiplicities(v_by_end.values()),
    "terminal_mask_weight_distribution": dict(sorted(
        Counter(x.bit_count() for x in end).items())),
    "future_horizon": future,
    "axis_permutations_tested": 720,
    "initial_cells_tested": 3,
    "path_code_bits_from_terminal": 4,
    "path_code_bits_from_trace": 2,
    "future_safe_net_code_bits_from_terminal": 2,
    "result": "R724_TWO_STEP_X6_RESIDUAL_EXACT_PASS",
}
out = Path(__file__).with_name("R724_X6_TwoStep_Observer_20261111_evidence.json")
out.write_text(json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
               encoding="utf-8")
print(record["result"])
