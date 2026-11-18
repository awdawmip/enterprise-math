#!/usr/bin/env python3
"""Exhaustive H2 triple / H3 pair with exactly two full positive BRC keys.
Scientific source frozen: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import itertools,json
from EC49FDS_seedpairs import language,rank_ok,key,pref
from EC49FDS_independent_fraction_audit import rank
A=language(2);B=language(3)
accepted_a=[v for v in itertools.combinations(A,3) if rank_ok([w[1] for w in v])]
accepted_b=[v for v in itertools.combinations(B,2) if rank_ok([w[1] for w in v])]
assert len(accepted_a)==6 and len(accepted_b)==16
out=[]
for aa in accepted_a:
    for bb in accepted_b:
        ws=[w[0] for w in aa+bb]
        keys=sorted({key(w) for w in ws})
        if len(keys)!=2:continue
        assert rank(ws[:3])==9 and rank(ws[3:])==9
        assert all(len(w)==(2 if i<3 else 3) for i,w in enumerate(ws))
        cost=len(set().union(*(pref(w) for w in ws)))
        out.append({'H2':sorted(ws[:3]),'H3':sorted(ws[3:]),'full_keys':[list(k) for k in keys],'signed_native_prefix_edges':cost})
out.sort(key=lambda x:(x['H2'],x['H3']))
assert len(out)==8
assert sorted(x['signed_native_prefix_edges'] for x in out)==[31,31,31,31,35,35,35,35]
if __name__=='__main__':
 print(json.dumps({'schema':'EC49FDS_H2_THREE_H3_TWO_EARLY_TWO_KEY_CENSUS_V1',
 'science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 'h2_accepted_single_words':6,'h3_accepted_single_words':38,
 'h2_rank9_three_word_subsets':6,'h3_rank9_two_word_subsets':16,
 'all_rank9_seed_combinations_examined':96,
 'two_key_seed_count':len(out),
 'two_key_seed_cost_multiset':sorted(x['signed_native_prefix_edges'] for x in out),
 'certificates':out},indent=2))
