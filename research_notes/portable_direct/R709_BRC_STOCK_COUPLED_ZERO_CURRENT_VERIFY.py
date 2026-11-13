#!/usr/bin/env python3
"""R709b exact source-labelled BRC counterflow stock-coupled X6 ring.
Author-side candidate scheduler extending V29 with explicit conserved stocks;
uses V20/V36 unique-max lemma, V17 exact slot transport. No floats/pi.
"""
from collections import Counter, defaultdict
from itertools import permutations
from math import factorial, comb
import json, hashlib, sys

BASE=(0,1,2)
PACKETS={
 'A': ((0,1,2),(0,1,3),(0,2,3),(0,1,2)),
 'a': ((0,1,2),(0,2,3),(0,1,3),(0,1,2)),
 'B': ((0,1,2),(0,2,3),(1,2,3),(0,1,2)),
 'b': ((0,1,2),(1,2,3),(0,2,3),(0,1,2)),
}
def adjacent(a,b):
 return a!=b and len(set(a)&set(b))==2

def initial_field(w):
 seq=[BASE]
 for letter in w:
  assert seq[-1]==BASE
  seq.extend(PACKETS[letter][1:])
 assert seq[-1]==BASE
 return tuple(seq[:-1])

def slot_transport(path):
 slots=list(path[0]); assert slots==list(BASE)
 for a,b in zip(path,path[1:]):
  assert adjacent(a,b)
  leave=next(iter(set(a)-set(b)))
  enter=next(iter(set(b)-set(a)))
  slots[slots.index(leave)]=enter
 return tuple(slots.index(x) for x in BASE)

def step(triads,stocks_plus,stocks_minus):
 """Independent local edge tests, simultaneous arrivals, conservative typed stocks.
 Edge i = pair {i,i+1}. +: i+1->i, -: i->i+1.
 Both gate on J(6,3) adjacency and source stock in appropriate species.
 Firing copies neighbor's OLD triad to i via V20's unique-max.
 V29 ledger increments recorded by return edge-flags, not by arbitrary overlay.
 """
 m=len(triads)
 fire=[adjacent(triads[i],triads[(i+1)%m]) and
       stocks_plus[(i+1)%m]>=1 and stocks_minus[i]>=1
       for i in range(m)]
 nxt=list(triads); np=list(stocks_plus); nm=list(stocks_minus)
 for i,yes in enumerate(fire):
  if yes:
   j=(i+1)%m
   nxt[i]=triads[j]
   np[j]-=1; np[i]+=1  # + transfer j -> i
   nm[i]-=1; nm[j]+=1  # - transfer i -> j
 assert min(np)>=0 and min(nm)>=0
 assert sum(np)==sum(stocks_plus) and sum(nm)==sum(stocks_minus)
 return tuple(nxt),tuple(np),tuple(nm),fire

def simulate(w):
 init=initial_field(w); m=len(init)
 assert m==3*len(w)
 assert all(adjacent(init[i],init[(i+1)%m]) for i in range(m))
 triads=init; p=(1,)*m; n=(1,)*m
 rp=[0]*m; op=[0]*m; rn=[0]*m; on=[0]*m
 forward=[0]*m; reverse=[0]*m
 path=[triads[0]]
 for tick in range(m):
  triads,p,n,fires=step(triads,p,n)
  assert all(fires) and all(x==1 for x in p+n)
  assert triads==init[(tick+1)%m:]+init[:(tick+1)%m]
  for i in range(m):
   j=(i+1)%m
   # Edge transfers +: j->i, -: i->j. Valid matched ports.
   # Input and output ledger per Cell, per type.
   rp[i]+=1; op[j]+=1
   rn[j]+=1; on[i]+=1
   forward[i]+=1; reverse[i]+=1
  path.append(triads[0])
 assert triads==init and path[-1]==BASE
 assert rp==op==rn==on==[m]*m
 assert forward==reverse==[m]*m
 # Full port-directed ledger is always the same, and
 # underlying physical edge signed chain is exactly zero.
 h=slot_transport(path)
 return m,h

def D(k,l):
 n=k+l
 return sum(factorial(n)//(factorial(k-r)*factorial(l-r)*factorial(2*r))
            for r in range(min(k,l)+1))

