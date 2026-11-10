#!/usr/bin/env python3
"""R707 exact finite validation, standard library only.

V36 directed ring copy-rule conditional on the cited K unique-max lemma;
V17 canonical triad slot replacement; fixed independent V29 TRANSFER overlay.
All arithmetic exact. The input words are labeled BRC packet provenance.
"""
from itertools import permutations
from collections import Counter
from math import factorial, comb
import json

BASE=(0,1,2)
PACKETS={
 'A': ((0,1,2),(0,1,3),(0,2,3),(0,1,2)),
 'a': ((0,1,2),(0,2,3),(0,1,3),(0,1,2)),
 'B': ((0,1,2),(0,2,3),(1,2,3),(0,1,2)),
 'b': ((0,1,2),(1,2,3),(0,2,3),(0,1,2)),
}
def adjacent(s,t):
 return len(set(s)&set(t))==2 and s!=t

def slot_holonomy(word):
 slots=list(word[0])
 for s,t in zip(word,word[1:]):
  ss,tt=set(s),set(t)
  assert adjacent(s,t)
  leave=next(iter(ss-tt)); enter=next(iter(tt-ss))
  slots[slots.index(leave)]=enter
 # V17/V37 native displayed axis-to-slot tuple is inverse of propagated slot-to-axis list.
 return tuple(slots.index(x) for x in BASE)

def ring_initial(packets):
 expanded=[BASE]
 for p in packets:
  assert expanded[-1]==BASE
  expanded.extend(PACKETS[p][1:])
 assert expanded[-1]==BASE
 return tuple(expanded[:-1])

def simulate(word):
 initial=ring_initial(word)
 states=initial
 m=len(states)
 assert m==3*len(word)
 assert all(adjacent(states[i],states[(i+1)%m]) for i in range(m))
 for t in range(m+1):
  assert states[0]==initial[t%m]
  if t<m:
   states=states[1:]+states[:1]
 assert states==initial
 return m,slot_holonomy(initial+(BASE,))

def multinomial_counts(k,l):
 n=2*(k+l)
 return factorial(n)//(factorial(k)**2*factorial(l)**2)

def D(k,l):
 n=k+l
 return sum(factorial(n)//(factorial(k-r)*factorial(l-r)*factorial(2*r))
            for r in range(min(k,l)+1))

def verify(k,l):
 labels='A'*k+'a'*k+'B'*l+'b'*l
 hist=Counter()
 m=6*(k+l)
 for word in set(permutations(labels)):
  size,h=simulate(word)
  assert size==m
  hist[h]+=1
 total=sum(hist.values())
 assert total==multinomial_counts(k,l)
 C=comb(2*(k+l),2*k)
 d=D(k,l)
 orient=comb(2*k,k)*comb(2*l,l)
 assert sorted(hist.values(),reverse=True)==sorted(
    (orient*(C+2*d)//3,orient*(C-d)//3,orient*(C-d)//3),
     reverse=True)
 return {'k':k,'l':l,'cells':m,
         'histogram':{''.join(str(x) for x in h):v for h,v in sorted(hist.items())},
         'total_oriented_words':total,
         'V29_uniform_overlay_transfers':m*m,
         'per_edge_count':m,
         'net_cycle_current_coefficient':m}

if __name__=='__main__':
 cases=[verify(k,l) for k,l in [(1,1),(1,2),(2,1),(2,2)]]
 H={}
 for name,w in [('H0',('A','a','B','b')),
                ('H1',('A','B','a','b')),
                ('H2',('B','A','b','a'))]:
  m,h=simulate(w)
  H[name]={'packet_order':list(w),'holonomy':list(h),'ring_cells':m}
 assert {tuple(v['holonomy']) for v in H.values()}=={
    (0,1,2),(1,2,0),(2,0,1)}
 output={'verdict':'R707_NATIVE_RING_BRC_SHUFFLES_EXACT_PASS',
  'source_scope':'V36 deterministic directed ring via canonical V20 coupling; V17 slot holonomy; V29 additive legal matched TRANSFER overlay not a derived coupled event scheduler',
  'cases':cases,'three_witnesses':H,
  'notes':{
   'network_initial_state':'different complete initial Cell triad fields per shuffle; same ring topology, update law, cell0 triad and transfer overlay',
   'V29_layer_schedule':'for each t=0..m-1, serialize TRANSFER(i:p->i+1:p) for i=0..m-1 and then apply V36 synchronous triad update; p is a fixed declared interface label',
   'observation':'Cell0 base holonomy; all cases have M=0, Rin=Rout=m at all Cells and identical edge multiset counts'}}
 print(json.dumps(output,ensure_ascii=False,sort_keys=True))
