#!/usr/bin/env python3
"""Exact-rational six-source BRC S23 checks for the c_AV lower-endpoint phase.
The analytic proof covers real 0<=t<=1/8; this checks 65 rational boxes,
and encloses the single irrational constant by an exact isqrt certificate.
Python 3 standard library only. No floating point arithmetic is used.
"""
from fractions import Fraction as F
from itertools import product
from math import isqrt
import json

M20 = ((10, 10, 0, 0, 0, 0), (9, 11, 0, 0, 0, 0),
       (0, 0, 20, 0, 0, 0), (0, 0, 0, 10, 10, 0),
       (0, 0, 0, 2, 18, 0), (0, 0, 0, 0, 0, 20))

def stop(a,b,c):
    return (a, (1-a)*b, (1-a)*(1-b)*c, (1-a)*(1-b)*(1-c))

def rows(a,b,c):
    src = (stop(a,b,F(1,2)), stop(a,b,F(1,2)),
           stop(a,F(0),c), stop(F(1,4),b,F(1,2)),
           stop(F(1,4),b,F(1,2)), stop(F(1,4),F(1,3),F(1,2)))
    assert all(sum(p)==1 and min(p)>=0 for p in src)
    out = tuple(tuple(sum(F(M20[i][j],20)*src[j][k] for j in range(6))
                      for k in range(4)) for i in range(6))
    assert all(sum(p)==1 and min(p)>=0 for p in out)
    assert out[0]==out[1] and out[3]==out[4]
    return out

def dist(p,q):
    return sum((abs(x-y) for x,y in zip(p,q)),F(0))/2

def risk(t,center):
    high = F(0)
    compared=0
    for a,b,c in product((F(1,2),F(7,8)),(F(1,8),F(1,2)),
                         (F(1,2)-t,F(7,8))):
        observed = rows(a,b,c)
        for i in range(6):
            d=dist(observed[i],center[i]); compared+=1
            high=max(high,d)
    assert compared==48
    return high,compared

PREC=100
floor=isqrt(43*2**(2*PREC))
assert floor**2 <=43*2**(2*PREC)<(floor+1)**2
rlo=(F(floor,2**PREC)-5)/8
rhi=(F(floor+1,2**PREC)-5)/8
poly=lambda r: 32*r*r+40*r-9
assert poly(rlo)<0<poly(rhi)
assert rhi-rlo==F(1,8*2**PREC)
assert F(3,16)<rlo<rhi<F(5,24)

TVALUES=[F(j,512) for j in range(65)]
assert TVALUES[0]==0 and TVALUES[-1]==F(1,8)
comparisons=0; vertex_rows=0; exact_lawful_cases=0
for t in TVALUES:
    rh=F(3,16)+t/6
    weights=(F(4,9)+16*t/27, F(1,18)-4*t/27,
             F(2,9)-16*t/27, F(5,18)+4*t/27)
    assert min(weights)>=0 and sum(weights)==1
    ch=(F(1,4)-t/6)/(F(5,16)+t/6)
    assert F(1,2)-t<=ch<=F(7,8)
    vtx=((F(1,2),F(1,8),ch),(F(1,2),F(1,2),ch),
         (F(7,8),F(1,8),ch),(F(7,8),F(1,2),ch))
    vrows=[rows(*x) for x in vtx]
    H=tuple(tuple(sum(weights[j]*vrows[j][i][k] for j in range(4))
                  for k in range(4)) for i in range(6))
    assert H[0]==(F(11,16)-t/6,F(1,16),F(1,8)+t/12,F(1,8)+t/12)
    assert H[2]==(F(11,16)-t/6,F(0),F(1,4)-t/6,F(1,16)+t/3)
    assert H[3]==(F(1,4),F(3,16),F(9,32),F(9,32))
    hmax,n1=risk(t,H)
    assert hmax==rh, (t,hmax,rh)
    r= rh if poly(rh)>=0 else rhi
    if poly(rh)>=0: exact_lawful_cases+=1
    assert F(3,16)<=r<=F(5,24)
    x=F(7,8)-r; y=F(1,2)-4*r/3
    cl=(F(7,16)-r)/(F(1,8)+r)
    assert F(1,2)<=x<=F(7,8)
    assert F(1,8)<=y<=F(1,2)
    assert F(1,2)-t<=cl<=F(7,8)
    L=rows(x,y,cl)
    lmax,n2=risk(t,L)
    assert lmax==r,(t,lmax,r)
    comparisons+=n1+n2; vertex_rows+=8*6

# Exact rational characterization of the algebraic transition:
# r*=positive root of poly; t*=6*(r*-3/16).
# This bracket is derived with rational arithmetic, not floats.
tcrit_lo=6*(rlo-F(3,16)); tcrit_hi=6*(rhi-F(3,16))
assert 0<tcrit_lo<tcrit_hi<F(1,8)
assert tcrit_hi-tcrit_lo==F(6,8*2**PREC)
print(json.dumps({
    "status":"PASS_BRC_N4_S23_C_LOWER_ENDPOINT_EXACT_PHASE_20261102",
    "scientific_input":"enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34",
    "boxes":len(TVALUES), "vertices_evaluated":len(TVALUES)*8,
    "observation_rows_evaluated":vertex_rows,
    "total_center_row_tv_checks":comparisons,
    "lawful_exact_rational_cases":exact_lawful_cases,
    "lawful_irrational_rational_enclosure_cases":len(TVALUES)-exact_lawful_cases,
    "sqrt43_radius_enclosure_width":str(rhi-rlo),
    "critical_t_enclosure_width":str(tcrit_hi-tcrit_lo),
    "arithmetic":"Fraction/isqrt exact; no floating point",
    "continuous_scope":"by analytic proof in PROOF.md, not by this finite grid"
},ensure_ascii=False,sort_keys=True,indent=2))
