#!/usr/bin/env python3
"""Bounded exact certificate; not a universal prime theorem."""
from math import isqrt, comb
from collections import Counter
LIMIT = 10000
sieve = bytearray(b'\1') * (LIMIT + 1)
sieve[0:2] = b'\0\0'
for d in range(2, isqrt(LIMIT) + 1):
    if sieve[d]:
        sieve[d*d:LIMIT+1:d] = b'\0' * ((LIMIT-d*d)//d+1)
primes = [p for p in range(5,LIMIT+1) if sieve[p]]
counts = Counter()
failures = []
def value(p, exp=3):
    mod = p**exp
    term, total = 1, 0
    for k in range(p):
        total = (total+(6*k+1)*term) % mod
        if k+1 < p:
            term = (term*(2*k+1)*(3*k+1)*(3*k+2)
                    *pow(36*(k+1)**3,-1,mod)) % mod
    return total
for p in primes:
    counts[p%24] += 1
    expected = (p if p%3==1 else -p) % p**3
    observed = value(p)
    if observed != expected:
        failures.append((p,observed,expected))
    r = (p-1)//6 if p%6==1 else (p-5)//6
    cuts = (2*r,3*r,4*r) if p%6==1 else (2*r+1,3*r+2,4*r+3)
    if p <= 397:
        for k in range(p):
            num = comb(2*k,k)**2 * comb(3*k,k)
            v = 0
            while num%p==0:
                num//=p
                v+=1
            predicted = sum(k>q for q in cuts)
            if v!=predicted:
                failures.append((p,k,v,predicted))
for p in (5,7,11,13,19,31,37,61,109,373):
    mod=p**3
    inv=pow(216,-1,mod)
    independent=sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(inv,k,mod)
                    for k in range(p))%mod
    assert independent==value(p),(p,independent,value(p))
assert len(primes)==1227
assert not failures, failures[:10]
assert (value(7,4)-7)%(7**4)//(7**3)==1
assert (value(11,4)+11)%(11**4)//(11**3)==2
print({'domain':'all primes 5..10000','n':len(primes),
       'p_mod_3_counts':{'1':sum(p%3==1 for p in primes),'2':sum(p%3==2 for p in primes)},
       'mod_24_counts':dict(sorted(counts.items())),
       'exact_mismatches':len(failures),'independent_binomial_checks':10,
       'p4_correction_7':1,'p4_correction_11':2})
