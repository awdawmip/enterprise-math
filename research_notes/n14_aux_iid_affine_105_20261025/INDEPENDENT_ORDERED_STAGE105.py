#!/usr/bin/env python3
"""Fresh author cross-check for Stage105: recursive Bellman, actual ordered DFS.
No imports from derive105.py and no imported action table; rational arithmetic only.
"""
from fractions import Fraction as R
from functools import lru_cache
p=(R(1,8),R(1,24),R(5,6));q=(R(1,12),R(1,12),R(5,6))
K=R(2212824096,1992661);L=R(72)+R(8,9)*K
A=(8,5,1);B=(12,0,1)
a0=R(646648471503178867,1862537719238885376)
a1=R(38038153259411651,109561042308169728)
s0=R(4103853056103079,5222400000000000)
s1=R(241563037007287,307200000000000)
t0=R(6009287153480025269,465634429809721344)
t1=R(353483207227801957,27390260577042432)
tQ0=R(5709042008510518661,465634429809721344)
tQ1=R(111940980237083111,9130086859014144)
@lru_cache(None)
def V(n,a,b):
 opts={'P':K*R(2**(a+b),3**a),'Q':L}
 if n<14:opts['C']=1+p[0]*V(n+1,a+1,b)[0]+p[1]*V(n+1,a,b+1)[0]+p[2]*V(n+1,a,b)[0]
 best=min(opts.values());return best,tuple(k for k,x in opts.items() if x==best)
assert { (n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1) if len(V(n,a,b)[1])>1}=={A,B}
def act(n,a,b):
 if (n,a,b) in (A,B):return 'C'
 return V(n,a,b)[1][0]
# Genuine word-by-word until first hit (not combinatorially assumed reachable).
hit={A:[0,R(0),R(0)],B:[0,R(0),R(0)]}
def first(n,a,b,wp,wq):
 z=(n,a,b)
 if z in hit:
  hit[z][0]+=1;hit[z][1]+=wp;hit[z][2]+=wq;return
 if act(n,a,b)!='C':return
 for i,(x,y) in enumerate(((a+1,b),(a,b+1),(a,b))):first(n+1,x,y,wp*p[i],wq*q[i])
first(0,0,0,R(1),R(1))
assert hit[A]==[112,R(175,1769472),R(175,6718464)]
assert hit[B]==[12,R(48828125,725594112),R(48828125,362797056)]
print('PASS genuine first hits',hit)
# Direct full word-by-word endpoint traversal with P/Q branch weights.
def full(u,s):
 out=[R(0),R(0),R(0),R(0)]; nodes=[0]; leaves=[0]
 def walk(n,a,b,wp,wq):
  nodes[0]+=1
  z=(n,a,b)
  if z==A:
   out[1]+=wq*u;out[2]+=wp*u*n;out[3]+=wq*u*n
   wp*=1-u;wq*=1-u;t='C'
  elif z==B:
   out[0]+=wp*s;out[2]+=wp*s*n;out[3]+=wq*s*n
   wp*=1-s;wq*=1-s;t='C'
  else:t=act(n,a,b)
  if wp==0 and wq==0:return
  if t=='P':out[1]+=wq;out[2]+=wp*n;out[3]+=wq*n;leaves[0]+=1
  elif t=='Q':out[0]+=wp;out[2]+=wp*n;out[3]+=wq*n;leaves[0]+=1
  else:
   for i,(x,y) in enumerate(((a+1,b),(a,b+1),(a,b))):walk(n+1,x,y,wp*p[i],wq*q[i])
 walk(0,0,0,R(1),R(1))
 return tuple(out),nodes[0],leaves[0]
for u,s,alpha,tP,tQ in ((R(0),s0,a0,t0,tQ0),(R(1),s1,a1,t1,tQ1),(R(1,2),(s0+s1)/2,(a0+a1)/2,(t0+t1)/2,(tQ0+tQ1)/2)):
 outcome,nodes,leaves=full(u,s)
 assert outcome==(alpha,alpha,tP,tQ)
 assert outcome[2]>outcome[3]
 print('PASS ordered DFS',str(u),'nodes',nodes,'leaves',leaves,'moments',[str(x) for x in outcome])
print('PASS_INDEPENDENT_ORDERED_STAGE105')
