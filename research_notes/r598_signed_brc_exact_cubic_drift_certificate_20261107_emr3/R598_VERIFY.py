"""R598: exact rational complex-ball zero and cubic-drift coefficient certificate.
Pure Python 3 standard library; rational arithmetic only in proof checks.
The mpmath value was used solely to select the printed rational centre.
"""
from fractions import Fraction as Q
from math import factorial

N = 44
rho = Q(1, 10**24)
re = Q('6.33923451020742194898840830174914205')
im = Q('9.48095171645470905742279785138458204')

# A ball (a+ib; e) means complex values at Euclidean distance <= e.
class Ball:
    def __init__(self, a=0, b=0, e=0):
        self.a, self.b, self.e = Q(a), Q(b), Q(e)
        assert self.e >= 0
    def __add__(self, y):
        y = lift(y)
        return Ball(self.a+y.a, self.b+y.b, self.e+y.e)
    __radd__ = __add__
    def __neg__(self): return Ball(-self.a, -self.b, self.e)
    def __sub__(self, y): return self+-lift(y)
    def __rsub__(self, y): return lift(y)+-self
    def upper(self): return abs(self.a)+abs(self.b)+self.e
    def lower(self): return max(abs(self.a),abs(self.b))-self.e
    def __mul__(self, y):
        y=lift(y)
        v=self.a*y.a-self.b*y.b
        w=self.a*y.b+self.b*y.a
        e=(abs(self.a)+abs(self.b))*y.e+(abs(y.a)+abs(y.b))*self.e+self.e*y.e
        return Ball(v,w,e)
    __rmul__=__mul__
    def inv(self):
        d=self.lower()
        assert d>0
        n=self.a*self.a+self.b*self.b
        return Ball(self.a/n, -self.b/n, self.e/(d*(d-self.e)))
    def __truediv__(self,y): return self*lift(y).inv()
    def __rtruediv__(self,y): return lift(y)*self.inv()
    def __pow__(self,n):
        assert n>=0
        z=Ball(1)
        for _ in range(n):z=z*self
        return z
    def in_box(self,a,b,c,d):
        return self.a-self.e>a and self.a+self.e<b and self.b-self.e>c and self.b+self.e<d

def lift(y): return y if isinstance(y,Ball) else Ball(y)

def coeff(j,order):
    if order==0:return Q(1)
    if order==1:return Q(0) if j==0 else Q(15*j+3,8)
    if order==2:
        q=Q(-32*j**3+501*j*j-349*j-18,384)
        return q+(Q(3,64) if j==0 else Q(15,64) if j==1 else Q(0))
    if order==3:
        q=Q(-160*j**4+359*j**3-1814*j*j+1159*j+36,1024)
        return q+(Q(-9,256) if j==0 else Q(105,256) if j==1 else Q(-105,512) if j==2 else Q(0))
    raise ValueError(order)

def tail():
    # For all order<=3 and derivative<=3, j>N, |z|<=12:
    # |term_j| <= 96 (j+1)^8 * 96^j /(2j+4)!.
    # Adjacent envelope ratio < 1/2 for every j>=N+1.
    j=N+1
    return Q(192*(j+1)**8*96**j, factorial(2*j+4))
TAIL=tail()
j=N+1
assert Q(96*(j+2)**8, (j+1)**8*(2*j+5)*(2*j+6)) < Q(1,2)

def series(order,derivative,z):
    v=Ball(0)
    for j in range(derivative,N+1):
        falling=factorial(j)//factorial(j-derivative)
        a=Q(24*8**j*falling,factorial(2*j+4)) * coeff(j,order) * (-1)**j
        if a:v=v+z**(j-derivative)*a
    return v+Ball(0,0,TAIL)

c=Ball(re,im)
Z=Ball(re,im,rho)
assert re*re+im*im < (12-rho)**2
fc=series(0,0,c)
fprime=series(0,1,c)
f2=series(0,2,Z)
assert fc.upper() < Q(1,10**30), f'centre residual {float(fc.upper())}'
assert fprime.lower()>Q(1,25), f'derivative lower {float(fprime.lower())}'
assert f2.upper()<Q(1), f'derivative2 upper {float(f2.upper())}'
assert fc.upper()+rho*rho/2 < rho/25
print('R598_EXACT_ROUCHE_SIMPLE_ROOT_DISC_PASS', 'radius=1e-24',
      'center_re=6.33923451020742194898840830174914205',
      'center_im=9.48095171645470905742279785138458204')
print('R598_ROOT_RESIDUAL_UPPER',float(fc.upper()),
      'DERIVATIVE_LOWER',float(fprime.lower()),'F2_UPPER',float(f2.upper()),
      'TAIL_UPPER',float(TAIL))

# R597 cubic shift and R596 first and second shifts, now evaluated
# on the certified root disc via exact rational ball operations.
F1=series(0,1,Z)
F2=series(0,2,Z)
F3=series(0,3,Z)
G=series(1,0,Z)
G1=series(1,1,Z)
G2=series(1,2,Z)
H=series(2,0,Z)
H1=series(2,1,Z)
J=series(3,0,Z)
assert F1.lower()>Q(1,25)
ell=-G/F1
m=-(H+G1*ell+F2*ell*ell/2)/F1
nu=-(J+H1*ell+G1*m+G2*ell*ell/2+F2*ell*m+F3*ell*ell*ell/6)/F1
assert nu.in_box(Q('-93.087448'),Q('-93.087445'),Q('24.149782'),Q('24.149786')), ('box fail',float(nu.a),float(nu.b),float(nu.e))
print('R598_CUBIC_DRIFT_RATIONAL_BOX_PASS',
      '-93.087448<Re(n)<-93.087445, 24.149782<Im(n)<24.149786')
print('R598_COMPUTED_CENTRE_AND_ERROR',float(nu.a),float(nu.b),float(nu.e))
print('R598_ALL_CERTIFICATES_PASS')
