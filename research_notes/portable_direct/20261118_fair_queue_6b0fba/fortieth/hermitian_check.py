#!/usr/bin/env python3
"""Gaussian-primitive fibres for diag(1,1,1,-1,-1,-3); stdlib, deterministic."""
from collections import Counter
from fractions import Fraction as F
from math import isqrt
import json

COEFFICIENTS = (1, 1, 1, -1, -1, -3)


def local_factor(p, k, t):
    u = F(1, p)
    if p == 2:
        if k == 1:
            return 1 - (t % 2 == 0) * F(1, 32)
        return 1 - (t % 4 == 0) * F(1, 16)
    if p == 3:
        if t % 3:
            return 1 + u**5
        smooth = (1 - u**4) * (1 + u**5)
        if k == 1:
            return smooth + 8 * u**11
        return smooth + (t % 9 != 0) * 4 * u**10
    chi = 1 if p % 4 == 1 else -1
    return (1 - u**6) * (1 - (t % p == 0) * chi * u**5)


def direct_residue_counts(p, k):
    """Convolve actual Gaussian coordinates, marking the primes where they are units."""
    m = p**k
    split = p % 4 == 1
    root = next((r for r in range(p) if (r*r + 1) % p == 0), None) if split else None
    gaussian = Counter()
    for x in range(m):
        for y in range(m):
            if p == 2:
                mask = 3 if (x+y) % 2 else 0
            elif split:
                mask = int((x+root*y) % p != 0) + 2 * int((x-root*y) % p != 0)
            else:
                mask = 3 if x % p or y % p else 0
            gaussian[(x*x+y*y) % m, mask] += 1
    tally = {(0, 0): 1}
    for c in COEFFICIENTS:
        combined = Counter()
        for (a, previous), n in tally.items():
            for (b, new), count in gaussian.items():
                combined[(a+c*b) % m, previous | new] += n * count
        tally = combined
    assert sum(tally.values()) == m**12
    return [tally[t, 3] for t in range(m)]


def split_primitive_example():
    # Modulo 5, i -> (2,-2); Q(x)=N(3+4i)-N(3-4i)=0.
    z = [(3,4),(0,0),(0,0),(3,-4),(0,0),(0,0)]
    projected = [[(a + sign*2*b) % 5 for a,b in z] for sign in (1,-1)]
    assert all(any(v) for v in projected)
    assert not any(a*b % 5 for a,b in zip(*projected))
    assert sum(c*(a*a+b*b) for c,(a,b) in zip(COEFFICIENTS,z)) == 0
    return projected


def local_tests():
    rows = []
    for p, max_k in [(2,6),(3,4),(5,3),(7,2),(11,2),(13,2),(17,1),(19,1),(23,1),(29,1)]:
        for k in range(1,max_k+1):
            m = p**k
            counts = direct_residue_counts(p, k)
            for t, value in enumerate(counts):
                assert F(value,m**11) == local_factor(p,k,t), (p,k,t)
            primitive_space = (1-F(1,2**6) if p == 2 else
                               (1-F(1,p**6))**2 if p % 4 == 1 else 1-F(1,p**12))
            assert F(sum(counts), m**12) == primitive_space
            distribution = Counter(str(F(n,m**11)) for n in counts)
            rows.append(dict(p=p, k=k, all_targets_checked=m, zero_count=counts[0],
                             normalized_value_multiplicities=dict(sorted(distribution.items()))))
    return rows


def positive_convolution(left, right):
    out = [0] * len(left)
    for i, a in enumerate(left):
        if a:
            for j in range(len(left)-i):
                out[i+j] += a * right[j]
    return out


def global_shells(heights):
    """Direct definite theta coefficients, then ideal Möbius across exact energy shells."""
    bound = max(heights)**2 // 2
    r = [0] * (bound+1)
    lo = isqrt(bound)
    for x in range(-lo,lo+1):
        for y in range(-isqrt(bound-x*x),isqrt(bound-x*x)+1):
            r[x*x+y*y] += 1
    two = positive_convolution(r,r)
    pos = positive_convolution(two,r)
    r3 = [r[n//3] if n % 3 == 0 else 0 for n in range(bound+1)]
    neg = positive_convolution(two,r3)
    # PID: each nonzero principal ideal has four generators, of the same norm.
    ideals = [0] + [v//4 for v in r[1:]]
    assert ideals[1] == 1 and all(v % 4 == 0 for v in r[1:])
    all_shell = [0] + [pos[n]*neg[n] for n in range(1,bound+1)]
    primitive = all_shell.copy()
    for n in range(1,bound+1):
        assert primitive[n] >= 0 and primitive[n] % 4 == 0
        for d in range(2,bound//n+1):
            primitive[d*n] -= ideals[d] * primitive[n]
    assert all(sum(ideals[d]*primitive[n//d] for d in range(1,n+1) if n%d==0)
               == all_shell[n] for n in range(1,65))
    assert all_shell[1] == primitive[1] == 96
    assert all_shell[2] == 1440 and primitive[2] == 1344
    return [dict(B=b, nonzero_all=sum(all_shell[:b*b//2+1]),
                 gaussian_primitive=sum(primitive[:b*b//2+1]),
                 primitive_over_B10=str(F(sum(primitive[:b*b//2+1]), b**10)))
            for b in heights]


def main():
    correction = F(15,16) / (1-F(1,2**6)) * (1-F(1,3**4)) / (1-F(1,3**6))
    local_multiple = correction * 945 * F(1536,5)
    global_multiple = local_multiple / 1920
    assert (correction,local_multiple,global_multiple) == (F(600,637),F(24883200,91),F(12960,91))
    rows = local_tests()
    shells = global_shells([2,4,8,16,32,48,64,128])
    assert (shells[-1]["nonzero_all"], shells[-1]["gaussian_primitive"]) == (
        567684605080372664832, 549573120779023765920)
    data = dict(coefficients=COEFFICIENTS,
                tested_prime_powers=len(rows),
                tested_fibres=sum(r['all_targets_checked'] for r in rows),
                prime_power_checks=rows,
                split_example_components_mod_5=split_primitive_example(),
                zero_euler_correction=str(correction),
                zero_local_multiple_of_pi_to_minus_11=str(local_multiple),
                global_multiple_of_pi_to_minus_5=str(global_multiple),
                global_integer_counts=shells)
    print(json.dumps(data,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
