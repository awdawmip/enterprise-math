#!/usr/bin/env python3
"""Exact rational regression for the four-signature signed-threshold quadratic oracle."""
from fractions import Fraction as F
from random import Random
from itertools import product

S=(F(1,2),F(1),F(3,2),F(5,2)); i_merge=2
MU=((F(7,50),F(11,75),F(1,2),F(16,75)),
    (F(17,200),F(23,150),F(3,5),F(97,600)))
NU_L=((F(1,2),F(1,6),F(1,4),F(1,12)),
      (F(5,12),F(1,3),F(1,6),F(1,12)))
NU_R=((F(17,100),F(23,75),F(1,5),F(97,300)),
      (F(31,120),F(5,18),F(1,15),F(143,360)))
ETA=((F(1,8),F(1,4),F(3,8),F(1,4)),
     (F(5,32),F(3,16),F(13,32),F(1,4)))
Q_ORIGIN=(F(1,4),F(1,4))
V=tuple(Q_ORIGIN[i]*MU[i][1]*NU_L[i][i_merge] for i in range(2))
W=tuple(Q_ORIGIN[i]*MU[i][2]*NU_R[i][i_merge] for i in range(2))
A=tuple(sum((V[i]*ETA[i][j] for i in range(2)),F(0)) for j in range(4))
B=tuple(sum((W[i]*ETA[i][j] for i in range(2)),F(0)) for j in range(4))
C_L=sum(V); C_R=sum(W)

def base(U,L,R):
    """Q-law global terminal likelihood-ratio histogram when merger stops."""
    h=C_L*L+C_R*R
    z=[F(1,2),F(0),F(1,2)*(1-U)+h,F(0)]
    for i in range(2):
        m=Q_ORIGIN[i]
        z[0]+=U*m*MU[i][0]
        z[3]+=U*m*MU[i][3]
        z[1]+=(U-L)*m*MU[i][1]
        z[2]+=(U-R)*m*MU[i][2]
        for j in (0,1,3):
            z[j]+=L*m*MU[i][1]*NU_L[i][j]+R*m*MU[i][2]*NU_R[i][j]
    return tuple(z)

def residual(L,R):
    h=C_L*L+C_R*R
    return tuple(L*A[j]+R*B[j]-(h if j==i_merge else 0) for j in range(4))

def whole(U,L,R,gamma):
    h=C_L*L+C_R*R
    H0=base(U,L,R); D=residual(L,R)
    H=tuple(H0[j]+gamma*D[j] for j in range(4))
    tQ=F(1)+U/2+F(3,40)*L+F(11,40)*R+gamma*h
    tP=F(1)+F(3,4)*U+F(3,40)*L+F(33,80)*R+F(3,2)*gamma*h
    return H,tP,tQ,H0,D,h

def greedy(q,H):
    if not F(0)<=q<=sum(H):return None
    def allocate(ids):
        z=q; val=F(0)
        for j in ids:
            v=min(z,H[j]);val+=S[j]*v;z-=v
        assert z==0
        return val
    return allocate(range(4)),allocate(range(3,-1,-1))

def threshold(q,b,H):
    if q<0 or q>sum(H):return False
    for lam in S:
        z=b-lam*q
        lo=sum(((s-lam)*H[j] for j,s in enumerate(S) if s<lam),F(0))
        hi=sum(((s-lam)*H[j] for j,s in enumerate(S) if s>lam),F(0))
        if not lo<=z<=hi:return False
    return True

def quadratic(U,L,R,M,q,b):
    """Cross-multiplied degree <=2 test (U,R unknown, times/errors fixed)."""
    h=C_L*L+C_R*R
    H0=base(U,L,R);D=residual(L,R)
    if h==0:
        assert L==R==M==0
        return threshold(q,b,H0)
    if not 0<=M<=h:return False
    if q<0 or q>1:return False
    for lam in S:
        z=h*(b-lam*q)
        low=sum(((s-lam)*(h*H0[j]+M*D[j]) for j,s in enumerate(S) if s<lam),F(0))
        high=sum(((s-lam)*(h*H0[j]+M*D[j]) for j,s in enumerate(S) if s>lam),F(0))
        if not low<=z<=high:return False
    return True

