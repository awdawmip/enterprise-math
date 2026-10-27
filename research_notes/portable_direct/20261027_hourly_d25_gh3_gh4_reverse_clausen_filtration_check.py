#!/usr/bin/env python3
"""Author-side exact finite-field checks for GH-3/GH-4.
No native X6, H0/B0, formal proof, or independent review is performed.
"""
from math import isqrt


def primes_below(bound):
    sieve = bytearray(b'\x01') * bound
    sieve[:2] = b'\x00\x00'
    for j in range(2, isqrt(bound - 1) + 1):
        if sieve[j]:
            sieve[j * j:bound:j] = b'\x00' * ((bound - 1 - j * j) // j + 1)
    return [p for p in range(5, bound) if sieve[p]]


def inverses(p, maximum):
    inv = [0] * (maximum + 1)
    inv[1] = 1
    for j in range(2, maximum + 1):
        inv[j] = -(p // j) * inv[p % j] % p
    return inv


def t_scalar(p, inv):
    d = (p - 1) // 4
    h = 1
    total = 1
    for j in range(d):
        h = (h * 9 * (4 * j + 1) ** 3 * inv[4] * inv[4*j+2]
             * inv[4*j+3] * inv[j+1]) % p
        total = (total + (8 * (j+1) + 1) * h) % p
    return total


def gh3_port(p, inv):
    assert p % 24 == 19
    a, b, h = (p - 3) // 8, (3*p - 1) // 8, (p - 1) // 2
    d = b - a - 1
    unit = 1
    beta = []
    inv576 = inv[576] if p > 576 else pow(576, -1, p)
    for k in range(b):
        numerator = (8*k + 1) * (8*k + 3)
        while numerator % p == 0:
            numerator //= p
        unit = (unit * numerator * inv576 * inv[k+1] ** 2) % p
        if k + 1 > a:
            beta.append(unit)
    assert len(beta) == d + 1 and beta[-1] != 0
    suffix0 = [0] * (d + 2)
    suffix1 = [0] * (d + 2)
    for r in range(d, -1, -1):
        suffix0[r] = (suffix0[r+1] + beta[r]) % p
        suffix1[r] = (suffix1[r+1] + (a+1+r)*beta[r]) % p
    port = 0
    for r, value in enumerate(beta):
        i = a + 1 + r
        start = h + 1 - i - (a + 1)
        assert 0 <= start <= d
        port += value * ((8*i+1)*suffix0[start] + 8*suffix1[start])
    port %= p
    t = t_scalar(p, inv)
    assert port == (-beta[-1]**2 * t) % p
    if p < 2000:
        # Independent direct labelled middle-middle convolution.
        direct = sum((8*(i+j)+1)*beta[i-a-1]*beta[j-a-1]
                     for i in range(a+1,b+1) for j in range(a+1,b+1)
                     if i+j > h) % p
        assert direct == port
        invbeta = pow(beta[-1], -1, p)
        g = [beta[d-r]*invbeta % p for r in range(d+1)]
        for r in range(d):
            assert g[r+1] == (g[r]*9*(8*r+1)**2
                              *pow(16*(r+1)*(4*r+3), -1, p)) % p
        coeff = 1
        for r in range(d+1):
            assert sum(g[s]*g[r-s] for s in range(r+1)) % p == coeff
            if r < d:
                coeff = (coeff*9*(4*r+1)**3
                         *pow(4*(4*r+2)*(4*r+3)*(r+1),-1,p)) % p
    return port, t, beta[-1]


def v_step(k, p, side):
    n = (8*k+1)*(8*k+3) if side == 'S' else (6*k+1)*(3*k+1)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def gh4_filtration(p):
    assert p % 24 in (13,19)
    m = (p-1)//6
    if p % 24 == 19:
        a, b = (p-3)//8, (3*p-1)//8
        def predicted(k):
            return (0 if k <= a else 1 if k <= m else 0
                    if k <= 2*m else -1 if k <= b else 0)
    else:
        a, b = (5*p-1)//8, (7*p-3)//8
        def predicted(k):
            return (0 if k <= m else -1 if k <= 2*m else -2
                    if k <= a else -1 if k <= b else 0)
    vs = vw = plus = minus = 0
    for k in range(p):
        if k:
            vs += v_step(k-1, p, 'S')
            vw += v_step(k-1, p, 'W')
        delta = vs - vw
        assert delta == predicted(k), (p, k, delta)
        plus += max(delta, 0)
        minus += max(-delta, 0)
    if p % 24 == 19:
        assert plus == minus == (p+5)//24
    else:
        assert plus == 0 and minus == p
    return plus, minus


def main():
    prime_set = primes_below(10000)
    q19 = [p for p in prime_set if p % 24 == 19]
    for p in q19:
        inv = inverses(p, p - 1)
        port, t, unit = gh3_port(p, inv)
        assert port == t == 0, (p, port, t)
    print('PASS GH3 p≡19 (mod24) primes<10000:', len(q19))
    all_20k = [p for p in prime_set if p < 20000]
    for p in all_20k:
        inv = inverses(p, p - 1)
        assert t_scalar(p, inv) == 0, p
    print('OBSERVATION T_p=0 for all primes 5<=p<10000:', len(all_20k))
    classes = {13:0,19:0}
    for p in prime_set:
        if p < 10000 and p % 24 in classes:
            gh4_filtration(p)
            classes[p % 24] += 1
    print('PASS GH4 valuation profiles p<10000:', classes)
    for p in (13,19,43,67,139,181,373):
        if p % 24 in classes:
            print('CERT', p, gh4_filtration(p))


if __name__ == '__main__':
    main()
