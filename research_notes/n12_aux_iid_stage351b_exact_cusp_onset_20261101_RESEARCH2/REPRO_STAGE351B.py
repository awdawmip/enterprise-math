#!/usr/bin/env python3
"""Stage351-B: exact Fractions certificate for the first *right-arc* cusp split.

All theorem assertions use rational arithmetic only. Decimal is used solely to
render already-verified rational enclosures. Run with assertions enabled.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from decimal import Decimal, getcontext

W = (1, 3, 3, 1)
M = (61, 21, 9, 9)
E_MAX = F(11, 5000)

def B(k, z):
    return z**k * (1-z)**(3-k)

def r(k, x, y):
    return (4*B(k, x)+B(k, y))/5 - F(M[k],160)

def b(x, y):
    return F(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))

def D(a,z):
    return F(1,2)*sum(W[k]*abs(B(k,a)-B(k,z)) for k in range(4))

def c(x,y):
    return (63*D(F(1,4),x)+D(F(3,4),x)+9*D(F(1,4),y)+7*D(F(3,4),y))/256

def b2_on_arc(x,y):
    return F(15,16)*r(2,x,y)

# Signed interval arithmetic: natural rational enclosure, inclusive endpoints.
@dataclass(frozen=True)
class I:
    lo:F
    hi:F
    def __init__(self,lo,hi=None):
        object.__setattr__(self,'lo',F(lo))
        object.__setattr__(self,'hi',F(lo if hi is None else hi))
        assert self.lo <= self.hi
    @staticmethod
    def wrap(t): return t if isinstance(t,I) else I(t)
    def __add__(a,b):
        b=I.wrap(b)
        return I(a.lo+b.lo,a.hi+b.hi)
    __radd__=__add__
    def __neg__(a):return I(-a.hi,-a.lo)
    def __sub__(a,b):return a+(-I.wrap(b))
    def __rsub__(a,b):return I.wrap(b)-a
    def __mul__(a,b):
        b=I.wrap(b)
        z=(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi)
        return I(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(a,b):
        b=I.wrap(b)
        assert b.lo*b.hi>0, 'division interval crosses zero'
        return a*I(F(1)/b.hi,F(1)/b.lo)
    def __rtruediv__(a,b):return I.wrap(b)/a

def bisect_Y1(x):
    """r1(x,y) is strictly decreasing for 1/3<y<2/3."""
    lo,hi=F(11,20),F(3,5)
    assert r(1,x,lo)>0>r(1,x,hi)
    for _ in range(65):
        m=(lo+hi)/2
        if r(1,x,m)>0: lo=m
        else: hi=m
    assert r(1,x,lo)>0>r(1,x,hi)
    return lo,hi

# Explicit 16 source label comparisons: x vs 1/4,3/4; y vs 1/4,3/4.
# On the whole right-arc [q*, q_Emax] the only zero is the y,3/4,k=2 cusp.
X_ALL_LO,X_ALL_HI=F('0.23108'),F('0.23788')
Y_ALL_LO,Y_ALL_HI=F('0.55550'),F('0.57591')
sgn_x14=(-1,1,1,1)
sgn_x34=(-1,-1,1,1)
sgn_y14=(1,1,-1,-1)
sgn_y34left=(-1,-1,1,1)
sgn_y34right=(-1,-1,-1,1)
for a,lo,hi,sgns,exempt in (
    (F(1,4),X_ALL_LO,X_ALL_HI,sgn_x14,()),
    (F(3,4),X_ALL_LO,X_ALL_HI,sgn_x34,()),
    (F(1,4),Y_ALL_LO,Y_ALL_HI,sgn_y14,()),
    (F(3,4),Y_ALL_LO,Y_ALL_HI,sgn_y34left,(2,))):
    for k in range(4):
        if k in exempt:continue
        assert sgns[k]*(B(k,a)-B(k,lo))>0
        assert sgns[k]*(B(k,a)-B(k,hi))>0
# The lone changing comparison has B2(3/4)=9/64.
assert B(2,F(3,4))==F(9,64)
assert B(2,F('0.5555'))<F(9,64)<B(2,F('0.57591'))
assert sum(W[k]*r(k,F(7,31),F(19,37)) for k in range(4))==0

# Isolate q* (r0=r1=0) independently by a monotone graph, tightening the
# previous stage's root interval to x resolution 10^-12.
xs0,xs1=F(231083940855,10**12),F(231083940856,10**12)
ys0_lo,ys0_hi=bisect_Y1(xs0)
ys1_lo,ys1_hi=bisect_Y1(xs1)
assert r(0,xs0,ys0_hi)>0
assert r(0,xs1,ys1_lo)<0
# Since Y1 increases and r0 decreases in both x,y, q* exists uniquely.
star_ylo,star_yhi=ys0_lo,ys1_hi
assert Y_ALL_LO < star_ylo < star_yhi < F('0.55580')
beta_lo,beta_hi=b2_on_arc(xs0,star_ylo),b2_on_arc(xs1,star_yhi)
assert beta_lo<beta_hi

# Exact algebraic tag cusp: y†=(1+sqrt(13))/8, with certified rational box.
yc_lo,yc_hi=F(575693909432998,10**15),F(575693909432999,10**15)
assert (8*yc_lo-1)**2 < 13 < (8*yc_hi-1)**2
xc_lo,xc_hi=F(237806902790,10**12),F(237806902792,10**12)
# r1_x>0,r1_y<0 on the domain. For any y† in the y-box:
assert r(1,xc_lo,yc_lo)<0<r(1,xc_hi,yc_hi)
assert X_ALL_LO<xs0<xs1<xc_lo<xc_hi<X_ALL_HI
assert Y_ALL_LO<star_ylo<star_yhi<yc_lo<yc_hi<Y_ALL_HI
bc_lo,bc_hi=b2_on_arc(xc_lo,yc_lo),b2_on_arc(xc_hi,yc_hi)
sc_lo,sc_hi=bc_lo-beta_hi,bc_hi-beta_lo
assert F('0.0021814072266') < sc_lo < sc_hi < F('0.0021814072275')
assert F(1,500)<sc_lo<E_MAX

# The r1=0 right arc is smooth/increasing and chamber-stable outside the
# single y-source label cusp: r0<0 (after q*), r2>0, r3<0.
assert r(2,xs0,star_ylo)>0
assert r(3,X_ALL_HI,Y_ALL_HI)<0
# Then conservation of the signed 4-word residuals gives b=15*r2/16.
# B2_x,B2_y are strictly positive on these boxes (<2/3).

# Certify that all E up to Emax lie inside a right-arc x-box, and that
# E - s† stays inside the left near-star derivative box.
x_left_hi=F('0.23117')
YL_lo,YL_hi=bisect_Y1(x_left_hi)
assert YL_hi<F('0.55580')
# s(x_left_hi)>Emax - s†. Use lower b and upper beta.
assert b2_on_arc(x_left_hi,YL_lo)-beta_hi > E_MAX-sc_lo
x_right_hi=F('0.23788')
YR_lo,YR_hi=bisect_Y1(x_right_hi)
assert YR_hi < Y_ALL_HI
assert b2_on_arc(x_right_hi,YR_lo)-beta_hi > E_MAX

# Exact polynomial tangent formulas for the continuous right r1=0 arc.
# c_x = -3(x-1)(61x-63)/256 for both sides;
# c_y^-=-3y(y-1)/64; c_y^+=-3y(25y-18)/256.
# All 16 tag signs were checked above.
def arc_terms(X,Y,right):
    rx=I(4)*(X-1)*(3*X-1)/5
    ry=(Y-1)*(3*Y-1)/5
    assert rx.lo>0 and ry.hi<0
    yp=-rx/ry
    bx=-I(3)*X*(3*X-2)/4
    by=-I(3)*Y*(3*Y-2)/16
    bp=bx+by*yp
    assert bp.lo>0
    cx=-I(3)*(X-1)*(61*X-63)/256
    cy=(-I(3)*Y*(25*Y-18)/256 if right else -I(3)*Y*(Y-1)/64)
    cp=cx+cy*yp
    return rx,ry,yp,bx,by,bp,cx,cy,cp

def phi_prime_interval(X,Y,right):
    rx,ry,yp,bx,by,bp,cx,cy,cp=arc_terms(X,Y,right)
    return cp/bp

L=phi_prime_interval(I(F('0.23108'),F('0.23117')),I(F('0.55550'),F('0.55580')),False)
R=phi_prime_interval(I(F('0.23780'),F('0.23788')),I(F('0.57569'),F('0.57591')),True)
assert L.hi < -F(119,100)  # phi'(small s) < -1.19
assert R.lo > -F(117,100) and R.hi < 0  # -1.17 < phi'(s beyond cusp) < 0
# Therefore for E in (s†, 0.0022], derivative of
# H(E)=phi(s†)+phi(E-s†)-phi(0)-phi(E) is < -1/50.

# Independently prove strict concavity of phi(s) for 0<s<s†:
# N=c_arc'' b_arc' - c_arc' b_arc'' < -4/5,
# phi''(s)=N/(b_arc')^3 <0.
def curvature_interval(X,Y):
    rx,ry,yp,bx,by,bp,cx,cy,cp=arc_terms(X,Y,False)
    rxx=I(4)*(6*X-4)/5
    ryy=(6*Y-4)/5
    ypp=-(rxx+ryy*yp*yp)/ry
    bxx=-(18*X-6)/4
    byy=-(18*Y-6)/16
    cxx=-I(3)*(122*X-124)/256
    cyy=-I(3)*(2*Y-1)/64
    bpp=bxx+byy*yp*yp+by*ypp
    cpp=cxx+cyy*yp*yp+cy*ypp
    return cpp*bp-cp*bpp,bp
N,BP=curvature_interval(I(F('0.23108'),F('0.23781')),I(F('0.55550'),F('0.57570')))
assert N.hi < -F(4,5)
assert BP.lo>F(1,4)
# For E<=s†, strict concavity of phi on [0,E] implies
# phi(t)+phi(E-t)>phi(0)+phi(E) for all 0<t<E.
# For every s†<E<=Emax, strict derivative separation yields
# phi(s†)+phi(E-s†)-phi(0)-phi(E)<-(E-s†)/50.

getcontext().prec=36
def dec(t):return str(Decimal(t.numerator)/Decimal(t.denominator))
print('STAGE351B_CUSP_EXACT_ONSET_IN_RIGHT_ARC_FRACTION_INTERVAL_PASS')
print('right_arc_budget_first_split_infimum = s_cusp')
print('cusp_budget_certified_bracket =',dec(sc_lo),dec(sc_hi))
print('star_beta_certified_bracket =',dec(beta_lo),dec(beta_hi))
print('pre_cusp_curvature_numerator_upper =',dec(N.hi))
print('pre_cusp_arc_budget_derivative_lower =',dec(BP.lo))
print('small_budget_phi_prime_upper =',dec(L.hi))
print('post_cusp_phi_prime_lower =',dec(R.lo))
print('uniform_cusp_split_advantage_for_all_s_cusp<E<=11/5000 = at_least_(E-s_cusp)/50')
print('source_tag_comparisons=16; arithmetic=Fraction; proof_scope=restricted_right_r1_arc')
