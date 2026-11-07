#!/usr/bin/env python3
"""Exact Fraction checks for three-stage R5 occupancy convexification."""
from fractions import Fraction as F
from random import Random
R=tuple(map(F,('1/2','1','3/2')))
S=tuple(map(F,('1/4','1/2','1','3/2','7/4')))
w=(F(2,5),F(3,5))
K=((F(1,4),F(1,2),F(1,4)),(F(3,8),F(1,4),F(3,8)))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def row(r,eps):
    x=(r-eps)/(1-eps);p=(x-S[0])/(S[-1]-S[0]);assert 0<p<1
    a=[eps/F(5) for _ in S];a[0]+=(1-eps)*(1-p);a[-1]+=(1-eps)*p
    assert sum(a)==1 and dot(a,S)==r and min(a)>0
    return tuple(a)
M=tuple(tuple(row(r,(F(1,8),F(1,4))[h]) for r in R) for h in range(2))
for h in range(2):assert sum(K[h])==dot(K[h],R)==1
Q=tuple(sum(w[h]*K[h][j] for h in range(2)) for j in range(3))
C=tuple(tuple(sum(w[h]*K[h][j]*M[h][j][l] for h in range(2)) for l in range(5)) for j in range(3))
assert sum(Q)==dot(Q,R)==1
for j in range(3):assert sum(C[j])==Q[j] and dot(C[j],S)==Q[j]*R[j]

def flow(pol,q,c):
    a,b,d,e,f=pol; v=tuple(a*x for x in b)
    x=(1-a)*d; y=tuple(q[j]*(a-v[j])*e[j] for j in range(3))
    t=tuple(sum(c[j][l]*v[j] for j in range(3)) for l in range(5))
    z=tuple(t[l]*f[l] for l in range(5))
    return a,v,x,y,t,z

def inverse(fl,q,c):
    a,v,x,y,t,z=fl
    b=tuple(zj/a if a else F(0) for zj in v)
    d=x/(1-a) if a<1 else F(0)
    e=tuple(y[j]/(q[j]*(a-v[j])) if a>v[j] else F(0) for j in range(3))
    f=tuple(z[l]/t[l] if t[l] else F(0) for l in range(5))
    assert all(0<=v<=1 for v in (a,d)+b+e+f)
    return a,b,d,e,f

def obs(fl,q):
    a,v,x,y,t,z=fl
    eQ=x+sum(y)+sum(z)
    eP=(1-a-x)+sum(R[j]*(q[j]*(a-v[j])-y[j]) for j in range(3))+sum(S[l]*(t[l]-z[l]) for l in range(5))
    return eP,eQ,1+a+sum(R[j]*q[j]*v[j] for j in range(3)),1+a+sum(q[j]*v[j] for j in range(3))

def blend(x,y,t):
    if isinstance(x,tuple):return tuple(blend(a,b,t) for a,b in zip(x,y))
    return t*x+(1-t)*y
rng=Random(419703)
def f():return F(rng.randrange(17),16)
def policy():return f(),tuple(f() for _ in R),f(),tuple(f() for _ in R),tuple(f() for _ in S)
for mode in ('LR','FULL'):
    for i in range(120):
        lam=F((13*i)%19,18) if i%3 else F(0)
        if mode=='LR':
            p1,p2=policy(),policy()
            a,b=flow(p1,Q,C),flow(p2,Q,C)
            goal=blend(obs(a,Q),obs(b,Q),lam)
            mixed=blend(a,b,lam)
            recovered=inverse(mixed,Q,C)
            assert flow(recovered,Q,C)==mixed and obs(mixed,Q)==goal
        else:
            p1=tuple(policy() for _ in w);p2=tuple(policy() for _ in w)
            a=tuple(flow(p1[h],K[h],tuple(tuple(K[h][j]*M[h][j][l] for l in range(5)) for j in range(3))) for h in range(2))
            b=tuple(flow(p2[h],K[h],tuple(tuple(K[h][j]*M[h][j][l] for l in range(5)) for j in range(3))) for h in range(2))
            mixed=blend(a,b,lam)
            for h in range(2):
                c=tuple(tuple(K[h][j]*M[h][j][l] for l in range(5)) for j in range(3))
                assert flow(inverse(mixed[h],K[h],c),K[h],c)==mixed[h]
                assert obs(mixed[h],K[h])==blend(obs(a[h],K[h]),obs(b[h],K[h]),lam)
    print('PASS_120_EXACT_MIXTURES_'+mode)
print('PASS_EXACT_R5_THREE_STAGE_REAL_IMAGE_CONVEXITY_CORE')
