#!/usr/bin/env python3
"""Exact rational checker for the frozen R5 signed low-key support plane.

An affine identity checked on origin plus seven coordinate vectors is exact
for all real flow variables; rational examples exercise the attainability flow.
"""
from fractions import Fraction as F

R = (F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
ZERO = F(0)


def model(g,a,b,u,v,w,z, legal=True):
    c0 = F(13,40)*a+b/80
    c1 = a/10+F(9,40)*b
    c2 = F(3,40)*a+F(21,80)*b
    tp = 1+g+(3*a+5*b)/8+u/2+v+F(3,2)*w
    tq = 1+g+(a+b)/2+u+v+w
    m0 = F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100
    m6 = u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w
    mass = (m0,c0-u,(g-a)/2,
            1-g+c1-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,c2-w,m6)
    pos = F(9,10)*mass[0] + mass[1]/2 + mass[2]/4
    upper = F(13269,53000)+F(391,6625)*(tp-F(31,10))+F(364,6625)*(tq-F(31,10))
    slack = (1-g,u,c1-v,w,F(9,40)*b-v+z)
    dual = sum((x*y for x,y in zip(
        (F(117,10600),F(3999,53000),F(1283,10600),F(7127,53000),F(247,1800)),slack)),ZERO)
    assert upper-pos == dual
    if legal:
        assert ZERO <= a <= g <= 1 and ZERO <= b <= g
        assert ZERO <= u <= c0 and ZERO <= v <= c1 and ZERO <= w <= c2
        assert ZERO <= z <= a/10 and ZERO <= v-z <= F(9,40)*b
        assert all(x>=ZERO for x in mass)
        assert sum(mass,ZERO)==1
        assert sum((x*y for x,y in zip(R,mass)),ZERO)==1
        assert dual >= 0
    return tp,tq,mass,pos,upper,dual


# Exact affine certificate, evaluated on an affine spanning set.
model(*(ZERO,)*7,legal=False)
for j in range(7):
    x=[ZERO]*7
    x[j]=F(1)
    model(*x,legal=False)
print('PASS_EXACT_AFFINE_IDENTITY_EIGHT_BASIS_POINTS')

# Analytic one-parameter equality family: 0<=r<=1, 2<=t<=133/40.
for i in range(54):
    r=F(i,53)
    flow=(F(1),r,r,ZERO,F(13,40)*r,ZERO,r/10)
    tp,tq,mm,obj,bound,dual=model(*flow)
    assert tp==tq==2+F(53,40)*r
    assert dual==0 and obj==bound==F(1,8)+F(151,1000)*r
    assert mm == (F(143,1200)*r,F(27,80)*r,(1-r)/2,
                  F(13,150)*r,(1-r)/2,F(27,80)*r,F(143,1200)*r)
    assert F(9,1)*flow[-1]*flow[2] == F(4,1)*flow[1]*(flow[4]-flow[-1])
print('PASS_54_RATIONAL_EQUALITY_FLOWS_SEEDLESS_AND_MOMENTS')

# Every seven-key declaration vector obeys the observer-level support plane.
flow=(F(1),F(44,53),F(44,53),ZERO,F(143,530),ZERO,F(22,265))
tp,tq,m,objective,upper,dual=model(*flow)
assert tp==tq==F(31,10) and objective==upper==F(13269,53000)
assert m==(F(1573,15900),F(297,1060),F(9,106),F(286,3975),
           F(9,106),F(297,1060),F(1573,15900))
assert sum(m[j] for j in (0,1,2))==F(3689,7950)
assert sum(R[j]*m[j] for j in (0,1,2))==F(641,3000)
assert F(1)-F(641,3000)==F(2359,3000)
for k in range(128):
    e=tuple(m[j]*F((k*(j+1)+3*j)%13,12) for j in range(7))
    # each declaration is in [0,M_j] by construction
    assert all(ZERO<=e[j]<=m[j] for j in range(7))
    eQ=sum(e,ZERO)
    eP=1-sum((R[j]*e[j] for j in range(7)),ZERO)
    assert eP+eQ-1<=upper
print('PASS_128_SEVEN_KEY_DECLARATION_TESTS_AND_EXACT_OPTIMAL_OBSERVER')
print('SHARP_OBSERVER', 'eP=2359/3000', 'eQ=3689/7950', 'TP=TQ=31/10')
print('PASS_EXACT_R5_SIGNED_ERROR_ALL_SEVEN_KEYS_SHARP_REAL_INTERVAL')
