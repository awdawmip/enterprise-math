#!/usr/bin/env python3
"""R727 exact six-axis triad-incidence checker; Python stdlib, integer only."""
from itertools import combinations, product
from functools import lru_cache
from math import factorial, prod
import json

AXES = range(6)
TRIPLES = tuple(combinations(AXES, 3))

def greedy(counts):
    a = list(counts)
    result = []
    for _ in range(sum(a) // 3):
        idx = sorted(AXES, key=lambda i: (-a[i], i))[:3]
        if min(a[i] for i in idx) < 1:
            return None
        result.append(tuple(idx))
        for i in idx:
            a[i] -= 1
    return result if all(x == 0 for x in a) else None

def coefficient(counts):
    @lru_cache(None)
    def f(rem):
        if not any(rem):
            return 1
        out = 0
        for triple in TRIPLES:
            if all(rem[i] for i in triple):
                nxt = list(rem)
                for i in triple:
                    nxt[i] -= 1
                out += f(tuple(nxt))
        return out
    return f(tuple(counts))

def direct_labeled_count(counts):
    atoms = tuple(i for i, a in enumerate(counts) for _ in range(a))
    n = len(atoms)
    @lru_cache(None)
    def rec(mask):
        if not mask:
            return 1
        lowest = mask & -mask
        i = lowest.bit_length() - 1
        remaining = mask ^ lowest
        available = [j for j in range(i + 1, n)
                     if (remaining >> j) & 1 and atoms[j] != atoms[i]]
        ans = 0
        for j, k in combinations(available, 2):
            if atoms[j] != atoms[k]:
                ans += rec(remaining ^ (1 << j) ^ (1 << k))
        return ans
    return rec((1 << n) - 1)

def run():
    results = []
    for m in (1, 2, 3):
        count_vectors = feasible = total_lifts = maximum = 0
        witness = None
        for a in product(range(3*m + 1), repeat=6):
            if sum(a) != 3*m:
                continue
            count_vectors += 1
            yes = max(a) <= m
            g = greedy(a)
            assert (g is not None) == yes, (m,a,g)
            direct = direct_labeled_count(a)
            if yes:
                feasible += 1
                polynomial_coefficient = coefficient(a)
                labeled = polynomial_coefficient * prod(factorial(x) for x in a) // factorial(m)
                assert labeled == direct, (m,a,labeled,direct)
                total_lifts += labeled
                if labeled > maximum:
                    maximum, witness = labeled, a
            else:
                assert direct == 0, (m,a,direct)
        results.append(dict(m=m,all_count_vectors_sum_3m=count_vectors,
                           axis_compatible=feasible,
                           total_labeled_decompositions_over_vectors=total_lifts,
                           largest_labeled_count=maximum,argmax=witness))
    examples = {}
    for a in ((1,1,1,1,1,1),(2,2,2,0,0,0),(2,1,1,1,1,0),(3,1,1,1,0,0)):
        examples[''.join(map(str,a))] = dict(m=sum(a)//3,
                     greedy=greedy(a),labeled_count=direct_labeled_count(a))
    assert [examples[k]['labeled_count'] for k in ('111111','222000','211110','311100')] == [10,4,6,0]
    assert [(x['all_count_vectors_sum_3m'],x['axis_compatible'],
             x['largest_labeled_count']) for x in results] == [
             (56,20,1),(462,141,10),(2002,580,124)]
    out=dict(schema='EM_R727_TRIAD_AXIS_FEASIBILITY_V1',
             model='AXIS_DISTINCT_EQUAL_QUANTUM_CANDIDATE_ONLY',
             frozen_science='a72226e2430ffa4786321ac86e7f0c599d5f0389',
             exact_exhaustion=results,examples=examples,
             result='R727_X6_TRIAD_AXIS_PARTITION_EXACT_PASS')
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))
    print(out['result'])
    return out
if __name__ == '__main__':
    run()
