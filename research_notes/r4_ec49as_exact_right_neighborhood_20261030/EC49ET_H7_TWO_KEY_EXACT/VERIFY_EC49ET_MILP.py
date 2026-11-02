#!/usr/bin/env python3
"""EC49ET exact finite-H=7 two-BRC-key optimization on signed native X6.

Finite domain and mandatory terminal observer signatures are inherited from
EC49EI/EJ, and source pins are included in the accompanying paper.
Run with Python>=3.11, numpy and scipy (HiGHS). No hidden data files.
"""
from itertools import permutations
from collections import defaultdict,Counter
import argparse, json, time
from pathlib import Path
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix

OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
HIST=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')
BASE=('ce','de','ec','ed')
T4=('ce','de','ec','ed')
T2=('feg','gef')
TARGET_P0=(3,1,1,0,0,0)
TARGET_P1=(5,3,1,0,0,0)

def path(w):return sum((OPS[x] for x in w),())
def pvec(w):
 s=path(w);return tuple(s.count(k) for k in range(1,7))
def disp(w):
 s=path(w);return tuple(s.count(k)-s.count(-k) for k in range(1,7))
def trans(w):
 out=[]
 for evt,p0 in HIST:
  p=p0; e=evt
  for t in path(w):
   if p==1 and t==2:
    if e=='N':e='A'
    elif e=='B':e='BA'
   elif p==2 and t==1:
    if e=='N':e='B'
    elif e=='A':e='AB'
   p=t
  out.append(BUCKETS.index(e))
 return tuple(out)
SIGS={w:trans(w) for w in set(T4+T2)}
COLOR_NAMES=[(h,k) for h in range(3,8) for k in (T2 if h in (3,7) else T4)]
COLOR_INDEX={x:i for i,x in enumerate(COLOR_NAMES)}
LETTERS={3:'efg',4:'ccce',5:'ccefg',6:'ceffgg',7:'efffggg'}

def eligible():
 out={}; counts={}
 for h,letters in LETTERS.items():
  choices={''.join(p) for p in permutations(letters)}
  if h in (4,5,6):
   choices|={''.join(p) for p in permutations(letters.replace('c','d'))}
  sigs={SIGS[k]:k for k in (T2 if h in (3,7) else T4)}
  eligible_words={w:sigs[trans(w)] for w in sorted(choices) if trans(w) in sigs}
  target=TARGET_P0 if h==3 else TARGET_P1
  assert all(pvec(w)==target and disp(w)==(2,0,0,0,0,0) for w in choices)
  assert {k for k in eligible_words.values()}==set(T2 if h in (3,7) else T4)
  out[h]=eligible_words
  counts[h]={'complete_words':len(choices),'eligible_words':len(eligible_words),'signature_counts':dict(Counter(eligible_words.values()))}
 return out,counts

def build_trie(eligible_words):
 idx={():0}; prefixes=[()]; parent=[-1]; terminal_colors=defaultdict(set)
 def add_word(w):
  prefix=()
  for t in path(w):
   prefix=prefix+(t,)
   if prefix not in idx:
    idx[prefix]=len(prefixes);prefixes.append(prefix);parent.append(idx[prefix[:-1]])
  return idx[prefix]
 base_ids=set()
 for w in BASE:
  add_word(w)
  for k in range(1,len(path(w))+1):base_ids.add(idx[path(w)[:k]])
 assert len(base_ids)==28
 for h,word_types in eligible_words.items():
  for w,k in word_types.items():
   v=add_word(w)
   terminal_colors[v].add(COLOR_INDEX[h,k])
 count=len(prefixes)
 assert len(terminal_colors)==sum(len(d) for d in eligible_words.values())
 return idx,prefixes,parent,terminal_colors,base_ids

