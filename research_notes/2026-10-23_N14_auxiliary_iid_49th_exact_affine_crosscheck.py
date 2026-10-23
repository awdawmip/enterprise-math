#!/usr/bin/env python3
"""Second author-side N14-49 check: backward absorbing corners + all 3^7 ordered words."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import runpy
v=runpy.run_path(str(Path(__file__).with_name("2026-10-23_N14_auxiliary_iid_49th_exact_affine_portable.py")))
P,Q,A,B,N,action,child=(v[x] for x in ('P','Q','A','B','N','act','child'))
AL,V,S=(v[x] for x in ('AL','V','S'))
H=F(129735679,870400000000);ETA=F(241752875,12934289716936704)
G=v['G']
def root(u,s):
 @lru_cache(None)
 def f(st):
  z=action(st)
  if st==A:z='A'
  elif st==B:z='B'
  if z=='P':return F(),F(1),F(),F()
  if z=='Q':return F(1),F(),F(),F()
  assert st[0]<N
  xs=[f(child(st,i)) for i in range(3)]
  c=(sum((P[i]*xs[i][0] for i in range(3)),F()),
     sum((Q[i]*xs[i][1] for i in range(3)),F()),
     F(1)+sum((P[i]*xs[i][2] for i in range(3)),F()),
     F(1)+sum((Q[i]*xs[i][3] for i in range(3)),F()))
  r=u if z=='A' else s if z=='B' else F()
  return r+(1-r)*c[0],(1-r)*c[1],(1-r)*c[2],(1-r)*c[3]
 return f((0,0,0))
def check():
 live=0;pa=qa=F()
 for word in product(range(3),repeat=7):
  if word.count(0)!=1 or word.count(1)!=3:continue
  st=(0,0,0);valid=True
  for i in word:
   if action(st)!='C':valid=False;break
   st=child(st,i)
  if not valid:continue
  assert st==A
  live+=1;wp=wq=F(1)
  for i in word:wp*=P[i];wq*=Q[i]
  pa+=wp;qa+=wq
 assert (live,pa,qa)==(106,F(6625,11943936),F(6625,2239488))
 corners={(u,s):root(F(u),F(s)) for u in (0,1) for s in (0,1)}
 assert all(corners[1,1][j]-corners[1,0][j]-corners[0,1][j]+corners[0,0][j]==0 for j in range(4))
 for u in (F(),F(1,3),F(1,2),F(2,3),F(1)):
  s=S-H*u
  z=root(u,s)
  interpol=tuple(corners[0,0][j]+u*(corners[1,0][j]-corners[0,0][j])+s*(corners[0,1][j]-corners[0,0][j]) for j in range(4))
  assert z==interpol
  assert z[0]==z[1]==AL+ETA*u
  assert z[2]==V-G*ETA*u and z[2]>=z[3]
 assert root(F(1),S-H)[:3]==(F(5171824816656394397,14900301753911083008),)*2+(F(12378473542489900069,931268859619442688),)
 print("PASS author-side independent backward corners and full ordered-word enumeration")
if __name__=='__main__':check()
