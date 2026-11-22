"""R762IZ: exact constructive certificate and 9-triangle all-essential census.
Composite six-axis Port-Euler observer; Python stdlib only.
"""
from itertools import combinations, permutations
from collections import defaultdict, deque
import hashlib, json

AXES=tuple(range(6))
PORTS=list(combinations(AXES,2))
SUPPORTS=list(combinations(AXES,3))
INDEX={p:i for i,p in enumerate(PORTS)}
T=set(s for s in SUPPORTS if 5 in s)-{(0,1,5),(1,2,5)} | {(0,1,2)}
J=(0,1,2)
LEAVES={(0,1),(1,2)}
RETAINED=T-{J}
W=set(PORTS)-LEAVES
Q={(0,1):(0,1,3),(1,2):(1,2,3)}

def triangle(s):
    p=list(combinations(s,2))
    return ((p[0],p[1]),(p[0],p[2]),(p[1],p[2]))

def components(subset):
    parent=list(range(15))
    def find(x):
        while parent[x]!=x:x=parent[x]
        return x
    for s in subset:
        a,b,c=(INDEX[p] for p in combinations(s,2))
        root=find(a)
        parent[find(b)]=root
        parent[find(c)]=root
    return len({find(i) for i in range(15)})

def all_essential(subset):
    old=components(subset)
    return all(components(subset-{s})>old for s in subset)

def orbit(subset):
    return {tuple(sorted(tuple(sorted(pi[a] for a in s)) for s in subset)) for pi in permutations(AXES)}

def construct(singles):
    counts={s:(3 if s in T else 1 if s in singles else 2) for s in SUPPORTS}
    x=defaultdict(int)
    def add(s,a,b,n=1):
        assert n>=0
        assert a!=b and a in combinations(s,2) and b in combinations(s,2)
        if n:x[(s,tuple(sorted((a,b))))]+=n
    # One J bridge, then two private nontriple supports attach both leaf Ports.
    add(J,(0,1),(1,2))
    add(Q[(0,1)],(0,1),(0,3))
    add(Q[(0,1)],(0,3),(1,3),counts[Q[(0,1)]]-1)
    add(Q[(1,2)],(1,2),(2,3))
    add(Q[(1,2)],(1,3),(2,3),counts[Q[(1,2)]]-1)
    for s in SUPPORTS:
        if s in RETAINED or s==J or s in Q.values():continue
        a,b=next((a,b) for a,b in triangle(s) if a in W and b in W)
        add(s,a,b,counts[s])
    parity={p:0 for p in PORTS}
    for (_, (a,b)),n in x.items():
        parity[a]^=n&1; parity[b]^=n&1
    assert parity[(0,1)]==parity[(1,2)]==0
    assert sum(parity.values())%2==0
    # The eight retained full-star triangles connect all thirteen core Ports.
    graph=defaultdict(list)
    for s in RETAINED:
        for a,b in triangle(s):
            graph[a].append((b,s));graph[b].append((a,s))
    root=(0,5)
    parent={root:None};via={};todo=deque([root])
    while todo:
        a=todo.popleft()
        for b,s in graph[a]:
            if b not in parent:
                parent[b]=a;via[b]=s;todo.append(b)
    assert set(parent)==W
    # Route all remaining odd-degree defects inside the connected core.
    boundary={s:set() for s in RETAINED}
    for p in W:
        if p==root or not parity[p]:continue
        cur=p
        while cur!=root:
            prev=parent[cur];s=via[cur]
            for v in (cur,prev):
                if v in boundary[s]:boundary[s].remove(v)
                else:boundary[s].add(v)
            cur=prev
    for s,b in boundary.items():
        if not b:
            for a,c in triangle(s):add(s,a,c)
        else:
            assert len(b)==2
            a,c=sorted(b)
            third=next(p for p in combinations(s,2) if p not in b)
            add(s,a,c);add(s,a,third,2)
    support_counts=defaultdict(int);degree=defaultdict(int);adj=defaultdict(set)
    for (s,(a,b)),n in x.items():
        support_counts[s]+=n
        degree[a]+=n;degree[b]+=n
        adj[a].add(b);adj[b].add(a)
    expected=dict(counts);expected[J]=1
    assert dict(support_counts)==expected
    assert set(degree)==set(PORTS)
    assert all(degree[p]>0 and degree[p]%2==0 for p in PORTS)
    seen={(0,5)};queue=[(0,5)]
    for p in queue:
        for q in adj[p]:
            if q not in seen:seen.add(q);queue.append(q)
    assert seen==set(PORTS)
    assert sum(support_counts.values())==45
    return sorted(((SUPPORTS.index(s),INDEX[a],INDEX[b],n) for (s,(a,b)),n in x.items()))

if __name__=='__main__':
    assert len(T)==9 and all_essential(T)
    essential={frozenset(family) for family in (set(c) for c in combinations(SUPPORTS,9)) if all_essential(family)}
    bridge_orbit={frozenset(t) for t in orbit(T)}
    star_minus_one=set(s for s in SUPPORTS if 5 in s)-{(0,1,5)}
    star_orbit={frozenset(t) for t in orbit(star_minus_one)}
    assert len(essential)==240
    assert len(bridge_orbit)==180 and len(star_orbit)==60
    assert essential==bridge_orbit|star_orbit
    assert not bridge_orbit&star_orbit
    assert set.union(*(set(combinations(s,2)) for s in T))==set(PORTS)
    nons=[s for s in SUPPORTS if s not in T]
    certificates=[construct(set(singles)) for singles in combinations(nons,2)]
    assert len(certificates)==55
    blob=json.dumps(certificates,separators=(',',':'),ensure_ascii=True).encode()
    print('PASS R762IZ all-essential9=240; bridge-orbit=180; star-minus-one-orbit=60')
    print('PASS R762IZ 55/55 exact connected Euler witnesses of length 45')
    print('symmetry coverage 180*55=',len(bridge_orbit)*len(certificates))
    print('canonical-certificates-sha256',hashlib.sha256(blob).hexdigest())
