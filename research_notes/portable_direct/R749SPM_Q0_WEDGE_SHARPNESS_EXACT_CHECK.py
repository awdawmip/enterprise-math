#!/usr/bin/env python3
"""R749SPM: exact rational witness audit for R749SPK q0 risk sharpness.

Grid check is a reproducibility audit; universal theorem is proved algebraically
using the four explicit case-wise probability laws in the accompanying note.
"""
from fractions import Fraction as F
import json

MASKS=(3,12,15,1,2,4,8)
W=tuple(tuple((-1 if (k&m).bit_count()%2 else 1) for m in MASKS) for k in range(16))
def law(t,s,h=0,u=0,v=0,w=0,z=0):
    return tuple((1+sum(a*b for a,b in zip(row,(t,s,h,u,v,w,z))))/16 for row in W)
def tv(p,q):return sum(map(abs,(a-b for a,b in zip(p,q))),F(0))/2

def witness(t,s):
    assert 0<=t<=s and t+s<=1
    if s<2*t:
        return 'LOWER_FACE',law(t,s,1+t-s),(1+t-s)/2,(2*t-s)/2
    assert s+3*t>1
    if t+s==1:
        return 'TOP_EDGE',law(t,s,0,t,t,s,s),(2*s+t)/4,t/4
    if s<=1-2*t:
        return 'UPPER_INNER',law(t,s,-t,0,0,1-t,t+s),(1+s+t)/4,(s+3*t-1)/4
    return 'UPPER_OUTER',law(t,s,t+s-1,0,0,1-t,1-t),(3-3*t-s)/4,(1-t-s)/4

def run(N=40):
    checks=0; classes={};bad=[];max_abs_err=F(0)
    for i in range(N+1):
        for j in range(i,N-i+1):
            t,s=F(i,N),F(j,N)
            inside = s>=2*t and s+3*t<=1
            if inside:continue
            label,p,expected_risk,excess=witness(t,s)
            q=law(t,s)
            assert min(p)>=0 and sum(p)==1 and min(q)>=0 and sum(q)==1
            risk=tv(p,q)
            err=abs(risk-expected_risk);max_abs_err=max(max_abs_err,err)
            if risk!=(1-t)/2+excess or excess<=0:
                bad.append((t,s,label,risk,expected_risk,excess))
            classes[label]=classes.get(label,0)+1;checks+=1
    assert not bad and checks==sum(classes.values())
    print(json.dumps({
        'status':'PASS',
        'scope':'Exact rational sample grid audit; universal theorem proved algebraically in accompanying note',
        'sample_grid_denominator':N,'outside_T_observed':checks,'witness_classes':classes,
        'full_atom_nonnegative_and_normalized':True,'maximum_formula_error':str(max_abs_err),
        'exact_witness_excess_strict_positive':True,
        'universal_theorem':'q0 risk <=(1-t)/2 iff s>=2t and s+3t<=1 in 0<=t<=s,t+s<=1',
        'scientific_status':'AUTHOR_EXACT_NOT_REVIEWED'
    },indent=2,sort_keys=True))
if __name__=='__main__':run()
