#!/usr/bin/env python3
"""Exact no-upgrade support-choice fiber census, unsigned M3 Port-Euler auxiliary model.
No packages beyond Python standard library. Exact integer / GF(2) arithmetic.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
import json

missing = {(0,1),(2,3),(4,5)}
ports = [p for p in combinations(range(6),2) if p not in missing]
bit = {p:1 << i for i,p in enumerate(ports)}
cube = list(product((0,1),repeat=3))

def edge(a,b):
    return bit[a] ^ bit[b]

def projections(t):
    i,j,k=t
    return (i,2+j),(i,4+k),(2+j,4+k)

choices = []
for t in cube:
    a,b,c=projections(t)
    choices.append((edge(a,b),edge(a,c),edge(b,c)))

forced=[]
for support in combinations(range(6),3):
    ps=[p for p in combinations(support,2) if p not in missing]
    if len(ps)==2:
        forced.append(edge(*ps))
assert len(forced)==12
F={0}
for f in forced:
    F |= {x ^ f for x in tuple(F)}
assert len(F)==512

# Oracle 1: direct exact enumeration with witness storage.
direct=Counter()
connected=Counter()
witness=defaultdict(list)
for assignment in product(range(3),repeat=8):
    boundary=0
    for i,a in enumerate(assignment):
        boundary ^= choices[i][a]
    if boundary not in F:
        continue
    direct[boundary]+=1
    # Each edge-choice type links the corresponding pair of three forced components.
    # Two distinct types make that quotient graph connected.
    if len(set(assignment)) >= 2:
        connected[boundary]+=1
        if len(witness[boundary])<2:
            witness[boundary].append(assignment)

# Oracle 2: coefficient recurrence in Z[(Z/2)^12], independent of direct tuples.
dp={0:1}
for option in choices:
    nxt=Counter()
    for mask, count in dp.items():
        for e in option:
            nxt[mask ^ e]+=count
    dp=nxt
assert sum(dp.values())==3**8
assert all(dp.get(f,0)==direct[f] for f in F)
assert sum(direct.values())==1641
assert sum(connected.values())==1638
assert set(direct)==set(connected)
assert len(connected)==465
assert min(connected.values())==2
assert connected[0]==6 and direct[0]==9
assert all(direct.get(f,0)==0 for f in F if f not in connected)
assert Counter(connected.values())=={2:132,3:112,4:135,5:36,6:35,7:12,8:3}
assert sum(1 for f in F if direct.get(f,0)==0)==47
assert len(witness[783])==2 and witness[783][0]!=witness[783][1]
assert witness[783]==[(1,2,2,1,0,0,2,2),(2,1,1,2,0,0,2,2)]
assert (0,0,2,2,0,0,2,2) in witness[0]
# Confirm each of the three disconnected assignments is a constant edge type, boundary zero.
assert {b:direct[b]-connected[b] for b in F if direct[b]!=connected[b]}=={0:3}

result={
    "schema":"R762KL_EXACT_FIBER_CENSUS_V1",
    "model":"unsigned six-axis Port-Euler auxiliary; missing ports 01,23,45",
    "port_order":["".join(map(str,p)) for p in ports],
    "cube_order":["".join(str(x) for x in (i,2+j,4+k)) for i,j,k in cube],
    "choice_order":["AB","AC","BC"],
    "forced_boundary_size":len(F),
    "all_flexible_choice_assignments":3**8,
    "even_grid_boundary_assignments":sum(direct.values()),
    "connected_even_grid_assignments":sum(connected.values()),
    "reachable_forced_boundaries":len(connected),
    "holes":len(F)-len(connected),
    "connected_fiber_histogram":{str(k):v for k,v in sorted(Counter(connected.values()).items())},
    "forced_boundary_zero":{"total":direct[0],"connected":connected[0]},
    "full_euler_witness_boundary":0,
    "full_euler_witness_choice_vectors":[[0,0,2,2,0,0,2,2],[1,0,1,0,1,0,1,0]],
    "witness_boundary":783,
    "witness_choice_vectors":[list(x) for x in witness[783]],
    "all_passed":True
}
print(json.dumps(result,ensure_ascii=False,indent=2))
