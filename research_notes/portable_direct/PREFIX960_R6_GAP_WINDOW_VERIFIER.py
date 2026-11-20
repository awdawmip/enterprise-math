#!/usr/bin/env python3
"""Independent exact check of the universal adjacent/d-spaced core quotient-gap window.
Never loads prior pair certificate to generate or classify witnesses.
"""
import json
from collections import Counter
from pathlib import Path

PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'

def named_quotients(p, k, a, b):
    z=[]
    x=k*a
    for i in range(p):
        for j in range(p):
            y=(x ^ (1 << j))-(1 << i)
            if y>0 and y%b==0:
                z.append((y//b,i,j))
    return z

def bound(d):
    return (d-1)//2, 2*d+2

def brute_small():
    summary=Counter(); minmax={}
    # All odd cores, all even positive core spacings, all off-diagonal odd a,b.
    for p in range(4,7):
        H=1<<(p-1)
        for k in range(1,H,2):
            for d in range(2,H-k,2):
                low,high=bound(d)
                observed=[]
                for a in range(H+1,2*H,2):
                    for b in range(H+1,2*H,2):
                        if a==b: continue
                        x=named_quotients(p,k,a,b)
                        if not x: continue
                        y=named_quotients(p,k+d,a,b)
                        for t,i,j in x:
                            for T,I,J in y:
                                m=T-t
                                if not(low<=m<=high):
                                    raise AssertionError((p,k,d,a,b,t,T,i,j,I,J))
                                observed.append(m)
                                summary['joint_named_witnesses']+=1
                summary['core_spacings']+=1
                if observed: minmax[f'{p}/{k}/{d}']=[min(observed),max(observed)]
    # Independent expanded adjacent-core sweep includes all 56 cases at p=4..7.
    for p in range(4,8):
        H=1<<(p-1)
        for k in range(1,H-2,2):
            observed=Counter()
            for a in range(H+1,2*H,2):
                for b in range(H+1,2*H,2):
                    if a==b: continue
                    x=named_quotients(p,k,a,b)
                    if not x: continue
                    y=named_quotients(p,k+2,a,b)
                    for t,_,_ in x:
                        for T,_,_ in y:
                            assert 0<=T-t<=6
                            observed[T-t]+=1
            summary['adjacent_core_cases']+=1
            summary['adjacent_named_witnesses']+=sum(observed.values())
            for m,v in observed.items(): summary[f'adjacent_gap_{m}']+=v
    return summary,minmax

EXAMPLES=[(4,1,2,9,11,1,1,1,2,3,3,0),
          (6,5,2,59,33,7,13,5,5,4,5,6)]

def check_examples():
    for p,k,d,a,b,t,T,i,j,I,J,m in EXAMPLES:
        assert ((k*a)^(1<<j))-(1<<i)==t*b
        assert (((k+d)*a)^(1<<J))-(1<<I)==T*b
        assert m==T-t
        assert (d-1)//2<=m<=2*d+2

if __name__=='__main__':
    check_examples()
    summary,minmax=brute_small()
    out={'frozen_scientific_input_pin':PIN,
         'claim':'For every p>=3, core increment d>=2 and valid named joint witness, floor((d-1)/2)<=T-t<=2*d+2. In particular d=2 gives 0..6, and both endpoints are achieved.',
         'verification_method':'Original XOR integer brute for all described finite p,k,d and (a,b,i,j,I,J), plus exact endpoint witnesses.',
         'verified_domain':{'all_even_core_spacings_p':[4,5,6],'adjacent_all_odd_core_p':[4,5,6,7]},
         'counts':dict(sorted(summary.items())),
         'observed_gap_ranges_by_core_spacing':minmax,
         'sharp_examples':EXAMPLES,
         'review_status':'AUTHOR_PROOF_PLUS_FINITE_CHECK;NOT_REVIEWED',
         'source_not_used_to_generate_pairs':'Historical PREFIX-959B pair list and SHA256'}
    dst=Path(__file__).with_name('PREFIX960_R6_EXACT_RESULTS.json')
    dst.write_text(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'output':str(dst),'counts':out['counts'],'examples':out['sharp_examples']},ensure_ascii=False))
