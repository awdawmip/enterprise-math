#!/usr/bin/env python3
"""Exact observer-time and hinge-balance identities for frozen seven-node P/Q-BRC."""
from fractions import Fraction as F
R = tuple(map(F,('1/10','1/2','3/4','1','5/4','3/2','19/10')))
C = tuple(map(F,('2','2','31/18','1','5/18','0','0')))

def masses(x):
    g,a,b,u,v,w,z=x
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            F(13,40)*a+b/80-u,(g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def tp(x):
    g,a,b,u,v,w,z=x
    return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w

def tq(x):
    g,a,b,u,v,w,z=x
    return 1+g+(a+b)/2+u+v+w

def hinges(x):
    m=masses(x)
    return tuple(sum(max(F(0),rr-k)*mi for rr,mi in zip(R,m)) for k in R[1:-1])

def lawful(x):
    g,a,b,u,v,w,z=x
    assert 0<=a<=g<=1 and 0<=b<=g
    assert 0<=u<=F(13,40)*a+b/80
    assert 0<=w<=F(3,40)*a+F(21,80)*b
    assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
    m=masses(x)
    assert all(v>=0 for v in m)
    assert sum(m)==sum(rr*vv for rr,vv in zip(R,m))==1

def cobs(x):return sum(cc*mm for cc,mm in zip(C,masses(x)))

zero=(F(0),)*7
basis=[tuple(F(i==j) for i in range(7)) for j in range(7)]
for xx in [zero]+basis:
    assert F(9)*cobs(xx)==F(9)+8*(tp(xx)-tq(xx))
print('PASS_8_EXACT_AFFINE_COEFFICIENT_TESTS_ALL_REAL_C_IDENTITY')

x=tuple(map(F,('1','1/6','1','1/20','29/240','11/160','1/120')))
y=tuple(map(F,('7/8','9/40','5/6','107/1600','21/100','227/1600','9/400')))
lawful(x);lawful(y)
assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])
assert tp(x)==tp(y) and tq(x)==tq(y)
delta=tuple(hi-hj for hi,hj in zip(hinges(y),hinges(x)))
assert all(d>0 for d in delta)
assert 10*delta[0]+16*delta[1]==16*delta[3]+10*delta[4]
assert masses(x)[4]==0 and masses(y)[4]>0
print('PASS_EXACT_PHYSICAL_SOURCE_SEEDLESS_TARGET_ALL_FIVE_STRICT_HINGES')
print('HINGE_GAPS',' '.join(map(str,delta)))
print('TIME_DIFFERENCE',tp(x)-tq(x),'C_OBSERVER',cobs(x))
print('EXACT_SIGNED_HINGE_BALANCE_10D1_PLUS_16D2_EQUALS_16D4_PLUS_10D5')
