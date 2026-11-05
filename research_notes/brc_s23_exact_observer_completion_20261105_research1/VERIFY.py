#!/usr/bin/env python3
"""Exact Fraction certificate for frozen six-source S23 observer completion."""
from fractions import Fraction as F
from itertools import product, combinations
A=(F(1,2), F(7,8)); B=(F(1,8),F(1,2)); C=(F(1,2),F(7,8))
def law(a,b,c):
    au=(a,(1-a)*b,(1-a)*(1-b)/2,(1-a)*(1-b)/2)
    av=(a,F(0), (1-a)*c,(1-a)*(1-c))
    bu=(F(1,4),3*b/4,3*(1-b)/8,3*(1-b)/8)
    bv=(F(1,4),)*4
    return (au,au,av,bu,bu,bv)
def obs(a,b,c):
    return (a,(1-a)*(1-b),3*b/4,(1-a)*c)
def tv(x,y): return sum((abs(s-t) for s,t in zip(x,y)),F(0))/2
def D(p,q): return max(tv(x,y) for x,y in zip(p,q))
def d_formula(x,y):
    da=x[0]-y[0]; dq=x[1]-y[1]; dr=x[2]-y[2]; dw=x[3]-y[3]
    return max(map(abs,(da,dq,dr,dw,da+dq,da+dw)))
def recover(tags, v):
    d=dict(zip(tags,v))
    if 'a' in d: a=d['a']
    if 'r' in d: b=F(4,3)*d['r']
    if 'a' in d and 'q' in d and 'r' not in d: b=1-d['q']/(1-a)
    if 'a' not in d: a=1-d['q']/(1-b)
    c=d['w']/(1-a)
    return a,b,c
tags=('a','q','r','w')
vertices=list(product(A,B,C))
for x in vertices:
    P=law(*x); O=obs(*x)
    assert all(sum(row)==1 and min(row)>=0 for row in P)
    assert P[2][0]==O[0] and P[0][2]+P[0][3]==O[1]
    assert P[3][1]==O[2] and P[2][2]==O[3]
    assert O[1]==(1-O[0])*(1-F(4,3)*O[2])
for x,y in product(vertices,repeat=2):
    assert D(law(*x),law(*y)) == d_formula(obs(*x),obs(*y))
complete_triples=[]
for sub in combinations(tags,3):
    if 'w' in sub:
        complete_triples.append(''.join(sub))
        for theta in vertices:
            z=recover(sub, [dict(zip(tags,obs(*theta)))[k] for k in sub])
            assert z==theta
assert complete_triples==['aqw','arw','qrw']
x=(F(1,2),F(1,8),F(1,2));y=(F(1,2),F(1,8),F(7,8))
assert obs(*x)[:3]==obs(*y)[:3] and D(law(*x),law(*y))==F(3,16)
for sub in combinations(tags,2):
    if 'w' not in sub:
        p,q=x,y
    elif sub==('a','w'):
        p=(F(1,2),F(1,8),F(1,2));q=(F(1,2),F(1,2),F(1,2))
    elif sub==('q','w'):
        p=(F(1,2),F(1,2),F(1,2));q=(F(2,3),F(1,4),F(3,4))
    elif sub==('r','w'):
        p=(F(1,2),F(1,4),F(1,2));q=(F(2,3),F(1,4),F(3,4))
    else: raise RuntimeError(sub)
    v1=dict(zip(tags,obs(*p)));v2=dict(zip(tags,obs(*q)))
    assert all(v1[t]==v2[t] for t in sub) and D(law(*p),law(*q))>0
cstar=F(11,16)
for a,b,c in vertices:
    center=law(a,b,cstar)
    assert D(law(a,b,c),center)==(1-a)*abs(c-cstar)
    assert D(law(a,b,c),center)<=F(3,32)
assert D(law(F(1,2),F(1,8),F(1,2)),law(F(1,2),F(1,8),F(7,8))) == F(3,16)
assert (F(3,16)/2)==F(3,32)
print('SOURCE_VERTICES=8')
print('PAIRWISE_METRIC_EQUALITIES=64')
print('COMPLETE_THREE_TAG_SETS=aqw,arw,qrw')
print('INCOMPLETE_THREE_TAG_SET=aqr')
print('INCOMPLETE_TWO_TAG_SETS=6')
print('ORIGINAL_TRIPLE_FIBER_DIAMETER=3/16')
print('OPTIMAL_FULL_SOURCE_RECONSTRUCTION_RADIUS_FROM_AQR=3/32')
print('MIDPOINT_RECONSTRUCTION_ENDPOINT_CHECKS=8')
print('PASS_S23_EXACT_OBSERVER_COMPLETION_20261105')
