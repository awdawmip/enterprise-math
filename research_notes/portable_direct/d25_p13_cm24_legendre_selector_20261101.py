#!/usr/bin/env python3
"""D25: independent finite certificates for the CM(-24) Legendre selector.

Pure integer arithmetic. The all-prime proof is in the companion research note:
finite checks do not replace Deuring's theorem or independent review.
"""
from math import comb


def primes_to(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for d in range(2, int(limit**0.5) + 1):
        if sieve[d]:
            for k in range(d*d, limit+1, d):
                sieve[k] = False
    return [p for p in range(5, limit + 1) if sieve[p]]


def mul(x, y, p):
    return ((x[0]*y[0]+2*x[1]*y[1]) % p,
            (x[0]*y[1]+x[1]*y[0]) % p)


def scalar(x, k, p):
    return (x[0]*k % p, x[1]*k % p)


def add(x, y, p):
    return ((x[0]+y[0])%p, (x[1]+y[1])%p)


def horner(coeff, x, p):
    y = (0, 0)
    for c in reversed(coeff):
        y = add(mul(y, x, p), (c, 0), p)
    return y


def legendre_at_s(p):
    n = (p - 1)//4
    x = (0, 2*pow(3, -1, p) % p)
    prev, cur = (1,0), x
    if n==0:
        return prev
    if n==1:
        return cur
    for j in range(1,n):
        nxt = add(scalar(mul(x,cur,p), (2*j+1),p),
                  scalar(prev,-j,p),p)
        nxt = scalar(nxt,pow(j+1,-1,p),p)
        prev,cur=cur,nxt
    return cur


def check(p):
    n, m = (p-1)//4, (p-1)//2
    # Hasse coefficient [X^(p-1)] {X (X^2-2X+1-t)}^((p-1)/2).
    # As a polynomial in t it has degree n.
    h = [(-1)**k * comb(m,k) * comb(p-1-2*k,m) % p
         for k in range(n+1)]
    # Independently: P_n(1-2t) = hypergeom(-n,n+1;1;t).
    leg = [(-1)**k * comb(n,k) * comb(n+k,k) % p
           for k in range(n+1)]
    assert h==leg, (p, 'Hasse polynomial <> Legendre polynomial')
    t = (pow(2,-1,p), -pow(3,-1,p)%p)
    assert horner(h,t,p) == legendre_at_s(p), p
    if p%8==5:
        selector = legendre_at_s(p)
        assert selector[0]==0, (p, 'anti-invariant coordinate')
        assert (selector==(0,0)) == (p%24==13), (p,selector)
        return selector
    return None


def main():
    # The quadratic CM discriminant -24 has H_D(X)=X^2-4834944 X+14670139392.
    a,b=2417472,1707264
    assert 2*a==4834944
    assert a*a-2*b*b==14670139392
    ps=[p for p in primes_to(1200) if p%4==1]
    targets,controls=[],[]
    for p in ps:
        s=check(p)
        if s is not None:
            (targets if p%24==13 else controls).append((p,s))
    print('HASSE_POLYNOMIAL_IDENTITY checked primes p=1 mod 4:',len(ps))
    print('CM_SELECTOR_ZERO checked primes p=13 mod24:',len(targets))
    print('CM_SELECTOR_NONZERO checked primes p=5 mod24:',len(controls))
    for p in (5,13,29,37,53,61,109,373):
        print('p=',p,'P_n(2sqrt2/3) in F_p[s], s^2=2:',check(p))
    print('PASS; finite evidence is separate from all-prime CM/Deuring proof')


if __name__=='__main__':
    main()
