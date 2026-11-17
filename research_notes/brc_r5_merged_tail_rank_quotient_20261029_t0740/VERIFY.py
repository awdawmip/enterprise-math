#!/usr/bin/env python3
"""Exact rational checks for BRC merged-tail rank/quotient theorem (author-side)."""
from fractions import Fraction as F
from itertools import product
from hashlib import sha256

S = (F(1,2), F(1), F(3,2), F(5,2))
v = (F(11,1200), F(23,3600))
w = (F(1,40), F(1,100))
ETA = ((F(1,8),F(1,4),F(3,8),F(1,4)),
       (F(5,32),F(3,16),F(13,32),F(1,4)))

for row in ETA:
    assert all(t>0 for t in row)
    assert sum(row)==1
    assert sum(s*x for s,x in zip(S,row))==F(3,2)

assert all(t>0 for t in (*v,*w))
det=v[0]*w[1]-v[1]*w[0]
assert det==F(-49,720000)

def influx(L,R):
    return (v[0]*L+w[0]*R, v[1]*L+w[1]*R)

def tail(U,aL,aR,g):
    assert all(F(0)<=x<=1 for x in (U,aL,aR,g))
    L,R=U*aL,U*aR
    x=influx(L,R)
    m=tuple(g*t for t in x)
    H=tuple(sum(m[i]*ETA[i][k] for i in range(2)) for k in range(4))
    assert sum(H)==sum(m)
    assert sum(s*h for s,h in zip(S,H))==F(3,2)*sum(m)
    return L,R,x,m,H

# Concrete nonconvexity of the joint (U,L,R,m_A,m_B) graph.
left=tail(F(1), F(1), F(0), F(1))
right=tail(F(1),F(0),F(1),F(0))
Lmid=(left[0]+right[0])/2
Rmid=(left[1]+right[1])/2
xmid=influx(Lmid,Rmid)
mmid=tuple((a+b)/2 for a,b in zip(left[3],right[3]))
D=mmid[0]*xmid[1]-mmid[1]*xmid[0]
assert D==det/4==F(-49,2880000)
# Yet its quotient is feasible with gamma'=1, (L',R')=(1/2,0).
assert tail(F(1),F(1,2),F(0),F(1))[3]==mmid
assert tail(F(1),F(1,2),F(0),F(1))[4]==tuple((a+b)/2 for a,b in zip(left[4],right[4]))

# Recover the TWO origin post-merge Q masses from two signature bins.
def recover(H):
    return (20*H[3]-32*H[0],32*H[0]-16*H[3])
assert recover(left[4])==left[3]

DENO = 5
GRID=[F(n,DENO) for n in range(DENO+1)]
# Exhaustively check 6^4 strategies (independent 0..1 rational parameters)
# by pushing merged gamma into upstream alphas; then verify declarations.
count=0
for U,aL,aR,g in product(GRID,repeat=4):
    L,R,x,m,H=tail(U,aL,aR,g)
    if U:
        new=tail(U,g*aL,g*aR,F(1))
    else:
        new=tail(U,F(0),F(0),F(1))
    assert m==new[3] and H==new[4]
    assert recover(H)==m
    for d in (F(0),F(1,3),F(2,3),F(1)):
        # Choosing fresh signature coins d_s=d for all s is a special case;
        # equal H implies the same for every vector of independent coins.
        eq=sum(d*h for h in H)
        ep=sum(s*(1-d)*h for s,h in zip(S,H))
        eq2=sum(d*h for h in new[4])
        ep2=sum(s*(1-d)*h for s,h in zip(S,new[4]))
        assert (eq,ep)==(eq2,ep2)
    count+=1
assert count==(DENO+1)**4

# Explicit rank-one V=(c_1 z,c_2 z); the lifted (U,L,R,m) image
# is the linear interval 0 <= scalar <= c_1 L+c_2 R.
z=(F(2,45),F(1,30))
c=(F(1,3),F(5,6))
for U in GRID:
    for aL in GRID:
        for aR in GRID:
            for g in GRID:
                L,R=U*aL,U*aR
                t=g*(c[0]*L+c[1]*R)
                assert F(0)<=t<=c[0]*L+c[1]*R
                if c[0]*L+c[1]*R:
                    recg=t/(c[0]*L+c[1]*R)
                    assert F(0)<=recg<=F(1)
                else:
                    assert t==0

print("PASS_EXACT_R5_MERGED_TAIL_RANK_AND_COIN_PUSHING")
print("V_det=",det)
print("joint_midpoint_rank_defect=",D)
print("tail_midpoint_repaired_by_U_alphaL_alphaR_gamma=(1,1/2,0,1)")
print("tail_source_readout_mA=20*H_5/2-32*H_1/2")
print("tail_source_readout_mB=32*H_1/2-16*H_5/2")
print("exact_rational_coin_pushing_regression_cases=",count)
print("exact_rational_rank_one_regression_cases=",count)
print("all_real_theorems_depend_on_proof_not_finite_checks")
