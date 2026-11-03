#!/usr/bin/env python3
"""Exact finite-field D25 H2 carrier/checker; no external deps or native benchmark."""
from math import comb

def primes(n):
    sieve = bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for i in range(2,int(n**0.5)+1):
        if sieve[i]: sieve[i*i:n+1:i]=b'\x00'*(((n-i*i)//i)+1)
    return [i for i in range(7,n+1) if sieve[i] and i%6==1]

def inv(x,p):
    return pow(x%p,-1,p)

def fact_units(p,stop):
    values=[1]*(stop+1)
    for k in range(1,stop+1):
        values[k] = values[k-1] * (1 if k%p==0 else k) % p
    return values

def b_reduced(k,p,f):
    valuation=2*k//p+3*k//p
    denominator = pow(f[k],5,p)*pow(216,k,p)%p
    return valuation, (f[2*k]*f[3*k]*inv(denominator,p))%p

def verify(p):
    r=(p-1)//6
    a,b=3*r+1,4*r
    f=fact_units(p,3*b)
    vL,L=b_reduced(3*r,p,f)
    assert vL==1
    character=pow(6,(p-1)//2,p)
    assert character in (1,p-1)
    chi=1 if character==1 else -1
    assert L == (-2*chi)%p
    assert L*L%p == 4%p
    high=0
    for k in range(a,b+1):
        v,u=b_reduced(k,p,f)
        assert v==2
        high=(high+(6*k+1)*u)%p
    # Direct modular hypergeometric coefficient recurrence at x=1/2.
    term=1
    weighted=4
    terms=[1]
    for s in range(1,r):
        numerator=s*(36*s*s-1)
        denominator=9*(2*s+1)**3
        term=term*numerator*inv(denominator,p)%p
        terms.append(term)
        weighted=(weighted+(6*s+4)*term)%p
    high_from_hyper=chi*inv(9,p)*weighted%p
    assert high_from_hyper==high, (p,high,high_from_hyper)
    # Independent recurrence-derived polynomial for 4F3 differential equation:
    # D=theta(theta+1/2)^3 - x(theta+1)^2(theta+5/6)(theta+7/6).
    coeff=[(v*pow(2,i,p))%p for i,v in enumerate(terms)]
    for s in range(1,r+1):
        lhs=0 if s==r else s*pow((2*s+1)*inv(2,p)%p,3,p)*coeff[s]%p
        rhs=s*s*((36*s*s-1)*inv(36,p)%p)*coeff[s-1]%p
        assert lhs==rhs,(p,s,lhs,rhs)
    return (p,r,L,chi,high,weighted)

def independent_binomial_high(p):
    r=(p-1)//6
    m=p**3
    inv216=pow(216,-1,m)
    total=0
    for k in range(3*r+1,4*r+1):
        b=comb(2*k,k)**2*comb(3*k,k)*pow(inv216,k,m)%m
        total=(total+(6*k+1)*b)%m
    assert total%p**2==0
    return total//p**2

if __name__=='__main__':
    test_primes=primes(2000)
    assert len(test_primes)==148,len(test_primes)
    rows=[verify(p) for p in test_primes]
    for p in (7,13,19,37,373):
        direct=independent_binomial_high(p)
        observed=next(row for row in rows if row[0]==p)
        assert direct==observed[4]
        print(f'p={p} r={observed[1]} L={observed[2]} chi6={observed[3]:+d} '
              f'H2_over_p2={observed[4]} weighted_4F3={observed[5]}')
    print(f'PASS: {len(rows)} primes p<=2000, p=1 (mod 6); '
          f'quadratic boundary L, hypergeometric H2 and order-4 ODE; '
          f'5 independent binomial checks.')
