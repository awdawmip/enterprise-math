"""Limit of the initial double-5 placement relative to the optimum, divided by (k-1)^2."""
from fractions import Fraction as Q
import sympy as s

def run():
    r=s.symbols('r',positive=True)
    K=2*r+1
    rho=(K+4*r)/(K+r)
    tau=7*(K+4*r)/(K+r/4)*(K+4*r-1)/(K+r-1)
    width=tau*(rho-1)/((tau+1)*(tau+rho))
    assert s.limit(width,r,s.oo)==s.Rational(168,6785)
    result=Q(168,6785)/Q(42,4225)
    assert result==Q(3380,1357)
    return str(result)

if __name__=='__main__':
    print(run())
