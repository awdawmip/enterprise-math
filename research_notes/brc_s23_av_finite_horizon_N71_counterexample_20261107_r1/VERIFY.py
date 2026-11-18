#!/usr/bin/env python3
"""Exact independent Fraction certificate for S23/AV N(71)=439.

Finite triangular likelihood pair enumeration. No floating-point comparison.
"""
from bisect import bisect_left
from fractions import Fraction

H = 71
N_BEFORE = 438
N_AT = 439
seven = [7**i for i in range(N_AT + H + 2)]
ten = [10**i for i in range(N_AT + H + 2)]

# Suffix ratios 7^j(7/10)^i; threshold is the reciprocal.
thresholds = sorted(Fraction(ten[i], seven[i + j])
                    for i in range(H + 1)
                    for j in range(H - i + 1))
assert len(thresholds) == 2628
assert len(set(thresholds)) == len(thresholds)
zero_threshold_index = bisect_left(thresholds, Fraction(1))
assert zero_threshold_index == 2196
assert thresholds[zero_threshold_index - 1] == Fraction(10**60, 7**71)
assert thresholds[zero_threshold_index] == 1
L = thresholds[zero_threshold_index - 1]

# A simple exact lower bound on N(71) is only 388; the conjecture
# would predict precisely 388. Confirm with integers, not logarithms.
assert seven[458] > ten[387]
assert seven[459] < ten[388]

# For fixed ell, the smallest k with Lambda(k,ell)<1 yields the
# largest below-one likelihood. Prove the critical gap empty for n<=438.
# k_min(ell) increases with ell. At ell=68, its first below-one
# candidate already has total length 439, so ell>=68 cannot occur.
kmins = []
for ell in range(69):
    k = 0
    while seven[k + ell] >= ten[k]:
        k += 1
    assert seven[k + ell] < ten[k]
    if k:
        assert seven[k - 1 + ell] >= ten[k - 1]
    kmins.append(k)
assert kmins[-1] == 371
assert 68 + kmins[-1] == 439
assert all(kmins[i] <= kmins[i + 1] for i in range(68))
assert all(Fraction(seven[ell + kmins[ell]], ten[kmins[ell]]) <= L
           for ell in range(68))
# The single first gap-filling prefix is (k,ell)=(371,68).
witness = Fraction(seven[439], ten[371])
assert L < witness < 1

# Independently enumerate every finite threshold interval, including
# both unbounded intervals. The lone exact equality class is Lambda=1.

def reachable_intervals(n):
    seen = set()
    visited = 0
    for ell in range(n + 1):
        for k in range(n - ell + 1):
            if k == ell == 0:
                continue  # equality Lambda=1 (all label 3)
            v = Fraction(seven[k + ell], ten[k])
            i = bisect_left(thresholds, v)
            # Unique-factorization gives exactly one equality class.
            assert i == len(thresholds) or thresholds[i] != v
            seen.add(i)
            visited += 1
    return seen, visited

for n, expected_missing in ((388, {2196}), (438, {2196}), (439, set())):
    seen, inspected = reachable_intervals(n)
    absent = set(range(len(thresholds) + 1)) - seen
    assert absent == expected_missing, (n, sorted(absent))
    print(f'n={n}; prefixes_checked={inspected}; occupied_open_intervals={len(seen)}/2629; missing={sorted(absent)}')

# One equality class {1} is always present via all-3 words;
# hence S(438,71)=2629 and S(439,71)=2630.
assert len(thresholds) + 2 == 2630
print('N(71)=439; S(438,71)=2629; S(439,71)=2630')
print('critical threshold interval: (10^60/7^71, 1)')
print('first filling prefix: k=371 label-1, ell=68 label-4, length=439')
print('prior conjecture at h=71 predicts 388: REFUTED')
print('PASS_S23_AV_FINITE_HORIZON_N71_SHARP_COUNTEREXAMPLE_20261107')
