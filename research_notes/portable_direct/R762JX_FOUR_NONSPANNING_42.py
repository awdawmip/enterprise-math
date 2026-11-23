#!/usr/bin/env python3
"""Four explicit 42-event witnesses outside JX.1 triple-spanning condition.
The edges are numbered by the 15 lexicographically ordered Port pairs of six axes.
'/' separates the 20 colors in lexicographic order. Commas separate events.
All checked with independent stdlib graph and parity assertions.
"""
from itertools import combinations
from collections import Counter

CASES=[
 ((),(0,1,2,3,4),(5,6,7,8,9,10,11),
  '0-5/0-2/3-7/4-8/2-9/1-3,1-3,1-3/1-11,1-11,1-11/2-3,2-3,3-12/2-13,2-13,4-13/3-14,3-14,3-14/5-6,5-6,5-6/5-7,5-10,5-10/5-11,8-11/6-7,7-12/8-13,8-13/7-14,7-14/10-12,10-12/9-13,11-13/10-11,10-11/12-13,12-14'),
 ((0,),(4,5,6,7,8),(0,1,2,3,9,10,11),
  '1-5,1-5,1-5/2-6,2-6,2-6/3-7,3-7,3-7/4-8,4-8,4-8/2-9/3-10/1-11/2-3/2-13/3-4,3-14,3-14/5-9,5-9,5-9/5-10,5-10,7-10/5-8,5-8/6-12,6-12/6-13,8-13/8-14,8-14/9-10,9-10/9-11,9-13/11-14,11-14/12-14,12-14'),
 ((0,9),(5,6,7,8,9),(0,1,2,3,4,10,11),
  '1-5,1-5,1-5/2-6,2-6,2-6/3-7,3-7,3-7/4-8,4-8,4-8/1-2,1-2,1-2/1-3/1-11/3-12/4-13/3-14/5-6,5-6,5-6/5-7,5-7,7-10/5-8,5-8/6-7,7-12/6-13,8-13/8-14,8-14/10-12,10-12/11-13,11-13/10-14,11-14/12-13,12-14'),
 ((0,9,14),(5,6,7,8,11),(0,1,2,3,4,9,10),
  '1-5,1-5,1-5/2-6,2-6,2-6/3-7,3-7,3-7/4-8,4-8,4-8/1-2,1-2,1-2/1-10/1-4/2-12/2-4/3-4,3-4,3-4/5-6,5-6,5-6/7-10/8-11,8-11/6-7,7-12/6-13,8-13/7-8,7-8/10-12,10-12/11-13,11-13/10-11,10-11/12-13,12-13')
]
P=list(combinations(range(6),2));S=list(combinations(range(6),3));pi={p:i for i,p in enumerate(P)}
tri=[tuple(pi[q] for q in combinations(s,2)) for s in S]

def connected(V,edges):
    parent={v:v for v in V}
    def root(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]];v=parent[v]
        return v
    for u,v in edges:
        a,b=root(u),root(v)
        if a!=b:parent[a]=b
    return len({root(v) for v in V})==1

def verify(M,D,T,txt):
    V=set(range(15))-set(M)
    assert len(M)<=3 and len(D)==5 and len(T)==7 and not (set(D)&set(T))
    rows=[[(int(a),int(b)) for a,b in (e.split('-') for e in line.split(','))] for line in txt.split('/')]
    assert len(rows)==20
    edges=[];degree=Counter()
    for color,events in enumerate(rows):
        opts={tuple(sorted(e)) for e in combinations([p for p in tri[color] if p in V],2)}
        n=1 if color in D else 3 if color in T else 2
        assert len(events)==n
        for e in events:
            assert e in opts
            edges.append(e);degree.update(e)
    assert len(edges)==42
    assert all(degree[v]>=2 and degree[v]%2==0 for v in V)
    assert all(degree[v]==0 for v in M)
    assert connected(V,edges)
    # Construct the full flexible candidate support graph and its components.
    full=[k for k in range(20) if k not in D and all(v in V for v in tri[k])]
    flexedges=[e for k in full for e in combinations(tri[k],2)]
    # Require that the triple supports do NOT connect some flexible component.
    tripleedges=[e for k in T if k in full for e in combinations(tri[k],2)]
    # connectivity partition via ordinary pair reachability
    def reach(seed,arcs):
        seen={seed}
        while True:
            nxt=seen|{v for a,b in arcs for v in (a,b) if (a in seen or b in seen)}
            if nxt==seen:return seen
            seen=nxt
    seen=set();fails=0
    for v in sorted(V):
        if v in seen:continue
        comp=reach(v,flexedges);seen|=comp
        for u in comp:
            if reach(u,tripleedges)&comp!=comp:
                fails+=1;break
    assert fails>=1
    return fails

if __name__=='__main__':
    for i,(M,D,T,txt) in enumerate(CASES):print('M-size',len(M),'case',i,'triple_not_spanning_components',verify(M,D,T,txt))
    print('FOUR_EXACT_NONSPANNING_EULER_WITNESSES_PASS')
