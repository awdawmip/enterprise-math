#!/usr/bin/env python3
"""R322 independent integer certificate: original M_s recursion, s=0..192."""
import json
from math import comb,factorial
MAX_S=192
P10_DEN=1048576
P10_NUM=[59049,-1476225,-17452260,1134666630,-17876052243,105293849535,500912600310,-13511047863780,105842210675544,-414136077320160,691268379379200]
D10_DEN=524288
D10_NUM=[295245,-7971615,-39694050,4147463250,-65930377275,417673308465,276315645600,-21096639526500,126789710687280,-266932963987200]
Q10_DEN=152202903552
Q10_NUM=[390625,-9765625,126937500,-997406250,4369693125,-13510205625,36487366310,14180963260,21073172760,-511748665056,-691481774592]
SHIFT=[390625,29296875,1005843750,20876343750,289976255625,2801680756875,18846923022560,85552644990660,244575209356560,386762812758144,254338037710848]
def C(n,k):return comb(n,k) if 0<=k<=n else 0
def n(i):return [0,-C(3,i-1),-C(6,i-1),C(8,i-2)]
def delta(i):return [0,-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)]
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:out[i+j]+=x*y
    return out
def add(dest,src,sign):
    if len(dest)<len(src):dest.extend([0]*(len(src)-len(dest)))
    for i,x in enumerate(src):dest[i]+=sign*x
def pow1mz(k):return [(-1)**i*C(k,i) for i in range(k+1)]
def horner(p,x):
    out=0
    for c in p:out=out*x+c
    return out
def moment(p,r):
    if r==0:return sum(p)
    return sum(p[j]*factorial(j)//factorial(j-r) for j in range(r,len(p)))
M=[[1]]
counts={"degree":1,"P10_moment":0,"D10_difference":0,"direct_q10":0,"factorial_recovery":0,"shift_identity":0,"strict_lower_bound":0}
samples={}
old=None
for s in range(1,MAX_S+1):
    cur=mul(n(s),pow1mz(s))
    for i in range(1,min(s,12)+1):
        term=mul(mul(delta(i),M[s-i]),pow1mz(i-1))
        add(cur,term,-1)
    while len(cur)>1 and cur[-1]==0:cur.pop()
    assert len(cur)-1<=2*s+1
    counts["degree"]+=1
    M.append(cur)
    if s<10:continue
    m=moment(cur,10)
    assert m*P10_DEN==(1<<s)*horner(P10_NUM,s)
    counts["P10_moment"]+=1
    if s>=11:
        assert (m-2*old)*D10_DEN==(1<<s)*horner(D10_NUM,s)
        counts["D10_difference"]+=1
    old=m
    a=sum(p*C(2*s+1-j,10) for j,p in enumerate(cur))
    assert a*Q10_DEN==(1<<s)*horner(Q10_NUM,s)
    counts["direct_q10"]+=1
    moms=[moment(cur,r) for r in range(11)]
    numer=sum((-1)**r*C(2*s+1-r,10-r)*moms[r]*(factorial(10)//factorial(r)) for r in range(11))
    assert numer==factorial(10)*a
    counts["factorial_recovery"]+=1
    assert horner(Q10_NUM,s)==horner(SHIFT,s-10)
    counts["shift_identity"]+=1
    assert a*1024>=1711151*(1<<s)
    if s>10:assert a*1024>1711151*(1<<s)
    counts["strict_lower_bound"]+=1
    if s in (10,11,12,13):samples[str(s)]=str(a)
print(json.dumps({"schema":"R322_EXACT_INTEGER_CHECK_V1","result":"PASS","original_recurrence":"R321 M_s with n_i,delta_i,integer polynomial coefficients","finite_domain":"s=0..192; q=10 tested s=10..192","arithmetic":"Python arbitrary precision integers; no floating point","counts":counts,"samples":samples,"symbolic_induction_required":True,"claim_boundary":"Finite verification is independent of infinite-index algebraic induction, not a universal proof"},ensure_ascii=False,indent=2))
