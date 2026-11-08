#!/usr/bin/env python3
"""Exact 9-edge all-real negative residual corner R5 proof checker."""
from fractions import Fraction as F
from VERIFY import mass,tp,tq,R

def xsrc(t):return (F(1),t,F(1),F(13,40)*t+F(1,80),F(9,40),F(0),F(0))
def ytgt(t):
 return (F(1)-F(15744,274955)*t,F(287406,274955)*t,F(1)-F(60856,274955)*t,
         F(1,80)+F(74117,219964)*t,F(9,40)+F(15048,274955)*t,
         F(172901,2199640)*t,F(143703,1374775)*t)
def transport(t):
 E={
   (0,0):(13234*t+7209)/72000,
   (0,2):F(28195,1979676)*t,
   (2,2):(54991-60630*t)/109982,
   (3,2):F(73307,1979676)*t,
   (3,3):(8566*t+1591)/36000,
   (4,5):F(22556,274955)*t,
   (5,5):(1154811-256510*t)/4399280,
   (6,5):F(5639,109982)*t,
   (6,6):(234*t+6709)/72000
 }
 return [[E.get((i,j),F(0)) for j in range(7)] for i in range(7)]

def lawful(y):
 g,a,b,u,v,w,z=y
 return (0<=a<=g<=1 and 0<=b<=g and 0<=u<=F(13,40)*a+b/80 and
   0<=w<=F(3,40)*a+F(21,80)*b and 0<=z<=a/10 and 0<=v-z<=F(9,40)*b)

def check(t):
 x,y=xsrc(t),ytgt(t); q=transport(t)
 assert lawful(x) and lawful(y)
 assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])
 assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
 assert all(v>=0 for row in q for v in row)
 mx,my=mass(x),mass(y)
 assert sum(mx)==sum(my)==1
 assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==1
 assert all(sum(q[i])==my[i] for i in range(7))
 assert all(sum(q[i][j] for i in range(7))==mx[j] for j in range(7))
 assert all(sum(R[i]*q[i][j] for i in range(7))==R[j]*mx[j] for j in range(7))
 assert tp(x)==tp(y) and tq(x)==tq(y)
 return x,y,q

# Every quantity above is affine in t (and F is a linear face), so the
# endpoint checks plus nonnegativity at both endpoints are an all-real proof.
for t in [F(0),F(1,5)]:check(t)
print('PASS_TWO_EXACT_NEGATIVE_CORNER_ENDPOINT_TRANSPORTS')
for i in range(101):check(F(i,500))
print('PASS_101_EXACT_NEGATIVE_CORNER_RATIONAL_REGRESSIONS')
print('PASS_ALL_REAL_NEGATIVE_RESIDUAL_CORNER_0_TO_1_OVER_5_AFFINE_F_FACE')
