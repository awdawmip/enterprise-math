#!/usr/bin/env python3
"""Exact Fraction certificate for S23's tagged AV binary-hypothesis comparison.
All arithmetic uses Fraction; continuum conclusion comes from affine sign regions
proved in PROOF.md, with exact endpoint/interior checks as a regression witness.
"""
from fractions import Fraction as F
from itertools import pairwise

half = F(1, 2)
quarter = F(1, 4)

def rows(a, b, c):
    au = (a, (1-a)*b, (1-a)*(1-b)/2, (1-a)*(1-b)/2)
    av = (a, F(0), (1-a)*c, (1-a)*(1-c))
    bu = (quarter, 3*b/4, 3*(1-b)/8, 3*(1-b)/8)
    bv = (quarter,)*4
    return (au, au, av, bu, bu, bv)

def tv(P, Q):
    return sum((abs(x-y) for x,y in zip(P,Q)), F(0))/2

minus = (half, F(1,8), half)
plus = (half, F(1,8), F(7,8))
P0, P1 = rows(*minus), rows(*plus)
assert all(sum(row)==1 and min(row)>=0 for row in P0+P1)
assert all(P0[i] == P1[i] for i in [0,1,3,4,5])
A0, A1 = P0[2], P1[2]
assert A0 == (F(1,2), F(0), F(1,4), F(1,4))
assert A1 == (F(1,2), F(0), F(7,16), F(1,16))
B0, B1 = (A0[2], 1-A0[2]), (A1[2], 1-A1[2])
assert B0 == (F(1,4), F(3,4))
assert B1 == (F(7,16), F(9,16))
assert tv(A0,A1) == tv(B0,B1) == F(3,16)

def risk(P,Q,t):
    return sum((min((1-t)*x, t*y) for x,y in zip(P,Q)),F(0))

def claimed_gap(t):
    if t <= F(1,2): return F(0)
    if t <= F(4,7): return t-F(1,2)
    if t <= F(4,5): return (4-5*t)/16
    return F(0)

points = (F(0), F(4,11), F(1,2), F(4,7), F(4,5), F(1))
checks = list(points)+[(x+y)/2 for x,y in pairwise(points)]
for t in checks:
    assert risk(B0,B1,t)-risk(A0,A1,t) == claimed_gap(t), (t,risk(B0,B1,t),risk(A0,A1,t),claimed_gap(t))
assert risk(A0,A1,F(1,2)) == risk(B0,B1,F(1,2)) == F(13,32)
assert risk(B0,B1,F(4,7)) == F(3,7)
assert risk(A0,A1,F(4,7)) == F(5,14)
assert claimed_gap(F(4,7)) == F(1,14)
# Reverse kernel contradiction: for output AV stop3, two distinct input tag probabilities
# force K(yes,stop3)=1 and K(no,stop3)=0; since both AV stop1 masses
# equal 1/2, they simultaneously force K(yes,stop1)=K(no,stop1)=1/2,
# incompatible with stochastic row sum for yes.
assert B0[0] != B1[0] and A0[2] == B0[0] and A1[2] == B1[0]
assert A0[0] == A1[0] == F(1,2)
assert F(1)+F(1,2)>1
print('FROZEN_SOURCE_PIN=43ec6098b1330ae86d0a7863be336c5d97f6ef34')
print('HYPOTHESES=(1/2,1/8,1/2) vs (1/2,1/8,7/8)')
print('FULL_AV_TV=3/16')
print('TAGGED_BERNOULLI_TV=3/16')
print('EQUAL_PRIOR_BOTH_BAYES_RISK=13/32')
print(f'EXACT_RISK_GRID_CHECKS={len(checks)}')
print('MAX_PRIOR_BAYES_RISK_GAP=1/14 at prior_plus=4/7')
print('NO_HYPOTHESIS_INDEPENDENT_REVERSE_MARKOV_KERNEL=PROVED_BY_ROW_CONTRADICTION')
print('PASS_S23_TAGGED_BINARY_TV_BLACKWELL_SEPARATION_EXACT_20261106')
