#!/usr/bin/env python3
"""R5 fifth chamber exact full 256-state f=2 unmarked-error proof.
Usage: python VERIFY_R5_FIFTH_F2_ALL256.py EXACT_R5_ALL_101_BUDGETS.json
"""
import hashlib, json, sys
from functools import lru_cache
from pathlib import Path
INPUT_SHA='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
L=25845652773852463277015040000
U=58182461585441404127941754880
H=(18,24,82,34,17)

def table_from(path):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==INPUT_SHA
    d=json.loads(raw)
    tab={int(k):tuple(map(int,r['counts'])) for k,r in d['counts_and_cohorts'].items()}
    assert set(tab)==set(range(214,315))
    assert all(len(r)==256 for r in tab.values())
    return tab

def response_family(row,masks,tau):
    vals={}
    for i,h in enumerate(masks):vals[row[h]]=vals.get(row[h],0)|(1<<i)
    candidates=[]
    for low in sorted(vals):
        cover=0
        for v,b in vals.items():
            if low<=v<=low+tau:cover|=b
        candidates.append(cover)
    unique=set(candidates)
    return tuple(sorted(a for a in unique if not any(a!=b and a&b==a for b in unique)))

def solve(tab,masks,tau):
    full=(1<<len(masks))-1
    acts={}
    for k in range(214,315):
        a=response_family(tab[k],masks,tau)
        acts.setdefault(a,k)
    acts=sorted(((k,a) for a,k in acts.items()),key=lambda t:(t[0] not in (216,223,296),t[0]))
    missing={a:full^a for _,answers in acts for a in answers}
    @lru_cache(None)
    def V(zero,one,two):
        if (zero|one|two).bit_count()<=1:return 0
        best=1<<40
        for k,answers in acts:
            worst=0;valid=True
            for a in answers:
                b=missing[a]
                z=zero&a
                o=(one&a)|(zero&b)
                t=(two&a)|(one&b)
                if (z,o,t)==(zero,one,two):valid=False;break
                if (z|o|t).bit_count()>1:worst=max(worst,V(z,o,t))
                if k+worst>=best:valid=False;break
            if valid:best=min(best,k+worst)
        assert best<1<<40
        return best
    value=V(full,0,0)
    return {'value':value,'memo_states':V.cache_info().currsize,
            'action_families':len(acts),
            'cheapest_budget_representatives':sorted(k for k,a in acts)}

def verify(path):
    tab=table_from(path)
    lower=solve(tab,H,L)
    upper=solve(tab,tuple(range(256)),U-1)
    assert lower['value']==upper['value']==2635
    return {'status':'PASS_R5_FIFTH_CHAMBER_FULL256_F2_EXACT_2635',
            'pin':PIN,'input_sha256':INPUT_SHA,
            'tau_interval':[str(L),str(U)],
            'normal_reading_rule':'abs(y-N_h(k))<=eta, tau=2eta',
            'arbitrary_unmarked_error_count':2,
            'exact_adaptive_worst_budget':2635,
            'lower_five_mask_L':lower,'upper_full256_U_minus_1':upper,
            'status_of_result':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED'}

if __name__=='__main__':
    assert len(sys.argv)==2
    result=verify(sys.argv[1])
    print(result['status'])
    print(json.dumps(result,ensure_ascii=False,indent=2))
