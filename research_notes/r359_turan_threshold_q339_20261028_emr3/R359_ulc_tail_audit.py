#!/usr/bin/env python3
"""R359 exact symbolic tail-ULC transition, conditional on R353/R354 formulas."""
import sympy as sp
r=sp.symbols('r',integer=True,positive=True)
A=(17*r+11)/sp.Integer(10)
B=(7803*r**3+2252*r**2-5523*r+3328)/(2700*(2*r-1))
ordinary=sp.factor(A**2-B)
ULC=sp.factor(A**2/(2*r)**2-B/(r*(2*r-1)))
P=172*r**3+2571*r**2-16282*r+3267
assert sp.factor(ordinary-(7803*r**3+10141*r**2+1959*r-6595)/(2700*(2*r-1)))==0
assert sp.factor(ULC-P/(10800*r**2*(2*r-1)**2))==0
assert [int(P.subs(r,k)) for k in range(1,6)]==[-10272,-17637,-17796,-9717,7632]
assert sp.diff(P,r).subs(r,5)==22328
assert sp.expand(sp.diff(P,r,2)-(1032*r+5142))==0
assert ULC.subs(r,1)*900**2==-770400
assert ordinary.subs(r,1)*900**2==2520**2-2620*900
print('PASS: top Turan all r>=1; top ULC fails r1..4, passes r>=5, conditional inherited formulas')
