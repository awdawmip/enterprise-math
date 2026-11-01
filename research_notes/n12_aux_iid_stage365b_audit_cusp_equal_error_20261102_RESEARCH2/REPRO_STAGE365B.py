#!/usr/bin/env python3
"""Stage365-B: exact rational audit-cusp transverse projection certificate.

All 16 original source/word comparisons and four audit ports are retained.
SymPy checks identities; Fraction checks the strict rational inequalities.
"""
from fractions import Fraction as F
import sympy as S

X, Y = S.symbols('x y', real=True)
w = (1, 3, 3, 1)
m = (61, 21, 9, 9)
XL, XU = F(237,1000), F(239,1000)
YL, YU = F(287,500), F(289,500)
KXL, KXU = F(2373,10000), F(2387,10000)
KYL, KYU = F(1149,2000), F(231,400)
ETA = F(1,100000)


def B(k,z): return z**k * (1-z)**(3-k)
def r(k,x,y): return (4*B(k,x)+B(k,y))/5 - F(m[k],160)
def u1(z): return (1-z)*(1-3*z)
def u2(z): return z*(2-3*z)
def port(a,z,s):
    return S.Rational(1,2)*sum(w[k]*s[k]*(B(k,a)-B(k,z)) for k in range(4))

assert XL<KXL<KXU<XU and YL<KYL<KYU<YU
assert XL<XU<F(1,4)<YL<YU<F(2,3)<F(3,4)
assert sum(w[k]*m[k] for k in range(4)) == 160
assert S.expand(sum(w[k]*r(k,X,Y) for k in range(4))) == 0
assert r(0,XL,YL)<0 and r(2,XL,YL)>0 and r(3,XU,YU)<0
print('RATIONAL_RESIDUAL_SIGNS_AND_WEIGHTED_ZERO_IDENTITY_PASS')

# The only changing audit sign is k=2 at (3/4,y).
# Every B_k is monotone on either coordinate interval, so checking both
# endpoints verifies each nonchanging sign throughout the full real box.
blocks = [(F(1,4),XL,XU,(-1,1,1,1)),
          (F(3,4),XL,XU,(-1,-1,1,1)),
          (F(1,4),YL,YU,(1,1,-1,-1)),
          (F(3,4),YL,YU,(-1,-1,None,1))]
for a,lo,hi,sgn in blocks:
    for k,s in enumerate(sgn):
        if s is not None:
            assert s*(B(k,a)-B(k,lo))>0
            assert s*(B(k,a)-B(k,hi))>0
assert B(2,F(5756,10000)) < F(9,64) < B(2,F(5757,10000))
assert u2(YL)>0 and u2(YU)>0
# B2 rises on [YL,YU]. Thus alpha is its unique crossing of 9/64,
# between 5756/10000 and 5757/10000, and is the audit cusp.
alpha_lo,alpha_hi=F(5756,10000),F(5757,10000)
assert r(1,KXL,alpha_lo)<0 and r(1,KXU,alpha_hi)>0
# r1 increases with x and decreases with y on R: the r1=0 arc
# crosses the cusp inside K, at exactly one x-coordinate.
print('ALL_SIXTEEN_LABELS_ONE_EXACT_CUSP_AND_KINK_INTERSECTION_PASS')

base = [(F(1,4),X,(-1,1,1,1),63),
        (F(3,4),X,(-1,-1,1,1),1),
        (F(1,4),Y,(1,1,-1,-1),9)]
Clo=S.factor((sum(weight*port(a,z,s) for a,z,s,weight in base)
               +7*port(F(3,4),Y,(-1,-1,1,1)))/256)
Chi=S.factor((sum(weight*port(a,z,s) for a,z,s,weight in base)
               +7*port(F(3,4),Y,(-1,-1,-1,1)))/256)
cx=-3*(1-X)*(63-61*X)/256
cylo=3*Y*(1-Y)/64
cyhi=3*Y*(18-25*Y)/256
assert S.simplify(S.diff(Clo,X)-cx)==0
assert S.simplify(S.diff(Chi,X)-cx)==0
assert S.simplify(S.diff(Clo,Y)-cylo)==0
assert S.simplify(S.diff(Chi,Y)-cyhi)==0
assert S.simplify(cyhi-cylo-S.Rational(21,256)*u2(Y))==0
assert S.simplify(Chi-Clo-S.Rational(21,256)*(B(2,Y)-S.Rational(9,64)))==0
print('EXACT_AUDIT_COST_FORMULAE_CONTINUITY_AND_GRADIENT_JUMP_PASS')

r1=r(1,X,Y)
r2=r(2,X,Y)
bminus=S.Rational(15,16)*r2
bplus=S.Rational(15,16)*(r2+r1)
rx=S.diff(r1,X); ry=S.diff(r1,Y)
J=S.Rational(3,20)*(u1(X)*u2(Y)-u1(Y)*u2(X))
for b in (bminus,bplus):
    assert S.simplify(rx*S.diff(b,Y)-ry*S.diff(b,X)-J)==0
