#!/usr/bin/env python3
"""Independent dual-number differentiation of original C275 branch products.
Validates C285 analytic log derivatives at all 187 C284 bracket midpoints.
All equalities are exact Fraction comparisons.
"""
from fractions import Fraction as F
import json
import C275_STANDALONE_EXACT_REPLAY as c
from C285_EXACT_UNIFORM_DERIVATIVE import slope_range, branch_mass

class Dual:
    __slots__=('x','d')
    def __init__(self,x,d=0):self.x=F(x);self.d=F(d)
    def __add__(self,o):
        o=coerce(o);return Dual(self.x+o.x,self.d+o.d)
    __radd__=__add__
    def __neg__(self):return Dual(-self.x,-self.d)
    def __sub__(self,o):return self+-coerce(o)
    def __rsub__(self,o):return coerce(o)+-self
    def __mul__(self,o):
        o=coerce(o);return Dual(self.x*o.x,self.d*o.x+self.x*o.d)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=coerce(o);return Dual(self.x/o.x,(self.d*o.x-self.x*o.d)/(o.x*o.x))
    def __rtruediv__(self,o):return coerce(o)/self
    def __pow__(self,n):
        assert isinstance(n,int)
        return Dual(self.x**n,n*(self.x**(n-1))*self.d)
    def __abs__(self):return self if self.x>0 else -self

def coerce(o):return o if isinstance(o,Dual) else Dual(o)

def main():
    d=json.load(open('C284_187_EXACT_DYADIC_BRACKETS.json',encoding='utf-8'))
    weights,_=c.floor_fixed_masses(); hulls=c.hulls()
    for i,j,h,k in d['records']:
        lo,hi,_=hulls[(i,j)];w=c.WITNESSES[h-1];pos=c.high_point(lo,hi)
        v=tuple(x+F(2*k+1,8192)*(y-x) for x,y in zip(w,pos))
        dv=tuple(y-x for x,y in zip(w,pos))
        m=c.original_F(tuple(Dual(x,z) for x,z in zip(v,dv)),weights)
        assert isinstance(m,Dual)
        exact=F(0)
        for branch in range(79):
            slope1,slope2=slope_range(branch,v,v,dv)
            assert slope1==slope2
            exact+=branch_mass(branch,v,weights)*slope1
        assert m.x==c.original_F(v,weights)
        assert m.d==exact
    print('C285_INDEPENDENT_DUAL_187_EXACT_PASS')

if __name__=='__main__': main()
