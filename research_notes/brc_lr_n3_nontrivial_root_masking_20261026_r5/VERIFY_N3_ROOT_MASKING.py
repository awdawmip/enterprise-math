#!/usr/bin/env python3
"""Exact rational author checker for depth-3 LR root masking.
All computations use fractions.Fraction, no floating-point.
The finite cost grid is not a proof for arbitrary real coefficients.
"""
from fractions import Fraction as F
from itertools import product

R = (F(1, 2), F(1), F(3, 2))
S = (F(1, 2), F(3, 2))
Q3 = (F(1, 2), F(1, 2))
P3 = tuple(s*q for s,q in zip(S,Q3))
ALPHA = {"a":F(1,4),"b":F(1,3)}
H1 = {h:F(1,2) for h in ALPHA}
Q2 = {h:(v,1-2*v,v) for h,v in ALPHA.items()}
P2 = {h:tuple(r*q for r,q in zip(R,Q2[h])) for h in ALPHA}
QBAR=tuple(sum(H1[h]*Q2[h][i] for h in ALPHA) for i in range(3))
assert sum(P3)==sum(Q3)==1
assert QBAR==(F(7,24),F(5,12),F(7,24))
assert Q2["a"] != Q2["b"]
for h in ALPHA:
    assert sum(Q2[h])==sum(P2[h])==1
    assert all(x>0 for x in Q2[h]+P2[h])

def support(A,B,C,D):
    def H(r):return min(A*r,B)
    gamma=C+D
    def phi(r):
        return min(H(r),C*r+D+sum(q*H(r*s) for q,s in zip(Q3,S)))
    f={h:sum(q*phi(r) for q,r in zip(Q2[h],R)) for h in ALPHA}
    m=H(F(1))
    full=min(m,gamma+sum(H1[h]*min(m,gamma+f[h]) for h in ALPHA))
    pooled=sum(q*phi(r) for q,r in zip(QBAR,R))
    lr=min(m,gamma+min(m,gamma+pooled))
    d=[m-f[h] for h in ALPHA]
    gap=2*phi(F(1))-phi(F(1,2))-phi(F(3,2))
    assert gap>=0 and m>=phi(F(1))
    assert sum(d)/2 <= 2*min(d)
    return full,lr

def observe(compressed=False):
    ep=eq=tp=tq=F(0)
    def go(t,h,r,s,p,q):
        nonlocal ep,eq,tp,tq
        if t==0: acts={"C":F(1)}
        elif compressed:
            if t==1: acts={"P":F(1,2),"C":F(1,2)}
            elif t==2:
                acts={"P":F(1,7),"C":F(6,7)} if r==F(3,2) else {"P":F(1)}
            else: acts={"P":F(1)} if r*s>=1 else {"Q":F(1)}
        else:
            if t==1: acts={"C":F(1)} if h=="a" else {"P":F(1)}
            elif t==2: acts={"C":F(1)} if h=="a" and r==F(3,2) else {"P":F(1)}
            else: acts={"P":F(1)} if r*s>=1 else {"Q":F(1)}
        assert sum(acts.values())==1
        for action,w in acts.items():
            pp,qq=p*w,q*w
            if action=="P":eq+=qq
            elif action=="Q":ep+=pp
            else:
                assert t<3
                tp+=pp;tq+=qq
                if t==0:
                    for h2 in ALPHA:go(1,h2,None,None,pp*H1[h2],qq*H1[h2])
                elif t==1:
                    for i,r2 in enumerate(R):go(2,h,r2,None,pp*P2[h][i],qq*Q2[h][i])
                else:
                    for j,s2 in enumerate(S):go(3,h,r,s2,pp*P3[j],qq*Q3[j])
    go(0,None,None,None,F(1),F(1))
    return ep,eq,tp,tq

raw,compressed=observe(False),observe(True)
assert raw==compressed==(F(3,64),F(15,16),F(27,16),F(13,8)),(raw,compressed)
n=0
for a,b,c,d in product(range(-3,4),repeat=4):
    f,l=support(F(a),F(b),F(c),F(d))
    assert f==l,(a,b,c,d,f,l)
    n+=1
print("EXACT_POSITIVE_MASS_NORMALIZATION=PASS")
print("TIME1_STRONG_LR_LUMPABILITY=FAIL (Q2 a,b differ)")
print("TIME2_TO_TIME3_SIGNAL=NONTRIVIAL (LR multipliers 1/2,3/2)")
print("EXACT_FULL_FOUR_VECTOR=",tuple(map(str,raw)))
print("EXACT_COMPRESSED_FOUR_VECTOR=",tuple(map(str,compressed)))
print("RATIONAL_WITNESS=PASS")
print("SIGNED_SUPPORT_GRID_POINTS=",n)
print("BELLMAN_FULL_VS_LR_GRID=PASS")
print("UNIVERSAL_REAL_COEFFICIENT_CLAIM=ALGEBRAIC_PROOF_REQUIRED")
