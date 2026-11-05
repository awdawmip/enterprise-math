#!/usr/bin/env python3
"""Exact certificates: time-only hull indistinguishability and 4D separation."""
from fractions import Fraction as F
from itertools import product

R = (F(1,4), F(1,2), F(1), F(3,2), F(7,4))
S = (F(1,8), F(1,2), F(1), F(3,2), F(15,8))
K0 = (F(1,8), F(1,4), F(1,4), F(1,4), F(1,8))
D = (15, -26, 22, -26, 15)
KA = tuple(v + F(z,512) for v,z in zip(K0,D))
KB = tuple(v - F(z,512) for v,z in zip(K0,D))
W_SOURCE = (F(1,2), F(1,2))
EPS = F(1,16)
BETA = F(13,50)
N = (-F(1), -F(1), F(0), -BETA)

def m_kernel(r):
    target = (r-EPS)/(1-EPS)
    high = (target-S[0])/(S[-1]-S[0])
    low = 1-high
    return tuple(EPS/F(5) + (1-EPS)*(low if l==0 else high if l==4 else 0)
                 for l in range(5))

M = tuple(m_kernel(r) for r in R)

def pos(x):
    return max(x,F(0))

def score(v):
    return sum((a*b for a,b in zip(N,v)),F(0))

def step(v, q, r, time, label):
    eP,eQ,TP,TQ=v
    return (eP+(q*r if label=='Q' else 0),
            eQ+(q if label=='P' else 0),
            TP+time*q*r, TQ+time*q)

def witness():
    v=step((F(0),)*4,W_SOURCE[1],F(1),1,'P')
    for j,r in enumerate(R):
        q=W_SOURCE[0]*KA[j]
        if j==2:
            for l,s in enumerate(S):
                v=step(v,q*M[j][l],s,3,'Q' if s<=1 else 'P')
        else:
            v=step(v,q,r,2,'Q' if r<=1 else 'P')
    return v

def first_advantage(K, B):
    L=lambda r: max(-r,-F(1))
    A=sum((k*L(r) for k,r in zip(K,R)),F(0))-L(F(1))
    return A-BETA+sum((k*pos(b-BETA) for k,b in zip(K,B)),F(0))

def terminal_gain():
    L=lambda r:max(-r,-F(1))
    return tuple(sum((p*L(s) for p,s in zip(m,S)),F(0))-L(r)
                 for r,m in zip(R,M))

def payoff(q,r,t,label):
    return score(step((F(0),)*4,q,r,t,label))

def lr_exhaustive():
    qbar=tuple((KA[j]+KB[j])/2 for j in range(5))
    best=None
    cases=0
    for terminal in product(('P','Q'),repeat=5):
        late=tuple(sum((payoff(qbar[j]*M[j][l],s,3,terminal[l])
                        for l,s in enumerate(S)),F(0)) for j in range(5))
        choices=tuple((payoff(qbar[j],R[j],2,'P'),
                       payoff(qbar[j],R[j],2,'Q'),late[j]) for j in range(5))
        for layer2 in product(range(3),repeat=5):
            v=sum((choices[j][layer2[j]] for j in range(5)),F(0))
            for layer1 in ('P','Q','C'):
                cases+=1
                value=v if layer1=='C' else payoff(F(1),F(1),1,layer1)
                best=value if best is None else max(best,value)
    return cases,best

def main():
    for K in (KA,KB):
        assert all(p>0 for p in K)
        assert sum(K)==1 and sum((p*r for p,r in zip(K,R)),F(0))==1
    for m,r in zip(M,R):
        assert all(p>0 for p in m)
        assert sum(m)==1 and sum((p*s for p,s in zip(m,S)),F(0))==r
    assert KA != KB
    low_root=F(37,44)
    high_root=F(51,44)
    for K in (KA,KB):
        assert low_root-1+sum((p*pos(low_root-r) for p,r in zip(K,R)),F(0))==0
        assert 1-high_root+sum((p*pos(r-high_root) for p,r in zip(K,R)),F(0))==0
    assert sum((z*pos(low_root-r) for z,r in zip(D,R)))==0
    assert sum((z*pos(r-high_root) for z,r in zip(D,R)))==0
    B=terminal_gain()
    assert B==(F(67,1280),F(227,1280),F(547,1280),F(227,1280),F(67,1280))
    assert tuple(b>BETA for b in B)==(False,False,True,False,False)
    xa=first_advantage(KA,B)
    xb=first_advantage(KB,B)
    assert xa==F(7141,1638400) and xb==-F(5221,1638400)
    hfull=-F(1)-BETA+pos(xa)/2+pos(xb)/2
    hlr=-F(1)-BETA+pos((xa+xb)/2)
    assert hfull==-F(4121627,3276800)
    assert hlr==-F(32241,25600)
    gap=hfull-hlr
    assert gap==F(5221,3276800)>0
    w=witness()
    assert w==(F(10571,131072),F(12273,16384),F(843,512),F(843,512))
    assert score(w)==hfull
    count,best=lr_exhaustive()
    assert count==3*(3**5)*(2**5)==23328 and best==hlr
    dist=gap/sum(map(abs,N))
    assert dist==F(5221,7405568)
    print('R=',R)
    print('K_A=',KA,'K_B=',KB)
    print('time_only_roots=',low_root,high_root)
    print('late_gain=',B)
    print('normal=',N,'first_advantages=',(xa,xb))
    print('FULL_witness=',w)
    print('FULL_support=',hfull,'LR_support=',hlr,'gap=',gap)
    print('infinity_distance_lower_bound=',dist)
    print('seedless_LR_deterministic_policies=',count)
    print('PASS_EXACT_R5_TIME_FACE_CLASSIFICATION_SEPARATION')

if __name__=='__main__':
    main()
