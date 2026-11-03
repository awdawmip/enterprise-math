#!/usr/bin/env python3
"""Exact D25 middle-band second-digit lift and full one-sided congruence check."""
from math import comb
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

OLD = str(Path(__file__).with_name('d25_h2_quadratic_character_hypergeometric_20261103.py'))
spec = spec_from_file_location('d25_h2', OLD)
module = module_from_spec(spec)
spec.loader.exec_module(module)

def unit_factorials(p, limit, modulus):
    unit = [1] * (limit+1)
    for i in range(1,limit+1):
        unit[i] = unit[i-1] * (i if i % p else 1) % modulus
    return unit

def check_one(p, full=False):
    assert p % 6 == 1 and p >= 7
    r = (p-1)//6
    n = 3*r
    m2 = p*p
    f = unit_factorials(p, p+n-1, m2)
    chi = 1 if pow(6,n,p) == 1 else -1
    q2 = (pow(2,p-1,m2)-1)//p
    q3 = (pow(3,p-1,m2)-1)//p
    inv2 = pow(2,-1,p)
    epsilon = (3+(q2-3*q3)*inv2)%p
    L = (-2*chi*(1+p*epsilon)) % m2
    exact_L = f[p-1]*f[p+n-1]*pow(pow(f[n],5,m2)*pow(216,n,m2)%m2,-1,m2)%m2
    assert L == exact_L
    products = {n:1}
    for j in range(n-1,2*r,-1):
        numer = (2*j+1)*(3*j+1)*(3*j+2)
        denom = 36*(j+1)**3
        products[j] = products[j+1] * denom * pow(numer,-1,m2)%m2
    middle = 0
    fbig=unit_factorials(p, 3*n, m2)
    for j in range(2*r+1,n+1):
        direct = fbig[2*j]*fbig[3*j]*pow(pow(fbig[j],5,m2)*pow(216,j,m2)%m2,-1,m2)%m2
        predicted = L*products[j]%m2
        assert direct == predicted, (p,j,direct,predicted)
        middle=(middle+(6*j+1)*predicted)%m2
    if full:
        m3=p**3
        inv216=pow(216,-1,m3)
        low=0
        complete=0
        for k in range(p):
            b=comb(2*k,k)**2 * comb(3*k,k) * pow(inv216,k,m3)%m3
            term = ((6*k+1)*b)%m3
            complete=(complete+term)%m3
            if k<=2*r: low=(low+term)%m3
        _,_,_,chi2,high, _ = module.verify(p)
        assert chi2==chi
        reduced=(low+p*middle+p*p*high)%m3
        assert reduced==complete, (p,reduced,complete)
        return p,chi,L,epsilon,middle,high,complete
    return p,chi,L,epsilon,middle

if __name__=='__main__':
    candidates=module.primes(2000)
    assert len(candidates)==148
    for p in candidates:
        check_one(p)
    for p in (7,13,19,37,43,373):
        print('full',check_one(p,True))
    print('PASS 148 primes: Fermat-quotient p^2 entry + all oriented middle units; '
          '6 independent original-binomial full W modulo p^3 checks.')
