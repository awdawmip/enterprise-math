#!/usr/bin/env python3
"""EC49EG: all-h native X6 prefix-optimality for the full a-g language.

Self-contained standard-library exact reproduction, using nine real ten-step
native-X6 histories, integer terminal transfers, and two positive BRC channels.
Proof of all-h minimax lower bound is mathematical, documented in README.
"""
from collections import defaultdict
from itertools import product
import json

OPS = {
 'a':(-1,-1), 'b':(-2,-2),
 'c':(1,2,-1,-2), 'd':(2,1,-2,-1),
 'e':(3,1,1,-3), 'f':(1,-1), 'g':(2,-2),
}
BUCKETS=('N','A','B','AB','BA')
ATOMS=('N0','N1','N2','A0','A2','B0','B1','AB','BA')


def native(word):return tuple(s for ch in word for s in OPS[ch])
def positive(seq):return tuple(sum(s==j for s in seq) for j in range(1,7))
def displacement(seq):return tuple(sum(1 if s>0 else -1 for s in seq if abs(s)==j) for j in range(1,7))
def brc(seq,x):
 p=positive(seq);return __import__('math').prod(x[i]**p[i] for i in range(6))

def label(seq,s='N',previous=0):
 for step in seq:
  A=(previous==1 and step==2)
  B=(previous==2 and step==1)
  if s=='N':s='A' if A else 'B' if B else 'N'
  elif s=='A' and B:s='AB'
  elif s=='B' and A:s='BA'
  previous=step
 return s

def history_atom(seq):
 s=label(seq); last=seq[-1]
 if s=='N':return 'N1' if last==1 else 'N2' if last==2 else 'N0'
 if s=='A':return 'A2' if last==2 else 'A0'
 if s=='B':return 'B1' if last==1 else 'B0'
 return s

def find_history_atoms():
 remain={-2:2,-1:4,1:2,2:2}; path=[];hits={}
 def dfs():
  if len(hits)==9:return
  if len(path)==10:
   hits.setdefault(history_atom(path),tuple(path));return
  for v in (-2,-1,1,2):
   if remain[v]:
    remain[v]-=1;path.append(v);dfs();path.pop();remain[v]+=1
    if len(hits)==9:return
 dfs();assert set(hits)==set(ATOMS)
 return tuple(hits[a] for a in ATOMS)
HISTORIES=find_history_atoms()

def signature(word):
 path=native(word)
 assert displacement(path)==(2,0,0,0,0,0)
 return tuple(BUCKETS.index(label(path,label(h),h[-1])) for h in HISTORIES)

def modular_rank(sigs,p=1000003):
 """Exact Q-full-rank decision for nine-row 0/1 matrix by Hadamard bound."""
 piv={};r=0
 for sig in sigs:
  for bucket in range(5):
   col=[int(x==bucket) for x in sig]
   for q in sorted(piv):
    if col[q]:
     v=col[q];col=[(x-v*y)%p for x,y in zip(col,piv[q])]
   if not any(col):continue
   q=next(i for i,v in enumerate(col) if v)
   inv=pow(col[q],-1,p);piv[q]=tuple(v*inv%p for v in col);r+=1
 return r

def determinant(matrix):
 # Fraction-free exact integer elimination.
 a=[list(z) for z in matrix];n=len(a);sign=1;old=1
 for k in range(n-1):
  if a[k][k]==0:
   j=next((t for t in range(k+1,n) if a[t][k]),None)
   if j is None:return 0
   a[k],a[j]=a[j],a[k];sign=-sign
  z=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    q=a[i][j]*z-a[i][k]*a[k][j]
    assert q%old==0
    a[i][j]=q//old
   a[i][k]=0
  old=z
 return sign*a[-1][-1]

def witness_words(h):
 assert h>=2
 return ('fe'+'f'*(h-2),'ge'+'f'*(h-2))

def minor(words):
 assert len(words)==2
 # First future: A,B,AB,BA (drop N). Second: all five buckets.
 sigs=[signature(w) for w in words]
 cols=[(0,i) for i in (1,2,3,4)]+[(1,i) for i in (0,1,2,3,4)]
 a=[[int(sigs[word][i]==bucket) for word,bucket in cols] for i in range(9)]
 return determinant(a)

