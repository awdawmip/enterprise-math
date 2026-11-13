#!/usr/bin/env python3
"""Exact independent signed-triad word / 12-slot incidence / X6 endpoint check.

Model: a labelled triadic incidence event selects three distinct native axis
indices and independently chooses +/- on each. No claim is made that every
such event satisfies a physical P000 triadic-closure transition.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, product
from math import comb

AXES = tuple(range(6))
TRIPLES = tuple(combinations(AXES, 3))
def make_events():
    out = []
    for S in TRIPLES:
        for signs in product((-1, 1), repeat=3):
            v = [0] * 6
            for i, sign in zip(S, signs):
                v[i] = sign
            out.append(tuple(v))
    return tuple(out)

EVENTS = make_events()
assert len(EVENTS) == len(set(EVENTS)) == 160

@lru_cache(None)
def unsigned_ordered(D):
    if not any(D):
        return 1
    count = 0
    for S in TRIPLES:
        if all(D[i] > 0 for i in S):
            R = list(D)
            for i in S: R[i] -= 1
            count += unsigned_ordered(tuple(R))
    return count

def feasible(z, m):
    A = sum(abs(x) for x in z)
    if any(abs(x) > m for x in z) or A > 3*m or (3*m - A) % 2:
        return False
    K = (3*m - A)//2
    return K <= sum((m-abs(x))//2 for x in z)

def fibre_formula(z, m):
    if not feasible(z, m):
        return 0
    a = tuple(abs(x) for x in z)
    K = (3*m - sum(a))//2
    caps = tuple((m-x)//2 for x in a)
    total = 0
    def visit(i, remaining, ks):
        nonlocal total
        if i == 6:
            if remaining: return
            D = tuple(a[j]+2*ks[j] for j in AXES)
            n = unsigned_ordered(D)
            for j in AXES:
                n *= comb(D[j], (D[j]+z[j])//2)
            total += n
            return
        for k in range(min(remaining, caps[i])+1):
            visit(i+1, remaining-k, ks+(k,))
    visit(0, K, ())
    return total

def word_dp(m):
    current = {(0,)*6:1}
    for _ in range(m):
        nxt = defaultdict(int)
        for z, count in current.items():
            for event in EVENTS:
                nxt[tuple(z[i]+event[i] for i in AXES)] += count
        current = dict(nxt)
    return current

def main():
    summaries = []
    for m in (1,2,3):
        words = word_dp(m)
        feasible_set = {z for z in product(range(-m,m+1), repeat=6)
                        if feasible(z,m)}
        assert set(words) == feasible_set
        for z,n in words.items():
            assert n == fibre_formula(z,m), (m,z,n,fibre_formula(z,m))
        assert sum(words.values()) == 160**m
        summaries.append((m,len(words),sum(words.values()),max(words.values())))
    assert summaries == [(1,160,160,1),(2,3477,25600,160),(3,26440,4096000,4320)]
    words2 = word_dp(2)
    words3 = word_dp(3)
    assert words2[(0,)*6] == 160
    assert words3.get((0,)*6,0) == 0
    maxima = [z for z,n in words3.items() if n == 4320]
    assert set(maxima) == {
        tuple(sign if j==i else 0 for j in AXES)
        for i in AXES for sign in (-1,1)
    }
    bands = Counter()
    weights = Counter()
    for z,n in words3.items():
        a = sum(abs(x) for x in z)
        bands[a] += 1
        weights[a] += n
    expected = ((1,12,51840),(3,292,656160),(5,2232,1683360),
                (7,8064,1369440),(9,15840,335200))
    assert tuple((a,bands[a],weights[a]) for a,_,_ in expected) == expected
    print('PASS_X6_TRIADIC_12_TO_6_ENDPOINT_PUSHFORWARD_M3')
    print('endpoint_count_by_m / total_words / maximal_fibre:',summaries)
    print('m2_origin_two_event_loops:',words2[(0,)*6])
    print('m3_origin_three_event_loops:',words3.get((0,)*6,0))
    print('m3_maximal_fibres:',len(maxima),'at signed unit endpoints')
    print('m3_L1_bands (norm, endpoints, words):',expected)
    print('validation: exact integer DP vs independent 12-slot incidence summation')

if __name__ == '__main__':
    main()
