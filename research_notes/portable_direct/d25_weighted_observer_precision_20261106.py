#!/usr/bin/env python3
"""Exact modular verification of the coefficientwise D=1+6z*d/dz
observer's p-adic image/kernel precision for 5<=p<=3000.
"""
from math import isqrt, gcd


def primes(n):
    return [p for p in range(5,n+1) if all(p%d for d in range(2,isqrt(p)+1))]


def check(p):
    assert p>=5
    m=(p-1)//6 if p%6==1 else (p+1)//6
    jstar=m if p%6==1 else 5*m-1
    assert 0<=jstar<p
    for j in range(p):
        w=6*j+1
        if j==jstar:
            assert w==p if p%6==1 else w==5*p
        else:
            assert gcd(w,p)==1
    v=2 if p==5 else 1
    wstar=6*jstar+1
    assert wstar%(p**v)==0 and wstar%(p**(v+1))!=0
    for r in (1,2,3,4):
        modulus=p**r
        g=min(v,r)
        # Each fiber of multiplication by w has cardinality gcd(w,p^r).
        assert gcd(wstar,modulus)==p**g
        assert modulus//gcd(wstar,modulus)==p**(r-g)
        x=(p//2)*(p**max(0,r-1))+1
        y=wstar*x%modulus
        for z in (0,1,2,p-1):
            restored=(x+z*(p**(r-g)))%modulus
            assert wstar*restored%modulus==y
        for j in (0,jstar-1,jstar+1,p-1):
            if 0<=j<p and j!=jstar:
                assert ((6*j+1)*pow(6*j+1,-1,modulus))%modulus==1
    return p,jstar,v


if __name__=='__main__':
    rows=[check(p) for p in primes(3000)]
    print(f'WEIGHTED OBSERVER p-ADIC PRECISION: {len(rows)}/{len(rows)} PASS')
    for p,j,v in rows:
        if p in (5,7,11,13,19,373,1009,2999):
            print(f'p={p}, j*={j}, v_p(6*j*+1)={v}, kernel_size_mod_p2={p**min(v,2)}')
