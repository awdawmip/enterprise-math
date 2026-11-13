#!/usr/bin/env python3
"""Exact 16-leaf P/Q evidence for H-strictly-suboptimal BRC BU family.

Explicit policy upper bound holds inside the declared finite model.
Inherited L0/L3 legality and S2->S23 contraction in old lower bound
remain author-side hypotheses requiring independent review.
"""
from collections import defaultdict
from fractions import Fraction as F
import sympy as sp

a,b = F(961,1000),F(151,1000)
E = (a+3*b-1)*(7-a-21*b)/(12*(4*a+12*b+2))
H = b*(2*a-7*b)/(8*(a+2*b))
OLD_LOWER = E+F(1,1500000)
assert E==F(16491,1276000) and H==F(26123,2020800)
assert OLD_LOWER==F(1546111,119625000)

qmass={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
likelihood={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
            'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaves=[(cat,j,l,qmass[cat]/4,qmass[cat]*likelihood[cat][j]/4)
        for cat in ('AU','AV','BU','BV') for j in range(2) for l in range(2)]
assert len(leaves)==16 and all(P>0 and Q>0 for cat,j,l,Q,P in leaves)
assert sum(x[3] for x in leaves)==sum(x[4] for x in leaves)==1
atoms=((1,'Q',0),(2,'Q',0),(3,'P',0),(3,'Q',1))

def observed(law,first,second):
    counts=defaultdict(F)
    for cat,j,l,Q,P in leaves:
        mass=Q if law=='Q' else P
        stage1=first[cat[0]]
        stage2=second[cat]
        z=int(cat=='BU')
        counts[(1,'Q',0)]+=mass*(1-stage1)
        counts[(2,'Q',0)]+=mass*stage1*(1-stage2)
        counts[(3,'Q' if z else 'P',z)]+=mass*stage1*stage2
    assert sum(counts.values())==1
    return tuple(counts[k] for k in atoms)

def TV(x,y): return sum(abs(xi-yi) for xi,yi in zip(x,y))/2

def policy(u):
    A=(1414*u+1033)/(250*(7-2*u))
    B=(961-1414*u)/(500*(7-2*u))
    U=(1+u)*B
    V=B
    return A,B,U,V

def p(u): return 1414*u*u+4091*u-1730

def validate_rational_policy(name,u):
    assert F(865,2526)<=u and p(u)<=0 and u<F(239,638)
    A,B,U,V=policy(u)
    assert 0<u<1 and 0<A<=1 and 0<B<=1 and 0<=U<=A and 0<=V<=B
    first={'A':A,'B':B}
    second={'AU':u,'AV':U/A,'BU':u,'BV':V/B}
    assert all(0<=r<=1 for r in second.values())
    target1={'A':a,'B':b}
    target2={'AU':F(1),'AV':F(0),'BU':F(0),'BV':F(0)}
    h=u*B/4
    for law in ('P','Q'):
        t=observed(law,target1,target2)
        c=observed(law,first,second)
        d=tuple(z-y for z,y in zip(c,t))
        assert sum(d)==0 and d[3]==h
        if law=='P': assert d==(F(0),F(0),-h,h)
        else: assert d[0]<=0 and d[1]<=0 and d[2]==0
        assert TV(t,c)==h
        print('FULL16',name,law,'TV',TV(t,c),'DIFFERENCES',','.join(map(str,d)))
    assert h<H if u>F(187,500) else h<=H
    print('POLICY',name,'u',u,'A',A,'B',B,'U',U,'V',V,
          'e',h,'H_MINUS_e',H-h)
    return h

uH=F(865,2526)
u_compact=F(234,625)
u_near=F(18721181,50000000)
u_right=F(37442363,100000000)
assert F(0)<uH<u_compact<u_near<u_right<F(239,638)<1
assert p(u_near)<0<p(u_right)
assert 2828*uH+4091>0
hH=validate_rational_policy('OLD_ENDPOINT',uH)
assert hH==H
h_compact=validate_rational_policy('COMPACT_STRICT',u_compact)
h_near=validate_rational_policy('NEAR_ROOT',u_near)
assert OLD_LOWER<h_near<h_compact<H

u=sp.symbols('u')
r=(sp.sqrt(26521161)-4091)/2828
As=(1414*u+1033)/(250*(7-2*u))
Bs=(961-1414*u)/(500*(7-2*u))
assert sp.simplify(1414*r*r+4091*r-1730)==0
assert sp.simplify(Bs.subs(u,r)-(7221-sp.sqrt(26521161))/15000)==0
estar=sp.sqrt(26521161)/15000-sp.Rational(413,1250)
assert sp.simplify((u*Bs/4).subs(u,r)-estar)==0
assert sp.simplify(As.subs(u,r))>0

sqrt_lower=F(5149869998,1000000)
sqrt_upper=F(514987,100)
assert sqrt_lower**2<26521161<sqrt_upper**2
lo=sqrt_lower/15000-F(413,1250)
hi=sqrt_upper/15000-F(413,1250)
assert OLD_LOWER<lo<hi<H
assert h_near>lo and h_near>OLD_LOWER
print('EXACT_ROOT_IS_BETWEEN',u_near,u_right)
print('RADICAL_UPPER',estar)
print('RADICAL_BOUND_INTERVAL',lo,hi)
print('UPDATED_CONDITIONAL_BRACKET_LOWER',OLD_LOWER,'UPPER',estar)
print('OLD_H_STRICTLY_FALSIFIED_BY_RATIONAL_WITNESS',h_compact)
print('PASS_BRC_N4_BU_H_STRICT_COUNTEREXAMPLE_RADICAL_UPPER_20261030')
