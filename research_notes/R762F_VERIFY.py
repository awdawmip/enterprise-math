#!/usr/bin/env python3
"""R762F: exact global Pareto capacity frontiers for three directed triads.
Candidate port model only; Python stdlib, exact integers and permutations.
"""
from collections import deque
from itertools import product
import json

N = 6
E = tuple(range(N))
SUPPORTS = ((0, 1, 2), (0, 3, 4), (1, 3, 5))

def compose(p, q):
    return tuple(p[q[i]] for i in range(N))

def triad(s):
    p = list(E)
    a, b, c = s
    p[a], p[b], p[c] = b, c, a
    return tuple(p)

GENS = tuple(triad(s) for s in SUPPORTS)
ZERO = (0, 0, 0)

def below(a, b):
    return all(a[i] <= b[i] for i in range(3))

def step_count(c, i):
    return tuple(c[j] + int(i == j) for j in range(3))

# An exact antichain label-correcting algorithm, with no arbitrary cost cutoff.
labels = {E: {ZERO}}
queue = deque([(E, ZERO)])
processed = 0
while queue:
    p, c = queue.popleft()
    if c not in labels.get(p, ()):
        continue
    processed += 1
    for i, g in enumerate(GENS):
        pp = compose(p, g)
        cc = step_count(c, i)
        old = labels.get(pp, set())
        if any(below(d, cc) for d in old):
            continue
        labels[pp] = {d for d in old if not below(cc, d)} | {cc}
        queue.append((pp, cc))

assert len(labels) == 360
assert len({p for p in labels}) == 360
assert all(not (a != b and below(a, b)) for ls in labels.values()
           for a in ls for b in ls)
assert all(all(x >= 0 for x in c) for ls in labels.values() for c in ls)
# Closure certificate: every one-event extension is represented by a no-more-
# expensive known label of the identical final permutation. Hence the finite
# label family dominates ALL finite event histories, regardless of length.
for p, ls in labels.items():
    for c in ls:
        for i, g in enumerate(GENS):
            pp, cc = compose(p, g), step_count(c, i)
            assert any(below(d, cc) for d in labels[pp]), (p, c, i)

max_axis_counts = [max(c[i] for ls in labels.values() for c in ls)
                   for i in range(3)]
assert max_axis_counts == [8, 8, 8]
assert sum(len(ls) for ls in labels.values()) == 1861
assert max(map(len, labels.values())) == 12

# Independent count-vector recurrence in the complete [0,8]^3 box.
M = 8
DP = {ZERO: {E}}
R = {ZERO: {E}}
for c in product(range(M+1), repeat=3):
    if c == ZERO:
        continue
    current = set()
    covered = set()
    for i in range(3):
        if c[i]:
            prior = tuple(c[j] - int(i == j) for j in range(3))
            current.update(compose(p, GENS[i]) for p in DP[prior])
            covered.update(R[prior])
    DP[c] = current
    R[c] = covered | current
    assert R[c] == {p for p, ls in labels.items()
                    if any(below(d, c) for d in ls)}, c

full = {c for c, ps in R.items() if len(ps) == 360}
mins = sorted(c for c in full if all(
    (c[i] == 0 or tuple(c[j] - int(i == j) for j in range(3)) not in full)
    for i in range(3)))
expected = [
    (1,4,6), (1,5,5), (1,7,4), (2,3,4),
    (3,2,4), (3,3,3), (4,1,5), (4,2,3),
    (4,3,2), (4,7,1), (5,1,4), (5,5,1), (6,4,1)
]
assert mins == expected
assert len(R[2,2,2]) == 196
assert len(R[3,3,3]) == 360
assert len(R[1,4,6]) == 360

# Local predecessor noncoverage witnesses for each Pareto-minimal budget.
minimality_witnesses = []
for c in mins:
    missing = {}
    for i in range(3):
        if c[i]:
            smaller = tuple(c[j] - int(i == j) for j in range(3))
            absent = sorted(set(labels).difference(R[smaller]))
            assert absent
            missing[str(i)] = {"smaller_budget": list(smaller),
                               "missing_port_image": list(absent[0]),
                               "missing_port_count": len(absent)}
    minimality_witnesses.append({"budget": list(c), "predecessor_witnesses": missing})

report = {
    "schema": "R762F_GLOBAL_PARETO_BUDGET_CERTIFICATE_V1",
    "model": "six labelled ports; g012, g034, g135 single forward 3-cycles; independent per-generator finite upper budgets",
    "parent_task": "RS-X6-TRIADIC-CLOSURE-DYNAMICS",
    "frozen_source_commit": "a72226e2430ffa4786321ac86e7f0c599d5f0389",
    "exhaustive_algorithm": "unbounded nondominated-label fixed point, every one-step extension certified dominated; independent exact count-vector DP over [0,8]^3",
    "group_size": len(labels),
    "nondominated_endpoint_labels": sum(len(ls) for ls in labels.values()),
    "max_labels_per_permutation": max(map(len, labels.values())),
    "max_component_of_all_labels": max_axis_counts,
    "label_processing_steps": processed,
    "checked_one_step_extensions": sum(len(ls) for ls in labels.values()) * 3,
    "independent_budget_box": [M+1]*3,
    "independent_budget_cases": len(R),
    "full_coverage_cases_in_box": len(full),
    "global_pareto_minima": [list(c) for c in mins],
    "global_pareto_minima_count": len(mins),
    "minimality_witnesses": minimality_witnesses,
    "uniform_K2_port_count": len(R[2,2,2]),
    "uniform_K3_port_count": len(R[3,3,3]),
    "scientific_scope": "exact candidate finite group combinatorics; no native TRIADIC_CLOSURE_E scheduler or V29/V39 event realization inferred",
}
print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
