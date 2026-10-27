#!/usr/bin/env python3
"""Exact checks for R40 exceptional S-weight valuation/first p-adic jet.

Universal proof is factorial-block algebra; this checker independently builds
the original rational source and p-free factorial unit. Not a native CM test.
"""
from math import factorial
from fractions import Fraction

def primes_1_mod6(limit):
    return [p for p in range(7,limit+1) if p%6==1
            and all(p%d for d in range(2,int(p**0.5)+1))]

def vp(n,p):
    v=0
    while n%p==0:
        n//=p; v+=1
    return v

def fact_unit_mod(n,p,mod):
    assert n<p*p
    product=1
    for i in range(1,n+1):
        product=product*(i//p if i%p==0 else i)%mod
    return product

def norm_fraction(x,p,mod):
    assert x.denominator%p
    return x.numerator*pow(x.denominator,-1,mod)%mod

def main():
    results=[]; n=0; counts={}; checks_fraction=0
    for p in primes_1_mod6(997):
        ell=p%8
        assert (ell*p-1)%8==0
        k=(ell*p-1)//8
        assert 0<=k<p and 8*k+1==ell*p
        R=(p-1)//2
        q=(ell-1)//2
        assert 4*k==q*p+R and 4*k<p*p
        weight_excess=vp(ell,p)
        valuation=q+1+weight_excess
        ellprime=ell//p**weight_excess
        modulus=p*p
        denominator=factorial(k)**4*pow(2304,k,modulus)
        actual=(ellprime*fact_unit_mod(4*k,p,modulus)
                *pow(denominator,-1,modulus))%modulus
        Q=(factorial(p-1)+1)//p
        H=sum(pow(i,-1,p) for i in range(1,R+1))%p
        D=(ellprime*(-1)**q*factorial(q)*factorial(R)
           *pow(denominator,-1,modulus))%modulus
        predicted=D*(1+q*p*(H-Q))%modulus
        assert actual==predicted,(p,ell,k,actual,predicted)
        assert actual%p!=0,(p,k)
        assert (4*k)//p==q
        counts[p%24]=counts.get(p%24,0)+1
        if p in (7,13,19,31,37,73,181,373,733):
            results.append((p,p%24,ell,k,q,valuation,actual,actual%p))
        if p in (7,13,19,31,37,73,181):
            s=Fraction((8*k+1)*factorial(4*k),
                       factorial(k)**4*2304**k)
            scaled=s/p**valuation
            assert scaled.denominator%p
            assert norm_fraction(scaled,p,modulus)==actual
            assert norm_fraction(scaled,p,p)!=0
            checks_fraction+=1
        n+=1
    assert sorted(counts)==[1,7,13,19]
    print('PASS primes=',n,'class_counts=',dict(sorted(counts.items())),
          'independent_exact_fraction=',checks_fraction)
    for row in results: print('ROW',row)

if __name__=='__main__': main()
