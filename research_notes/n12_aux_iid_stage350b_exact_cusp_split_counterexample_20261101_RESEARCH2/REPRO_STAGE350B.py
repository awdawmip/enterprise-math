#!/usr/bin/env python3
"""Stage350-B: exact rational disproof of endpoint allocation at E=11/5000.

Standard-library only, Python 3.10+. No floating point is used in assertions.
The inequalities certify real implicit roots by monotonicity/IVT in the accompanying proof.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext

W=(1,3,3,1)
M=(61,21,9,9)
E=F(11,5000)

def B(k,z):
    return z**k*(1-z)**(3-k)

def r(k,x,y):
    return (4*B(k,x)+B(k,y))/5-F(M[k],160)

def b(x,y):
    return F(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))

def D(a,z):
    return F(1,2)*sum(W[k]*abs(B(k,a)-B(k,z)) for k in range(4))

def c(x,y):
    return (63*D(F(1,4),x)+D(F(3,4),x)+9*D(F(1,4),y)+7*D(F(3,4),y))/256

def B2_curve(x,y):
    return F(15,16)*r(2,x,y)

def show(name,x):
    getcontext().prec=35
    print(f'{name}: {Decimal(x.numerator)/Decimal(x.denominator)}')

# Original labeled D3 formula: all 4 words, w=(1,3,3,1), both anchors.
assert sum(W[k]*r(k,F(7,31),F(19,37)) for k in range(4)) == 0
assert all(v>0 for v in W)

# The double-zero q_* exists uniquely in this rectangle.  For x in [a0,a1],
# r1(x,y)=0 has a unique solution Y1(x); B1'(x)>0, B1'(y)<0.
# Therefore Y1 is increasing, while r0(x,Y1(x)) is strictly decreasing.
a0,a1=F(2310839408,10**10),F(2310839409,10**10)
d0,d1=F(555508855,10**9),F(555508860,10**9)
s_y0lo,s_y0hi=F(555508857100,10**12),F(555508857101,10**12)
s_y1lo,s_y1hi=F(555508857418,10**12),F(555508857419,10**12)
for x,lo,hi in ((a0,s_y0lo,s_y0hi),(a1,s_y1lo,s_y1hi)):
    assert d0<lo<hi<d1
    assert r(1,x,lo)>0>r(1,x,hi)
for x in (a0,a1):
    assert r(1,x,d0)>0>r(1,x,d1)
assert r(0,a0,s_y0hi)>0
assert r(0,a1,s_y1lo)<0
# B2 strictly increasing in each coordinate in these narrow boxes (z<2/3).
beta_lo=B2_curve(a0,d0)
beta_hi=B2_curve(a1,d1)
assert 0<beta_lo<beta_hi

# Beyond the tag cusp, q_E is the unique r1=0, b=beta_*+E point on the
# right arc in the following fully rational rectangle.
xL,xH=F(23786633,10**8),F(23786635,10**8)
yL_lo,yL_hi=F(575862128811,10**12),F(575862128812,10**12)
yH_lo,yH_hi=F(575862185396,10**12),F(575862185397,10**12)
assert d1<yL_lo<yL_hi<yH_lo<yH_hi<F(2,3)
assert a1<xL<xH<F(1,3)
for x,lo,hi in ((xL,yL_lo,yL_hi),(xH,yH_lo,yH_hi)):
    assert r(1,x,lo)>0>r(1,x,hi)
# The r1=0 arc has r0<0,r2>0,r3<0, hence b=15*r2/16.
assert r(0,xL,yL_lo)<0
assert r(2,xL,yL_lo)>0
assert r(3,xH,yH_hi)<0
left_margin=beta_lo+E-B2_curve(xL,yL_hi)
right_margin=B2_curve(xH,yH_lo)-(beta_hi+E)
assert left_margin>0 and right_margin>0
# r1_x>0, r1_y<0, and r2_x,r2_y>0 on the rectangle, ensuring IVT,
# uniqueness and the x_E,y_E enclosure claimed in the proof.

# A fully specified, exactly rational *feasible* two-source competitor.
Q1=(F(231139116642,10**12),F(555684475793,10**12))
Q2=(F(237806870832,10**12),F(575693818922,10**12))
assert all(F(0)<t<F(1) for q in (Q1,Q2) for t in q)
B_witness=b(*Q1)+b(*Q2)
C_witness=c(*Q1)+c(*Q2)
feasible_margin=2*beta_lo+E-B_witness
assert feasible_margin>F(9,10**9)

# Exact global Lipschitz bound D3(p,q)<=3|p-q|, by coupling three
# Bernoulli coordinates (union bound). Therefore:
# |c(x,y)-c(x',y')| <= 3/4 |x-x'|+3/16 |y-y'|.
# Use rational anchors at the LOWER corners of the two implicit root boxes.
C_star_lower=c(a0,d0)-F(3,4)*(a1-a0)-F(3,16)*(d1-d0)
C_E_lower=c(xL,yL_lo)-F(3,4)*(xH-xL)-F(3,16)*(yH_hi-yL_lo)
advantage_lower=C_star_lower+C_E_lower-C_witness
assert advantage_lower>F(1,2*10**6)

# This strict inequality is independent of the Stage349 global-Pareto claim.
# Any true q_* and q_E in the certified boxes obey
# T(Q1,Q2) < T(q_*,q_E), with the additive 33/1024 cancelling.
print('STAGE350B_E_11_OVER_5000_STRICT_RATIONAL_SPLIT_COUNTEREXAMPLE_EXACT_PASS')
show('beta_lower',beta_lo)
show('beta_upper',beta_hi)
show('left_arc_bracket_margin',left_margin)
show('right_arc_bracket_margin',right_margin)
show('witness_budget_safe_margin_lower',feasible_margin)
show('witness_cost',C_witness)
show('incumbent_cost_lower',C_star_lower+C_E_lower)
show('strict_cost_advantage_lower',advantage_lower)
print('witness_Q1=',tuple(str(t) for t in Q1))
print('witness_Q2=',tuple(str(t) for t in Q2))
print('full_source_labels=16; arithmetic=Fraction; exact_implicit_root_enclosures=True')
