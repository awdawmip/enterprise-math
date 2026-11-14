#!/usr/bin/env python3
"""Reproduce the exact Boolean support/interaction phase diagram for R5 cuts 8,9.
Consumes the immutable GitHub exact 256-case value table; no floating point.
"""
import json
from collections import Counter
from pathlib import Path
BITS=(3,8,9,10,27)

def closed(mask,bit):
    return (mask>>BITS.index(bit))&1

def formula(K,cut,mask):
    a=closed(mask,8)
    b=closed(mask,9)
    c=closed(mask,10)
    if cut==8:
        if K==214:return 7-4*b*(1-c)
        if K==215:return 6-3*b*(1-c)
        if K==216:return 6-3*b-c+3*b*c
        if K<=220:return 5-2*b*(1-c)
        return 5-2*b
    if K==214:return 7-2*a
    if K==215:return 6-a
    if K==216:return 5+(1-a)*(1-c)
    return 5

def main():
    data=json.loads(Path(__file__).with_name('EXACT_R5_OFFLINE_MAXMIN_ALL_BACKGROUND_VALUES.json').read_text())
    assert data['verified_transition_count']==256
    assert data['full_stdout_json_sha256']=='e8157e196f3d8408a11bf5f67935d4e083578844d6461433f209fed63f4e04ed'
    assert set(data['rows'])=={f'{k}_{bit}' for k in range(214,222) for bit in (8,9)}
    total=0
    result=[]
    for K in range(214,222):
        for cut in (8,9):
            row=data['rows'][f'{K}_{cut}']
            masks=row['old_effective_mask_order']
            vals=row['recourse_by_old_mask']
            assert len(masks)==len(vals)==16 and len(set(masks))==16
            assert all(not closed(m,cut) for m in masks)
            assert masks==sorted(masks)
            for mask,value in zip(masks,vals):
                assert formula(K,cut,mask)==value,(K,cut,mask,value)
                total+=1
            support=[]
            for other_bit in (b for b in BITS if b!=cut):
                flag=1<<BITS.index(other_bit)
                d=dict(zip(masks,vals))
                if any(d[m]!=d[m^flag] for m in masks):support.append(other_bit)
            assert support==([9,10] if cut==8 and K<=220 else
                             [9] if cut==8 else [8,10] if K==216 else
                             [8] if K<=215 else []),(K,cut,support)
            result.append({'K':K,'cut':cut,'minimal_support':support,
                           'histogram':dict(sorted(Counter(vals).items()))})
    assert total==256
    print(json.dumps({'status':'PASS_EXACT_R5_RECOURSE_BOOLEAN_PHASE',
                      'exact_transition_checks':total,'rows':result,
                      'review':'NOT_REVIEWED'},sort_keys=True))

if __name__=='__main__':main()
