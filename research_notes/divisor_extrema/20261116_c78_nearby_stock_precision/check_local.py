"""Exact local exponents, regular-branch tests and cutoff comparisons."""
from fractions import Fraction as Q
import json
import sympy as sp


def main():
    x, d, r = sp.symbols('x d r', positive=True)
    a, q, u = Q(15,4), Q(21,2), Q(7,16)
    f=x**a*(1-4*x**a)
    det=(q-1)*f*sp.diff(f,x,2)-q*sp.diff(f,x)**2
    lead=sp.limit(det/x**(2*a-2),x,0)
    assert lead == -a*(a+q-1)
    phi=lambda d: d**14*(d-1)**3/(1+u*d)**6
    assert phi(Q(2))>1 and phi(Q(2))>phi(Q(3,2))
    A=1-r
    m=u*A**4*d
    R=5-4*m/(1+m)-5*m*A/(1+m*A)
    rt=r/(1-r*R)
    assert rt.subs(r,0)==0 and sp.diff(rt,r).subs(r,0)==1
    assert Q(14,3)-2>0
    print(json.dumps(dict(hessian_leading=str(lead), tail_power=str(q),
                          normalized_r_derivative=1, phi2_cubed=str(phi(Q(2))),
                          phi_three_halves_cubed=str(phi(Q(3,2)))),indent=2))


if __name__ == '__main__':
    main()
