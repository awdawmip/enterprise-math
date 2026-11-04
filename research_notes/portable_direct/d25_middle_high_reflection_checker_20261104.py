"""Exact D25 middle/high complementary-index signed-port checks.

Recomputes original a_k and b_k from factorial-unit arrays at p^3 precision.
One checker for the proved reciprocal invariant, another for finite signed data.
All arithmetic is integer modular; finite checks are not an all-prime proof.
"""
from math import isqrt, factorial
import json


def primes(limit):
    sieve = bytearray(b'\\x01') * (limit + 1)
    sieve[:2] = b'\\x00\\x00'
    for d in range(2, isqrt(limit) + 1):
        if sieve[d]:
            sieve[d*d::d] = b'\\x00' * ((limit-d*d)//d+1)
    return [p for p in range(7, limit+1) if sieve[p] and p % 6 == 1]


def units(nmax, p, modulus):
    fact = [1] * (nmax + 1)
    for j in range(1, nmax + 1):
        x = j
        while x % p == 0:
            x //= p
        fact[j] = fact[j-1] * x % modulus
    return fact


def a216(k, p, fact, modulus):
    val = (2*k)//p + (3*k)//p
    if val >= 3:
        return 0
    den = fact[k]**5 * pow(216, k, modulus) % modulus
    return pow(p, val, modulus)*fact[2*k]*fact[3*k]*pow(den, -1, modulus)%modulus


def b2304(k, p, fact, modulus):
    val = (4*k)//p
    if val >= 3:
        return 0
    den = fact[k]**4 * pow(2304, k, modulus) % modulus
    return pow(p, val, modulus)*fact[4*k]*pow(den, -1, modulus)%modulus


def check():
    total_pairs = 0
    factorial_spots = 0
    samples = {}
    ps = primes(2000)
    for p in ps:
        r = (p - 1)//6
        h = 3*r
        mod = p**3
        f = units(4*p, p, mod)
        parts = [0, 0, 0]
        for k in range(p):
            val = (2*k)//p + (3*k)//p
            if val <= 2:
                parts[val] = (parts[val] + (6*k+1)*a216(k,p,f,mod))%mod
        half = sum((8*k+1)*b2304(k,p,f,mod) for k in range(h+1))%mod
        full = sum((8*k+1)*b2304(k,p,f,mod) for k in range(p))%mod
        assert half == full, (p,'quartic-cutoff',half,full)
        mdiff = (parts[0]+parts[1]-half)%mod
        assert mdiff % p**2 == 0, (p,'integrality',mdiff)
        mval = mdiff//p**2
        high_observer = 0
        for n in range(r):
            mid = a216(h-n,p,f,mod)
            hi = a216(h+1+n,p,f,mod)
            assert mid%p == 0 and hi%p**2 == 0
            m = mid//p%p
            q = hi//p**2%p
            assert m and q
            invariant = (2*n+1)**3*m*q%p
            expected = -2*pow(9,-1,p)%p
            assert invariant == expected, (p,n,invariant,expected)
            reciprocal = -2*pow(9*(2*n+1)**3*m,-1,p)%p
            assert q == reciprocal, (p,n,q,reciprocal)
            high_observer = (high_observer+(6*n+4)*reciprocal)%p
            total_pairs += 1
            if p in (7,13,19,37,373) and n in (0,1,r-1):
                for k,v,x in ((h-n,1,m),(h+1+n,2,q)):
                    numerator = factorial(2*k)*factorial(3*k)
                    denominator = factorial(k)**5*216**k
                    assert numerator%p**v == 0
                    assert (numerator//p**v)*pow(denominator,-1,p)%p == x
                    factorial_spots += 1
                samples.setdefault(str(p),[]).append((n,m,q,invariant))
        hval = parts[2]//p**2
        assert hval == high_observer, (p,hval,high_observer)
        # Second check is a finite observation only, not part of the proof.
        assert (mval+hval)%p == 0, (p,mval,hval)
    return {
      "prime_count":len(ps),"tested_pairs":total_pairs,
      "ordinary_factorial_spots":factorial_spots,
      "finite_signed_bridge_tests":len(ps),
      "samples":samples,
      "native_H0_B0_executed":False,
      "status":"FINITE_EXACT_CHECK_ONLY",
    }


if __name__ == "__main__":
    print(json.dumps(check(),indent=2))