def trie(words):
 prefixes=set()
 for w in words:
  p=native(w)
  for i in range(1,len(p)+1):prefixes.add(p[:i])
 return len(prefixes)

def run():
 assert all(len(h)==10 and displacement(h)==(-2,0,0,0,0,0) and positive(h)==(2,2,0,0,0,0) for h in HISTORIES)
 check_x=(2,3,5,7,11,13);check_y=(3,4,7,11,13,17)
 rows=[]
 for h in range(2,26):
  pair=witness_words(h);seqs=[native(w) for w in pair]
  assert all(displacement(s)==(2,0,0,0,0,0) and len(s)==2*h+2 for s in seqs)
  assert seqs[0][0]==1 and seqs[1][0]==2
  assert minor(pair)==-1, (h,minor(pair))
  assert modular_rank(signature(w) for w in pair)==9
  assert trie(pair)==4*h+4
  assert all((pair[i].startswith(witness_words(h-1)[i]) for i in (0,1))) if h>2 else True
  for future in seqs:
   for historical in HISTORIES:
    for x in (check_x,check_y):
     assert brc(historical+future,x)==brc(historical,x)*brc(future,x)
  p1,p2=[positive(p) for p in seqs]
  assert p1==(h+1,0,1,0,0,0) and p2==(h,1,1,0,0,0)
  rows.append({'h':h,'words':list(pair),'unimodular_minor':-1,'transfer_rank':9,
               'shared_prefix_cost':trie(pair),'X_factors':[brc(s,check_x) for s in seqs],
               'Y_factors':[brc(s,check_y) for s in seqs],
               'positive_count_vectors':[list(p1),list(p2)]})
 finite=[]
 for h in range(1,6):
  words=[''.join(chars) for chars in product('acdefg',repeat=h)
         if displacement(native(chars))==(2,0,0,0,0,0)]
  sigs=[signature(w) for w in words]
  left1=[w for w in words if native(w)[0]!=1]
  left2=[w for w in words if native(w)[0]!=2]
  full=modular_rank(sigs)
  no1=modular_rank(signature(w) for w in left1)
  no2=modular_rank(signature(w) for w in left2)
  assert no1<9 and no2<9,(h,no1,no2)
  minimum=min(map(lambda w:len(native(w)),words))
  assert minimum==2*h+2
  if h==1:assert full==5
  else:assert full==9
  finite.append({'h':h,'returning_word_count':len(words),'full_rank':full,
                 'rank_without_first_+E1':no1,'rank_without_first_+E2':no2,
                 'minimum_signed_primitive_length':minimum})
 # First H=2 to H=25 nested schedules have exactly the longest pair's trie.
 multi=[]
 for H in range(2,26):
  allwords=[w for h in range(2,H+1) for w in witness_words(h)]
  assert trie(allwords)==trie(witness_words(H))==4*H+4
  multi.append({'H':H,'all_horizon_shared_cost':trie(allwords),
                'per_horizon_rank':9,'last_pair':list(witness_words(H))})
 return {'status':'PASS','unit':'EC49EG_FULL_A_TO_G','proof_claim':
         'For all integers H>=2, U_full_a_g(H)=4H+4, count unrestricted, exact native signed-prefix cost.',
         'source_science_pins':{'global':'773d538180bfb49e24cffeb35c3ee75eb0628e2e',
                               'enterprise_math':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'},
         'typed_ops':{k:list(v) for k,v in OPS.items()},'historical_atom_order':list(ATOMS),
         'history_realizations':[list(p) for p in HISTORIES],
         'checked_uniform_witness_h2_25':rows,
         'complete_return_word_audits_h1_5':finite,
         'nested_schedule_H2_25':multi,
         'rank_justification':'0/1 minors of size at most 9 have abs determinant <= 9^(9/2)<1000003, so mod-prime rank9 is exact over rationals.',
         'all_H_lower_bound':'Rank9 requires two histories A0/A2 and B0/B1 to separate; hence at least one word first +E1 and one first +E2. Distinct first signed X6 primitives prevent sharing; any returning h-letter word needs >=1 e of four primitives and all remaining letters >=2 primitives, so at least 2h+2 per path.',
         'all_H_upper_bound':'fe f^(h-2), ge f^(h-2), each primitive length 2h+2, nine-column determinant -1 and nested across horizons.'}

if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
