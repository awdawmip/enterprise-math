#!/usr/bin/env python3
"""R667. Fixed multiplicities of the three V17-J(6,3) reflection loops.

Exact S3, independently cross-checked by (i) count-lattice DP,
(ii) enumeration of every 3-letter word of length <=9, and
(iii) direct slot inheritance on actual 3-step J(6,3) loops.
No third-party dependencies and no floating-point operations.
"""
from itertools import product, permutations
from collections import Counter, defaultdict
import json
from pathlib import Path

IDENT=(0,1,2)
REFLECTIONS={'A':(0,2,1),'B':(2,1,0),'C':(1,0,2)}
O=(0,1,2)
LOOPS={
 'A':(O,(0,1,3),(0,2,3),O),
 'B':(O,(0,1,3),(1,2,3),O),
 'C':(O,(0,2,3),(1,2,3),O),
}

def multiply(p,q): return tuple(p[q[i]] for i in range(3))
def sign(p):return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
def slot_step(u,v,f):
    assert len(set(u)&set(v))==2
    leave=next(iter(set(u)-set(v)))
    enter=next(iter(set(v)-set(u)))
    by_member=dict(zip(u,f)); by_member[enter]=by_member[leave]
    return tuple(by_member[t] for t in v)
def native_word(word):
    f=IDENT
    counts=Counter()
    for token in word:
        ring=LOOPS[token]
        for u,v in zip(ring,ring[1:]):
            f=slot_step(u,v,f)
            counts[(u,v)]+=1
    return f, tuple(sorted(counts.items()))

def formula(c):
    positives=sorted(x for x in c if x)
    if len(positives)<=1:return 1
    if len(positives)==2:return min(3, positives[0]+1)
    return 3

assert all(multiply(v,v)==IDENT and sign(v)==1 for v in REFLECTIONS.values())
assert len(set(REFLECTIONS.values()))==3
assert all(native_word(k)[0]==REFLECTIONS[k] for k in 'ABC')

# Dynamic programming over multiplicities (0..12 per reflection).
B=12
T={}
for a in range(B+1):
 for b in range(B+1):
  for c in range(B+1):
   count=(a,b,c)
   if count==(0,0,0): states={IDENT}
   else:
    states=set()
    for i,key in enumerate('ABC'):
     if count[i]:
      prev=list(count); prev[i]-=1
      states.update(multiply(h,REFLECTIONS[key]) for h in T[tuple(prev)])
   assert len(states)==formula(count),(count,states)
   assert all(sign(h)==sum(count)%2 for h in states)
   T[count]=states

# Independently enumerate every literal word of lengths 0 through 9.
full=defaultdict(set)
words=0
native_checks=0
for length in range(10):
 for token_tuple in product('ABC',repeat=length):
  w=''.join(token_tuple)
  key=tuple(w.count(t) for t in 'ABC')
  f=IDENT
  for t in w:f=multiply(f,REFLECTIONS[t])
  assert sign(f)==length%2
  full[key].add(f)
  words+=1
  if length<=7:
   native, hist=native_word(w)
   assert native==f
   # Every block is closed at 012, so counts are additive by block.
   expect=Counter()
   for token in w:
    for edge in zip(LOOPS[token],LOOPS[token][1:]):expect[edge]+=1
   assert hist==tuple(sorted(expect.items()))
   native_checks+=1
for counts,states in full.items():
 assert states==T[counts]
 assert len(states)==formula(counts)

# Six equal directed histograms, three different frames with three loop kinds.
examples={}
for order in ['ABC','ACB','BAC','BCA','CAB','CBA']:
 f,hist=native_word(order)
 examples[order]={'frame':list(f),'frame_parity':sign(f)}
assert len({tuple(x['frame']) for x in examples.values()})==3
assert len({native_word(order)[1] for order in examples})==1

# Two-loop family: first fully saturated at two copies of each.
for order in ['AABB','ABAB','BABA']:
 assert native_word(order)[0] in T[(2,2,0)]
assert len({native_word(order)[0] for order in ['AABB','ABAB','BABA']})==3

# A proper subset 0<m,n and min=1 produces exactly two frames.
assert len(T[(2,1,0)])==2
# For arbitrary counts with all 3 kinds, each of the 3 parity-compatible frames occurs.
three_checks=sum(all(v>0 for v in key) for key in T)
assert three_checks==B**3

out={
 'marker':'R667_THREE_REFLECTION_FIXED_MULTIPLICITY_S3_SPECTRUM_EXACT_PASS',
 'model':'V17, 20 vertices J(6,3), fixed base 012, three closed length-3 reflection loops',
 'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
 'source_predecessors':{
  'R665':'c28925c3c0881894111a7049e16216fb2656cd60',
  'R666':'42b81a59b9bdb174a01c86e1fbf4326a8d141101'},
 'theorem':'support<=1:1; support==2:min(3,1+min(positive counts)); support==3:3',
 'three_loops':{k:[list(x) for x in v] for k,v in LOOPS.items()},
 'one_block_frames':{k:list(v) for k,v in REFLECTIONS.items()},
 'dp_bound_per_count':B,'dp_count_vectors':len(T),'dp_all_three_support':three_checks,
 'exhaustive_max_block_word_length':9,'exhaustive_words':words,
 'exhaustive_distinct_count_vectors':len(full),'native_slot_historic_checks':native_checks,
 'three_block_witness':examples,
 'same_complete_directed_histogram':True,
 'two_support_first_three_value_count':'A2B2, four blocks',
 'three_support_first_three_value_count':'A1B1C1, three blocks',
 'scope':'arbitrary permutations of closed reflection blocks, not an autonomous V29/V27 schedule',
 'review':'AUTHOR_SIDE_UNREVIEWED'
}
path=Path(__file__).with_name('R667_EVIDENCE.json')
path.write_text(json.dumps(out,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
print(out['marker'])
print('DP vectors:',len(T),'all three:',three_checks,'words:',words,'count vectors:',len(full),'native slot checks:',native_checks)
print('ABC six permutations:',examples)
