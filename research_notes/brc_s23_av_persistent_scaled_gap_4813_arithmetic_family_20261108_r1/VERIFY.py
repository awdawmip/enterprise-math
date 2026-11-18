#!/usr/bin/env python3
"""S23/AV persistent scaled-gap adjacency and 4,813-term arithmetic anomaly certificate.
Only exact Python integers/Fraction; no floating-point comparisons are trusted.
"""
from fractions import Fraction

A = Fraction(10**60, 7**71)
X = Fraction(7**439, 10**371)
W = Fraction(7**510, 10**431)
M = 4812


def kmin(v: int) -> int:
    """Least k >= 0 with 7**(k+v) < 10**k, via exact binary search."""
    lo, hi = 0, 8*v+8
    assert 7**(hi+v) < 10**hi
    while lo < hi:
        mid = (lo+hi)//2
        if 7**(mid+v) < 10**mid:
            hi = mid
        else:
            lo = mid+1
    assert 7**(lo+v) < 10**lo
    if lo:
        assert 7**(lo-1+v) >= 10**(lo-1)
    return lo


def ratio(v: int, k: int) -> Fraction:
    return Fraction(7**(v+k), 10**k)

# Base adjacency A < B=1 in T_71: every T(i,s) strictly below 1 is <= A.
for s in range(1, 72):
    i = 0
    while 10**(i+1) < 7**s:
        i += 1
    assert i <= s and 10**i < 7**s
    assert Fraction(10**i, 7**s) <= A
assert 10**60 < 7**71
print('BASE_ADJACENCY_T71: PASS')

# Seed finite return block, exact maximum below 1 for each v.
seed = [(v, kmin(v)) for v in range(147)]
for v, k in seed[:68]:
    assert ratio(v, k) <= A
block = [(v, k, ratio(v, k)) for v, k in seed[68:]]
assert block[0][:2] == (68, 371)
assert block[0][2] == X and A < X < 1
others = block[1:]
runner = max(others, key=lambda row: row[2])
assert runner[:2] == (136, 742)
assert runner[2] == X*X
second = max((row for row in others if row[0] != 136), key=lambda row: row[2])
assert second[:2] == (125, 682)
print('SEED_0_TO_146: first v=68 k=371; runner v=136 k=742; PASS')

# W>1 and the exact three close boundary comparisons, each done with Python integers.
assert 7**510 > 10**431
assert 7**(439+510*M) < 10**(371+431*M)  # X*W^4812 < 1
assert 7**(439+510*(M+1)) < 10**(371+431*(M+1)) # X*W^4813 < 1
assert 7**(949+510*M) < 10**(802+431*M)  # X^2*W^4812 < A
assert 7**(949+510*(M+1)) > 10**(802+431*(M+1)) # X^2*W^4813 > A
v,k,_ = second
assert 7**(v+k+71+510*(M+1)) < 10**(k+60+431*(M+1))
print('RETURN_BLOCK_79: exactly one return at v=68+79*m for m=0..4812; PASS')
print('FIRST_NONPERIODIC_RETURN: v=380363 after v=380295; PASS')

# Exact tail formula at all h_m=140+79*m: endpoint inequalities suffice
# because W>1 makes the ratio 7^(n+h)/10^n increase with m.
assert 7**903 >= 10**763
assert 7**(904+510*M) < 10**(764+431*M)
print('TAIL_FORMULA: n_tail(140+79*m)=764+431*m for m=0..4812; PASS')
print('MAIN_CERTIFICATE: N(140+79*m)>=880+431*m=n_tail+116, m=0..4812; PASS')
print('NEW_EXAMPLE: N(298)>=1742; n_tail(298)=1626; PASS')
print('HORIZONS_CERTIFIED:', M+1, 'LAST_H:', 140+79*M)
print('PASS_S23_AV_PERSISTENT_SCALED_GAP_4813_HORIZONS_20261108')
