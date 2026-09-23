#!/usr/bin/env python3
"""Independent finite partition/erasure checks, without factor/order inputs."""
import argparse
from dataclasses import asdict
from itertools import combinations
from math import gcd
from pathlib import Path
import json
import platform
from random import Random
from statistics import median
from time import perf_counter_ns

from enterprise_math.group_ring_span_erasures import (
    certify_span_erasures, verify_span_erasure_certificate,
    full_interval_threshold, interval_period_threshold, minimum_erasure_span,
    robust_tail_parameters, robust_tail_support, translated_lag_witness, robust_tail_order,
)
from enterprise_math.group_ring_support_design import certify_mark_erasures
from enterprise_math.group_ring_sparse_identifiability import labeled_collision_gcd


def max_identified(mask,A):
    """Independent labeled-pair equality signatures for all1..A and aboveA."""
    s=tuple(i for i in range(A+1) if mask>>i&1)
    signatures=[]
    for r in range(1,A+2):
        bits=0
        for i,x in enumerate(s):
            for j in range(i+1,len(s)):
                if (s[j]-x)%r==0:bits |= 1 << (i*len(s)+j)
        signatures.append(bits)
    seen={};first_bad=A+1
    for r,bits in enumerate(signatures,1):
        if bits in seen:first_bad=min(first_bad,seen[bits],r)
        else:seen[bits]=r
    return first_bad-1


def brute_threshold(s,H,table,protected=()):
    initial=sum(1<<x for x in s)
    allowed=tuple(x for x in s if x not in protected)
    for e in range(len(allowed)+1):
        for F in combinations(allowed,e):
            remaining=initial ^ sum(1<<x for x in F)
            if table[remaining]<H:return e
    return None


def actual_order(n,a):
    r=1;u=a%n
    while u!=1:
        u=u*a%n;r+=1
    return r


def timed(fn,repeats=7):
    expected=fn();times=[]
    for _ in range(repeats):
        t=perf_counter_ns();answer=fn();times.append((perf_counter_ns()-t)/1e6)
        assert answer==expected
    return {'median_ms':median(times),'raw_ms':times}


