"""Exact Fricke two-leg Picard--Fuchs source transport verifier.
SymPy checks the Gauss gauge (whose symmetric square gives the third-order
operator transport), then standard-library integers check p-adic residues.
This does not execute the separate original p=373 native benchmark.
"""
from math import comb
import sympy as sp


def symbolic_transport():
    t = sp.symbols('t')
    z = 108*t*t*(t+9)*(t+8)**2/(t+12)**6
    w = 256*t**3*(t+8)*(t+9)**3/(t*t+36*t+216)**4
    H = 3*(t+12)**2/(2*(t*t+36*t+216))

    def pq(x, a, b):
        prime = sp.diff(x,t)
        P = (1-(a+b+1)*x)*prime/(x*(1-x))-sp.diff(x,t,2)/prime
        Q = -a*b*prime**2/(x*(1-x))
        return P, Q
    pa, qa = pq(z, sp.Rational(1,6), sp.Rational(1,3))
    pb, qb = pq(w, sp.Rational(1,8), sp.Rational(3,8))
    d = 6*t/((t+12)*(t*t+36*t+216))
    assert sp.cancel((pb-pa)/2-d) == 0
    assert sp.cancel(qb-(sp.diff(d,t)+d*d+pa*d+qa)) == 0
    assert sp.cancel(sp.diff(H,t)/(2*H)-d) == 0

    M = sp.factor((z/sp.diff(z,t))**3 * (1-z) /
                  ((w/sp.diff(w,t))**3 * (1-w)))
    expect = ((t*t-72*t-648)*(t*t+16*t+72)*(t*t+36*t+216) /
              ((t+6)*(t+12)**3*(t*t-24*t-288)))
    assert sp.cancel(M-expect) == 0
    for t0 in (6*sp.sqrt(2),-6*sp.sqrt(2)):
        assert sp.simplify(z.subs(t,t0)-sp.Rational(1,2)) == 0
        assert sp.simplify(w.subs(t,t0)-sp.Rational(1,9)) == 0
        assert sp.simplify((H*M).subs(t,t0)-4) == 0
    print('GAUSS_SYMMETRIC_SQUARE_TRANSPORT_PASS; two fibers; M(t)=', M)


def modular_checks():
    for p in (5,7,11,13,19,373):
        mod = p**4
        cp = comb(2*p,p)**2*comb(3*p,p)*pow(108,-p,mod) % mod
        dp = comb(2*p,p)**2*comb(4*p,2*p)*pow(256,-p,mod) % mod
        exact = (-p**3*(cp*pow(2,-p,mod)-4*dp*pow(9,-p,mod)))%mod
        predicted = (-p**3*pow(72,-1,mod))%mod
        assert exact == predicted, (p,exact,predicted)
        print(f'p={p}: source={exact} mod {mod}; PASS')


if __name__ == '__main__':
    symbolic_transport()
    modular_checks()
