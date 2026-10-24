#!/usr/bin/env python3
"""Exact support and boundary-fibre verifier for the R268--R276 BRC auxiliary reset model.
All counts are Python arbitrary-precision nonnegative integers; no numerical limits are inferred.
"""
from collections import defaultdict
from itertools import product
from math import comb
import json

EDGE = (((2, -1, -1), (2, +1, -1)),
        ((0, -1, -1), (0, +1, -1)),
        ((1, +1, +1), (2, +1, -1)))


def path_end(word):
    q, e, k, last, dirty = 0, 1, 0, None, False
    for bit in word:
        nq, eta, b = EDGE[q][bit]
        dirty = dirty or (last == 0 and bit == 0)
        q, e, k, last = nq, eta * e, eta * k + b, bit
    return q, e, e * k, dirty


def atom(sign, a):
    assert a >= (1 if sign == 1 else 2)
    return (1 if sign == 1 else 0, ) + (1,) * (a - 1) + (0, 1)


def witness(n, sign, t):
    assert n >= 9 and (n - t) % 2 == 0
    if sign == 1:
        if t == -(n-2): return atom(1, n-2)
        if t == -(n-4): return atom(1, 1) + atom(1, n-5)
        if t == -(n-6): return atom(1, 1) + atom(1, 1) + atom(1, n-8)
        assert -(n-8) <= t <= n-8
        a1, a2 = (n-4+t)//2, (n-4-t)//2
        return atom(-1, a1) + atom(-1, a2)
    if t == n-2: return atom(-1, n-2)
    if t == n-4: return atom(-1, 2) + atom(+1, n-6)
    assert -(n-8) <= t <= n-6
    a1, a2 = (n-4-t)//2, (n-4+t)//2
    return atom(+1, a1) + atom(-1, a2)


def projected_reset_hist(states):
    res = defaultdict(int)
    for (q, last, dirty, e, k), count in states.items():
        if q == 0 and not dirty:
            res[e, e*k] += count
    return dict(res)


def original_step(state, bit):
    q, last, dirty, e, k = state
    nq, eta, b = EDGE[q][bit]
    return nq, bit, dirty or (last == 0 and bit == 0), eta*e, eta*k+b


def run(max_depth=200, block_depth=75, raw_depth=15):
    # Independent atomic renewal recursion, NOT a relabeling of original DFA.
    block = [defaultdict(int) for _ in range(block_depth+1)]
    block[0][(1,0)] = 1
    for n in range(block_depth+1):
        for (s,t),v in list(block[n].items()):
            for eta in (+1,-1):
                lo = 1 if eta == 1 else 2
                for a in range(lo, block_depth-n-1):
                    dest = n+a+2
                    ns = s*eta
                    block[dest][(ns,t-ns*a)] += v

    states = {(0,None,False,1,0):1}
    small = {}
    support_checks = 0
    witness_checks = 0
    renewal_comparisons = 0
    exact_edge_checks = 0
    raw_words = 0
    result_samples = {}
    for n in range(max_depth+1):
        hist = projected_reset_hist(states)
        assert sum(states.values()) == 2**n, n
        if n <= block_depth:
            assert hist == dict(block[n]), ('independent_renewal', n)
            renewal_comparisons += len(hist)
        if n <= raw_depth:
            raw = defaultdict(int)
            for word in product((0,1),repeat=n):
                q,s,t,dirty = path_end(word)
                if q==0 and not dirty:raw[(s,t)]+=1
            assert hist == dict(raw), ('raw_word_check',n)
            raw_words += 2**n
        if n < 9:
            small[str(n)] = {str(s):sorted(t for (e,t) in hist if e==s) for s in (+1,-1)}
        else:
            expected = {(1,t) for t in range(-n+2,n-7,2)}
            expected |= {(-1,t) for t in range(-n+8,n-1,2)}
            assert set(hist)==expected,('support',n)
            assert len(hist)==2*(n-4)
            k_expected = set(range(-n+2,n-7,2))
            assert all({s*t for (e,t) in hist if e==s}==k_expected for s in (+1,-1)),('both_signs_equal_k_support',n)
            support_checks += len(hist)
            if n <= 120:
                for sign,t in sorted(expected):
                    w=witness(n,sign,t)
                    assert len(w)==n
                    assert path_end(w)==(0,sign,t,False),('witness',n,sign,t)
                    witness_checks += 1
            for r in (1,2,3):
                if n >= 3*r:
                    assert hist.get((1,-n+2*r),0)==comb(n-2*r-1,r-1),(n,r,'plus')
                    exact_edge_checks += 1
            if n >= 12:
                assert hist[(1,-n+8)] == comb(n-9,3)+1, ('fourth plus layer', n)
                exact_edge_checks += 1
            if n>=4:
                assert hist[(-1,n-2)]==1
                exact_edge_checks += 1
            if n>=7:
                assert hist[(-1,n-4)]==n-6
                exact_edge_checks += 1
            if n>=10:
                assert hist[(-1,n-6)]==comb(n-8,2)+1
                exact_edge_checks += 1
            if n in (9,12,20,40,75,120,200):
                vmax=max(hist.values())
                result_samples[str(n)]={'support_size':len(hist), 'reset_total':str(sum(hist.values())),
                          'peak_count':str(vmax),'peak_effects':[[s,s*t] for (s,t),v in hist.items() if v==vmax]}
        if n == max_depth:break
        nxt=defaultdict(int)
        for st,v in states.items():
            for bit in (0,1):
                nxt[original_step(st,bit)]+=v
        states=nxt
    return {'schema':'R277_CLEAN_RESET_SUPPORT_EXACT_V1','status':'PASS',
        'model':'R276 original positive-weight ordered-word BRC, full affine effect g=(epsilon,k)',
        'derived_tag':'t=epsilon*k',
        'analytic_claim': 'For n>=9, clean q0 support is BOTH eps signs for every k=-n+2,-n+4,...,n-8 (k=eps*t); exactly 2(n-4) full effects.',
        'finite_independent_checks': {'raw_words_n_0_to_15':raw_words,
           'independent_atomic_DP_depth_0_to':block_depth,
           'compared_positive_atomic_coefficients':renewal_comparisons,
           'original_DFA_DP_depth_0_to':max_depth,
           'verified_support_effects_n_9_to_200':support_checks,
           'independent_constructed_witnesses_n_9_to_120':witness_checks,
           'exact_boundary_coefficients_checked':exact_edge_checks},
        'small_n_complete_supports':small,
        'samples':result_samples,
        'infinite_scope_requires_proof_not_finite_extrapolation':True,
        'original_enterprise_math_package_executed':False,
        'native_P000_X6_dynamics_claimed':False,
        'driver_review':'NOT_PERFORMED'}


if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
