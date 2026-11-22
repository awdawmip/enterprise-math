#!/usr/bin/env python3
"""R284EN: exact graph deduction from frozen R284EM minima.
Run with optional R284EM_history_aware_tag_certificate.json in same directory;
otherwise uses embedded pinned published distance table, verified by paper link.
"""
import json
from pathlib import Path
EDGES = [(i,j) for i in range(4) for j in range(i+1,4)]
PINS = {
 'two_port': {'0-1':60,'0-2':9394,'0-3':9526,'1-2':9289,'1-3':9421,'2-3':60},
 'four_port':{'0-1':60,'0-2':9432,'0-3':9564,'1-2':9327,'1-3':9459,'2-3':60}
}
TAGS={
 'a': lambda u: u & 1,
 'b': lambda u: (u>>1)&1,
 'a_xor_b': lambda u: (u&1)^((u>>1)&1)
}
def edges_at_E(d,e):
 return {(u,v) for u,v in EDGES if d[f'{u}-{v}']<=2*e}
def allowed_t(T,edges):
 return all(T(u)!=T(v) for u,v in edges)
def num_noiseless_redundancy(d,T,e,k):
 return 0 if allowed_t(T,edges_at_E(d,e)) else 2*k+1

def main():
 p=Path(__file__).with_name('R284EM_history_aware_tag_certificate.json')
 if p.exists():
  z=json.loads(p.read_text(encoding='utf-8'))
  assert z['pinned_source_commit']=='acba2d8667903434aaa2a10720f43637fcc2421b'
  for kind in PINS:
   assert z[kind]['min_cross_label_linf']==PINS[kind]
 answer={}
 for kind,d in PINS.items():
  tau=4697 if kind=='two_port' else 4716
  zero_threshold={name:(min(d[f'{u}-{v}'] for u,v in EDGES if fn(u)==fn(v))-1)//2 for name,fn in TAGS.items()}
  assert zero_threshold == ({'a':4696,'b':29,'a_xor_b':4644} if kind=='two_port' else {'a':4715,'b':29,'a_xor_b':4663})
  # All 16 functions from four logical source classes to one trusted bit.
  mk=lambda m: lambda u: (m>>u)&1
  solutions={e:tuple(m for m in range(16) if allowed_t(mk(m),edges_at_E(d,e))) for e in range(8657)}
  assert all(solutions[e] for e in range(tau))
  assert all(not solutions[e] for e in range(tau,8657))
  assert solutions[tau-1]==(5,10)
  assert allowed_t(TAGS['a'],edges_at_E(d,tau-1))
  assert not allowed_t(TAGS['a'],edges_at_E(d,tau))
  assert {(0,1),(1,2),(0,2)}.issubset(edges_at_E(d,tau))
  for k in range(9):
   # One trusted bit a, one binary residual codeword of length 2k+1,
   # codewords 0^(2k+1),1^(2k+1), correcting k flips.
   cw0='0'*(2*k+1);cw1='1'*(2*k+1)
   assert sum(u!=v for u,v in zip(cw0,cw1))==2*k+1
   for e in (0,29,30,tau-1,tau,8656):
    assert num_noiseless_redundancy(d,TAGS['a'],e,k)==(0 if e<tau else 2*k+1)
  answer[kind]={
   'optimal_one_trusted_bit_no_noisy_storage_error_ceiling':tau-1,
   'first_unavoidable_untrusted_bit_error':tau,
   'optimal_trusted_bit_name':'a=(i>>12)&1',
   'zero_untrusted_storage_error_ceiling_by_source_bit':zero_threshold,
   'unique_optimal_trusted_bit_at_ceiling_up_to_complement':list(solutions[tau-1]),
   'truth_table_mask_a':10,
   'result_for_error_E_0_to_8656':'n=0 if E<%d; n=2k+1 otherwise'%tau,
   'all_16_trusted_functions_checked_each_E':8657,
   'max_k_checked':8
  }
 print(json.dumps({'status':'PASS','source':'R284EM exact six min distances','results':answer},ensure_ascii=False,indent=2))
 Path(__file__).with_name('R284EN_trusted_witness_certificate.json').write_text(json.dumps({'schema':'R284EN_TRUSTED_INVARIANT_SIDE_INFO_V1','verification':'exact integer graph enumeration from pinned R284EM distances','frozen_source_commit':'acba2d8667903434aaa2a10720f43637fcc2421b','source_certificate':'research_notes/portable_direct/R284EM_history_aware_tag_certificate.json','results':answer,'review':'NOT_REVIEWED'},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
if __name__=='__main__':
 main()
