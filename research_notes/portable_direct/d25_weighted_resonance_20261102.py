#!/usr/bin/env python3
"""Exact finite check: 2304 weighted resonance for p>=5, via independent paths."""
from math import factorial


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n+1)
    sieve[:2] = b'\x00\x00'
    for q in range(2, int(n**0.5)+1):
        if sieve[q]:
            sieve[q*q:n+1:q] = b'\x00' * (((n-q*q)//q)+1)
    return [p for p in range(5,n+1) if sieve[p]]


def factorial_mod(n,p):
    a=1
    for i in range(2,n+1): a=(a*i)%p
    return a


def unit_factorial_mod(n,p):
    # floor(n/p)<p for the range used; delete each factor of p exactly.
    unit=1
    for j in range(1,n+1):
        t=j
        while t%p==0: t//=p
        unit=unit*(t%p)%p
    return unit


def one_prime(p):
    m=next(t for t in (1,3,5,7) if (t*p)%8 == 1)
    k=(m*p-1)//8
    r=(m-1)//2
    assert 4*k == r*p+(p-1)//2
    norm=pow(2304, k, p)
    denom=(pow(factorial_mod(k,p),4,p)*norm)%p
    vp_m=1 if m%p==0 else 0
    m_unit=m//(p**vp_m)
    valuation=r+1+vp_m
    pred=(m_unit * ((-1)**r) * factorial(r)*factorial_mod((p-1)//2,p) * pow(denom,-1,p))%p
    actual=(m_unit*unit_factorial_mod(4*k,p)*pow(denom,-1,p))%p
    assert actual==pred and actual!=0, (p,m,k,actual,pred)
    # Independent exact finite-ring coefficient recurrence: a_k=(4k)!/(k!)^4 /2304^k.
    modulus=p**7
    a=1; resonance=None; total=0
    for j in range(p):
        term=(a*(8*j+1))%modulus
        total=(total+term)%modulus
        if j==k: resonance=term
        if j<p-1:
            a=a* ((4*j+1)*(4*j+2)*(4*j+3)*(4*j+4))
            a=a*pow(((j+1)**4)*2304,-1,modulus)%modulus
    assert resonance is not None
    assert total%(p**3) == (p if p%3 == 1 else -p)%(p**3), (p, total%(p**3))
    assert resonance%p**valuation==0
    assert ((resonance//p**valuation)%p)==pred
    assert resonance%p**(valuation+1) != 0
    if p%24==19:
        assert ((total-resonance-p)%(p**3)) == (-p*p*pred)%(p**3)
    if p%24==13:
        assert (total-resonance-p)%(p**3) == 0
    return (p, m, k, valuation, pred)

if __name__=='__main__':
    ps=primes_upto(997)
    rows=[one_prime(p) for p in ps]
    print('PASS_COUNT=',len(rows))
    print('COUNT_BY_M=',{m:sum(x[1]==m for x in rows) for m in (1,3,5,7)})
    print('TARGET_13_19=',[row for row in rows if row[0] in (13,19,37,43,61,67,163,373)])
    print('ALL_RESIDUES_NONZERO=True; MAX_P=997')
