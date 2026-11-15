#!/usr/bin/env python3
"""Exact signed-Z6 native-vs-two-axis shell checker; NOT original R063 replay."""
from collections import defaultdict
from math import comb, factorial, isqrt

EXPECTED = [(1,12,12,12,12),(2,252,5772,12,12),(3,876,982092,12,12),
            (4,4092,13507212,12,12),(5,7812,2538954612,132,4212),
            (6,18396,438976641612,12,12)]

def direct(r):
    out=[0,0,0,0]
    def visit(i,left,L,denom,s):
        if i == 6:
            if left: return
            b=factorial(L)//denom
            out[0]+=1;out[1]+=b
            if s<=2:out[2]+=1;out[3]+=b
            return
        for a in range(isqrt(left)+1):
            for _ in range(1 if a==0 else 2):
                visit(i+1,left-a*a,L+a,denom*factorial(a),s+(a>0))
    visit(0,r*r,0,1,0)
    return out

def convolution(r):
    dp={(0,0,0):(1,1)}
    for _ in range(6):
        nd=defaultdict(lambda:[0,0])
        for (g,L,s),(cnt,mass) in dp.items():
            for a in range(isqrt(r*r-g)+1):
                row=nd[(g+a*a,L+a,s+(a>0))]
                sg=1 if a==0 else 2
                row[0]+=sg*cnt
                row[1]+=sg*mass*comb(L+a,a)
        dp=nd
    out=[0,0,0,0]
    for (g,L,s),(cnt,mass) in dp.items():
        if g==r*r:
            out[0]+=cnt;out[1]+=mass
            if s<=2:out[2]+=cnt;out[3]+=mass
    return out

for r,c,b,c2,b2 in EXPECTED:
    assert direct(r)==convolution(r)==[c,b,c2,b2], r
assert 252-12==240 and 5772-12==240*24
print('PASS_SHARP_R2_SIGNED_X6_OVER_R063_TWO_AXIS; exact r=1..6')
