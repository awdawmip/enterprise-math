#!/usr/bin/env python3
"""Author-side exact check of first digit link between D25 Green gamma and 216 tail.

Only finite certificates: proof of congruences is supplied separately.
"""
from math import comb


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n+1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2,int(n**.5)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * ((n-p*p)//p+1)
    return [p for p in range(7,n+1) if sieve[p] and p%6==1]


def inv(a,power):
    return pow(a,-1,power)


def harmonic(n,p):
    return sum(inv(i,p) for i in range(1,n+1))%p


def quotient(a,p):
    return (pow(a,p-1,p*p)-1)//p


def direct_endpoint_mod(p):
    """Independent modular use of exact p-stripped factorial product (not gamma)."""
    m=p*p
    numerator=2
    for a,k in [(p-2,1),(p-1,1),(p-3,2)]:
        prod=1
        for r in range(1,a+1):
            prod=prod*(1+k*p*inv(r,m))%m
        numerator=numerator*prod%m
    denominator=(p-1)**2*(p-2)*pow(216,p-1,m)%m
    return (-numerator*inv(denominator,m))%m


def check(limit=5000):
    ps=primes_upto(limit)
    anchor_data=[]
    zero_primes=[]
    for p in ps:
        l=(p-1)//6
        m=p*p
        q2,q3,q216=(quotient(a,p) for a in (2,3,216))
        h1,h2,h3=(harmonic(t*l,p) for t in (1,2,3))
        assert h1==(h2+h3)%p,('sixth-root relation',p)
        assert h3==(-2*q2)%p,('base2',p)
        assert h2==(-3*q3*inv(2,p))%p,('base3',p)
        assert q216==(3*(q2+q3))%p,('base216',p)
        A=(h1+h2)%p
        assert A==(q2-q216)%p,('main H bridge',p)
        s=comb(p-1,l)*comb(p-1,2*l)
        gamma18=(-1 if l%2 else 1)*inv(s,m)%m
        mirror=direct_endpoint_mod(p)
        assert gamma18==(1+p*(q2-q216))%m,('gamma',p)
        assert mirror==(1+p*(inv(2,p)*13-q216))%m,('mirror',p)
        delta=((gamma18-mirror)//p)%p if (gamma18-mirror)%p==0 else None
        assert delta==(q2-13*inv(2,p))%p,('delta',p,delta)
        assert (gamma18*inv(mirror,m))%m==(1+p*(q2-13*inv(2,p)))%m,('ratio',p)
        if delta==0:zero_primes.append(p)
        if p in (7,13,19,37,67,283,373):
            # Direct original integer factorial expression: p^3 exact divisor.
            b=comb(2*p-2,p-1)**2*comb(3*p-3,p-1)
            assert b%(p**3)==0
            direct=(-b//(p**3))*inv(pow(216,p-1,m),m)%m
            assert direct==mirror
            anchor_data.append(dict(p=p,l=l,h=(h1,h2,h3),q=(q2,q3,q216),gamma18=gamma18,mirror=mirror,delta=delta,direct_original=direct))
    return len(ps),zero_primes,anchor_data


if __name__=='__main__':
    n,z,a=check(5000)
    print('PASS_D25_GREEN_MIRROR_FERMAT_BRIDGE',n,'primes; delta-zero:',z)
    for x in a:
        print('ANCHOR',x)
