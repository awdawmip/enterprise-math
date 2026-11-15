#!/usr/bin/env python3
"""Independent exact EC49FPF native signed/named BRC Trie-cost certificate.
Usage: python VERIFY_EC49FPF_FIXED_FOUR.py EVIDENCE_DIRECTORY
The evidence directory needs frozen_original_master.txt, EC49FPD_PROFILE.csv
and EC49FPD_CLASSES.json from the immutable EC49FPD/EC49FPF evidence.
No floating point, MILP, or sampled search is needed.
"""
import csv
import hashlib
import itertools
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOTS = (3, 5, 6, 7)
B = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
SOURCE_SHA = "cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
TABLE_SHA = "2e07ad0d935efd9824729feec6349c2af162e152cd9c8a2a93848fd4343eea93"
assert hashlib.sha256((B / "frozen_original_master.txt").read_bytes()).hexdigest() == SOURCE_SHA
assert hashlib.sha256((B / "EC49FPD_PROFILE.csv").read_bytes()).hexdigest() == TABLE_SHA

with (B / "frozen_original_master.txt").open() as f:
    nk, nw, nc = map(int, f.readline().split())
    assert (nk, nw, nc) == (94, 178850, 38169)
    families = []
    total_words = 0
    for _ in range(nk):
        masks = [0] * 4
        count = int(f.readline())
        total_words += count
        for _ in range(count):
            label, code = f.readline().split()
            masks[ROOTS.index(int(code[:2], 16))] |= 1 << int(label)
        families.append(tuple(masks))
    assert total_words == nw
    configurations = [tuple(map(int, f.readline().split())) for _ in range(nc)]

def domain(keys):
    legal = [0] * 24
    for k in keys:
        for ri, mask in enumerate(families[k]):
            while mask:
                bit = mask & -mask
                legal[bit.bit_length() - 1] |= 1 << ri
                mask ^= bit
    assert all(legal)
    return tuple(legal)

domains = defaultdict(list)
for i, keys in enumerate(configurations):
    domains[domain(keys)].append(i)
assert len(domains) == 625

members = {int(k): v for k, v in json.loads(
    (B / "EC49FPD_CLASSES.json").read_text()).items()}
costs = defaultdict(dict)
with (B / "EC49FPD_PROFILE.csv").open() as f:
    for row in csv.DictReader(f):
        cid, root, subset, value = (
            int(row[k]) for k in ("config", "root", "subset", "cost"))
        assert (root, subset) not in costs[cid]
        costs[cid][root, subset] = value
assert sum(map(len, costs.values())) == 104104

CERT = {
    16864: {
        "queries": [79, 887, 920, 1212],
        "pairs": [(16864, 17249), (17249, 26174),
                  (17249, 26250), (19743, 26250)],
        "separated_per_pair": [144, 4, 20, 24],
    },
    16988: {
        "queries": [122, 502, 609, 847],
        "pairs": [(17373, 20051), (17373, 20659),
                  (17373, 32442), (20051, 32434)],
        "separated_per_pair": [20, 144, 4, 24],
    },
}
for rep, cert in CERT.items():
    d = domain(configurations[rep])
    ids = domains[d]
    assert len(ids) == 77 and ids == members[rep]
    optional = [l for l, allowed in enumerate(d) if allowed.bit_count() > 1]
    actions = list(itertools.product(*(
        tuple(ROOTS[j] for j in range(4) if d[label] >> j & 1)
        for label in optional)))
    assert len(actions) == 1296
    root_subsets = {
        r: sorted(s for rr, s in costs[rep] if rr == r)
        for r in ROOTS
    }
    unique = {}
    for cid in ids:
        p = tuple(costs[cid][r, s]
                  for r in ROOTS for s in root_subsets[r])
        unique.setdefault(p, cid)
    profiles = list(unique.values())
    assert len(profiles) == 39
    endpoints = {c for pair in cert["pairs"] for c in pair}
    assert endpoints <= set(profiles)
    response = {}
    for cid in profiles:
        values = []
        for action in actions:
            subset = {r: 0 for r in ROOTS}
            for label, r in zip(optional, action):
                subset[r] |= 1 << label
            values.append(sum(costs[cid][r, subset[r]] for r in ROOTS))
        response[cid] = values
    assert len({tuple(row) for row in response.values()}) == 39
    histogram = Counter()
    per_pair = [0] * 4
    for q in range(1296):
        hit = [response[a][q] != response[b][q]
               for a, b in cert["pairs"]]
        assert sum(hit) <= 1, (rep, q, hit)
        histogram[sum(hit)] += 1
        for i, b in enumerate(hit):
            per_pair[i] += int(b)
    assert histogram == {0: 1104, 1: 192}
    assert per_pair == cert["separated_per_pair"]
    queries = cert["queries"]
    assert len(queries) == len(set(queries)) == 4
    signatures = {tuple(response[cid][q] for q in queries)
                  for cid in profiles}
    assert len(signatures) == 39
    print("CHECK_OK", rep, "complete_configurations", len(ids),
          "root_profiles", len(profiles), "terminal_queries", len(actions),
          "zero_witness_actions", histogram[0],
          "one_witness_actions", histogram[1],
          "four_query_signatures", len(signatures),
          "optimal_fixed_depth", 4)
print("EC49FPF_EXACT_CERTIFICATE_PASS")
