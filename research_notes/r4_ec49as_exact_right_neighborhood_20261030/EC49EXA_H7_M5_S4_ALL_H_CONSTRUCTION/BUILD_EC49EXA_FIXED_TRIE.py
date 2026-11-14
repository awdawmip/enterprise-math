#!/usr/bin/env python3
"""Create the exact integer OR-mask trie for the specified 5-key seven-window schedule.

Requires immutable scientific model MODEL_EC49EU.py (Git blob bcad085da0655d41753c166fd993cdb35e4d4815).
Pipes to VERIFY_EC49EU_EXACT_DP.cpp compiled C++17 kernel (blob d08c90554d205730ce6a36e89a59754e28f36902).
"""
from MODEL_EC49EU import BASE,PAID_BASE,T4,words,signature,path,rank_mod
from itertools import combinations
KEYS={3:(4,2,1,0,0,0),4:(4,2,1,0,0,0),5:(5,2,1,0,0,0),6:(6,2,1,0,0,0),7:(7,2,1,0,0,0)}
T=tuple(sorted(T4))
assert rank_mod(T)==9
assert all(rank_mod(combo)<9 for combo in combinations(T,3))
class Node:
  __slots__=('parent','paid','mask','prefix','children')
  def __init__(self,parent,prefix):
    self.parent=parent;self.prefix=prefix
    self.paid=int(prefix in PAID_BASE);self.mask=0;self.children={}
ns=[Node(-1,())]
for h,p in KEYS.items():
  found={t:0 for t in T}
  for w in words(h,p):
    t=signature(w)
    if t not in found:continue
    found[t]+=1
    ptr=0
    for step in path(w):
      node=ns[ptr]
      if step not in node.children:
        child=len(ns)
        node.children[step]=child
        ns.append(Node(ptr,node.prefix+(step,)))
      ptr=node.children[step]
    ns[ptr].mask|=1<<(4*(h-3)+T.index(t))
  assert all(found.values()),(h,found)
print(len(ns),20)
for n in ns:print(n.parent,n.paid,n.mask)
