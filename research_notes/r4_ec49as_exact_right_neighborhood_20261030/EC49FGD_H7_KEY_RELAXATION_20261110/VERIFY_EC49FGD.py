#!/usr/bin/env python3
"""Exact literal signed native prefix-trie DP for H7-low minimal-r single-key extensions
of a frozen 20-word original-mother background. One word for each terminal signature.
The admissible op alphabet and DFA are transcribed from frozen_model.py, blob
7e97065ac9a0ff70435b92ee2f4bd718c9bf1859 (frozen science pin
fc0f038e7bfd12c886b4d37f900bfb770c0f61ab).
"""
from collections import Counter
from functools import lru_cache
import json, sys
from pathlib import Path
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
FIX={2:{16:'fe',32:'ge'},3:{16:'feg',32:'gef'},4:{1:'gefd',2:'fegd',4:'cefg',8:'gefc'},5:{16:'feggf',32:'geffg'},6:{1:'gefdfg',2:'fegdgf',4:'feggfc',8:'geffgc'},8:{1:'geffgfgd',2:'feggffgd',4:'feggfcfg',8:'geffgcgf'},9:{16:'feggffggf',32:'geffgfggf'}}
NEED=(1,2,4,8)

def native(w):return tuple(k for ch in w for k in STEPS[ch])
def observe(w):
 q=0
 for ch in w:q=T[q][OPS.index(ch)]
 return SIG[q]
def key(w):
 s=native(w);return tuple(s.count(i) for i in (1,2,3))
def pref(w):
 s=native(w);return [s[:i] for i in range(1,len(s)+1)]
BASE=set(p for d in FIX.values() for w in d.values() for p in pref(w))
assert len(BASE)==89
assert sum(len(d) for d in FIX.values())==20
assert all(len(w)==h and observe(w)==s for h,d in FIX.items() for s,w in d.items())
assert all(Counter(w)['e']==Counter(w)['a']+1 for d in FIX.values() for w in d.values())

def candidates(h,x,y,z):
 a=z-1; r=x+y-h-1; f=h+1-y-2*z;g=h+1-x
 if min(a,r,f,g)<0: return {},(a,r,f,g)
 pool={s:[] for s in NEED}
 for c in range(r+1):
  left={'a':a,'c':c,'d':r-c,'e':z,'f':f,'g':g}
  def visit(word,q):
   if len(word)==h:
    s=SIG[q]
    if s in pool:pool[s].append(word)
    return
   for ch in OPS:
    if left[ch]:
     nq=T[q][OPS.index(ch)]
     if nq==8:continue
     left[ch]-=1; visit(word+ch,nq); left[ch]+=1
  visit('',0)
 return pool,(a,r,f,g)

def optimize(pool):
 # Complete exact dynamic program. Root=0, descendants uniquely labeled
 children=[{}]; label=[0]; terminals=[{}]
 for sig,words in pool.items():
  for w in words:
   node=0
   for s in native(w):
    kids=children[node]
    if s not in kids:
     kids[s]=len(children);children.append({});label.append(0);terminals.append({})
    node=kids[s]
   label[node] |= 1<<NEED.index(sig)
   terminals[node][sig]=w

 # Assign prefix and solve tree exactly. state dp[mask] min new edges for chosen terminal labels
 def visit(node, path):
  cur={0: (0, ())}
  tmask=label[node]
  if tmask:
   for bit in range(4):
    if tmask & (1<<bit):
     s=NEED[bit]
     cur[1<<bit]=(0,(terminals[node][s],))
  for step,ch in children[node].items():
   newpath=path+(step,)
   sub=visit(ch,newpath)
   edge_cost=0 if newpath in BASE else 1
   nex={}
   for oldmask,(oc,ow) in cur.items():
    for submask,(sc,sw) in sub.items():
     if oldmask&submask: continue
     mask=oldmask|submask
     v=oc+sc+(edge_cost if submask else 0)
     if mask not in nex or v<nex[mask][0]:nex[mask]=(v,ow+sw)
   cur=nex
  return cur
 ret=visit(0,())
 if 15 not in ret: return None,len(children)
 v,w=ret[15]
 assert len(w)==4 and {observe(x) for x in w}==set(NEED)
 allword=[x for d in FIX.values() for x in d.values()]+list(w)
 P=set(p for x in allword for p in pref(x))
 assert len(P)==len(BASE)+v
 return {'fresh_edges':v,'total_edges':len(P),'witness':{str(observe(z)):z for z in w}},len(children)

def run():
 report={'model':'EC49FGD_H7_LOW_FIXED_BACKGROUND_ALL_MINIMAL_R_KEYS','base_edges':len(BASE),'frozen_scientific_input':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','rows':[]}
 for z in (1,2,3,4):
  for x in range(1,9):
   for y in range(1,9-2*z):
    if x+y<8:continue
    pool,counts=candidates(7,x,y,z)
    if not pool or min(len(pool[s]) for s in NEED)==0: continue
    best,nodes=optimize(pool)
    report['rows'].append({'r':counts[1],'key':[x,y,z],'multiplicities':{'a':counts[0],'r':counts[1],'f':counts[2],'g':counts[3]},'pool_counts':{str(s):len(pool[s]) for s in NEED},'pool_total':sum(len(v) for v in pool.values()),'trie_nodes':nodes,'best':best})
    print('r',counts[1],'K',x,y,z,'pools',sum(len(v) for v in pool.values()),'optimum',best['total_edges'] if best else None,flush=True)
 report['row_count']=len(report['rows']);report['best']=min((row['best']['total_edges'],row['key']) for row in report['rows'] if row['best'])
 with open(str(Path(__file__).with_name('EXACT_REPORT_EC49FGD.json')),'w') as f:json.dump(report,f,indent=2);f.write('\n')
 print('MIN',report['best']);return report
if __name__=='__main__':run()
