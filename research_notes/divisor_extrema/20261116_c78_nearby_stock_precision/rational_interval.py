"""C76 rational outward interval arithmetic used by the C78 curvature check."""
from fractions import Fraction as F
from math import isqrt



class Interval:
    def __init__(self, lo, hi=None):
        scale=10**24
        l=F(lo)*scale
        h=F(hi if hi is not None else lo)*scale
        self.lo=F(l.numerator // l.denominator,scale)
        self.hi=F(-(-h.numerator // h.denominator),scale)
        assert self.lo <= self.hi

    def __add__(self, other):
        b = box(other)
        return Interval(self.lo+b.lo, self.hi+b.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-box(other))

    def __rsub__(self, other):
        return box(other) - self

    def __mul__(self, other):
        b=box(other)
        terms=[a*z for a in (self.lo,self.hi) for z in (b.lo,b.hi)]
        return Interval(min(terms),max(terms))

    __rmul__=__mul__

    def __truediv__(self,other):
        b=box(other)
        assert b.lo*b.hi > 0
        return self*Interval(1/b.hi,1/b.lo)

    def __rtruediv__(self,other):
        return box(other)/self

    def __pow__(self,power):
        if power==2:
            lo,hi=self.lo,self.hi
            return Interval(0 if lo*hi<=0 else min(lo**2,hi**2), max(lo**2,hi**2))
        assert power>=0 and self.lo>=0
        return Interval(self.lo**power,self.hi**power)

    def sqrt(self):
        assert self.lo>=0
        D=10**22
        def lower(v):
            return isqrt(v.numerator*D*D//v.denominator)
        return Interval(F(lower(self.lo),D),F(lower(self.hi)+1,D))

    def inside(self, lo, hi):
        return F(lo)<self.lo and self.hi<F(hi)


def box(x):
    return x if isinstance(x,Interval) else Interval(x)


