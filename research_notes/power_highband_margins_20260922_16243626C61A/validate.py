#!/usr/bin/env python3
"""Reproduce finite checks and fair support-certification benchmarks, offline."""
from __future__ import annotations
import argparse
from dataclasses import asdict
from fractions import Fraction as F
import hashlib
from itertools import combinations, product
import json
from math import gcd
from pathlib import Path
import platform
from random import Random
from statistics import median
from time import perf_counter_ns
import tracemalloc
from types import MappingProxyType

from enterprise_math.group_ring_sparse_identifiability import (
    period_closures, structural_alias, sparse_ruler, compile_sparse_codebook, difference_set,
    collision_spectrum, SparseCollisionCodebook,
)
from enterprise_math.group_ring_support_certificates import (
    certify_runs, certify_support, verify_support_certificate, support_runs, high_band_identifiable,
    order_from_certified_support, support_mark_lower_bound,
    certify_readout_margin, decode_bounded_readout,
)

ROOT = Path(__file__).resolve().parents[2]
OLD = ROOT/'src/enterprise_math/group_ring_sparse_identifiability.py'
BLOB = '35567d80b1b0f1bb864f381cc0ee7b4613d0273a'


def encode(value):
    if isinstance(value, F):
        return {'numerator': value.numerator, 'denominator': value.denominator}
    raise TypeError(type(value).__name__)


def measure(call):
    call()
    times = []
    for _ in range(7):
        start = perf_counter_ns(); result = call(); times.append(perf_counter_ns()-start)
    tracemalloc.start(); result = call(); _, peak = tracemalloc.get_traced_memory(); tracemalloc.stop()
    return {'median_ms': median(times)/1e6, 'peak_python_bytes': peak, 'result': result}


