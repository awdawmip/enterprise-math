"""R762IY two-leaf star-minus-one constructive Port–Euler check.
Standard library only. Two J/L incidence types x both active choices x C(11,2)=55.
"""
from itertools import combinations
from collections import defaultdict, deque
P=list(combinations(range(6),2))
S=list(combinations(range(6),3))
STAR=[s for s in S if 0 in s]
OUTER=[s for s in S if 0 not in s]
L=(0,1,2)

def edges(s):
    a,b,c=tuple(combinations(s,2))
    return ((a,b),(a,c),(b,c))

def leaf(s):return tuple(x for x in s if x!=0)

def verify(J,singles,leaf_L_active):
    T=set(STAR)-{L}; assert J in T and len(singles)==2
    counts0={s:(3 if s in T else 1 if s in singles else 2) for s in S}
    vL=leaf(L);vJ=leaf(J)
    inactive=set() if leaf_L_active else {vL}
    V=set(P)-inactive
    mult=defaultdict(int)
    def add(a,b,m=1):
        assert m>=1 and a!=b and not ({a,b}&inactive) and len(set(a+b))==3
        if a>b:a,b=b,a
        mult[(a,b)]+=m
    # Attach required leaves with J and L; leave an inactive vL unused.
    add(vJ,(0,J[1]))
    if leaf_L_active:
        add(vL,(0,L[1]))
        if counts0[L]>1:add((0,L[1]),(0,L[2]),counts0[L]-1)
    else:add((0,L[1]),(0,L[2]),counts0[L])
    # Each active leaf has an independent private positive outer support.
    chosen={}
    for v in ((vJ,vL) if leaf_L_active else (vJ,)):
        other=vL if v==vJ else vJ
        eligible=[s for s in OUTER
                  if v in combinations(s,2) and other not in combinations(s,2)]
        assert eligible
        chosen[v]=eligible[0]
    assert len(set(chosen.values()))==len(chosen)
    for s in OUTER:
        if s in chosen.values():continue
        a,b=next((a,b) for a,b in edges(s) if a not in inactive and b not in inactive)
        add(a,b,counts0[s])
    for v,s in chosen.items():
        parity=sum(m for (a,b),m in mult.items() if a==v or b==v)%2
        other=[p for p in combinations(s,2) if p!=v]
        if parity:
            add(v,other[0])
            if counts0[s]>1:add(other[0],other[1],counts0[s]-1)
        else:add(other[0],other[1],counts0[s])
    assert all(sum(m for (a,b),m in mult.items() if v in (a,b))%2==0
               for v in (vJ,vL) if v not in inactive)
    # Retained full-star triangle graph connects W (13 ports).
    W=set(P)-{vJ,vL}
    full=T-{J}
    adjacency=defaultdict(list)
    for s in full:
        for a,b in edges(s):
            adjacency[a].append((b,s));adjacency[b].append((a,s))
    root=(0,1)
    parent={root:None};via={};todo=deque([root])
    while todo:
        x=todo.popleft()
        for y,s in adjacency[x]:
            if y not in parent:
                parent[y]=x;via[y]=s;todo.append(y)
    assert set(parent)==W
    odd={p:0 for p in P}
    for (a,b),m in mult.items():odd[a]^=m%2;odd[b]^=m%2
    assert odd[vJ]==odd[vL]==0 and sum(odd.values())%2==0
    changes={s:set() for s in full}
    for p in W:
        if p==root or odd[p]==0:continue
        x=p
        while x!=root:
            y=parent[x];s=via[x]
            for z in (x,y):
                if z in changes[s]:changes[s].remove(z)
                else:changes[s].add(z)
            x=y
    for s,boundary in changes.items():
        if not boundary:
            for a,b in edges(s):add(a,b)
        else:
            assert len(boundary)==2
            a,b=tuple(boundary)
            c=next(p for p in combinations(s,2) if p not in boundary)
            add(a,b);add(a,c,2)
    # Verify exact support multiset, V, parity and connectivity independently.
    tally=defaultdict(int);deg=defaultdict(int);neighbors=defaultdict(set)
    for (a,b),m in mult.items():
        tally[tuple(sorted(set(a+b)))]+=m
        deg[a]+=m;deg[b]+=m
        neighbors[a].add(b);neighbors[b].add(a)
    expected=dict(counts0);expected[J]=1
    assert tally==expected
    assert set(deg)==V and all(x>0 and x%2==0 for x in deg.values())
    visited={root};q=[root]
    for x in q:
        for y in neighbors[x]:
            if y not in visited:visited.add(y);q.append(y)
    assert visited==V and sum(tally.values())==45
    return len(mult)

results=[]
for J in ((0,1,3),(0,3,4)):  # J and L adjacent/disjoint on K5
    for pair in combinations(OUTER+[L],2):
        for leaf_active in (False,True):
            results.append(verify(J,set(pair),leaf_active))
assert len(results)==220
print("PASS R762IY-2: 220/220 full histogram, parity, V and connectivity checks")
print("distinct used edge types min/max:",min(results),max(results))
