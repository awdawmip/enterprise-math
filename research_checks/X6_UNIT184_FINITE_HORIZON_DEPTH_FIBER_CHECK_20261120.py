#!/usr/bin/env python3
"""Independent exact six-axis length-M finite-horizon observer-fiber check.
Unit184 checker: no code/import from project production; math is frozen X6 signed-axis.
"""
from collections import defaultdict
from math import ceil, log2, factorial
import json
import hashlib

DIM = 6
ZERO = (0,) * DIM

def canonical(z):
    t=min(z)
    return tuple(x-t for x in z),t

def norm1(z):
    return sum(map(abs,z))

def relation(z):
    return tuple(tuple(zi-zj for zj in z) for zi in z)

def from_field(Z):
    return tuple(max(row) for row in Z)

def recover(q,C):
    delta=C-sum(q)
    if delta%DIM:
        raise ValueError('incompatible C')
    h=delta//DIM
    return tuple(x+h for x in q)

def candidates(q,M):
    # All possible integer lifts lie in [-M-min(q), M], since each coordinate is bounded by M
    if (M-sum(q))&1:
        return []
    return [h for h in range(-M-max(q), M+1)
            if sum(abs(x+h) for x in q)<=M]

def witness(M):
    d,r=divmod(M,3)
    # Three -d and three zero; use +1 on last coordinate when M mod 3 = 1
    z=(-d,-d,-d,0,0,1 if r==1 else 0)
    q,_=canonical(z)
    return q

def main():
    counts={ZERO:1}
    cases=0
    verified_relation=0
    verified_recovery=0
    verified_interval=0
    bound_violations=0
    table=[]
    example=[]
    for M in range(11):
        fibers=defaultdict(set)
        for z, count in counts.items():
            assert count>0
            q,h=canonical(z)
            Z=relation(z)
            if from_field(Z)!=q:
                raise RuntimeError('relation mismatch')
            verified_relation+=1
            if recover(q,sum(z))!=z:
                raise RuntimeError('grand-total recovery mismatch')
            verified_recovery+=1
            fibers[q].add(h)
        max_n=0
        for q,H in fibers.items():
            actual=sorted(H)
            expected=candidates(q,M)
            if actual!=expected:
                raise RuntimeError(f'fiber mismatch M={M}, q={q}, {actual} != {expected}')
            verified_interval+=1
            max_n=max(max_n,len(H))
        sharp=M//3+1
        if max_n>sharp or max_n!=sharp:
            raise RuntimeError(f'sharp error M={M}: {max_n} vs {sharp}')
        q=witness(M)
        expected=candidates(q,M)
        if len(expected)!=sharp:
            raise RuntimeError(f'witness failed M={M} q={q} lifts={expected}')
        if q not in fibers or fibers[q]!=set(expected):
            raise RuntimeError('witness not realized')
        if M==10:
            example=[{'h':h,'z':[a+h for a in q], 'native_BRC_paths':counts[tuple(a+h for a in q)]} for h in expected]
        table.append({'M':M,'reachable_endpoints':len(counts),'relative_states':len(fibers),
                      'max_fiber_lifts':max_n,'optimal_worstcase_bits':(sharp-1).bit_length(),
                      'witness_relative':list(q),'witness_depths':expected})
        cases+=len(counts)
        if M<10:
            nxt=defaultdict(int)
            for z,cnt in counts.items():
                for i in range(DIM):
                    zp=z[:i]+(z[i]+1,)+z[i+1:]
                    zm=z[:i]+(z[i]-1,)+z[i+1:]
                    nxt[zp]+=cnt
                    nxt[zm]+=cnt
            counts=nxt
    output={'schema':'X6_UNIT184_EXACT_FIBER_LABEL_CHECK_V1','model':'Z6_signed_12_unit_moves',
      'tested_M':list(range(11)), 'all_length_endpoints_checked':cases,
      'relation_recovery_checks':verified_relation,'grand_total_recovery_checks':verified_recovery,
      'fiber_interval_checks':verified_interval,'failures':bound_violations,
      'results':table,'M10_concrete_BRC_multiplicities':example,
      'source_scope':'Independent arithmetic check against frozen X6 signed-axis and A3 equal-capacity relation-field formulas; no native R063 benchmark run',
      'status':'FINITE_DIAGNOSTIC_NOT_GLOBAL_PROOF'}
    path='/mnt/data/x6_unit184_fiber_bits_results.json'
    with open(path,'w',encoding='utf8') as f:json.dump(output,f,ensure_ascii=False,indent=2,sort_keys=True);f.write('\n')
    digest=hashlib.sha256(open(path,'rb').read()).hexdigest()
    print(json.dumps({'all_length_endpoints_checked':cases,'distinct_fibers_checked':verified_interval,
      'M10_concrete_BRC_multiplicities':example,'max_fibers':[x['max_fiber_lifts'] for x in table],
      'results_sha256':digest},indent=2))
if __name__=='__main__':main()
