#!/usr/bin/env python3
"""EC49FOW five-allocation certificate; reads original frozen corpus and full integer CSV.
Usage: python EC49FOW_VERIFY_FIVE.py frozen_original_master.txt PROFILES_25_COMPLETE.csv
Run alongside EC49FOW_VERIFY_CLASS25.py, both in the same directory.
"""
import collections
import csv
import itertools
import json
import math
import sys
from pathlib import Path
from EC49FOW_VERIFY_CLASS25 import ROOTS, source, legal

FIVE = (477, 107, 137, 110, 367)

def verify(raw, costs):
    masks, words, cases = source(raw)
    domain = legal(cases[25], masks)
    ids = [c for c, case in enumerate(cases) if legal(case, masks) == domain]
    assert len(ids) == 442
    opt = [i for i, mask in enumerate(domain) if mask.bit_count() > 1]
    assert opt == [5, 7, 11, 13, 15, 17, 19, 21]
    options = [tuple(ROOTS[j] for j in range(4) if domain[i] & (1 << j)) for i in opt]
    allocations = list(itertools.product(*options))
    assert len(allocations) == 576
    profile = collections.defaultdict(dict)
    with costs.open() as file:
        for row in csv.DictReader(file):
            c, r, subset, value = (int(row[x]) for x in ('config','root','subset','cost'))
            profile[c][r,subset] = value
    assert set(profile) == set(ids)
    unique = {}
    for c in ids:
        p = tuple(profile[c][key] for key in sorted(profile[c]))
        assert len(p) == 292
        unique.setdefault(p,c)
    assert len(unique) == 344
    signatures = []
    for c in unique.values():
        def total(idx):
            subsets = {r:0 for r in ROOTS}
            for label,r in zip(opt,allocations[idx]):
                subsets[r] |= 1 << label
            return sum(profile[c][r,subsets[r]] for r in ROOTS)
        signatures.append(tuple(total(idx) for idx in FIVE))
    remaining = []
    for n in range(1,6):
        group = collections.Counter(sig[:n] for sig in signatures)
        remaining.append(sum(math.comb(count,2) for count in group.values()))
    assert remaining == [1340,99,29,13,0]
    assert len(set(signatures)) == len(unique) == 344
    return dict(configurations=442,distinct_root_profiles=344,
                five_allocation_indices=list(FIVE),
                five_allocations=[allocations[i] for i in FIVE],
                colliding_class_pairs_by_step=remaining,minimum_observation_count_claimed=False)

if __name__ == '__main__':
    assert len(sys.argv)==3
    print(json.dumps(verify(Path(sys.argv[1]), Path(sys.argv[2])),indent=2))
