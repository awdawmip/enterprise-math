#!/usr/bin/env python3
"""PREFIX-416 exact rational interval certificate; floating point is display only."""
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt

@dataclass(frozen=True)
class J:
    lo: F
    hi: F
    def __init__(self, lo, hi=None):
        lo=F(lo); hi=lo if hi is None else F(hi)
        assert lo<=hi
        object.__setattr__(self,'lo',lo);object.__setattr__(self,'hi',hi)
    def __add__(self, other):
        other=j(other);return J(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self):return J(-self.hi,-self.lo)
    def __sub__(self,other):return self+-j(other)
    def __rsub__(self,other):return j(other)+-self
    def __mul__(self,other):
        other=j(other);v=[a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return J(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,other):
        other=j(other);assert other.lo>0 or other.hi<0
        return self*J(1/other.hi,1/other.lo)
    def __rtruediv__(self,other):return j(other)/self
    def __repr__(self):return f'[{float(self.lo):.16g}, {float(self.hi):.16g}]'

def j(x):return x if isinstance(x,J) else J(x)
def sq(x):
    x=j(x)
    if x.lo>=0:return J(x.lo*x.lo,x.hi*x.hi)
    if x.hi<=0:return J(x.hi*x.hi,x.lo*x.lo)
    return J(0,max(x.lo*x.lo,x.hi*x.hi))
def sqrt_iv(x,scale=10**25):
    x=j(x);assert x.lo>=0
    def floor(v):return F(isqrt(v.numerator*scale*scale//v.denominator),scale)
    return J(floor(x.lo),floor(x.hi)+F(1,scale))
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def assert_between(x,lo,hi):
    x=j(x);assert F(lo)<x.lo and x.hi<F(hi),(lo,x,hi)

B=F(37577,64);E=F(53,8);beta=F(1,10**6)
lo=F(1806822353106,10**15);hi=F(1806822353107,10**15)
tlo=F(865703047568,10**18);thi=F(865703047570,10**18)
def f(eta,t):return (eta+t)**2/4+F(45,368)**2*(t-eta)**2-t
assert f(lo,tlo)>0 and f(hi,thi)<0
def qplus(eta):
    C=j(eta)-E*beta
    S=sqrt_iv(j(B*beta)-sq(C))
    return (1165*C+182*S)/B+16*beta
def qminus(eta,t):return (141*j(eta)+43*j(t))/23
assert (qplus(lo)-qminus(lo,J(tlo,thi))).lo>0
assert (qplus(hi)-qminus(hi,J(tlo,thi))).hi<0
eta=J(lo,hi);t=J(tlo,thi);C=eta-E*beta;S=sqrt_iv(B*beta-sq(C))
xp=(23*C+F(61,8)*S)/B
yp=(F(61,8)*C-23*S)/B
xm=-(eta+t)/2
ym=F(45,368)*(t-eta)
assert xp.lo>0 and yp.hi<0 and xm.hi<0 and ym.hi<0
assert (2*xp+beta).hi<lo
assert sq(xm).hi+sq(ym).hi<beta
gP=(48+32*xp,8+32*yp)
gKp=(23+F(53,4)*xp,F(61,8)+F(53,4)*yp)
gT=(2*xp,2*yp)
denp=det(gKp,gT)
assert denp.lo>0 or denp.hi<0
lp=det(gP,gT)/denp
mp=det(gKp,gP)/denp
assert lp.lo>0 and mp.lo>0
gM=(-24-32*xm,48-32*ym)
gHm=(-2-2*xm,-2*ym)
gKm=(-F(61,8)-F(53,4)*xm,23-F(53,4)*ym)
denm=det(gHm,gKm)
assert denm.lo>0 or denm.hi<0
lh=det(gM,gKm)/denm
lk=det(gHm,gM)/denm
assert lh.lo>0 and lk.lo>0
P4r=-8*xp+20*yp-7
P4s=14*xp-6*yp+F(39,2)
Pkr=-F(61,16)*xp+F(23,2)*yp
Pks=F(245,32)*xp-F(123,32)*yp+F(709,64)
M4r=-20*xm-8*ym-3
M4s=14*xm-6*ym+F(39,2)
Mkr=-F(23,2)*xm-F(61,16)*ym
Mks=F(245,32)*xm-F(123,32)*ym+F(709,64)
P_r=P4r-lp*Pkr
P_s=P4s-lp*Pks
M_r=-M4r+lk*Mkr
M_s=-M4s+lk*Mks
assert P_r.hi<0 and P_s.hi<0 and M_r.lo>0 and M_s.lo>0
Aplus=-P_r-P_s
Aminus=M_r+M_s
den=(lh+lk)-lp
assert den.lo>4
crossover_prime=(Aplus-Aminus)/den
assert_between(crossover_prime,F(6241785101433,10**13),F(6241785101437,10**13))
for name,z in [('eta_cross',eta),('t_cross',t),('plus_k_multiplier',lp),('plus_t_multiplier',mp),('minus_h_multiplier',lh),('minus_k_multiplier',lk),('plus_q_r',P_r),('plus_q_s',P_s),('minus_q_r',M_r),('minus_q_s',M_s),('d_eta_cross_d_epsilon_at_zero',crossover_prime)]:
    print(name,repr(z))
print('PASS_PREFIX416_EXACT_RATIONAL_KKT_ACTIVE_CORNERS_AND_RIGHT_SLOPE')
