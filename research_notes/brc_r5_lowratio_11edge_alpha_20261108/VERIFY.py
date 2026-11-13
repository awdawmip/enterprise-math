#!/usr/bin/env python3
"""Exact rational certificate for low-ratio eleven-edge R5 Blackwell lift.
All-real identities: each equation, after multiplication by t+2, is a
polynomial of degree <=2, verified at 3 distinct exact rational values.
Nonnegativity is certified by explicit decreasing quadratic inequalities.
"""
from fractions import Fraction as F
R=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
def source(t):
    return (F(1),t,F(1),F(0),t/10,F(3,40)*t+F(21,80),t/10)
def target(t):
    a=t/(4*(t+2));u=7*t*(4*t+7)/(160*(t+2))
    z=t*t/(20*(t+2));v=z+9*t/20
    w=3*(15*t+28)/(160*(t+2))
    return (F(1),a,F(1),u,v,w,z)
def kernel(t):
    E={
      (0,0):(1934*t+189)/72000,
      (0,1):19*t*(257*t+466)/(18000*(t+2)),
      (1,1):(2250-55477*t-34229*t*t)/(90000*(t+2)),
      (1,2):t*(18479*t+36352)/(90000*(t+2)),
      (2,1):19*t*(257*t+466)/(11250*(t+2)),
      (2,2):(45000-58852*t-40979*t*t)/(45000*(t+2)),
      (2,3):t*(2383*t+4479)/(5000*(t+2)),
      (3,2):t*(18479*t+36352)/(90000*(t+2)),
      (3,3):(121110-116819*t-95288*t*t)/(180000*(t+2)),
      (6,3):t*(2383*t+4479)/(18000*(t+2)),
      (6,6):(4934*t+10689)/72000
    }
    return [[E.get((i,j),F(0)) for j in range(7)] for i in range(7)]
def mass(f):
    g,a,b,u,v,w,z=f
    return (
      F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
      F(13,40)*a+b/80-u,(g-a)/2,
      1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
      (g-b)/2,F(3,40)*a+F(21,80)*b-w,
      u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w
    )
def tp(f):
    g,a,b,u,v,w,z=f
    return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w
def tq(f):
    g,a,b,u,v,w,z=f
    return 1+g+(a+b)/2+u+v+w
def check_equalities(t):
    x,y=source(t),target(t)
    mx,my=mass(x),mass(y);Q=kernel(t)
    assert sum(mx)==sum(my)==1
    assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==1
    assert all(sum(Q[i])==my[i] for i in range(7))
    assert all(sum(Q[i][j] for i in range(7))==mx[j] for j in range(7))
    assert all(sum(R[i]*Q[i][j] for i in range(7))==R[j]*mx[j] for j in range(7))
    assert tp(x)==tp(y) and tq(x)==tq(y)
    assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])
    return Q
# All algebraic equations have denominator dividing a constant times
# (t+2), with degree <=2 numerators after clearing this denominator.
for t in (F(0),F(1,52),F(1,26)):
    check_equalities(t)
print("PASS_ALL_7x7_CALIBRATION_IDENTITIES_BY_THREE_POINT_DEGREE_TWO_CERTIFICATE")
# On t>=0 these numerator polynomials are decreasing. N1 vanishes
# at alpha=(sqrt(3385758529)-55477)/68458; alpha in (1/26,1/25).
# All other possibly negative numerators stay positive even at 1/25.
lo,hi=F(1,26),F(1,25)
N1=lambda t:2250-55477*t-34229*t*t
assert N1(lo)>0 and N1(hi)<0
for f in (lambda t:45000-58852*t-40979*t*t,
          lambda t:121110-116819*t-95288*t*t,
          lambda t:4-34*t-28*t*t):
    assert f(hi)>0
assert 1-2*hi>0
print("PASS_ALL_REAL_NONNEGATIVITY_TO_EXACT_QUADRATIC_ROOT")
for k in range(101):
    t=F(k,2600)
    Q=check_equalities(t)
    assert all(v>=0 for row in Q for v in row)
    g,a,b,u,v,w,z=target(t)
    assert 0<=g<=1 and 0<=a<=g and 0<=b<=g
    assert 0<=u<=F(13,40)*a+b/80 and 0<=w<=F(3,40)*a+F(21,80)*b
    assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
print("PASS_101_EXACT_RATIONAL_IMPLEMENTATION_REGRESSIONS")
print("PASS_R5_LOW_RATIO_POSITIVE_RESIDUAL_ELEVEN_EDGE_ALL_REAL_LIFT")
