#!/usr/bin/env python3
"""EC49FNQ exact finite triple-stable native-BRC graph audit. Python standard library."""
import base64
import hashlib
import itertools
import json
import lzma
from pathlib import Path
from collections import Counter, defaultdict, deque

p = Path(__file__).with_name("EDGE_VECTOR_EC49FNP.u8x11.xz.b64")
raw = lzma.decompress(base64.b64decode(p.read_text().strip(), validate=True))
assert len(raw) == 11000
assert hashlib.sha256(raw).hexdigest() == "4d6540181b8c25a324aa701f551602ed53156be46b70170f1c104230c6443e9b"
rows = [tuple(raw[11*i:11*i+11]) for i in range(1000)]
K = [frozenset(r[:7]) for r in rows]
V = [tuple(r[7:10]) for r in rows]  # (native-prefix C, optimal allocation m, positive next-cost gap g)
assert len(set(K)) == 1000
assert all(len(k) == 7 and min(V[i]) > 0 for i,k in enumerate(K))

# Independent exchange enumerations: all unordered pairs, then inverse six-key index.
E = {(i,j) for i in range(1000) for j in range(i+1,1000)
     if len(K[i]-K[j]) == len(K[j]-K[i]) == 1}
six_to_ids = defaultdict(list)
for i,k in enumerate(K):
    for six in itertools.combinations(sorted(k),6):
        six_to_ids[six].append(i)
E_inv = set()
for ids in six_to_ids.values():
    E_inv.update(tuple(sorted((i,j))) for i,j in itertools.combinations(ids,2))
assert E == E_inv and len(E) == 27942
signature = Counter("".join(str(int(V[i][t] == V[j][t])) for t in range(3)) for i,j in E)
assert signature == {"000":3613,"001":4700,"010":2287,"011":3862,
                     "100":501,"101":830,"110":575,"111":11574}

adj = [set() for _ in K]
for i,j in E:
    if V[i] == V[j]:
        adj[i].add(j)
        adj[j].add(i)

# BFS and separately independent union-find must return the same exact components.
seen, components = set(), []
for start in range(1000):
    if start in seen:
        continue
    dq, comp = deque([start]), {start}
    seen.add(start)
    while dq:
        i = dq.popleft()
        for j in adj[i]:
            if j not in seen:
                seen.add(j)
                comp.add(j)
                dq.append(j)
    components.append(frozenset(comp))
parent = list(range(1000))
def root(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i
for i,j in E:
    if V[i] == V[j]:
        a,b = root(i),root(j)
        if a != b:
            parent[b] = a
uf = defaultdict(set)
for i in range(1000):
    uf[root(i)].add(i)
assert set(components) == {frozenset(c) for c in uf.values()}

hist = Counter(map(len, components))
assert len(components) == 244
assert hist == {1:155,2:53,3:10,4:2,5:1,6:3,7:1,8:2,9:1,14:1,
                16:1,18:1,24:1,30:1,34:1,36:3,38:1,40:1,42:1,43:1,67:1,85:1,87:1}
assert sum(bool(nei) for nei in adj) == 845
assert max(map(len,components)) == 87
assert all(len({V[i] for i in c}) == 1 for c in components)
assert len([c for c in components if len(c)==87 and V[next(iter(c))]==(138,1,1)])==1

# A provably shortest three-exchange path with disjoint three-key endpoint changes.
path = [32291,32296,32773,32916]
t = [i-32000 for i in path]
assert all(V[i] == (154,1,1) for i in t)
assert all(j in adj[i] for i,j in zip(t,t[1:]))
assert len(K[t[0]]-K[t[-1]]) == len(K[t[-1]]-K[t[0]]) == 3
assert len(path)-1 == 3

# All-pairs exact shortest distances, over each component (including isolates).
diameter=0
for c in components:
    for s in c:
        dist={s:0}
        dq=deque([s])
        while dq:
            i=dq.popleft()
            for j in adj[i]:
                if j not in dist:
                    dist[j]=dist[i]+1
                    dq.append(j)
        assert len(dist)==len(c)
        diameter=max(diameter,max(dist.values()))
assert diameter==4

same_pairs=sum(n*(n-1)//2 for n in Counter(V).values())
connected_pairs=sum(len(c)*(len(c)-1)//2 for c in components)
assert (same_pairs,connected_pairs,same_pairs-connected_pairs)==(18609,16558,2051)
def disjoint3(i,j):
    return len(K[i]-K[j])==len(K[j]-K[i])==3
c3=sum(any(disjoint3(i,j) for i,j in itertools.combinations(sorted(c),2)) for c in components)
v3=sum(any(disjoint3(i,j) for j in c if j!=i) for c in components for i in c)
assert (c3,v3)==(4,95)
print(json.dumps({"input_sha256":hashlib.sha256(raw).hexdigest(),
    "vertices":1000,"one_key_edges":len(E),"stable_edges":signature["111"],
    "signature_histogram":dict(sorted(signature.items())),
    "stable_components":len(components),"isolates":hist[1],"nonisolates":845,
    "component_size_histogram":dict(sorted(hist.items())),
    "largest_component":87,"largest_component_signature":[138,1,1],
    "max_stable_shortest_path":diameter,
    "three_swap_shortest_path":path,"three_swap_signature":[154,1,1],
    "disjoint_three_key_components":c3,"disjoint_three_key_vertices":v3,
    "equal_signature_pairs":same_pairs,"connected_equal_signature_pairs":connected_pairs,
    "disconnected_equal_signature_pairs":same_pairs-connected_pairs},indent=2,sort_keys=True))
