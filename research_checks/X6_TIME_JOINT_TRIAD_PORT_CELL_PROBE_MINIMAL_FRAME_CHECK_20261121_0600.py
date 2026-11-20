#!/usr/bin/env python3
"""Exact S6 marked-port and P000 signed-Cell-step observer quotient checks."""
from itertools import permutations
from math import factorial, prod
import json
S6 = list(permutations(range(6)))
IDENT = tuple(range(6))
def multinomial(n, ks):
    assert sum(ks) == n and min(ks) >= 0
    return factorial(n) // prod(factorial(x) for x in ks)
def fall(a, b):
    return factorial(a) // factorial(a-b) if 0 <= b <= a else 0
def expected(r, k):
    s=(r,3-r,3); total=0
    for a in range(k+1):
        for b in range(k-a+1):
            c=k-a-b; t=(a,b,c)
            if any(t[i] > s[i] for i in range(3)): continue
            total += multinomial(k,t)*multinomial(6-k,tuple(s[i]-t[i] for i in range(3)))*prod(fall(s[i],t[i]) for i in range(3))
    return total
def mark(p,r):
    return tuple(sorted((p.index(i),1 if i<r else -1) for i in range(3)))
def sig(p,r,O):
    return (mark(p,r),tuple(p[j] for j in O))
def group(g):
    seen={IDENT}; todo=[IDENT]
    while todo:
        p=todo.pop()
        q=tuple(p[g[i]] for i in range(6))
        if q not in seen:
            seen.add(q);todo.append(q)
    return seen
rows=[];group_rows=[]
for r in range(4):
    for k in range(7):
        O=tuple(range(k))
        n=len({sig(p,r,O) for p in S6})
        assert n==expected(r,k),(r,k,n,expected(r,k))
        rows.append(dict(r=r,k=k,states=n,bits=(n-1).bit_length()))
    bymark={}
    for p in S6:
        m=mark(p,r)
        if m in bymark and bymark[m][0]!=p[0]:break
        bymark.setdefault(m,p)
    else:raise AssertionError("Port-only observer unexpectedly resolves the first Cell probe")
    assert mark(bymark[m],r)==mark(p,r) and bymark[m][0]!=p[0]
generators={"identity":IDENT,"swap01":(1,0,2,3,4,5),"cycle012":(1,2,0,3,4,5),"cycle6":(1,2,3,4,5,0)}
for name,g in generators.items():
    H=group(g); O=tuple(sorted({h[0] for h in H}))
    for r in range(4):
        classes={sig(p,r,O) for p in S6}
        assert len(classes)==expected(r,len(O))
        for h in H:
            transition={}
            for p in S6:
                t=tuple(p[h[i]] for i in range(6))
                before=sig(p,r,O);after=sig(t,r,O)
                assert before not in transition or transition[before]==after
                transition[before]=after
        group_rows.append(dict(group=name,group_size=len(H),orbit=list(O),r=r,states=len(classes),bits=(len(classes)-1).bit_length()))
result={"schema":"X6_TIME_JOINT_PORT_CELL_FRAME_CERT_V1","task_id":"RS-X6-NATIVE-TIME-DYNAMICS","worldview":"P000_V5_SIGNED_NATIVE_CELL_STEP; SELECTIVE_MARKED_PORT_CONDITIONAL","permutations":720,"signature_rows":rows,"subgroup_rows":group_rows,"mismatches":0,"physical_triadic_closure_admitted":False,"original_R063_native_benchmark_executed":False}
print(json.dumps(result,sort_keys=True,separators=(",",":")))
