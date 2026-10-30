#!/usr/bin/env python3
"""Exact independent finite-prime check for the reversed terminating 4F3 D25 strip.

All arithmetic uses integer residues and modular inverses; no floats.
This is author-side evidence, not a native divided-power or Frobenius run.
"""
from math import factorial


def primes(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for i in range(2, int(limit**.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = b'\x00' * (((limit-i*i)//i)+1)
    return [p for p in range(7, limit+1) if sieve[p] and p % 6 == 1]


def modular_216_coeffs(p):
    modulus = p*p
    values = [1]
    for n in range(p-1):
        v = values[-1] * (2*n+1)*(3*n+1)*(3*n+2)
        v *= pow(36*(n+1)**3, -1, modulus)
        values.append(v % modulus)
    return values


def original_signed_middle_inverse(p, l):
    # Source: independent original (1/2,1/3,2/3)/2^n n!^3 recurrence
    m, h = 2*l, 3*l
    a = modular_216_coeffs(p)
    answer = 0
    for k in range(m+1, h+1):
        assert a[k] % p == 0
        unit = (a[k] // p) % p
        assert unit
        answer += (1 - 6*k)*pow(36*k**3*unit, -1, p)
    return answer % p


def factorial_direct(p, l):
    m, h = 2*l, 3*l
    C = factorial(h)*factorial(2*m)*factorial(m) % p
    assert C
    vals = []
    for j in range(1, l+1):
        t = pow(2,m+j,p)*pow(factorial(m+j-1),3,p)
        t *= factorial(l-j)*factorial(m-j)
        t *= pow(factorial(j-1),-1,p)
        vals.append(t%p)
    I = sum((1-6*m-6*j)*val for j,val in enumerate(vals,1))*pow(12*C,-1,p)%p
    return I, vals


def reversed_4f3(p, l):
    # 4F3(1,1,1-l,1+l;1-3l,1-3l,1-3l; z)
    # weighted (4+6 theta) at z=1/2, in F_p
    hs = [1]
    inv2 = pow(2,-1,p)
    for s in range(1,l):
        den = (s-3*l)**3
        assert den % p
        hs.append(hs[-1]*s*(s-l)*(s+l)*pow(den,-1,p)*inv2 % p)
    # The terminating hypergeometric differential equation has zero
    # coefficient at each n >= 0.  For n=l the source vanishes at n-l=0.
    for n in range(1,l+1):
        left = n*(n-3*l)**3*(hs[n] if n<l else 0)
        right = n*n*(n-l)*(n+l)*hs[n-1]
        assert (left-right*inv2)%p == 0, (p,n,left,right)
    weighted = sum((4+6*s)*h for s,h in enumerate(hs)) % p
    prefactor = pow(2,3*l,p)*pow(factorial(3*l-1),2,p)
    prefactor *= pow(36*factorial(4*l)*factorial(2*l),-1,p)
    return prefactor*weighted%p, hs


def check(prime_limit=5000):
    tested = primes(prime_limit)
    anchors = {}
    terms = 0
    for p in tested:
        l = (p-1)//6
        i_orig = original_signed_middle_inverse(p,l)
        i_fact, ts = factorial_direct(p,l)
        i_4f3, hs = reversed_4f3(p,l)
        assert i_orig == i_fact == i_4f3, (p,i_orig,i_fact,i_4f3)
        tl_inv = pow(ts[-1],-1,p)
        for s in range(l):
            assert hs[s] == ts[l-1-s]*tl_inv%p, (p,s)
            terms += 1
        if p in (7,13,19,37,67,157,373,1327,3347):
            anchors[p] = i_orig
    assert len(tested)==330
    assert len([p for p in tested if p%24 in (13,19)])==166
    for p,v in {7:5,13:10,19:9,37:20,67:58,157:98,373:266}.items():
        assert anchors[p]==v, (p,anchors.get(p))
    print('PRIMES',len(tested),'D25_TARGETS',166,'REVERSED_TERMS',terms)
    print('ANCHORS',','.join(f'{k}:{anchors[k]}' for k in sorted(anchors)))
    print('PASS_D25_TERMINATING_REVERSED_4F3_SIGNED_E2_STRIP_EXACT')


if __name__=='__main__':
    check()
