#!/usr/bin/env python3
"""Exact one-sided dual-ray scan Stage137 -> Stage138 candidate (not primal)."""
from fractions import Fraction as F

N=14
P=(F(1,8),F(1,24),F(5,6))
K=F(214326,401); L=F(203912,401)
dK=F(-1);dL=F(-112,129)
B=(11,0,1);G=(13,6,4)

def states(n):
    return ((n,a,b) for a in range(n+1) for b in range(n-a+1))
def children(s):
    n,a,b=s
    return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))

H={};directional={};closures=[];ties=[]
for n in range(N,-1,-1):
    for s in states(n):
        n,a,b=s
        r=F(2**(a+b),3**a)
        v={'P':K*r,'Q':L}
        dv={'P':dK*r,'Q':dL}
        if n<N:
            v['C']=1+sum((P[i]*H[c] for i,c in enumerate(children(s))),F(0))
            dv['C']=sum((P[i]*directional[c] for i,c in enumerate(children(s))),F(0))
        m=min(v.values())
        active=[x for x,c in v.items() if c==m]
        if len(active)>1:ties.append((s,active))
        derivative=min(dv[x] for x in active)
        H[s]=m;directional[s]=derivative
        for a,price in v.items():
            gap=price-m
            dgap=dv[a]-derivative
            if gap>0 and dgap<0:
                closures.append((gap/(-dgap),s,a))
            if gap==0 and dgap<0:
                raise AssertionError((s,a,'not a valid one-sided direction'))
closures.sort(key=lambda e:e[0])
t,hit,action=closures[0]
Knext=K+dK*t
Lnext=L+dL*t
assert t==F(6966,2783341) and Knext==F(3709800,6941) and Lnext==F(3529544,6941)
assert hit==(11,4,1) and action=='P'

H2={};tie2=[];strict=[]
for n in range(N,-1,-1):
    for s in states(n):
        n,a,b=s;r=F(2**(a+b),3**a)
        v={'P':Knext*r,'Q':Lnext}
        if n<N:
            v['C']=1+sum((P[i]*H2[c] for i,c in enumerate(children(s))),F(0))
        m=min(v.values())
        H2[s]=m
        tied=[a for a,c in v.items() if c==m]
        if len(tied)>1:tie2.append((s,tied))
        strict.extend(c-m for c in v.values() if c>m)
assert len(H2)==680 and len(strict)==1238
assert min(strict)==F(4,187407)
assert set((s,tuple(v)) for s,v in tie2)=={
    (B,('Q','C')),((11,4,1),('P','C'))
}
assert H2[(0,0,0)]==F(190052304168624227306189,506975463107337388032)
assert H2[(0,0,0)]==H[(0,0,0)]+t*directional[(0,0,0)]
print('PASS_STAGE138_DUAL_CANDIDATE_ONLY',t,Knext,Lnext,tie2,'strict_gaps',len(strict))
