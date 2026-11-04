#!/usr/bin/env python3
"""Independent exact-rational crosscheck for EC49FAP.
Run: python CROSSCHECK_EC49FAP.py > CROSSCHECK_REPORT_EC49FAP.json
Imports only frozen operation/observation definitions and fixed source words
from the sibling verifier; the rational elimination and suffix count use
separately implemented algorithms.
"""
import json
from fractions import Fraction
from VERIFY_EC49FAP import OPS,B2,B3,CASES,steps,key,net,obs,rank,prefixes

def rational_rank(sigs):
    sigs=list(sigs)
    if not sigs:return 0
    m=[[Fraction(int(s[i]==bucket)) for s in sigs for bucket in range(5)] for i in range(9)]
    r=0
    for col in range(len(m[0])):
        p=next((i for i in range(r,9) if m[i][col]),None)
        if p is None:continue
        m[p],m[r]=m[r],m[p]
        for i in range(r+1,9):
            v=m[i][col]/m[r][col]
            if v:
                for j in range(col,len(m[i])):m[i][j]-=v*m[r][j]
        r+=1
        if r==9:break
    return r

def independently_count_zero_six_axis_words(length):
    d={(0,0,0,0,0,0):1}
    for _ in range(length):
        nxt={}
        for vec,count in d.items():
            for primitive in OPS.values():
                v=list(vec)
                for s in primitive:v[abs(s)-1]+=1 if s>0 else -1
                t=tuple(v);nxt[t]=nxt.get(t,0)+count
        d=nxt
    return d.get((0,0,0,0,0,0),0)

def check():
    assert independently_count_zero_six_axis_words(6)==13236
    cases=[]
    for case,src in CASES.items():
        by_h={2:B2,3:B3,**src}
        original=[w for h in range(2,8) for w in by_h[h]]
        six=sorted({obs(steps(w)) for w in original})
        assert len(six)==6
        for mask in range(64):
            sigs=[s for i,s in enumerate(six) if (mask>>i)&1]
            assert rational_rank(sigs)==rank(sigs)
        h8=[w+suffix for w in by_h[7] for suffix in ('c','d')]
        h9=[w+'fg' for w in by_h[7]]
        whole=original+h8+h9
        assert all(net(steps(w))==(2,0,0,0,0,0) for w in whole)
        assert len({key(steps(w)) for w in whole})==5
        assert len({obs(steps(w)) for w in whole})==6
        assert all(rational_rank({obs(steps(w)) for w in by_h[h]})==9 for h in range(2,8))
        assert rational_rank({obs(steps(w)) for w in h8})==9
        assert rational_rank({obs(steps(w)) for w in h9})==9
        assert len(prefixes(whole))==94
        assert all(any(w.startswith(root) for j in (3,4,5,6) for root in by_h[j]) for w in h8+h9)
        cases.append({'case':case,'fraction_masks_checked':64,'native_prefix_edges':94,'all_horizons_rational_rank_9':True,'full_keys':5,'observer_signatures':6})
    return {'result':'PASS_INDEPENDENT_FRACTION_AND_VECTOR_DP','six_step_zero_net_words':13236,'total_fraction_mask_checks':256,'cases':cases}

if __name__=='__main__':print(json.dumps(check(),ensure_ascii=False,indent=2))
