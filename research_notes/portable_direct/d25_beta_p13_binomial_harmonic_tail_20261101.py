#!/usr/bin/env python3
"""D25 p=5 (mod 8) beta Gauss modulo p^2: independent combinatorial decomposition.
Author-side proof regression; NOT native H0/B0, NOT formal Source Result.
"""
from math import isqrt, comb, factorial


def primes(limit):
    sieve = bytearray(b'\1') * (limit + 1)
    sieve[:2] = b'\0\0'
    for j in range(2, isqrt(limit) + 1):
        if sieve[j]:
            sieve[j * j:limit + 1:j] = b'\0' * ((limit - j * j) // j + 1)
    return [p for p in range(11, limit + 1) if sieve[p] and p % 8 == 5]


def original_beta(p):
    mod = p * p
    beta = [1]
    for k in range(p - 1):
        beta.append(beta[-1] * (8*k+1) * (8*k+3)
                    * pow(576 * (k+1)**2, -1, mod) % mod)
    return beta


def source_decomposition(p):
    assert p > 7 and p % 8 == 5
    mod = p*p
    a = (5*p-1)//8
    b = (7*p-3)//8
    d = (p-1)//4
    inv8 = pow(8, -1, p)
    inv9 = pow(9, -1, mod)
    harmonic = [0]*(b+1)
    for j in range(1,b+1):
        harmonic[j] = (harmonic[j-1] + pow(j,-1,p)) % p

    base = 0
    harmonic_carry = 0
    coefficient = 1
    for k in range(a+1):
        # c_k = binom(a,k)*binom(b,k)*9^(-k), in Z/p^2.
        if k:
            coefficient = (coefficient * (a-k+1) * (b-k+1)
                           * pow(k*k*9, -1, mod)) % mod
        delta_a = (harmonic[a] - harmonic[a-k]) % p
        delta_b = (harmonic[b] - harmonic[b-k]) % p
        base = (base + coefficient) % mod
        harmonic_carry = (harmonic_carry - coefficient * inv8
                          * (5*delta_a+7*delta_b)) % p

    endpoint = comb(b,a)*pow(inv9,a,p) % p
    reflected = 1
    reflected_sum = 1
    for r in range(1,d):
        reflected = (reflected * (8*r)*(8*r+2)
                     * pow(9*(8*r+7)**2, -1, p)) % p
        reflected_sum = (reflected_sum + reflected) % p
    tail_carry = 10 * pow(441,-1,p) * endpoint * reflected_sum % p

    total = (base + p*(harmonic_carry + tail_carry)) % mod
    return {"p":p,"a":a,"b":b,"d":d,"J":base,
            "Hcarry":harmonic_carry,"tailcarry":tail_carry,
            "G":total,"tail_norm":tail_carry,
            "J_divp":base//p if base%p==0 else None,
            "G_divp":total//p if total%p==0 else None}


def test(limit=3000):
    ps = primes(limit)
    for p in ps:
        u = source_decomposition(p)
        beta = original_beta(p)
        a,b = u['a'],u['b']
        mod = p*p
        tail = sum(beta[a+1:b+1])%mod
        assert sum(beta[b+1:])%mod == 0
        assert tail//p == u['tailcarry']
        assert sum(beta[:a+1])%mod == (u['J']+p*u['Hcarry'])%mod
        assert sum(beta)%mod == u['G']
        assert beta[a]%p == comb(b,a)*pow(9,-a,p)%p
        assert beta[a+1]//p == 10*pow(441,-1,p)*beta[a]%p
        # This branch of the original D25 target has chi_{-6}=-1:
        if p%24 == 13:
            assert u['G'] == 0  # finite regression of still-unproved p^2 annihilation
        else:
            assert p%24 == 5 and u['G']%p != 0  # split-prime control
        if p in (13,29,37,61,373):
            numerator = 1
            for k in range(p):
                if k:
                    numerator *= (8*(k-1)+1)*(8*(k-1)+3)
                direct = numerator * pow(576**k*factorial(k)**2,-1,mod)%mod
                assert direct == beta[k]
        if p in (13,29,37,61,109,373,541):
            print({**u,"actual_tail":tail})
    print("PASS",len(ps),"p=5 mod 8 primes <=",limit,"including",sum(p%24==13 for p in ps),"p=13 mod 24 target primes")

if __name__ == '__main__':
    test()