def test(U,L,R,gamma,coins,deep=False):
    assert 0<=L<=U<=1 and 0<=R<=U
    H,tP,tQ,H0,D,h=whole(U,L,R,gamma)
    assert all(x>=0 for x in H)
    assert sum(H)==sum(H0)==1
    assert sum((S[j]*H[j] for j in range(4)),F(0))==1
    assert sum((S[j]*H0[j] for j in range(4)),F(0))==1
    assert sum(D)==sum((S[j]*D[j] for j in range(4)),F(0))==0
    q=sum((coins[j]*H[j] for j in range(4)),F(0))
    b=sum((coins[j]*H[j]*S[j] for j in range(4)),F(0))
    assert threshold(q,b,H)
    assert quadratic(U,L,R,gamma*h,q,b)
    assert greedy(q,H)[0]<=b<=greedy(q,H)[1]
    assert L==F(80,3)*(F(3,2)*tQ-tP-F(1,2))
    assert gamma*h==tQ-F(1)-U/2-F(3,40)*L-F(11,40)*R
    if deep:
        print('S',tuple(map(str,S)))
        print('origin_route_Q_masses',tuple(map(str,V)),tuple(map(str,W)))
        print('origin_flow_determinant',V[0]*W[1]-V[1]*W[0])
        print('tail_A',tuple(map(str,A)));print('tail_B',tuple(map(str,B)))
        print('U_L_R_gamma',*(str(x) for x in (U,L,R,gamma)))
        print('H0',tuple(map(str,H0)))
        print('D',tuple(map(str,D)))
        print('H',tuple(map(str,H)))
        print('h,M',h,gamma*h)
        print('observer_eP_eQ_TP_TQ',*(str(x) for x in (1-b,q,tP,tQ)))
        print('threshold_oracle',threshold(q,b,H),'quadratic_oracle',quadratic(U,L,R,gamma*h,q,b))
    return H

def main():
    for parent,kernel in [(F(3,2),MU),(F(1),NU_L),(F(3,2),NU_R),(F(3,2),ETA)]:
        for row in kernel:
            assert all(v>0 for v in row)
            assert sum(row)==1
            assert sum((row[j]*S[j] for j in range(4)),F(0))==parent
    assert V==(F(11,1200),F(23,3600))
    assert W==(F(1,40),F(1,100))
    assert V[0]*W[1]-V[1]*W[0]==F(-49,720000)
    test(F(1),F(1,2),F(1,3),F(2,5),(F(1,7),F(2,5),F(4,7),F(3,4)),True)
    assert not quadratic(F(1),F(1,2),F(1,3),F(2,5)*(C_L/2+C_R/3),F(0),F(1))
    rng=Random(20261029)
    for n in range(1600):
        U=F(rng.randrange(0,10),9);L=U*F(rng.randrange(0,10),9)
        R=U*F(rng.randrange(0,10),9);gamma=F(rng.randrange(0,10),9)
        coins=tuple(F(rng.randrange(0,10),9) for _ in range(4))
        H=test(U,L,R,gamma,coins)
        h=C_L*L+C_R*R
        H0=base(U,L,R);D=residual(L,R)
        for _ in range(5):
            q=F(rng.randrange(0,41),40)
            b=F(rng.randrange(0,41),40)
            gr=greedy(q,H)
            oracle=gr is not None and gr[0]<=b<=gr[1]
            assert threshold(q,b,H)==oracle
            assert quadratic(U,L,R,gamma*h,q,b)==oracle
    # Dense exact grid on an active rational point; reject as well as accept.
    U=F(1);L=F(1,2);R=F(1,3);gamma=F(2,5)
    H,*_=whole(U,L,R,gamma);h=C_L*L+C_R*R
    accept=reject=0
    for i,j in product(range(51), repeat=2):
        q=F(i,50);b=F(j,50)
        g=greedy(q,H)
        expected=g is not None and g[0]<=b<=g[1]
        assert threshold(q,b,H)==expected
        assert quadratic(U,L,R,gamma*h,q,b)==expected
        if expected:accept+=1
        else:reject+=1
    print('random_rational_policies_checked',1600)
    print('random_valid_and_invalid_observer_pairs_checked',1600*5)
    print('dense_grid_pairs_checked',accept+reject,'accepted',accept,'rejected',reject)
    print('h_zero_case',quadratic(F(0),F(0),F(0),F(0),F(1,2),F(1,4)))
    print('PASS_EXACT_R5_SIGNED_THRESHOLD_QUADRATIC_ORACLE')
if __name__=='__main__':main()
