#!/usr/bin/env python3
"""Exact, finite checks for X6 time Unit229: static root lineage vs candidate cochain.
No physical transition law is assumed or simulated; only declared C12 OUTER
oriented halfturn provenance and P_rot finite readouts are used.
"""
import json
from math import gcd
from pathlib import Path

OUT = Path(__file__).with_name('X6_TIME_STATIC_ROOT_VS_WINDING_COCHAIN_RESULTS_20261121.json')

def gamma(q, k):
    return 3*((q+k)//6-q//6)

def order(x, n):
    return n//gcd(x, n)

def main():
    data = {
        'schema': 'X6_UNIT229_EXACT_FINITE_CERTIFICATE_V1',
        'scope': 'frozen OUTER C12 Cell starts E_k=2k, k modulo 6; principal relative root section Sigma=3epsilon is fixed along same-chirality physical Cell successor, while Gamma is a separately postulated cochain',
        'checked_levels': list(range(7)),
        'checked_lengths': list(range(-24,25)),
        'mismatches': [],
        'counts': {'cocycle':0,'even_start_two_step':0,'halfturn':0,'full_loop':0,'winding_quotient':0,'C24_order':0},
        'samples': {},
    }
    c=data['counts']
    # Exact cocycle in broad signed range, verifying the scope's finite test only.
    for q in range(12):
        for a in range(-12,13):
            for b in range(-12,13):
                c['cocycle']+=1
                if gamma(q,a+b)!=gamma(q,a)+gamma((q+a)%12,b):
                    data['mismatches'].append(['cocycle',q,a,b])
    for k in range(6):
        q=2*k
        for eps in (-1,1):
            # Source: principal relative-root marker is unchanged when moving the same-chirality arc's start one Cell forward.
            # Difference of Sigma is zero, but Gamma of two positive physical microsteps is sometimes nonzero.
            dg=gamma(q,2)
            c['even_start_two_step']+=1
            if dg != (3 if k in (2,5) else 0):
                data['mismatches'].append(['two_step',k,eps,dg])
            for m in range(7):
                n=6*(2**m)
                for signed_k in (6,-6):
                    c['halfturn']+=1
                    if gamma(q,signed_k) % n != (3 if signed_k>0 else -3) % n:
                        data['mismatches'].append(['halfturn',q,eps,m,signed_k])
                    # Identifying Gamma with change of invariant Sigma would require zero; it never equals zero for these halfturns.
                    if gamma(q,signed_k) % n == 0:
                        data['mismatches'].append(['halfturn_false_zero',q,eps,m,signed_k])
                for signed_k in (12,-12):
                    c['full_loop']+=1
                    want=(6 if signed_k>0 else -6)%n
                    if gamma(q,signed_k)%n != want:
                        data['mismatches'].append(['full_loop',q,eps,m,signed_k])
                    # m=0 detects no winding; m>=1 detects +6
                    if (gamma(q,12)%n==0) != (m==0):
                        data['mismatches'].append(['level_alias',q,eps,m])
    # Exact full winding quotient size for fixed phase and same endpoint.
    for m in range(7):
        N=6*(2**m)
        for q in range(12):
            obs={gamma(q,12*w)%N for w in range(2**m)}
            c['winding_quotient']+=1
            if len(obs)!=2**m:
                data['mismatches'].append(['winding_classes',m,q,len(obs)])
    # If a root-lineage STATE starts at +3 and is changed by Gamma=+3 over physical halfturn,
    # its C24 value is 6 and hence order falls from 8 to 4, violating principal root-type stability.
    N=24
    data['samples']['C24']={'selected_root':3,'hypothetical_after_additive_halfturn':6,
                            'selected_root_order':order(3,N),'after_transport_order':order(6,N)}
    c['C24_order']+=1
    if (order(3,N),order(6,N))!=(8,4):
        data['mismatches'].append(['C24_order'])
    data['samples']['two_step_by_E_start']={str(k):gamma(2*k,2) for k in range(6)}
    data['samples']['halfturn_by_E_start']={str(k):gamma(2*k,6) for k in range(6)}
    data['samples']['closed_loop_by_m']={str(m):gamma(0,12)%(6*(2**m)) for m in range(7)}
    data['total_checks']=sum(c.values())
    data['mismatch_count']=len(data['mismatches'])
    OUT.write_text(json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    assert not data['mismatches'],data['mismatches'][:10]
    print(json.dumps({'total_checks':data['total_checks'],'mismatch_count':0,'by_type':c,'output':str(OUT)},ensure_ascii=False))

if __name__=='__main__': main()
