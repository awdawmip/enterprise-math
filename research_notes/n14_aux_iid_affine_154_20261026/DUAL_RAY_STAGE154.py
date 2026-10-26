#!/usr/bin/env python3
"""Exact finite Bellman direction/closure certificate at Stage153->154 and Stage154->155.
Author-side Fraction computation; external iid ternary N=14 only.
"""
from fractions import Fraction as F
from functools import lru_cache
P=(F(1,8),F(1,24),F(5,6)); N=14
B=(11,0,1); R=(12,2,2); S=(10,5,4)
def child(st,i):n,a,b=st;return n+1,a+(i==0),b+(i==1)
def states():
 for n in range(N+1):
  for a in range(n+1):
   for b in range(n-a+1):yield n,a,b
def ratio(st):_,a,b=st;return F(2**(a+b),3**a)
def audit(K0,L0,tie_override):
 @lru_cache(None)
 def H(st):
  acts={'P':K0*ratio(st),'Q':L0}
  if st[0]<N:acts['C']=1+sum(P[i]*H(child(st,i))[0] for i in range(3))
  v=min(acts.values());return v,tuple(a for a,x in acts.items() if x==v)
 def selected(st):
  return tie_override.get(st,H(st)[1][0])
 @lru_cache(None)
 def exps(st):
  e={'P':(F(0),ratio(st),F(0)),'Q':(F(0),F(0),F(1))}
  if st[0]<N:
   v=[exps(child(st,i))[selected(child(st,i))] for i in range(3)]
   e['C']=(1+sum(P[i]*w[0] for i,w in enumerate(v)),
           sum(P[i]*w[1] for i,w in enumerate(v)),
           sum(P[i]*w[2] for i,w in enumerate(v)))
  return e
 dk=F(-1);dl=-F(112,129)
 closure=[]
 for st in states():
  e=exps(st);base=e[selected(st)]
  for name,w in e.items():
   dg=(w[0]-base[0])+(w[1]-base[1])*K0+(w[2]-base[2])*L0
   der=(w[1]-base[1])*dk+(w[2]-base[2])*dl
   assert dg>=0
   # Tied alternatives cannot point below zero in the forward ray.
   if dg==0:assert der>=0,(st,name,der)
   if dg>0 and der<0:closure.append((dg/(-der),st,name,selected(st)))
 return min(closure),H
first,old=audit(F(5994,17),F(5960,17),{R:'Q',B:'Q'})
assert first==(F(30922074,3386893),S,'C','Q'),first
K=F(68426856,199229);L=F(68268104,199229)
second,new=audit(K,L,{S:'C',B:'Q'})
assert second==(F(20479008,3386893),(14,0,0),'P','Q'),second
assert K-second[0]==F(5736,17)
assert L-F(112,129)*second[0]==F(5736,17)
print('PASS exact Stage154 first gap closure:',first)
print('PASS exact Stage155 dual candidate:',second)
