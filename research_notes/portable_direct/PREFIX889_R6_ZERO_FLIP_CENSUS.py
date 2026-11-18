#!/usr/bin/env python3
"""PREFIX-889 exact zero-step vs one-named-XOR-flip collision census.

Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d
Only integer arithmetic; no external dependencies.
"""
import json
from collections import defaultdict
from math import gcd

PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'


def ones_before(t, i):
    """Number of x in [0,t) whose bit i is 1."""
    half = 1 << i
    period = half << 1
    return (t // period) * half + max(0, t % period - half)


def zero_flip_count(p, q1, q2):
    """Exact number of unordered pairs (zero transition, named XOR flip)
    with the same ordered (start mod q1, end mod q2) observation.
    Here q1,q2 are odd integers >1. Arbitrary positive p is supported.
    """
    assert p >= 1 and q1 > 1 and q2 > 1 and q1 % 2 and q2 % 2
    if gcd(q1, q2) != 1:
        return 0
    n = 1 << p
    K = (n-1) // q1
    if K == 0:
        return 0
    inv = pow(q1, -1, q2)
    r = inv
    count_positive = 0
    for i in range(p):
        # Positive k with k*q1 - 2^i == 0 (mod q2): bit i of x' is 1.
        k = r
        while k <= K:
            a = k*q1
            count_positive += n // 2 - ones_before(a, i)
            k += q2
        # Positive k with k*q1 + 2^i == 0 (mod q2): bit i of x' is 0.
        k = q2-r
        while k <= K:
            a = k*q1
            count_positive += (n-a) - (n//2 - ones_before(a, i))
            k += q2
        r = (r * 2) % q2
    # Bitwise complementation pairs every k>0 witness with a k<0 witness.
    return 2*count_positive


def direct_bruteforce(p, q1, q2):
    n = 1 << p
    counts = defaultdict(lambda: [0, 0])
    for x in range(n):
        counts[(x % q1, x % q2)][0] += 1
        for i in range(p):
            counts[(x % q1, (x ^ (1 << i)) % q2)][1] += 1
    return sum(z*f for z, f in counts.values())


def check_small():
    pairs = 0
    for p in range(1, 9):
        for q1 in range(3, min((1 << p) + 5, 16), 2):
            for q2 in range(3, min((1 << p) + 5, 16), 2):
                a = zero_flip_count(p, q1, q2)
                b = direct_bruteforce(p, q1, q2)
                assert a == b, (p, q1, q2, a, b)
                assert a == zero_flip_count(p, q2, q1)
                assert a % 2 == 0
                pairs += 1
    medium_cases = [(10,257,259),(10,511,521),(11,521,1023),
                    (12,521,539),(12,1023,1025),(13,2049,2051),
                    (13,4095,4097),(14,521,615),(15,32767,32765)]
    for p,q1,q2 in medium_cases:
        assert zero_flip_count(p,q1,q2) == direct_bruteforce(p,q1,q2)
    return pairs, len(medium_cases)


def scan_slice(p, q1, lo, hi):
    assert lo % 2 and hi % 2 and lo <= hi
    out = dict(q1=q1, q2_lower_odd=lo, q2_upper_odd=hi,
               ordered_pairs=(hi-lo)//2+1, coprime_pairs=0,
               non_coprime_pairs=0, positive_zero_flip_pairs=0,
               sum_zero_flip_collision_pairs=0,
               max_zero_flip_collision_pairs=0, maximizers=[], examples={})
    for q2 in range(lo, hi+1, 2):
        g = gcd(q1, q2)
        out['coprime_pairs' if g == 1 else 'non_coprime_pairs'] += 1
        value = zero_flip_count(p, q1, q2)
        if value:
            out['positive_zero_flip_pairs'] += 1
        out['sum_zero_flip_collision_pairs'] += value
        if value > out['max_zero_flip_collision_pairs']:
            out['max_zero_flip_collision_pairs'] = value
            out['maximizers'] = [q2]
        elif value == out['max_zero_flip_collision_pairs']:
            out['maximizers'].append(q2)
        if q2 in {lo, hi, q1, 500383, 523001, 524285}:
            out['examples'][str(q2)] = value
    return out


def main():
    checked, medium_checked = check_small()
    p=32
    slices=[scan_slice(p, q1, 262145, 524287) for q1 in (262145, 500383, 524287)]
    totals = {'pairs':sum(x['ordered_pairs'] for x in slices),
              'coprime_pairs':sum(x['coprime_pairs'] for x in slices),
              'non_coprime_pairs':sum(x['non_coprime_pairs'] for x in slices),
              'positive_zero_flip_pairs':sum(x['positive_zero_flip_pairs'] for x in slices),
              'sum_zero_flip_collision_pairs':sum(x['sum_zero_flip_collision_pairs'] for x in slices)}
    result = {'schema':'PREFIX889_R6_ZERO_FLIP_CENSUS_V1',
              'frozen_scientific_pin':PIN, 'p':p,
              'q2_domain':'all odd q2 in [262145,524287]',
              'slices':slices,'totals':totals,
              'validation':{'small_full_brute_parameter_triples':checked,
                            'medium_full_brute_parameter_triples':medium_checked,
                            'small_full_brute_disagreements':0,
                            'reversal_symmetry_disagreements':0,
                            'arithmetic':'exact integers; no external dependencies'},
              'classification':'AUTHOR_PROVED / FINITE_EXACT_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED'}
    print(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True))

if __name__=='__main__':
    main()
