#!/usr/bin/env python3
"""R762AA: exact integer Bellman verification for ordered cyclic PASS macros.
Run: python research_notes/R762AA_THREE_ROOT_VERIFY.py
Writes sibling R762AA_THREE_ROOT_EVIDENCE.json.
"""
from collections import Counter
from functools import lru_cache
from itertools import permutations, product
from pathlib import Path
import json

INF = 10**6

def stocks_of(q, roots, initial, progress):
    s = list(initial)
    for r,p in zip(roots, progress):
        if 0 < p < q:
            s[r] -= 1
            s[(r+p)%q] += 1
    return s

def optimum(q, roots, initial, witness=False):
    roots, initial = tuple(roots), tuple(initial)
    n = len(roots)
    assert q >= 2 and len(initial) == q and sum(initial) >= 1
    assert all(x >= 0 for x in initial)
    assert all(0 <= r < q for r in roots)
    @lru_cache(None)
    def solve(progress, last):
        if all(p == q for p in progress):
            return (0, ())
        started = sum(p > 0 for p in progress)
        stocks = stocks_of(q, roots, initial, progress)
        best = (INF, ())
        for i,p in enumerate(progress):
            if p == q or (p == 0 and i != started):
                continue
            tail = (roots[i]+p)%q
            if stocks[tail] == 0:
                continue
            next_progress = progress[:i] + (p+1,) + progress[i+1:]
            subcost, subplan = solve(next_progress, i)
            switching = int(last >= 0 and last != i and progress[last] < q)
            candidate = (switching + subcost, (i,)+subplan)
            if candidate[0] < best[0]:
                best = candidate
        return best
    h, plan = solve((0,)*n, -1)
    return {"h":h,"macro_step_indices":list(plan),"visited_states":solve.cache_info().currsize} if witness else h

def allocations(total, q):
    if q == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for tail in allocations(total-first,q-1):
                yield (first,)+tail

def frontier(q, word, K):
    return min(optimum(q,word,initial) for initial in allocations(K,q))

def verify():
    census = []
    for n in range(1,8):
        costs, genuine = Counter(), Counter()
        for tail in product((0,1,2),repeat=n-1):
            word = (0,)+tail
            cost = optimum(3,word,(1,0,0))
            costs[cost] += 1
            if len(set(word)) == 3:
                genuine[cost] += 1
        assert sum(costs.values()) == 3**(n-1)
        census.append({"n":n,"words":sum(costs.values()),
            "cost_hist":dict(sorted(costs.items())),
            "three_root_words":sum(genuine.values()),
            "three_root_hist":dict(sorted(genuine.items()))})
    pal_tests = 0
    for q in (3,4):
        d = q
        for rest in permutations(range(1,q)):
            roots = (0,)+rest
            word = roots+roots[-2::-1]
            for K in range(1,d+1):
                assert frontier(q,word,K) == d-K,(q,word,K)
                pal_tests += 1
    assert pal_tests == 30
    two_root_tests = 0
    for n in range(1,8):
        for tail in product((0,1),repeat=n-1):
            word = (0,)+tail
            b_runs = sum(word[i] == 1 and (i == 0 or word[i-1] != 1)
                         for i in range(len(word)))
            assert optimum(3,word,(1,0,0)) == b_runs
            two_root_tests += 1
    assert two_root_tests == 127
    cases = {}
    for label,word in {
        "blocked":(0,0,1,1,2,2),
        "alternating":(0,1,2,0,1,2),
        "nested_palindrome":(0,1,2,1,0),
        "nongreedy":(0,1,2,0,2,1),
    }.items():
        cases[label] = {"word":list(word),
            "frontier_K1_to_3":[frontier(3,word,K) for K in (1,2,3)],
            "K1_initial_at_0":optimum(3,word,(1,0,0),True)}
    assert cases["blocked"]["frontier_K1_to_3"] == [2,1,0]
    assert cases["alternating"]["frontier_K1_to_3"] == [4,2,0]
    assert cases["nested_palindrome"]["frontier_K1_to_3"] == [2,1,0]
    assert cases["nongreedy"]["K1_initial_at_0"]["h"] == 3
    return {"schema":"R762AA_THREE_ROOT_ORDERED_FRONTIER_V1",
      "date":"2026-11-14",
      "model":"conditional integer q-cycle PASS scheduler with prescribed macro first-start order",
      "finite_scope":"q=3, all 1093 first-root-0 words length1..7 at K1=(1,0,0); q3,q4 palindrome all labelled other-root permutations and all initial allocations K1..d",
      "census":census,"cases":cases,
      "palindrome_tests":pal_tests,"two_root_regressions":two_root_tests,
      "result":"ALL_ASSERTIONS_PASSED",
      "universal_palindrome_theorem":"separately human-proved for all q>=d>=1, K>=1",
      "native_triadic_admission":"UNVERIFIED",
      "formal_result":"NOT_PUBLISHED","independent_review":"NOT_REVIEWED"}

if __name__ == "__main__":
    result = verify()
    target = Path(__file__).with_name("R762AA_THREE_ROOT_EVIDENCE.json")
    target.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,sort_keys=True))
