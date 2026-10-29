#!/usr/bin/env python3
"""Exact, author-side 16-leaf rational counterexample; no theorem admission."""
from collections import defaultdict
from fractions import Fraction as F
import sympy as S

q2={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
rat={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
     'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaves=[(k,j,z,q2[k]/4,q2[k]*rat[k][j]/4)
        for k in q2 for j in (0,1) for z in (0,1)]
assert len(leaves)==16 and all(q>0 and p>0 for _,_,_,q,p in leaves)
assert sum(q for _,_,_,q,p in leaves)==sum(p for _,_,_,q,p in leaves)==1

def vec(law,a,b,A,B,u,U,V,target):
    out=defaultdict(F)
    for k,j,z,q,p in leaves:
        mass=q if law=='Q' else p
        first=(a if k[0]=='A' else b) if target else (A if k[0]=='A' else B)
        cont=(F(1) if k=='AU' else F(0)) if target else {
            'AU':u,'BU':u,'AV':U/A,'BV':V/B}[k]
        assert 0<=first<=1 and 0<=cont<=1
        out[(1,'Q',0)] += mass*(1-first)
        out[(2,'Q',0)] += mass*first*(1-cont)
        out[(3,'Q' if k=='BU' and not target else 'P',int(k=='BU'))] += mass*first*cont
    assert sum(out.values())==1
    return out

def tv(x,y):
    return sum(abs(x.get(k,0)-y.get(k,0)) for k in x.keys()|y.keys())/2

a,b=F(97,100),F(4,25)
A,B=a,b
u=(2*a-7*b)/(2*a+4*b)
U=b*(4*a-3*b)/(2*(a+2*b))
V=b
H=b*u/4
C=(7-a-21*b)/(4*a+12*b+2)
E=(b-(1-a)/3)*C/4
G=5*a*a+8*a*b-21*b*b-2*b-5
assert 0<a<1 and 0<b<1 and 0<u<1 and 0<U<A and 0<V<=B
assert G==F(177,2000)>0 and H==F(41,3225)
assert E==F(267,20800) and E-H==F(331,2683200)>0
for law in ('P','Q'):
    target=vec(law,a,b,A,B,u,U,V,True)
    competitor=vec(law,a,b,A,B,u,U,V,False)
    assert tv(target,competitor)==H
    print(law,'TV=',H,'target=',sorted(target.items()),'competitor=',sorted(competitor.items()))

x,y=S.symbols('a b',real=True)
w=(2*x-7*y)/(2*x+4*y)
Up=y*(4*x-3*y)/(2*(x+2*y))
T=x*x+38*x*y-7*x+105*y*y-14*y
E_sym=(y-(1-x)/3)*(7-x-21*y)/(4*(4*x+12*y+2))
H_sym=y*w/4
assert S.factor(E_sym-H_sym-(1-x)*T/(24*(x+2*y)*(2*x+6*y+1)))==0
h=y*w/4
rQ=x*(1-w)/6-Up/3-y/4
rP=x*(1-w)/6-Up/12-y/2
assert S.factor(rQ)==0 and S.factor(rP-h)==0
assert S.factor(T.subs({x:S.Rational(97,100),y:S.Rational(4,25)})-S.Rational(993,2000))==0
print('PASS_16_POSITIVE_LEAVES_BOTH_NORMALIZED')
print('PASS_FULL_PQ_TERMINAL_TV',H)
print('PASS_SYMBOLIC_FAMILY_GAP_FACTORIZATION')
print('PARAMETERS','a=',a,'b=',b,'u=',u,'A=',A,'B=',B,'U=',U,'V=',V,'G=',G)
print('CURVED_EXTRAPOLATION',E,'LEGAL_COMPETITOR',H,'STRICT_GAP',E-H)
print('STATUS AUTHOR_SIDE_EXACT_COUNTEREXAMPLE_UNREVIEWED_NOT_ADMITTED')
