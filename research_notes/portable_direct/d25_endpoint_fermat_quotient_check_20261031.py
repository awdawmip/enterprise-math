#!/usr/bin/env python3
"""Independent all-prime p^2 endpoint product and Fermat quotient certificate."""
from fractions import Fraction
from math import comb


def primes(n):
    b = bytearray([1]) * (n+1)
    b[:2] = b'\x00\x00'
    for a in range(2,int(n**0.5)+1):
        if b[a]:
            b[a*a:n+1:a]=bytes((n-a*a)//a+1)
    return [p for p in range(5,n+1) if b[p]]


def inv(a,m):
    return pow(a%m,-1,m)


def direct_endpoint_factorial(p):
    # Independently accumulate p-local unit parts of (2p-2)! and (3p-3)!.
    mod=p*p
    u2=1
    for k in range(1,2*p-1):
        if k%p: u2=u2*k%mod
        elif k!=p: raise AssertionError('wrong u2 range')
    u3=1
    for k in range(1,3*p-2):
        if k%p: u3=u3*k%mod
        # p and 2p each contribute a p; 2p contributes an extra factor of 2.
        elif k==2*p: u3=u3*2%mod
    fact=1
    for k in range(1,p): fact=fact*k%mod
    return u2*u3*inv(pow(fact,5,mod)*pow(216,p-1,mod),mod)%mod


def product_endpoint(p):
    mod=p*p
    t=2*inv((p-1)**2*(p-2)*pow(216,p-1,mod),mod)%mod
    for r in range(1,p-1): t=t*(1+p*inv(r,mod))%mod
    for r in range(1,p): t=t*(1+p*inv(r,mod))%mod
    for r in range(1,p-2): t=t*(1+2*p*inv(r,mod))%mod
    return t


def run(p):
    mod=p*p
    endpoint=product_endpoint(p)
    assert endpoint == direct_endpoint_factorial(p), (p,'factorial chunking')
    assert endpoint%p==p-1,(p,'Wilson endpoint')
    q=(((-endpoint)%mod-1)%mod)//p
    fquot=(pow(216,p-1,mod)-1)//p
    predicted=(13*inv(2,p)-fquot)%p
    assert q==predicted,(p,q,predicted)
    Eterminal=(-1*inv(18,mod)+p*fquot*inv(18,mod))%mod
    Eterminal_ind=(-((2*p-1)*(3*p-2)*(3*p-1))*inv(36,mod)*endpoint)%mod
    assert Eterminal==Eterminal_ind,(p,'terminal',Eterminal,Eterminal_ind)
    if p in (5,11,17,23,29,41,73,373,1327):
        n=p-1
        a=comb(2*n,n)**2*comb(3*n,n)
        a=a//p**3
        assert a*inv(pow(216,n,mod),mod)%mod==endpoint,(p,'integer binomial anchor')
    return (p,q,fquot,Eterminal)


def rational_identity_checks():
    # This confirms the exact (non-congruent) factorial chunking relation.
    for p in (5,7,11,13,17,19):
        n=p-1
        raw=Fraction(comb(2*n,n)**2*comb(3*n,n),p**3*216**n)
        rhs=Fraction(2,(p-1)**2*(p-2)*216**(p-1))
        for r in range(1,p-1):rhs*=1+Fraction(p,r)
        for r in range(1,p):rhs*=1+Fraction(p,r)
        for r in range(1,p-2):rhs*=1+Fraction(2*p,r)
        assert raw==rhs,(p,'exact product')
    return 6


def main():
    out=[run(p) for p in primes(3000)]
    print('PRIMES',len(out),'P5_BRANCH',sum(p%6==5 for p,*_ in out),'P1_BRANCH',sum(p%6==1 for p,*_ in out))
    print('EXACT_FACTORIAL_RATIONAL_CHECKS',rational_identity_checks())
    for row in out:
        if row[0] in (5,11,17,23,29,41,373,1327):print('ANCHOR',row)
    print('PASS_D25_ENDPOINT_FERMAT_QUOTIENT_ALL_PRIMES_EXACT')


if __name__=='__main__':main()
