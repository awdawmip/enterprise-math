#!/usr/bin/env python3
"""PREFIX-894: exact finite 19-bit collision coverage by reversal and LCM.

Python 3 standard library; no network and no floating-point counting.
Recomputes all reported counts using two complementary arithmetic methods.
"""
import json
from math import gcd
A, B, N = 262145, 524287, 1 << 32
S = (262147, 280001, 300001, 320003, 340007, 360007, 380003,
     400009, 420001, 440003, 460001, 480007, 500383, 510007,
     520001, 524285)
SIZE = (B - A) // 2 + 1

def odd_count(lo, hi):
    return 0 if hi < lo else (hi + 1) // 2 - lo // 2

def distinct_prime_factors(n):
    f, p = [], 3
    while p * p <= n:
        if n % p == 0:
            f.append(p)
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        f.append(n)
    return f

def odd_coprime_count(a, low, high):
    # Inclusion/exclusion over squarefree divisors of a. a must be odd.
    if high < low:
        return 0
    factors = distinct_prime_factors(a)
    ans = 0
    for mask in range(1 << len(factors)):
        d = 1
        sign = 1
        for i, prime in enumerate(factors):
            if mask & (1 << i):
                d *= prime
                sign *= -1
        left = (low + d - 1) // d
        right = high // d
        ans += sign * odd_count(left, right)
    return ans

def low_gcd_zz(g):
    low, high = (A + g - 1) // g, B // g
    if low % 2 == 0:
        low += 1
    result = 0
    for a in range(low, high + 1, 2):
        b_upper = min(high, (N - 1) // (g * a))
        result += odd_coprime_count(a, low, b_upper)
    return result

def high_gcd_zz_and_partition():
    # Descending exact-gcd counts E[g]. Integer Python lists avoid overflow.
    e = [0] * (B + 1)
    high_total = 0
    for g in range(B, 0, -2):
        m = odd_count((A + g - 1) // g, B // g)
        exact = m * m
        for multiple in range(3 * g, B + 1, 2 * g):
            exact -= e[multiple]
        assert exact >= 0
        e[g] = exact
        if g >= 65:
            high_total += exact
    assert sum(e[1::2]) == SIZE * SIZE
    return high_total

def zz(q1, q2):
    return (q1 // gcd(q1, q2)) * q2 < N

def selftest():
    for a in range(1, 160, 2):
        for low, high in ((1, 75), (17, 151), (65, 65)):
            expected = sum(gcd(a, b) == 1 for b in range(low, high + 1) if b & 1)
            assert odd_coprime_count(a, low, high) == expected
    # A finite direct check of the elementary ZZ witness criterion.
    for n in (4, 8, 16, 32, 64):
        for q1 in (3, 5, 7, 9, 11):
            for q2 in (3, 5, 7, 9, 11):
                brute = len({(x % q1, x % q2) for x in range(n)}) < n
                assert brute == (q1 // gcd(q1, q2)) * q2 < n
    assert len(S) == len(set(S)) == 16
    assert all(A <= s <= B and s % 2 for s in S)

def main():
    selftest()
    small = {str(g): low_gcd_zz(g) for g in range(17, 65, 2)}
    small_total = sum(small.values())
    high_total = high_gcd_zz_and_partition()
    full_zz = small_total + high_total
    one = sum(zz(s, q) for s in S for q in range(A, B + 1, 2))
    double = sum(zz(s, t) for s in S for t in S)
    zz_outside_s = full_zz - (2 * one - double)
    panel_union = 2 * len(S) * SIZE - len(S) ** 2
    combined = panel_union + zz_outside_s
    answer = dict(schema="PREFIX894_R6_LCM_REVERSE_RESULTS_V1",
                  frozen_scientific_pin="f42f2906d77f24085c123f3ccfe9667d41caa96d",
                  p=32, N=N, q_bounds=[A,B], q_count=SIZE,
                  first_port_source_rows=list(S),
                  first_port_panel=16*SIZE,
                  two_sided_panel=panel_union,
                  low_gcd_exact_counts=small,
                  low_gcd_zz_total=small_total,
                  high_gcd_zz_total=high_total,
                  full_zz_positive=full_zz,
                  source_rows_zz_count=one,
                  source_rows_overlap_zz_count=double,
                  zz_outside_source_rows=zz_outside_s,
                  proven_collision_positive_union=combined,
                  total_ordered_pairs=SIZE*SIZE,
                  unexcluded_by_this_union=SIZE*SIZE-combined,
                  verification="exact integer finite enumeration plus explicit time-reversal and ZZ proofs")
    assert (small_total, high_total, full_zz) == (100280938,108769846,209050784)
    assert (one, double, zz_outside_s) == (15250,22,209020306)
    assert (panel_union, combined) == (4194048,213214354)
    print(json.dumps(answer, indent=2, ensure_ascii=False))
if __name__ == "__main__":
    main()
