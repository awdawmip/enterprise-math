#!/usr/bin/env python3
"""Exact source-count certificate for R749SQP (independent auxiliary Walsh fiber)."""
import json
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import comb, factorial, gcd

A = (1, 1, 1, 2, 7, 11, 15)
B = (1, 1, 1, 3, 5, 13, 14)
MAX_R = 12000


def conv(a, b, order):
    out = [F(0)] * (order + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= order:
                out[i + j] += x * y
    return out


def reciprocal_factor(s, order):
    """Series of s*w/[1-(1-w)**s], with w=1-z."""
    q = [F((-1)**j * comb(s, j+1), s) if j+1 <= s else F(0)
         for j in range(order+1)]
    assert q[0] == 1
    v = [F(1)]
    for k in range(1, order+1):
        v.append(-sum(q[j] * v[k-j] for j in range(1, k+1)))
    return v


def polynomial_product(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def rising_polynomial(k, divide_by_r=False):
    # [z^r](1-z)^(-k) = r(r+1)...(r+k-1)/k!, k>=1.
    a = [F(1)]
    for j in range(k):
        a = polynomial_product(a, (F(j), F(1)))
    a = [v/factorial(k) for v in a]
    if divide_by_r:
        assert a[0] == 0
        a = a[1:]
    return a


def smooth_mean_coefficients(weights, order=6, marked=0):
    d, h = len(weights), weights[marked]
    assert d >= order
    f = [F(1)] + [F(0)]*order
    for s in weights:
        f = conv(f, reciprocal_factor(s, order), order)
    z_to_h = [F((-1)**j * comb(h, j)) if j <= h else F(0)
              for j in range(order+1)]
    factor_marked = conv(reciprocal_factor(h, order), z_to_h, order)
    b = conv(f, factor_marked, order)
    count, moment = [F(0)]*(d+1), [F(0)]*(d+1)
    for j in range(order+1):
        for k, v in enumerate(rising_polynomial(d-j)):
            count[k] += f[j]*v
        for k, v in enumerate(rising_polynomial(d+1-j, True)):
            moment[k] += b[j]*v
    c = [count[d-j] for j in range(order+1)]
    n = [moment[d-j] for j in range(order+1)]
    ans = []
    for k in range(order+1):
        ans.append((n[k] - sum(c[j]*ans[k-j] for j in range(1,k+1)))/c[0])
    return ans


def count_dp(weights, max_r, marked=0):
    counts = [0]*max_r
    marks = [0]*max_r
    counts[0] = 1
    for i, s in enumerate(weights):
        for j in range(s, max_r):
            counts[j] += counts[j-s]
            marks[j] += marks[j-s] + (counts[j-s] if i == marked else 0)
    C, M = [0]*(max_r+1), [0]*(max_r+1)
    for r in range(1, max_r+1):
        C[r] = C[r-1] + counts[r-1]
        M[r] = M[r-1] + marks[r-1]
    return C, M


def independent_enumeration(weights, r, marked=0):
    @lru_cache(None)
    def walk(i, remainder):
        if i == len(weights):
            return 1, 0
        C = M = 0
        for k in range(remainder//weights[i]+1):
            c, m = walk(i+1, remainder-k*weights[i])
            C += c
            M += m+(k*c if i == marked else 0)
        return C, M
    return walk(0,r-1)


def run():
    for arr in (A, B):
        assert len(arr) == 7 and arr[:3] == (1,1,1)
        assert all(gcd(x,y) == 1 for x,y in combinations(arr[3:],2))
    shared = {f'S{p}':sum(x**p for x in A) for p in (1,2,4)}
    assert all(shared[f'S{p}'] == sum(x**p for x in B) for p in (1,2,4))
    ds6 = sum(x**6 for x in A)-sum(x**6 for x in B)
    assert ds6 == 907200
    ca = smooth_mean_coefficients(A)
    cb = smooth_mean_coefficients(B)
    assert ca[:6] == cb[:6]
    assert ca[6]-cb[6] == F(-9450)
    # B_6=1/42 and (7)_5/(8*6!)=2520/(8*720).
    assert F(-1,42)*F(7*6*5*4*3,8*factorial(6))*ds6 == F(-9450)
    C1,M1 = count_dp(A,MAX_R)
    C2,M2 = count_dp(B,MAX_R)
    count_checks = enumeration_checks = 0
    for weights,C,M in ((A,C1,M1),(B,C2,M2)):
        running = 0
        for r in range(1,MAX_R+1):
            running += C[r-1]
            assert M[r] == running  # marked unit-weight source deletion identity
            count_checks += 1
        for r in range(1,33):
            assert (C[r],M[r]) == independent_enumeration(weights,r)
            enumeration_checks += 1
    samples = []
    for r in (100,200,500,1000,2000,4000,8000,12000):
        scaled = r**6*(F(M1[r],r*C1[r])-F(M2[r],r*C2[r]))
        samples.append({'r':r,'scaled_r6_difference_exact':str(scaled),
                        'scaled_r6_difference_decimal':f'{float(scaled):.9f}'})
    return {'schema':'R749SQP_EVEN_SIGNATURE_EXACT_CERT_V1','status':'PASS',
            'model':'auxiliary labeled positive weighted-source multiset; no native X6 transfer',
            'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
            'weights_A':A,'weights_B':B,'d':7,'h':1,
            'shared_sums':shared,'delta_S6':ds6,
            'smooth_mean_coefficients_A':list(map(str,ca)),
            'smooth_mean_coefficients_B':list(map(str,cb)),
            'predicted_r6_mean_difference':'-9450',
            'identity_checks':count_checks,'independent_enumeration_checks':enumeration_checks,
            'largest_integer_dp_r':MAX_R,'samples':samples,
            'limitation':'Exact finite checks and exact formal Taylor coefficients; all-r asymptotic conclusion uses root-of-unity pole argument in paper; author checked, independent review pending'}


if __name__ == '__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False))
