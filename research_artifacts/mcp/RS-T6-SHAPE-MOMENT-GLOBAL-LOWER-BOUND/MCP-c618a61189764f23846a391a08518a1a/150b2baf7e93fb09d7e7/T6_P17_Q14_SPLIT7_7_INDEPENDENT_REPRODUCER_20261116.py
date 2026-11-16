#!/usr/bin/env python3
"""Independent exact reproduction of T6 p17 q14 split(7,7) pre-affine roster/count."""
import json, sys, itertools, time
from collections import Counter
from pathlib import Path

PRIMES = (2,3,5,7,11,13,17)
P, Q, B = 17, 7, 2331

def smooth(n):
    for d in PRIMES:
        while n % d == 0:
            n //= d
    return n == 1

def partitions(n, lo=1):
    if n == 0:
        yield ()
    for k in range(lo, n+1):
        for tail in partitions(n-k, k):
            yield (k,) + tail

def construct(atoms):
    lookup = {a:i for i,a in enumerate(atoms)}
    available = {q: tuple(r for qq,r in atoms if qq == q) for q in range(1,8)}
    out = set()
    part_counts = Counter()
    for part in partitions(Q):
        multiplicities = sorted(Counter(part).items())
        choices = [itertools.combinations_with_replacement(available[q],n)
                   for q,n in multiplicities]
        for blocks in itertools.product(*choices):
            indexes = tuple(sorted(lookup[(q,r)] for (q,n),block
                                   in zip(multiplicities,blocks) for r in block))
            cost = sum(289*atoms[i][0] + 17*atoms[i][1] - 1 for i in indexes)
            if cost <= B:
                assert indexes not in out, "duplicate canonical roster"
                out.add(indexes)
                part_counts[part] += 1
    return sorted(out), part_counts

def pair_count(rosters):
    masks = []
    for x in rosters:
        m = 0
        for i in x:
            m |= 1 << i
        masks.append(m)
    return sum((a & b) == 0 for k,a in enumerate(masks) for b in masks[k+1:])

def main(path):
    started = time.perf_counter()
    d = json.loads(Path(path).read_text(encoding="utf8"))
    assert d["schema"] == "T6_P17_Q14_SPLIT7_7_SIDE_ROSTER_V1"
    all_atoms = [(q,r) for q in range(1,8) for r in range(1,17)]
    atoms = [(q,r) for q,r in all_atoms if smooth(17*q+r)]
    assert d["atoms"] == [list(a) for a in atoms], "source atom roster mismatch"
    exact, by_partition = construct(atoms)
    full, _ = construct(all_atoms)
    assert d["roster_index_arrays"] == [list(x) for x in exact]
    observed = {"literal_atoms":len(all_atoms),"smooth_atoms":len(atoms),
      "literal_side_rosters":len(full),"admissible_side_rosters":len(exact),
      "unoriented_disjoint_sign_pairs":pair_count(exact),
      "literal_unoriented_disjoint_pairs":pair_count(full)}
    assert observed == d["reported_counts"], (observed,d["reported_counts"])
    assert observed == {"literal_atoms":112,"smooth_atoms":60,
      "literal_side_rosters":8697,"admissible_side_rosters":1907,
      "unoriented_disjoint_sign_pairs":809566,
      "literal_unoriented_disjoint_pairs":19582587}
    print(json.dumps({"status":"PASS_EXACT_PREFLIGHT","counts":observed,
      "partitions":{",".join(map(str,k)):v for k,v in sorted(by_partition.items())},
      "elapsed_seconds":round(time.perf_counter()-started,3)},sort_keys=True))
if __name__ == "__main__":
    assert len(sys.argv)==2, "usage: python checker.py canonical_roster.json"
    main(sys.argv[1])
