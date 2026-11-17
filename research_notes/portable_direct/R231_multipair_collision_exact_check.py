#!/usr/bin/env python3
"""R231 exact rational spectral-collision certificate (stdlib only).

Finite check of 63 proper killed-source blocks for a 7-source sticky-reset
chain. This verifies exact polynomial gcds, not native BRC dynamics.
"""
from fractions import Fraction as F
from itertools import combinations
import json

alpha = tuple(F(p, q) for p, q in [(1,5),(1,4),(3,4),(3,10),(7,10),(7,20),(13,20)])
pi = tuple(F(w,96) for w in (36,5,15,6,14,7,13))
assert sum(pi) == 1 and all(0 < t < 1 for t in alpha) and all(t > 0 for t in pi)
beta = tuple((1-a)*p for a,p in zip(alpha,pi))
zero=F(0); one=F(1)

def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]: a.pop()
    return a

def add(a,b):
    c=[zero]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return trim(c)

def mul(a,b):
    c=[zero]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return trim(c)

def monic(a):
    a=trim(a)
    return [v/a[-1] for v in a] if a != [zero] else [zero]

def remainder(a,b):
    a=trim(a)
    b=trim(b)
    assert b != [zero]
    while a!=[zero] and len(a)>=len(b):
        c=a[-1]/b[-1]
        i=len(a)-len(b)
        for j,v in enumerate(b):a[i+j]-=c*v
        a=trim(a)
    return a

def gcd(a,b):
    while b!=[zero]: a,b=b,remainder(a,b)
    return monic(a)

def poly_product(indices):
    z=[one]
    for j in indices: z=mul(z,[-alpha[j],one])
    return z

def killed_poly(mask):
    D=[0]+[j for j in range(1,7) if mask>>(j-1)&1]
    p=poly_product(D)
    for j in D:
        minus=[-beta[j]*v for v in poly_product([q for q in D if q!=j])]
        p=add(p,minus)
    return monic(p)

polys={mask:killed_poly(mask) for mask in range(63)}
assert len(polys)==63
assert polys[0]==[-F(1,2),one]
assert sum(len(p)-1 for p in polys.values())+1==250
root_masks={0,3,12,15,48,51,60}
assert all(sum(v*F(1,2)**i for i,v in enumerate(poly))==0 for m,poly in polys.items() if m in root_masks)
assert all(sum(v*F(1,2)**i for i,v in enumerate(poly))!=0 for m,poly in polys.items() if m not in root_masks)
assert all(gcd(p,[F(i)*v for i,v in enumerate(p)][1:])==[one] for p in polys.values())
assert all(sum(p)!=0 for p in polys.values())

pairs=[]
for m,n in combinations(range(63),2):
    q=gcd(polys[m],polys[n])
    if len(q)>1:
        assert q==[-F(1,2),one], (m,n,q)
        pairs.append((m,n))
assert len(pairs)==21
assert all(m in root_masks and n in root_masks for m,n in pairs)
rank=1+sum(len(p)-1 for p in polys.values())-(len(root_masks)-1)
assert rank==244

lam=F(1,2)
assert beta[0]/(lam-alpha[0])==1
for j,h in ((1,2),(3,4),(5,6)):
    assert beta[j]/(lam-alpha[j])+beta[h]/(lam-alpha[h])==0
out={"schema":"R231_EXACT_CERTIFICATE_V1","status":"PASS","k":6,
"source_count":7,"proper_blocks":63,"generic_degree_upper":250,
"observed_minimal_recurrence_order":rank,
"shared_rational_mode":"1/2","blocks_with_shared_mode":sorted(root_masks),
"nontrivial_pairwise_gcd_count":len(pairs),"all_nontrivial_gcds":"x-1/2",
"pairwise_gcd_checks":1953,"squarefree_block_checks":63,
"full_block_observer":"eigenvalue 1 only","arithmetic":"exact fractions.Fraction",
"native_BRC_integration":"NOT_EXECUTED","independent_review":"NOT_REVIEWED"}
print(json.dumps(out,indent=2,ensure_ascii=False))
