#!/usr/bin/env python3
"""Exact X6 signed-axis word/relative-quotient verification.

Native scientific pin: 59538f585d037d09ef687b28715c4bc1a3f9fe03.
Historical comparison pin: fd2bcff10ca6e147348b6c1236027fc0d2877df3.
No native claim, status or research admission is made by this checker.
"""
from collections import defaultdict
from functools import lru_cache
from math import factorial

DIM = 6
ZERO = (0,) * DIM


def canon(z):
    low = min(z)
    return tuple(x - low for x in z)


def min_signed_length(a):
    b = sorted(a)
    return sum(b[3:]) - sum(b[:3])


@lru_cache(None)
def compositions(k, d):
    if d == 1:
        return ((k,),)
    return tuple((i,) + rest for i in range(k + 1)
                 for rest in compositions(k - i, d - 1))


def signed_relative_brc(n, a):
    """Independent histogram sum over native signed lifts and hidden 2-step pairs."""
    total, components = 0, []
    for h in range(-n - max(a), n + 1):
        z = tuple(x + h for x in a)
        shortest = sum(abs(x) for x in z)
        if shortest > n or (n - shortest) % 2:
            continue
        k_total = (n - shortest) // 2
        subtotal = 0
        for k in compositions(k_total, DIM):
            denominator = 1
            for zi, ki in zip(z, k):
                denominator *= factorial(max(zi, 0) + ki)
                denominator *= factorial(max(-zi, 0) + ki)
            subtotal += factorial(n) // denominator
        total += subtotal
        components.append((h, z, shortest, subtotal))
    return total, components


def step_distribution(previous):
    next_counts = defaultdict(int)
    for a, count in previous.items():
        for axis in range(DIM):
            for direction in (-1, 1):
                z = list(a)
                z[axis] += direction
                next_counts[canon(z)] += count
    return dict(next_counts)


def main():
    counts = {ZERO: 1}
    cases, histogram = 0, []
    for n in range(7):
        assert sum(counts.values()) == 12**n
        for a, actual in counts.items():
            bound = min_signed_length(a)
            assert n >= bound and (n - sum(a)) % 2 == 0
            calculated, _ = signed_relative_brc(n, a)
            assert calculated == actual, (n, a, calculated, actual)
            cases += 1
        histogram.append((n, len(counts)))
        counts = step_distribution(counts)
    assert signed_relative_brc(2, ZERO)[0] == 12
    assert signed_relative_brc(6, ZERO)[0] == 21360
    a = (0, 1, 1, 2, 3, 5)
    assert min_signed_length(a) == 8
    total, components = signed_relative_brc(8, a)
    assert total == 4200
    assert [(h, mass) for h, _, _, mass in components] == [(-2, 3360), (-1, 840)]
    # Old positive-only C6 grade would demand n == sum(a) (mod 6).
    assert (8 - sum(a)) % 6 != 0 and (8 - sum(a)) % 2 == 0
    print("PASS X6_SIGNED_RELATIVE_PARITY_MEDIAN_BRC")
    print("independent_dp_vs_histogram_cases", cases)
    print("signed_relative_state_counts", histogram)
    print("r_zero_n6", 21360, "r_011235_n8", total)


if __name__ == "__main__":
    main()
