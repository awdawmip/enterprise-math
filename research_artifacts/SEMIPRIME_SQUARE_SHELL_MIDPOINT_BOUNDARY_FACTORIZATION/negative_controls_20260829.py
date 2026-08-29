#!/usr/bin/env python3
"""Deterministic negative-control replay for the semiprime shell exploration."""
import bisect, math, random

LIMIT=10_000_000
COUNT=2000
KMAX=64

def ceil_sqrt(n):
    s=math.isqrt(n)
    return s if s*s==n else s+1

def sieve(limit):
    isp=bytearray(b"\x01")*(limit+1)
    isp[:2]=b"\x00\x00"
    for i in range(2,math.isqrt(limit)+1):
        if isp[i]:
            st=i*i
            isp[st:limit+1:i]=b"\x00"*(((limit-st)//i)+1)
    return [i for i in range(2,limit+1) if isp[i]]

def immediate_hit(n):
    for k in range(1,KMAX+1):
        g0=math.gcd(k,n)
        if 1<g0<n:
            return True
        c=ceil_sqrt(4*k*n)
        d=c*c-4*k*n
        y=math.isqrt(d)
        if y*y==d:
            g=math.gcd(c-y,n)
            if 1<g<n:
                return True
    return False

def main():
    primes=sieve(LIMIT)
    rng=random.Random(77173)
    lo=max(101,LIMIT//10)
    pool=primes[bisect.bisect_left(primes,lo):]
    prime_sample=[pool[rng.randrange(len(pool))] for _ in range(COUNT)]
    small=[p for p in primes if 3<=p<=int(LIMIT**(1/3))*5]
    triples=[]
    while len(triples)<COUNT:
        a,b,c=rng.choice(small),rng.choice(small),rng.choice(small)
        n=a*b*c
        if n<=LIMIT and n&1:
            triples.append(n)
    random_odd=[rng.randrange(3,LIMIT,2) for _ in range(COUNT)]
    got={
      "prime_controls":COUNT,
      "prime_nontrivial_immediate_hits":sum(immediate_hit(n) for n in prime_sample),
      "three_prime_composite_controls":COUNT,
      "three_prime_nontrivial_immediate_hits":sum(immediate_hit(n) for n in triples),
      "random_odd_controls":COUNT,
      "random_odd_nontrivial_immediate_hits":sum(immediate_hit(n) for n in random_odd),
    }
    expected={
      "prime_controls":2000,
      "prime_nontrivial_immediate_hits":0,
      "three_prime_composite_controls":2000,
      "three_prime_nontrivial_immediate_hits":1885,
      "random_odd_controls":2000,
      "random_odd_nontrivial_immediate_hits":1619,
    }
    assert got==expected,(got,expected)
    print(got)
    print("SEMIPRIME_SHELL_NEGATIVE_CONTROLS=PASS")

if __name__=="__main__":
    main()
