#!/usr/bin/env python3
"""Exact verification of signed X6 Path-Formal BRC finite-horizon quotient.
Scientific scope: formal ordered signed unit-step words, no heartbeat simulator.
"""
from __future__ import annotations
import itertools
import json
from functools import lru_cache
from math import comb, factorial
from collections import defaultdict


def shell_count(m: int, r: int) -> int:
    return 1 if r == 0 else sum(
        2**j * comb(m, j) * comb(r - 1, j - 1)
        for j in range(1, min(m, r) + 1)
    )


def reachable_count(m: int, k: int) -> int:
    return sum(shell_count(m, r) for r in range(k % 2, k + 1, 2))


@lru_cache(maxsize=None)
def prefix_fiber(m: int, k: int, z: tuple[int, ...]) -> int:
    norm = sum(map(abs, z))
    if len(z) != m or norm > k or (k - norm) % 2:
        return 0
    backtracks = (k - norm) // 2
    total = 0
    for c in itertools.product(range(backtracks + 1), repeat=m):
        if sum(c) != backtracks:
            continue
        denominator = 1
        for zi, ci in zip(z, c):
            denominator *= factorial(max(zi, 0) + ci) * factorial(max(-zi, 0) + ci)
        total += factorial(k) // denominator if factorial(k) % denominator == 0 else 0
        assert factorial(k) % denominator == 0
    return total


def endpoint(word: tuple[tuple[int, int], ...], m: int) -> tuple[int, ...]:
    v = [0] * m
    for i, sign in word:
        v[i] += sign
    return tuple(v)


def exhaustive_check(m: int, n: int) -> dict:
    alphabet = tuple((i, sign) for i in range(m) for sign in (-1, 1))
    output = {}
    for h in range(n + 1):
        obs_to_prediction = {}
        prediction_to_obs = {}
        sizes = defaultdict(int)
        for w in itertools.product(alphabet, repeat=n):
            actual = tuple(endpoint(w[:n-t], m) for t in range(h + 1))
            prefix_z = endpoint(w[:n-h], m)
            prediction = (prefix_z, w[n-h:])
            assert obs_to_prediction.setdefault(actual, prediction) == prediction
            assert prediction_to_obs.setdefault(prediction, actual) == actual
            sizes[prediction] += 1
        expected = (2*m)**h * reachable_count(m, n-h)
        assert len(sizes) == expected == len(obs_to_prediction)
        assert sum(sizes.values()) == (2*m)**n
        for (prefix_z, suffix), multiplicity in sizes.items():
            assert multiplicity == prefix_fiber(m, n-h, prefix_z), (m, n, h, prefix_z)
        output[str(h)] = {"classes": len(sizes), "expected_classes": expected,
                          "word_total": sum(sizes.values())}
    return {"m": m, "n": n, "total_words": (2*m)**n, "horizons": output}


def exact_checks() -> dict:
    cases = [(1, 7), (2, 7), (3, 6), (6, 4)]
    exhaustive = [exhaustive_check(m, n) for m,n in cases]
    assert prefix_fiber(6, 10, (0,)*6) > 0
    assert prefix_fiber(6, 10, (10,0,0,0,0,0)) == 1
    assert prefix_fiber(6, 10, (9,0,0,0,0,0)) == 0
    for suffix in itertools.product(((i,si) for i in range(6) for si in (-1,1)), repeat=2):
        z = tuple(-v for v in endpoint(suffix,6))
        assert prefix_fiber(6,10,z) > 0
    big = {"m":6,"n":12,"h":2,
           "endpoint_only_classes":reachable_count(6,12),
           "prefix_length_10_endpoints":reachable_count(6,10),
           "future_safe_classes": 12**2*reachable_count(6,10),
           "words_total": 12**12,
           "zero_endpoint_possible_suffixes":12**2,
           "additional_fixed_bit_lower_bound":8,
           "zero_endpoint_prefix_mass_10":prefix_fiber(6,10,(0,)*6)}
    return {"status":"PASS","exhaustive":exhaustive,"signed_six_axis_example":big,
            "scope":"formal ordered signed native X6 paths only; no native heartbeat BRC execution"}


if __name__ == "__main__":
    print(json.dumps(exact_checks(),indent=2,ensure_ascii=False,sort_keys=True))
