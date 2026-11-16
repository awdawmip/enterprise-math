#!/usr/bin/env python3
"""Exact finite Bellman tag-channel order, concavity, and robustness checks."""
from fractions import Fraction as F
from itertools import product
import random

def plus(x): return max(F(0),x)
def optimum(w,A,u,T):
    m=len(w); k=len(T[0]); assert len(A)==len(u)==len(T)==m
    assert all(w[i]>0 and all(x>=0 for x in T[i]) and sum(T[i])==1 for i in range(m))
    full=sum((w[i]*max(F(0),A[i],A[i]+u[i]) for i in range(m)),F(0))
    tagged=max((sum((w[i]*plus(A[i]+u[i]*sum((T[i][j]*z[j] for j in range(k)),F(0))) for i in range(m)),F(0)) for z in product((0,1),repeat=k)))
    return full,tagged,full-tagged

def channel_product(T,K):
    return [[sum((T[i][j]*K[j][y] for j in range(len(K))),F(0)) for y in range(len(K[0]))] for i in range(len(T))]

def mix(T,R,lam): return [[lam*a+(1-lam)*b for a,b in zip(t,r)] for t,r in zip(T,R)]
def randrow(rng,k):
    x=[rng.randint(1,8) for _ in range(k)]; return [F(v,sum(x)) for v in x]

def run():
    w=[F(1),F(1)]; A=[F(1),F(-1)];u=[F(-2),F(2)]
    ident=[[F(1),F(0)],[F(0),F(1)]]
    swap=[[F(0),F(1)],[F(1),F(0)]]
    half=mix(ident,swap,F(1,2))
    a=optimum(w,A,u,ident); b=optimum(w,A,u,swap); c=optimum(w,A,u,half)
    assert a==(F(2),F(2),F(0)) and b==a
    assert c==(F(2),F(1),F(1))
    print('PERMUTATION_MIXTURE: D(T0)=0 D(T1)=0 D(half*(T0+T1))=1')
    K=[[F(3,4),F(1,4)],[F(1,4),F(3,4)]]
    noisy=channel_product(ident,K)
    q=optimum(w,A,u,noisy)
    assert q==(F(2),F(1),F(1))
    print('BINARY_GARBLING: FULL=2 TAG=1 D=1')
    rng=random.Random(225135)
    cnt=0
    for iteration in range(300):
        m=rng.randint(2,5); k=rng.randint(2,5); out=rng.randint(2,4)
        w=[F(rng.randint(1,7),rng.randint(1,8)) for _ in range(m)]
        A=[F(rng.randint(-8,8),rng.randint(1,7)) for _ in range(m)]
        u=[F(rng.randint(-8,8),rng.randint(1,7)) for _ in range(m)]
        T=[randrow(rng,k) for _ in range(m)]; R=[randrow(rng,k) for _ in range(m)]
        K=[randrow(rng,out) for _ in range(k)]
        lam=F(rng.randint(0,7),7)
        FT,HT,DT=optimum(w,A,u,T)
        FR,HR,DR=optimum(w,A,u,R)
        FM,HM,DM=optimum(w,A,u,mix(T,R,lam))
        assert FT==FR==FM
        assert DM>=lam*DT+(1-lam)*DR
        _,Hgarb,Dgarb=optimum(w,A,u,channel_product(T,K))
        assert Dgarb>=DT
        total_tv=sum((w[i]*abs(u[i])*sum((abs(T[i][j]-R[i][j]) for j in range(k)),F(0))/2 for i in range(m)),F(0))
        assert abs(DT-DR)<=total_tv
        cnt+=1
    print('FRACTION_SEEDED_INSTANCES='+str(cnt))
    print('PASS_EXACT_R5_TAG_CHANNEL_CONCAVITY_BLACKWELL_TV')

if __name__=='__main__':run()
