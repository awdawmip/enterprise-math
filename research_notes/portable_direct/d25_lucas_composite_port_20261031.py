#!/usr/bin/env python3
"""D25 author-side finite-field Lucas port for the integer toric carrier.

No native H0/B0, Source ownership or mathematical admission is claimed.
Exact integer and modular arithmetic only; standard library.
"""
from math import comb


def primes_through(limit):
    s = bytearray(b'\x01') * (limit + 1)
    s[:2] = b'\x00\x00'
    for j in range(2, int(limit ** 0.5) + 1):
        if s[j]:
            s[j * j:limit + 1:j] = b'\x00' * ((limit - j * j) // j + 1)
    return [j for j in range(5, limit + 1) if s[j]]


def local_factor_scaled(p):
    """Return exact 2^d * local factor for p|6*l+1 (d=min low digit)."""
    r = (-pow(6, -1, p)) % p
    a, b, c = (3 * r) % p, (2 * r) % p, (4 * r) % p
    d = min(a, b, c)
    assert d == (p - 1) // 3
    f = sum((6*k + 1) * (-1)**k * 2**(d-k)
            * comb(a, k) * comb(b, k) * comb(c, k)
            for k in range(d+1))
    return r, (a, b, c), d, f


def direct_U_mod(l, p):
    n = 6*l+1
    assert n % p == 0
    return sum((6*k + 1) * (-1)**k * pow(2, 2*l-k, p)
               * comb(3*l, k) * comb(2*l, k) * comb(4*l, k)
               for k in range(2*l+1)) % p


def lucas_factor_mod(l, p):
    """Frobenius/Lucas factorization with signed/weighted first digit retained."""
    tops = [3*l, 2*l, 4*l]
    factor = 1
    digit = 0
    inv2 = pow(2, -1, p)
    while any(tops):
        digits = [n % p for n in tops]
        tops = [n // p for n in tops]
        cutoff = min(digits)
        inner = 0
        for k in range(cutoff+1):
            base = (-inv2)**k * comb(digits[0], k) * comb(digits[1], k) * comb(digits[2], k)
            if digit == 0:
                base *= 6*k+1
            inner = (inner + base) % p
        factor = (factor*inner) % p
        digit += 1
    return pow(2, 2*l, p)*factor % p


def run():
    cap = 997
    plist = primes_through(cap)
    assert plist[-1] == 997
    vals = {}
    for p in plist:
        r, digits, d, num = local_factor_scaled(p)
        assert num % p == 0, (p, num % p)
        vals[p] = (r, digits, d, num)
    for p, numerator in [(5,-40), (7,-98), (11,6798), (13,-23686), (17,-497080)]:
        # Exact scaled numbers; denominator is 2^d.
        assert vals[p][3] == numerator, (p, vals[p][3], numerator)
    probes = [4, 8, 14, 19, 20, 28, 39, 49, 50, 57, 64, 79, 80, 104, 125, 150, 200, 250, 300, 400]
    count = 0
    for l in probes:
        n = 6*l+1
        for p in plist:
            if n%p==0:
                observed = direct_U_mod(l,p)
                decomposed = lucas_factor_mod(l,p)
                assert observed == decomposed == 0, (l,p,observed,decomposed)
                count += 1
    print('PASS_D25_LUCAS_TORIC_FINITE_PRIME_FACTORS_20261031')
    print('PRIMES_CHECKED', len(plist), 'MAX_PRIME', plist[-1])
    print('PROBES',len(probes),'DIVISOR_PROBES',count)
    for p in (5,7,11,13,17,19,23,29):
        r,digits,d,num=vals[p]
        print('LOCAL',p,'l0',r,'digits',digits,'d',d,'numerator',num,'denominator',2**d,'quotient_mod_p',num//p%p)

if __name__ == '__main__':
    run()
