#!/usr/bin/env python3
"""Second author-side exact check: 19683 ordered words, backward absorption, four corners."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import runpy
m=runpy.run_path(str(Path(__file__).with_name("2026-10-23_N14_auxiliary_iid_50th_exact_affine_portable.py")))
P,Q,A,B,N=(m[x] for x in ("P","Q","A","B","N"))
act,child=m["act"],m["child"]
AL,V,S,G=(m[x] for x in ("AL","V","S","G"))
H=F(13277523,21760000000)
ETA=F(33254375,538928738205696)
def root(u,s):
 @lru_cache(None)
 def f(st):
  z=act(st)
  if st==A:z="A"
  elif st==B:z="B"
  if z=="P":return F(),F(1),F(),F()
  if z=="Q":return F(1),F(),F(),F()
  assert st[0]<N
  xs=[f(child(st,i)) for i in range(3)]
  c=(sum((P[i]*xs[i][0] for i in range(3)),F()),
     sum((Q[i]*xs[i][1] for i in range(3)),F()),
     1+sum((P[i]*xs[i][2] for i in range(3)),F()),
     1+sum((Q[i]*xs[i][3] for i in range(3)),F()))
  r=u if z=="A" else s if z=="B" else F()
  if z=="A":return (1-r)*c[0],r+(1-r)*c[1],(1-r)*c[2],(1-r)*c[3]
  return r+(1-r)*c[0],(1-r)*c[1],(1-r)*c[2],(1-r)*c[3]
 return f((0,0,0))
def check():
 live=0;pa=qa=F()
 for word in product(range(3),repeat=A[0]):
  if word.count(0)!=A[1] or word.count(1)!=A[2]:continue
  st=(0,0,0);wp=wq=F(1)
  for i in word:
   if act(st)!="C":break
   st=child(st,i);wp*=P[i];wq*=Q[i]
  else:
   assert st==A
   live+=1;pa+=wp;qa+=wq
 assert (live,pa,qa)==(126,F(4375,2359296),F(4375,17915904))
 corners={(u,s):root(F(u),F(s)) for u in (0,1) for s in (0,1)}
 assert all(corners[1,1][j]-corners[1,0][j]-corners[0,1][j]+corners[0,0][j]==0 for j in range(4))
 for u in (F(),F(1,4),F(1,2),F(3,4),F(1)):
  s=S+H*u
  z=root(u,s)
  interp=tuple(corners[0,0][j]+u*(corners[1,0][j]-corners[0,0][j])+s*(corners[0,1][j]-corners[0,0][j]) for j in range(4))
  assert z==interp
  assert z[0]==z[1]==AL+ETA*u
  assert z[2]==V-G*ETA*u and z[2]>=z[3]
 assert root(F(1),S+H)[:3]==(F(5171825736073354397,14900301753911083008),)*2+(F(12376506639448300069,931268859619442688),)
 print("PASS: 19683 ordered paths, 126 surviving, 4 corners, 5 mixtures")
if __name__=="__main__":check()
