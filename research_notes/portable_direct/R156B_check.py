#!/usr/bin/env python3
"""Exhaustive exact alias-fiber cardinality through word length 20.

All 2^m binary words for each m=1..20; no floating point.
"""
from collections import defaultdict
from fractions import Fraction
from math import gcd
import json


def key_integer(n, m):
    p = [0] * (m + 1)
    for i in range(m):
        p[i + 1] = p[i] + ((n >> (m - 1 - i)) & 1)
    an, ad, bn, bd = 0, 1, 1, 1
    for i in range(m):
        pi = p[i]
        for j in range(i + 1, m + 1):
            q = p[j] - pi
            k = j - i
            if (q - 1) * ad > an * k:
                an, ad = q - 1, k
            if (q + 1) * bd < bn * k:
                bn, bd = q + 1, k
    if an * bd >= bn * ad:
        return None
    ga = gcd(abs(an), ad)
    gb = gcd(abs(bn), bd)
    an, ad = an // ga, ad // ga
    bn, bd = bn // gb, bd // gb
    U = ad + min(p[j] * ad - an * j for j in range(m + 1))
    V = max(p[j] * bd - bn * j for j in range(m + 1))
    return an, ad, bn, bd, U, V


def key_fraction(n, m):
    p = [0] * (m + 1)
    for i in range(m):
        p[i + 1] = p[i] + ((n >> (m - 1 - i)) & 1)
    a, b = Fraction(0), Fraction(1)
    for i in range(m):
        for j in range(i + 1, m + 1):
            q = p[j] - p[i]
            k = j - i
            a = max(a, Fraction(q - 1, k))
            b = min(b, Fraction(q + 1, k))
    if a >= b:
        return None
    U = a.denominator + min(p[j] * a.denominator - j * a.numerator
                            for j in range(m + 1))
    V = max(p[j] * b.denominator - j * b.numerator
            for j in range(m + 1))
    return a.numerator, a.denominator, b.numerator, b.denominator, U, V


def main():
    out = {
        "marker": "R156B_EXHAUSTIVE_M20_NO_TRIPLE_ALIAS_PASS",
        "length_range_inclusive": [1, 20],
        "binary_candidates_total": 0,
        "fraction_crosscheck_candidates": 0,
        "all_lengths_maximum_fiber": 0,
        "by_length": [],
    }
    for m in range(1, 21):
        cls = defaultdict(int)
        for n in range(1 << m):
            k = key_integer(n, m)
            if m <= 10:
                assert k == key_fraction(n, m), (m, n, k)
                out["fraction_crosscheck_candidates"] += 1
            if k is not None:
                cls[k] += 1
        max_size = max(cls.values())
        record = {
            "m": m,
            "candidate_words": 1 << m,
            "admissible_words": sum(cls.values()),
            "distinct_exact_observers": len(cls),
            "alias_pairs": sum(v == 2 for v in cls.values()),
            "triple_or_larger_classes": sum(v >= 3 for v in cls.values()),
            "maximum_fiber": max_size,
        }
        assert record["triple_or_larger_classes"] == 0
        assert sum(cls.values()) == (len(cls) + record["alias_pairs"])
        out["by_length"].append(record)
        out["binary_candidates_total"] += 1 << m
        out["all_lengths_maximum_fiber"] = max(out["all_lengths_maximum_fiber"], max_size)
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
