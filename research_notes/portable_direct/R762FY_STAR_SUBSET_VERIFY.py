#!/usr/bin/env python3
"""R762FY: exact positive-rational BRC branch counts on 15 K4 STAR subsets."""
from itertools import combinations, permutations
from collections import Counter, deque
from fractions import Fraction
import json

V=tuple(range(4)); edges=tuple(combinations(V,2)); E=tuple(range(6))
ID=tuple(E)
def mul(p,q): return tuple(p[q[i]] for i in E)
def cyc(t,positive):
    a,b,c=t; x=list(ID)
    if positive: x[a],x[b],x[c]=b,c,a
    else: x[a],x[b],x[c]=c,a,b
    return tuple(x)
stars=tuple(tuple(i for i,e in enumerate(edges) if v in e) for v in V)
even={p for p in permutations(E) if sum(p[i]>p[j] for i in E for j in range(i+1,6))%2==0}
assert len(even)==360
rows=[]
for n in range(1,5):
 for selected in combinations(V,n):
    branches=[cyc(stars[v],orientation) for v in selected for orientation in (True,False)]
    assert len(set(branches))==2*n and set(branches)<=even
    bfs={ID:0}; queue=deque([ID])
    while queue:
        p=queue.popleft()
        for b in branches:
            y=mul(b,p)
            if y not in bfs:
                bfs[y]=bfs[p]+1;queue.append(y)
    assert set(bfs)<=even
    lengths=dict(sorted(Counter(bfs.values()).items()))
    counts={ID:1}; horizons=[]
    for h in range(1,max(bfs.values())+3):
        nxt=Counter()
        for p,v in counts.items():
            for b in branches: nxt[mul(b,p)]+=v
        counts=nxt
        assert sum(counts.values())==(2*n)**h
        distance=sum((abs(Fraction(counts.get(p,0),(2*n)**h)-Fraction(1,len(bfs))) for p in bfs),Fraction(0,1))/2
        horizons.append(dict(h=h,support=len(counts),min=min(counts.values()),max=max(counts.values()),tv=str(distance)))
    rows.append(dict(subset=selected,n=n,branch_count=2*n,group_size=len(bfs),shortest_length=lengths,diameter=max(bfs.values()),horizons=horizons,globally_fixed_axes=[i for i in E if all(p[i]==i for p in bfs)]))
for n,order in [(1,3),(2,60),(3,360),(4,360)]:
    family=[r for r in rows if r['n']==n]
    assert len(family)==[0,4,6,4,1][n]
    assert all(r['group_size']==order for r in family)
    assert len({(tuple(r['shortest_length'].items()),tuple((h['support'],h['tv']) for h in r['horizons'])) for r in family})==1
for r in rows:
 if r['n']==3:
    assert r['shortest_length']=={0:1,1:6,2:24,3:96,4:187,5:46}
    assert [x['support'] for x in r['horizons'][:5]]==[6,31,127,314,360]
    assert r['horizons'][4]['min']==4 and r['horizons'][4]['max']==159
    assert r['horizons'][4]['tv']=='713/2160'
 if r['n']==4: assert r['horizons'][4]['tv']=='28619/184320'
print(json.dumps(dict(research_id='R762FY',status='PASS',review='NOT_REVIEWED',
   edges=edges,stars=stars,even_group_size=len(even),
   tested_nonempty_subsets=len(rows),subsets=rows),indent=2))
