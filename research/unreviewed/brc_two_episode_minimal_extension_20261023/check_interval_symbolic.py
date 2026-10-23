#!/usr/bin/env python3
"""Exact symbolic boundary certificate for the four-label auxiliary BRC observer.
Run: python check_interval_symbolic.py (requires sympy). Author-side unreviewed.
"""
from sympy import symbols, Rational, factor, sqrt

z = symbols("z", real=True)
q = {
    "0":(0,(1+z)/3,(1-z)/3,Rational(1,3)),
    "2":(Rational(1,3),Rational(1,3),0,Rational(1,3)),
    "N":(0,Rational(1,4),0,Rational(3,4)),
}
good = ((0,1),(1,2),(1,3),(2,3))
word = "0N20NN"

def delta(prefix):
    out = 0
    for i,j in good:
        a=b=c=1
        for char in prefix:
            p=q[char]
            a*=p[i]+p[j]
            b*=p[i]
            c*=p[j]
        out+=a-b-c
    return factor(out)

ds=[delta(word[:i]) for i in range(1,7)]
expected=[
    0,(8-z)/12,(4*z+17)/36,
    (10*z*z+18*z+41)/108,
    (40*z*z+90*z+149)/432,
    (154*z*z+402*z+569)/1728,
]
assert all(factor(a-b)==0 for a,b in zip(ds,expected))
incs=[factor(ds[i]-ds[i-1]) for i in range(2,6)]
expected_incs=[
    7*(z-1)/36,
    (5*z*z+3*z-5)/54,
    (6*z-5)/144,
    (-2*z*z+14*z-9)/576,
]
assert all(factor(a-b)==0 for a,b in zip(incs,expected_incs))
t=Rational(5,6)
values=[factor((ds[1]-ds[i]).subs(z,t)) for i in range(2,6)]
assert values==[
    Rational(7,216), Rational(7,486),
    Rational(7,486), Rational(379,31104),
]
assert factor((5*z*z+3*z-5).subs(z,Rational(11,15)))==-Rational(1,9)
assert factor((-2*z*z+14*z-9).subs(z,Rational(11,15)))==Rational(43,225)
alpha=(sqrt(109)-3)/10
assert Rational(11,15)<alpha<Rational(3,4)
print("PASS exact interval formulae and boundary certificates",alpha)
