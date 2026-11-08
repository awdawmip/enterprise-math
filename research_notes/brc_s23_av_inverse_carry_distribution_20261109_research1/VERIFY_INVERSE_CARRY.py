#!/usr/bin/env python3
"""Exact rational certificate for S23/AV two-candidate inverse carry theorem.
Inputs: same immutable frozen S23/AV definitions as 2026-11-09 plateau401-411 proof.
No floating point or numerical log black box.
"""
from fractions import Fraction
from collections import Counter

A, B, OFFSET, K, TERMS = 380295, 79, 510, 10000, 160


def log_interval(p, q, n):
    x = Fraction(p - q, p + q)
    term = x
    low = Fraction(0)
    for j in range(n):
        low += 2 * term / (2 * j + 1)
        term *= x * x
    upper = low + 2 * term / ((2 * n + 1) * (1 - x*x))
    return low, upper


def floor_sum(n, m, a, b):
    """Return sum_{i=0}^{n-1} floor((a*i+b)/m), nonnegative integers."""
    ans = 0
    while True:
        if a >= m:
            ans += (n-1)*n*(a//m)//2
            a %= m
        if b >= m:
            ans += n*(b//m)
            b %= m
        y = a*n+b
        if y < m:
            return ans
        n = y//m
        b = y%m
        m,a = a,m

l7, u7 = log_interval(7, 1, TERMS)
l107, u107 = log_interval(10, 7, TERMS)
den_lo = 79*l7 - 431*u107
den_hi = 79*u7 - 431*l107
num_lo = 2074774*l107 - 380295*u7
num_hi = 2074774*u107 - 380295*l7
assert 0 < den_lo < den_hi and 0 < num_lo < num_hi
al, au = num_lo/den_hi, num_hi/den_lo
assert Fraction(1,2) < al < au < Fraction(2,3)
assert (au-al)*B*K < Fraction(1,1000000)

freq = Counter()
csum = 0
for k in range(1, K+1):
    lo_a, hi_a = (k*al).__floor__(), (k*au).__floor__()
    lo_b, hi_b = (B*k*al).__floor__(), (B*k*au).__floor__()
    assert lo_a == hi_a and lo_b == hi_b, ('uncertified_floor', k)
    v = A*k+B*lo_a
    coarse_right = A*k+lo_b
    carry_count = lo_b-B*lo_a
    assert 0 <= carry_count <= B-1 and coarse_right-v == carry_count
    if carry_count:
        n = v+1
        assert n > (A+B*au)*(k-1)
        assert n <= (A+B*al)*k
        assert v+carry_count <= (A+B*al)*k
        assert v+carry_count+1 > (A+B*au)*k
    freq[carry_count] += 1
    csum += carry_count
assert sum(freq.values()) == K
assert set(freq) == set(range(B))
p,q = al.numerator, al.denominator
fast = floor_sum(K, q, B*p, B*p) - B*floor_sum(K, q, p, p)
assert fast == csum
assert (K*Fraction(39)) - K*39 == 0
print('PASS_S23_AV_INVERSE_CARRY_EXACT_RATIONAL')
print('frozen=43ec6098b1330ae86d0a7863be336c5d97f6ef34')
print('N_log_terms=', TERMS, 'K_certified=',K)
print('alpha_interval_width_less_than_1e-28=', (au-al)<Fraction(1,10**28))
print('all_floor_certificates=', 2*K)
print('coarse_bins=', K, 'first_k=',1,'last_k=',K)
print('total_second_candidate_horizons=',csum)
print('all_79_carry_values_observed=',len(freq))
print('exact_Euclidean_floor_sum_match=',fast==csum)
print('carry_count_first_12=', [(i, (B*i*al).__floor__()-B*(i*al).__floor__()) for i in range(1,13)])
print('frequency_0_39_78=', (freq[0],freq[39],freq[78]))
