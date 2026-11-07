#!/usr/bin/env python3
"""PREFIX-566: gate-retaining 37-state quotient for the frozen native X6-BRC kernel.
Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Exact integer certificate. Depends only on published PREFIX565_positive_marginal_certificate.py
(reuses its pinned original 48-phase/96-port/6-action kernel; no third-party deps).
Observer: q1=q2=q3=q4=1, x=q5,y=q6,z=gate; nine roots r5=r6=0.
"""
from PREFIX565_positive_marginal_certificate import (PHASES, ZERO_ROOT, ROOTS,
    ACTIONS, edge, SCIENCE_PIN, clean)
from collections import Counter
from time import perf_counter
import json

# PREFIX-566: retain gate z, keeping q5 and q6 independent.

def sigma_signed(k):
    return (1 if k>0 else -1) * {5:6,6:5}.get(abs(k),abs(k))

def native_involution():
    # Phase is uniquely identified by its ordered signed (previous,current) pair.
    lookup={(p,c):i for i,(a,p,c) in enumerate(PHASES)}
    assert len(lookup)==48
    return tuple(2*lookup[(sigma_signed(PHASES[i//2][1]),
                           sigma_signed(PHASES[i//2][2]))]+i%2
                 for i in range(96))

def marginal_gate_rows(root):
    return [Counter((j,w[4],w[5],w[6])
            for action in ACTIONS for j,w in [edge(i,action,root)])
            for i in range(96)]

def weighted_quotient(rows):
    ids=[0]*len(rows)
    growth=[1]
    for _ in range(len(rows)):
        keys=[]
        for row in rows:
            out=Counter()
            for (j,a,b,g),m in row.items():out[(ids[j],a,b,g)]+=m
            keys.append(tuple(sorted(out.items())))
        lookup={}
        nxt=[lookup.setdefault(k,len(lookup)) for k in keys]
        if nxt==ids:break
        ids=nxt
        growth.append(len(lookup))
    else:
        raise AssertionError('partition failed to stabilize')
    quotient={}
    for i,row in enumerate(rows):
        q=Counter()
        for (j,a,b,g),m in row.items():q[ids[j],a,b,g]+=m
        if ids[i] in quotient:assert quotient[ids[i]]==q
        else:quotient[ids[i]]=q
    return tuple(ids),tuple(quotient[i] for i in range(len(quotient))),growth

def step_gate(current,rows):
    result=[]
    for row in rows:
        s=Counter()
        for (j,a,b,g),mult in row.items():
            for (x,y,z),val in current[j].items():
                s[x+a,y+b,z+g]+=mult*val
        result.append(clean(s))
    return result

POWER={0:{(0,0):2},1:{(1,0):1}}
def powersum(n):
    if n in POWER:return POWER[n]
    for k in range(max(POWER)+1,n+1):
        r=Counter()
        for (a,b),c in POWER[k-1].items():r[a+1,b]+=c
        for (a,b),c in POWER[k-2].items():r[a,b+1]-=c
        POWER[k]=clean(r)
    return POWER[n]

def symmetric_to_uvz(poly):
    result=Counter()
    for (a,b,z),val in poly.items():
        if a>b:continue
        if a==b:result[0,a,z]+=val
        else:
            for (u,v),cc in powersum(b-a).items():result[u,v+a,z]+=val*cc
    return clean(result)

def verify_566(check_depth=24,sign_depth=64):
    t0=perf_counter()
    rows=marginal_gate_rows(ZERO_ROOT)
    root_count=0
    for root in ROOTS:
        assert marginal_gate_rows(root)==rows
        root_count+=1
    ids,quot,growth=weighted_quotient(rows)
    assert len(quot)==37,(len(quot),growth)
    assert len(ids)==96
    lift=native_involution()
    assert all(lift[lift[i]]==i for i in range(96))
    assert sum(lift[i]==i for i in range(96))==32
    fixed=sorted({ids[i] for i in range(96) if lift[i]==i})
    assert len(fixed)==11,(fixed, len(fixed))
    # The native involution fixes all paths read at fixed ports with root r5=r6=0.
    # Check all 576 native actions against the swapped weights and matched edge.
    swapped_edges=0
    for i in range(96):
        mapped=[]
        for action in ACTIONS:
            j,w=edge(i,action,ZERO_ROOT)
            matching=[a for a in ACTIONS
                      if edge(lift[i],a,ZERO_ROOT)==
                          (lift[j],w[:4]+(w[5],w[4])+w[6:])]
            assert len(matching)==1
            mapped.append(matching[0]);swapped_edges+=1
        assert set(mapped)==set(ACTIONS)
    current=[{(0,0,0):1} for _ in range(len(quot))]
    original=[{(0,0,0):1} for _ in range(96)]
    exact_matches=0;positions=0
    snapshots=[];negative_witness=None
    for depth in range(max(check_depth,sign_depth)+1):
        if depth<=check_depth:
            for i in range(96):
                assert original[i]==current[ids[i]],('native-vs-37',depth,i)
                exact_matches+=1
                positions+=len(original[i])
        uvz_positions=0
        for cls in fixed:
            poly=current[cls]
            assert all(poly.get((b,a,g),0)==val
                       for (a,b,g),val in poly.items()),('sigma-failure',depth,cls)
            uvz=symmetric_to_uvz(poly)
            uvz_positions+=len(uvz)
            neg=next(((k,v) for k,v in uvz.items() if v<0),None)
            if neg and negative_witness is None:
                negative_witness={'depth':depth,'class':cls,'monomial':neg[0],
                                  'value':neg[1]}
        if depth in (0,4,8,12,16,24,32,48,64):
            snapshots.append({'depth':depth,'fixed_uvz_positions':uvz_positions,
                              'all_37_xyz_positions':sum(len(p) for p in current)})
        if depth==max(check_depth,sign_depth):break
        current=step_gate(current,quot)
        if depth<check_depth:original=step_gate(original,rows)
    return {'status':'ALL_CHECKS_PASS','science_pin':SCIENCE_PIN,
        'observer':'q1=q2=q3=q4=1, x=q5,y=q6,z=gate',
        'root_count':root_count,'native_root_edge_checks':root_count*96*6,
        'native_involution_edge_checks':swapped_edges,
        'partition_growth':growth,'quotient_class_count':len(quot),
        'fixed_native_ports':32,'fixed_observer_classes':len(fixed),
        'fixed_class_ids':fixed,
        'native_to_37_exact_polynomials':exact_matches,
        'native_to_37_nonzero_coefficient_positions':positions,
        'native_checked_depth':[0,check_depth],
        'finite_uvz_sign_scan_depth':[0,sign_depth],
        'finite_negative_witness':negative_witness,
        'snapshots':snapshots,'elapsed_seconds':round(perf_counter()-t0,3),
        'theorem':'37-state strongly weighted gate-preserving quotient, all finite depths',
        'gate_aware_e_positivity':'FINITE_TEST_ONLY; not established for arbitrary depths'}

if __name__=='__main__':
    print(json.dumps(verify_566(),ensure_ascii=False,indent=2))
