#!/usr/bin/env python3
"""PREFIX-411 exact rational interval certificates and symbolic Port audit.

Model scope: external static coherent 5-Port model. All decisions below use
Fraction or SymPy exact identities; decimal output is informational only.
The analytic monotonicity proof is in the accompanying research note.
"""
from fractions import Fraction as F
from math import isqrt
from dataclasses import dataclass
import sympy as sp

@dataclass(frozen=True)
class IV:
    lo: F
    hi: F
    def __init__(self, lo, hi=None):
        object.__setattr__(self, 'lo', F(lo))
        object.__setattr__(self, 'hi', F(lo if hi is None else hi))
        assert self.lo <= self.hi
    @staticmethod
    def coerce(other):
        return other if isinstance(other, IV) else IV(other)
    def __add__(self, other):
        o = self.coerce(other)
        return IV(self.lo + o.lo, self.hi + o.hi)
    __radd__ = __add__
    def __neg__(self): return IV(-self.hi, -self.lo)
    def __sub__(self, other): return self + -self.coerce(other)
    def __rsub__(self, other): return self.coerce(other) - self
    def __mul__(self, other):
        o = self.coerce(other)
        vals = (self.lo*o.lo, self.lo*o.hi, self.hi*o.lo, self.hi*o.hi)
        return IV(min(vals), max(vals))
    __rmul__ = __mul__
    def __truediv__(self, other):
        o = self.coerce(other)
        assert o.lo > 0 or o.hi < 0, 'denominator contains zero'
        return self * IV(F(1, 1)/o.hi, F(1, 1)/o.lo)
    def __rtruediv__(self, other): return self.coerce(other) / self
    def sq(self):
        if self.lo <= 0 <= self.hi:
            return IV(0, max(self.lo*self.lo, self.hi*self.hi))
        return IV(min(self.lo*self.lo, self.hi*self.hi),
                  max(self.lo*self.lo, self.hi*self.hi))

eta=F(1, 10000)
beta=F(1, 1000000)
eps=F(1,1000000)
E=F(53,8)

# Check the global rational inequalities used for complete domain coverage.
X=F(101,2000000)  # |x| <= (eta+beta)/2
Y=F(1,5000)       # |y| < Y
Pmin=F(23)-F(3,100000)
Pmax=F(23)+F(3,100000)
Qmin=F(61,8)-F(3,100000)
Qmax=F(61,8)+F(3,100000)
assert (F(245)+F(123)*F(3,5))/16*eps < F(3,100000)
assert (F(123)+F(245)*F(3,5))/16*eps < F(3,100000)
assert (eta+F(12,1000000)+Pmax*X+E*beta)/Qmin < Y
assert X*X+Y*Y < beta
assert (Pmax/2-E)/Qmin < 1
assert X+2*Y < F(1,1000)
assert 4*F(6,5)*eps+4*(X+Y) < F(101,100000)  # |z4-(-1+6i)|
assert 8*(4*F(6,5)*eps+3*(X+Y)) < F(1,100) # |Kp,Kq - 709/32|
Dmin=Qmin*(1-X)-(Pmax-2*E)*Y
Dmax=Qmax*(1+X)+(Pmax-2*E)*Y
assert Dmin > F(762,100) and Dmax < F(763,100)
Nmin=F(799,100)*(1-X)-F(4801,100)*Y
Nmax=F(801,100)*(1+X)+F(4801,100)*Y
assert Nmin > F(797,100) and Nmax < F(803,100)
assert F(797,100)/F(763,100)>F(104,100)
assert F(803,100)/F(762,100)<F(106,100)
assert F(3899,100)-F(106,100)*F(2218,100)>15
assert F(3901,100)-F(104,100)*F(2214,100)<17
assert F(2499,100)-F(106,100)*F(2218,100)>1
assert F(2501,100)-F(104,100)*F(2214,100)<3
assert F(4799,100)*F(762,100)-F(801,100)*F(2301,100)>0
assert (-15+3*F(1000003,1000000))<0
assert F(4)-(F(141)*eta+F(43)*beta)/23-F(16)*eps>F(3999,1000)
assert F(4)-(F(792)*eta-F(176)*beta)/61<F(3999,1000)

