#!/usr/bin/env python3
"""R42: integer-recurrence certified suffix source ownership for circle rotations.
Independent reference: pinned R41 exact Euclidean floor-sum implementation.
This is an auxiliary interval/observer computation, not native X6 dynamics.
"""
from __future__ import annotations
from bisect import bisect_right
from fractions import Fraction
from math import lcm
import hashlib, json
from pathlib import Path
from time import perf_counter_ns

import REFERENCE_R41 as ref

FREEZE = '43ec6098b1330ae86d0a7863be336c5d97f6ef34'

class Uncertified(ValueError):
    pass


def recurrence_selector(lo:Fraction, hi:Fraction, m:int, J:int, N:int, budget:int|None=None):
    """Return certified last-source vector (possibly partially via R40 fallback).

    Fraction enclosure [lo,hi] may use unequal denominators; do all
    phase comparisons using fixed-width integers, no floating point.
    """
    if not (0 < lo <= hi < 1 and m >= 2 and N >= 1):
        raise ValueError('invalid input')
    D=lcm(lo.denominator, hi.denominator)
    lower=lo.numerator*(D//lo.denominator)
    upper=hi.numerator*(D//hi.denominator)
    q=2*D; u=lower+upper; delta=upper-lower
    assert 0 < u < q
    historical=sorted(((z*u)%q,z) for z in range(m))
    residues=[x for x,_ in historical]
    # Invariant: cyclic historical owner order is fixed over the whole enclosure.
    for k in range(m):
        x,a=historical[k];y,b=historical[(k+1)%m]
        gap=(y-x)%q
        if not (gap>delta*abs(b-a) and q-gap>delta*abs(b-a)):
            raise Uncertified(('historical-order',k,a,b))
    if budget is None:budget=4*m
    if budget<0:raise ValueError('negative scan budget')
    H=min(N,budget)
    r=((J-1)*u)%q
    found=[None]*m
    seen=0; scanned=0; certchecks=0; recurrent_updates=0
    for age in range(1,H+1):
        t=J-age
        k=(bisect_right(residues,r)-1)%m
        a=historical[k][1]; b=historical[(k+1)%m][1]
        left=(r-residues[k])%q
        right=(residues[(k+1)%m]-r)%q
        gap=(residues[(k+1)%m]-residues[k])%q
        certchecks+=2
        if not (left+right==gap and (left>delta*abs(t-a) or (t==a and left==0)) and right>delta*abs(t-b)):
            raise Uncertified(('source-near-owner-boundary',age,t,k,left,right))
        if found[k] is None:
            found[k]=t;seen+=1
        scanned=age
        if seen==m:break
        r-=u
        if r<0:r+=q
        recurrent_updates+=1
    stat={'scan':scanned,'seen':seen,'certified_owner_boundaries':certchecks,
          'initial_large_product_remainders':1, 'recurrence_modular_subtractions':recurrent_updates,
          'source_phase_fraction_multiplications':0,
          'historical_integer_product_remainders':m,
          'certified_scalar_floors_fallback':0,'fallback_owners':0}
    if seen==m or scanned==N:
        return found,stat
    obs=ref.Observer(lo,hi,m)
    selector=ref.CoboundarySelector(obs,J,N)
    missing=[i for i,a in enumerate(found) if a is None]
    # historical arrays use same cyclic rank as Observer's midpoint sorting
    assert [z for _,z in historical]==obs.order
    more,counters=selector.solve(missing)
    for k in missing:found[k]=more[k]
    stat['fallback_owners']=len(missing)
    stat['certified_scalar_floors_fallback']=counters['certified_scalar_floor_evaluations']
    return found,stat


def direct_full_fraction_scan(lo,hi,m,J,N,budget):
    # R41 exact predecessor, used to compare work and output.
    from REFERENCE_R41 import r41_hybrid
    return r41_hybrid(lo,hi,m,J,N,budget=budget)


def check_case(name,lo,hi,m,J,N,budget, independent=True):
    got,stat=recurrence_selector(lo,hi,m,J,N,budget)
    baseline,base_stat=direct_full_fraction_scan(lo,hi,m,J,N,budget)
    assert got==baseline,(name,'R41 mismatch')
    obs=ref.Observer(lo,hi,m)
    if independent:
        ref_values,calls=ref.independent_last(obs.arcs,J-N,J,obs.mid)
        assert got==ref_values,(name,'Euclidean floor sum mismatch')
    else:calls=None
    if N<=700:
        assert got==ref.brute(obs,J,N),(name,'brute mismatch')
    return dict(name=name,m=m,J=J,N=N,budget=budget,
                last_age_max=max((J-v for v in got if v is not None),default=None),
                last_age_none=sum(x is None for x in got),
                r42=stat,r41=base_stat,euclidean_reference_queries=calls,
                last_source_sha256=hashlib.sha256(json.dumps(got,separators=(',',':')).encode()).hexdigest())


def benchmarks(case,repeat=5):
    name,lo,hi,m,J,N,budget=case
    tA=[];tB=[]
    for _ in range(repeat):
        a=perf_counter_ns();recurrence_selector(lo,hi,m,J,N,budget);tA.append(perf_counter_ns()-a)
        b=perf_counter_ns();direct_full_fraction_scan(lo,hi,m,J,N,budget);tB.append(perf_counter_ns()-b)
    return {'case':name,'ns_median_r42':sorted(tA)[repeat//2], 'ns_median_r41':sorted(tB)[repeat//2]}


def main():
    s23=(Fraction(262204504569236716045286,10**24),Fraction(262204504569236716045287,10**24))
    cases=[('S23_M128_1e12',*s23,128,10**12+128,10**9,4*128),
           ('SQRT2_M16',*ref.theta_pair(0,1,2,1),16,10**9,10**8,4*16)]
    # sqrt2-1, valid theta in (0,1)
    cases[1]=('SQRT2_M16',*(x-1 for x in ref.sqrt_enclose(2)),16,10**9,10**8,4*16)
    cases+= [('SQRT2_M257',*(x-1 for x in ref.sqrt_enclose(2)),257,10**9,10**8,4*257),
             ('NEAR_THIRD_M21',*ref.theta_pair(1,3,2,10**7),21,10**9,10**8,4*21),
             ('MIXED_M257',*ref.theta_pair(1,3,2,1000),257,10**9,10**8,4*257),
             ('SHORT_M16',*(x-1 for x in ref.sqrt_enclose(2)),16,320,120,45),
             ('HISTORICAL_M16',*(x-1 for x in ref.sqrt_enclose(2)),16,16,16,16),
             ('NEGATIVE_M16',*(x-1 for x in ref.sqrt_enclose(2)),16,-30,80,80)]
    results=[];bench=[]
    for case in cases:
        result=check_case(*case)
        results.append(result)
        bench.append(benchmarks(case,repeat=3))
        print('PASS',case[0],result['r42'],flush=True)
    # The certification is strict: a broad enclosure must not be sold as exact.
    coarse_refused=False
    try:recurrence_selector(Fraction(2,5),Fraction(21,50),16,10**9,10**8,64)
    except Uncertified:coarse_refused=True
    assert coarse_refused,'must reject unrefined enclosure'
    deterministic={'scientific_input_pin':FREEZE,'method':'R42_INTEGER_PHASE_RECURRENCE_CERTIFIED',
                   'cases':results,'coarse_enclosure_refused':coarse_refused,
                   'status':'AUTHOR_EXACT_TESTS_PASS_NOT_INDEPENDENTLY_REVIEWED'}
    output=Path(__file__).with_name('CERTIFICATE_R42.json')
    output.write_text(json.dumps(deterministic,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    Path(__file__).with_name('BENCHMARK_R42.json').write_text(json.dumps(bench,indent=2)+'\n')
    print('PASS_R42_CERTIFIED_RECURRENCE_8_FAMILIES_AND_COARSE_REJECTION')
if __name__=='__main__':main()
