#!/usr/bin/env python3
"""Derive two-step directed-Hausdorff recourse certificates from the prior
R5 exact single-cut compact table. No old path DP is replayed here.
Run: python VERIFY_R5_TWO_CUT_ORDER_CERTIFICATES.py EXACT_R5_OFFLINE_MAXMIN_ALL_BACKGROUND_VALUES.json
"""
import json, sys
from collections import Counter

BIT8, BIT9 = 2, 4  # positions of original cuts 8 and 9 in BITS=(3,8,9,10,27)

def inspect(data):
    assert data['frozen_science_commit'] == '435e77af0d180eac32bd1f9c4c464bc4010b7551'
    assert data['verified_transition_count'] == 256
    assert data['effective_cut_bits'] == [3,8,9,10,27]
    single = {}
    for k in range(214,222):
        for cut in (8,9):
            row = data['rows'][f'{k}_{cut}']
            assert row['K'] == k and row['cut'] == cut
            masks = row['old_effective_mask_order']; vals = row['recourse_by_old_mask']
            assert len(masks) == len(vals) == 16
            bit = BIT8 if cut==8 else BIT9
            assert len(set(masks)) == 16 and all(m & bit == 0 for m in masks)
            for mask,v in zip(masks,vals): single[k,cut,mask] = v

    counts=Counter(); gap=Counter(); by_k={}; examples=[]
    for k in range(214,222):
        by_k[str(k)]={}
        for b in range(32):
            if b&(BIT8|BIT9): continue
            U89 = single[k,8,b] + single[k,9,b|BIT8]
            U98 = single[k,9,b] + single[k,8,b|BIT9]
            lb = max(single[k,8,b],single[k,9,b]); ub = min(U89,U98)
            assert lb <= ub
            dif = U89-U98
            counts['9-first' if dif>0 else '8-first' if dif<0 else 'tie'] += 1
            gap[ub-lb] += 1
            if b in (0,8): by_k[str(k)][f'cut10_{int(bool(b&8))}']=[U89,U98]
            examples.append([k,b,lb,ub,U89,U98])
    assert len(examples)==64
    assert counts=={'9-first':36,'8-first':8,'tie':20}
    assert gap=={3:36,5:28}
    return {'status':'PASS_R5_TWO_CUT_ORDERED_CERTIFICATES',
            'scope':'R5 derived observer K214..221, all 8 effective backgrounds without cuts 8 or 9',
            'two_step_certificates':64,
            'tighter_bound_route_counts':dict(counts),
            'upper_minus_lower_gap_histogram':dict(sorted(gap.items())),
            'U8_then_9_U9_then_8_by_K_and_cut10':by_k,
            'baseline':'author-side exact single-cut recourse table; these are upper and lower certificates, not joint exact distances'}

def main():
    if len(sys.argv)!=2: raise SystemExit('Usage: script.py <compact R5 JSON table>')
    print(json.dumps(inspect(json.load(open(sys.argv[1]))),indent=2,sort_keys=True))

if __name__=='__main__': main()
