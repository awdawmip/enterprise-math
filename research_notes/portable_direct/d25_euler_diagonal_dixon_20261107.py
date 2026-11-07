#!/usr/bin/env python3
"""Exact finite-rational and finite-field check for D25 Euler-cutoff Dixon summation.
This is author-side portable proof support, not a native research experiment.
"""
from fractions import Fraction
from math import factorial


def primes(N):
    a=bytearray(b'\x01')*(N+1)
    a[:2]=b'\x00\x00'
    for d in range(2,int(N**.5)+1):
        if a[d]:
            a[d*d:N+1:d]=b'\x00'*(((N-d*d)//d)+1)
    return [p for p in range(5,N+1) if a[p] and p%8==5]


def hypergeometric_fraction(k):
    # T = 2/9 * 3/[64(k+1)(3k+2)] * sum_{j=0}^k (-k)_j(-3k-1)_j / [(k+2)_j(3k+3)_j]
    t=Fraction(1)
    total=t
    for j in range(k):
        t*=Fraction((k-j)*(3*k+1-j),(k+2+j)*(3*k+3+j))
        total+=t
    return total


def dixon_fraction(k):
    return Fraction(2*factorial(k+1)**2 * factorial(3*k+2)**2 * factorial(8*k+4),
                    factorial(2*k+2) * factorial(6*k+4) * factorial(4*k+2)**2)


def inverse(a,p):
    return pow(a%p,-1,p)


def tail_diagonal_direct(p):
    k=(p-5)//8
    q=r=1
    r=3*inverse(64*(k+1)*(3*k+2),p)%p
    acc=0
    for j in range(k+1):
        acc=(acc+q*r)%p
        if j<k:
            q=q*(k-j)*(3*k+1-j)*inverse((j+1)**2,p)%p
            r=r*(j+1)**2*inverse((k+2+j)*(3*k+3+j),p)%p
    return acc*2*inverse(9,p)%p


def diagonal_closed(p):
    k=(p-5)//8
    # T = -k!(k+1)!(3k+1)!(3k+2)! /
    #   [48 (2k+2)! (6k+4)! ((4k+2)!)^2] (mod p), by Dixon and Wilson.
    F=[1]*p
    for i in range(1,p):F[i]=F[i-1]*i%p
    top=F[k]*F[k+1]*F[3*k+1]*F[3*k+2]
    bot=48*F[2*k+2]*F[6*k+4]*F[4*k+2]**2
    return -top*inverse(bot,p)%p


def diagonal_simplified(p):
    k=(p-5)//8
    # Wilson-reflected Dixon form in F_p.
    u=factorial(k)%p
    v=factorial(3*k+1)%p
    return u*u*v*v*inverse(192,p)%p


def main():
    for k in range(0,12):
        exact=hypergeometric_fraction(k)
        formula=dixon_fraction(k)
        assert exact==formula,(k,exact,formula)
    ps=primes(50000)
    for p in ps:
        x=tail_diagonal_direct(p)
        y=diagonal_closed(p)
        assert x==y==diagonal_simplified(p) and x!=0,(p,x,y,diagonal_simplified(p))
    values={p:tail_diagonal_direct(p) for p in [5,13,29,37,61,109,373,997] if p%8==5}
    print('EXACT_RATIONAL_DIXON: PASS 12 k values (k=0..11)')
    print('FINITE_FIELD: PASS',len(ps),'primes p<50000 with p=5(mod8); all nonzero and equal two factorial expressions')
    print('selected:',values)

if __name__=='__main__':main()
