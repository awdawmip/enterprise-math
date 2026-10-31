#!/usr/bin/env python3
"""Stage337-B exact Bernoulli/BRC tagged residual r0-boundary certificate.

Independent finite algebra/rational checks only; continuous quantifiers are
proved by the derivative inequalities in PROOF_STAGE337B.md.
"""
from fractions import Fraction as Q
import sympy as S

w = (1, 3, 3, 1)
m = (61, 21, 9, 9)
xa, xb = Q(2311, 10000), Q(2354, 10000)
ymin, ymax = Q(5091, 10000), Q(5554, 10000)

def B(k, z):
    return z**k * (1-z)**(3-k)

def rr(k, x, y):
    return (4*B(k, x)+B(k, y))/5 - Q(m[k], 160)

def r0(x,y): return rr(0,x,y)

def Fdet(x,y):
    return (1-x)*(189-183*x)*(2*y-1) - 48*(1-2*x)*y*(1-y)

def D3(a,z):
    return sum(Q(w[k],2)*abs(B(k,a)-B(k,z)) for k in range(4))

def b(x,y):
    return Q(5,32)*sum(w[k]*abs(rr(k,x,y)) for k in range(4))

def c(x,y):
    return (63*D3(Q(1,4),x)+D3(Q(3,4),x)
            +9*D3(Q(1,4),y)+7*D3(Q(3,4),y))/256

def check_bracket(x,lo,hi):
    assert r0(x,lo)>0 and r0(x,hi)<0, (x,lo,hi)

def signs_on_interval(a,lo,hi):
    # B_k monotone on each specified subinterval: x<1/3 or 1/2<y<2/3.
    sl = [S.sign(B(k,a)-B(k,lo)) for k in range(4)]
    sh = [S.sign(B(k,a)-B(k,hi)) for k in range(4)]
    assert sl == sh and all(z!=0 for z in sl)
    return ''.join('+' if z==1 else '-' for z in sl)

# Immutable algebraic definition of the model; conservation and tagged gradients.
x,y=S.symbols('x y',real=True)
BS=lambda k,z: z**k*(1-z)**(3-k)
RS=lambda k: (4*BS(k,x)+BS(k,y))/5-S.Rational(m[k],160)
assert S.simplify(sum(w[k]*RS(k) for k in range(4)))==0

def weighted_tag_derivative(z,signs):
    return -S.Rational(1,2)*sum(w[k]*signs[k]*S.diff(BS(k,z),z) for k in range(4))

cx=S.factor((63*weighted_tag_derivative(x,[-1,1,1,1])
             +weighted_tag_derivative(x,[-1,-1,1,1]))/256)
cy=S.factor((9*weighted_tag_derivative(y,[1,1,-1,-1])
             +7*weighted_tag_derivative(y,[-1,-1,1,1]))/256)
assert S.simplify(cx+(1-x)*(189-183*x)/256)==0
assert S.simplify(cy-3*y*(1-y)/64)==0
assert S.simplify(S.diff(RS(0),x)+S.Rational(12,5)*(1-x)**2)==0
assert S.simplify(S.diff(RS(0),y)+S.Rational(3,5)*(1-y)**2)==0
assert S.simplify(S.diff(RS(3),x)-S.Rational(12,5)*x*x)==0
assert S.simplify(S.diff(RS(3),y)-S.Rational(3,5)*y*y)==0

# Graph Y0 exists over xa..xb; y decreases. Rational endpoint brackets.
assert r0(xb,Q(1,2))>0 and r0(xa,Q(2,3))<0
check_bracket(xa,Q(5553,10000),ymax)
check_bracket(xb,ymin,Q(5092,10000))

# r1>0, r3<0 and r2>0 on graph by monotone along-graph derivatives.
assert rr(1,xa,ymax)>0
assert rr(3,xa,ymax)<0
assert rr(2,xa,ymin)>0
print('GRAPH_ENDPOINT_BRACKETS_PASS')
print('r1(xa,ymax)=',rr(1,xa,ymax))
print('r3(xa,ymax)=',rr(3,xa,ymax))
print('r2(xa,ymin)=',rr(2,xa,ymin))

# Across the graph the complete 16 tagged comparisons are constant.
patterns=(signs_on_interval(Q(1,4),xa,xb),
          signs_on_interval(Q(3,4),xa,xb),
          signs_on_interval(Q(1,4),ymin,ymax),
          signs_on_interval(Q(3,4),ymin,ymax))
assert patterns == ('-+++','--++','++--','--++'),patterns
print('ALL_16_TAG_COMPARISONS',patterns)

# For the upper endpoint, b=-5r3/16, increasing along Y0.
assert -Q(5,16)*rr(3,xb,ymin)<Q(61,10000)
print('LOW_ERROR_GLOBAL_ARC_BOUND',-Q(5,16)*rr(3,xb,ymin),'<',Q(61,10000))

# Analytical first-order dominance/KKT determinant:
p=(1-x)*(189-183*x)/256  # c_x=-p
q=3*y*(1-y)/64            # c_y=q
A=S.Rational(3,4)*(1-2*x) # b_{r0<0,x}
G=S.Rational(3,16)*(2*y-1) # b_{r0<0,y}=-G
assert S.simplify(p*G-A*q-S.Rational(3,4096)*((1-x)*(189-183*x)*(2*y-1)-48*(1-2*x)*y*(1-y)))==0

# Root isolation by all-rational boxes; F strictly increases in y in the range.
critical=[(Q(233494,10**6),Q(528433,10**6),Q(528434,10**6),1),
          (Q(233495,10**6),Q(528423,10**6),Q(528424,10**6),-1)]
for x0,lo,hi,s in critical:
    check_bracket(x0,lo,hi)
    assert S.sign(Fdet(x0,lo))==s and S.sign(Fdet(x0,hi))==s
    print('CRITICAL_INTERVAL',x0,lo,hi,'F_LOW',Fdet(x0,lo),'F_HIGH',Fdet(x0,hi),'SIGN',s)

# One rational witness of simultaneous strict improvement in the r0<0 chamber.
q0=(Q(233,1000),Q(533717,10**6))
h=Q(1,10**7)
q1=(q0[0]+h,q0[1]+35*h)
assert rr(0,*q0)<0 and rr(0,*q1)<0
assert all(rr(k,*z)>0 for z in (q0,q1) for k in (1,2))
assert all(rr(3,*z)<0 for z in (q0,q1))
db=b(*q1)-b(*q0)
dc=c(*q1)-c(*q0)
assert db<0 and dc<0
print('RATIONAL_WITNESS',q0,'TO',q1,'delta_b',db,'delta_c',dc)
print('STAGE337B_EXACT_R0_KKT_FIRST_ORDER_SWITCH_PASS')
