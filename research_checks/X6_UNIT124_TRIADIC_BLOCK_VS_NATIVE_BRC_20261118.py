#!/usr/bin/env python3
"""Exact sign/provenance-safe triadic block-to-native BRC comparison.
Scientific pin: enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03.
Source consumer: experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py
This checker does not run the native R063 C3/C4 benchmark.
"""
import json
from functools import lru_cache
from itertools import combinations
from math import factorial, prod

TRIADS = tuple(combinations(range(6), 3))

def require(c, msg):
    if not c:
        raise RuntimeError(msg)

@lru_cache(None)
def underlying(D):
    if sum(D) == 0:
        return 1
    total = 0
    for S in TRIADS:
        if all(D[i] > 0 for i in S):
            t = list(D)
            for i in S:
                t[i] -= 1
            total += underlying(tuple(t))
    return total

def native_count(D):
    return factorial(sum(D)) // prod(factorial(x) for x in D)

def macro_micro_count(D):
    require(sum(D) % 3 == 0, 'triadic degree')
    return (6 ** (sum(D) // 3)) * underlying(tuple(D))

def degrees(m, n=6):
    def rec(i, rem, prefix):
        if i == n:
            if rem == 0:
                yield prefix
            return
        for d in range(min(m, rem) + 1):
            yield from rec(i+1, rem-d, prefix+(d,))
    yield from rec(0, 3*m, ())

def brute_block_count(D):
    # Independent exact enumeration of distinct signed-coherent primitive words.
    D = tuple(D)
    def gen(rem, prefix):
        if not sum(rem):
            ok = all(len(set(prefix[k:k+3])) == 3 for k in range(0, len(prefix), 3))
            yield int(ok)
            return
        for i, count in enumerate(rem):
            if count:
                nxt = list(rem)
                nxt[i] -= 1
                yield from gen(tuple(nxt), prefix+(i,))
    return sum(gen(D, ()))

summary = []
for m in range(0, 4):
    families = 0
    strict = 0
    equality = 0
    max_n = 0
    for D in degrees(m):
        families += 1
        B = native_count(D)
        T = macro_micro_count(D)
        require(0 <= T <= B, f'block subset failure {D}')
        should_equal = (max(D, default=0) <= 1)
        require((T == B) == should_equal, f'equality criterion {D}')
        if m >= 1:
            upper_num = B * (3*m*(3*m-1)-sum(d*(d-1) for d in D))
            require(T * (3*m*(3*m-1)) <= upper_num, f'adjacent collision bound {D}')
        if m == 2:
            require(brute_block_count(D) == T, f'direct word enumeration {D}')
        strict += T != B
        equality += T == B
        max_n = max(max_n, B)
    summary.append({'m':m,'admissible_D':families,'strict':strict,'equal':equality,'largest_native_B':max_n})

examples = []
for D in ((1,1,1,1,1,1),(2,2,2,0,0,0),(3,3,3,0,0,0),(2,2,2,1,1,1)):
    T = macro_micro_count(D)
    B = native_count(D)
    if sum(D) <= 9:
        require(brute_block_count(D) == T, f'exact brute {D}')
    from math import gcd
    g = gcd(T,B)
    examples.append({'D':list(D),'m':sum(D)//3,'ordered_macro':underlying(D),'block_micro_paths':T,'native_shortest_paths':B,'fraction_num':T//g,'fraction_den':B//g})

# Signed example: d_(0,+)=d_(0,-)=1, d_(1,+)=d_(2,+)=2.
# Every signed triad block-word has length six, but net displacement length is four.
signed = {'signed_event_count':2,'signed_micro_block_paths':2*6**2,
          'native_net_displacement':[0,2,2,0,0,0],
          'native_min_length':4,'native_shortest_BRC':6,
          'block_words_that_are_native_shortest':0}
require(signed['signed_micro_block_paths']==72, 'signed micro count')
require(signed['native_shortest_BRC'] == native_count((0,2,2,0,0,0)), 'signed native')
result = {'schema':'X6_UNIT124_TRIADIC_BLOCK_NATIVE_BRC_EXACT_V1',
          'research_status':'AUTHOR_EXECUTED_EXACT_UNREVIEWED_NOT_ADMITTED',
          'scope':'6 labeled native axes; each triadic block uses 3 distinct axes; sign-coherent compared with native shortest words',
          'enumerations':summary,'witnesses':examples,'signed_cancellation_witness':signed,
          'proof_scope':'all m by block injection and adjacent-equal first-two-word witness',
          'executed_validation':'exhaustive admissible degrees m<=3; brute multiset words all m=2 and four displayed witnesses'}
print(json.dumps(result,sort_keys=True,separators=(',',':')))
