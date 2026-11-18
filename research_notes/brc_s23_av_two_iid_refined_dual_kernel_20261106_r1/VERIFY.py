#!/usr/bin/env python3
"""Exact rational S23/AV two-iid refined certificates (2026-11-06)."""
from fractions import Fraction as F
from itertools import product
CORNERS=tuple(product((F(1,2),F(7,8)),repeat=2))
POINTS=((F(1,2),F(1,2)),(F(11,16),F(7,8)),(F(23,32),F(7,8)))
WEIGHTS=(F(5983,11967),F(6176,83769),F(11904,27923))
TESTS=((-1,-1,1,-1,0,1,1,1,1),
       (1,1,-1,1,F(4,35),-1,-1,-1,-1),
       (1,1,-1,1,-F(4,189),-1,-1,-1,-1))
D=1000000000
COUNTS=((0,0,0,0,D,0,0,0,0),
        (0,0,0,579190219,0,0,420809781,0,0),
        (0,553921569,66364911,90824631,0,111111111,0,111111111,66666667),
        (753350886,37581699,148315790,26583388,0,0,34168237,0,0))
K=tuple(tuple(F(x,D) for x in row) for row in COUNTS)
LOWER=F(15383,83769)
UPPER=F(387769986271,2048000000000)
n=0
def check(ok,label):
    global n
    assert ok,label
    n+=1
def full(a,c):
    z=(1-a)*c
    return (a,z,1-a-z)
def binary(a,c):
    z=(1-a)*c
    return(z,1-z)
def tensor(a,b):
    return tuple(x*y for x in a for y in b)
def tv(e):
    return sum(map(abs,e))/2
check(sum(WEIGHTS)==1 and all(w>=0 for w in WEIGHTS),'weights')
for v in TESTS:check(len(v)==9 and all(-1<=x<=1 for x in v),'test')
P=[tensor(full(*p),full(*p)) for p in POINTS]
Q=[tensor(binary(*p),binary(*p)) for p in POINTS]
C=sum(WEIGHTS[k]*sum(TESTS[k][j]*P[k][j] for j in range(9)) for k in range(3))
d=[[sum(WEIGHTS[k]*Q[k][r]*TESTS[k][j] for k in range(3)) for j in range(9)] for r in range(4)]
mx=tuple(max(row) for row in d)
check(C/2==F(30773,167538),'dual constant')
check(mx==(F(1,11967),F(0),F(0),F(0)),'dual maxima')
check((C-sum(mx))/2==LOWER,'dual lower')
for row in COUNTS:check(sum(row)==D and min(row)>=0,'stochastic')
def g(i,j):
    pi=tensor(full(*CORNERS[i]),full(*CORNERS[j]))
    pj=tensor(full(*CORNERS[j]),full(*CORNERS[i]))
    qi=tensor(binary(*CORNERS[i]),binary(*CORNERS[j]))
    qj=tensor(binary(*CORNERS[j]),binary(*CORNERS[i]))
    return tuple((pi[t]+pj[t])/2-sum((qi[r]+qj[r])/2*K[r][t] for r in range(4)) for t in range(9))
values=[]
for i in range(4):
    for j in range(i,4):
        val=tv(g(i,j));values.append((i,j,val))
        check(val<=UPPER,'upper corner')
check(max(x[2] for x in values)==UPPER,'upper max')
check(tv(g(3,3))==UPPER,'upper attained')
check(F(1491,8125)<LOWER<=UPPER<F(7573633,40000000),'improvement')
print('PASS_S23_AV_TWO_IID_DUAL_AND_KERNEL_EXACT_20261106_R1')
print('CHECKS',n)
print('FROZEN_SCIENCE','43ec6098b1330ae86d0a7863be336c5d97f6ef34')
print('LOWER',LOWER,'UPPER',UPPER)
print('WEIGHTS',WEIGHTS,'DUAL_HALF_CONSTANT',C/2,'ROW_MAXIMA',mx)
for i,j,val in values:print('CORNER',i,j,val)
