#!/usr/bin/env python3
"""Exact p17 q6 split(2,4) and split(3,3) affine-q0 check.

Reuses the published saturated 16D q0 lattice, exact rational
Gram-Schmidt, affine particular construction, frozen state generator,
and complete sphere search of the q5 source. No float comparisons.
The standalone computation was run separately in two and three
disjoint, exhaustive chunks; this is its compact reproducer.
"""
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py"
spec = importlib.util.spec_from_file_location("t6_p17_q5_exact", SOURCE)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)

assert len(old.STATES[2]) == 152
assert len(old.STATES[3]) == 1088
assert len(old.STATES[4]) == 6460
expected = {
    "2,4": {
        "raw_pairs": 981920, "shared_vertical_pairs": 262720,
        "primitive_pairs": 719200, "gs_nodes": 1917830,
        "sphere_leaves": 0, "budget_valid_kernels": 0,
        "max_sphere_R_squared": 4360450,
    },
    "3,3": {
        "raw_pairs": 591328, "shared_vertical_pairs": 171136,
        "primitive_pairs": 420192, "gs_nodes": 1035941,
        "sphere_leaves": 0, "budget_valid_kernels": 0,
        "max_sphere_R_squared": 4193408,
    },
}

result = {}
for a, b in [(2, 4), (3, 3)]:
    left, right = old.STATES[a], old.STATES[b]
    radius = ((2331 - min(x[1] for x in left)) ** 2
              + (2331 - min(x[1] for x in right)) ** 2)
    assert radius < old.Dmin
    counts = {
        "raw_pairs": 0, "shared_vertical_pairs": 0,
        "primitive_pairs": 0, "gs_nodes": 0,
        "sphere_leaves": 0, "budget_valid_kernels": 0,
        "max_sphere_R_squared": radius,
    }
    for i, pos in enumerate(left):
        positive = set(pos[0])
        for j, neg in enumerate(right):
            if a == b and j <= i:  # unoriented up to global sign
                continue
            counts["raw_pairs"] += 1
            if positive.intersection(neg[0]):
                counts["shared_vertical_pairs"] += 1
                continue
            counts["primitive_pairs"] += 1
            nodes, leaves, solution = old.ball_search(pos, neg)
            counts["gs_nodes"] += nodes
            counts["sphere_leaves"] += leaves
            if solution is not None:
                counts["budget_valid_kernels"] += 1
    key = f"{a},{b}"
    assert counts == expected[key], (key, counts)
    result[key] = counts
    print("verified", key, json.dumps(counts, sort_keys=True), flush=True)

print(json.dumps({
    "schema": "T6_P17_Q6_SPLIT24_33_REPRODUCER_V1",
    "source": SOURCE.name,
    "splits": result,
    "scope": "p17 valuation-one primitive q6 only",
    "status": "AUTHOR_CHECK_ONLY_UNREVIEWED_NOT_ADMITTED",
}, indent=2))
