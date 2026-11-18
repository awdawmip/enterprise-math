#!/usr/bin/env python3
"""Exact finite signed-X6 prefix minimization for original frozen nine-state BRC.
The imported functions define the complete native operation alphabet, observation
and complete-key rules. An auxiliary single-horizon solver is also included.
"""
from itertools import product
from collections import Counter
import json,sys
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
CODES={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
B2=('de','ed','ce','ec')
B3=('feg','gef')
REQUIRED=(1,2,4,8)
def expand(word):return tuple(y for x in word for y in CODES[x])
def pref(word):
 st=expand(word)
 return set(st[:k] for k in range(1,len(st)+1))
def signature(w):
 s=0
 for c in w:s=T[s][OPS.index(c)]
 return SIG[s]
def key(w):
 h=len(w);cnt=Counter(w)
 return (h+1-cnt['g'],h+1-2*cnt['e']-cnt['f'],cnt['e'])
def pool(h):
 out=[]
 def visit(pre,state,counts):
  k=len(pre)
  if k==h:
   if SIG[state] in REQUIRED and counts[3]==counts[0]+1>=1:
    ky=(h+1-counts[5],h+1-2*counts[3]-counts[4],counts[3])
    if min(ky)>0:out.append((pre,SIG[state],ky))
   return
  if state==8:return
  a,c,d,e,f,g=counts
  if a>h//2 or e>h//2+1:return
  for i,op in enumerate(OPS):
   q=T[state][i]
   if q==8:continue
   cc=list(counts);cc[i]+=1
   if cc[3]>cc[0]+1+(h-k-1):continue
   if cc[0]>cc[3]+(h-k-1):continue
   visit(pre+op,q,cc)
 visit('',0,(0,0,0,0,0,0))
 return out
class Node:
 __slots__=('children','sig','word')
 def __init__(self):self.children={};self.sig=0;self.word={}
def optimize(h,include_high=True):
 fixed=set().union(*(pref(w) for w in (B2+B3 if include_high else B2)))
 P=pool(h);root=Node()
 bits={s:1<<i for i,s in enumerate(REQUIRED)}
 for w,s,k in P:
  node=root
  for ch in expand(w):node=node.children.setdefault(ch,Node())
  node.sig|=bits[s];node.word[s]=w
 def solve(node,pre):
  base={0:(0,{})}
  for s,w in node.word.items():base[bits[s]]=(0,{s:w})
  for ch,child in node.children.items():
   other=solve(child,pre+(ch,))
   z=0 if pre+(ch,) in fixed else 1
   new={}
   for a,(ca,wa) in base.items():
    for b,(cb,wb) in other.items():
     m=a|b;cost=ca+cb+(z if b else 0)
     if m not in new or cost<new[m][0]:new[m]=(cost,wa|wb)
   base=new
  return base
 extra,chosen=solve(root,())[15]
 total=extra+len(fixed);union=set(fixed)
 for s,w in chosen.items():
  assert signature(w)==s and len(w)==h and min(key(w))>0
  union|=pref(w)
 assert len(union)==total
 return {'h':h,'candidates':len(P),'baseline_edges':len(fixed),'extra_edges':extra,'optimum':total,'witness':{str(k):v for k,v in sorted(chosen.items())}}
if __name__=='__main__':
 ans=[optimize(int(x)) for x in sys.argv[1:]]
 print(json.dumps(ans,ensure_ascii=False))
