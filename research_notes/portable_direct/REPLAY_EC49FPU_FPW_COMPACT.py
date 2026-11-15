#!/usr/bin/env python3
"""Replay EC49FPU/FPV/FPW compact BRC splices on the original frozen input.
Usage: python3 REPLAY_EC49FPU_FPW_COMPACT.py RAW_MASTER ROOT_COST_CSV EC49FPT_CERT SPLICING_CERT
"""
import csv, hashlib, itertools, json, sys
from fractions import Fraction
from pathlib import Path
master, table, parent_path, steps_path = map(Path, sys.argv[1:5])
parent = json.loads(parent_path.read_text())
cert = json.loads(steps_path.read_text())
assert hashlib.sha256(master.read_bytes()).hexdigest() == parent['original_master_sha256'] == cert['original_master_sha256']
assert hashlib.sha256(table.read_bytes()).hexdigest() == parent['root_cost_table_sha256'] == cert['root_cost_table_sha256']
roots = (3, 5, 6, 7)
with master.open() as f:
    n, words, count = map(int, f.readline().split())
    assert (n, words, count) == (94, 178850, 38169)
    families = []
    for _ in range(n):
        masks = [0]*4
        for _ in range(int(f.readline())):
            label, word = f.readline().split()
            masks[roots.index(bytes.fromhex(word)[0])] |= 1 << int(label)
        families.append(masks)
    configurations = [tuple(map(int, f.readline().split())) for _ in range(count)]
def signature(keys):
    out = [0]*24
    for k in keys:
        for j, mask in enumerate(families[k]):
            while mask:
                bit = mask & -mask
                out[bit.bit_length()-1] |= 1 << j
                mask ^= bit
    return tuple(out)
dom = signature(configurations[16995])
ids = [i for i, c in enumerate(configurations) if signature(c) == dom]
assert len(ids) == 242
idset = set(ids)
cost = {}
with table.open(newline='') as f:
    for row in csv.DictReader(f):
        i = int(row['config'])
        if i in idset:
            cost.setdefault(i, {})[(int(row['root']), int(row['subset']))] = int(row['cost'])
keys = sorted(cost[ids[0]])
assert len(keys) == 96
profiles, weights = {}, []
for i in ids:
    p = tuple(cost[i][k] for k in keys)
    if p not in profiles:
        profiles[p] = len(profiles)
        weights.append(0)
    weights[profiles[p]] += 1
assert len(profiles) == 112
assert weights == parent['weights']
reps = parent['source_profile_ids']
assert [ids[0], len(reps)] == [16995, 112]
optional = [l for l, v in enumerate(dom) if v.bit_count() > 1]
allocations = list(itertools.product(*[tuple(r for j,r in enumerate(roots) if v>>j&1) for v in (dom[l] for l in optional)]))
assert len(allocations) == 324
rkeys = [(r,s) for r in roots for s in sorted(k[1] for k in keys if k[0] == r)]
assert len(rkeys) == 96
responses = []
for allocation in allocations:
    mask = {r:0 for r in roots}
    for l,r in zip(optional, allocation): mask[r] |= 1 << l
    responses.append([sum(cost[i][r,mask[r]] for r in roots) for i in reps])
for key in rkeys: responses.append([cost[i][key] for i in reps])
assert len(responses) == 420
FULL = (1<<112)-1
def members(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length()-1
        mask ^= bit
def groups(mask, q):
    b = {}
    for i in members(mask):
        v = responses[q][i]
        b[v] = b.get(v, 0) | (1<<i)
    return b
def restrict(tree, mask):
    if mask.bit_count() == 1: return {'leaf':next(members(mask))}
    q = tree['action_index']; b = groups(mask, q)
    if len(b) == 1: return restrict(tree['children'][str(next(iter(b)))], mask)
    return {'action_index':q,'children':{str(v):restrict(tree['children'][str(v)],m) for v,m in b.items()}}
def splice(tree, mask, path, q):
    if not path:
        b = groups(mask,q); assert len(b)>1
        return {'action_index':q,'children':{str(v):restrict(tree,m) for v,m in b.items()}}
    old = tree['action_index']; b = groups(mask,old)
    assert len(b)>1 and path[0] in b
    ch = dict(tree['children']); v = path[0]
    ch[str(v)] = splice(tree['children'][str(v)],b[v],path[1:],q)
    return {'action_index':old,'children':ch}
def measure(tree):
    R = T = 0
    for k in range(112):
        node = tree
        while 'leaf' not in node:
            q = node['action_index']
            R += weights[k]*(q>=324)
            T += weights[k]*(q<324)
            node = node['children'][str(responses[q][k])]
        assert node['leaf'] == k
    return R,T
assert measure(parent['tree']) == (762,44)
intervals = [(Fraction(44,79), Fraction(199,254))]
for scenario in cert['policies']:
    tree = parent['tree']
    for st in scenario['splices']:
        tree = splice(tree,FULL,st['path'],st['action'])
    R,T = measure(tree)
    assert [R,T] == scenario['weighted_counts']
    rp,tp = scenario['construction_prices']
    assert rp*R+tp*T == scenario['total_scaled']
    intervals.append((Fraction(T,841-R), Fraction(641-T,R)))
    print(scenario['tag'],'REPLAY_PASS',R,T,'TOTAL',scenario['total_scaled'])
left,right = intervals[0]
for a,b in intervals[1:]:
    assert a<right
    right = max(right,b)
assert (left,right) == (Fraction(44,79),Fraction(483,586))
print('FORCED_MIXING_INTERVAL_PASS',left,right)
