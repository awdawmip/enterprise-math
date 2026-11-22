"""R762IY exact constructive check for the star branch of (10,7,3,0).
No external dependencies; tests every C(10,3)=120 nonstar singleton selection.
The theorem's star-leaf argument is independent of this checker.
"""
from itertools import combinations
from collections import defaultdict, deque

AXES=range(6)
PORTS=list(combinations(AXES,2))
SUPPORTS=list(combinations(AXES,3))
STAR=[s for s in SUPPORTS if 0 in s]
OUTER=[s for s in SUPPORTS if 0 not in s]
J=(0,1,2)
V=(1,2)

def tri_edges(s):
    p=tuple(combinations(s,2))
    return [(p[0],p[1]),(p[0],p[2]),(p[1],p[2])]

def verify(singles):
    original={s:(3 if s in STAR else 1 if s in singles else 2) for s in SUPPORTS}
    m=defaultdict(int)
    def add(a,b,k=1):
        assert a!=b and len(set(a+b))==3 and k>0
        if a>b:a,b=b,a
        m[(a,b)]+=k
    add((0,1),V)
    for s in OUTER:
        e=tri_edges(s)
        if s==(1,2,3):
            add(V,(1,3))
            if original[s]>1:add((1,3),(2,3),original[s]-1)
        elif V in tuple(combinations(s,2)):
            other=[p for p in combinations(s,2) if p!=V]
            add(other[0],other[1],original[s])
        else:
            add(*e[0],original[s])
    # The nine retained star triangles connect PORTS minus V.
    adj=defaultdict(list)
    for s in STAR:
        if s==J:continue
        for a,b in tri_edges(s):
            adj[a].append((b,s));adj[b].append((a,s))
    U=set(PORTS)-{V}
    root=(0,1)
    parent={root:None};support_to_parent={}
    todo=deque([root])
    while todo:
        x=todo.popleft()
        for y,s in adj[x]:
            if y not in parent:
                parent[y]=x;support_to_parent[y]=s;todo.append(y)
    assert set(parent)==U
    parity={p:0 for p in PORTS}
    for (a,b),k in m.items():
        parity[a]^=k%2;parity[b]^=k%2
    assert parity[V]==0 and sum(parity.values())%2==0
    boundary={s:set() for s in STAR if s!=J}
    for p in U:
        if p==root or parity[p]==0:continue
        y=p
        while y!=root:
            x=parent[y];s=support_to_parent[y]
            for z in (x,y):
                if z in boundary[s]:boundary[s].remove(z)
                else:boundary[s].add(z)
            y=x
    for s,ends in boundary.items():
        ps=tuple(combinations(s,2))
        if not ends:
            for a,b in tri_edges(s):add(a,b)
        else:
            assert len(ends)==2 and ends<=set(ps)
            a,b=tuple(ends);c=next(p for p in ps if p not in ends)
            add(a,b);add(a,c,2)
    # Check exact histogram, full active set, all degrees, Euler connectivity.
    counts=defaultdict(int);degrees=defaultdict(int);neighbors=defaultdict(set)
    for (a,b),k in m.items():
        assert k>0
        counts[tuple(sorted(set(a+b)))]+=k
        degrees[a]+=k;degrees[b]+=k
        neighbors[a].add(b);neighbors[b].add(a)
    expected=dict(original);expected[J]=1
    assert counts==expected
    assert set(degrees)==set(PORTS)
    assert all(x>0 and x%2==0 for x in degrees.values())
    seen={root};queue=[root]
    for x in queue:
        for y in neighbors[x]:
            if y not in seen:seen.add(y);queue.append(y)
    assert seen==set(PORTS)
    return sum(counts.values()),len(m),max(degrees.values())

results=[verify(set(s)) for s in combinations(OUTER,3)]
assert len(results)==120 and all(t[0]==45 for t in results)
print("PASS R762IY: 120/120 classes, 45 events, all 15 Ports positive-even and connected")
print("distinct used edges min/max:",min(t[1] for t in results),max(t[1] for t in results))
print("maximum Port degree:",max(t[2] for t in results))
