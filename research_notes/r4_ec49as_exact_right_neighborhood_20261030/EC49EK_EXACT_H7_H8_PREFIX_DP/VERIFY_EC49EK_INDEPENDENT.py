#!/usr/bin/env python3
"""EC49EK cross-check: original EC49EG historical-path simulator and brute h=3 subsets."""
import json
from collections import defaultdict
from itertools import combinations
import VERIFY_EC49EG as old
import VERIFY_EC49EK as new

def brute_h3():
 base=('ce','de','ec','ed')
 groups=defaultdict(list)
 for w in new.returning(3):groups[new.pcount(new.native(w))].append(w)
 total=0;best=10**9;witness=None
 for fiber,ws in groups.items():
  for mask in range(1,1<<len(ws)):
   total+=1
   chosen=[w for i,w in enumerate(ws) if mask>>i&1]
   if old.modular_rank(old.signature(w) for w in chosen)!=9:continue
   cost=old.trie(base+tuple(chosen))
   if cost<best:best=cost;witness=(fiber,chosen)
 assert best==36 and total==12369
 return {'h3_total_nonempty_subsets':total,'exact_best_h2_h3':best,'witness':witness}

def run():
 assert tuple(old.ATOMS)==('N0','N1','N2','A0','A2','B0','B1','AB','BA')
 assert len(old.HISTORIES)==9
 # Independently reconstruct native history from the source exact checker.
 comparisons=[]
 for h in (7,8):
  represented={}
  for w in new.returning(h):
   k=(new.pcount(new.native(w)),new.transfer(new.native(w)))
   if k not in represented:represented[k]=w
  for (p,t),w in represented.items():assert old.signature(w)==t
  comparisons.append({'h':h,'distinct_p_and_transfer_pairs':len(represented),'all_signature_matches':True})
 base=('ce','de','ec','ed')
 schedule=[w for h in range(3,9) for w in ('feg'+'f'*(h-3),'gef'+'f'*(h-3))]
 allwords=base+tuple(schedule)
 assert old.trie(allwords)==new.trie_cost(allwords)==62
 assert len(set(new.pcount(new.native(w)) for w in allwords))==6
 assert len(set(new.transfer(new.native(w)) for w in allwords))==6
 x=(2,3,5,7,11,13); y=(3,4,7,11,13,17)
 for w in allwords:
  p=old.native(w)
  assert old.signature(w)==new.transfer(new.native(w))
  for hist in old.HISTORIES:
   for weights in (x,y):
    assert old.brc(hist+p,weights)==old.brc(hist,weights)*old.brc(p,weights)
 assert old.modular_rank(old.signature(w) for w in base)==9
 for h in range(3,9):
  ww=('feg'+'f'*(h-3),'gef'+'f'*(h-3))
  assert old.modular_rank(old.signature(w) for w in ww)==9
 return {'status':'PASS','finite_independent_h3':brute_h3(),
  'h7_h8_independent_seam_signature':comparisons,
  'history_realizations_count':len(old.HISTORIES),
  'all_2_to_8_full_rank_and_brc_exact':True,
  'cost_h2_to_h8':old.trie(allwords),
  'h2_to_h8_word_observations':len(allwords),
  'distinct_positive_brc_monomial_fibers':6,
  'distinct_seam_transfer_types':6}

if __name__=='__main__':print(json.dumps(run(),sort_keys=True,ensure_ascii=False,indent=2))
