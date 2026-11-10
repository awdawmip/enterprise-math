#!/usr/bin/env python3
"""R696 exact rational S6 port-subset kernel classification; candidate only."""
from itertools import permutations, combinations
from fractions import Fraction
from collections import Counter
from pathlib import Path
import json

I = tuple(range(6)); PERMS = tuple(permutations(I))

def kernel(pair, mask):
    i,j=pair; R=set(I)-{i,j}; A=set(mask)
    assert A<=R
    if not A: return {'HALT':Fraction(1)}
    return {k:Fraction(1,len(A)) for k in A}

def masks(pair):
    rem=sorted(set(I)-set(pair))
    return tuple(tuple(rem[k] for k in range(4) if bits>>k & 1) for bits in range(16))

def verify():
    pairs=tuple((i,j) for i in I for j in I if i!=j)
    assert len(pairs)==30 and len(PERMS)==720
    sizes=Counter(); checks=0
    for pair in pairs:
        ms=masks(pair)
        assert len(ms)==16
        distributions=[kernel(pair,A) for A in ms]
        assert len({tuple(sorted((str(k),str(v)) for k,v in d.items())) for d in distributions})==16
        for A in ms:
            D=kernel(pair,A); sizes[len(A)]+=1
            assert sum(D.values())==1
            for p in PERMS:
                pair2=(p[pair[0]],p[pair[1]])
                A2=tuple(p[k] for k in A)
                E=kernel(pair2,A2)
                F={p[k] if k!='HALT' else 'HALT':v for k,v in D.items()}
                assert F==E
                checks+=1
    assert sizes=={0:30,1:120,2:180,3:120,4:30}
    assert checks==345600
    a=kernel((0,1),(2,)); b=kernel((0,1),(3,))
    assert a[2]==1 and 2 not in b and len(a)==len(b)==1
    ev={'schema':'R696_S6_PORT_MASK_KERNEL_EXACT_V1','date':'2026-11-10',
        'model':'Abstract port-permission subset on four unused native axes; fixed third force sign; S6 axis-label covariance, not native dynamic port admission',
        'ordered_pairs':len(pairs),'masks_per_pair':16,'per_mask_cardinality_counts_for_all_pairs':dict(sorted(sizes.items())),
        'axis_permutations':len(PERMS),'equivariant_kernel_configurations_checked':checks,
        'minimal_bits_for_label_sensitive_kernel_with_halt':4,
        'singleton_deterministic_additional_states':4,
        'rational_weights_by_mask_size':{str(k):str(Fraction(1,k)) for k in range(1,5)},
        'count_only_observer_witness':{'A':[2],'B':[3],'both_cardinality':1,'future_query_k_is_2':{'A':1,'B':0}},
        'verification_marker':'R696_S6_PORT_MASK_KERNEL_EXACT_PASS'}
    Path(__file__).with_name('R696_EVIDENCE.json').write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf-8')
    print(ev['verification_marker'],checks)
    return ev

if __name__=='__main__':verify()