def solve_milp(prefs,parents,colors,base_ids,mip_rel_gap=0.,time_limit=300):
 from scipy.sparse import coo_matrix
 n=len(prefs); m=len(COLOR_NAMES)
 rows=[];cols=[];vals=[]
 for i in range(1,n):
  rows.extend((i-1,i-1));cols.extend((i,parents[i]));vals.extend((1.,-1.))
 color_roots=defaultdict(list)
 for term,c in colors.items():
  for k in c:color_roots[k].append(term)
 assert sorted(color_roots)==list(range(m))
 for k in range(m):
  for i in color_roots[k]:rows.append(n-1+k);cols.append(i);vals.append(1.)
 matrix=coo_matrix((vals,(rows,cols)),shape=(n-1+m,n)).tocsr()
 lo=np.full(n-1+m,-np.inf)
 hi=np.r_[np.zeros(n-1),np.full(m,np.inf)]
 lo[n-1:]=1
 c=np.array([0. if i in base_ids or i==0 else 1. for i in range(n)])
 lb=np.zeros(n);ub=np.ones(n)
 for i in base_ids:lb[i]=1
 ans=milp(c,integrality=np.ones(n),bounds=Bounds(lb,ub),constraints=LinearConstraint(matrix,lo,hi),options={'mip_rel_gap':mip_rel_gap,'time_limit':time_limit,'disp':False})
 if ans.x is None:return {'status':int(ans.status),'message':str(ans.message),'dual_bound':float(ans.mip_dual_bound) if hasattr(ans,'mip_dual_bound') and ans.mip_dual_bound is not None else None}
 chosen={i for i in range(n) if ans.x[i]>0.5}
 witnesses=defaultdict(dict)
 for h,ww in ELIG.items():
  for w,k in sorted(ww.items()):
   if prefs.index(path(w)) in chosen:
    witnesses[h].setdefault(k,w)
 # One can obtain multiple terminal choices; all included to reflect actual MILP solution.
 all_terminal_words={str(h):[w for w,k in sorted(ww.items()) if prefs.index(path(w)) in chosen] for h,ww in ELIG.items()}
 union=set();total_keys=set();total_sig=set()
 for w in BASE:union|={path(w)[:i] for i in range(1,len(path(w))+1)};total_keys.add(pvec(w));total_sig.add(trans(w))
 for ww in all_terminal_words.values():
  for w in ww:union|={path(w)[:i] for i in range(1,len(path(w))+1)};total_keys.add(pvec(w));total_sig.add(trans(w))
 assert len(union)==len(chosen)-1
 assert len(total_keys)==2 and len(total_sig)==6
 assert all(set(ELIG[int(h)][w] for w in words)==set(T2 if int(h) in (3,7) else T4) for h,words in all_terminal_words.items())
 return {'status':int(ans.status),'message':str(ans.message),'objective':int(round(ans.fun+28)),'extra_edges':int(round(ans.fun)), 'gap':float(ans.mip_gap),'dual_bound_extra':float(ans.mip_dual_bound), 'binary_nodes':len(prefs)-1,'selected_nodes':len(chosen)-1, 'selected_terminals':sum(map(len,all_terminal_words.values())), 'witness':all_terminal_words,'resources':[len(union),len(total_keys),len(total_sig)]}

if __name__=='__main__':
 start=time.perf_counter()
 ELIG,counts=eligible()
 ix,prs,pa,colors,base=build_trie(ELIG)
 print('enumeration',json.dumps(counts,sort_keys=True),'trie nodes',len(prs),flush=True)
 ans=solve_milp(prs,pa,colors,base,0.,300)
 result={'unit':'EC49ET','target':'H7-M2-S6','enumeration':counts,'color_names':[[h,k] for h,k in COLOR_NAMES],'base_edges':28,'trie_nodes':len(prs),'optimizer':ans}
 p=Path('EC49ET_MILP_EXECUTED.json');p.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
 with open('EC49ET_TRIE_INPUT.txt','w') as f:
  f.write(f'{len(prs)} {len(COLOR_NAMES)}\n')
  for i in range(len(prs)):
   mask=sum(1<<k for k in colors.get(i,set()))
   f.write(f'{pa[i]} {int(i in base)} {mask}\n')
 print('result',json.dumps(ans,ensure_ascii=False),flush=True)

