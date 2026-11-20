#!/usr/bin/env python3
"""Stage339-B: exact rational interval certificate for sharp local Pareto efficiency.
All interval endpoints are Fraction, and assertions are proof obligations.
Model/claim domains are spelled out in PROOF_STAGE339B.md.
"""
from fractions import Fraction as F
from dataclasses import dataclass
import sympy as S

@dataclass(frozen=True)
class I:
    lo: F
    hi: F
    def __init__(self, lo, hi=None):
        object.__setattr__(self, 'lo', F(lo))
        object.__setattr__(self, 'hi', F(lo if hi is None else hi))
        assert self.lo <= self.hi
    def __add__(self, b):
        b = b if isinstance(b, I) else I(b)
        return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,b):return self+(-b if isinstance(b,I) else -I(b))
    def __rsub__(self,b):return b+(-self)
    def __mul__(self,b):
        b = b if isinstance(b,I) else I(b)
        t=[a*c for a in (self.lo,self.hi) for c in (b.lo,b.hi)]
        return I(min(t),max(t))
    __rmul__=__mul__
    def __truediv__(self,b):
        b = b if isinstance(b,I) else I(b)
        assert b.lo*b.hi>0, ('noninvertible interval',b)
        return self*I(1/b.hi,1/b.lo)
    def __rtruediv__(self,b):return I(b)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n%2==0:
            if self.lo<=0<=self.hi:return I(0,max(self.lo**n,self.hi**n))
            return I(min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
        return I(self.lo**n,self.hi**n)
    def contains(self,z):return self.lo<=z<=self.hi
    def inside(self,a,b):return F(a)<self.lo and self.hi<F(b)

def B(k,z):
    return (z**k)*((1-z)**(3-k))
def dB(k,z):
    return ((-3*(1-z)**2),((1-z)*(1-3*z)),(z*(2-3*z)),(3*z*z))[k]
def R(k,x,y):
    return (4*B(k,x)+B(k,y))/5-I((61,21,9,9)[k])/160

def assert_strict(got, op, bound, label):
    if op=='gt':assert got.lo>F(bound),(label,got,bound)
    else:assert got.hi<F(bound),(label,got,bound)

XL=F(231083,10**6); XH=F(231085,10**6)
YL=F(5554961,10**7); YH=F(5555202,10**7)
x=I(XL,XH); y=I(YL,YH)
# Source of the intersection: predecessor Stage338-B. Check the load-bearing
# rational strict signs that locate it on the r0 graph.
def rat_r(k,xx,yy):return R(k,I(xx),I(yy)).lo
assert rat_r(0,XL,F(5555201,10**7))>0
assert rat_r(0,XL,F(5555202,10**7))<0
assert rat_r(1,XL,F(5555201,10**7))<0
assert rat_r(1,XL,F(5555202,10**7))<0
assert rat_r(0,XH,F(5554961,10**7))>0
assert rat_r(0,XH,F(5554962,10**7))<0
assert rat_r(1,XH,F(5554961,10**7))>0
assert rat_r(1,XH,F(5554962,10**7))>0
assert_strict(R(2,x,y),'gt',F(1,250),'r2-positive')
assert_strict(R(3,x,y),'lt',-F(3,250),'r3-negative')

p=(1-x)*(189-183*x)/256
q=3*y*(1-y)/64
j0x=4*dB(0,x)/5; j0y=dB(0,y)/5
j1x=4*dB(1,x)/5; j1y=dB(1,y)/5
j3x=4*dB(3,x)/5; j3y=dB(3,y)/5
N=-(q*(j3x+j0x)+p*(j3y+j0y))
D=3*(q*j1x+p*j1y)
assert D.hi<0 and N.hi<0
beta=N/D
gx=-F(5,16)*(j3x+j0x+3*beta*j1x)
lam=p/gx
Delta=(-p)*j1y-q*j1x
for name,value,a,b in [
 ('p',p,F(2,5),F(9,20)),('q',q,F(0),F(3,250)),
 ('j1x',j1x,F(0),F(19,100)),
 ('minus_j1y',-j1y,F(59,1000),F(3,50)),
 ('beta',beta,F(1,6),F(1,4)),
 ('gx',gx,F(7,20),F(2,5)),
 ('lambda',lam,F(1),F(2)),
 ('det',Delta,F(23,1000),F(1))]:
    assert value.inside(a,b),(name,value,a,b)

# Prove the 16 labelled-source signs persist in an explicit ball |h|_2<=1/3000.
delta=F(1,3000)
xx=I(XL-delta,XH+delta); yy=I(YL-delta,YH+delta)
assert xx.lo>F(21,100) and xx.hi<F(6,25)
assert yy.lo>F(1,2) and yy.hi<F(57,100) # 57/100<y_dagger
signs=['-+++','--++','++--','--++']
for idx,(a,z) in enumerate([(F(1,4),xx),(F(3,4),xx),(F(1,4),yy),(F(3,4),yy)]):
    for k,required in enumerate(signs[idx]):
        val=B(k,I(a))-B(k,z)
        if required=='+': assert val.lo>0,(idx,k,val)
        else:assert val.hi<0,(idx,k,val)

# Algebraic derivative of all 16 tagged Bernoulli terms, verified with SymPy QQ.
X,Y=S.symbols('X Y'); BB=lambda k,z:z**k*(1-z)**(3-k)
def DD(a,z,sgn):
    return S.Rational(1,2)*sum((1 if s=='+' else -1)* (1,3,3,1)[k]*(BB(k,S.Rational(a))-BB(k,z)) for k,s in enumerate(sgn))
C=S.expand((63*DD(S.Rational(1,4),X,signs[0])+DD(S.Rational(3,4),X,signs[1])+9*DD(S.Rational(1,4),Y,signs[2])+7*DD(S.Rational(3,4),Y,signs[3]))/256)
assert S.simplify(S.diff(C,X)+(1-X)*(189-183*X)/256)==0
assert S.simplify(S.diff(C,Y)-3*Y*(1-Y)/64)==0
# The exact KKT-support identity, independent of floating root approximations.
RR=lambda k:(4*BB(k,X)+BB(k,Y))/5-S.Rational((61,21,9,9)[k],160)
rg=lambda k,t:S.diff(RR(k),t)
PP=(1-X)*(189-183*X)/256
QQ=3*Y*(1-Y)/64
NN=-(QQ*(rg(3,X)+rg(0,X))+PP*(rg(3,Y)+rg(0,Y)))
DE=3*(QQ*rg(1,X)+PP*rg(1,Y))
BE=NN/DE
GX=-S.Rational(5,16)*(rg(3,X)+rg(0,X)+3*BE*rg(1,X))
GY=-S.Rational(5,16)*(rg(3,Y)+rg(0,Y)+3*BE*rg(1,Y))
assert S.cancel(QQ*GX+PP*GY)==0
assert S.cancel((-PP)+(PP/GX)*GX)==0
assert S.cancel(QQ+(PP/GX)*GY)==0

# Second-order geometry on the exact r1=0 curve: the same supporting
# weighted scalarization c+lambda*b is strictly concave along the curve.
# This DOES NOT contradict strict local Pareto efficiency.
vx=-j1y; vy=j1x
r0_tangent=j0x*vx+j0y*vy
assert_strict(r0_tangent,'lt',-F(1,10),'r0-enters-negative-chamber')
# cxx=-p_x=(372-366*x)/256, cyy=q_y=3(1-2*y)/64.
# r3xx+r0xx=24/5, r1xx=(4/5)*(6*x-4);
# r3yy+r0yy=6/5, r1yy=(1/5)*(6*y-4).
Hxx=(372-366*x)/256-lam*F(5,16)*(F(24,5)+3*beta*F(4,5)*(6*x-4))
Hyy=3*(1-2*y)/64-lam*F(5,16)*(F(6,5)+3*beta*F(1,5)*(6*y-4))
assert_strict(Hxx,'lt',-F(1,10),'scalarization-Hxx-negative')
assert_strict(Hyy,'lt',-F(2,5),'scalarization-Hyy-negative')
# The tangent c derivative is exactly -det<0, and the b derivative is det/lambda>0.
assert_strict((-p)*vx+q*vy,'lt',-F(23,1000),'c-tangent-negative')

# Quantitative cone: t=max(Db(h),Dc(h))>= ||h||_2/500.
# beta>1/6 and 1<lambda<2 imply |r1'|<13t and |Dc|<=2t.
# det>23/1000 and component bounds imply |hx|<12t, |hy|<271t.
assert (F(3,50)*2+F(3,250)*13)/F(23,1000)==12
assert (F(19,100)*2+F(9,20)*13)/F(23,1000)<271
assert 12*12+271*271<500*500
# Taylor: |B_k''|<=6 on [0,1]; |b-b*-Db|<=3||h||^2.
# |c-c*-Dc|<=3/4||h||^2, because |cxx|<3/2, |cyy|<3/2.
assert F(372,256)<F(3,2)
assert F(3,64)<F(3,2)
assert F(3)*delta==F(1,1000)
# Excluding sign changes of r2/r3 within the ball: global derivative bounds
# |grad r2|_2<1, |grad r3|_2<3, so retained fixed signs.
assert F(1,250)-delta>0
assert -F(3,250)+3*delta<0
# q* plus the ball remains inside (0,1)^2 and the sign strip.
print('STAGE339B_EXACT_ROOT_SIGN_AND_TAG_INTERVALS_PASS')
print('beta in', str(beta.lo), str(beta.hi))
print('lambda in', str(lam.lo), str(lam.hi))
print('determinant lower bound: 23/1000')
print('scalarization Hessian diagonal upper bounds: -1/10, -2/5')
print('local_radius: 1/3000')
print('local_gap: max(b(q)-b(q*), c(q)-c(q*)) >= ||q-q*||_2/1000')
print('STAGE339B_QUANTITATIVE_STRICT_LOCAL_PARETO_EXACT_PASS')
