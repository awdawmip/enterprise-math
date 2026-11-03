#!/usr/bin/env python3
"""Original 216/2304 modular cubic-boundary checker. Python stdlib only."""
from math import comb, factorial

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n+1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(n**.5)+1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00'*((n-i*i)//i+1)
    return [i for i in range(5,n+1) if sieve[i]]

def coeffs(p,d,a):
    m=p**5
    values=[1]
    for k in range(p-1):
        values.append(values[-1]*a(k)*pow(d*(k+1)**3,-1,m)%m)
    return values

def verify(p):
    m=p**5
    b=coeffs(p,36,lambda k:(2*k+1)*(3*k+1)*(3*k+2))
    c=coeffs(p,576,lambda k:(4*k+1)*(4*k+2)*(4*k+3))
    lhs_b=sum((-18*k**3+27*k**2+13*k+2)*v for k,v in enumerate(b))%m
    lhs_c=sum((-512*k**3+96*k**2+44*k+6)*v for k,v in enumerate(c))%m
    q_b=(pow(216,p-1,p**2)-1)//p
    q_c=(pow(2304,p-1,p**2)-1)//p
    assert lhs_b==(2*p**3-2*q_b*p**4)%m, (p,"216")
    assert lhs_c==(6*p**3-6*q_c*p**4)%m, (p,"2304")
    if p in (5,7,13,19,37,373):
        bp=comb(2*p,p)**2*comb(3*p,p)*pow(216,-p,m)%m
        cp=(factorial(4*p)//factorial(p)**4)*pow(2304,-p,m)%m
        assert lhs_b==36*p**3*bp%m
        assert lhs_c==576*p**3*cp%m
        assert bp%p**2==pow(18,-1,p**2)*(1-p*q_b)%p**2
        assert cp%p**2==pow(96,-1,p**2)*(1-p*q_c)%p**2
    return p,q_b,q_c,lhs_b,lhs_c

if __name__=="__main__":
    ps=primes_upto(2000)
    data=[verify(p) for p in ps]
    print("PASS",len(ps),"primes 5..2000 modulo p^5 (both source kernels)")
    for p in (5,7,13,19,37,373):
        print(next(row for row in data if row[0]==p))
