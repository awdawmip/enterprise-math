#!/usr/bin/env python3
"""Author-side, exact original-beta p13 coefficient/first-jet transport.

All computation is in Z/p^2Z with p-unit denominators; it does NOT run
native H0/B0 divided-power benchmark, create a Source claim, or prove the
remaining infinite-prime p13 cancellation conjecture.
"""
from math import comb, isqrt


def beta_gauss(p):
    mod = p * p
    b = total = 1
    for k in range(p - 1):
        b = b * (8*k+1)*(8*k+3)*pow(576*(k+1)*(k+1), -1, mod) % mod
        total = (total + b) % mod
    return total


def kpoly(n, x, lam, mod):
    return sum(comb(n, k)*comb(x, k)*pow(lam, k, mod)
               for k in range(min(n, x)+1)) % mod


def f_coefficient(a,b,lam,mod,r):
    """[t^r](1+t)^a(t+lambda)^b; base provenance retained."""
    return sum(comb(a,j)*comb(b,r-j)*pow(lam,b-r+j,mod)
               for j in range(max(0,r-b),min(a,r)+1)) % mod


def inspect(p, full_ports=True):
    assert p>7 and p%8==5
    a,b=(5*p-1)//8,(7*p-3)//8
    assert 0<a<b<p
    mod=p*p
    lam=pow(9,-1,mod)
    j=kpoly(a,b,lam,mod)
    ka=kpoly(b,a+p,lam,mod)
    kb=kpoly(a,b+p,lam,mod)
    g=beta_gauss(p)
    # Theorem T, independently recomputed original Pochhammer recurrence.
    lhs=(20*j-5*ka-7*kb)%mod
    assert lhs==(8*g)%mod,(p,lhs,g)
    if full_ports:
        # Coefficients built independently from the *unshifted* F-polynomial.
        assert j==f_coefficient(a,b,lam,mod,b)
        shifted_a=sum(comb(p,k)*f_coefficient(a,b,lam,mod,b-k)
                      for k in range(b+1))%mod
        shifted_b=sum(comb(p,k)*pow(lam,p-k,mod)*
                      f_coefficient(a,b,lam,mod,b+p-k)
                      for k in range(p+1))%mod
        assert (shifted_a,shifted_b)==(ka,kb)
        # Divided Frobenius differences in *integer* binomial arithmetic.
        e1=sum((comb(p,k)//p)*f_coefficient(a,b,lam,mod,b-k)
               for k in range(1,b+1))%p
        el=sum((comb(p,k)//p)*pow(lam,p-k,mod)*
               f_coefficient(a,b,lam,mod,b+p-k)
               for k in range(1,p))%p
        assert (ka-j)%mod==(p*e1)%mod
        assert (kb-j)%mod==(p*el)%mod
        # CM root vanishes modulo p at target p13; its first lift remains open.
        if p%24==13:
            assert j%p==0
            assert (g//p- (j//p- (5*e1+7*el)*pow(8,-1,p)))%p==0
        return dict(p=p, a=a,b=b,J=j,Ka=ka,Kb=kb,E1=e1,El=el,
                    G=g, G_over_p=(g//p)%p if g%p==0 else None,
                    residual=((j//p-(5*e1+7*el)*pow(8,-1,p))%p)
                    if j%p==0 else None)
    return dict(p=p, J=j, G=g)


def primes(limit):
    sieve=bytearray([1])*(limit+1)
    sieve[:2]=b'\0\0'
    for j in range(2,isqrt(limit)+1):
        if sieve[j]:
            sieve[j*j::j]=b'\0'*((limit-j*j)//j+1)
    return [i for i in range(11,limit+1) if sieve[i] and i%8==5]


if __name__=='__main__':
    cases=primes(500)
    for p in cases:
        inspect(p, False)
    fixed=(13,29,37,61,109,373)
    readings=[inspect(p,True) for p in fixed]
    print('P5_MOD8_EXACT_JACOBI_AND_ORIGINAL_BETA',len(cases),'primes <=500 PASS')
    print('INDEPENDENT_FROBENIUS_COEFFICIENT_PORTS',len(fixed),'PASS')
    for row in readings:
        print(row)
    print('UNIVERSAL_P13_SECOND_DIGIT_IS_UNPROVED; NATIVE_NOT_RUN')