def validate(out):
    b = OLD.read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest() == BLOB
    counts = dict(arbitrary_lag_sets=0, supports=0, negative_aliases=0,
                  randomized_supports=0, actual_group_cases=0, noise_box_checks=0,
                  erasure_subsets_checked=0)
    for H in range(1, 17):
        required = set(range(H//3+1, H+1))
        for mask in range(1 << H):
            D = {x+1 for x in range(H) if mask >> x & 1}
            original = all(gcd(*[d for d in D if d % r == 0]) == r for r in range(1,H+1))
            assert original == (required <= D)
            counts['arbitrary_lag_sets'] += 1
    for H in range(1,13):
        for mask in range(1, 1 << (H+1)):
            S = tuple(x for x in range(H+1) if mask >> x & 1)
            result = certify_support(S, H); cert = result.certificate
            assert verify_support_certificate(cert)
            labels = period_closures(S,H)
            truth = labels == tuple(range(1,H+1))+(0,)
            assert (cert.status == 'IDENTIFYING') == truth
            if cert.alias:
                a,b = cert.alias
                assert labels[a-1] == labels[b-1]
                counts['negative_aliases'] += 1
            else:
                assert len(S) >= support_mark_lower_bound(H)
            counts['supports'] += 1
    rng = Random(20260922)
    for _ in range(500):
        H = rng.randrange(20,1001)
        S = tuple(sorted(rng.sample(range(H+1), rng.randrange(2,min(H+1,100)))))
        cert = certify_support(S,H).certificate
        assert verify_support_certificate(cert)
        assert (cert.status == 'IDENTIFYING') == (structural_alias(S,H) is None)
        counts['randomized_supports'] += 1
    for H in (3,6,9,20,64):
        S = (0,1,5,7,9) if H == 9 else sparse_ruler(H)
        cert = certify_support(S,H).certificate
        for n in range(2,102):
            for a in range(1,n):
                if gcd(a,n) != 1: continue
                z=a; r=1
                while z != 1: z=z*a%n; r+=1
                got=order_from_certified_support(n,a,S,cert)
                assert got.order == (r if r<=H else None)
                assert (got.lower_bound==H+1) if r>H else (got.lower_bound==r)
                counts['actual_group_cases'] += 1
    margins=[]
    for H in (6,12,32,64):
        for alphabet in ('large','binary'):
            book=compile_sparse_codebook(H,alphabet=alphabet).codebook
            assert book is not None
            cert=certify_readout_margin(book)
            assert cert.status=='COMPLETE' and cert.minimum_gap>0
            totals=[sum(w)**2 for w in book.profiles]
            codes=[tuple(F(v,totals[j]) for j,v in enumerate(row)) for row in book.codes]
            epsilon=cert.minimum_gap/3
            # Every candidate, selected extreme corners (all corners for <=5 channels).
            for r,row in enumerate(codes,1):
                for signs in product((-1,1), repeat=min(5,len(row))):
                    query=tuple(v+(signs[j]*epsilon if j<len(signs) else 0) for j,v in enumerate(row))
                    got=decode_bounded_readout(book,query,epsilon)
                    assert got.candidates==(r,)
                    counts['noise_box_checks']+=1
            if len(book.profiles)>1:
                ec=certify_readout_margin(book,erased_channels=1)
                i,j=ec.critical_pair
                query=tuple((x+y)/2 for x,y in zip(codes[i-1],codes[j-1]))
                got=decode_bounded_readout(book,query,ec.minimum_gap/2,erased=ec.critical_erased)
                assert i in got.candidates and j in got.candidates
                if H<=12:
                    for E in combinations(range(len(book.profiles)),1):
                        direct=min(max(abs(codes[i][j]-codes[k][j]) for j in range(len(codes[0])) if j not in E)
                                   for i,k in combinations(range(len(codes)),2))
                        assert direct>=ec.minimum_gap
                        counts['erasure_subsets_checked']+=1
            else:
                baseline=codes[-1][0]
                assert cert.minimum_gap<=(1-baseline)/H
            margins.append({'H':H,'alphabet':alphabet,'marks':len(book.support),
                            'channels':len(book.profiles),'margin':asdict(cert)})
    bench=[]
    for H in (4096,16384,65536):
        S=sparse_ruler(H)
        def old(): return structural_alias(S,H) is None
        def direct_band():
            return high_band_identifiable(S,H)
        def new():
            cert=certify_support(S,H).certificate
            return verify_support_certificate(cert) and cert.status=='IDENTIFYING'
        result=certify_support(S,H)
        def verify(): return verify_support_certificate(result.certificate)
        row={'H':H,'marks':len(S),'runs':len(result.certificate.runs),
             'run_pairs':result.evaluated_run_pairs,'published_witness_pairs':len(result.certificate.cover),
             'old_divisor_sweep':measure(old),'direct_high_band':measure(direct_band),'new_construct_and_verify':measure(new),
             'warm_verify_only_setup_excluded':measure(verify)}
        assert row['old_divisor_sweep']['result'] and row['new_construct_and_verify']['result']
        bench.append(row)
    H=10**30+2; b=(H+2)//3
    result=certify_runs(((0,b),(H-b,H)),H)
    assert verify_support_certificate(result.certificate)
    result_data={'status':'RESEARCH_CANDIDATE_NOT_ADMITTED','environment':platform.python_version(),
                 'unchanged_reference_blob':BLOB,'checks':counts,'benchmarks':bench,'margins':margins,
                 'symbolic_large_horizon':{'H':H,'run_count':2,'represented_marks':2*(b+1),
                      'run_pairs':result.evaluated_run_pairs,'witness_pairs':len(result.certificate.cover),
                      'scope':'Support certification only; no represented modular powers were generated.'},
                 'timing_scope':'Same boolean identifiability answer, fixed preexisting support input. Seven calls after warmup; setup included in new construct+verify. Tracing separate, not RSS.'}
    out.write_text(json.dumps(result_data,ensure_ascii=False,indent=2,default=encode)+'\n')
    print(json.dumps(result_data,ensure_ascii=False,indent=2,default=encode))


if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--out',type=Path,default=Path('results.json'))
    validate(parser.parse_args().out)
