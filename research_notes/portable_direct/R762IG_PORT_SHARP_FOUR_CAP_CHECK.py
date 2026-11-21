#!/usr/bin/env python3
"""R762IG: exact finite cap-four sharpness and local pair-deletion checks."""
from itertools import combinations
from collections import defaultdict, deque
import json
P = tuple(combinations(range(6), 2))
SALL = tuple(combinations(range(6), 3))
S=(0,1,2)
T=((0,1,3),(0,2,4),(1,2,5))
def triangle(s):
    v=tuple(combinations(s,2))
    return ((v[0],v[1]),(v[0],v[2]),(v[1],v[2]))
def comp(n):
    for a in range(n+1):
        for b in range(n-a+1):
            yield a,b,n-a-b
def pieces(s, cs):
    return [(s,e,k) for e,k in zip(triangle(s),cs) if k]
def legal(edges, base=(0,1)):
    deg=defaultdict(int)
    adj=defaultdict(set)
    for _,(u,v),k in edges:
        deg[u]+=k;deg[v]+=k
        adj[u].add(v);adj[v].add(u)
    if not deg[base] or any(d%2 for d in deg.values()):
        return False
    seen={base}; todo=[base]
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen:seen.add(v);todo.append(v)
    return seen==set(deg)
def components(cs):
    adj=defaultdict(set);vertices=set()
    for (u,v),k in zip(triangle(S),cs):
        if k:vertices|={u,v};adj[u].add(v);adj[v].add(u)
    remaining=set(vertices); ans=[]
    while remaining:
        u=remaining.pop();part={u};todo=[u]
        while todo:
            for v in adj[todo.pop()]:
                if v not in part:part.add(v);remaining.discard(v);todo.append(v)
        ans.append(frozenset(part))
    return frozenset(ans)
def can_remove(cs,i):
    if cs[i]<2:return False
    new=list(cs);new[i]-=2
    return components(cs)==components(new)
assert len(P)==15 and len(SALL)==20
assert len({v for e in triangle(S) for v in e})==3
shared=[]
for t in T:
    vi={v for e in triangle(t) for v in e}
    shared.append(vi.intersection({v for e in triangle(S) for v in e}))
assert shared==[{(0,1)},{(0,2)},{(1,2)}]
assert all(not ({v for e in triangle(T[i]) for v in e}&
                {v for e in triangle(T[j]) for v in e})
           for i in range(3) for j in range(i+1,3))
original=pieces(S,(2,0,2))
for t in T:original+=pieces(t,(1,1,1))
assert legal(original) and sum(k for _,_,k in original)==13
checked=even_count=legal_count=0
for s2 in comp(2):
    for a in comp(3):
        for b in comp(3):
            for c in comp(3):
                es=pieces(S,s2)+pieces(T[0],a)+pieces(T[1],b)+pieces(T[2],c)
                checked+=1
                deg=defaultdict(int)
                for _,(u,v),k in es:deg[u]+=k;deg[v]+=k
                even_count+=all(d%2==0 for d in deg.values())
                legal_count+=legal(es)
assert (checked,even_count,legal_count)==(6000,3,0)
local_count=0
for n in range(5,35):
    for cs in comp(n):
        assert any(can_remove(cs,i) for i in range(3)),(n,cs)
        local_count+=1
assert local_count==7735
hist=[]
for i,s in enumerate(SALL):
    cs=[1,1,1];cs[i%3]+=2*(2+i);cs[(i+1)%3]+=2*(i%4)
    hist.append((s,cs))
assert legal([e for s,cs in hist for e in pieces(s,cs)])
old_total=sum(sum(cs) for s,cs in hist)
reduced=[]
for s,initial in hist:
    cs=list(initial);n=sum(cs);target=n if n<=4 else (4 if n%2==0 else 3)
    while sum(cs)>target:
        i=next(i for i in range(3) if can_remove(cs,i))
        cs[i]-=2
    reduced.append((s,cs))
new_total=sum(sum(cs) for s,cs in reduced)
assert legal([e for s,cs in reduced for e in pieces(s,cs)])
assert new_total<=80
print(json.dumps({
 "status":"PASS R762IG","port_count":15,"support_count":20,
 "sharpness_original_legal":True,"sharpness_13_event_histogram":{"012":4,"013":3,"024":3,"125":3},
 "cap3_all_edge_allocations":checked,"cap3_even_degree_allocations":even_count,
 "cap3_legal_allocations":legal_count,
 "local_pair_delete_totals":[5,34],"local_pair_delete_triples":local_count,
 "mixed_original_length":old_total,"mixed_cap4_length":new_total,
 "claimed_uniform_optimal_cap":4,
 "scope":"composite Port Euler existence, not native P000 dynamics"
},sort_keys=True))
