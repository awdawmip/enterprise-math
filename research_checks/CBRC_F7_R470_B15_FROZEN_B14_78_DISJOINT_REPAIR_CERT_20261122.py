#!/usr/bin/env python3
"""Exact integer audit of the frozen F7 B14 witness on the full B15 box.

Mathematical scope: repair cost of the particular r469 q*, not E_15^*.
Run from any working directory with the repository research_artifacts available.
"""
from collections import Counter
from hashlib import sha256
from itertools import product
from json import loads
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
B14_PATH = ROOT / "research_artifacts/F7_R469_B14_Exact_Quarter_Witness_20261122.json"
PACK_PATH = ROOT / "research_artifacts/F7_R470_B15_Frozen_B14_Disjoint78_Witnesses_20261122.json"
B14_SHA256 = "83bb9dabbace1a6ab4542538cc6a8b8c8fb06bb5ce055e7d9fddf842e01d5169"
EXPECTED_DISTRIBUTION = {-4: 56, -3: 2856, -2: 54994, -1: 268878,
                         0: 433365, 1: 147832, 2: 15538, 3: 2}


def key(point):
    x, y = point
    return (abs(x), y)


def mutable(point):
    x, y = point
    return y != 0 and (x, y) not in ((2, 1), (1, -1))


def points(z):
    a, b, c, d = z
    k = a - 2 * b - c + 2 * d
    return ((a + k, b + k), (c - k, d - k), (a, b), (c, d))


def check():
    original = B14_PATH.read_bytes()
    assert sha256(original).hexdigest() == B14_SHA256
    rows = loads(original)
    assert len(rows) == 1190
    assert rows == sorted(rows)
    assert all(len(row) == 3 and row[0] >= 0 and row[1] != 0
               and row[2] in (1, 2) for row in rows)
    increments = {(x, y): n for x, y, n in rows}
    assert len(increments) == 1190
    assert (2, 1) not in increments and (1, -1) not in increments

    def mq(point):
        x, y = point
        if x == 0 and y == 0:
            return 0
        if y == 0:
            return 4
        return 2 + increments.get(key(point), 0)

    def four_d(p):
        return mq(p[0]) + mq(p[1]) - mq(p[2]) - mq(p[3])

    old_keys = set()
    old_max = 0
    for z in product(range(-14, 15), repeat=4):
        p = points(z)
        old_keys.update(map(key, p))
        old_max = max(old_max, abs(four_d(p)))
    assert len(old_keys) == 4159 and old_max == 2

    distribution = Counter()
    new_keys = set()
    violations = 0
    for z in product(range(-15, 16), repeat=4):
        p = points(z)
        n = four_d(p)
        distribution[n] += 1
        key_set = {key(pt) for pt in p}
        new_keys.update(key_set)
        if abs(n) > 2:
            violations += 1
            assert key_set <= old_keys, (z, sorted(key_set - old_keys))
    assert sum(distribution.values()) == 31**4 == 923521
    assert dict(distribution) == EXPECTED_DISTRIBUTION
    assert violations == 2914
    assert len(new_keys) == 4763 and len(new_keys - old_keys) == 604

    witnesses = loads(PACK_PATH.read_text(encoding="utf-8"))
    assert len(witnesses) == 78
    assert len({tuple(z) for z in witnesses}) == 78
    used = set()
    margin_sum = 0
    for z in witnesses:
        assert len(z) == 4 and all(type(v) is int and -15 <= v <= 15
                                   for v in z)
        p = points(z)
        n = four_d(p)
        assert abs(n) > 2
        coeff = Counter()
        for idx, pt in enumerate(p):
            k = key(pt)
            if mutable(k):
                coeff[k] += 1 if idx < 2 else -1
        support = {k for k, c in coeff.items() if c}
        assert support and all(abs(coeff[k]) == 1 for k in support)
        assert support <= old_keys
        assert not (used & support), z
        used.update(support)
        margin_sum += abs(n) - 2
    assert margin_sum == 78

    print("EXACT: B14 q* on B15, 923521 inputs, 2914 violations")
    print("4D distribution:", sorted(distribution.items()))
    print("B14 keys=4159; B15 keys=4763; 604 new")
    print("CERTIFIED: any B15 half-feasible repair changes >=78 old mutable keys")
    print("CERTIFIED: sum_old |q'-q*| >= 78/4 = 39/2")
    print("Scope: fixed r469 witness repair, not B15 global infeasibility")


if __name__ == "__main__":
    check()
