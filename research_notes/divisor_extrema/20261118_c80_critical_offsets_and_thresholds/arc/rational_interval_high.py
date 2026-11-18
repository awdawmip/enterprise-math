"""Directed intervals with a common exact dyadic denominator."""
from fractions import Fraction
from math import isqrt
import os

BITS = int(os.environ.get("ARC_BITS", "780"))
D = 1 << BITS

class Interval:
    __slots__ = ("a", "b")
    def __init__(self, lo, hi=None):
        upper = lo if hi is None else hi
        lo, upper = Fraction(lo)*D, Fraction(upper)*D
        self.a = lo.numerator // lo.denominator
        self.b = -(-upper.numerator // upper.denominator)
        assert self.a <= self.b

    @classmethod
    def endpoints(cls, a, b):
        ret = cls.__new__(cls)
        ret.a, ret.b = a, b
        return ret

    @property
    def lo(self):
        return Fraction(self.a, D)
    @property
    def hi(self):
        return Fraction(self.b, D)

    def __add__(self, other):
        o = box(other)
        return Interval.endpoints(self.a+o.a,self.b+o.b)
    __radd__ = __add__
    def __neg__(self):
        return Interval.endpoints(-self.b,-self.a)
    def __sub__(self, other):
        o = box(other)
        return Interval.endpoints(self.a-o.b,self.b-o.a)
    def __rsub__(self, other):
        return box(other)-self
    def __mul__(self, other):
        o = box(other)
        a,b,c,d=self.a,self.b,o.a,o.b
        if a>=0:
            if c>=0: low,high=a*c,b*d
            elif d<=0: low,high=b*c,a*d
            else: low,high=b*c,b*d
        elif b<=0:
            if c>=0: low,high=a*d,b*c
            elif d<=0: low,high=b*d,a*c
            else: low,high=a*d,a*c
        elif c>=0: low,high=a*d,b*d
        elif d<=0: low,high=b*c,a*c
        else: low,high=min(a*d,b*c),max(a*c,b*d)
        return Interval.endpoints(low>>BITS,-((-high)>>BITS))
    __rmul__ = __mul__
    def __truediv__(self, other):
        o = box(other)
        assert o.a*o.b > 0
        return self*Interval.endpoints(D*D//o.b, -(-D*D//o.a))
    def __rtruediv__(self, other):
        return box(other)/self
    def __pow__(self, n):
        assert n>=0
        if n==0:
            return box(1)
        den = D**(n-1)
        p, q = self.a**n, self.b**n
        low = 0 if n%2==0 and self.a*self.b<=0 else min(p,q)
        return Interval.endpoints(low//den, -(-max(p,q)//den))
    def sqrt(self):
        assert self.a>=0
        return Interval.endpoints(isqrt(self.a*D),isqrt(self.b*D)+1)
    def inside(self, lo, hi):
        return Fraction(lo)<self.lo and self.hi<Fraction(hi)

from functools import lru_cache
@lru_cache(maxsize=128)
def constant(v):
    return Interval(v)
def box(v):
    return v if isinstance(v, Interval) else constant(v)
