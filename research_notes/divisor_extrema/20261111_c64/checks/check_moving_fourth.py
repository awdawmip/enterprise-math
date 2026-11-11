"""Exact symbolic certificates for the transient schedule E."""
from sympy import Poly, Rational as Q, cancel, factor, fraction, symbols
import json

def check():
    r,x = symbols('r x')
    k = 2*r+1
    rho=(k+4*r)/(k+r)
    tau=7*(k+4*r)*(k+4*r-1)/((k+r/4)*(k+r-1))
    e0=tau/(tau+1)
    e1=tau/(tau+rho)
    a=(9*r+4)*(9*r+5)/(14*(6*r+1)*(6*r+5))
    b=-3*(9*r+4)*(9*r+5)/(56*(3*r+1)*(3*r+2)*(6*r+1)*(6*r+5))
    a0=1/(1+a)
    a1=1/(1+a+b)
    initial=12*r*(13*r*r+13*r+2)*(195*r*r+195*r+44)/((9*r+5)*(23*r+4)*(59*r+20))
    assert cancel((e0-e1)/(a1-a0)-initial)==0
    assert cancel(e0-e1-56*r*(9*r+4)/(15*(23*r+4)*(59*r+20)))==0
    assert cancel(e1-a1-56*(2*r+1)*(3*r+1)*(9*r+4)/
                  (3*(59*r+20)*(195*r*r+195*r+44)))==0
    eps=3/(4*(3*r-2)*(3*r-1))
    assert cancel(-(b/a).subs(r,r-1)-eps)==0
    quadr=Q(3380,1357)
    linear=Q(38454260,16573041)
    num, den = fraction(cancel(initial-quadr*r*r-linear*r))
    assert Poly(num,r).degree()<=Poly(den,r).degree()
    cases={'unit_error':(1-initial*((1-eps)**-2-1),3),
           'monotonicity':(initial.subs(r,r+1)-initial-1,0)}
    out={}
    for name,(v,offset) in cases.items():
        n,d = fraction(factor(v))
        rows=[[int(c) for c in Poly(p.subs(r,x+offset),x).all_coeffs()] for p in (n,d)]
        assert all(min(c)>0 for c in rows)
        out[name]=dict(shift=offset,positive_numerator_coefficients=rows[0],
                       positive_denominator_coefficients=rows[1])
    return out

if __name__=='__main__':
    print(json.dumps(check(),indent=2))
