#!/usr/bin/env python3
"""EC49FPX exact frozen native-BRC sensor witness.
Usage: python REPRODUCE_EC49FPX.py FROZEN_DIR EC49FPN.json EC49FPS.json EC49FPT.json
"""
import csv, hashlib, itertools, json, collections, sys
from fractions import Fraction
from pathlib import Path

D = Path(sys.argv[1])
FPN, FPS, FPT = [json.loads(Path(s).read_text()) for s in sys.argv[2:5]]
HMASTER = "cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
HROOT = "a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f"
assert hashlib.sha256((D / "frozen_original_master.txt").read_bytes()).hexdigest() == HMASTER
assert hashlib.sha256((D / "EC49FPG_PROFILE.csv").read_bytes()).hexdigest() == HROOT
roots = (3, 5, 6, 7)
with (D / "frozen_original_master.txt").open() as f:
    nfamilies, nwords, nconfigs = map(int, f.readline().split())
    assert (nfamilies, nwords, nconfigs) == (94, 178850, 38169)
    families = []
    for _ in range(nfamilies):
        m = [0] * 4
        for _ in range(int(f.readline())):
            label, word = f.readline().split()
            m[roots.index(bytes.fromhex(word)[0])] |= 1 << int(label)
        families.append(m)
    configs = [tuple(map(int, f.readline().split())) for _ in range(nconfigs)]

def signature(config):
    a = [0] * 24
    for family_id in config:
        for j, bits in enumerate(families[family_id]):
            for label in range(24):
                if bits >> label & 1:
                    a[label] |= 1 << j
    return tuple(a)

sig = signature(configs[16995])
ids = [i for i, c in enumerate(configs) if signature(c) == sig]
assert len(ids) == 242
opt = [l for l, m in enumerate(sig) if m.bit_count() > 1]
actions = list(itertools.product(*(tuple(r for j, r in enumerate(roots) if sig[l] >> j & 1) for l in opt)))
assert len(actions) == 324
subsets = {}
for r in roots:
    labels = [l for l in opt if sig[l] >> roots.index(r) & 1]
    subsets[r] = sorted(sum(1 << l for l, b in zip(labels, bs) if b)
                        for bs in itertools.product((0, 1), repeat=len(labels)))
assert sum(map(len, subsets.values())) == 96
entries = collections.defaultdict(dict)
idset = set(ids)
with (D / "EC49FPG_PROFILE.csv").open() as f:
    for row in csv.DictReader(f):
        cid = int(row["config"])
        if cid in idset:
            entries[cid][int(row["root"]), int(row["subset"])] = int(row["cost"])
keys = [(r, s) for r in roots for s in subsets[r]]
assert len(keys) == 96
profiles, weights, reps = {}, [], []
for cid in ids:
    p = tuple(entries[cid][k] for k in keys)
    if p not in profiles:
        profiles[p] = len(profiles)
        weights.append(0)
        reps.append(cid)
    weights[profiles[p]] += 1
assert len(profiles) == 112
assert weights == FPT["weights"] and reps == FPT["source_profile_ids"]

def response(cid, q):
    if q >= 324:
        return entries[cid][keys[q - 324]]
    masks = {r: 0 for r in roots}
    for l, r in zip(opt, actions[q]):
        masks[r] |= 1 << l
    return sum(entries[cid][r, masks[r]] for r in roots)

obs = [tuple(response(cid, q) for cid in reps) for q in range(420)]
FULL = (1 << 112) - 1

def mass(mask):
    return sum(weights[i] for i in range(112) if mask >> i & 1)

def partition(mask, q):
    g = {}
    for i in range(112):
        if mask >> i & 1:
            v = obs[q][i]
            g[v] = g.get(v, 0) | (1 << i)
    return g

def restrict_tree(old, mask):
    if mask.bit_count() == 1:
        return {"leaf": mask.bit_length() - 1}
    q = old["q"]
    g = partition(mask, q)
    assert len(g) > 1
    return {"action_index": q,
            "children": {str(v): restrict_tree(old["children"][str(v)], m) for v, m in g.items()}}

def weighted_reads(tree):
    nr = nt = 0
    for cid in ids:
        node = tree
        while "leaf" not in node:
            q = node["action_index"]
            nr += (q >= 324)
            nt += (q < 324)
            node = node["children"][str(response(cid, q))]
        assert node["leaf"] == profiles[tuple(entries[cid][k] for k in keys)]
    return nr, nt

base = restrict_tree(FPN["verified_tree"], FULL)
assert weighted_reads(base) == (0, 641)
node, mask = base, FULL
for v in (210, 205, 205):
    mask = partition(mask, node["action_index"])[v]
    node = node["children"][str(v)]
assert mask.bit_count() == 2 and mass(mask) == 37 and node["action_index"] == 4
assert len(partition(mask, 327)) == 2
node["action_index"] = 327
node["children"] = {str(v): {"leaf": m.bit_length() - 1}
                    for v, m in partition(mask, 327).items()}
assert weighted_reads(base) == (37, 604)
assert weighted_reads(FPT["tree"]) == (762, 44)
assert Fraction(604, 804) == Fraction(151, 201)
assert Fraction(151, 201) < Fraction(199, 254)
print("FORCED_MIXING", "44/79", "1", "R", 37, "T", 604,
      "configs", len(ids), "profiles", len(profiles))

def root_cost(node, mask):
    if mask.bit_count() == 1:
        return 0
    q = node["action_index"]
    g = partition(mask, q)
    if len(g) == 1:
        return root_cost(node["children"][str(next(iter(g)))], mask)
    return mass(mask) * (q >= 324) + sum(
        root_cost(node["children"][str(v)], m) for v, m in g.items()
        if m.bit_count() > 1)

least, candidates = None, 0
stack = [(FPS["tree"], FULL)]
while stack:
    node, mask = stack.pop()
    if mask.bit_count() == 1:
        continue
    old = root_cost(node, mask)
    for q in range(324):
        g = partition(mask, q)
        if len(g) < 2:
            continue
        saving = old - sum(root_cost(node, m) for m in g.values() if m.bit_count() > 1)
        if saving > 0:
            candidates += 1
            ratio = Fraction(mass(mask), saving)
            if least is None or ratio < least:
                least = ratio
    for v, m in partition(mask, node["action_index"]).items():
        if m.bit_count() > 1:
            stack.append((node["children"][str(v)], m))
assert candidates == 9747 and least == Fraction(44, 79)
print("SHARP_SINGLE_SPLICE", candidates, str(least))
print("EC49FPX_REPRODUCTION_PASS")
