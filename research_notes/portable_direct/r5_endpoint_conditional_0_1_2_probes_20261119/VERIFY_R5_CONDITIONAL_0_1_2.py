#!/usr/bin/env python3
"""Exact endpoint-class-conditional probe certificate for frozen R5 nine-state model.
Run beside frozen table, stages_18.json and 620-pair predecessor witness CSV.
No floating-point operations or unnamed hypothesis merges.
"""
import collections
import csv
import hashlib
import itertools
import json
from pathlib import Path

P = Path(__file__).resolve().parent
DATA = P / "EXACT_R5_ALL_101_BUDGETS.json"
WIT = P / "interior_distinguishing_budget_witnesses.csv"
EXPECTED_INPUT = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
EXPECTED_WITNESS = "3d2706270c490433b7c6fab8a4b606b570e771c27e35aed37260969225bacc32"
assert hashlib.sha256(DATA.read_bytes()).hexdigest() == EXPECTED_INPUT
assert hashlib.sha256(WIT.read_bytes()).hexdigest() == EXPECTED_WITNESS
D = json.loads(DATA.read_text())["counts_and_cohorts"]
centers = {k: [int(v) for v in D[str(k)]["counts"]] for k in range(214, 315)}
stages = [int(v) for v in json.loads((P / "stages_18.json").read_text())["stage_taus"]]
rows = list(csv.DictReader(WIT.open()))
assert len(rows) == 620 and len(stages) == 18

parent = {}
def find(x):
    parent.setdefault(x, x)
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[max(a, b)] = min(a, b)

def pair(r, p):
    return int(r["x" + p]), int(r["y" + p])

for r in rows:
    union(pair(r, "A"), pair(r, "B"))
classes = collections.defaultdict(set)
for a in parent:
    classes[find(a)].add(a)
edges = collections.defaultdict(list)
for r in rows:
    a, b = pair(r, "A"), pair(r, "B")
    edges[find(a)].append((a, b, int(r["witness_budget_list"])))

cache = {}
def support(a, k, stage):
    key = a, k, stage
    if key in cache:
        return cache[key]
    h = (18, 24, 82, 34, 17, a[0], 144, 208, a[1])
    values = [centers[k][i] for i in h]
    tau = stages[stage]
    # Independent exact method: closed correct-response interval right endpoints.
    masks = set()
    for t in {2*v + tau for v in values}:
        masks.add(sum(1 << i for i, v in enumerate(values)
                      if 2*v - tau <= t <= 2*v + tau))
    result = tuple(sorted(m for m in masks
                          if not any(m != n and m & n == m for n in masks)))
    cache[key] = result
    return result

probe_counts = collections.Counter()
members_counts = collections.Counter()
edge_counts = collections.Counter()
records = []
for anchor, vs in sorted(classes.items()):
    E = edges[anchor]
    budget_set = {v[2] for v in E}
    assert len(budget_set) == 1
    budget = budget_set.pop()
    need = set(range(len(E)))
    coverage = {}
    for stage in range(18):
        hits = {i for i, (a, b, _) in enumerate(E)
                if support(a, budget, stage) != support(b, budget, stage)}
        if hits:
            coverage[stage] = hits
    singles = [(s,) for s in coverage if coverage[s] == need]
    if singles:
        best = min(singles)
    else:
        doubles = [(a, b) for a, b in itertools.combinations(coverage, 2)
                   if coverage[a] | coverage[b] == need]
        assert doubles
        best = min(doubles)
    daughters = collections.defaultdict(list)
    for a in vs:
        daughters[tuple(support(a, budget, s) for s in best)].append(a)
    sizes = sorted(map(len, daughters.values()))
    assert len(E) == sum(sizes[i] * sizes[j]
                         for i in range(len(sizes))
                         for j in range(i + 1, len(sizes)))
    n = len(best)
    probe_counts[(budget, len(sizes), n)] += 1
    members_counts[n] += len(vs)
    edge_counts[n] += len(E)
    records.append({"anchor": list(anchor), "members": len(vs),
                    "witness_edges": len(E), "budget": budget,
                    "daughters": len(sizes), "daughter_sizes": sizes,
                    "min_extra_probes": n, "stages": list(best)})

assert len(records) == 108 and sum(edge_counts.values()) == 620
assert probe_counts == {(214, 2, 1): 40, (214, 3, 2): 40, (220, 2, 1): 28}
assert members_counts == {1: 256, 2: 192}
assert edge_counts == {1: 284, 2: 336}

# One genuinely three-daughter class proves worst-case minimum >=2:
# independently test ALL 101 original budgets, not only the predecessor's two.
example = next(r for r in records if r["min_extra_probes"] == 2)
E = edges[tuple(example["anchor"])]
for k in range(214, 315):
    for s in range(18):
        assert any(support(a, k, s) == support(b, k, s) for a, b, _ in E)

out = {
    "status": "PASS_EXACT",
    "frozen_sha256": EXPECTED_INPUT,
    "witness_sha256": EXPECTED_WITNESS,
    "endpoint_classes": 2563,
    "full_interval_classes": 2711,
    "exceptional_classes": len(records),
    "class_types": {",".join(map(str, k)): v for k, v in sorted(probe_counts.items())},
    "ordinary_zero_probe_instances": 30876 - sum(members_counts.values()),
    "one_probe_instances": members_counts[1],
    "two_probe_instances": members_counts[2],
    "conditional_worst_case": 2,
    "global_fixed_worst_case": 3,
    "sum_extra_probes_uniform_population": members_counts[1] + 2*members_counts[2],
    "population": 30876,
    "witness_edges": 620,
    "lower_bound_example": example,
    "cache_entries": len(cache),
    "classes": records,
}
(P / "R5_CONDITIONAL_PROBE_RESULT.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n")
print("PASS_EXACT_CLASS_CONDITIONAL_0_1_2",
      len(records), len(cache), sum(edge_counts.values()))
