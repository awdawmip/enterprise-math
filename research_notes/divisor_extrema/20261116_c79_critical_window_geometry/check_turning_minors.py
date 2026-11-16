"""Exact coefficient certificates for the three physical turning curves."""
from fractions import Fraction as Q
from itertools import combinations
import json
import sympy as s


def certify():
    h, D, order = s.symbols("h D order")
    v = order*h
    m = s.Rational(7,16)*D*v**4
    n = v*m
    B = (1-v)*(1+m)*(1+n)
    U = s.Rational(19,5)-v/(1-v)-4*m/(1+m)-5*n/(1+n)
    V = (14-17*D)/3-(1-D)*(m/(1+m)+n/(1+n))
    U0, V0 = s.cancel(U*B), s.cancel(V*B)
    records = {}
    base = (14-17*D)/3
    for i,j in combinations((1,2,3), 2):
        first = U0.subs(order,i)*V0.subs(order,j)
        second = U0.subs(order,j)*V0.subs(order,i)
        P = s.Poly(s.cancel((first-second)/((j-i)*h)),h,D)
        assert s.cancel(P.as_expr().subs(h,0)-base)==0
        error = s.Poly(P.as_expr()-base,h,D)
        def bound(poly):
            return sum(abs(Q(int(co.p),int(co.q)))*Q(1,256)**a*4**b
                       for (a,b),co in poly.terms())
        b0, b1 = bound(error), bound(error.diff(D))
        assert max(b0,b1)<Q(1,1000)
        records[f"{i},{j}"] = dict(degrees=list(P.degree_list()),
                                     error_ceil_millionths=-(-b0*10**6//1),
                                     derivative_error_ceil_millionths=-(-b1*10**6//1))
    return records


if __name__=="__main__":
    print(json.dumps(certify(),indent=2))
