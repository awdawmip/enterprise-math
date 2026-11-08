#!/usr/bin/env python3
"""Exact integer-only verifier for pooled full BRC native-X6 prefix duals.
Author finite certificate, NOT independent Driver admission.
"""
import json,sys
from collections import Counter,defaultdict
from WORD_MODEL_EC49FET import words_with_label, OPERATIONS,NEXT,OBS,ALPHABET
from EC49FEU_STANDALONE import keys as keygen
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def verify(path):
 C=json.load(open(path));assert C['schema']=='EC49FEW_UNIVERSAL_POOLED_PREFIX_DUAL_V1' and C['science_pin']==PIN
 mixed=C['mixed_horizon'];assert mixed==6
 high=set(C['late_high_horizons'])|{3}
 assert len(high)==5 and mixed in high and 9 in high
 assert keygen(3,frozenset((16,32)))==((3,1,1),)
 pool={(3,1,1)}
 for h in sorted(high-{3}):
  need=frozenset((16,)) if h==mixed else frozenset((16,32))
  pool.update(keygen(h,need))
 pool=tuple(sorted(pool));Q=C['Q'];assert type(Q)==int and Q>0
 gamma=C['gamma'];assert len(gamma)==23 and all(type(x)==int and x>=0 for x in gamma)
 sparse=C['t_sparse'];weight={int(i):int(v) for i,v in sparse}
 assert len(weight)==len(sparse) and all(i>=0 and v>0 for i,v in weight.items())
 index={};prefix_load=defaultdict(int);gi=0;word_count=0
 for h in range(2,10):
  labels=(1,8,16) if h==mixed else ((16,32) if h in high else (1,2,4,8))
  for label in labels:
   opts=sorted({word for k in pool for lab,word in words_with_label(h,k) if lab==label})
   assert opts,(h,label)
   for word in opts:
    pos=Counter(step for ch in word for step in OPERATIONS[ch]);assert len(word)==h
    assert tuple(pos[i]-pos[-i] for i in range(1,7))==(2,0,0,0,0,0)
    assert tuple(pos[i] for i in range(1,4)) in pool
    st=0
    for ch in word:st=NEXT[st][ALPHABET.index(ch)]
    assert OBS[st]==label
    pref=bytearray();score=0
    for ch in word:
     for step in OPERATIONS[ch]:
      pref.append(step+6);token=(gi,bytes(pref));idx=index.get(token)
      if idx is None:
       idx=len(index);index[token]=idx;prefix_load[bytes(pref)]+=weight.get(idx,0)
      score+=weight.get(idx,0)
    assert score>=gamma[gi],('word inequality',h,label,word,score,gamma[gi])
    word_count+=1
   gi+=1
 assert gi==23
 assert all(i<len(index) for i in weight)
 assert all(v<=Q for v in prefix_load.values()),'prefix capacity violation'
 LB=sum(gamma)
 assert LB>93*Q,('target',LB,Q)
 return {'late_high_horizons':sorted(high-{3}),'eligible_keys_pooled':len(pool),'observed_groups':gi,'all_candidate_words':word_count,'group_prefix_pair_constraints':len(index),'nonzero_dual_weights':len(weight),'lower_numerator':LB,'denominator':Q,'min_integer_cost':(LB+Q-1)//Q,'verified':'EXACT_INTEGER_PASS'}
if __name__=='__main__':
 for file in sys.argv[1:]:print(json.dumps(verify(file)),flush=True)