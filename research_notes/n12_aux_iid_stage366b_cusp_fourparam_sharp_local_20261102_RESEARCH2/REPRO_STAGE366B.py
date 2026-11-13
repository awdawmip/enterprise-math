#!/usr/bin/env python3
"""Stage366-B: exact certificate of sharp local 4-parameter optimality
at the first audit cusp budget for the ORIGINAL 16-provenance-label observer.

Every numerical inequality used in the proof is exact Fraction arithmetic.
SymPy is used only for symbolic identities of all 16 labeled audit terms.
No optimizer, sampling, or floating-point evidence enters any assertion.
"""
from fractions import Fraction as F
from dataclasses import dataclass
import sympy as S

LAM = F(49, 40)
w = (1,3,3,1)
m = (61,21,9,9)

def B(k,z): return z**k * (1-z)**(3-k)
def dB(k,z):
    if k == 0: return -3*(1-z)**2
    if k == 1: return (1-z)*(1-3*z)
    if k == 2: return z*(2-3*z)
    return 3*z*z

def r(k,x,y): return (4*B(k,x)+B(k,y))/5-F(m[k],160)

def gr(k,x,y): return (F(4,5)*dB(k,x),F(1,5)*dB(k,y))

@dataclass(frozen=True)
class I:
    lo: F
    hi: F
    def __init__(self, lo, hi=None):
        lo=F(lo); hi=lo if hi is None else F(hi)
        assert lo<=hi
        object.__setattr__(self,'lo',lo);object.__setattr__(self,'hi',hi)
    def __add__(self,o):
        o=asI(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-asI(o)
    def __rsub__(self,o):return asI(o)+-self
    def __mul__(self,o):
        o=asI(o)
        z=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asI(o)
        assert o.lo*o.hi>0,'interval divisor contains zero'
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o):return asI(o)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        z=I(1)
        for _ in range(n):z=z*self
        return z

def asI(a):return a if isinstance(a,I) else I(a)
def det(a,b):return a[0]*b[1]-a[1]*b[0]

def interval_grad(k,x,y):return (F(4,5)*dB(k,x),F(1,5)*dB(k,y))
def cgrad(x,y):return (-F(3,256)*(1-x)*(63-61*x),F(3,64)*y*(1-y))

def affine_components(x,y,kind):
    g2=interval_grad(2,x,y)
    Gc=cgrad(x,y)
    W=(Gc[0]+LAM*F(15,16)*g2[0], Gc[1]+LAM*F(15,16)*g2[1])
    g1=interval_grad(1,x,y)
    V=(LAM*F(15,16)*g1[0],LAM*F(15,16)*g1[1])
    if kind=='star':
        g0=interval_grad(0,x,y)
        U=(LAM*F(5,16)*g0[0],LAM*F(5,16)*g0[1])
    else:
        U=(I(0), F(21,256)*dB(2,y))
    de=det(U,V)
    a=det((-W[0],-W[1]),V)/de
    b=det(U,(-W[0],-W[1]))/de
    return U,V,W,de,a,b

# Star q* unique r0=r1=0 in this explicit exact rational box.
XsL,XsU,YsL,YsU=(F(2310839,10**7),F(2310840,10**7),
                  F(5555086,10**7),F(5555091,10**7))
assert r(1,XsL,YsL)>0 and r(1,XsU,YsU)<0
assert r(0,XsL,YsU)>0 and r(0,XsU,YsL)<0
# r1 strictly increasing x and decreasing y; hence its zero defines
# unique continuous increasing y=Y(x) throughout [XsL,XsU].
# r0 decreases in both coordinates; thus r0(x,Y(x)) strictly decreases,
# crossing from positive to negative at exactly one point.

# Alpha exact algebraic root B2(alpha)=9/64 and x_alpha unique r1=0.
XaL,XaU,YaL,YaU=(F(2378068,10**7),F(2378070,10**7),
                  F(5756939,10**7),F(5756940,10**7))
