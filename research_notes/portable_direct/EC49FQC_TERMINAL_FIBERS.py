#!/usr/bin/env python3
"""Independently find terminal-indistinguishable full rooted profiles for class 16943.
Usage: python EC49FQC_TERMINAL_FIBERS.py frozen_original_master.txt EC49FPG_PROFILE.csv
"""
import collections
import csv
import hashlib
import itertools
import sys
from pathlib import Path

A, B = map(Path, sys.argv[1:3])
assert hashlib.sha256(A.read_bytes()).hexdigest() == "cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
assert hashlib.sha256(B.read_bytes()).hexdigest() == "a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f"
roots = (3, 5, 6, 7)
with A.open() as source:
    nf, nw, nc = map(int, source.readline().split())
    assert (nf, nw, nc) == (94, 178850, 38169)
    families = []
    for _ in range(nf):
        d = {r: set() for r in roots}
        for _ in range(int(source.readline())):
            label, word = source.readline().split()
            d[bytes.fromhex(word)[0]].add(int(label))
        families.append(d)
    configs = [tuple(map(int, source.readline().split())) for _ in range(nc)]

def domain(index):
    out = [set() for _ in range(24)]
    for fid in configs[index]:
        for root, labels in families[fid].items():
            for label in labels:
                out[label].add(root)
    return tuple(tuple(sorted(v)) for v in out)

target = domain(16943)
ids = [i for i in range(nc) if domain(i) == target]
assert len(ids) == 310
multi = [i for i, vals in enumerate(target) if len(vals) > 1]
alloc = list(itertools.product(*(target[k] for k in multi)))
assert len(alloc) == 144
coords = sorted((r, sum(1 << l for l, bit in zip(
    [k for k in multi if r in target[k]], bits) if bit))
    for r in roots for bits in itertools.product((0, 1), repeat=sum(r in target[k] for k in multi)))
assert len(coords) == 84
costs = collections.defaultdict(dict)
with B.open() as source:
    for row in csv.DictReader(source):
        i = int(row["config"])
        if i in ids:
            costs[i][int(row["root"]), int(row["subset"])] = int(row["cost"])
assert len(costs) == 310 and all(len(v) == 84 for v in costs.values())
profiles = collections.defaultdict(list)
for i in ids:
    profiles[tuple(costs[i][c] for c in coords)].append(i)
assert len(profiles) == 141
terminal_signatures = collections.defaultdict(list)
for profile, origin in profiles.items():
    index = origin[0]
    observations = []
    for assignment in alloc:
        masks = {r: 0 for r in roots}
        for label, r in zip(multi, assignment):
            masks[r] |= 1 << label
        observations.append(sum(costs[index][r, masks[r]] for r in roots))
    terminal_signatures[tuple(observations)].append((index, len(origin)))
pairs = [fiber for fiber in terminal_signatures.values() if len(fiber) > 1]
assert len(terminal_signatures) == 139 and len(pairs) == 2
assert sorted(tuple(sorted(i for i, _ in fiber)) for fiber in pairs) == [(17928, 38165), (24541, 38166)]
assert all(w == 1 for fiber in pairs for _, w in fiber)
print("EC49FQC_TERMINAL_FIBERS_PASS", len(terminal_signatures), pairs, "root_count_lower_bound=4")
