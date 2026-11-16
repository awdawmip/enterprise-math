#!/usr/bin/env python3
"""Exact rational lift for the full g=a=b cone, built from VERIFY_4D.py."""
from fractions import Fraction as F
from itertools import product
import VERIFY_4D as face
h=face.h
R=face.R
def scaled(s,t,p,q,theta):
    x,y,Q=face.lifted(s,t,p,q)
    x=tuple(theta*v for v in x)
    y=tuple(theta*v for v in y)
    Q=[[theta*Q[i][j]+((1-theta) if (i,j)==(3,3) else F(0))
        for j in range(7)] for i in range(7)]
    return x,y,Q
def check(x,y,Q):
    assert h.legal(x) and h.legal(y)
    assert h.residual(y)==0
    assert y[6]==y[1]/10 and y[4]==y[1]/10+F(9,40)*y[2]
    assert h.times(x)==h.times(y)
    mx,my=h.masses(x),h.masses(y)
    assert sum(mx)==sum(my)==F(1)
    assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==F(1)
    assert all(q>=0 for row in Q for q in row)
    for i in range(7): assert sum(Q[i])==my[i]
    for j in range(7):
        assert sum(Q[i][j] for i in range(7))==mx[j]
        assert sum(R[i]*Q[i][j] for i in range(7))==R[j]*mx[j]
    K=[[Q[i][j]/my[i] if my[i] else F(i==j) for j in range(7)] for i in range(7)]
    assert all(sum(row)==1 for row in K)
    for d in product((F(0),F(1)),repeat=7):
        dp=[sum(K[i][j]*d[j] for j in range(7)) for i in range(7)]
        assert all(F(0)<=v<=F(1) for v in dp)
        assert sum(mx[j]*d[j] for j in range(7))==sum(my[i]*dp[i] for i in range(7))
        assert sum(R[j]*mx[j]*d[j] for j in range(7))==sum(R[i]*my[i]*dp[i] for i in range(7))
for theta in (F(0),F(1,5),F(1,2),F(4,5),F(1)):
    for s,t,p,q in product((F(0),F(1,2),F(1)),repeat=4):
        check(*scaled(s,t,p,q,theta))
    print('RAY_SCALING',theta,'81_EXACT_QUADRUPLES','128_BINARY_DECLARATIONS_EACH')
print('PASS_R5_ALL_REAL_FIVE_PARAMETER_MAXIMAL_EARLY_FLOW_CONE_BLACKWELL_LIFT')
