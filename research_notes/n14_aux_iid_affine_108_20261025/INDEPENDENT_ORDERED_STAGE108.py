#!/usr/bin/env python3
"""Author-side independent top-down Bellman and literal ordered-word DFS. External iid model only."""
from fractions import Fraction as F
from functools import lru_cache
p=(F(1,8),F(1,24),F(5,6));q=(F(1,12),F(1,12),F(5,6))
K=F(208946709,206588);L=F(50075544,51647)
A=(10,3,0);Z=(11,5,4)
u0=F(1115808042440821,1479206400000000)
d=F(67761451,4930688000000)
a0=F(91588670614917102449,263775056922062880768)
a1=F(13084095824621807507,37682150988866125824)
t0=F(13541383133505475882195,1055100227688251523072)
t1=F(1934483126570299962385,150728603955464503296)
q0=F(805267616960628807535,65943764230515720192)
q1=F(38346074856588751535,3140179249072177152)
@lru_cache(None)
def dp(n,a,b):
 opts={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<14:
  opts['C']=1+sum((p[i]*dp(n+1,a+(i==0),b+(i==1))[0] for i in range(3)),F(0))
 v=min(opts.values());return v,tuple(t for t,x in opts.items() if x==v)
assert { (n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1) if len(dp(n,a,b)[1])>1}=={A,Z}
def action(z):
 if z in (A,Z):return 'C'
 return dp(*z)[1][0]
reached={A:[0,F(0),F(0)],Z:[0,F(0),F(0)]}
def first(n,a,b,mp,mq):
 z=n,a,b
 if z in reached:
  reached[z][0]+=1;reached[z][1]+=mp;reached[z][2]+=mq;return
 if action(z)!='C':return
 for i in range(3):first(n+1,a+(i==0),b+(i==1),mp*p[i],mq*q[i])
first(0,0,0,F(1),F(1))
assert reached[A]==[120,F(390625,5971968),F(390625,20155392)]
assert reached[Z]==[2258,F(28225,195689447424),F(28225,92876046336)]
print('FIRST_HITS_PASS',reached)
def literal(u,w):
 out=[F(0)]*4;nodes=0;leaves=0
 def walk(n,a,b,mp,mq):
  nonlocal nodes,leaves
  nodes+=1;z=n,a,b
  if z==A:
   out[1]+=mq*u;out[2]+=mp*u*n;out[3]+=mq*u*n
   mp*=1-u;mq*=1-u;act='C'
  elif z==Z:
   out[0]+=mp*w;out[2]+=mp*w*n;out[3]+=mq*w*n
   mp*=1-w;mq*=1-w;act='C'
  else:act=action(z)
  if mp==mq==0:return
  if act=='P':out[1]+=mq;out[2]+=mp*n;out[3]+=mq*n;leaves+=1
  elif act=='Q':out[0]+=mp;out[2]+=mp*n;out[3]+=mq*n;leaves+=1
  else:
   for i in range(3):walk(n+1,a+(i==0),b+(i==1),mp*p[i],mq*q[i])
 walk(0,0,0,F(1),F(1))
 return tuple(out),nodes,leaves
for w,aa,tt,qq in ((F(0),a0,t0,q0),(F(1),a1,t1,q1),
                    (F(1,2),(a0+a1)/2,(t0+t1)/2,(q0+q1)/2)):
 u=u0+d*w
 out,nodes,leaves=literal(u,w)
 assert out==(aa,aa,tt,qq)
 assert tt>qq
 print('DFS_PASS', 'w=',w,'u=',u,'nodes=',nodes,'leaves=',leaves,'moments=',*[str(x) for x in out])
print('PASS_INDEPENDENT_ORDERED_STAGE108')
