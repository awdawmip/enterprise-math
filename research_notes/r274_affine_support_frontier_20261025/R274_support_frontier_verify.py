#!/usr/bin/env python3
"""Exact verification for R274 support-frontier theorem, formal BRC only.

No floating-point arithmetic. Not a native Enterprise Math X6 execution.
"""
import json
from collections import defaultdict
from itertools import product

EDGES = {
    0: ((2, -1, -1), (2, +1, -1)),
    1: ((0, -1, -1), (0, +1, -1)),
    2: ((1, +1, +1), (2, +1, -1)),
}
DELTA = ((1, 0), (2, 0), (2, 2))
# For n>=10: k in {-n+lo,-n+lo+2,...,n+hi}, both sign values.
INTERVALS = {
    (0, 0): (2, -8),
    (0, 2): (4, -4),
    (1, 1): (2, -6),
    (1, 2): (4, -4),
    (2, 0): (0, -6),
    (2, 1): (8, -4),
    (2, 2): (2, -6),
}

def step(state, bit):
    q, r, eps, k = state
    q1, eta, b = EDGES[q][bit]
    return (q1, DELTA[r][bit], eta * eps, eta * k + b)

def propagate(counts):
    nxt = defaultdict(int)
    for state, amount in counts.items():
        for bit in (0, 1):
            nxt[step(state, bit)] += amount
    return nxt

def support_interval(n, pair):
    lo, hi = INTERVALS[pair]
    return set(range(-n + lo, n + hi + 1, 2))

def pure_nonhit(counts):
    channels = defaultdict(lambda: [0, 0])
    for (q, r, eps, k), amount in counts.items():
        channels[(q, eps, k)][int(r == 2)] += amount
    return {key: ab[0] for key, ab in channels.items() if ab[0] and not ab[1]}

def expected_pure(n):
    return {(q, eps, k): 1
            for eps in (-1, 1)
            for q, k in ((0, 2-n), (1, 2-n), (2, -n), (2, n-4))}

def certify_interval_induction():
    # Every incoming image at depth n+1 has shape [-n+L,n+R] step 2.
    incoming = defaultdict(list)
    for (q,r),(lo,hi) in INTERVALS.items():
        for bit, (q1, eta, bias) in enumerate(EDGES[q]):
            r1 = DELTA[r][bit]
            assert (q1,r1) in INTERVALS
            if eta == 1:
                pair = (lo + bias, hi + bias)
            else:
                pair = (-hi + bias, -lo + bias)
            incoming[(q1,r1)].append(pair)
    assert set(incoming) == set(INTERVALS)
    for target, terms in incoming.items():
        want_lo, want_hi = INTERVALS[target]
        assert min(left for left,right in terms) == want_lo-1
        assert max(right for left,right in terms) == want_hi+1
        n=10
        formed=set()
        for left,right in terms:
            assert -n+left <= n+right
            formed.update(range(-n+left, n+right+1, 2))
        assert formed == support_interval(n+1,target)
    return {f'{q},{r}': terms for (q,r),terms in sorted(incoming.items())}

def verify(N=128):
    induction = certify_interval_induction()
    counts={(0,0,1,0):1}
    samples={}
    checked_words=0
    for n in range(N+1):
        assert sum(counts.values()) == 2**n
        if n<=12:
            enum=defaultdict(int)
            for bits in product((0,1), repeat=n):
                state=(0,0,1,0)
                for bit in bits:state=step(state,bit)
                enum[state]+=1
            assert dict(enum)==dict(counts)
            checked_words+=2**n
        if n>=10:
            have=defaultdict(set)
            for (q,r,eps,k) in counts:
                have[(q,r,eps)].add(k)
            assert set(have)=={(q,r,eps) for (q,r) in INTERVALS for eps in (-1,1)}
            for pair in INTERVALS:
                for eps in (-1,1):
                    assert have[(*pair,eps)] == support_interval(n,pair)
            for eps in (-1,1):
                for q,r,k in ((0,0,2-n),(1,1,2-n),(2,0,-n),(2,1,n-4)):
                    assert counts.get((q,r,eps,k)) == 1
        if n>=5:
            assert pure_nonhit(counts) == expected_pure(n)
        if n in (4,5,6,10,12,20,40,80,128):
            samples[str(n)]={
                'path_total':str(sum(counts.values())),
                'pure_nonhit_fibers':len(pure_nonhit(counts)),
                'pure_nonhit_total_mass':sum(pure_nonhit(counts).values()),
                'reachable_full_states':len(counts),
            }
        if n<N:counts=propagate(counts)
    return {
      'result':'PASS','formal_model_only':True,'native_X6_execution':'NOT_RUN',
      'exact_depth_max':N,'bruteforce_raw_words_checked':checked_words,
      'induction_interval_images':induction,'samples':samples,
      'proven_claim':'all n>=5 have exactly eight pure-nohit (q,eps,k) fibers of mass one; all n>=10 have exact interval supports in every reachable (q,r,eps) carrier'
    }

if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
