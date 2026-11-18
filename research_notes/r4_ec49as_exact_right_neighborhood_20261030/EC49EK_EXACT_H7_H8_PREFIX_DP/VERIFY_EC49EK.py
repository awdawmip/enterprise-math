#!/usr/bin/env python3
"""EC49EK: exact finite group-Steiner dynamic program on *native signed-X6* prefix trees.

Computes the H=2 plus H=7 lower-bound optimization, and checks it against an
explicit nested all-horizon equal-positive-count witness. Requires Python stdlib.
The rank predicate is exact over Q because 9x9 integer 0/1 minors are bounded
by 9^(9/2) < 1,000,003, so modular rank 9 iff rational rank 9.
"""
from collections import defaultdict, Counter
from itertools import product
from hashlib import sha256
import json
import math
import sys
import time

OP={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ATOMS=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')
P=1000003

def native(w):return tuple(s for ch in w for s in OP[ch])
def pcount(seq):return tuple(seq.count(i) for i in range(1,7))
def displacement(seq):return tuple(seq.count(i)-seq.count(-i) for i in range(1,7))
def state(path,s='N',last=0):
 for v in path:
  A=last==1 and v==2; B=last==2 and v==1
  if s=='N':
   if A:s='A'
   elif B:s='B'
  elif s=='A' and B:s='AB'
  elif s=='B' and A:s='BA'
  last=v
 return s,last

def transfer(path):
 return tuple(BUCKETS.index(state(path,s,last)[0]) for s,last in ATOMS)

def transfer_cols(t):
 return tuple(sum((1<<i) for i,x in enumerate(t) if x==j) for j in range(5))

def rank(cols):
 piv={}
 for bits in cols:
  v=[(bits>>i)&1 for i in range(9)]
  for j in range(9):
   if not v[j]:continue
   if j in piv:
    factor=v[j];row=piv[j]
    for k in range(j,9):v[k]=(v[k]-factor*row[k])%P
   else:
    inv=pow(v[j],-1,P)
    piv[j]=[(x*inv)%P for x in v]
    break
 return len(piv)

def rank_words(ws):return rank([c for w in ws for c in transfer_cols(transfer(native(w)))])

def prefix_list(path):return [path[:k] for k in range(1,len(path)+1)]
def trie_cost(ws):return len(set().union(*(set(prefix_list(native(w))) for w in ws)))

def returning(h):
 """Complete grammar: zero-displacement operations c,d,f,g; e count=a count+1; b=0."""
 for letters in product('acdefg',repeat=h):
  if letters.count('e')!=letters.count('a')+1:continue
  w=''.join(letters)
  yield w

def minimal_rank_type_subsets(types):
 ts=tuple(types)
 full=[]
 for mask in range(1,1<<len(ts)):
  if any((mask & m)==m for m in full):continue
  if rank([col for i,t in enumerate(ts) if mask>>i&1 for col in transfer_cols(t)])==9:
   full.append(mask)
 return ts,full

class Node:
 __slots__=('kids','term')
 def __init__(self):self.kids={};self.term=None

def solve_fixed_fiber(type_words, required, base):
 """Exact minimum incremental prefix count needed to hit each required terminal type.

Bottom-up tree DP: for every prefix node and mask of required observation
classes, dp[mask] is the min newly charged native edges in its subtree.
Merge children by mask union and minimum. The empty mask has cost zero.
"""
 idx={t:i for i,t in enumerate(required)}
 root=Node()
 nodes=1
 for t in required:
  for w in type_words[t]:
   node=root
   for p in native(w):
    if p not in node.kids:node.kids[p]=Node();nodes+=1
    node=node.kids[p]
   assert node.term is None
   node.term=(idx[t],w)
 def dp(v,path):
  out={0:(0,())}
  if v.term is not None:
   i,w=v.term
   out[1<<i]=(0,(w,))
  for p,child in v.kids.items():
   pp=path+(p,)
   childstates=dp(child,pp)
   weight=0 if pp in base else 1
   # A chosen child contributes the incoming edge once, any number of leaves.
   nxt=dict(out)
   for m,(cost,chosen) in out.items():
    for cm,(ccost,cwords) in childstates.items():
     if not cm:continue
     mnew=m|cm
     vnew=cost+ccost+weight
     old=nxt.get(mnew)
     if old is None or (vnew,len(chosen+cwords),chosen+cwords)<(old[0],len(old[1]),old[1]):
      nxt[mnew]=(vnew,chosen+cwords)
   out=nxt
  return out
 result=dp(root,tuple())
 return result[(1<<len(required))-1],nodes

def verify_h2():
 g=defaultdict(list)
 for w in returning(2):g[pcount(native(w))].append(w)
 assert sum(map(len,g.values()))==8
 possibles=[]
 for fiber,ws in sorted(g.items()):
  ts=defaultdict(list)
  for w in ws:ts[transfer(native(w))].append(w)
  types,masks=minimal_rank_type_subsets(ts)
  for m in masks:
   required=[types[i] for i in range(len(types)) if (m>>i)&1]
   value,nodes=solve_fixed_fiber(ts,required,set())
   possibles.append((value[0],fiber,tuple(sorted(value[1]))))
 assert len(possibles)==1,possibles
 cost,fiber,ws=possibles[0]
 assert fiber==(3,1,1,0,0,0) and cost==28 and set(ws)=={'ce','de','ec','ed'}
 return {'mandatory_words':list(ws),'fiber':fiber,'trie_cost':cost,'rank':rank_words(ws)}

def execute(H=7):
 start=time.monotonic()
 h2=verify_h2()
 base_words=tuple(h2['mandatory_words'])
 base=set().union(*(set(prefix_list(native(w))) for w in base_words))
 fibers=defaultdict(lambda:defaultdict(list))
 for w in returning(H):
  p=native(w)
  assert displacement(p)==(2,0,0,0,0,0)
  fibers[pcount(p)][transfer(p)].append(w)
 stats=[]; best=None
 type_dist=Counter()
 for fiber,g in sorted(fibers.items()):
  types,masks=minimal_rank_type_subsets(g)
  type_dist[len(types)]+=1
  if not masks:
   stats.append({'p':fiber,'words':sum(map(len,g.values())),'types':len(types),'rank_max':rank([c for ty in types for c in transfer_cols(ty)]),'min_added':None})
   continue
  best_fiber=None
  for mask in masks:
   required=tuple(types[i] for i in range(len(types)) if (mask>>i)&1)
   (extra,ws),nnodes=solve_fixed_fiber(g,required,base)
   if best_fiber is None or extra<best_fiber[0]:best_fiber=(extra,tuple(ws),len(required),nnodes)
  extra,ws,necessary,nodecount=best_fiber
  assert pcount(native(ws[0]))==fiber
  assert len({pcount(native(w)) for w in ws})==1
  assert rank_words(ws)==9
  assert trie_cost(base_words+ws)==28+extra
  item={'p':fiber,'words':sum(map(len,g.values())),'types':len(types),'minimal_rank_masks':len(masks),'necessary_types':necessary,'min_added':extra,'prefix_nodes':nodecount,'witness_words':list(ws)}
  stats.append(item)
  if best is None or (extra,fiber)<(best['min_added'],tuple(best['p'])):best=item
 print('H',H,'fibers',len(fibers),'words',sum(sum(map(len,g.values())) for g in fibers.values()),'best',best['min_added'],'time',time.monotonic()-start,file=sys.stderr)
 # Upper witness extends the h2 base with two nested equal-count paths for each 3..H.
 schedule={h:['feg'+'f'*(h-3),'gef'+'f'*(h-3)] for h in range(3,H+1)}
 for h,ws in schedule.items():
  assert all(displacement(native(w))==(2,0,0,0,0,0) for w in ws)
  assert len({pcount(native(w)) for w in ws})==1
  assert rank_words(ws)==9
 joint=base_words+tuple(w for h in sorted(schedule) for w in schedule[h])
 upper=trie_cost(joint)
 assert upper==4*H+30
 assert 28+best['min_added']<=upper
 return {'status':'PASS','scope':'Exact h=2+h='+str(H)+' lower-bound problem; full 2..'+str(H)+' upper witness',
  'pinned_model':{'operations':{k:list(v) for k,v in OP.items()},'history_atoms':[list(t) for t in ATOMS],
    'BRC':'two independent positive multiplicative instruments; cached by full six-axis positive step counts'},
  'h2':h2,'h'+str(H):{'total_returning_words':sum(sum(map(len,g.values())) for g in fibers.values()),
    'fibers_total':len(fibers),'fiber_types_distribution':dict(type_dist),
    'full_rank_fibers':sum(row['min_added'] is not None for row in stats),
    'minimal_rank_subsets_computed_exactly':sum(row.get('minimal_rank_masks',0) for row in stats),
    'minimum_added_edges_over_all_fibers':best['min_added'],
    'base_plus_h'+str(H)+'_minimum_native_edges':28+best['min_added'],
    'best_fiber':best,'per_fiber_exact_minima':stats},
  'complete_all_horizons_witness':{'schedule':schedule,'joint_cost':upper,
    'prefix_witness_h2':list(base_words),
    'all_within_horizon_positive_count_fibers_equal':True,
    'each_horizon_nine_atom_rank':9},
  'evidence_method':'Finite full grammar enumeration, exhaustive rank subset masks, exact prefix-trie masked DP. Rank over GF(1000003) is exact for full rank of nine-row 0/1 matrix via determinant bound.'}

if __name__=='__main__':
 obj=execute(int(sys.argv[1]) if len(sys.argv)>1 else 7)
 print(json.dumps(obj,sort_keys=True,ensure_ascii=False,indent=2))
