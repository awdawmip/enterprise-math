#!/usr/bin/env python3
"""Exact-rational verification for R5 overlap-gluing polytope; author-side proof examples."""
from fractions import Fraction as F
from itertools import product
from random import Random

def tv(a,b):
    return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2

def stats(s,r,q,qa,k):
    assert len(s)==len(q)==len(qa)
    assert sum(q)==sum(qa)==1
    assert sum((x*y for x,y in zip(s,q)),F(0))==r
    assert sum((x*y for x,y in zip(s,qa)),F(0))==r
    u=tv(q,qa)
    v=tv([x*y/r for x,y in zip(s,q)], [x*y/r for x,y in zip(s,qa)])
    return u,v,min(q[k],qa[k])

def feasible(s,r,u,v,g,k,strict=False):
    assert len(s)>=3 and s[0]<r<s[-1] and all(0<s[i]<s[i+1] for i in range(len(s)-1))
    o=[s[j] for j in range(len(s)) if j!=k]
    M=1-u; C=r-r*v; R=M-g; D=C-s[k]*g
    if not(u>=0 and s[1]*u<=r*v<=s[-2]*u and 0<=g<=M): return False
    if not strict: return min(o)*R<=D<=max(o)*R
    return g>0 and R>0 and min(o)*R<D<max(o)*R

def construct(s,r,u,v,g,k):
    assert feasible(s,r,u,v,g,k)
    n=len(s); M=1-u; C=r-r*v
    a=[F(0)]*n; b=[F(0)]*n; c=[F(0)]*n
    if u:
        m=r*v/u
        a[0]=(s[-1]-m)/(s[-1]-s[0]);a[-1]=(m-s[0])/(s[-1]-s[0])
        if n==3: b[1]=1
        else:
            b[1]=(s[-2]-m)/(s[-2]-s[1])
            b[-2]=(m-s[1])/(s[-2]-s[1])
    c[k]=g
    other=[j for j in range(n) if j!=k]
    lo=min(other,key=lambda j:s[j]);hi=max(other,key=lambda j:s[j])
    R=M-g;D=C-s[k]*g
    if R:
        c[hi]+=(D-s[lo]*R)/(s[hi]-s[lo])
        c[lo]+=(s[hi]*R-D)/(s[hi]-s[lo])
    q=[c[j]+u*a[j] for j in range(n)]
    qa=[c[j]+u*b[j] for j in range(n)]
    assert all(x>=0 for x in q+qa)
    assert stats(s,r,q,qa,k)==(u,v,g)
    return q,qa

def mean_kernel(s,r,rng):
    n=len(s);q=[F(rng.randint(1,6),1000*n) for _ in s]
    M=1-sum(q);C=r-sum((z*x for z,x in zip(s,q)),F(0))
    q[0]+=(s[-1]*M-C)/(s[-1]-s[0])
    q[-1]+=(C-s[0]*M)/(s[-1]-s[0])
    assert all(x>0 for x in q)
    return q

def verify():
    s=[F(1,2),F(1),F(2),F(3)];r=F(3,2);u=v=F(3,5)
    M=1-u;C=r-r*v
    lo=max(F(0),(C-s[-2]*M)/(s[-1]-s[-2]))
    hi=(C-s[0]*M)/(s[-1]-s[0])
    assert (lo,hi)==(F(0),F(4,25))
    assert not feasible(s,r,u,v,F(1,5),3)
    q,qa=construct(s,r,u,v,hi,3)
    assert q==[F(3,5),F(0),F(0),F(2,5)]
    assert qa==[F(6,25),F(3,10),F(3,10),F(4,25)]
    q=[F(147,250),F(1,100),F(1,100),F(49,125)]
    qa=[F(57,250),F(31,100),F(31,100),F(19,125)]
    assert stats(s,r,q,qa,3)==(u,v,F(19,125))
    assert feasible(s,r,u,v,F(19,125),3,strict=True)
    assert all(x>0 for x in q+qa)
    t=[F(1),F(2),F(4),F(5)];r2=F(3)
    z=[F(3,8),F(1,8),F(1,8),F(3,8)]
    za=[F(1,8),F(3,8),F(3,8),F(1,8)]
    assert stats(t,r2,z,za,0)[:2]==(F(1,2),F(1,2))
    Wq=[F(1,4),F(1,4),F(1,2)]
    Wp=[F(3,8),F(3,8),F(1,4)]
    assert sum(Wq)==sum(Wp)==1
    massQ=massP=F(0)
    for source_idx,first in enumerate([q,qa]):
        for i,prob in enumerate(first):
            Q0=Wq[source_idx]*prob
            P0=Wp[source_idx]*(s[i]/r)*prob
            assert P0==s[i]*Q0
            if i==3:
                second=[z,za][source_idx]
                for j,prob2 in enumerate(second):
                    Q=Q0*prob2;P=P0*(t[j]/r2)*prob2
                    assert P==t[j]*Q
                    massQ+=Q;massP+=P
            else:
                massQ+=Q0;massP+=P0
    massQ+=Wq[2];massP+=Wp[2]
    assert massQ==massP==1
    assert min(Wq[0]*q[-1],Wq[1]*qa[-1])==F(19,500)
    assert F(19,500)<F(1,25)<F(1,20)
    print('EXACT_TWO_LEVEL_WITNESS Q_min=19/500, upper_Q_min=1/25, rejected_target=1/20')
    print('FIRST_STAGE_LR=3/2, TV_Q=3/5, TV_P=3/5, gamma_max=4/25')
    print('SECOND_STAGE_LR=3, TV_Q=1/2, TV_P=1/2; BOTH_LAWS_NORMALIZED=1')
    rng=Random(20261028);tested=0
    for n in (3,4,5,6):
        s=[F((j+1)**2,j+2) for j in range(n)]
        assert all(s[i]<s[i+1] for i in range(n-1))
        r=(s[0]+s[-1])/2
        for _ in range(60):
            q=mean_kernel(s,r,rng);qa=mean_kernel(s,r,rng)
            for k in range(n):
                u,v,g=stats(s,r,q,qa,k)
                assert feasible(s,r,u,v,g,k,strict=True)
                cq,ca=construct(s,r,u,v,g,k)
                assert stats(s,r,cq,ca,k)==(u,v,g)
                tested+=1
    print('EXACT_RANDOM_POSITIVE_TRIPLES_CHECKED',tested)
    grid=[F(j,12) for j in range(13)]
    checked=0
    for s,r in [([F(1),F(3),F(4)],F(2)),([F(1,2),F(1),F(2),F(3)],F(3,2))]:
        for k in range(len(s)):
            for u,v,g in product(grid,repeat=3):
                if feasible(s,r,u,v,g,k):
                    qa,qb=construct(s,r,u,v,g,k)
                    assert stats(s,r,qa,qb,k)==(u,v,g)
                    checked+=1
    print('EXACT_GRID_FEASIBLE_TRIPLES_CONSTRUCTED',checked)
    print('ALL EXACT OVERLAP-GLUING CHECKS PASSED')
if __name__=='__main__':verify()
