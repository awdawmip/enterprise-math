#!/usr/bin/env python3
"""R186: exact pair-only latest-source query sorting decision trees."""
from functools import lru_cache
from itertools import permutations
from json import dumps
from pathlib import Path


def pair_answer(history, a, b):
    return a if history.index(a) > history.index(b) else b


def mergesort_oracle(history, items):
    calls = 0

    def sort(part):
        nonlocal calls
        if len(part) < 2:
            return list(part)
        half = len(part) // 2
        left, right = sort(part[:half]), sort(part[half:])
        out = []
        i = j = 0
        while i < len(left) and j < len(right):
            later = pair_answer(history, left[i], right[j])
            calls += 1
            if later == left[i]:
                out.append(right[j])
                j += 1
            else:
                out.append(left[i])
                i += 1
        return out + left[i:] + right[j:]

    return tuple(sort(items)), calls


def exact_pair_minimax(k):
    states = tuple(permutations(range(k)))
    if k <= 1:
        return 0, 1
    choices = []
    for a in range(k):
        for b in range(a+1, k):
            first = sum(1 << i for i, p in enumerate(states) if p.index(a) > p.index(b))
            choices.append(first)

    @lru_cache(None)
    def solve(belief):
        if belief.bit_count() == 1:
            return 0
        best = k * (k-1) // 2
        for first in choices:
            x = belief & first
            y = belief & ~first
            if not x or not y:
                continue
            best = min(best, 1+max(solve(x),solve(y)))
        return best

    return solve((1 << len(states))-1), solve.cache_info().currsize


def run():
    result = {
        'schema': 'R186_PAIR_ORACLE_SORT_CHECK_V1',
        'test_status': 'PASS',
        'arithmetic': 'exact integer and finite permutation enumeration',
        'scope': 'known full source support; binary latest-of-two query, no X6 path/provenance erasure',
        'frozen_science_pin': '43ec6098b1330ae86d0a7863be336c5d97f6ef34',
        'exact_minimax': [],
        'mergesort_full_permutations': 0,
        'max_mergesort_calls': {},
    }
    for k in range(1, 6):
        optimum, beliefs = exact_pair_minimax(k)
        assert optimum == [0, 1, 3, 5, 7][k-1]
        result['exact_minimax'].append({'r': k, 'optimal_worst_case_calls': optimum, 'explored_beliefs': beliefs})
    for k in range(1, 9):
        largest = 0
        for p in permutations(range(k)):
            got, calls = mergesort_oracle(p, list(range(k)))
            assert got == p
            assert calls <= k * (k-1) // 2
            largest = max(largest, calls)
            result['mergesort_full_permutations'] += 1
        result['max_mergesort_calls'][str(k)] = largest
    return result


if __name__ == '__main__':
    data = run()
    Path(__file__).with_name('R186_verification.json').write_text(dumps(data, sort_keys=True, indent=2)+'\n', encoding='utf-8')
    print(dumps(data, sort_keys=True))
