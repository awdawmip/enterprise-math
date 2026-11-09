#!/usr/bin/env python3
"""Exhaustive native signed-prefix 4-mask extension of a fixed original 20-word core."""
from ec49fgd_mixed_seed_dp import OPS,T,SIG,expand,pref,key,signature,Node
import json
CORE={'2:16':'fe','2:32':'ge','3:16':'feg','3:32':'gef'}
low={4:['gefd','fegd','fegc','gefc'],
     6:['gefdff','fegdff','fegcgg','gefcgg'],
     7:['gefdfff','fegdfff','fegcggg','gefcggg'],
     8:['gefdffff','fegdffff','fegcgggg','gefcgggg']}
for h,ws in low.items():
 for s,w in zip((1,2,4,8),ws):CORE[f'{h}:{s}']=w
BASE=set().union(*(pref(w) for w in CORE.values()))
assert len(BASE)==64
def high_pool(h):
 out=[]
 def go(s,q,counts):
  n=len(s)
  if n==h:
   if SIG[q] in (16,32) and counts[3]==counts[0]+1>=1 and min(key(s))>0:
    out.append((s,SIG[q]))
   return
  if q==8:return
  if counts[0]>counts[3]+(h-n):return
  if counts[3]>counts[0]+1+(h-n):return
  for k,ch in enumerate(OPS):
   nxt=T[q][k]
   if nxt==8:continue
   cc=list(counts);cc[k]+=1
   go(s+ch,nxt,cc)
 go('',0,(0,0,0,0,0,0))
 return out
root=Node();N=0
for h in (5,9):
 arr=high_pool(h);N+=len(arr)
 print('H',h,'candidate',len(arr),flush=True)
 for w,s in arr:
  q=root
  for ch in expand(w):q=q.children.setdefault(ch,Node())
  bit={(5,16):1,(5,32):2,(9,16):4,(9,32):8}[h,s]
  q.sig|=bit;q.word[h,s]=w
nodes=0;merges=0
def solve(v,pre):
 global nodes,merges
 nodes+=1;d={0:(0,{})}
 for tag,w in v.word.items():
  b={(5,16):1,(5,32):2,(9,16):4,(9,32):8}[tag]
  d[b]=(0,{tag:w})
 for ch,child in v.children.items():
  nd=solve(child,pre+(ch,))
  edge=0 if pre+(ch,) in BASE else 1
  tmp={}
  for a,(ca,wa) in d.items():
   for b,(cb,wb) in nd.items():
    merges+=1
    score=ca+cb+(edge if b else 0);mask=a|b
    if mask not in tmp or score<tmp[mask][0]:tmp[mask]=(score,wa|wb)
  d=tmp
 return d
cost,ws=solve(root,())[15]
assert set(ws)=={(5,16),(5,32),(9,16),(9,32)}
assert len(BASE|set().union(*(pref(w) for w in ws.values())))==64+cost
print(json.dumps({'fixed20':64,'candidate_count':N,'trie_nodes':nodes,'dp_merges':merges,
 'extra_high_edges':cost,'optimum_given_exact_20_paths':64+cost,
 'high_words':{f'{h}:{s}':w for (h,s),w in sorted(ws.items())},
 'high_keys':{f'{h}:{s}':key(w) for (h,s),w in sorted(ws.items())}},indent=2))
