#!/usr/bin/env python3
"""Exact rational verification of arbitrary-m shared-gate support formula."""
from fractions import Fraction as F
from itertools import product
from random import Random

def pos(x):
    return max(F(0),x)

def closed_form(w,a,u):
    M=[max(F(0),x,x+y) for x,y in zip(a,u)]
    H=sum((z*v for z,v in zip(w,M)),F(0))
    L0=sum((z*pos(x) for z,x in zip(w,a)),F(0))
    L1=sum((z*pos(x+y) for z,x,y in zip(w,a,u)),F(0))
    d0,d1=H-L0,H-L1
    assert d0>=0 and d1>=0 and H-max(L0,L1)==min(d0,d1)
    return H,max(L0,L1),d0,d1

def brute(w,a,u):
    m=len(w)
    hf=max(sum((w[i]*(a[i]+(u[i] if q==2 else 0)) if q else F(0)
                for i,q in enumerate(opts)),F(0))
           for opts in product((0,1,2),repeat=m))
    hl=max(sum((w[i]*(a[i]+z*u[i]) if k else F(0)
                for i,k in enumerate(opts)),F(0))
           for z in (0,1) for opts in product((0,1),repeat=m))
    return hf,hl

rng=Random(20261105)
tests=0
for m in range(1,6):
    for _ in range(48):
        w=[F(rng.randint(1,7),rng.randint(1,8)) for _ in range(m)]
        a=[F(rng.randint(-9,9),rng.randint(1,12)) for _ in range(m)]
        u=[F(rng.randint(-9,9),rng.randint(1,12)) for _ in range(m)]
        assert closed_form(w,a,u)[:2]==brute(w,a,u)
        tests+=1

w=[F(1,2),F(1,2)]
a=[F(1,200),-F(47,400)]
u=[-F(9,500),F(49,400)]
hf,hl,d0,d1=closed_form(w,a,u)
assert (hf,hl,d0,d1)==(F(1,200),F(1,400),F(1,400),F(1,400))
assert brute(w,a,u)==(hf,hl)
base=-F(43,40)
assert base+hf==-F(107,100) and base+hl==-F(429,400)
n=[-F(1),-F(1),-F(3,25),F(1,50)]
wh=[F(1141,3600),F(31,72),F(129,40),F(129,40)]
assert sum((x*y for x,y in zip(n,wh)),F(0))==base+hf
norm=sum((abs(x) for x in n),F(0))
assert norm==F(107,50) and (hf-hl)/norm==F(1,856)
assert a[0]>0>a[0]+u[0] and a[1]<0<a[1]+u[1]
assert a[0]==a[1]+u[1]==F(1,200)
print("TESTED_EXACT_REDUCED_MODELS",tests)
print("S_LOCAL_ENDPOINT_REGRETS",d0,d1)
print("S_SUPPORT_FULL",base+hf)
print("S_SUPPORT_SEEDLESS",base+hl)
print("S_SUPPORT_GAP",hf-hl)
print("S_LINF_HULL_DISTANCE_LOWER_BOUND",(hf-hl)/norm)
print("PASS_EXACT_R5_SHARED_GATE_DEFECT_N_HISTORY")
