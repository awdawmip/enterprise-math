#!/usr/bin/env python3
"""R606 exact author-side auxiliary checks; no native BRC dynamics executed."""
from fractions import Fraction
from math import comb


def catalan(k):
    return comb(2 * k, k) // (k + 1)


def h2(k):
    return comb(2 * k + 3, 4) * catalan(k)


# Exact fixed-Catalan-family k-separation and strict log-concavity.
for k in range(2, 33):
    assert Fraction(h2(k + 1), h2(k)) == Fraction(2 * (2 * k + 5), k)
for k in range(3, 33):
    assert h2(k) ** 2 > h2(k - 1) * h2(k + 1)
assert len({h2(k) for k in range(2, 34)}) == 32
print("R606_H2_RECURRENCE_EXACT_PASS k=2..32; strict log-concavity k=3..32")


# Twelve distinct SIGNED-DIRECTION LABELS (+/- E_i), one occupied label.
# This update is a declared finite symbolic test, not a native X6 rotation.
labels = tuple((sign, axis) for sign in (+1, -1) for axis in range(1, 7))
N = len(labels)
states = tuple(range(N))

def move(i):
    return (i + 1) % N


def pi(i):
    return 1  # occupied-branch scalar; erases which signed direction


def output(i):
    return int(i == 0)  # distinguished-branch readout


def class_ids(signatures):
    distinct = {}
    result = []
    for signature in signatures:
        if signature not in distinct:
            distinct[signature] = len(distinct)
        result.append(distinct[signature])
    return tuple(result)


def actual_word_signature(i, h):
    return (pi(i),) + tuple(output((i + t) % N) for t in range(h + 1))

current = class_ids(tuple((pi(i), output(i)) for i in states))
counts = [len(set(current))]
for h in range(0, N):
    # Independent direct comparison of all 12x12 pairs through the h-step word language.
    direct = class_ids(tuple(actual_word_signature(i, h) for i in states))
    assert all((current[i] == current[j]) == (direct[i] == direct[j])
               for i in states for j in states)
    if h == N - 1:
        break
    current = class_ids(tuple((current[i], current[move(i)]) for i in states))
    counts.append(len(set(current)))
assert counts == list(range(2, 13)) + [12]
assert counts[9] == 11 and counts[10] == 12
assert len(set(tuple(output((i + t) % N) for t in range(N)) for i in states)) == N
print("R606_12_DIRECTION_PARTITION_COUNTS", *counts)
print("R606_SHARP_HORIZON h=10; n=12; initial_blocks=2; n-initial_blocks=10")
print("R606_12_DIRECTION_ALL_144_PAIR_COMPARISONS_AT_EACH_HORIZON_PASS")
print("R606_ALL_EXACT_TESTS_PASS")
