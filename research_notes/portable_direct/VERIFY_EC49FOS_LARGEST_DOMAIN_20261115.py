#!/usr/bin/env python3
"""EC49FOS exact exhaustive witness checker (Python standard library).

Usage: python3 VERIFY_EC49FOS_20261115.py EXTRACTED_EVIDENCE_DIRECTORY
Requires the original frozen bytes + five complete C++ output fragments.
The supplied local research bundle also contains a NumPy-vectorized
checker and an independent original-byte-Trie implementation.
"""
import collections
import csv
import hashlib
import itertools
import json
import pathlib
import sys

D = pathlib.Path(sys.argv[1])
SRC = D / "EC49FOR_EVIDENCE_20261114/EC49FOQ_RADIUS3_EVIDENCE_20261114/master_and_radius3_cases.txt"
assert hashlib.sha256(SRC.read_bytes()).hexdigest() == "cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
ROOTS = (3, 5, 6, 7)
with SRC.open() as f:
    nk, nw, nc = map(int, f.readline().split())
    assert (nk, nw, nc) == (94, 178850, 38169)
    families = []
    for _ in range(nk):
        n = int(f.readline())
        row = [0] * 4
        for _ in range(n):
            label, word = f.readline().split()
            row[ROOTS.index(int(word[:2], 16))] |= 1 << int(label)
        families.append(row)
    cases = [tuple(map(int, f.readline().split())) for _ in range(nc)]

def domain(case):
    legal = [0] * 24
    for key in case:
        for j, mask0 in enumerate(families[key]):
            mask = mask0
            while mask:
                bit = mask & -mask
                legal[bit.bit_length() - 1] |= 1 << j
                mask ^= bit
    assert all(legal)
    return tuple(legal)

ids = [int(x) for x in (D / "EC49FOS_CLASS16768_IDS.txt").read_text().split()]
assert len(ids) == len(set(ids)) == 2368 and ids[0] == 16768
legal = domain(cases[16768])
assert [i for i, case in enumerate(cases) if domain(case) == legal] == ids
optional = [l for l, x in enumerate(legal) if x.bit_count() > 1]
assert optional == [5, 7, 11, 13, 15, 17, 19, 21]
choices = [tuple(ROOTS[j] for j in range(4) if (legal[l] >> j) & 1) for l in optional]
alloc = list(itertools.product(*choices))
assert len(alloc) == 1296

subsets = {}
must = {}
opts = {}
for j, r in enumerate(ROOTS):
    mine = [l for l in optional if legal[l] & (1 << j)]
    subsets[r] = tuple(sorted(sum(1 << l for l, take in zip(mine, flags) if take)
                       for flags in itertools.product((0, 1), repeat=len(mine))))
    must[r] = sum(1 << l for l in range(24) if legal[l] == 1 << j)
    opts[r] = sum(1 << l for l in mine)
assert sum(map(len, subsets.values())) == 336

data = {}
parts = [D / "EC49FOS_CLASS16768_PROFILES.csv"] + [
    D / ("EC49FOS_PART%d.csv" % i) for i in range(1, 5)]
for part in parts:
    with part.open() as f:
        for row in csv.DictReader(f):
            try:
                c, r, m, o, subset, cost = (
                    int(row[k]) for k in
                    ("config", "root", "must", "opt", "subset", "cost"))
            except (TypeError, ValueError):
                continue
            assert c in ids and r in ROOTS
            assert m == must[r] and o == opts[r]
            key = (r, subset)
            observed = data.setdefault(c, {})
            assert key not in observed, (c, key)
            observed[key] = cost
expected = {(r, subset) for r in ROOTS for subset in subsets[r]}
assert set(data) == set(ids)
for c, profile in data.items():
    assert set(profile) == expected and len(profile) == 336

root_equiv = collections.defaultdict(list)
terminal_equiv = collections.defaultdict(list)
# Every terminal allocation exactly sums four named-root reachable-subset costs.
allocation_keys = []
for assignment in alloc:
    assignment_keys = []
    for r in ROOTS:
        mask = sum(1 << l for l, selected_root in zip(optional, assignment)
                   if selected_root == r)
        assignment_keys.append((r, mask))
    allocation_keys.append(tuple(assignment_keys))
probes = (396, 1212, 33, 1096, 77, 845, 1124, 248, 666, 429, 24, 60, 378, 425, 485)
probe_equiv = {}
for c in ids:
    p = data[c]
    root_vector = tuple(p[r, s] for r in ROOTS for s in subsets[r])
    terminal_vector = tuple(sum(p[k] for k in keys) for keys in allocation_keys)
    probe_vector = tuple(terminal_vector[i] for i in probes)
    assert len(root_vector) == 336 and len(terminal_vector) == 1296
    if probe_vector in probe_equiv:
        assert probe_equiv[probe_vector] == root_vector
    else:
        probe_equiv[probe_vector] = root_vector
    root_equiv[root_vector].append(c)
    terminal_equiv[terminal_vector].append(c)

def pair_count(classes):
    return sum(len(v) * (len(v) - 1) // 2 for v in classes.values())

assert len(root_equiv) == len(terminal_equiv) == len(probe_equiv) == 258
assert pair_count(root_equiv) == pair_count(terminal_equiv) == 468517
assert {frozenset(v) for v in root_equiv.values()} == {
    frozenset(v) for v in terminal_equiv.values()}
print(json.dumps({
    "status": "EXACT_FINITE_CHECK_PASSED",
    "complete_configs": len(ids),
    "root_entries": len(ids) * 336,
    "terminal_evaluations": len(ids) * 1296,
    "unordered_pairs": len(ids) * (len(ids) - 1) // 2,
    "equivalence_classes": 258,
    "equal_pairs": 468517,
    "nonzero_gauge_pairs": 0,
    "15_probe_separation": True
}, indent=2))
