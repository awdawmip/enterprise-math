#!/usr/bin/env python3
"""Stage99 separate ordered-word DFS author check: deliberately no count aggregation."""
from fractions import Fraction as F
from functools import lru_cache
p=(F(1,8),F(1,24),F(5,6));q=(F(1,12),F(1,12),F(5,6))
K=F(6696,5); L=F(6312,5);A=(11,3,0);B=(12,0,1)
alpha=F(2586269937332842327,7450150876955541504)
V=F(757686022002985135,58204303726215168)
s=F(12366057190345211,20889600000000000)
h=F(26961,108800);eta=F(107421875,2806920511488)
@lru_cache(None)
def best(n,a,b):
 opts={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<14:opts['C']=1+sum(p[i]*best(n+1,a+(i==0),b+(i==1))[0] for i in range(3))
 v=min(opts.values())
 return v,next(t for t in ('C','P','Q') if opts.get(t,None)==v)
def exhaustive(u):
 stats=[F(0),F(0),F(0),F(0)];hits={A:[F(0),F(0),0],B:[F(0),F(0),0]};visits=0
 def walk(n,a,b,x,y,seenA=False,seenB=False):
  nonlocal visits
  visits+=1;v=(n,a,b)
  if v==A:
   assert not seenB
   hits[A][0]+=x;hits[A][1]+=y;hits[A][2]+=1
   stats[1]+=u*y;x*=1-u;y*=1-u;seenA=True
  elif v==B:
   assert not seenA
   hits[B][0]+=x;hits[B][1]+=y;hits[B][2]+=1
   w=s+h*u;stats[0]+=w*x;x*=1-w;y*=1-w;seenB=True
  else:
   t=best(n,a,b)[1]
   if t=='P':stats[1]+=y;return
   if t=='Q':stats[0]+=x;return
  if x==0 and y==0:return
  stats[2]+=x;stats[3]+=y
  assert n<14
  for i in range(3):walk(n+1,a+(i==0),b+(i==1),x*p[i],y*q[i],seenA,seenB)
 walk(0,0,0,F(1),F(1))
 assert tuple(hits[A])==(F(21484375,286654464),F(21484375,967458816),165)
 assert tuple(hits[B])==(F(48828125,725594112),F(48828125,362797056),12)
 assert stats[0]==stats[1]==alpha+eta*u
 assert stats[2]==V-(K+L)*eta*u and stats[2]>stats[3]
 assert visits>1000000
 return visits
if __name__=='__main__':
 for u in (F(0),F(1,7),F(1,2),F(1)):print('u',u,'ordered_prefix_visits',exhaustive(u))
 print('INDEPENDENT_ORDERED99_AUTHOR_PASS')
