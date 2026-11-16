"""R599: exact rational intervals for the first auxiliary conjugate root-pair's
root drift and positive spectral-energy expansion. Standard library only.
The mathematical inputs are the frozen R462 auxiliary observer and R597/R598.
All PASS decisions are Fraction comparisons (never binary floating point).
"""
from fractions import Fraction as Q
from math import factorial

N = 44
rad = Q(1, 10**24)
center_re = Q('6.33923451020742194898840830174914205')
center_im = Q('9.48095171645470905742279785138458204')

class Ball:
    """Complex Euclidean closed ball, rational center and conservative radius."""
    def __init__(self, re=0, im=0, err=0):
        self.a, self.b, self.e = Q(re), Q(im), Q(err)
        assert self.e >= 0
    def __add__(self, other):
        t = lift(other)
        return Ball(self.a+t.a, self.b+t.b, self.e+t.e)
    __radd__ = __add__
    def __neg__(self): return Ball(-self.a, -self.b, self.e)
    def __sub__(self, other): return self + -lift(other)
    def __mul__(self, other):
        t = lift(other)
        err = (abs(self.a)+abs(self.b))*t.e + (abs(t.a)+abs(t.b))*self.e + self.e*t.e
        return Ball(self.a*t.a-self.b*t.b, self.a*t.b+self.b*t.a, err)
    __rmul__ = __mul__
    def inv(self):
        d = max(abs(self.a), abs(self.b)) - self.e
        assert d > self.e
        n = self.a*self.a+self.b*self.b
        return Ball(self.a/n, -self.b/n, self.e/(d*(d-self.e)))
    def __truediv__(self, other): return self * lift(other).inv()
    def __pow__(self, exp):
        assert isinstance(exp,int) and exp >= 0
        result, base = Ball(1), self
        while exp:
            if exp & 1: result = result * base
            base = base * base
            exp //= 2
        return result
    def box(self, a,b,c,d):
        return self.a-self.e > Q(a) and self.a+self.e < Q(b) and self.b-self.e > Q(c) and self.b+self.e < Q(d)
    def approximate(self): return (float(self.a), float(self.b), float(self.e))

def lift(x): return x if isinstance(x,Ball) else Ball(x)

def a_correction(j, order):
    if order == 0: return Q(1)
    if order == 1: return Q(0) if j == 0 else Q(15*j+3,8)
    if order == 2:
        p = Q(-32*j**3+501*j**2-349*j-18,384)
        return p + (Q(3,64) if j==0 else Q(15,64) if j==1 else Q(0))
    if order == 3:
        p = Q(-160*j**4+359*j**3-1814*j**2+1159*j+36,1024)
        return p + (Q(-9,256) if j==0 else Q(105,256) if j==1 else Q(-105,512) if j==2 else Q(0))
    raise ValueError(order)

# Uniform bound for order <= 3 and derivative <= 3, |z| <= 12.
tail_index = N+1
tail = Q(192*(tail_index+1)**8*96**tail_index, factorial(2*tail_index+4))
assert Q(96*(tail_index+2)**8, (tail_index+1)**8*(2*tail_index+5)*(2*tail_index+6)) < Q(1,2)

def series(order,derivative,z):
    s=Ball()
    for j in range(derivative,N+1):
        factor = Q(24*(-8)**j*factorial(j),factorial(2*j+4)*factorial(j-derivative))*a_correction(j,order)
        if factor: s += factor*(z**(j-derivative))
    return s+Ball(0,0,tail)

C=Ball(center_re,center_im)
Z=Ball(center_re,center_im,rad)
assert center_re**2+center_im**2 < (12-rad)**2
Fc = series(0,0,C)
F1c = series(0,1,C)
F2 = series(0,2,Z)
assert Fc.a.__abs__()+abs(Fc.b)+Fc.e < Q(1,10**30)
assert max(abs(F1c.a), abs(F1c.b))-F1c.e > Q(1,25)
assert abs(F2.a)+abs(F2.b)+F2.e < 1
assert abs(Fc.a)+abs(Fc.b)+Fc.e + rad*rad/2 < rad/25
print('R599_ROOT_DISC_REUSED_AND_RECHECKED_PASS')

F1,F3=series(0,1,Z),series(0,3,Z)
G,G1,G2 = series(1,0,Z),series(1,1,Z),series(1,2,Z)
H,H1,J=series(2,0,Z),series(2,1,Z),series(3,0,Z)
ell=-G/F1
m=-(H+G1*ell+F2*ell*ell/2)/F1
n=-(J+H1*ell+G1*m+G2*ell*ell/2+F2*ell*m+F3*ell*ell*ell/6)/F1
assert ell.box('-4.387517','-4.387514','-17.129121','-17.129117')
assert m.box('32.713313','32.713318','20.925232','20.925237')
assert n.box('-93.087448','-93.087445','24.149782','24.149786')
print('R599_FIRST_SECOND_THIRD_DRIFT_RATIONAL_BOX_PASS')

# The coefficient of k^-p in the fixed conjugate pair contribution
# V_k(pair) = 2(Im(z_k))^2 / ((2k-1) k^4), with z_k=z+ell/k+m/k^2+n/k^3+O(k^-4).
b=Ball(center_im,0,rad)
u=Ball(ell.b,0,ell.e)
v=Ball(m.b,0,m.e)
w=Ball(n.b,0,n.e)
E5 = b*b
E6 = b*b/2+2*b*u
E7 = b*b/4+b*u+u*u+2*b*v
E8 = b*b/8+b*u/2+u*u/2+b*v+2*b*w+2*u*v
for name,e,lo,hi in [
    ('E5',E5,'89.888444','89.888447'),
    ('E6',E6,'-279.856486','-279.856482'),
    ('E7',E7,'550.260754','550.260760'),
    ('E8',E8,'16.194578','16.194585')]:
    assert e.box(lo,hi,'-0.000001','0.000001'), (name,e.approximate())
    print(name+'_STRICT_RATIONAL_INTERVAL_PASS',lo,hi,'approx=',e.approximate())
print('R599_ELL_M_AND_FOUR_ENERGY_COEFFICIENTS_ALL_PASS')
