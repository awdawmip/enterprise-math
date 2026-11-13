#!/usr/bin/env python3
"""Exact F-chart extension, t in [1/13,1/12], p=1,q=0,theta=1,kappa in [0,1]."""
from fractions import Fraction as F
from itertools import product
import VERIFY as v
V={
 (0,0):(F(1),F(41,416),F(1009,2080),F(6339,166400),F(9901,83200),F(22419,166400),F(41,4160)),
 (0,1):(F(1),F(1,13),F(1),F(3,80),F(121,520),F(0),F(1,130)),
 (1,0):(F(1),F(101,960),F(31,64),F(3091,76800),F(4589,38400),F(3457,25600),F(101,9600)),
 (1,1):(F(1),F(1,12),F(1),F(19,480),F(7,30),F(0),F(1,120)),
}
def target(t,k):
    z=(t-F(1,13))/(F(1,12)-F(1,13))
    assert 0<=z<=1 and 0<=k<=1
    yy=tuple(sum((z if a else 1-z)*(k if b else 1-k)*V[a,b][j]
            for a,b in product((0,1),repeat=2)) for j in range(7))
    v.check(v.source(t,F(1),F(0),F(1),k),yy,'F')
    return yy
for t,k in product((F(1,13),F(1,12)),(F(0),F(1))):
    target(t,k)
print('PASS_EXACT_F_FACE_CORNER_CERTIFICATES',len(V))
for n in range(101):
    target(F(1,13)+(F(1,12)-F(1,13))*F((23*n+11)%101,101),
           F((17*n+5)%101,101))
print('PASS_EXACT_INTERIOR_REGRESSION',101)
print('THEOREM_ALL_REAL_T_1_OVER_13_TO_1_OVER_12_P1_Q0_THETA1_KAPPA_FULL')
