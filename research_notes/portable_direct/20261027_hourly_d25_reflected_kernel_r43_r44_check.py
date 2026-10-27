#!/usr/bin/env python3
"""D25 R43/R44 author exact certificates; stdlib integers/Fraction, no floats."""
from fractions import Fraction
from math import factorial, isqrt


def primes_6m1(limit=997):
    for p in range(7, limit + 1):
        if p % 6 == 1 and all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def valuation_type(p, k):
    q2, q3, q4 = 2*k//p, 3*k//p, 4*k//p
    return q4-q2-q3


def coefficient(p, k, modulus):
    q2, q3, q4 = 2*k//p, 3*k//p, 4*k//p
    e = q4-q2-q3
    n = factorial(q4)*factorial(3-q4)
    d = factorial(q2)*factorial(1-q2)*factorial(q3)*factorial(2-q3)
    return (-1 if e & 1 else 1)*n*pow(16*d, -1, modulus) % modulus


def reduced_rational(x, p):
    assert x.denominator % p
    return x.numerator * pow(x.denominator, -1, p) % p


def run():
    primes = ranks = pairs = raw_checks = 0
    samples = []
    for p in primes_6m1():
        primes += 1
        p2 = p*p
        # p-free factorial prefix: F(n)=n!/p^floor(n/p), since n<4p<p^2.
        pf = [1]*(4*p)
        for n in range(1, 4*p):
            pf[n] = pf[n-1] * (n//p if n % p == 0 else n) % p2
        harmonic = [0]*p
        for n in range(1, p):
            harmonic[n] = (harmonic[n-1] + pow(n, -1, p)) % p
        # Fermat quotient of 3/32 = q_p(3)-5q_p(2) modulo p.
        qrat = ((pow(3,p-1,p2)-1)//p - 5*((pow(2,p-1,p2)-1)//p)) % p
        b = 3*pow(32, -1, p2) % p2
        def u(k):
            return (pow(b,k,p2)*pf[k]*pf[4*k]
                    *pow(pf[2*k]*pf[3*k] % p2, -1, p2)) % p2
        uv = [u(k) for k in range(p)]
        m = (p-1)//6
        positive = [k for k in range(1,p) if valuation_type(p,k) == 1]
        negative = [k for k in range(1,p) if valuation_type(p,k) == -1]
        assert len(positive) == len(negative) == (m+1)//2
        assert negative == sorted(p-k for k in positive)
        prod = 1
        for k in range(1,p):
            prod = prod * uv[k] % p
            e = valuation_type(p,k)
            assert e in (-1,0,1)
            assert valuation_type(p,p-k) == -e
            assert uv[k] % p != 0
            c = coefficient(p,k,p2)
            r2, r3, r4 = 2*k%p, 3*k%p, 4*k%p
            jet = (qrat + harmonic[k-1] + 4*harmonic[r4-1]
                   -2*harmonic[r2-1] -3*harmonic[r3-1]) % p
            lhs = uv[k]*uv[p-k] % p2
            rhs = c*(1+p*jet) % p2
            assert lhs == rhs, (p,k,lhs,rhs)
            ranks += 1
            if k < p-k:
                pairs += 1
        A, B = (3*m)//2, (m+1)//2
        assert A+B == 2*m
        global_product = ((-1 if B % 2 else 1)*pow(3,A,p)
                          *pow(pow(2,11*m,p),-1,p)) % p
        assert prod == global_product, (p,prod,global_product)
        if p <= 31:
            for k in range(1,p):
                tau = Fraction(factorial(k)*factorial(4*k)*3**k,
                               factorial(2*k)*factorial(3*k)*32**k)
                e = valuation_type(p,k)
                unit = tau / (p**e) if e >= 0 else tau*(p**(-e))
                assert reduced_rational(unit,p) == uv[k] % p
                raw_checks += 1
        if p in (7,13,19,181,373,733):
            k = positive[0]
            samples.append((p,k,p-k,uv[k]%p,uv[p-k]%p,
                            uv[k]*uv[p-k]%p,prod))
    assert primes == 80 and ranks == 36588 and pairs == 18294
    assert raw_checks == 66
    print('PASS: primes=%d ranks=%d reflected_pairs=%d exact_Fraction=%d' %
          (primes,ranks,pairs,raw_checks))
    print('Sample tuples (p,k,p-k,u_k mod p,u_ref mod p,pair mod p,global product):')
    for row in samples:
        print(row)


if __name__ == '__main__':
    run()
