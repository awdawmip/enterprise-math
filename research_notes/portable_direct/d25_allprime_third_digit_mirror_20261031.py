#!/usr/bin/env python3
"""Exact modular verifier of the all-prime p^3 Clausen reciprocal-mirror lift.

This is author-side computational evidence, not a formal proof or native EM run.
"""
from math import comb


def primerange(lo, hi):
    sieve=bytearray(b"\x01")*hi
    sieve[:2]=b"\x00\x00"
    for k in range(2,int(hi**0.5)+1):
        if sieve[k]:
            sieve[k*k:hi:k]=b"\x00"*(((hi-1-k*k)//k)+1)
    return (p for p in range(max(2,lo),hi) if sieve[p])

def inv(n, modulus):
    return pow(n % modulus, -1, modulus)


def residue_frac(num, den, mod):
    return (num * inv(den, mod)) % mod


def check_prime(p):
    mod = p**3
    mod_full = p**6
    h = (p - 1)//3
    # Recur the ORIGINAL a_n through p-1, with unit denominators.
    a = [1]
    for n in range(p-1):
        ratio_num = (2*n+1)*(3*n+1)*(3*n+2)
        ratio_den = 36*(n+1)**3
        a.append(a[-1]*ratio_num*inv(ratio_den,mod_full)%mod_full)
    # Fermat quotient q216 modulo p^2 (p^3 lift is not necessary).
    q216 = ((pow(216,p-1,p**3)-1)//p) % (p**2)
    half=inv(2,mod)
    quarter=inv(4,mod)
    A=(13*half-q216)%mod
    B=(115*quarter-13*half*q216+q216*q216)%mod
    # Independent exact-original endpoint M_1.
    assert a[p-1] % p**3 == 0
    endpoint = (-a[p-1]//p**3)%mod
    assert endpoint == (1 + p*A + p*p*B)%mod, ('endpoint',p, endpoint)
    H=0
    D=0
    signed_raw=0
    signed_mirror=0
    for k in range(1,h+1):
        if k>1:
            j=k
            H=(H + residue_frac(2,2*j-1,mod)+residue_frac(3,3*j-1,mod)
               +residue_frac(3,3*j-2,mod)-residue_frac(3,j-1,mod))%mod
            D=(D - residue_frac(3,(j-1)**2,mod)
                +residue_frac(4,(2*j-1)**2,mod)
                +residue_frac(9,(3*j-1)**2,mod)
                +residue_frac(9,(3*j-2)**2,mod))%mod
        assert a[p-k] % p**3 == 0
        M = (-18*k**3*a[k]*(a[p-k]//p**3))%mod
        predicted=(1+p*(A+H)+p*p*(B+A*H+(H*H+D)*inv(2,mod)))%mod
        assert M == predicted, ('mirror',p,k,M,predicted)
        weight=6*(p-k)+1
        signed_raw=(signed_raw+weight*(a[p-k]//p**3))%mod
        signed_mirror=(signed_mirror-weight*predicted*inv(18*k**3*a[k],mod))%mod
    assert signed_raw == signed_mirror, ('weighted_tail',p,signed_raw,signed_mirror)
    return h, endpoint, q216


def independent_anchor(p):
    # Original binomial integers, not the modular coefficient recurrence.
    e = comb(2*p-2,p-1)**2*comb(3*p-3,p-1)
    assert e % p**3 == 0
    v = (-e//p**3) * inv(pow(216,p-1,p**3),p**3) % p**3
    return v


def main():
    primes = list(primerange(5,3001))
    total=0
    anchors={5,7,11,17,23,29,37,157,373,1327}
    print('CASE p   k_max    M1_mod_p3   Q216_mod_p2')
    for p in primes:
        h, endpoint, q216=check_prime(p)
        total+=h
        if p in anchors:
            assert independent_anchor(p) == endpoint
            print(p,h,endpoint,q216)
    print('PRIMES',len(primes),'MIRROR_PAIRS',total,'WEIGHTED_TAILS',len(primes),'ANCHORS',sum(x in primes for x in anchors))
    print('PASS_D25_ALL_PRIME_THIRD_DIGIT_RECIPROCAL_MIRROR_EXACT')

if __name__=='__main__':
    main()
