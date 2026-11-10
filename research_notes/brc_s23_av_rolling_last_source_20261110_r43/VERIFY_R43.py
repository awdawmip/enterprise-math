#!/usr/bin/env python3
"""R43: certified rolling last-source vectors for an irrational circle observer.
Frozen R41/R42 references are required in the same directory; see PR #1983.
Only labelled auxiliary circle-observer mathematics, not native X6 dynamics.
"""
from __future__ import annotations
from bisect import bisect_right
from fractions import Fraction
from math import lcm
from pathlib import Path
import hashlib
import json

from VERIFY_R42 import recurrence_selector, Uncertified, FREEZE
import REFERENCE_R41 as ref


def rolling_window(lo:Fraction,hi:Fraction,m:int,J:int,N:int,K:int,init_budget:int|None=None):
    """Certified rolling updates of every labelled last source, including expiry repairs."""
    assert 0<lo<=hi<1 and m>=2 and N>=1 and K>=0
    tau,initial=recurrence_selector(lo,hi,m,J,N,budget=init_budget)
    D=lcm(lo.denominator,hi.denominator)
    A=lo.numerator*(D//lo.denominator)
    B=hi.numerator*(D//hi.denominator)
    q=2*D;u=A+B;delta=B-A
    historical=sorted(((z*u)%q,z) for z in range(m))
    residue=[a for a,_ in historical]
    assert len(set(residue))==m
    r=(J*u)%q
    results=[list(tau)]
    stat={'initial_scan':initial['scan'],'initial_fallback_owners':initial['fallback_owners'],
          'initial_historical_product_mods':initial['historical_integer_product_remainders'],
          'new_source_product_mods':1,'step_phase_additions':0,'new_source_owner_certificates':0,
          'new_source_owner_boundary_checks':0,'expired_maxima':0,
          'selective_repair_queries':0,'selective_repair_floors':0,
          'full_window_rescans':0,'num_window_transitions':K}
    ages=[max((J-t for t in results[-1] if t is not None),default=0)]
    for step in range(K):
        t=J+step
        k=(bisect_right(residue,r)-1)%m
        a=historical[k][1];b=historical[(k+1)%m][1]
        left=(r-residue[k])%q
        right=(residue[(k+1)%m]-r)%q
        gap=(residue[(k+1)%m]-residue[k])%q
        assert left+right==gap
        if not ((left>delta*abs(t-a) or (t==a and left==0)) and right>delta*abs(t-b)):
            raise Uncertified(('rolling-new-source',t,left,right))
        stat['new_source_owner_certificates']+=1
        stat['new_source_owner_boundary_checks']+=2
        tau[k]=t
        nextJ=t+1
        earliest=nextJ-N
        expired=[i for i,v in enumerate(tau) if v is not None and v<earliest]
        assert len(expired)<=1,(step,expired)
        if expired:
            i=expired[0]
            stat['expired_maxima']+=1
            core=ref.CoboundarySelector(ref.Observer(lo,hi,m),nextJ,N)
            repair,counters=core.solve([i])
            tau[i]=repair[i]
            stat['selective_repair_queries']+=1
            stat['selective_repair_floors']+=counters['certified_scalar_floor_evaluations']
        assert all(x is None or earliest<=x<nextJ for x in tau)
        results.append(list(tau))
        ages.append(max((nextJ-v for v in tau if v is not None),default=0))
        if step+1<K:
            r+=u
            if r>=q:r-=q
            stat['step_phase_additions']+=1
    return results,stat,ages


def audit_case(name,lo,hi,m,J,N,K,budget=None,oracle_all=True,bruteforce=False):
    result,stats,ages=rolling_window(lo,hi,m,J,N,K,budget)
    obs=ref.Observer(lo,hi,m)
    checked=0
    for s,got in enumerate(result):
        j=J+s
        if oracle_all:
            expected,calls=ref.independent_last(obs.arcs,j-N,j,obs.mid)
        else:
            expected=recurrence_selector(lo,hi,m,j,N,budget)[0]
        assert got==expected,(name,s,[(i,g,e) for i,(g,e) in enumerate(zip(got,expected)) if g!=e][:5])
        if bruteforce:
            assert got==ref.brute(obs,j,N),(name,s,'brute error')
        checked+=1
    initialH=ages[0]
    if initialH+K<=N and all(x is not None for x in result[0]):
        assert stats['selective_repair_queries']==0
    return {'name':name,'m':m,'J':J,'N':N,'K':K,'oracle':'Euclidean floor sum' if oracle_all else 'independent R42',
            'checked_vectors':checked,'checked_owner_slots':checked*m,
            'initial_max_source_age':initialH,'final_max_source_age':ages[-1],
            'max_age_in_stream':max(ages),'stats':stats,
            'last_vector_sha256':hashlib.sha256(json.dumps(result[-1],separators=(',',':')).encode()).hexdigest()}


def main():
    s23=(Fraction(262204504569236716045286,10**24),Fraction(262204504569236716045287,10**24))
    sqrt2=tuple(x-1 for x in ref.sqrt_enclose(2))
    sqrt3=tuple(x-1 for x in ref.sqrt_enclose(3))
    cases=[
        ('S23_TRILLION_32',*s23,128,10**12+128,10**9,32,None,True,False),
        ('SQRT2_M16_64',*sqrt2,16,10**9,10**8,64,None,True,False),
        ('SQRT2_M257_12',*sqrt2,257,10**9,10**8,12,None,True,False),
        ('SQRT3_M32_32',*sqrt3,32,10**8,10**7,32,None,True,False),
        ('NEAR_THIRD_M21_12',*ref.theta_pair(1,3,2,10**7),21,10**9,10**8,12,None,True,False),
        ('MIXED_M257_8',*ref.theta_pair(1,3,2,1000),257,10**9,10**8,8,None,False,False),
        ('SHORT_M16_N5_80',*sqrt2,16,100,5,80,5,True,True),
        ('SHORT_M16_N16_80',*sqrt2,16,100,16,80,16,True,True),
        ('SHORT_M16_N120_80',*sqrt2,16,320,120,80,45,True,True),
        ('NEGATIVE_M16_N12_60',*sqrt2,16,-30,12,60,12,True,True),
        ('HISTORICAL_M16_N16_20',*sqrt2,16,16,16,20,16,True,True),
    ]
    results=[]
    for case in cases:
        ans=audit_case(*case)
        results.append(ans)
        print('PASS',ans['name'],'vectors',ans['checked_vectors'],'repairs',ans['stats']['selective_repair_queries'],'new owner certs',ans['stats']['new_source_owner_certificates'],flush=True)
    assert any(x['stats']['selective_repair_queries']>0 for x in results)
    assert results[0]['stats']['selective_repair_queries']==0
    evidence={'pin':FREEZE,'scope':'auxiliary circle observer, half-open labelled historical arcs',
              'status':'author-side exact finite regression; independent review pending',
              'theorem':'rolling last survivor; at most one expired label per incoming source',
              'cases':results,'pass':'PASS_R43_ROLLING_LABELLED_LAST_SOURCE_11_CASES'}
    Path(__file__).with_name('CERTIFICATE_R43.json').write_text(json.dumps(evidence,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf8')
    print(evidence['pass'])

if __name__=='__main__':main()