def validate():
    rng=Random(20260923)
    counts=dict(arbitrary_support_target_cases=0,protected_cases=0,
                fixed_span_old_agreements=0,full_interval_exhaustive_cases=0,
                minimum_span_cases=0,robust_constructions=0,disjoint_lag_witnesses=0,
                actual_modular_cases=0,all_erasure_patterns=0,boundary_necessity_cases=0)
    for A in range(1,10):
        table=[max_identified(mask,A) for mask in range(1<<(A+1))]
        for mask in range(1,1<<(A+1)):
            s=tuple(i for i in range(A+1) if mask>>i&1)
            for H in range(1,A+1):
                out=certify_span_erasures(s,H,A).certificate
                wanted=brute_threshold(s,H,table)
                assert out.minimum_deletions==wanted,(s,H,A,out,wanted)
                counts['arbitrary_support_target_cases']+=1
                if A==H:
                    old=certify_mark_erasures(s,H).certificate
                    assert out.minimum_deletions==old.minimum_deletions
                    counts['fixed_span_old_agreements']+=1
                if H<=A and A-H<=H//2 and out.minimum_deletions is not None:
                    e=A-H
                    if out.minimum_deletions>e:
                        forced=set(range(e+1))|set(range(H,H+e+1))
                        assert forced.issubset(s)
                        counts['boundary_necessity_cases']+=1
            if mask % 5==0:
                H=1+rng.randrange(A)
                P=tuple(x for x in s if rng.randrange(2))
                out=certify_span_erasures(s,H,A,protected=P).certificate
                assert out.minimum_deletions==brute_threshold(s,H,table,P)
                assert verify_span_erasure_certificate(out)
                counts['protected_cases']+=1
        for H in range(1,A+1):
            s=tuple(range(A+1))
            assert full_interval_threshold(A,H)==brute_threshold(s,H,table)
            counts['full_interval_exhaustive_cases']+=1
    for H in range(1,129):
        for e in range(129):
            out=minimum_erasure_span(H,e)
            E=e+1;A=e+max(r*((E+r-1)//r) for r in range(1,H+1))
            assert out.minimum_span==A
            assert full_interval_threshold(A,H)>e
            assert full_interval_threshold(A-1,H)<=e
            assert interval_period_threshold(A-1,out.limiting_period)<=e
            counts['minimum_span_cases']+=1
    for H in range(1,401):
        for e in range(min(4,H//3)+1):
            p=robust_tail_parameters(H,e)
            s=robust_tail_support(H,e);lookup=set(s)
            assert p.span==minimum_erasure_span(H,e).minimum_span
            assert len(s)<=p.mark_upper_bound
            for d in range(H//3+1,H+1):
                pairs=translated_lag_witness(p,d)
                assert all(x in lookup and y in lookup and y-x==d for x,y in pairs)
                assert len({x for xy in pairs for x in xy})==2*(e+1)
                counts['disjoint_lag_witnesses']+=1
            if H<=25:
                assert certify_span_erasures(s,H,p.span).certificate.minimum_deletions==e+1
            counts['robust_constructions']+=1
    for H,e in [(3,1),(6,2),(9,2),(10,3)]:
        s=robust_tail_support(H,e);A=H+e
        for k in range(e+1):
            for F in combinations(s,k):
                mask=sum(1<<x for x in s if x not in F)
                assert max_identified(mask,A)>=H
                counts['all_erasure_patterns']+=1
    for n in range(2,61):
        for a in range(1,n):
            if gcd(a,n)!=1:continue
            r=actual_order(n,a)
            for H,e in [(3,1),(6,2),(12,3)]:
                s=robust_tail_support(H,e)
                patterns=[(),(s[0],),(s[-1],),tuple(rng.sample(s,e))]
                for F in patterns:
                    got=robust_tail_order(n,a,H,e,erased=F)
                    assert got.order==(r if r<=H else None),(n,a,H,e,F,got,r)
                    counts['actual_modular_cases']+=1
    # A concrete lower-bound deletion and a known-order-independent observation.
    failure=certify_span_erasures(tuple(range(12)),6,11).certificate
    assert failure.minimum_deletions==4 and failure.witness_period==4 and failure.alias_period==8
    sizes=[]
    for H in [4096,65536]:
        for e in [0,1,2,3]:
            p=robust_tail_parameters(H,e);s=robust_tail_support(H,e)
            sizes.append({**asdict(p),'marks':len(s),'dense_marks':p.span+1})
    # Same declared erasure-robust query: construction + remove two ends + powers + gcd.
    H,e,n,a=4096,2,100160063,2
    tail=timed(lambda: robust_tail_order(n,a,H,e,erased=(0,H+e)))
    def dense_call():
        s=tuple(x for x in range(H+e+1) if x not in (0,H+e))
        g=labeled_collision_gcd(n,a,s,H+e).gcd_multiple
        return None if g==0 or g>H else g
    dense=timed(dense_call)
    assert robust_tail_order(n,a,H,e,erased=(0,H+e)).order==dense_call()
    return {'schema':'POWER_SPAN_ERASURES_VALIDATION_V1','python':platform.python_version(),
            'platform':platform.platform(),'seed':20260923,'checks':counts,
            'failure_witness':asdict(failure),'construction_sizes':sizes,
            'bounded_query_measurement':{'n':n,'a':a,'H':H,'loss_budget':e,
                'erased':[0,H+e],'sparse':tail,'dense':dense,
                'scope':'construction and exact surviving powers; no classical speedup claim'},
            'scope':'finite tests and self-contained proofs; no full-repository or formal admission'}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',default='results.json')
    args=parser.parse_args();result=validate()
    Path(args.out).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
