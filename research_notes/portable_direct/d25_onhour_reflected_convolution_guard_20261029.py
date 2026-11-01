#!/usr/bin/env python3
"""Exact p-local, original-coefficient verification of reflected convolution endpoints.

An author-side finite check, not a native H0/B0 execution or an all-prime proof.
"""
from math import comb


def primes_below(n):
    sieve = bytearray(b'\x01') * n
    sieve[:2] = b'\x00\x00'
    for d in range(2, int(n ** 0.5) + 1):
        if sieve[d]:
            sieve[d*d:n:d] = b'\x00' * (((n-1-d*d)//d)+1)
    return [p for p in range(5, n) if sieve[p]]


def units_and_valuations(p):
    mod = p**3
    upper = 4 * (p-1)
    units = [1] * (upper+1)
    valuations = [0] * (upper+1)
    for k in range(1, upper+1):
        t, v = k, 0
        while t % p == 0:
            t //= p
            v += 1
        units[k] = units[k-1] * t % mod
        valuations[k] = valuations[k-1] + v
    return units, valuations


def original_streams(p):
    mod = p**3
    uf, vf = units_and_valuations(p)
    a, b = [], []
    inv216 = pow(216, -1, mod)
    inv2304 = pow(2304, -1, mod)
    pa, pb = 1, 1
    for n in range(p):
        ia = pow(uf[n], -1, mod)
        va = vf[2*n] + vf[3*n] - 5*vf[n]
        vb = vf[4*n] - 4*vf[n]
        av = (pow(p, va, mod)*uf[2*n]*uf[3*n]*pow(ia, 5, mod)*pa) % mod
        bv = (pow(p, vb, mod)*uf[4*n]*pow(ia, 4, mod)*pb) % mod
        a.append((av, va))
        b.append((bv, vb))
        pa = (pa * inv216) % mod
        pb = (pb * inv2304) % mod
    return a, b


def raw_a(n, mod):
    return (comb(2*n, n)**2 * comb(3*n, n) * pow(216, -n, mod)) % mod


def raw_b(n, mod):
    return (comb(2*n, n)**2 * comb(4*n, 2*n) * pow(2304, -n, mod)) % mod


def check(p, raw=False):
    mod, p2 = p**3, p**2
    a, b = original_streams(p)
    m = (p-1)//2
    la, ua = (p-1)//3, p-1-(p-1)//3
    lb, ub = (p-1)//4, p-1-(p-1)//4
    va = [(2*n)//p + (3*n)//p for n in range(p)]
    vb = [(4*n)//p for n in range(p)]
    assert [v for _, v in a] == va
    assert [v for _, v in b] == vb
    for n in range(p):
        mirror = p-1-n
        assert va[n]+va[mirror] == 3 - (n in (la,m,ua))
        assert vb[n]+vb[mirror] == 3 - (n in (lb,m,ub))
    assert (a[m][0]//p)**2 % p == 4 % p
    assert (a[la][0]*a[ua][0]//p2) % p == 3 % p
    assert (b[m][0]//p)**2 % p == 1 % p
    assert (b[lb][0]*b[ub][0]//p2) % p == 1 % p
    ca = sum(a[n][0]*a[p-1-n][0] for n in range(p)) % mod
    cb = sum(b[n][0]*b[p-1-n][0] for n in range(p)) % mod
    wa = sum((6*n+1)*a[n][0]*a[p-1-n][0] for n in range(p)) % mod
    wb = sum((8*n+1)*b[n][0]*b[p-1-n][0] for n in range(p)) % mod
    assert ca == (10*p2)%mod and cb == (3*p2)%mod
    assert wa == (-20*p2)%mod and wb == (-9*p2)%mod
    assert (ca-2*cb)%mod == (4*p2)%mod
    assert (wa-2*wb)%mod == (-2*p2)%mod
    assert wa == ((3*p-2)*ca)%mod and wb == ((4*p-3)*cb)%mod
    if raw:
        for n in range(p):
            assert a[n][0] == raw_a(n,mod)
            assert b[n][0] == raw_b(n,mod)
    return (p,ca,cb,wa,wb)


def main():
    ps = primes_below(1500)
    for p in ps:
        check(p,raw=p in (5,7,11,13,19,31,373))
    for p in (5,7,11,13,19,31,373):
        print('certificate',check(p))
    print('PASS_EXACT_REFLECTED_CONVOLUTION',len(ps),
          'primes below 1500; complete per-index valuation and convolution;',
          'independent raw binomial 5 7 11 13 19 31 373')


if __name__=='__main__':
    main()
