#!/usr/bin/env python3
"""Frozen R5 m=3 period at O(N): independent price vs signature capacities.

Run from any cwd. Requires sibling r5_m2_o1_exact_period_20261122 directory.
Python3 standard library, exact integer arithmetic.
"""
from math import lcm
from pathlib import Path
import json, sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'r5_m2_o1_exact_period_20261122'))
import VERIFY_R5_M2_O1 as base


def by_price(d, mask):
    """Per-price DP: each event may have up to two selected items."""
    union, sigs = base.data_for(mask)
    events = [i for i in range(5) if mask & (1 << i)]
    idx = {i:j for j,i in enumerate(events)}
    empty = (0,) * len(events)
    dp = {empty: ([1]+[0]*(d-1), [0]*d)}
    for p in union:
        affected = tuple(idx[i] for i in events if sigs[p] & (1 << i))
        nxt = {counts:(v[:],dv[:]) for counts,(v,dv) in dp.items()}
        for counts,(v,dv) in dp.items():
            limit = min(2-counts[j] for j in affected)
            for r in range(1, limit+1):
                new = tuple(counts[j]+(r if j in affected else 0)
                            for j in range(len(events)))
                a = base.cyclic_shift(v, p*r)
                b = [u+(p*r)*x for u,x in zip(base.cyclic_shift(dv,p*r),a)]
                if new not in nxt:
                    nxt[new]=(a,b)
                else:
                    x,y = nxt[new]
                    nxt[new]=(base.add(x,a),base.add(y,b))
        dp=nxt
    q,dq=[0]*d,[0]*d
    for v,dv in dp.values():
        q,dq=base.add(q,v),base.add(dq,dv)
    return base.prod_factor_jet(q,dq,union)


def class_jet(d, prices, r):
    """Exact homogeneous degree-r sum on a group of same event signature."""
    q,dq=[0]*d,[0]*d
    if r==0: q[0]=1
    elif r==1:
        for p in prices:
            q[p%d]+=1;dq[p%d]+=p
    elif r==2:
        for i,p in enumerate(prices):
            for t in prices[i:]:
                q[(p+t)%d]+=1;dq[(p+t)%d]+=p+t
    else:raise ValueError(r)
    return q,dq


def by_signature(d, mask):
    """Independent group-wise DP over complete homogeneous polynomials h0,h1,h2."""
    union,sigs = base.data_for(mask)
    events = [i for i in range(5) if mask & (1 << i)]
    idx = {i:j for j,i in enumerate(events)}
    groups = {}
    for p,sig in sigs.items():
        groups.setdefault(sig,[]).append(p)
    empty=(0,)*len(events)
    dp={empty:([1]+[0]*(d-1),[0]*d)}
    for sig,prices in groups.items():
        affected=tuple(idx[i] for i in events if sig & (1<<i))
        local=[class_jet(d,prices,r) for r in range(3)]
        nxt={}
        for counts,(v,dv) in dp.items():
            limit=min(2-counts[j] for j in affected)
            for r in range(limit+1):
                new=tuple(counts[j]+(r if j in affected else 0)
                          for j in range(len(events)))
                a,b=local[r]
                q=base.cyclic_mul(v,a)
                dq=base.add(base.cyclic_mul(dv,a),base.cyclic_mul(v,b))
                if new in nxt:
                    x,y=nxt[new]
                    nxt[new]=(base.add(x,q),base.add(y,dq))
                else:nxt[new]=(q,dq)
        dp=nxt
    q,dq=[0]*d,[0]*d
    for v,dv in dp.values():
        q,dq=base.add(q,v),base.add(dq,dv)
    return base.prod_factor_jet(q,dq,union)


def numerator(d,method):
    q,dq=[0]*d,[0]*d
    for mask in range(1,32):
        a,b=method(d,mask)
        if mask.bit_count()%2:
            q,dq=base.add(q,a),base.add(dq,b)
        else:
            q,dq=base.sub(q,a),base.sub(dq,b)
    return base.cyclotomic_reduce(q,d),base.cyclotomic_reduce(dq,d)


def verify():
    assert base.EXPECTED_L==229746052653717600
    candidates=[d for d in range(2,315) if sum(p%d==0 for p in base.PRICES)>=3]
    assert len(candidates)==39 and lcm(*candidates)==base.EXPECTED_L
    rows=[]
    for d in base.WITNESS_ORDERS:
        v=numerator(d,by_price)
        w=numerator(d,by_signature)
        assert v==w,('full vectors disagree',d)
        a,b=v
        j=0 if any(a) else 1
        assert any(v[j])
        n=sum(p%d==0 for p in base.PRICES)
        assert n-j>=3
        k=next(i for i,x in enumerate(v[j]) if x)
        rows.append({'d':d,'n_d':n,'first_jet':j,'pole':n-j,'coordinate':k,
                     'coefficient':v[j][k],'zero_jet_vector':a,'first_jet_vector':b})
    assert lcm(*(r['d'] for r in rows))==base.EXPECTED_L
    return {'schema':'R5_M3_O1_EXACT_PERIOD_V1','date':'2026-11-22',
            'frozen_model':'R5_TRUE_EVENT_SCALAR_M3','m':3,
            'least_period':str(base.EXPECTED_L),'candidate_orders':candidates,
            'method_A':'per-price five-event bounded-count DP',
            'method_B':'group-by-exact-event-signature homogeneous H2 convolution',
            'integer_arithmetic':'exact q d/dq jets and cyclotomic quotient',
            'review':'NOT_REVIEWED','witnesses':rows}


if __name__=='__main__':
    out=verify()
    print('UPPER',out['least_period'],'candidates',len(out['candidate_orders']))
    print('d n_d j pole coord coefficient')
    for x in out['witnesses']:
        print(x['d'],x['n_d'],x['first_jet'],x['pole'],x['coordinate'],x['coefficient'])
    print('ALL CHECKS PASS')
    with open('R5_M3_O1_CERTIFICATE_FULL.json','w',encoding='utf-8') as f:
        json.dump(out,f,ensure_ascii=False,indent=2)
