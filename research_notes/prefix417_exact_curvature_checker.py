"""PREFIX-417: exact rational interval certificate for local branch-switch curvature.
Model: auxiliary static five-port complex-amplitude problem; not native P000/BRC.
Requires SymPy; all inequality decisions use Fraction and integer isqrt.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
import sympy as S

E, H, T = S.symbols('eps eta t', real=True)
beta = S.Rational(1, 10**6)

def port(w):
    p, q = (245 + 123*w)/16, (-123 + 245*w)/16
    a, b = 36 + 12*w, -20 + 28*w
    j = (53 - 8*w + 29*w*w)/2
    c = S.Rational(709, 64)*(w*w-1)
    return p, q, a, b, j, c

wp, wm = S.sqrt(1-E), -S.sqrt(1+E)
pp, qp, ap, bp, jp, cp = port(wp)
pm, qm, am, bm, jm, cm = port(wm)
n = pp*pp + qp*qp
b = ap*pp + bp*qp
c = ap*qp - bp*pp
k = H - cp - S.Rational(53,8)*beta
d = n*beta-k*k
l = jp-37+16*beta+b*k/n
coef = c/n
plus = l+coef*S.sqrt(d)
x0, x1 = -H/2, S.Rational(-1,2)
y0 = (-H-cm-pm*x0)/qm
y1 = (-pm*x1-S.Rational(53,8))/qm
f2, f1, f0 = x1*x1+y1*y1, 2*(x0*x1+y0*y1)-1, x0*x0+y0*y0
f = f2*T*T+f1*T+f0
r0 = 45-jm-am*x0-bm*y0
r1 = -am*x1-bm*y1-16
minus = r0+r1*T

# All the derivatives are evaluated at eps=0 before interval evaluation.
def at0(expr):
    return S.factor(expr.subs(E,0))
def deriv(expr, ne, nh, nt=0):
    return at0(S.diff(expr, E, ne, H, nh, T, nt))

@dataclass(frozen=True)
class I:
    lo: F
    hi: F
    def __post_init__(self):
        assert self.lo <= self.hi
    def __add__(self, other):
        other=iv(other); return I(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self, other): return self+(-iv(other))
    def __rsub__(self,other): return iv(other)-self
    def __mul__(self,other):
        other=iv(other)
        v=(self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi)
        return I(min(v),max(v))
    __rmul__=__mul__
    def inverse(self):
        assert self.lo>0 or self.hi<0
        return I(1/self.hi,1/self.lo)
    def __truediv__(self,other): return self*iv(other).inverse()
    def __rtruediv__(self,other): return iv(other)/self
    def __pow__(self,n):
        assert isinstance(n,int)
        if n<0: return (self**(-n)).inverse()
        if n==0: return iv(1)
        if n%2: return I(self.lo**n,self.hi**n)
        if self.lo<=0<=self.hi: return I(F(0),max(abs(self.lo),abs(self.hi))**n)
        return I(min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
def iv(x):
    if isinstance(x,I): return x
    y=F(x);return I(y,y)

scale=10**32

def floor_sqrt_fraction(x):
    return F(isqrt(x.numerator*scale*scale//x.denominator),scale)

def sqrt_interval(x):
    assert x.lo>=0
    low=floor_sqrt_fraction(x.lo)
    hi0=floor_sqrt_fraction(x.hi)
    high=hi0 if hi0*hi0==x.hi else hi0+F(1,scale)
    return I(low,high)

def ev(expr,values):
    if expr in values: return values[expr]
    if expr.is_Rational: return iv(F(int(expr.p),int(expr.q)))
    if expr.is_Add: return sum((ev(v,values) for v in expr.args),iv(0))
    if expr.is_Mul:
        result=iv(1)
        for v in expr.args: result=result*ev(v,values)
        return result
    if expr.is_Pow:
        v=ev(expr.base,values)
        if expr.exp.is_Integer:return v**int(expr.exp)
        if expr.exp.q==2:return sqrt_interval(v)**int(expr.exp.p)
    raise ValueError(f'unsupported SymPy operation: {expr}')

eta_lo,eta_hi=F(1806822353106,10**15),F(1806822353107,10**15)
t_lo,t_hi=F(865703047568,10**18),F(865703047570,10**18)
P = S.Poly(411370922419157000000000000000000000000*H**4
+3406648973825365305852000000000000000000*H**3
+7207920358822113492588156702000000000000*H**2
-15929217691721140762689459588000000*H
-23522344829723509499221428663222123,H)
def pvalue(v):
    return sum(F(int(a))*v**(4-i) for i,a in enumerate(P.all_coeffs()))
def fvalue(e,t):return 35881*(e*e+t*t)+63662*e*t-135424*t
assert pvalue(eta_lo)<0<pvalue(eta_hi)
assert fvalue(eta_lo,t_lo)>0>fvalue(eta_hi,t_hi)
# The positive root of the quartic is unique by Descartes; F_t<0 in the small box.
assert S.Poly(fvalue(H,T),T).degree()==2

# Resultant reduction at eps=0: independently reconstruct PREFIX-413 polynomial.
wplus,wminus=S.symbols('wp wm',real=True)
Pp,Qp,Ap,Bp,Jp,Cp=port(wplus)
Pm,Qm,Am,Bm,Jm,Cm=port(wminus)
Np=Pp*Pp+Qp*Qp
bp=Ap*Pp+Bp*Qp
cp=Ap*Qp-Bp*Pp
K=H-Cp-S.Rational(53,8)*beta
D=Np*beta-K*K
L=Jp-37+16*beta+bp*K/Np
C=cp/Np
xx0,xx1=-H/2,S.Rational(-1,2)
yy0=(-H-Cm-Pm*xx0)/Qm
yy1=(-Pm*xx1-S.Rational(53,8))/Qm
A2=xx1*xx1+yy1*yy1
A1=2*(xx0*xx1+yy0*yy1)-1
A0=xx0*xx0+yy0*yy0
R0=45-Jm-Am*xx0-Bm*yy0
R1=-Am*xx1-Bm*yy1-16
Z=L-R0
h2=A2*C*C
h1=C*(2*A2*Z+A1*R1)
h0=A2*Z*Z+A1*R1*Z+A0*R1*R1
res=(h0+h2*D)**2-h1*h1*D
poly=S.Poly(S.cancel(res.subs({wplus:1,wminus:-1})),H)
primitive=poly.clear_denoms()[1].primitive()[1]
if primitive.LC()<0:primitive=-primitive
assert S.expand(primitive.as_expr()-P.as_expr())==0
print('PASS_PREFIX417_RESULTANT_REDUCES_TO_PREFIX413_QUARTIC')

box={H:I(eta_lo,eta_hi),T:I(t_lo,t_hi)}
val=lambda expression:ev(expression,box)
ft=val(deriv(f,0,0,1))
ftt=val(deriv(f,0,0,2))
fte=val(deriv(f,1,0,1))
fth=val(deriv(f,0,1,1))
rt=val(deriv(minus,0,0,1))
rte=val(deriv(minus,1,0,1))
rth=val(deriv(minus,0,1,1))
assert ft.hi<0
te=-val(deriv(f,1,0))/ft
th=-val(deriv(f,0,1))/ft
tee=-(val(deriv(f,2,0))+2*fte*te+ftt*te**2)/ft
teh=-(val(deriv(f,1,1))+fte*th+fth*te+ftt*te*th)/ft
thh=-(val(deriv(f,0,2))+2*fth*th+ftt*th**2)/ft
ge=val(deriv(plus,1,0))-(val(deriv(minus,1,0))+rt*te)
gh=val(deriv(plus,0,1))-(val(deriv(minus,0,1))+rt*th)
gee=val(deriv(plus,2,0))-(val(deriv(minus,2,0))+2*rte*te+rt*tee)
geh=val(deriv(plus,1,1))-(val(deriv(minus,1,1))+rte*th+rth*te+rt*teh)
ghh=val(deriv(plus,0,2))-(val(deriv(minus,0,2))+2*rth*th+rt*thh)
assert gh.hi<0
first=-ge/gh
second=-(gee+2*geh*first+ghh*first**2)/gh
assert F(6241785101433,10**13)<first.lo<=first.hi<F(6241785101437,10**13)
assert F(-422827868028,10**9)<second.lo<=second.hi<F(-422827868026,10**9)
print('PASS_PREFIX417_EXACT_RATIONAL_INTERVAL_SECOND_DERIVATIVE')
print('eta_first interval approximately',float(first.lo),float(first.hi))
print('eta_second interval approximately',float(second.lo),float(second.hi))
print('Curvature theorem: -422.827868028 < eta_cross_second(0+) < -422.827868026')
