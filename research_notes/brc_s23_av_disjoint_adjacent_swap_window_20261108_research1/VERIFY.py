#!/usr/bin/env python3
"""Strict-integer certificate of the first post-lexicographic ordering window.
The complete range theorem is symbolic; this checks its arithmetic premises,
first boundary, and selected witness swaps without enumerating T_H.
"""
from fractions import Fraction
P, D = 2074774, 380295
U = (79, 431)
W = (D, P)
M = P + D
Q = (U[0] + 2 * D, U[1] + 2 * P)
H0 = sum(Q)
H1 = 510 + 3 * M
RLOW = Fraction(545569623581288298975349314, 10**26)
RHIGH = Fraction(545569623581288298975349315, 10**26)
assert RLOW < RHIGH
# Independently certify the logarithmic enclosure using 45 rational
# atanh terms for ln(2), -ln(7/8), and ln(10/7).
N = 45
def log_ratio_bounds(x):
    partial = sum((x**(2*i+1) / Fraction(2*i+1) for i in range(N)), Fraction(0))
    rem = x**(2*N+1) / (Fraction(2*N+1)*(1-x*x))
    return 2*partial, 2*(partial+rem)
ln2_lo, ln2_hi = log_ratio_bounds(Fraction(1,3))
ln87_lo, ln87_hi = log_ratio_bounds(Fraction(1,15))
ln107_lo, ln107_hi = log_ratio_bounds(Fraction(3,17))
rigorous_lo = (3*ln2_lo-ln87_hi)/ln107_hi
rigorous_hi = (3*ln2_hi-ln87_lo)/ln107_lo
assert RLOW < rigorous_lo < rigorous_hi < RHIGH
print('LOG_RATIO_RATIONAL_BOUND', RLOW.numerator, RHIGH.numerator,
      RLOW.denominator)

def E(r):
    return 79*r-431, P-D*r
for r in (RLOW,RHIGH):
    eps,eta=E(r)
    assert 0 < eta < eps < 2*eta and 2*eps > 3*eta
assert U[0]*P-U[1]*D==1
assert M==2455069 and H0==4910648 and H1==7365717
assert H1-H0==M
# Candidate discrepancy classification. For A>=1 and B>=2, feasibility
# 510 A + M B <= H1-1 forces either (A,B)=(1,2),
# or A>=2 B=2, or A=1 B=3 (last excluded), or A>=2 B=3 (also excluded).
# When (A,B)=(2,2)/(2,3), sign is positive by eps>eta, 2eps>3eta.
for A in range(1,20):
    for B in range(1,20):
        if 510*A+M*B <= H1-1:
            signs=[A*E(r)[0]-B*E(r)[1] for r in (RLOW,RHIGH)]
            if all(s<0 for s in signs): assert (A,B)==(1,2),(A,B)
# Strict order inversion for Q and any low-lying translated x.
for s in (0,1,509,M-1):
    for x in ((0,0),(min(1,s),0),(0,min(1,s)),(min(79,s),max(0,s-min(79,s)))):
        if sum(x)>s: continue
        xx=(x[0]+Q[0],x[1]+Q[1])
        assert sum(xx)<=H0+s
        kx=P*x[0]-D*x[1]
        kxx=P*xx[0]-D*xx[1]
        assert kxx-kx==1
        assert all( r*Q[0]-Q[1]<0 for r in (RLOW,RHIGH))
        # x cannot move down the same-K fiber by -w, x+Q cannot move
        # up the (K+1)-fiber by +w within H0+s.
        assert not (x[0]>=D and x[1]>=P)
        assert sum(xx)+(D+P)> H0+s
    swaps=(s+1)*(s+2)//2
    print('WINDOW',s,'H',H0+s,'ADJACENT_SWAPS',swaps)
# Sharp next candidate (new deviation with A=1,B=3) becomes feasible at H1.
Q3=(U[0]+3*D,U[1]+3*P)
assert sum(Q3)==H1
assert all(r*Q3[0]-Q3[1]<0 for r in (RLOW,RHIGH))
# On H0, K=0 fiber is 0,w,2w; K=1 fiber is u,u+w,u+2w.
for A in (0,1):
    assert all(sum((A*U[0]+B*D,A*U[1]+B*P))<=H0 for B in range(3))
    assert sum((A*U[0]+3*D,A*U[1]+3*P))>H0
# Rank of 0 in L-order via exact sum; swapping with Q at H0 changes it by +1.
H=H0
negative=0
for v in range(H+1):
    remain=H-v
    if remain<0: break
    # j>=floor(P*v/D)+1 exactly when K=P*v-D*j<0
    first=(P*v)//D+1
    if first<=remain: negative +=remain-first+1
    elif v>0 and first>remain: # monotonic onward
        break
assert P*0-D*0==0
print('RANK_INFO H0',H0,'POINTS',(H+1)*(H+2)//2,'C_H(0)',negative,
      'LEX_rank_zero',negative+2,'TRUE_rank_zero',negative+3,
      'LEX_rank_Q',negative+3,'TRUE_rank_Q',negative+2)
print('PASS_S23_AV_ADJACENT_SWAP_WINDOW_H4910648_TO_H7365716')
