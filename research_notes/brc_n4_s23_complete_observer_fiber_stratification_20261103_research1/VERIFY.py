#!/usr/bin/env python3
"""Exact 32-stratum BRC S23 fiber certificate. Run: python VERIFY.py > RUN_EVIDENCE.json."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json
A=(0,0,0,1,1,1)
B=(2,2,3,2,2,4)
C=(5,6,7,8,9,10)
M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
   (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
def R(a,b,c):
    return (a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c))
def raw(z):
    return tuple(R(z[A[i]],z[B[i]],z[C[i]]) for i in range(6))
def obs(z):
    rr=raw(z)
    return tuple(tuple(sum((F(M[i][j],20)*rr[j][k] for j in range(6)),F(0))
                 for k in range(4)) for i in range(6))
def inverse(p):
    def L(u,i,v,j,d=1):return tuple((u*p[i][k]-v*p[j][k])/d for k in range(4))
    return (L(11,0,10,1),L(10,1,9,0),p[2],L(9,3,5,4,4),L(5,4,1,3,4),p[5])
def free_indices(z):
    a0,a1=z[0]==1,z[1]==1
    free=[]
    if a0 and a1:free.append(2)
    if a0:free.append(3)
    if a1:free.append(4)
    for i in range(6):
        if z[A[i]]==1 or z[B[i]]==1:free.append(C[i])
    return tuple(sorted(free))
def dim(flags):
    a,b,c,d,e=flags
    return (int(a and b)+int(a)+int(b)+2*int(a or c)+int(a or d)
            +2*int(b or c)+int(b or e))
def point(flags):
    a,b,c,d,e=flags
    return (F(1) if a else F(2,5),F(1) if b else F(3,5),
            F(1) if c else F(1,4),F(1) if d else F(2,5),
            F(1) if e else F(3,5),*(F(k,7) for k in range(1,7)))
def check():
    counts=Counter()
    corners=0
    tests=0
    signatures=[]
    for f in product((False,True),repeat=5):
        z=point(f);p=obs(z);rr=raw(z);free=free_indices(z)
        assert inverse(p)==rr
        assert len(free)==dim(f)
        counts[len(free)]+=1
        for vv in product((F(0),F(1)),repeat=len(free)):
            q=list(z)
            for j,v in zip(free,vv):q[j]=v
            assert obs(q)==p and inverse(obs(q))==rr
            corners+=1
        q=list(z)
        for j in free:q[j]=F(j+1,20)
        assert obs(q)==p
        for j in range(11):
            if j not in free:
                q=list(z)
                q[j]=F(1,2) if z[j]==1 else (F(1) if z[j]<F(1,2) else F(0))
                assert q[j]!=z[j] and obs(q)!=p
                tests+=1
        signatures.append({"flags":"".join("1" if x else "0" for x in f),
                           "free_coordinates":list(free),"dimension":len(free)})
    assert dict(counts)=={0:1,1:2,2:1,4:5,5:6,6:5,7:4,9:8}
    assert corners==5209 and tests==168
    return {
        "marker":"PASS_BRC_S23_COMPLETE_ELEVEN_PARAMETER_OBSERVER_FIBER_STRATIFICATION_20261103",
        "frozen_scientific_pin":"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
        "source_model":"six labeled preparations, four outcomes, invertible mixing M/20",
        "mixing_determinant":"1/50",
        "flags_order":"z0==1,z1==1,z2==1,z3==1,z4==1",
        "pattern_count":32,
        "dimensions_and_signature_counts":{str(k):counts[k] for k in sorted(counts)},
        "possible_fiber_dimensions":sorted(counts),
        "dimensions_three_and_eight_absent":True,
        "all_fiber_corner_comparisons":corners,
        "interior_fiber_checks":32,
        "exact_inverse_cases":32,
        "fixed_coordinate_discriminating_tests":tests,
        "arithmetic":"Python Fraction exact rationals, no approximate comparisons",
        "verification_scope":"32 upstream-degeneracy signatures; all box corners; inverse; one-coordinate discrimination",
        "real_parameter_proof":"Symbolic triangular inverse and zero-factor classification in PROOF.md",
        "patterns":signatures
    }
if __name__=="__main__":
    print(json.dumps(check(),indent=2,ensure_ascii=False))
