#!/usr/bin/env python3
"""Exact Farey-epoch near-rational stress example, Python standard library only.
No enumerating step is used for N=10**11.
"""
from fractions import Fraction as F
from math import isqrt

M = 128
# Exact irrational theta = 1/2 + sqrt(2)/10^12, rigorously enclosed.
K = isqrt(2 * 10**60)
assert K * K < 2 * 10**60 < (K + 1) ** 2
LO = F(1, 2) + F(K, 10**42)
HI = F(1, 2) + F(K + 1, 10**42)

def farey_neighbours(x, cap):
    p, q = x.numerator, x.denominator
    a, b, c, d = 0, 1, 1, 1
    while b + d <= cap:
        z = (a + c) * q - (b + d) * p
        if z < 0:
            step = min((cap - b) // d, (p*b - q*a - 1) // (q*c - p*d))
            assert step > 0
            a += step * c
            b += step * d
        elif z > 0:
            step = min((cap - d) // b, (q*c - p*d - 1) // (p*b - q*a))
            assert step > 0
            c += step * a
            d += step * b
        else:
            raise AssertionError('endpoint equals Farey mediant')
    assert b*c - a*d == 1 and a*q < b*p and p*d < q*c
    return (a, b, c, d)

def expected_epoch_count(m, n):
    q0 = m - 1 if (m - 1) % 2 else m - 2
    q1 = n - 1 if (n - 1) % 2 else n - 2
    return 1 + (q1 - q0) // 2

def verify_one(n, m=M):
    q = n - 1 if (n - 1) % 2 else n - 2
    target = (1, 2, (q+1)//2, q)
    assert farey_neighbours(LO, n-1) == farey_neighbours(HI, n-1) == target
    return target

def run(n):
    # Enclosure alone certifies theta-1/2 < 1/(2n).
    assert F(0) < LO - F(1, 2) < HI - F(1, 2) < F(1, 2*n)
    for j in [M, M+1, M+2, (M+n)//2, n-2, n-1, n]:
        if j >= M:
            verify_one(j)
    expected = expected_epoch_count(M, n)
    if n <= 100000:
        point = M
        total = 0
        while point <= n:
            a,b,c,d = verify_one(point)
            stop = min(n, b+d)
            assert verify_one(stop) == (a,b,c,d)
            total += 1
            point = stop + 1
        assert total == expected
        print('COMPLETE_EPOCH_ENUMERATION_CERTIFIED',n,total)
    else:
        print('SYMBOLIC_EPOCH_COUNT_CERTIFIED',n,expected)
    assert expected == 1 + ((n-1 if (n-1)%2 else n-2) - 127)//2
    return expected

if __name__ == '__main__':
    for N in (1000, 20000, 100000, 100000000000):
        run(N)
    print('PASS_NEAR_RATIONAL_LINEAR_FAREY_EPOCH_FAMILY')