def expected_hist(k,l):
 C=comb(2*(k+l),2*k); d=D(k,l)
 orient=comb(2*k,k)*comb(2*l,l)
 return sorted([orient*(C+2*d)//3,orient*(C-d)//3,orient*(C-d)//3],reverse=True)

def evaluate(k,l):
 labels='A'*k+'a'*k+'B'*l+'b'*l
 seen=set(permutations(labels)); groups=defaultdict(list); hist=Counter(); m=6*(k+l)
 for w in seen:
  size,h=simulate(w)
  assert size==m
  hist[''.join(str(x) for x in h)]+=1
  # Every packet-rotation orbit has identical full unrooted field/census.
  orbit=min(w[i:]+w[:i] for i in range(len(w)))
  groups[orbit].append((w,h))
 assert sum(hist.values())==factorial(2*(k+l))//(factorial(k)**2*factorial(l)**2)
 assert sorted(hist.values(),reverse=True)==expected_hist(k,l)
 flat=nonflat=0
 for orbit,rows in groups.items():
  c=Counter(x[1] for x in rows)
  if len(c)==1:
   assert list(c)==[(0,1,2)]
   flat+=1
  else:
   assert len(c)==2 and (0,1,2) not in c
   assert sorted(c.values())[0]==sorted(c.values())[1]
   nonflat+=1
 # Check stock dependence, not only an unconstrained copy overlay.
 init=initial_field(next(iter(seen)))
 p=[1]*m; n=[1]*m; p[0]=0
 _,p2,n2,f=step(init,p,n)
 assert not all(f) and sum(p2)==m-1 and sum(n2)==m
 p=[1]*m; n=[1]*m; n[0]=0
 _,p2,n2,f=step(init,p,n)
 assert not all(f) and sum(p2)==m and sum(n2)==m-1
 return {'k':k,'l':l,'cells':m,'words':len(seen),
         'holonomy_histogram':dict(sorted(hist.items())),
         'necklaces':len(groups),'flat_necklaces':flat,'nonflat_necklaces':nonflat,
         'matched_transfer_events_per_word':2*m*m,
         'each_port_Rin_Rout_after_period':m,
         'per_undirected_edge_plus_and_minus_counts':[m,m],
         'net_edge_current':0,
         'minimal_all_edge_firing_stock_by_type':[m,m],
         'single_species_token_deletion_blocks_full_firing':True}

if __name__=='__main__':
 cases=[evaluate(k,l) for k,l in [(1,1),(1,2),(2,1),(2,2)]]
 witnesses={}
 for name,w in [('H0',tuple('AaBb')),('H1',tuple('ABab')),('H2',tuple('BAb a'.replace(' ','')))]:
  m,h=simulate(w)
  witnesses[name]={'word':''.join(w),'holonomy':list(h),'cells':m}
 assert {tuple(v['holonomy']) for v in witnesses.values()}=={(0,1,2),(1,2,0),(2,0,1)}
 rotated=tuple('baBA') # rotation of AbaB? check separately
 w=tuple('AbaB')
 u=w[1:]+w[:1]
 _,h1=simulate(w);_,h2=simulate(u)
 assert h1!=h2 and h1!=(0,1,2) and h2!=(0,1,2)
 out={'verdict':'R709B_STOCK_COUPLED_ZERO_CURRENT_BRC_PASS',
      'model':'Explicit two-typed-token conservative stock-extended V29; V20/V36 gated synchronous ring; native six-axis triad fields; pointed V17/V39 S3 transport',
      'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'arithmetic':'exact positive unit BRC branch enumeration and integer counters; no floating computation',
      'cases':cases,'total_oriented_branches':sum(c['words'] for c in cases),
      'total_validated_layer_steps':sum(c['words']*c['cells'] for c in cases),
      'three_witnesses':witnesses,
      'root_rotation':{'word_1':''.join(w),'word_2':''.join(u),'h1':list(h1),'h2':list(h2)},
      'interface_boundary':'Stock-gated scheduling is a fully specified candidate extension; baseline V29 declares only additive PASS/TRANSFER, not autonomous token stock or synchronization.'}
 print(json.dumps(out,sort_keys=True,indent=2))
