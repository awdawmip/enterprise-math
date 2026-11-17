#!/usr/bin/env python3
"""Exact integer certificate for PREFIX-877; Python 3.10+, no dependencies.
Checks both algebraic line-count formulas and independent bounded line scans.
"""
import json

P=32
B=19
Q=(1<<B)-1
N=1<<P

def prior_difference_set():
    d={1<<i for i in range(1,B)}
    for i in range(1,B):
        for j in range(1,i):
            d.add((1<<i)+(1<<j))
    for i in range(1,B+1):
        for j in range(1,i):
            d.add((1<<i)-(1<<j))
    return d

D=prior_difference_set()
D3=D|{1<<B,1<<(B+1)}
Epos={1}|{(1<<i)+s for i in range(1,B+1) for s in (-1,1)}
E=Epos|{-v for v in Epos}
assert (len(D),len(D3),len(Epos),len(E))==(307,309,37,74)

def valid(q1,q2):
    return 1<=q1<=Q and 1<=q2<=Q and (q1&1)==1 and (q2&1)==1

def odd_count(lo,hi):
    lo=max(1,lo); hi=min(Q,hi)
    if not lo&1: lo+=1
    return max(0,(hi-lo)//2+1)

def ceildiv(a,b):
    return -((-a)//b)

C_with_diagonal=sum(odd_count(ceildiv(e+1,2),(Q+e)//2) for e in E)
diagonal=sum(1 for e in Epos if e<=Q)
C_total=C_with_diagonal-diagonal

CA=set()
CB=set()
CtB=set()
for e in E:
    for h in D:
        for sign in (-1,1):
            q1=e+sign*h; q2=2*q1-e
            if valid(q1,q2) and q1!=q2:
                CA.add((q1,q2))
    for d in D3:
        q1=d-e; q2=2*q1-e
        if valid(q1,q2) and q1!=q2:
            CB.add((q1,q2))
for f in E:
    for d in D3:
        if (3*f+d)%5: continue
        q2=(3*f+d)//5; q1=2*q2-f
        if valid(q1,q2) and q1!=q2:
            CtB.add((q1,q2))
CAtB={pair for pair in CB if abs(pair[0]-pair[1]) in D}
CtAtB={pair for pair in CtB if abs(pair[0]-pair[1]) in D}
CtA={(q2,q1) for (q1,q2) in CA}

cross=set()
for e in E:
    for f in E:
        if (2*e+f)%3: continue
        q1=(2*e+f)//3; q2=(e+2*f)//3
        if valid(q1,q2) and q1!=q2:
            cross.add((q1,q2))
cross_new={pair for pair in cross
           if abs(pair[0]-pair[1]) not in D
           and 3*pair[0]-pair[1] not in D3}

C_new=C_total-len(CA)-len(CB)+len(CAtB)
Ct_new=C_total-len(CtA)-len(CtB)+len(CtAtB)
new_union=C_new+Ct_new-len(cross_new)

scan_C=scan_C_new=scan_Ct=scan_Ct_new=0
for q1 in range(1,Q+1,2):
    for e in E:
        q2=2*q1-e
        if 1<=q2<=Q and q1!=q2:
            scan_C+=1
            if abs(q1-q2) not in D and (3*q1-q2) not in D3:
                scan_C_new+=1
for q2 in range(1,Q+1,2):
    for f in E:
        q1=2*q2-f
        if 1<=q1<=Q and q1!=q2:
            scan_Ct+=1
            if abs(q1-q2) not in D and (3*q1-q2) not in D3:
                scan_Ct_new+=1
assert (scan_C,scan_C_new,scan_Ct,scan_Ct_new)==(C_total,C_new,C_total,Ct_new)

def events_for_positive(a,b,d):
    assert a-b==d>0
    if d==1:
        return ((0,1),(a,a))
    for i in range(1,B+1):
        z=1<<i
        if d==z+1:
            u=0 if a&z else z
            return ((u,u+1),(u+a,u+a-z))
        if d==z-1:
            t=1
            u=t if (a+t)&z else t+z
            return ((u,u-t),(u+a,u+a-z))
    raise AssertionError('unclassified sparse difference')

def collision(q1,q2):
    e=2*q1-q2
    assert e in E
    if e>0:
        A,C=events_for_positive(2*q1,q2,e)
    else:
        A0,C0=events_for_positive(q2,2*q1,-e)
        A,C=(A0[1],A0[0]),(C0[1],C0[0])
    for x,y in (A,C):
        assert 0<=x<N and 0<=y<N
        v=x^y
        assert v==0 or (v&(v-1))==0
    assert A!=C and (A[0]%q1,A[1]%q2)==(C[0]%q1,C[1]%q2)
    return A,C

witnesses=0
for e in E:
    lo=max(1,ceildiv(e+1,2)); hi=min(Q,(Q+e)//2)
    if lo%2==0: lo+=1
    if lo>hi: continue
    end=hi if hi%2 else hi-1
    mid=lo+2*((end-lo)//4)
    for q1 in {lo,mid,end}:
        q2=2*q1-e
        if valid(q1,q2):
            collision(q1,q2)
            witnesses+=1

results={
 'schema':'PREFIX877_R6_PARITY_LATTICE_EXACT_CERTIFICATE_V1',
 'model':'p=32, B=19, Q=2^19-1, ordered positive odd modulus pairs',
 'frozen_scientific_input':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'D19_count':len(D),'Dstar_count':len(D3),
 'Epositive_count':len(Epos),'Esigned_count':len(E),
 'C_including_diagonal':C_with_diagonal,'diagonal':diagonal,
 'C_non_diagonal':C_total,'Ct_non_diagonal':C_total,
 'C_intersect_near':len(CA),'Ct_intersect_near':len(CtA),
 'C_intersect_3to1':len(CB),'Ct_intersect_3to1':len(CtB),
 'C_intersect_near_and_3to1':len(CAtB),
 'Ct_intersect_near_and_3to1':len(CtAtB),
 'C_intersect_Ct_non_diagonal':len(cross),
 'C_intersect_Ct_outside_prior_union':len(cross_new),
 'C_new_over_prior':C_new,'Ct_new_over_prior':Ct_new,
 'new_union_over_prior':new_union,
 'prior_prefix876_union':163028070,
 'combined_union':163028070+new_union,
 'independent_scan_C':scan_C,'independent_scan_C_new':scan_C_new,
 'independent_scan_Ct':scan_Ct,'independent_scan_Ct_new':scan_Ct_new,
 'witness_representatives_checked':witnesses,
 'status':'ALL_EXACT_ASSERTIONS_PASSED'
}
expected=(9175006,19116,14924,3638,2162,259,920,674,9143128,9152511,18294965,181323035)
observed=(C_total,len(CA),len(CB),len(CtB),len(CAtB),len(CtAtB),len(cross),len(cross_new),C_new,Ct_new,new_union,163028070+new_union)
assert observed==expected,(observed,expected)
print(json.dumps(results,indent=2,ensure_ascii=False,sort_keys=True))
