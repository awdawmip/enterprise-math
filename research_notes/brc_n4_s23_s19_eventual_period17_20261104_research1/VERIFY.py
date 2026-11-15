#!/usr/bin/env python3
"""Exact rational enclosure of BRC N4 S23 s=1/9 eventual integer-budget result.
No floating point is used for assertions; only for final printed diagnostics.
"""
from fractions import Fraction as F
from math import isqrt

PREC = 10**40
SERIES = 18

class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi
    @staticmethod
    def put(x): return x if isinstance(x, I) else I(x)
    def __add__(self, x):
        x = I.put(x)
        return I(self.lo+x.lo,self.hi+x.hi)
    __radd__ = __add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,x): return self+(-I.put(x))
    def __rsub__(self,x): return I.put(x)+(-self)
    def __mul__(self,x):
        x=I.put(x)
        p=[a*b for a in (self.lo,self.hi) for b in (x.lo,x.hi)]
        return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=I.put(x)
        assert x.lo*x.hi>0
        return self*I(1/x.hi,1/x.lo)
    def __rtruediv__(self,x): return I.put(x)/self
    def sq(self):
        if self.lo>=0: return I(self.lo**2,self.hi**2)
        if self.hi<=0: return I(self.hi**2,self.lo**2)
        return I(0,max(self.lo**2,self.hi**2))
    def __repr__(self): return f'[{float(self.lo):.15g}, {float(self.hi):.15g}]'

def sqrt_rational(z):
    assert z>=0
    q=isqrt(z.numerator*PREC*PREC//z.denominator)
    return I(F(q,PREC),F(q+1,PREC))

def sqrt_i(x):
    assert x.lo>=0
    return I(sqrt_rational(x.lo).lo, sqrt_rational(x.hi).hi)

def log_rational(x):
    assert x>0
    if x<1:
        p=log_rational(1/x)
        return -p
    y=(x-1)/(x+1)
    u=y*y
    term=y
    tot=F(0)
    for j in range(SERIES):
        tot+=2*term/(2*j+1)
        term*=u
    tail=2*term/((2*SERIES+1)*(1-u))
    return I(tot,tot+tail)

def log_i(x):
    assert x.lo>0
    return I(log_rational(x.lo).lo,log_rational(x.hi).hi)

def within(x,lo,hi):
    assert x.lo>F(lo), (x,lo)
    assert x.hi<F(hi), (x,hi)

s=F(1,9); v=F(1,21); a=F(11,189); b=F(10,189)
U=sqrt_rational(a*b)
V=sqrt_rational((1-a)*(1-b))
Z=U+V
C0=-log_i(Z)
CT=-log_i(I(1-s)+s*sqrt_rational(1-v*v))
L1=log_rational(a/b)
L2=log_rational((1-a)/(1-b))
Delta=L1-L2
D=-(U*L1+V*L2)/Z
w0=U/Z
m0=w0*(1-w0)*Delta.sq()
wplus=w0+Delta/1000
M0=wplus*(1-wplus)*Delta.sq()
assert D.lo>0 and w0.lo>0 and wplus.hi<F(1,2)
assert m0.lo>0 and M0.lo>m0.lo
assert (D/m0).hi<F(1,250), (D/m0)
assert (D/M0).hi<F(1,250), (D/M0)
d_lower=D.sq()/(2*M0)
d_upper=D.sq()/(2*m0)
d=I(d_lower.lo,d_upper.hi)
CB=C0+d
E=CT-F(17,9)*CB
residue=CB/9-8*E-16*d
endpoint=99*E-16*d
within(CB, F(667,10**7), F(668,10**7))
within(d,F(372,10**11),F(374,10**11))
within(E,F(64,10**11),F(67,10**11))
assert residue.lo>0
assert endpoint.lo>0
print('CB:',CB)
print('d:',d)
print('E:',E)
print('uniform non-9 residue lower:',float(residue.lo))
print('all K>=187 endpoint lower:',float(endpoint.lo))
print('PASS_S23_S19_ALL_K_GE_187_RATIONAL_ENDPOINT_20261104')
