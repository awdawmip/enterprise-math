#!/usr/bin/env python3
"""Exact rational scan for Stage172 dual-only candidate.
Requires only Python standard-library fractions and functools.
"""
from fractions import Fraction as F
from functools import lru_cache
N=14
P=(F(1,8),F(1,24),F(5,6))
K0,L0=F(378837,1529),F(1128472,4587)
dK,dL=F(-1),-F(10592,12501)
R,U=(10,0,1),(12,4,3)
A=('P','Q','C')
def ratio(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return(s[0]+1,s[1]+(i==0),s[2]+(i==1))
@lru_cache(None)
def pair(s):
    vals=[(K0*ratio(s),dK*ratio(s)),(L0,dL)]
    if s[0]<N:
        ch=[pair(child(s,i)) for i in range(3)]
        vals.append((1+sum((P[i]*ch[i][0] for i in range(3)),F(0)),
                     sum((P[i]*ch[i][1] for i in range(3)),F(0))))
    low=min(a for a,b in vals)
    wins=tuple(a for a,v in zip(A,vals) if v[0]==low)
    choose='Q' if s==R or s==U else wins[0]
    assert choose in wins,(s,wins)
    return *vals[A.index(choose)],dict(zip(A,vals)),choose,wins
candidate=[];old_ties=[]
for n in range(N+1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b);v,d,opts,chosen,w=pair(s)
            for act,(v2,d2) in opts.items():
                if act==chosen:continue
                gap,dgap=v2-v,d2-d
                assert gap>=0
                if gap==0:
                    old_ties.append((s,act,dgap))
                    assert (s==R and act=='C' and dgap==0) or (s==U and act=='C' and dgap>0)
                elif dgap<0:
                    candidate.append((-gap/dgap,s,act,gap,dgap))
candidate.sort()
assert len(candidate)==810 and len(old_ties)==2
step=candidate[0][0]
assert step==F(86081055229118646,15486841263522695)
closures=[x for x in candidate if x[0]==step]
assert len(closures)==1 and closures[0][1:3]==((5,4,1),'P')
K,L=K0+dK*step,L0+dL*step
assert K==F(2453276570264541,10128738563455)
assert L==F(7332367848199016,30386215690365)
@lru_cache(None)
def bell(s):
    opts=[K*ratio(s),L]
    if s[0]<N:
        opts.append(1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0)))
    m=min(opts)
    return m,tuple(a for a,v in zip(A,opts) if v==m),opts
ties={};gaps=[]
for n in range(N+1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b);v,w,opts=bell(s)
            if len(w)>1:ties[s]=w
            gaps.extend(x-v for x in opts if x>v)
assert ties=={(5,4,1):('P','C'),R:('Q','C')},ties
assert len(gaps)==1238
assert min(gaps)==F(3442966771823,273475941213285)
assert bell((0,0,0))[0]==F(7500321462434479703133415412645,41614318285465632307238928384)
print('STAGE172_DUAL_ONLY_EXACT_PASS')
print('step',step,'K',K,'L',L,'root',bell((0,0,0))[0])
print('tie states',ties,'strict gaps',len(gaps),'minimum',min(gaps))
print('first closure',closures)
