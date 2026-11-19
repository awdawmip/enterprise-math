#!/usr/bin/env python3
"""Exact O(log bit modulus) signed-bit cell counter for odd-core XOR collisions.

Scope: a,b odd in inclusive [L,U], source bits 0..J, source start k*a,
D=(k*a XOR 2**j)-2**i=t*b, t positive. No floating arithmetic.
No prior set files required; counts witnesses (a,i,j,t), not unique (a,b).
"""
import argparse
import json
from math import gcd


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def floor_sum(n: int, m: int, a: int, b: int) -> int:
    """Sum floor((a*x+b)/m) over 0<=x<n, all integer a,b, m>0."""
    assert n >= 0 and m > 0
    qa, a = divmod(a, m)
    qb, b = divmod(b, m)
    ans = qa * n * (n - 1) // 2 + qb * n
    while True:
        if a >= m:
            ans += n * (n - 1) // 2 * (a // m)
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m
        y_max = a * n + b
        if y_max < m:
            return ans
        n, b = divmod(y_max, m)
        m, a = a, m


def count_bit_one(n: int, m: int, a: int, b: int, threshold: int) -> int:
    """Count x in [0,n) with ((a*x+b) mod m)>=threshold."""
    return floor_sum(n, m, a, b + m - threshold) - floor_sum(n, m, a, b)


def cell_count(k: int, L: int, U: int, i: int, j: int, t: int, sign: int) -> int:
    """Exact number of valid odd a for the prescribed sign cell."""
    assert k > 0 and k % 2 and t > 0 and L % 2 and U % 2
    p = 1 << j
    C = sign * p - (1 << i)
    modulus = 2 * t  # b must be ODD, and tb = k*a+C
    g = gcd(k, modulus)
    target = t - C
    if target % g:
        return 0
    d = modulus // g
    a0 = ((target // g) * pow(k // g, -1, d)) % d
    if a0 % 2 == 0:
        return 0  # a must be odd
    lo = max(L, ceil_div(t * L - C, k))
    hi = min(U, (t * U - C) // k)
    if lo > hi:
        return 0
    h_lo = ceil_div(lo - a0, d)
    h_hi = (hi - a0) // d
    n = h_hi - h_lo + 1
    if n <= 0:
        return 0
    A = k * d
    B = k * (a0 + d * h_lo)
    one = count_bit_one(n, 2 * p, A, B, p)
    return one if sign == -1 else n - one


def census(k: int, L: int, U: int, J: int, tmax: int):
    total = 0
    by_t = []
    for t in range(1, tmax + 1):
        subtotal = sum(cell_count(k, L, U, i, j, t, sign)
                       for i in range(J + 1) for j in range(J + 1)
                       for sign in (1, -1))
        by_t.append(subtotal)
        total += subtotal
    return {"k":k,"L":L,"U":U,"max_source_bit":J,
            "t_range":[1,tmax],"raw_by_t":by_t,"raw_witnesses":total}


def direct(k, L, U, J, tmax):
    out = [0] * tmax
    for a in range(L, U + 1, 2):
        for j in range(J + 1):
            endpoint = (k*a) ^ (1 << j)
            for i in range(J + 1):
                D = endpoint - (1 << i)
                for t in range(1, tmax+1):
                    if D % t == 0 and L <= D // t <= U and (D//t)%2:
                        out[t-1] += 1
    return out


def self_test():
    for k in (1,3,5,11):
        for J in (0,1,2,4):
            # odd modulus domain includes 3..31; test bit values above all moduli.
            if k * 31 + (1<<J) >= 1 << 32:
                continue
            got = census(k, 3, 31, J, 10)["raw_by_t"]
            expected = direct(k, 3, 31, J, 10)
            assert got == expected,(k,J,got,expected)
    return "PASS: 16 exhaustive (small-domain) cases, with exact per-quotient matching"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--k',type=int,default=11)
    parser.add_argument('--min',dest='L',type=int,default=262145)
    parser.add_argument('--max',dest='U',type=int,default=524287)
    parser.add_argument('--jmax',dest='J',type=int,default=18)
    parser.add_argument('--tmax',type=int,default=22)
    args=parser.parse_args()
    check=self_test()
    print(json.dumps({"self_test":check,**census(args.k,args.L,args.U,args.J,args.tmax)},indent=2))

if __name__=='__main__':
    main()
