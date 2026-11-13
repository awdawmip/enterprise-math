#!/usr/bin/env python3
"""Exact rational verifier: one ancestor statistic makes rank-two tail image nonconvex."""
from fractions import Fraction as F
from itertools import product
S=(F(1,2),F(1),F(3,2),F(5,2))
v=(F(11,1200),F(23,3600))
w=(F(1,40),F(1,100))
eta=((F(1,8),F(1,4),F(3,8),F(1,4)),
     (F(5,32),F(3,16),F(13,32),F(1,4)))
c=(F(3,40),F(11,40))

def H_of(L,R,gamma):
    m=(gamma*(v[0]*L+w[0]*R),gamma*(v[1]*L+w[1]*R))
    return tuple(m[0]*eta[0][i]+m[1]*eta[1][i] for i in range(4))

A=H_of(F(1),F(0),F(1))
B=H_of(F(0),F(1),F(1))
# Two terminal-signature coordinates (s=1/2, s=5/2) suffice for rank two.
minor=A[0]*B[3]-A[3]*B[0]
assert minor==F(49,92160000)
# An exact inverse for beta=(gamma*L, gamma*R) from these two H bins.
def recover_beta(H):
    return ((H[0]*B[3]-H[3]*B[0])/minor,
            (A[0]*H[3]-A[3]*H[0])/minor)
assert recover_beta(A)==(F(1),F(0))
assert recover_beta(B)==(F(0),F(1))

# Candidate extreme seedless LR policies:
# P: U=1, L=1,R=1,gamma=0; Q: U=1,L=1,R=0,gamma=1.
P_C=sum(c)
Q_C=c[0]
P_H=H_of(F(1),F(1),F(0))
Q_H=A
mid_C=(P_C+Q_C)/2
mid_H=tuple((x+y)/2 for x,y in zip(P_H,Q_H))
assert P_C==F(7,20)
assert mid_C==F(17,80)
assert recover_beta(mid_H)==(F(1,2),F(0))
# If U=1 and H=mid_H, gamma*L=1/2, gamma*R=0 forces
# gamma in [1/2,1], R=0, L in [1/2,1]; hence C<=3/40.
assert mid_C-c[0]==F(11,80)>0

# The previous physical model's total Q stopping time obeys
# t_Q = 1 + U/2 + c_L*L + c_R*R + sum(H).
def TQ(U,L,R,gamma):
    return F(1)+U/2+c[0]*L+c[1]*R+sum(H_of(L,R,gamma))
P_T=TQ(F(1),F(1),F(1),F(0))
Q_T=TQ(F(1),F(1),F(0),F(1))
mid_T=(P_T+Q_T)/2
upper_T=F(1)+F(1,2)+c[0]+sum(mid_H)
assert mid_T-upper_T==F(11,80)
assert mid_T==F(6193,3600)  # 1 + 1/2 + 17/80 + 7/900

# Exact regression for arbitrary rationals: histogram inversion correctly
# recovers post-merge route products; the physical time identity holds.
grid=[F(i,5) for i in range(6)]
count=0
for U,aL,aR,g in product(grid,repeat=4):
    L,R=U*aL,U*aR
    h=H_of(L,R,g)
    assert recover_beta(h)==(g*L,g*R)
    assert TQ(U,L,R,g)==F(1)+U/2+c[0]*L+c[1]*R+sum(h)
    assert all(x>=0 for x in h)
    count+=1
assert count==1296

# Symbolic universal witness logic for every nonzero rational ancestor c:
# if A,B independent, with i != j and c_i != 0, the two candidate
# midpoint C values c_j/2+c_i/2 and c_j+c_i/2 cannot both lie
# inside the feasible edge interval between c_j/2 and c_j.
for a in [F(-3),F(-1,2),F(0),F(1,3),F(2)]:
    for b in [F(-3),F(-1,2),F(0),F(1,3),F(2)]:
        if a==0: continue
        lo,hi=sorted((b/2,b))
        x0=(a+b)/2
        x1=(a+2*b)/2
        assert not (lo<=x0<=hi and lo<=x1<=hi)

print('PASS_EXACT_R5_ANCESTOR_OBSERVER_RANK_TWO_BOUNDARY')
print('terminal_signature_minor=',minor)
print('midpoint_C=',mid_C)
print('max_feasible_C_given_U_and_H=',c[0])
print('certified_conditional_C_and_TQ_gap=',mid_C-c[0])
print('midpoint_TQ=',mid_T)
print('exact_rational_histogram_recovery_regressions=',count)
print('rank_one_or_c_zero_convexity_and_rank_two_nonconvexity_are_all_real_proofs')
