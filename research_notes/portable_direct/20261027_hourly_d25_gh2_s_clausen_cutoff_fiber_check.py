#!/usr/bin/env python3
"""GH-2 exact author checker: S Clausen cutoff conservation and W/S Gauss
valuation incompatibility; arithmetic ranks are not native X6 axes.
No native Hasse, H0/B0, Frobenius or independent review is performed.
"""
from math import isqrt

def primes(bound=2000):
    return [p for p in range(13, bound) if p % 24 in (13, 19)
            and all(p % q for q in range(2, isqrt(p) + 1))]

def gaussian(p, side):
    vals, units = [0] * p, [1] * p
    for k in range(p - 1):
        if side == 'S':
            num, den = (8*k + 1)*(8*k + 3), 576*(k+1)**2
        else:
            num, den = (6*k + 1)*(3*k + 1), 36*(k+1)**2
        extra = 0
        while num % p == 0:
            num //= p
            extra += 1
        vals[k+1] = vals[k] + extra
        units[k+1] = units[k]*num*pow(den, -1, p) % p
    return vals, units

def check(p):
    m = (p-1)//6
    wv, wu = gaussian(p, 'W')
    sv, su = gaussian(p, 'S')
    assert all(wv[k] == (0 if k <= m else 1 if k <= 2*m else 2)
               for k in range(p))
    if p % 24 == 13:
        a = (5*p-1)//8
        b = (7*p-3)//8
        assert all(sv[k] == (0 if k <= a else 1 if k <= b else 2)
                   for k in range(p))
        i = m+1
        assert i <= a and (wv[i], sv[i]) == (1,0)
        return (p, '13-class', i, wv[i], sv[i], None)
    a, b, h, H = (p-3)//8, (3*p-1)//8, (p-1)//2, (3*p-1)//4
    assert a+b == h and 2*b == H
    assert all(sv[k] == (0 if k <= a else 1 if k <= b else 2)
               for k in range(p))
    i = a+1
    assert i <= m and (wv[i], sv[i]) == (0,1)
    A = sum(su[:a+1]) % p
    J = sum(j*su[j] for j in range(a+1)) % p
    C = sum(su[b+1:]) % p
    C1 = sum(k*su[k] for k in range(b+1,p)) % p
    cutoff = sum((8*(j+k)+1)*su[j]*su[k]
                 for j in range(a+1) for k in range(b+1,p)
                 if j+k >= p) % p
    port_mm = port_lh = port_lh_low = 0
    p3, c, high_sum = p**3, 1, 0
    for n in range(p):
        if n > h:
            high_sum = (high_sum + (8*n+1)*c) % p3
        if h < n < p:
            M = sum(su[j]*su[n-j] for j in range(a+1,b+1)
                    if a < n-j <= b) % p
            B = sum(su[j]*su[n-j] for j in range(a+1)
                    if b < n-j < p) % p
            if n <= H:
                assert ((8*n+1)*c) % (p*p) == 0
                assert ((8*n+1)*(M+2*B) - ((8*n+1)*c//(p*p))) % p == 0
                port_mm = (port_mm+(8*n+1)*M) % p
                port_lh = (port_lh+2*(8*n+1)*B) % p
            else:
                assert M == B == 0
                assert su[n] == -sum(su[j]*su[n-j] for j in range(1,a+1)) % p
        elif b < n <= h:
            B = sum(su[j]*su[n-j] for j in range(a+1)
                    if b < n-j < p) % p
            port_lh_low = (port_lh_low+2*(8*n+1)*B) % p
        if n < p-1:
            num = (4*n+1)*(4*n+2)*(4*n+3)*(4*n+4)
            den = 2304*(n+1)**4
            c = c*num*pow(den, -1, p3) % p3
    rectangular = 2*(A*C+8*(J*C+A*C1)-cutoff) % p
    assert high_sum == 0
    assert (port_mm+port_lh) % p == 0
    assert rectangular == (port_lh_low+port_lh) % p
    assert (port_mm+rectangular-port_lh_low) % p == 0
    return (p, '19-class', i, wv[i], sv[i],
            (port_mm,port_lh,port_lh_low,cutoff,rectangular))

def main():
    checks = [check(p) for p in primes()]
    for row in checks:
        if row[0] in (13,19,37,43,67,139,181,199,277,373):
            print('CERT', row)
    nineteen = [r for r in checks if r[1] == '19-class']
    print('PASS GH2', 'primes', len(checks), '19-class',len(nineteen),
          '13-class',len(checks)-len(nineteen),
          '19-class-both-ports-zero-observed',
          sum(r[5][0] == r[5][1] == 0 for r in nineteen))

if __name__ == '__main__':
    main()
