#!/usr/bin/env python3
"""R762KF: exact complete classification for two inactive pair Ports."""
from itertools import combinations
from functools import reduce
from math import comb

AX=tuple(range(6))
PAIRS=tuple(combinations(AX,2))
COLORS=tuple(combinations(AX,3))

def cut(inactive):
    ports=tuple(p for p in PAIRS if p not in inactive)
    index={v:i for i,v in enumerate(ports)}
    edge={s:tuple(combinations((index[p] for p in combinations(s,2) if p in index),2)) for s in COLORS}
    return ports,edge

# Every pair of missing Ports is either incident at one axis or disjoint.
incident=sum(bool(set(a)&set(b)) for a,b in combinations(PAIRS,2))
assert incident==60 and comb(15,2)-incident==45
for a,b in combinations(PAIRS,2):
    _,edge=cut({a,b})
    empty=sum(len(e)==0 for e in edge.values())
    assert empty==(1 if set(a)&set(b) else 0)

# By S6 relabeling, {01,23} represents every disjoint pair.
PORTS,EDGE=cut({(0,1),(2,3)})
F=tuple(s for s in COLORS if len(EDGE[s])==1)
C=tuple(s for s in COLORS if len(EDGE[s])==3)
assert len(PORTS)==13 and len(F)==8 and len(C)==12
assert all(len(EDGE[s]) in (1,3) for s in COLORS)

bit=lambda ab:(1<<ab[0])^(1<<ab[1])
SUFFIX=[set() for _ in range(len(C)+1)]
SUFFIX[-1]={0}
for i in reversed(range(len(C))):
    SUFFIX[i]={x^bit(e) for x in SUFFIX[i+1] for e in EDGE[C[i]]}
assert len(SUFFIX[0])==2**12

FORCED_EDGES=tuple(EDGE[s][0] for s in F)
def connected(edges):
    parent=list(range(len(PORTS)))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]
            i=parent[i]
        return i
    for u,v in edges:
        a,b=root(u),root(v)
        if a!=b:parent[a]=b
    return len({root(i) for i in range(len(PORTS))})==1

def certificate(target):
    """Deterministic complete DFS; parity suffix prunes, connectivity checked at leaves."""
    selected=[]
    def walk(i,rem):
        if i==len(C):
            return rem==0 and connected(selected+list(FORCED_EDGES))
        for e in EDGE[C[i]]:
            if (rem^bit(e)) not in SUFFIX[i+1]:continue
            selected.append(e)
            if walk(i+1,rem^bit(e)):return True
            selected.pop()
        return False
    assert walk(0,target),target
    assert len(selected)==len(C) and connected(selected+list(FORCED_EDGES))
    assert reduce(lambda x,e:x^bit(e),selected,0)==target
    return tuple(selected)

TARGETS=set()
for mask in range(1<<len(F)):
    t=reduce(lambda x,ab:x^bit(ab),(e for i,e in enumerate(FORCED_EDGES) if (mask>>i)&1),0)
    TARGETS.add(t)
assert len(TARGETS)==128
CERT={t:certificate(t) for t in sorted(TARGETS)}

def exact_realization(counts):
    assert set(counts)==set(COLORS) and all(type(n)==int and n>=1 for n in counts.values())
    target=reduce(lambda x,s:x^bit(EDGE[s][0]),(s for s in F if counts[s]&1),0)
    selected=CERT[target]
    events=[]
    for s in F:events.extend([EDGE[s][0]]*counts[s])
    for s,e in zip(C,selected):
        n=counts[s]
        other=[v for v in EDGE[s] if v!=e]
        if n==1:part=[e]
        elif n%2==0:part=other+[EDGE[s][0]]*((n-2)//2)*2
        else:part=[e,other[0],other[0]]+[EDGE[s][0]]*((n-3)//2)*2
        assert len(part)==n
        events.extend(part)
    deg=[0]*len(PORTS)
    for u,v in events:deg[u]+=1;deg[v]+=1
    assert connected(events) and all(d>0 and d%2==0 for d in deg)
    assert len(events)==sum(counts.values())
    return len(events)

for k in range(256):
    counts={s:1+((k+3*i)%9) for i,s in enumerate(COLORS)}
    exact_realization(counts)
for k in range(256):
    order=COLORS[k%20:]+COLORS[:k%20]
    counts={s:(1 if s in order[:5] else 3 if s in order[5:12] else 2) for s in COLORS}
    assert exact_realization(counts)==42

print({'inactive_pair_configurations':105,'incident_pairs_no_go':60,'disjoint_pairs_universal':45,
       'disjoint_representative':'01,23','active_ports':13,'forced_colors':8,'flexible_colors':12,
       'reachable_even_boundaries':len(SUFFIX[0]),'distinct_forced_boundary_targets':len(TARGETS),
       'verified_connected_parity_certificates':len(CERT),
       'exact_regressions':512,
       'labeled_42_each_disjoint_pair':comb(20,5)*comb(15,7),
       'labeled_42_all_disjoint_pairs':45*comb(20,5)*comb(15,7),
       'failures':0})