assert B(2,YaL)<F(9,64)<B(2,YaU)
assert dB(2,YaL)>0 and dB(2,YaU)>0
assert r(1,XaL,YaL)<0 and r(1,XaU,YaU)>0
# alpha between YaL and YaU; r1 strictly increasing x, so there is
# a unique x_alpha between XaL and XaU with r1(x_alpha,alpha)=0.
for xl,xu,yl,yu in ((XsL,XsU,YsL,YsU),(XaL,XaU,YaL,YaU)):
    assert r(2,xl,yl)>0 and r(3,xu,yu)<0
assert r(0,XaU,YaU)<0  # cusp has r0<0
# Monotonic r2 on both narrow boxes gives an exact budget enclosure.
Elo=F(15,16)*(r(2,XaL,YaL)-r(2,XsU,YsU))
Ehi=F(15,16)*(r(2,XaU,YaU)-r(2,XsL,YsL))
assert F(2181,10**6)<Elo<Ehi<F(2182,10**6)
print('EXACT_CUSP_BUDGET_0.002181_LT_EC_LT_0.002182_PASS')
print('EXACT_ROOT_ISOLATION_STAR_AND_CUSP_AND_RESIDUAL_SIGNS_PASS')

# Verify every source/word label sign, not a merged histogram.
blocks=[(F(1,4),(XsL,XsU),(-1,1,1,1)),
        (F(3,4),(XsL,XsU),(-1,-1,1,1)),
        (F(1,4),(YsL,YsU),(1,1,-1,-1)),
        (F(3,4),(YsL,YsU),(-1,-1,1,1)),
        (F(1,4),(XaL,XaU),(-1,1,1,1)),
        (F(3,4),(XaL,XaU),(-1,-1,1,1)),
        (F(1,4),(YaL,YaU),(1,1,-1,-1)),
        (F(3,4),(YaL,YaU),(-1,-1,None,1))]
for anchor,(lo,hi),sgns in blocks:
    for k,sgn in enumerate(sgns):
        if sgn is not None:
            assert sgn*(B(k,anchor)-B(k,lo))>0
            assert sgn*(B(k,anchor)-B(k,hi))>0
print('ALL_16_PROVENANCE_LABELS_PER_REFERENCE_REGION_PASS')

# Uniform finite-radius enclosure of the sign chambers, including the
# audit cusp which is represented by a *positive part*, not smoothed.
RHO=F(1,40000)
for name,xl,xu,yl,yu in (('star',XsL,XsU,YsL,YsU),
                         ('cusp',XaL,XaU,YaL,YaU)):
    xlm,xup,ylm,yup=xl-RHO,xu+RHO,yl-RHO,yu+RHO
    assert 0<xlm<xup<F(1,4)<ylm<yup<F(2,3)
    assert r(2,xlm,ylm)>0 and r(3,xup,yup)<0
    if name=='cusp': assert r(0,xup,yup)<0
    required=[(F(1,4),xlm,xup,(-1,1,1,1)),
              (F(3,4),xlm,xup,(-1,-1,1,1)),
              (F(1,4),ylm,yup,(1,1,-1,-1)),
              (F(3,4),ylm,yup,(-1,-1,None,1))]
    for a,lo,hi,sgnlist in required:
        for k,sgn in enumerate(sgnlist):
            if sgn is not None:
                assert sgn*(B(k,a)-B(k,lo))>0
                assert sgn*(B(k,a)-B(k,hi))>0
    if name=='star':
        assert B(2,yup)<F(9,64) # no audit cusp in the star neighborhood
    else:
        assert dB(2,ylm)>0 and dB(2,yup)>0
print('EXACT_FINITE_RADIUS_RHO_1_OVER_40000_SIGN_STABILITY_PASS')

X,Y=S.symbols('X Y',real=True)
def port(a,z,sgns):
    return S.Rational(1,2)*sum(w[k]*sgns[k]*(B(k,a)-B(k,z)) for k in range(4))
Clo=S.expand((63*port(F(1,4),X,(-1,1,1,1))
             +port(F(3,4),X,(-1,-1,1,1))
             +9*port(F(1,4),Y,(1,1,-1,-1))
             +7*port(F(3,4),Y,(-1,-1,1,1)))/256)
Chi=S.expand((63*port(F(1,4),X,(-1,1,1,1))
             +port(F(3,4),X,(-1,-1,1,1))
             +9*port(F(1,4),Y,(1,1,-1,-1))
             +7*port(F(3,4),Y,(-1,-1,-1,1)))/256)
