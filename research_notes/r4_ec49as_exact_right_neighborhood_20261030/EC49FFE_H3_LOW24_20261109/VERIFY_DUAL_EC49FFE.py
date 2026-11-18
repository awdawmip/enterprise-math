#!/usr/bin/env python3
"""Independent integer-only check of EC49FFE full-key 106-edge exact dual.

Python standard library only. Adjacent VERIFY_EC49FFE.py and
VERIFY_OPT_EC49FFE.py provide original frozen DFA and legal-word generator.
No MILP/LP solver and no floating point arithmetic is used here.
"""
import json
from pathlib import Path
from collections import Counter
from VERIFY_OPT_EC49FFE import KEYS,HIGH,GROUPS,PIN,get_choices,prefixes,check_witness

root=Path(__file__).resolve().parent
J=json.loads((root/'DUAL_INDEX_CERT_EC49FFE.json').read_text())
assert J['format']=='EC49FFE_EXACT_GROUP_PREFIX_DUAL_V1'
assert J['science_pin']==PIN and tuple(map(tuple,J['keys']))==KEYS
assert tuple(J['high'])==HIGH and tuple(map(tuple,J['groups']))==GROUPS
assert J['prefix_index_sort']=='(length, signed_axis_prefix_tuple)'
Q=J['Q']
assert isinstance(Q,int) and Q>=1
choices=get_choices()
assert len(choices)==len(GROUPS)==24
allprefix=sorted({p for pool in choices for w in pool for p in prefixes(w)},
                 key=lambda p:(len(p),p))
assert len(allprefix)==J['prefix_count']==1327
lookup={p:i for i,p in enumerate(allprefix)}
gamma=J['gamma'];weightlists=J['weights_by_group']
assert len(gamma)==len(weightlists)==len(GROUPS)
assert all(isinstance(v,int) and v>=0 for v in gamma)
assert all(all(isinstance(v,int) and 0<=v<len(allprefix) for v in xs) for xs in weightlists)
assert all(len(xs)==len(set(xs)) for xs in weightlists)
usage=Counter(idx for xs in weightlists for idx in xs)
assert max(usage.values())<=Q
for g,pool in enumerate(choices):
    weightset=set(weightlists[g])
    for w in pool:
        total=sum(idx in weightset for idx in (lookup[p] for p in prefixes(w)))
        assert total>=gamma[g],(GROUPS[g],w,total,gamma[g])
assert sum(gamma)==106*Q
assert check_witness()==106
print(json.dumps({'status':'EXACT_INTEGER_DUAL_PASS', 'science_pin':PIN,
                  'model':'original ordered signed-X6 steps / full BRC keys / DFA',
                  'groups':len(GROUPS),'candidate_words':sum(map(len,choices)),
                  'prefixes':len(allprefix),'checked_group_word_inequalities':sum(map(len,choices)),
                  'checked_prefix_budgets':len(allprefix),
                  'nonzero_integer_weights':sum(map(len,weightlists)),
                  'denominator':Q,'dual_numerator':sum(gamma),
                  'lower_bound':sum(gamma)//Q,'verified_upper_witness':106,
                  'exact_fixed_key_optimum':106},indent=2))
