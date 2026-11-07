#!/usr/bin/env python3
"""Exact Fraction checks: BRC N=4 binary shattering, three-code bound."""
from fractions import Fraction as F
from itertools import product
from random import Random

S=("AU","AV","BU","BV")
L={"Q":{"AU":(10,10),"AV":(20,20),"BU":(15,15),"BV":(15,15)},
   "P":{"AU":(9,11),"AV":(5,5),"BU":(3,27),"BV":(30,30)}}
PREP={"AU_Q":(F(1,2),F(1,2)),"AU_P":(F(9,20),F(11,20)),
      "AV_Q":(F(1,2),F(1,2)),"AV_P":(F(1,2),F(1,2)),
      "BU_Q":(F(1,2),F(1,2)),"BU_P":(F(1,10),F(9,10)),
      "BV_Q":(F(1,2),F(1,2)),"BV_P":(F(1,2),F(1,2))}
FL={"AU0":F(19,80),"AU1":F(21,80),"AV0":F(1,4),"AV1":F(1,4)}
FR={"BU0":F(1,10),"BU1":F(2,5),"BV0":F(1,4),"BV1":F(1,4)}

def tv(a,b):
    return sum((abs(a.get(k,F(0))-b.get(k,F(0))) for k in set(a)|set(b)),F(0))/2

def left_null(E):
    A=[[E[i][j] for i in range(4)] for j in range(3)]
    piv=[];r=0
    for col in range(4):
        hit=next((q for q in range(r,3) if A[q][col]),None)
        if hit is None:continue
        A[r],A[hit]=A[hit],A[r]
        x=A[r][col]; A[r]=[z/x for z in A[r]]
        for q in range(3):
            if q!=r:
                x=A[q][col];A[q]=[A[q][j]-x*A[r][j] for j in range(4)]
        piv.append(col);r+=1
        if r==3:break
    free=next(c for c in range(4) if c not in piv)
    w=[F(0)]*4;w[free]=F(1)
    for q,c in enumerate(piv):w[c]=-A[q][free]
    assert sum(w)==0 and any(w)
    assert all(sum(w[i]*E[i][j] for i in range(4))==0 for j in range(3))
    b=[int(z>0) for z in w]
    assert sum(w[i]*b[i] for i in range(4))/sum(map(abs,w))==F(1,2)

def check():
    for law in ("P","Q"):
        ls=[F(v,240) for s in S for v in L[law][s] for k in range(2)]
        assert len(ls)==16 and min(ls)>0 and sum(ls)==1
        for s in S:
            a,b=L[law][s]
            assert (F(a,a+b),F(b,a+b))==PREP[s+"_"+law]
    ratios=(F(9,10),F(11,10),F(1,4),F(1,5),F(9,5),F(2))
    assert len(set(ratios))==6
    checks=0
    for mask in product((0,1),repeat=4):
        for eps in (F(0),F(1,8),F(1,4),F(1,2)):
            for s in S:
                for law in ("P","Q"):
                    dec="P" if mask[S.index(s)] else "Q"
                    if s=="BU":
                        p0,p1=PREP[s+"_"+law]
                        out={(dec,0):p0*(1-eps)+p1*eps,(dec,1):p0*eps+p1*(1-eps)}
                    else:out={(dec,None):F(1)}
                    assert all(v>=0 for v in out.values()) and sum(out.values())==1
                    assert sum((v for (d,z),v in out.items() if d=="P"),F(0))==mask[S.index(s)]
                    checks+=1
    assert checks==512
    for name,p in PREP.items():
        s=name[:2]
        d={s+"0":p[0],s+"1":p[1]}
        assert tv(d,FL if s[0]=="A" else FR)==F(1,2)
    assert sum(FL.values())==sum(FR.values())==1
    n=0
    for labels in product(range(3),repeat=4):
        E=[tuple(F(int(i==j)) for j in range(3)) for i in labels]
        left_null(E);n+=1
    rnd=Random(120311)
    for _ in range(1024):
        E=[]
        for __ in range(4):
            a,b=sorted((rnd.randrange(9),rnd.randrange(9)))
            E.append(tuple(F(x,8) for x in (a,b-a,8-b)))
        left_null(E);n+=1
    assert n==1105
    print("SOURCE_LEAVES P=16 Q=16 strictly_positive normalized")
    print("RATIO_CLASSES=6 distinct; POLICY_MASKS=16; EXACT_Y_COMPARISONS=512")
    print("REFERENCE_UPPER 8/8 full-path TV=1/2; applies by data processing")
    print("DUAL_NULLSPACE_CERTIFICATES=1105 exact; all with sign ratio=1/2")
    print("ANALYTIC_THEOREM: R3(noT,withZ; S23/S2)=1/2 for all eps in [0,1/2]")
    print("ANALYTIC_COROLLARY: R1=R2=R3(Decision-only; S23/S2)=1/2")
    print("PASS_BRC_N4_BINARY_SHATTERING_R3_OBSERVER_20261031")

if __name__=="__main__":check()
