#!/usr/bin/env python3
"""R762KB: exact full witnesses for all one-inactive-Port d=4,t=0 inventories."""
from itertools import combinations, permutations
import json

P=tuple(x for x in combinations(range(6),2) if x!=(0,1))
S=tuple(combinations(range(6),3))
F={(0,1,c) for c in range(2,6)}
H=[pair+tail for pair in ((0,1),(1,0)) for tail in permutations((2,3,4,5))]
TEMPLATES=[
 ((0,2,3), ((0,2),(0,3)),
  {(0,4,5):((0,4),(0,5)), (1,2,5):((1,2),(1,5)), (1,3,4):((1,3),(1,4))},
  {(0,2,4):((0,2),(2,4)), (0,3,5):((0,3),(3,5)), (1,2,3):((1,2),(2,3))}),
 ((2,3,4), ((2,3),(2,4)),
  {(0,2,5):((0,2),(0,5)), (0,3,4):((0,3),(0,4)), (1,2,3):((1,3),(2,3)),
   (1,2,4):((1,4),(2,4)), (1,2,5):((1,2),(1,5))},
  {(0,3,5):((0,3),(3,5)), (0,4,5):((0,4),(4,5))})
]

def perm_obj(x,p): return tuple(sorted(p[i] for i in x))
def perm_edge(e,p): return tuple(sorted((perm_obj(e[0],p),perm_obj(e[1],p))))
def allowed(s):
    ports=[x for x in combinations(s,2) if x!=(0,1)]
    return tuple(combinations(ports,2))

def verify(d,t,d_edge,repair,bridges):
    deg={p:0 for p in P}
    adj={p:set() for p in P}
    events=0
    for s in S:
        n=1 if s in F or s==d else 3 if s in t else 2
        opts=allowed(s)
        if s in F: es=(opts[0],)
        elif s==d: es=(d_edge,)
        elif s in repair:
            e=repair[s]
            es=tuple(x for x in opts if x!=e) if n==2 else (e,next(x for x in opts if x!=e),next(x for x in opts if x!=e))
        else:
            e=bridges.get(s,opts[0])
            es=(e,e) if n==2 else opts
        assert len(es)==n and all(e in opts for e in es)
        events+=len(es)
        for a,b in es:
            deg[a]+=1
            deg[b]+=1
            adj[a].add(b)
            adj[b].add(a)
    assert events==42 and all(x>0 and x%2==0 for x in deg.values())
    seen={P[0]}
    todo=[P[0]]
    while todo:
        x=todo.pop()
        for y in adj[x]-seen:
            seen.add(y)
            todo.append(y)
    assert len(seen)==14

count=0
for rep_d,rep_edge,rep_repair,rep_bridges in TEMPLATES:
    ds={perm_obj(rep_d,p) for p in H}
    assert len(ds)==(12 if rep_d[0]==0 else 4)
    for d in sorted(ds):
        p=next(p for p in H if perm_obj(rep_d,p)==d)
        de=perm_edge(rep_edge,p)
        r={perm_obj(s,p):perm_edge(e,p) for s,e in rep_repair.items()}
        b={perm_obj(s,p):perm_edge(e,p) for s,e in rep_bridges.items()}
        for t in combinations(sorted(set(S)-F-{d}),7):
            verify(d,set(t),de,r,b)
            count+=1
assert count==102960
print(json.dumps({'profile':'d=4,t=0',
                  'verified_full_42_event_inventories':count,'failed':0,
                  'status':'AUTHOR_EXACT_FINITE_CHECKED_NOT_REVIEWED'}))
