#!/usr/bin/env python3
"""Exact bounded graph-ball computation, radius 4, around R5 14-arc vertex."""
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from VERIFY_ADJACENCY import C,x
from sympy import Matrix
from itertools import combinations
from collections import Counter
R=C[list(C.T.rref()[1]),:]
assert R.rows==15 and R*x==R*x
b=R*x

def neighbors(y):
    p=[k for k,v in enumerate(y) if v>0]
    z=[k for k,v in enumerate(y) if v==0]
    n=len(p)
    assert n in (14,15) and R[:,p].rank()==n
    if n==15:
        inv=R[:,p].inv()
        jobs=[((k,),(1,),-inv*R[:,k]) for k in z]
    else:
        piv=list(R[:,p].T.rref()[1]); cf={k:R[piv,p].inv()*R[piv,k] for k in z}
        other=next(i for i in range(15) if any(R[i,k]!=(R[i,p]*cf[k])[0] for k in z))
        lam={k:R[other,k]-(R[other,p]*cf[k])[0] for k in z}
        jobs=[((k,),(1,),-cf[k]) for k in z if lam[k]==0]
        for k,l in combinations(z,2):
            if lam[k]<0<lam[l]:
                jobs.append(((k,l),(lam[l],-lam[k]),-cf[k]*lam[l]+cf[l]*lam[k]))
            elif lam[l]<0<lam[k]:
                jobs.append(((l,k),(lam[k],-lam[l]),-cf[l]*lam[k]+cf[k]*lam[l]))
    ans=[]
    for adds, weights, old in jobs:
        d=Matrix.zeros(30,1)
        for k,v in zip(adds,weights):d[k]=v
        for k,v in zip(p,old):d[k]=v
        assert C*d==Matrix.zeros(21,1)
        t=min(y[k]/(-d[k]) for k in p if d[k]<0)
        nxt=y+t*d
        assert min(nxt)>=0 and R*nxt==b
        ans.append(nxt)
    return ans
seen={tuple(x)};layer=[x]
for depth in range(1,5):
    nxt=[]; all_edges=0; supp=Counter()
    for v in layer:
        for w in neighbors(v):
            all_edges+=1
            key=tuple(w)
            if key not in seen:
                seen.add(key);nxt.append(w)
                supp[len([a for a in w if a>0])]+=1
    print('DEPTH',depth,'PARENTS',len(layer),'DIRECTED_EDGE_TESTS',all_edges,
          'NEW_VERTICES',len(nxt),'SUPPORT_COUNTS',dict(sorted(supp.items())),
          'CUMULATIVE_UNIQUE_VERTICES',len(seen))
    layer=nxt
assert len(seen)==1775
print('PASS_EXACT_BFS_RADIUS4_1775')
