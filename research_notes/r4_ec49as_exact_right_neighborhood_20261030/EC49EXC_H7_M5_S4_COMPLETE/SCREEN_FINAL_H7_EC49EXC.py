#!/usr/bin/env python3
"""Compute exact four-signature incremental min native edge cost for H7
against the optimistic union of all eligible earlier native prefixes.
An optimistic free edge universe yields a lower bound for any actual H6 selection.
"""
from VERIFY_EC49ER import *
from collections import defaultdict,Counter
from itertools import product
import json,time
from functools import lru_cache

class N:
 __slots__=('child','terminal')
 def __init__(self):self.child={};self.terminal=0

def min_new_cost(words_by_sig, old_prefix):
 root=N();sigmap={s:i for i,s in enumerate(sorted(words_by_sig))}
 for sig,words in words_by_sig.items():
  for w in words:
   node=root
   for step in path(w):node=node.child.setdefault(step,N())
   node.terminal|=1<<sigmap[sig]
 nodes=0
 def visit(n,pref):
  nonlocal nodes
  nodes+=1
  dp={0:0}
  for step,ch in n.child.items():
   sub=visit(ch,pref+(step,));out={}
   for a,va in dp.items():
    for b,vb in sub.items():
     k=a|b;v=va+vb
     if v<out.get(k,10**9):out[k]=v
   dp=out
  if pref:
   edge=0 if pref in old_prefix else 1
   out={0:0}
   for m,v in dp.items():
    k=m|n.terminal
    if k:
     c=v+edge
     if c<out.get(k,10**9):out[k]=c
   dp=out
  return dp
 d=visit(root,())
 return d[(1<<len(sigmap))-1],nodes

def main():
 start=time.time();base=fibers();t4=frozenset(signature(w) for w in BASE)
 report=json.load(open('EC49EXC_SCREENED.json'))
 bounded=json.load(open('EC49EXC_H6_BOUNDED_COMPLETE.json'))
 todo=[]
 for r in report['unresolved']:
  ks=':'.join(','.join(map(str,p)) for p in r['h3to6'])
  if bounded[ks] is not None:todo.append(r)
 assert len(todo)==32
 ps7={tuple(r['p7']) for r in todo}
 words7=defaultdict(lambda:defaultdict(list));num=0
 for xs in product(OPS,repeat=7):
  w=''.join(xs);p=poscount(w)
  if p not in ps7:continue
  if displacement(w)!=(2,0,0,0,0,0):continue
  s=signature(w)
  if s in t4:words7[p][s].append(w);num+=1
 print('h7 words selected',num,'keys',len(ps7),'elapsed',round(time.time()-start,2),flush=True)
 res=[]
 for i,row in enumerate(todo):
  old=set(PAID_BASE)
  for h,p in zip(range(3,7),row['h3to6']):
   for w in base[h][tuple(p)]:
    if signature(w) in t4:old.update(prefixes((w,)))
  cost,nodes=min_new_cost(words7[tuple(row['p7'])],old)
  res.append({'pair':row['pair'],'h3to6':row['h3to6'],'p7':row['p7'],'H6_min':68,'H7_new_native_edge_lower_if_all_earlier_fiber_prefixes_free':cost,'total_E_lower':68+cost,'h7_trie_nodes':nodes,'h7_word_count':sum(map(len,words7[tuple(row['p7'])].values()))})
 print('final cases',len(res),'H7_cost_hist',Counter(r['H7_new_native_edge_lower_if_all_earlier_fiber_prefixes_free'] for r in res),'elapsed',round(time.time()-start,2))
 report['H7_final_optimistic_prefix_lower']=res
 report['H7_final_certified_E>=80']=sum(r['total_E_lower']>=80 for r in res)
 report['certified_total']=4422+report['H7_final_certified_E>=80']
 report['truly_open_cases']=len(res)-report['H7_final_certified_E>=80']
 report['run_time_final_sec']=round(time.time()-start,2)
 json.dump(report,open('EC49EXC_FINAL_SCREEN.json','w'),indent=2)
 print('CERTIFIED',report['certified_total'],'OF',26037,'OPEN',report['truly_open_cases'],flush=True)
 for r in res:
  print(r['h3to6'],r['p7'],'cost',r['H7_new_native_edge_lower_if_all_earlier_fiber_prefixes_free'])
 return report
if __name__=='__main__':main()
