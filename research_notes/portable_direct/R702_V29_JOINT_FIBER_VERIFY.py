#!/usr/bin/env python3
"""R702 exact BRC/V29 four-/n-ring joint-circulation fiber verification."""
from itertools import product
from math import comb
from collections import Counter
import json

def weak_compositions(total, slots):
    if slots == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in weak_compositions(total - first, slots - 1):
                yield (first,) + tail

def signature(v, w):
    n = len(v)
    omega = tuple(v[i] - w[i] for i in range(n))
    u = tuple(omega[i] - omega[(i-1)%n] for i in range(n))
    return u, sum(v)+sum(w)

def joint_fiber(u,P):
    n=len(u)
    if n<3 or sum(u)!=0 or P<0:
        return 0,[]
    b=[0]
    for i in range(1,n):
        b.append(b[-1]+u[i])
    lo,hi=max(-P-z for z in b),min(P-z for z in b)
    parts=[]
    for k in range(lo,hi+1):
        omega=tuple(z+k for z in b)
        A=sum(abs(z) for z in omega)
        if A>P or (P-A)%2: continue
        Q=(P-A)//2
        parts.append({"circulation":k,"opposite_pairs":Q,"fiber_count":comb(Q+n-1,n-1)})
    return sum(x["fiber_count"] for x in parts),parts

results={}
for n,cap in [(3,7),(4,7),(5,6)]:
    counts=Counter(); total=0
    for P in range(cap+1):
        for arcs in weak_compositions(P,2*n):
            obs=signature(arcs[:n],arcs[n:])
            assert obs[1]==P
            counts[obs]+=1
            total+=1
    assert total==comb(cap+2*n,2*n)
    for (u,P),observed in counts.items():
        exact,parts=joint_fiber(u,P)
        assert observed==exact and parts,(n,u,P,observed,exact)
    results[str(n)]={"max_primitive_PASS_count":cap,"ledgers_checked":total,
                     "distinct_(u,P)_signatures":len(counts),
                     "fiber_checks":len(counts),"max_fiber_size_in_window":max(counts.values())}

for L,want in [(0,1),(1,4),(2,12),(3,28),(4,57),(6,176)]:
    count,ks=joint_fiber((0,0,0,0),2*L)
    formula=comb(L+3,3)+2*sum(comb(L-2*j+3,3) for j in range(1,L//2+1))
    assert count==formula==want
    if L in (0,1,2,6):
        results["zero_contrast_P"+str(2*L)]={"fiber":count,"summands":ks}

u=(1,-1,0,0)
count,terms=joint_fiber(u,3)
assert count==5 and [x["fiber_count"] for x in terms]==[1,4]
results["nonzero_contrast_example"]={"u":u,"P":3,"fiber":count,"summands":terms}
results["status"]="R702_JOINT_FIBER_EXACT_PASS"
print(json.dumps(results,ensure_ascii=False,sort_keys=True,indent=2))
