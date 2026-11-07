#!/usr/bin/env python3
"""Exact support and policy certificates for R5 late-kernel time tilt."""
from fractions import Fraction as F
from itertools import product

W = (F(1,2), F(1,2))
R = (F(1,2), F(1), F(3,2))
S = (F(1,4), F(1), F(7,4))
K = ((F(1,4), F(1,2), F(1,4)), (F(3,8), F(1,4), F(3,8)))
LOW = (F(3,4), F(1,6), F(1,12))
MID_A = (F(1,4), F(1,2), F(1,4))
MID_B = (F(1,3), F(1,3), F(1,3))
HIGH = (F(1,12), F(1,6), F(3,4))
ALT_LOW = (F(35,48), F(5,24), F(1,16))
ALT_HIGH = (F(1,16), F(5,24), F(35,48))

def stop_decision(r):
    return 'P' if r <= 1 else 'Q'

def value4(t1, t2, t3, M):
    eP=eQ=TP=TQ=F(0)
    def add(q,r,t,decision):
        nonlocal eP,eQ,TP,TQ
        if decision == 'P':
            eQ += q
        else:
            assert decision == 'Q'
            eP += q*r
        TQ += q*t
        TP += q*r*t
    for h in range(2):
        if t1[h] != 'C':
            add(W[h],F(1),1,t1[h])
            continue
        for j,r in enumerate(R):
            q=W[h]*K[h][j]
            if t2[h][j] != 'C':
                add(q,r,2,t2[h][j])
            else:
                for l,s in enumerate(S):
                    add(q*M[h][j][l],s,3,t3[h][j][l])
    return (eP,eQ,TP,TQ)

def dot(n,v):
    return sum((x*y for x,y in zip(n,v)),F(0))

def verify(tag,target,M,alpha):
    j0=R.index(target)
    L=lambda r:max(r,F(1))
    B=[[sum((M[h][j][l]*L(s) for l,s in enumerate(S)),F(0))-L(r)
        for j,r in enumerate(R)] for h in range(2)]
    assert B[0][j0] != B[1][j0]
    t=(B[0][j0]+B[1][j0])/2
    cost=lambda r:alpha*(r-target)+t
    n=(F(1),F(1),-alpha,alpha*target-t)
    assert sum(W)==1
    for h in range(2):
        assert all(x>0 for x in K[h])
        assert sum(K[h])==1 and sum((p*r for p,r in zip(K[h],R)),F(0))==1
        for j,r in enumerate(R):
            assert all(p>0 for p in M[h][j])
            assert sum(M[h][j])==1
            assert sum((p*s for p,s in zip(M[h][j],S)),F(0))==r
    A=[sum((K[h][j]*L(r) for j,r in enumerate(R)),F(0))-L(F(1)) for h in range(2)]
    D=[[B[h][j]-cost(r) for j,r in enumerate(R)] for h in range(2)]
    X=[A[h]-cost(F(1))+sum((K[h][j]*max(D[h][j],F(0)) for j in range(3)),F(0)) for h in range(2)]
    mu=sum((W[h]*X[h] for h in range(2)),F(0))
    eta=F(0)
    for j in range(3):
        positive_terms=sum((W[h]*K[h][j]*max(D[h][j],F(0)) for h in range(2)),F(0))
        combined=sum((W[h]*K[h][j]*D[h][j] for h in range(2)),F(0))
        eta+=positive_terms-max(combined,F(0))
    eta_target=min(W[0]*K[0][j0],W[1]*K[1][j0])*abs(B[0][j0]-B[1][j0])/2
    assert all(x>0 for x in X) and mu>eta and eta==eta_target>0
    assert D[0][j0]*D[1][j0]<0
    assert all(D[0][j]*D[1][j]>=0 for j in range(3) if j!=j0)
    h_full=L(F(1))-cost(F(1))+sum((W[h]*max(X[h],F(0)) for h in range(2)),F(0))
    h_lr=L(F(1))-cost(F(1))+max(mu-eta,F(0))
    assert h_full-h_lr==eta_target
    t1=('C','C')
    t2=tuple(tuple('C' if D[h][j]>0 else stop_decision(r) for j,r in enumerate(R)) for h in range(2))
    t3=tuple(tuple(tuple(stop_decision(s) for s in S) for _ in R) for _ in range(2))
    witness=value4(t1,t2,t3,M)
    assert dot(n,witness)==h_full
    lr_max=None
    count=0
    for a1 in ('P','Q','C'):
        for opts2 in product(('P','Q','C'),repeat=3):
            for opts3 in product(('P','Q'),repeat=3):
                count+=1
                v=dot(n,value4((a1,a1),(opts2,opts2),tuple(tuple(opts3 for _ in R) for _ in W),M))
                lr_max=v if lr_max is None else max(lr_max,v)
    assert count==648 and lr_max==h_lr
    distance=eta_target/sum(map(abs,n))
    print(f'{tag}: target={target}; normal={n}; terminal_gain={tuple(B[h][j0] for h in range(2))}')
    print(f'  X={X}; eta={eta}; h_FULL={h_full}; h_LR={h_lr}; gap={h_full-h_lr}')
    print(f'  FULL_witness_O4={witness}; score={dot(n,witness)}; LR_enumerated={count}')
    print(f'  infinity_distance_lower_bound={distance}')
    return count

def main():
    c1=verify('MIDDLE_NODE',F(1),((LOW,MID_A,HIGH),(LOW,MID_B,HIGH)),F(2))
    c2=verify('HIGH_NODE',F(3,2),((LOW,MID_A,HIGH),(LOW,MID_A,ALT_HIGH)),F(4))
    c3=verify('LOW_NODE',F(1,2),((LOW,MID_A,HIGH),(ALT_LOW,MID_A,HIGH)),F(-4))
    print(f'EXACT_LR_POLICIES_CHECKED={c1+c2+c3}')
    print('PASS_EXACT_R5_UNIVERSAL_LATE_KERNEL_SEPARATION')

if __name__ == '__main__':
    main()
