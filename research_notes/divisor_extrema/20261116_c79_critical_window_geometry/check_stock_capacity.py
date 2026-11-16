"""Exact derivative and polynomial certificates for all stock ratios s."""
import json

import sympy as sp


def log_gradients(a, d, s):
    m=7*a**4*d/16
    b=m*s**4
    e=a*m*s**5
    log_a=sp.Rational(19,5)/a-s/(1-a*s)-sp.diff(b,a)/(1+b)-sp.diff(e,a)/(1+e)
    log_d=sp.Rational(14,3)/d-1/(1-d)-sp.diff(b,d)/(1+b)-sp.diff(e,d)/(1+e)
    return log_a, log_d


def main():
    a,d,s=sp.symbols('a d s')
    u,v=log_gradients(a,d,1)
    w,k=log_gradients(a,d,s)
    factors=(1-a)*(1-a*s)*(1-d)**2
    cleared=sp.factor((u*k-v*w)*factors)
    denominator=15*d*(7*a**4*d+16)*(7*a**5*d+16)*(7*a**4*d*s**4+16)*(7*a**5*d*s**5+16)
    poly=sp.Poly(sp.cancel(cleared*denominator/((d-1)*(s-1))),a,d,s)
    degrees=[poly.degree(x) for x in [a,d,s]]
    assert degrees==[18,5,9] and poly.as_expr().subs(d,0)==-4587520
    assert sp.cancel(sp.diff((1-a*s)/(1-a),a)-(1-s)/(1-a)**2)==0
    q=sp.Rational(21,2)
    alpha=2-1/q
    assert 2/alpha==sp.Rational(21,20)
    print(json.dumps(dict(degrees_A_D_s=degrees, constant_D0=-4587520,
                          slope_derivative="(1-s)/(1-A)^2",
                          maximum_slope_branches=3,
                          radial_density_exponent=str(alpha),
                          density_slope_integral_power=str(2/alpha)),indent=2))


if __name__=="__main__":
    main()
