#!/usr/bin/env python3
"""Author exact checks: GH9/GH10 rank reflection at p and p^2.
This is neither a native experiment nor a proof of T_p=0.
"""
from fractions import Fraction
from math import gcd


def primes_up_to(n: int):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for k in range(2, int(n**0.5) + 1):
        if sieve[k]:
            sieve[k*k:n+1:k] = b'\x00' * ((n-k*k)//k+1)
    return [i for i in range(2,n+1) if sieve[i]]


def residue(q: Fraction, modulus: int) -> int:
    a, b = q.numerator, q.denominator
    assert gcd(b, modulus) == 1, (b,modulus)
    return (a % modulus) * pow(b, -1, modulus) % modulus


def exact_terms(d):
    C=[Fraction(1)]
    for j in range(d):
        C.append(C[-1]*Fraction(9*(4*j+1)**3,(4*j+2)*(4*j+3)*(4*j+4)))
    return C


def reflected_kernel(r: int):
    # B_r = 9^-r product_{i=1}^r (4i+1)(4i)(4i-1)/(4i+2)^3
    B=Fraction(1)
    H=Fraction(0)
    for i in range(1,r+1):
        B*=Fraction((4*i+1)*(4*i)*(4*i-1),9*(4*i+2)**3)
        H+=sum((Fraction(1,4*i+1), Fraction(1,4*i), Fraction(1,4*i-1)))-Fraction(3,4*i+2)
    return B,H


def check(p):
    assert p > 3 and p % 4 == 3
    d=(p-3)//4
    pp=p*p
    C=exact_terms(d)
    cd=residue(C[-1],pp)
    assert cd % p != 0
    T=sum((8*j+1)*v for j,v in enumerate(C))
    Tn=residue(T,pp)
    bvals=[]; hvals=[]
    for r in range(d+1):
        B,H=reflected_kernel(r)
        bvals.append(B)
        hvals.append(H)
        direct= C[d-r]/C[-1]
        modp=residue(direct,p)
        modp2=residue(direct,pp)
        assert modp==residue(B,p),('GH9',p,r)
        assert modp2==residue(B*(1-p*H),pp),('GH10',p,r)
        # Exact finite rational product; isolates order-of-operations errors.
        product=Fraction(1)
        for i in range(1,r+1):
            product*=Fraction((p-(4*i+1))*(p-4*i)*(p-(4*i-1)),9*(p-(4*i+2))**3)
        assert direct==product,('EXACT',p,r)
    # GH9 rank-reflection sum; no T=0 assumed.
    assert (Tn * pow(cd,-1,p))%p==residue(-sum((8*r+5)*bvals[r] for r in range(d+1)),p)
    # GH10: preserve first p-adic digit, including 2p weight and harmonic term.
    reflected=sum(-(8*r+5)*bvals[r]+p*(2*bvals[r]+(8*r+5)*bvals[r]*hvals[r]) for r in range(d+1))
    assert (Tn * pow(cd,-1,pp))%pp==residue(reflected,pp),('SUM',p)
    return d, Tn, cd



def check_modular_fast(p):
    """Independent p^2 residue recurrence, no Fraction conversion."""
    d=(p-3)//4
    m=p*p
    C=[1]
    for j in range(d):
        num=9*(4*j+1)**3
        den=(4*j+2)*(4*j+3)*(4*j+4)
        C.append(C[-1]*(num % m)*pow(den,-1,m)%m)
    cinv=pow(C[-1],-1,m)
    B=1;H=0
    sum_b=0;sum_wb=0;sum_wh=0
    for r in range(d+1):
        if r:
            i=r
            num=(4*i+1)*(4*i)*(4*i-1)
            den=9*(4*i+2)**3
            B=B*(num%m)*pow(den,-1,m)%m
            delta=(pow(4*i+1,-1,m)+pow(4*i,-1,m)+pow(4*i-1,-1,m)-3*pow(4*i+2,-1,m))%m
            H=(H+delta)%m
        direct=C[d-r]*cinv%m
        assert direct%p==B%p, ('fast-p',p,r)
        assert direct==(B*(1-p*H))%m, ('fast-p2',p,r)
        sum_b=(sum_b+B)%m
        sum_wb=(sum_wb+(8*r+5)*B)%m
        sum_wh=(sum_wh+(8*r+5)*B*H)%m
    T=sum((8*j+1)*c for j,c in enumerate(C))%m
    rhs=(-sum_wb+p*(2*sum_b+sum_wh))%m
    assert T*cinv%m==rhs, ('fast-sum',p)
    return d,T


if __name__=='__main__':
    small=[p for p in primes_up_to(151) if p>3 and p%4==3]
    for p in small:
        check(p)
    fast=[p for p in primes_up_to(2000) if p>3 and p%4==3]
    for p in fast: check_modular_fast(p)
    print('GH9/GH10 PASS: exact rational checks',len(small),'primes <=151, independent modular p/p^2 checks',len(fast),'primes <2000')
    for p in (7,11,19,43,67,139):
        d,T,cd=check(p)
        print(f'p={p},d={d},C_d mod p^2={cd},T mod p^2={T},T/p mod p={T//p if T%p==0 else "not divisible"}')
