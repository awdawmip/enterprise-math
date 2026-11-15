#!/usr/bin/env python3
"""EC49FPE exact nonadaptive sensing certificate; no MILP or float required.
Usage: python VERIFY_EC49FPE_FIXED_FIVE.py PATH_TO_EC49FPD_EVIDENCE_DIR
Requires frozen_original_master.txt, EC49FPD_PROFILE.csv, EC49FPD_CLASSES.json.
"""
from pathlib import Path
from collections import defaultdict, Counter
import csv, hashlib, itertools, json, sys

ROOTS = (3, 5, 6, 7)
B = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
DATA = B / "frozen_original_master.txt"
SOURCE_SHA = "cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
TABLE_SHA = "2e07ad0d935efd9824729feec6349c2af162e152cd9c8a2a93848fd4343eea93"
assert hashlib.sha256(DATA.read_bytes()).hexdigest() == SOURCE_SHA
assert hashlib.sha256((B / "EC49FPD_PROFILE.csv").read_bytes()).hexdigest() == TABLE_SHA

with DATA.open() as f:
    nk, nw, nc = map(int, f.readline().split())
    assert (nk, nw, nc) == (94, 178850, 38169)
    fam = []
    words = 0
    for _ in range(nk):
        masks = [0] * 4
        num = int(f.readline())
        words += num
        for _ in range(num):
            label, code = f.readline().split()
            masks[ROOTS.index(int(code[:2], 16))] |= 1 << int(label)
        fam.append(tuple(masks))
    assert words == nw
    cases = [tuple(map(int, f.readline().split())) for _ in range(nc)]

def domain(keys):
    legal = [0] * 24
    for key in keys:
        for root_index, mask in enumerate(fam[key]):
            while mask:
                bit = mask & -mask
                legal[bit.bit_length() - 1] |= 1 << root_index
                mask ^= bit
    assert all(legal)
    return tuple(legal)

domains = defaultdict(list)
for cid, keys in enumerate(cases):
    domains[domain(keys)].append(cid)
assert len(domains) == 625
selected = {int(k): v for k, v in json.loads(
    (B / "EC49FPD_CLASSES.json").read_text()).items()}
entries = defaultdict(dict)
with (B / "EC49FPD_PROFILE.csv").open() as f:
    for row in csv.DictReader(f):
        cid, root, subset, cost = (
            int(row[k]) for k in ("config", "root", "subset", "cost"))
        assert (root, subset) not in entries[cid]
        entries[cid][root, subset] = cost
assert sum(map(len, entries.values())) == 104104

# Indices refer to FIRST occurrence of each distinct P profile in ascending
# original configuration order, not to every one of the 77 raw configurations.
CERT = {
    16860: {
        "pairs": [(0, 2), (0, 6), (0, 9), (0, 17), (6, 21)],
        "queries": [62, 331, 732, 868, 992],
        "source_pairs": [(16860, 18514), (16860, 19727),
                         (16860, 21230), (16860, 25850), (19727, 25949)],
    },
    17022: {
        "pairs": [(0, 4), (0, 7), (0, 20), (0, 22), (1, 22)],
        "queries": [114, 271, 776, 798, 1126],
        "source_pairs": [(17022, 25612), (17022, 33870),
                         (17022, 34409), (17022, 34418), (20175, 34418)],
    },
}
for rep, cert in CERT.items():
    d = domain(cases[rep])
    ids = domains[d]
    assert ids == selected[rep] and len(ids) == 77
    optional = [i for i, mask in enumerate(d) if mask.bit_count() > 1]
    actions = list(itertools.product(*(
        tuple(ROOTS[j] for j in range(4) if d[label] >> j & 1)
        for label in optional)))
    assert len(actions) == 1296
    root_subsets = {
        root: sorted(subset for rr, subset in entries[rep] if rr == root)
        for root in ROOTS}
    unique = {}
    for cid in ids:
        vector = tuple(
            entries[cid][root, subset]
            for root in ROOTS for subset in root_subsets[root])
        unique.setdefault(vector, cid)
    profiles = list(unique.values())
    assert len(profiles) == 31
    assert [(profiles[i], profiles[j]) for i, j in cert["pairs"]] == cert["source_pairs"]
    V = []
    for cid in profiles:
        responses = []
        for action in actions:
            subsets = {r: 0 for r in ROOTS}
            for label, root in zip(optional, action):
                subsets[root] |= 1 << label
            responses.append(sum(
                entries[cid][root, subsets[root]] for root in ROOTS))
        V.append(responses)
    assert len({tuple(v) for v in V}) == 31
    histogram = Counter()
    for query in range(1296):
        count = sum(
            V[i][query] != V[j][query] for i, j in cert["pairs"])
        assert count <= 1, (rep, query, count)
        histogram[count] += 1
    assert histogram == {0: 1038, 1: 258}, (rep, histogram)
    chosen = cert["queries"]
    assert len(chosen) == 5
    observed = {tuple(V[i][q] for q in chosen) for i in range(31)}
    assert len(observed) == 31
    print("CHECK_OK", "domain", rep, "configs", len(ids),
          "profiles", 31, "actions", 1296, "exclusive_pairs", 5,
          "no_pair_query", 1038, "one_pair_query", 258,
          "min_fixed_observations", 5)
print("EC49FPE_CERTIFICATE_PASS")
