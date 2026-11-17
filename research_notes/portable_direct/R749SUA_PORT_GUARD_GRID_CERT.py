#!/usr/bin/env python3
"""Exact rational BRC one-port feedback stability-guard certificate.

Frozen science context: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Only finite positive-rational recurrent port contexts (WBRC-T30/T31) are used.
"""
from fractions import Fraction as F
from itertools import combinations
import json


def spectral_stable_2x2(w, c):
    """Exact Perron criterion of [[w,c],[1,0]] for 0<=w<1, c>=0."""
    assert F(0) <= w < 1 and c >= 0
    return 1 - w - c > 0


def guard_vector(w, K):
    return tuple(spectral_stable_2x2(w, F(j, K)) for j in range(1, K))


def adaptive_identify(w, K):
    """Binary searches bin index using only guard feedbacks j/K."""
    lo, hi, probes = 0, K, []
    while hi - lo > 1:
        mid = (lo + hi) // 2
        j = K - mid
        ans = spectral_stable_2x2(w, F(j, K))
        probes.append([j, ans])
        if ans:
            hi = mid
        else:
            lo = mid
    return lo, probes


def adaptive_budget_identify(w, K, M):
    """Binary searches the M+1 feedback-budget classes, 1<=M<K."""
    lo, hi, probes = 0, M+1, []
    while hi-lo>1:
        mid=(lo+hi)//2
        j=M-mid+1
        ans=spectral_stable_2x2(w,F(j,K))
        probes.append([j, ans])
        if ans:
            hi=mid
        else:
            lo=mid
    return lo,probes

def representative_values(K):
    # All class boundaries plus two strict interior rationals per bin.
    vals = set()
    for k in range(K):
        vals.add(F(k, K))
        vals.add(F(4 * k + 1, 4 * K))
        vals.add(F(4 * k + 3, 4 * K))
    return sorted(vals)


def run():
    records = []
    total_samples = total_probes = pattern_tests = budget_cases = 0
    for K in range(2, 33):
        bins = set()
        for w in representative_values(K):
            k = (w.numerator * K) // w.denominator
            vec = guard_vector(w, K)
            expected = tuple(j < K-k for j in range(1, K))
            assert vec == expected, (K, w, vec, expected)
            index, probes = adaptive_identify(w, K)
            assert index == k
            assert len(probes) <= (K-1).bit_length()
            bins.add((k, vec))
            total_samples += 1
            total_probes += len(probes)
        # Every bounded budget M/K has M+1 exact observable classes.
        for M in range(1,K):
            found=set()
            for w in representative_values(K):
                k=(w.numerator*K)//w.denominator
                expected_class=max(0,k-(K-M-1))
                pattern=tuple(spectral_stable_2x2(w,F(j,K)) for j in range(1,M+1))
                assert pattern==tuple(j<=M-expected_class for j in range(1,M+1))
                answer,probes=adaptive_budget_identify(w,K,M)
                assert answer==expected_class
                assert len(probes)<=(M).bit_length()
                found.add((expected_class,pattern))
                budget_cases+=1
            assert len(found)==M+1
        assert len(bins) == K
        assert len({v for _,v in bins}) == K
        # For *every* strict subset of at most 3 grid tests, at most m+1
        # patterns occur. This is a finite regression, not the universal proof.
        for m in range(0, min(2, K-1)+1):
            for tests in combinations(range(1,K), m):
                patterns={tuple(spectral_stable_2x2(F(k,K),F(j,K)) for j in tests) for k in range(K)}
                assert len(patterns)==m+1, (K,m,tests,len(patterns))
                pattern_tests+=1
        records.append({"K":K,"bins":K,"nonadaptive_min_probes":K-1,
                        "adaptive_min_worst_case_probes":(K-1).bit_length()})
    # Two explicit positive-rational recurrent modules with the same K=4
    # grid stability observations but different effective ports.
    a=F(0); x=F(1,4); y=F(1,4)
    w1=F(1,16)+y*x/(1-a)
    w2=F(1,8)+y*x/(1-a)
    assert (w1,w2)==(F(1,8),F(3,16))
    assert guard_vector(w1,4)==guard_vector(w2,4)
    separating_c=1-(w1+w2)/2
    assert separating_c==F(27,32)
    assert spectral_stable_2x2(w1,separating_c)
    assert not spectral_stable_2x2(w2,separating_c)
    assert all(spectral_stable_2x2(w,c)==(w+c<1)
               for w in representative_values(8)
               for c in (F(0),F(1,8),F(1,2),F(7,8),F(1)))
    result={"result":"PASS","arithmetic":"exact rational (Python fractions)",
            "tested_K":"2..32 inclusive", "sampled_effective_ports":total_samples,
            "adaptive_probe_executions":total_probes,
            "nonadaptive_subsets_checked":pattern_tests,
            "bounded_budget_sample_checks":budget_cases,
            "module_witness":{"w1":"1/8","w2":"3/16","grid_K":4,
                "guard_grid_equal":True,"separating_feedback":"27/32"},
            "uniform_formulas":{
                "grid_equivalence":"floor(K*w) equal",
                "classes":"M+1 for feedback j/K, j=1..M, 1<=M<K; K when M=K-1",
                "optimal_nonadaptive_tests":"M (K-1 for full grid)",
                "optimal_adaptive_worst_case":"ceil(log2(M+1))"},
            "scope":"finite tests supplement, do not prove, universal positive-rational algebra",
            "per_K":records}
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':
    run()
