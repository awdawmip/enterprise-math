#!/usr/bin/env python3
"""Exact 59-node BRC certification; standard library only.
Uses the prior 47 exact prices (PR #2591), adds 12 independently
certified new prices. Does NOT regenerate Bellman witnesses.
"""
from fractions import Fraction as F
from math import isqrt
K=lambda x: F(7557)-169*x
G=lambda x: F(310)*(3-x)/K(x)
old=list(map(F,"1 25/24 13/12 9/8 7/6 29/24 5/4 31/24 4/3 11/8 17/12 35/24 3/2 25/16 13/8 27/16 7/4 29/16 15/8 31/16 2 33/16 17/8 35/16 9/4 73/32 37/16 75/32 19/8 77/32 39/16 79/32 5/2 61/24 31/12 21/8 8/3 65/24 11/4 67/24 17/6 23/8 93/32 47/16 95/32 191/64 3".split()))
added=[F(n,32) for n in range(49,72,2)]
new=sorted(set(old+added))
assert len(old)==47 and len(new)==59 and old==sorted(old)
assert all(0<=G(x)<F(620,3299) for x in new)
area=lambda v:sum(((b-a)*(G(a)-G(b)) for a,b in zip(v,v[1:])),F(0))
S0,S1=area(old),area(new)
assert S0==F(5959469197718386554712955,1505500161665693064580080288)
assert S1==F(469038291667513006195,157330981467832904648352)
assert 1-S1/2==F(314192924643998296290509,314661962935665809296704)
gain=0
for x in added:
 a=max(p for p in old if p<x);b=min(p for p in old if p>x)
 d=F(2185500)*(x-a)*(b-x)/K(x)*(1/K(a)+1/K(b))
 gain+=d
assert gain==S0-S1==F(182125,186365844)
scale=10**24
def roots(z):
 n=isqrt(z.numerator*scale**2//z.denominator)
 lo,hi=F(n,scale),F(n+1,scale)
 assert lo**2<=z<hi**2
 return lo,hi
def bounds(a,b):
 la,ha=roots(K(a));lb,hb=roots(K(b))
 return F(50)*(b-a)/(ha+hb)**2,F(50)*(b-a)/(la+lb)**2
bounds_all=[(a,b,*bounds(a,b)) for a,b in zip(new,new[1:])]
winner=max(bounds_all,key=lambda x:x[2])
assert winner[:2]==(F(17,6),F(23,8))
assert all(winner[2]>c[3] for c in bounds_all if c is not winner)
assert winner[3] < F(73619708725015,10**18)
print("59NODE_EXACT_PASS",len(bounds_all),"certified_area",1-S1/2,"gain",gain)
print("max_interval",winner[:2],"rigorous_max_regret_over_t",winner[2:])