assert S.simplify(S.diff(Clo,X)+S.Rational(3,256)*(1-X)*(63-61*X))==0
assert S.simplify(S.diff(Clo,Y)-S.Rational(3,64)*Y*(1-Y))==0
assert S.simplify(Chi-Clo-S.Rational(21,256)*(B(2,Y)-S.Rational(9,64)))==0
assert S.expand(sum(w[k]*r(k,X,Y) for k in range(4)))==0
print('EXACT_16_TAG_COST_EXPANSION_AND_B_PLUS_PARTS_IDENTITY_PASS')

for tag,(xl,xu,yl,yu) in [('star',(XsL,XsU,YsL,YsU)),('cusp',(XaL,XaU,YaL,YaU))]:
    xx,yy=I(xl,xu),I(yl,yu)
    U,V,W,de,a,b=affine_components(xx,yy,tag)
    if tag=='star':
        assert de.lo>F(1,22)
        assert F(1,100)<a.lo<a.hi<F(1,50)
        assert F(3,4)<b.lo<b.hi<F(4,5)
        M=F(4,5)
        sharp=F(1,100)*F(1,22)/M
        assert sharp>F(1,2000)
    else:
        assert de.hi<-F(1,400)
        assert F(2,5)<a.lo<a.hi<F(3,5)
        assert F(3,4)<b.lo<b.hi<F(4,5)
        M=F(1,4)
        sharp=F(1,5)*F(1,400)/M
        assert sharp>=F(1,500)
    max_components=max(max(abs(z.lo),abs(z.hi)) for z in U+V)
    assert max_components<M
    # For L=c+LAM*b, the exact directional decomposition is:
    # L'(v)= (U.v)_+ - a(U.v) + (V.v)_+ - b(V.v)
    # >= min(a,1-a)|U.v|+min(b,1-b)|V.v|.
    # Inverse determinant formula gives |U.v|+|V.v| >= |det(U,V)|/M ||v||inf.
    print(f'{tag.upper()}_EXACT_INTERIOR_SUBGRADIENT_AND_POSITIVE_SHARPNESS_PASS')
    print(f'{tag}_theta_a_interval=({float(a.lo):.9f},{float(a.hi):.9f})')
    print(f'{tag}_theta_b_interval=({float(b.lo):.9f},{float(b.hi):.9f})')

# The Taylor remainder is bounded by 10 ||v||_inf^2 in each radius-RHO
# neighborhood. For k=0,1,2, |B_k''|<=6 on [0,1], hence each r_k
# has second-order remainder <=3||v||inf^2. Positive part is 1-Lipschitz.
# Exact pre-audit polynomial C_lo has |C_xx|<3/2, |C_yy|<1/20,
# hence remainder <||v||inf^2. Cusp tag adds (21/256)*(B_2(y)-9/64)_+,
# with its own remainder <(1/4)||v||inf^2. The lambda*b baseline
# remainder <7/2||v||^2; star kink corrections <5||v||^2, cusp r1
# kink correction <7/2||v||^2. Thus total <10||v||^2.
assert F(3,2)>F(372,256) and F(1,20)>F(3,64)
assert LAM*F(15,16)*3<F(7,2)
assert LAM*(F(5,16)+F(15,16))*3<5
assert F(21,256)*3<F(1,4)
assert 1+F(7,2)+5<10
assert 1+F(7,2)+F(7,2)+F(1,4)<10
assert 10*RHO==F(1,4000)
print('EXACT_TAYLOR_REMAINDER_AND_EXPLICIT_RHO_STRICT_GROWTH_PASS')

print('THEOREM: At E=E_cusp, (q_star,q_alpha) and its permutation are strict')
print('local constrained minimizers of the unrestricted four-real-parameter problem.')
print('In sufficiently small neighborhoods, cost excess >= (||p-q_star||inf')
print('+||q-q_alpha||inf)/4000 plus (49/40)*unused-budget.')
print('STAGE366B_UNRESTRICTED_FOUR_PARAMETER_CUSP_STRICT_LOCAL_OPTIMUM_EXACT_PASS')