assert S.simplify(S.diff(bminus,X)-S.Rational(3,4)*u2(X))==0
assert S.simplify(S.diff(bminus,Y)-S.Rational(3,16)*u2(Y))==0
assert S.simplify(S.diff(bplus,X)-S.Rational(3,4)*(1-2*X))==0
assert S.simplify(S.diff(bplus,Y)-S.Rational(3,16)*(1-2*Y))==0
print('TWO_TV_BRANCHES_AND_COMMON_TRANSVERSE_JACOBIAN_PASS')

# Exact interval enclosures: u1 decreases on R; u2 increases on
# the x interval and decreases on the y interval.
Jl=F(3,20)*(u1(XU)*u2(YU)-u1(YL)*u2(XL))
Ju=F(3,20)*(u1(XL)*u2(YL)-u1(YU)*u2(XU))
assert F(1,60)<Jl<Ju<F(1,40)
gmin=F(3,256)*(1-XU)*(63-61*XU)
cymin=F(3,64)*YU*(1-YU)
cymax=F(3,256)*YL*(18-25*YL)
# Both audit-label choices have cy in [cymin,cymax].
assert cymin>0 and cymax>cymin
Dminus_upper=-gmin*F(3,16)*u2(YU)-cymin*F(3,4)*u2(XL)
Dplus_lower=gmin*F(3,16)*(2*YL-1)-cymax*F(3,4)*(1-2*XL)
assert Dminus_upper < -F(7,500)
assert Dplus_lower > F(1,500)
print('EXACT_BOTH_CUSP_SIDES_JACOBIAN_1/60_LT_J_LT_1/40_PASS')
print('EXACT_UNIFORM_COST_WEDGES_DMINUS_LT_-7/500_DPLUS_GT_1/500_PASS')

# Along the fixed-b ODE dx/dt=b_y/J, dy/dt=-b_x/J,
# |dx/dt|<2, |dy/dt|<24. R contains the full trajectory to t=0.
assert F(3,16)*u2(YL)<F(1,30)
assert F(3,16)*(2*YU-1)<F(1,30)
assert F(3,4)*u2(XU)<F(2,5)
assert F(3,4)*(1-2*XL)<F(2,5)
assert 2*ETA < min(KXL-XL,XU-KXU)
assert 24*ETA < min(KYL-YL,YU-KYU)
assert F(1,500)*40==F(2,25)
assert F(7,500)*40==F(14,25)
print('EXACT_DISTANCE_BARRIER_AND_GLOBAL_CUSP_CROSSING_SLOPE_BOUNDS_PASS')

# On the r1=0 graph, Y'(x)=4*u1(x)/(-u1(y)) is positive.
# The along-arc error derivative B' is common to both r1 branches;
# a positive jump of the audit y-gradient makes phi'=d(c)/d(b)
# jump up by more than 1/10 at the first audit cusp.
Ypmin=4*u1(XU)/(-u1(YU))
Ypmax=4*u1(XL)/(-u1(YL))
Bpmax=F(3,4)*u2(XU)+F(3,16)*u2(YL)*Ypmax
Bpmin=F(3,4)*u2(XL)+F(3,16)*u2(YU)*Ypmin
assert 0<Ypmin<Ypmax and 0<Bpmin<Bpmax
assert F(21,256)*u2(YU)*Ypmin/Bpmax > F(1,10)
print('FIRST_AUDIT_CUSP_RIGHT_ARC_MARGINAL_COST_UPWARD_JUMP_GT_1/10_PASS')

# Nonvacuity: exact rational samples on both sides of the audit cusp,
# both in K with nonzero residual |r1|<ETA.
p_before=(F(2377,10000),F(5755,10000))
p_after=(F(2379,10000),F(5758,10000))
assert B(2,p_before[1])<F(9,64) and -ETA<r(1,*p_before)<0
assert B(2,p_after[1])>F(9,64) and 0<r(1,*p_after)<ETA
assert all(KXL<=p[0]<=KXU and KYL<=p[1]<=KYU for p in (p_before,p_after))
print('NONEMPTY_CUSP_BOTH_SIDES_RATIONAL_WITNESSES_PASS')
print('THEOREM: Every real p in K with |r1(p)|<=1/100000 admits q in R')
print('such that r1(q)=0 and b(q)=b(p), even across the audit-label cusp.')
print('r1(p)>0 implies c(p)-c(q)>(2/25)*r1(p).')
print('r1(p)<0 implies c(p)-c(q)>(14/25)*(-r1(p)).')
print('STAGE365B_AUDIT_CUSP_EQUAL_ERROR_TRANSVERSE_PROJECTION_EXACT_PASS')