# Exact SymPy check from the *original* complex 5x3 matrix.
I=sp.I
A=sp.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],
             [-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
a=sp.Rational(5,2)+sp.Rational(9,2)*I
b=sp.Rational(3,2)+sp.Rational(7,2)*I
d=sp.Rational(11,4)+sp.Rational(15,8)*I
e=sp.Rational(5,4)+sp.Rational(9,4)*I
assert A[:3,:].det()!=0
C=sp.simplify(A*A[:3,:].inv())
assert sp.simplify(C[3,0]-a)==0
assert sp.simplify(C[3,1]-b)==0
assert sp.simplify(C[3,2]-4*I)==0
assert sp.simplify(C[4,0]-d)==0
assert sp.simplify(C[4,1]-d)==0
assert sp.simplify(C[4,2]-e)==0
p,q,x,y=sp.symbols('p q x y', real=True)
u=p+I*q
v=x+I*y
z4=sp.expand(a+b*u+4*I*v)
z5=sp.expand(d*(1+u)+e*v)
intensity=lambda z:sp.expand_complex(z*sp.conjugate(z)).expand()
Z4R=(5+3*p-7*q)/2-4*y
Z4I=(9+7*p+3*q)/2+4*x
assert sp.simplify(intensity(z4)-(Z4R**2+Z4I**2))==0
h=sp.expand(2*x+x*x+y*y)
k=sp.expand(intensity(z5)-sp.Rational(709,32))
P=(245*(1+p)+123*q)/16
Q=(-123*(1+p)+245*q)/16
delta=sp.Rational(709,64)*(1+2*p+p*p+q*q-2) # Cu = 1+2p+r
assert sp.simplify(k-(delta+P*x+Q*y+sp.Rational(53,8)*(x*x+y*y)))==0

# Verify the derivative identity used for the monotone four-parameter theorem.
Mp=sp.diff(intensity(z4),p); Mq=sp.diff(intensity(z4),q)
Mx=sp.diff(intensity(z4),x); My=sp.diff(intensity(z4),y)
Kp=sp.diff(intensity(z5),p); Kq=sp.diff(intensity(z5),q)
D=Q*(1+x)+(2*sp.Rational(53,8)-P)*y
N=My*(1+x)-Mx*y
assert sp.simplify(N.subs({p:0,q:1})-8*(1+x-2*y))==0
assert sp.simplify(D.subs({p:0,q:1})-(61*(1+x)-78*y)/8)==0
Lp=sp.factor((Mp-N*Kp/D).subs({p:0,q:1}))
Lq=sp.factor((Mq-N*Kq/D).subs({p:0,q:1}))
S=sp.factor(Lp-Lq/2)
S_target=(1216*x*x-1704*x*y+3031*x+128*y*y-2506*y+1815)/(2*(61*x-78*y+61))
assert sp.simplify(S-S_target)==0

# Exact algebraic root isolation: the 409 root T* is polynomial and monotone.
def pol(t): return F(196100000000)*t*t-F(297747300000)*t+F(6389)
lo=F(0);hi=beta
assert pol(lo)>0 and pol(hi)<0
for _ in range(135):
    mid=(lo+hi)/2
    if pol(mid)>0:lo=mid
    else:hi=mid
assert pol(lo)>0 and pol(hi)<0
T=IV(lo,hi)
x0=(eta-T)/2
y0=(39*T-84*eta)/61
Siv=(1216*x0.sq()-1704*x0*y0+3031*x0+128*y0.sq()-2506*y0+1815)/(2*(61*x0-78*y0+61))
assert F('14.87775641266')<Siv.lo<=Siv.hi<F('14.87775641267')

# Exact sqrt interval via integer arithmetic: q^2=1-eps-eps^2.
q_squared=1-eps-eps*eps
scale=10**65
n=isqrt((q_squared.numerator*scale*scale)//q_squared.denominator)
ql=F(n,scale);qu=F(n+1,scale)
assert ql*ql<=q_squared<qu*qu
QI=IV(ql,qu)
pp=IV(eps)
Pu=(245*(1+pp)+123*QI)/16
Qu=(-123*(1+pp)+245*QI)/16
deltau=F(709,64)*eps # s=2+eps, exact

# F(t)=Phi_u(t)-t is strictly decreasing: |Phi_t|<1/1000.
def phi(t):
    XX=(eta-IV(t))/2
    YY=(eta-deltau-Pu*XX-E*t)/Qu
    return XX.sq()+YY.sq()
lo=F(0);hi=beta
assert (phi(lo)-lo).lo>0
assert (phi(hi)-hi).hi<0
for _ in range(132):
    mid=(lo+hi)/2
    test=phi(mid)-mid
    if test.lo>0:lo=mid
    elif test.hi<0:hi=mid
    else:break
assert (phi(lo)-lo).lo>0
assert (phi(hi)-hi).hi<0
TT=IV(lo,hi)
XX=(eta-TT)/2
YY=(eta-deltau-Pu*XX-E*TT)/Qu
assert TT.lo>0 and TT.hi<beta
Zr=(5+3*pp-7*QI)/2-4*YY
Zi=(9+7*pp+3*QI)/2+4*XX
Kappa=41-(Zr.sq()+Zi.sq())
assert F('3.998686823488066')<Kappa.lo<=Kappa.hi<F('3.998686823488068')

# Explicit source is Y=A[:3]^{-1}(1,u,v); determinant and observation identities above
# guarantee the *same* source generates all Port observations.
print('PASS_PREFIX411_GLOBAL_MONOTONICITY_RATIONAL_GUARDS')
print('PASS_PREFIX411_ORIGINAL_A_AND_DERIVATIVE_IDENTITIES')
print('PASS_PREFIX411_KAPPA_EXACT_INTERVAL')
print('KAPPA_ENCLOSED',float(Kappa.lo),float(Kappa.hi))
print('SLOPE_ENCLOSED',float(Siv.lo),float(Siv.hi))
print('t_enclosed_width < 1e-36:',TT.hi-TT.lo<F(1,10**36))
