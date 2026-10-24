#!/usr/bin/env python3
"""Ordered-history DFS crosscheck; shares predecessor stopping table, not independent Driver review."""
from fractions import Fraction as F
from collections import Counter
import json
import verify_n14_83 as m
def prefix(st):
 hits=[]
 def visit(state,p,q):
  if state==st:hits.append((p,q));return
  if state[0]>=st[0] or m.act(state)!='C':return
  for i in range(3):visit(m.child(state,i),p*m.P[i],q*m.Q[i])
 visit((0,0,0),F(1),F(1))
 return len(hits),sum((p for p,q in hits),F()),sum((q for p,q in hits),F())
def suffix(st):
 ends=Counter();r=[F(),F(),F(),F()]
 def visit(state,p,q,t):
  z=m.act(state)
  if z!='C':
   ends[(state,z)]+=1
   if z=='Q':r[0]+=p
   else:r[1]+=q
   r[2]+=t*p;r[3]+=t*q
   return
  for i in range(3):visit(m.child(state,i),p*m.P[i],q*m.Q[i],t+1)
 visit(st,F(1),F(1),0)
 return tuple(r),sum(ends.values()),len(ends)
def check():
 out={}
 for name,st in [('A',m.A),('B',m.B)]:
  k,p,q=prefix(st);r,words,term=suffix(st)
  assert (p,q,k)==m.firsthit(st) and r==m.suffix(st)
  out[name]=dict(live=k,p=str(p),q=str(q),suffix_words=words,terminal_states=term,truncated_paths=k*words)
 assert out['A']['live']==31 and out['A']['suffix_words']==57 and out['A']['truncated_paths']==1767
 assert out['B']['live']==12 and out['B']['suffix_words']==5 and out['B']['truncated_paths']==60
 assert m.check()['V83']=='24511993371361253729/1862537719238885376'
 return out
if __name__=="__main__":print(json.dumps(check(),indent=2))
