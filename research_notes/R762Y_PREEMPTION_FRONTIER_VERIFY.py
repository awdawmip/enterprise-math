#!/usr/bin/env python3
"""Exact finite cross-check for R762Y q-cycle macroevents.

This verifies the minimum number of internal macroevent interruptions for every
listed labelled phase word and each available initial token count. The recursive
state search admits *all* event interleavings preserving each macro's order and
all nonnegative per-port token allocations. It does not implement or validate
primitive TRIADIC_CLOSURE_E admission.
"""
from functools import lru_cache
from itertools import product
import json


def exact_min_interruptions(phases, q, token_count):
    n = len(phases)

    @lru_cache(maxsize=None)
    def rec(progress, stock, previous):
        if all(p == q for p in progress):
            return 0
        optimum = 10**9
        for i, p in enumerate(progress):
            if p == q:
                continue
            source = (phases[i] + p) % q
            if stock[source] < 1:
                continue
            next_stock = list(stock)
            next_stock[source] -= 1
            next_stock[(source + 1) % q] += 1
            next_progress = list(progress)
            next_progress[i] += 1
            interrupted = int(previous >= 0 and previous != i
                              and 0 < progress[previous] < q)
            candidate = interrupted + rec(tuple(next_progress),
                                          tuple(next_stock), i)
            optimum = min(optimum, candidate)
        return optimum

    best = 10**9
    for stock in product(range(token_count + 1), repeat=q):
        if sum(stock) == token_count:
            best = min(best, rec((0,) * n, stock, -1))
    return best


def main():
    cases = []
    for q, max_macros in [(2, 4), (3, 4), (4, 3)]:
        count = 0
        for n in range(1, max_macros + 1):
            for phases in product(range(q), repeat=n):
                distinct_roots = len(set(phases))
                for token_count in range(1, distinct_roots + 1):
                    expected = distinct_roots - token_count
                    actual = exact_min_interruptions(phases, q, token_count)
                    assert actual == expected, (q, phases, token_count, actual,
                                                expected)
                    count += 1
        cases.append({'q': q, 'max_macros': max_macros,
                      'exact_cases': count, 'mismatches': 0})
    evidence = {'schema': 'R762Y_EXACT_FINITE_VERIFICATION_V1',
                'domain': 'labelled q-cycle macroevents, event-shuffle within'
                          ' each macro, freely chosen initial port stocks',
                'tested': cases,
                'total_cases': sum(x['exact_cases'] for x in cases),
                'theorem_checked':
                    'min_preemptions(q, phases, K) = distinct_roots(phases)-K'
                    ' for 1<=K<=distinct_roots',
                'integer_semantics': 'exact Python int; exhaustive dynamic programming',
                'result': 'ALL_ASSERTIONS_PASSED',
                'native_admission_tested': False,
                'formal_review': 'NOT_REVIEWED'}
    print(json.dumps(evidence, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
