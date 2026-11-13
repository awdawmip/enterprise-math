#!/usr/bin/env python3
"""Stage319-B exact rational boundary extension and endpoint-curvature check.

Stage318-B's full-square exterior cover, local sharpness and R-box signs/derivatives
are prior proved premises at immutable research commit e3517f652de0c11bae9cfd39cc1ebd1dc1459a22;
this program verifies the NEW arithmetic implications and algebraic endpoint jets.
It does NOT independently re-run Stage318's 274-leaf global certificate.
"""
from fractions import Fraction as F

class I:
    __slots__ = ('lo','hi')
    def __init__(self, lo, hi=None):
        self.lo=F(lo)
        self.hi=self.lo if hi is None else F(hi)
        assert self.lo<=self.hi
    @staticmethod
    def of(z):
        return z if isinstance(z,I) else I(z)
    def __add__(self,z):
        z=I.of(z); return I(self.lo+z.lo,self.hi+z.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,z): return self+(-I.of(z))
    def __rsub__(self,z): return I.of(z)+(-self)
    def __mul__(self,z):
        z=I.of(z)
        xs=[self.lo*z.lo,self.lo*z.hi,self.hi*z.lo,self.hi*z.hi]
        return I(min(xs),max(xs))
    __rmul__=__mul__
    def reciprocal(self):
        assert not (self.lo<=0<=self.hi), 'interval denominator spans zero'
        return I(F(1,1)/self.hi,F(1,1)/self.lo)
    def __truediv__(self,z): return self*I.of(z).reciprocal()
    def __rtruediv__(self,z): return I.of(z)*self.reciprocal()
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0: return I(1)
        if n%2==0 and self.lo<=0<=self.hi:
            return I(0,max(self.lo**n,self.hi**n))
        if n%2==0 and self.hi<0:
            return I(self.hi**n,self.lo**n)
        return I(self.lo**n,self.hi**n)
    def in_open(self,lo,hi): return F(lo)<self.lo and self.hi<F(hi)

a_lo=F(768916059144478,10**15)
a_hi=F(768916059144479,10**15)
y_lo=F(555508857277,10**12)
y_hi=F(555508857278,10**12)
def poly(a):
    return (F(41,16)-4*a*a)**3-(F(61,32)-4*a**3)**2
assert poly(a_lo)*poly(a_hi)<0
q_lo=F(41,16)-4*a_hi*a_hi
q_hi=F(41,16)-4*a_lo*a_lo
assert 0 < (1-y_hi)**2 < q_lo <= q_hi < (1-y_lo)**2
x=I(1-a_hi,1-a_lo)
y=I(y_lo,y_hi)

delta=F(1,5000000)
R_xlo,R_xhi=F(231,1000),F(2312,10000)
R_ylo,R_yhi=F(555,1000),F(556,1000)
sharp_distance=384*delta
margins=[x.lo-R_xlo,R_xhi-x.hi,y.lo-R_ylo,R_yhi-y.hi]
assert all(m>sharp_distance for m in margins)
exterior_gap=F(5,16)*F(1,200000)
assert exterior_gap>delta
L=F(1,800000)
assert L<min(x.lo-R_xlo,R_xhi-x.hi)
assert 12*L<min(y.lo-R_ylo,R_yhi-y.hi)
assert F(18,100)*L>delta
assert F(1,10**8)*20==delta

def B1p(z): return 1-4*z+3*z*z
def B1pp(z): return -4+6*z
def B2p(z): return 2*z-3*z*z
def B2pp(z): return 2-6*z
def Ap(z): return -6*z+6*z*z
def App(z): return -6+12*z
v=-4*B1p(x)/B1p(y)
w=-(4*B1pp(x)+B1pp(y)*v*v)/B1p(y)
Bp=F(3,16)*(4*B2p(x)+B2p(y)*v)
Bpp=F(3,16)*(4*B2pp(x)+B2pp(y)*v*v+B2p(y)*w)
cx=(-189*(1-x)**2+Ap(x))/256
cy=-2*Ap(y)/256
cxx=(378*(1-x)+App(x))/256
cyy=-2*App(y)/256
Ep=cx+cy*v
Epp=cxx+cyy*v*v+cy*w
curvature=(Epp*Bp-Ep*Bpp)/(Bp**3)
kappa=-Ep/Bp
assert Bp.lo>0
assert kappa.in_open(F(119791766,10**8),F(119791767,10**8))
assert curvature.in_open(F(-39656,1000),F(-39655,1000))
assert curvature.in_open(F(-39655469,10**6), F(-39655468,10**6))

print('Stage319-B source dependency: Stage318-B @ e3517f652de0c11bae9cfd39cc1ebd1dc1459a22')
print('root polynomial signs:', ('+' if poly(a_lo)>0 else '-'), ('+' if poly(a_hi)>0 else '-'))
print('updated public budget: 1/5000000 = 20 * 1/100000000')
print('minimum R boundary margin (decimal display):',format(float(min(margins)),'.12g'))
print('local sharpness displacement bound:',sharp_distance)
print('outside-box b gap:',exterior_gap,' > updated budget:',delta)
print('four kink arc length:',L,'minimum certified b increment:',F(18,100)*L)
print('kappa endpoint interval:',format(float(kappa.lo),'.12f'),format(float(kappa.hi),'.12f'))
print('C3 second derivative endpoint interval:',format(float(curvature.lo),'.12f'),format(float(curvature.hi),'.12f'))
print('all interval signs and denominator exclusions are exact Fraction comparisons')
print('STAGE319B_TWENTYFOLD_GLOBAL_GERM_AND_QUADRATIC_ALLOCATION_GAP_PASS')
