"""Rational interval certificate of a globally identifiable interior neighborhood."""
from fractions import Fraction as F
from math import isqrt
import json


class Interval:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(hi if hi is not None else lo)
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


def h(x):
    return x**9/(1+112*x**15)


def J(x,y):
    return h(x)/y**12


def real(x,y,log_slope=False):
    a=4*(x.sqrt().sqrt())**15
    b=4*((y/x).sqrt().sqrt())**9
    B=F(7,16)*a**5
    D=F(7,16)*b**5
    value=B*D*(1-a)*(1-b)/(y.sqrt().sqrt()**3*(1+B*b)*(a+B*b))
    if not log_slope:
        return value
    # Derivative of log |S| in x along J constant.
    dy=(9/x-1680*x**14/(1+112*x**15))/12  # y'/y
    da=F(15,4)/x
    db=F(9,4)*(dy-1/x)
    return (-F(3,4)*dy+5*da+5*db-a*da/(1-a)-b*db/(1-b)
            -(5*da+db)*B*b/(1+B*b)
            -(a*da+B*b*(5*da+db))/(a+B*b))


def bracket(target, fun, lo, hi, increasing):
    lo,hi=F(lo),F(hi)
    f0,f1=fun(lo),fun(hi)
    assert (f0 < target < f1) if increasing else (f1 < target < f0)
    return Interval(lo,hi)


def main():
    x,y=F(4,5),F(9,25); j=J(x,y); m=F(1,5)
    assert m<x-y and m<y
    s=real(box(x),box(y)); assert s.inside('-0.006','-0.005')
    jac=real(box(x),box(y),True)
    assert jac.inside('-9','-7')
    u=bracket(j,lambda t:J(t,t-m),'0.48057','0.48059',False)
    assert real(u,u-m).inside('-0.001','0')
    zz=bracket(j*m**12,h,'0.30593','0.30595',True)
    assert zz.hi-m<m
    hh=bracket(j*m**12,h,'2.69','2.70',False)
    assert hh.lo>1
    left=bracket(j,lambda t:F(3,4)*J(1,t)/(1+F(1,448)),'0.32004','0.32006',False)
    sleft=real(box(1), left); assert sleft.inside('-0.0002','0')
    right=bracket(j,lambda t:F(3,4)*J(t,t),'0.05076','0.05077',False)
    sright=real(right,right); assert sright.inside('-0.00001','0')
    corner=F(9,16)/(1+F(1,448))*J(F(1),F(1))
    assert corner != j
    ab=bracket(j,lambda t:J(t,2*t-1),'0.67729','0.67730',False)
    assert real(ab,2*ab-1).inside('0.0005','0.0008')
    tied=J(F(2,3), F(1,3))
    assert j<tied and j<2**12*(F(3,2)**3)/(1+112*F(2,3)**15)
    # For y=1-x the derivative of log J has this numerator, whose
    # minimum is positive for x>=2/3 after grouping the high powers.
    assert 18*F(2,3)-6>0
    return dict(target=["4/5","9/25"], J=str(j),signed_real_interval=["-0.006","-0.005"],
                log_slope_interval=["-9","-7"], middle_competitor_first=["0.48057","0.48059"],
                middle_competitor_signed=["-0.001","0"], terminal_roots_first=[
                ["0.30593","0.30595"],["2.69","2.70"]], first_boundary_second=["0.32004","0.32006"],
                middle_boundary_first=["0.05076","0.05077"],
                last_short_ties_minimum_J=str(tied), first_middle_tie=['0.67729','0.67730'],
                first_middle_tie_signed=['0.0005','0.0008'])
if __name__ == '__main__':
    print(json.dumps(main(),indent=2))
