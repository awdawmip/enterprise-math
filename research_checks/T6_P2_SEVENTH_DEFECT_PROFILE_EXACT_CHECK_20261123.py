#!/usr/bin/env python3
"""Exact T6 v2(d)=7 finite ambiguity profile (full six reciprocal moments).

All arithmetic is integral; the two per-side budgets are each <=2331.
This enumerates necessary 2-adic signatures, not full rational solutions.
"""
from collections import Counter, defaultdict
from itertools import product

CAP = 2331
V = 7
J = tuple(range(1, ((CAP + 1) // (2**V)) + 1, 2))
WEIGHTS = tuple(2**V * j - 1 for j in J)
EXPECTED_PREFIX = ((2, 16032), (4, 7963), (16, 2293),
                   (58, 767), (141, 213), (227, 26))
EXPECTED_DEFECTS = {
    (-2, 1, 2, 0, 0, -1, 0, 0, 0): 10,
    (-1, 0, 1, 0, 1, 0, -1, 0, 0): 7,
    (-1, 2, 0, -2, 1, 0, 0, 0, 0): 5,
    (-2, 0, 2, 1, 0, 0, 0, -1, 0): 2,
    (-1, 0, 0, 0, 2, 0, 0, 0, -1): 1,
    (0, -1, 0, 1, 0, 1, 0, -1, 0): 1,
}

def recursive_profiles():
    m = [0] * len(WEIGHTS)
    def scan(i, remaining):
        if i == len(WEIGHTS):
            yield tuple(m)
            return
        for count in range(remaining // WEIGHTS[i] + 1):
            m[i] = count
            yield from scan(i + 1, remaining - count * WEIGHTS[i])
        m[i] = 0
    return set(scan(0, CAP))

def cartesian_profiles():
    return {counts for counts in product(*[range(CAP // w + 1) for w in WEIGHTS])
            if sum(c * w for c, w in zip(counts, WEIGHTS)) <= CAP}

def independent_dp_count():
    dp = [0] * (CAP + 1)
    dp[0] = 1
    for w in WEIGHTS:
        for mass in range(w, CAP + 1):
            dp[mass] += dp[mass - w]
    return sum(dp)

def signature(counts, kmax):
    return tuple(sum(n * pow(pow(j, k, 2**k), -1, 2**k)
                     for n, j in zip(counts, J)) % 2**k
                 for k in range(1, kmax + 1))

def canonical_delta(a, b):
    v = tuple(x - y for x, y in zip(a, b))
    first = next(x for x in v if x)
    return tuple(-x for x in v) if first > 0 else v

def main():
    assert J == (1, 3, 5, 7, 9, 11, 13, 15, 17)
    profiles = recursive_profiles()
    assert profiles == cartesian_profiles()
    assert len(profiles) == independent_dp_count() == 253
    for k, (unique, pair_count) in enumerate(EXPECTED_PREFIX, start=1):
        buckets = Counter(signature(a, k) for a in profiles)
        assert len(buckets) == unique
        assert sum(n * (n - 1) // 2 for n in buckets.values()) == pair_count
        print(f"K={k}: {unique} signatures, {pair_count} unordered colliding pairs")
    groups = defaultdict(list)
    for a in profiles:
        groups[signature(a, 6)].append(a)
    assert Counter(len(g) for g in groups.values()) == {1: 201, 2: 26}
    deltas = Counter()
    for group in groups.values():
        if len(group) == 2:
            a, b = group
            d = canonical_delta(a, b)
            deltas[d] += 1
            assert sum(d) == 0
            assert sum(c * w for c, w in zip(d, WEIGHTS)) == 0
            assert sum(c * j for c, j in zip(d, J)) == 0
    assert deltas == EXPECTED_DEFECTS
    print("PASS: 253 profiles, 227 signatures, 26 disjoint ambiguity pairs")
    for d, count in sorted(deltas.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  multiplicity={count}: delta={d}")
    print("Every possible defect preserves v2=7 layer count and exponent-mass")

if __name__ == "__main__":
    main()
