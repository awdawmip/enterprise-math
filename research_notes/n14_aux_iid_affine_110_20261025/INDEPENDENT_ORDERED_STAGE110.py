#!/usr/bin/env python3
"""Independent author-side top-down Bellman and full ordered-history DFS, Stage110."""
from fractions import Fraction as F
from functools import lru_cache
p=(F(1,8),F(1,24),F(5,6));q=(F(1,12),F(1,12),F(5,6))
K=F(6497577,6734);L=F(3069240,3367)
A=(10,3,0);E=(13,6,4)
u0=F(159859205042303,211315200000000)
du=F(327789,7043840000)
a0=F(13084102500820187507,37682150988866125824)
a1=F(13084102571183753507,37682150988866125824)
v0=F(1934432626777903782385,150728603955464503296)
v1=F(1934432098641265410385,150728603955464503296)
q0=F(115034081136642114605,9420537747216531456)
q1=F(115034069193316692605,9420537747216531456)
@lru_cache(None)
def dp(n,a,b):
 costs={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<14:costs['C']=1+sum((p[j]*dp(n+1,a+(j==0),b+(j==1))[0] for j in range(3)),F(0))
 m=min(costs.values())
 return m,tuple(t for t,v in costs.items() if v==m)
assert {(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1) if len(dp(n,a,b)[1])>1}=={A,E}
assert dp.cache_info().currsize==680
def act(z):return 'C' if z in (A,E) else dp(*z)[1][0]
hits=[0,F(0),F(0)]
def first_hit(n,a,b,px,qx):
 z=n,a,b
 if z==E:
  hits[0]+=1;hits[1]+=px;hits[2]+=qx;return
 if act(z)!='C':return
 for i in range(3):first_hit(n+1,a+(i==0),b+(i==1),px*p[i],qx*q[i])
first_hit(0,0,0,F(1),F(1))
assert hits==[16254,F(37625,347892350976),F(37625,247669456896)]
def literal(u,w):
 ans=[F(0)]*4;counts=[0,0]
 def walk(n,a,b,px,qx):
  counts[0]+=1;z=n,a,b
  if z==A:
   ans[1]+=qx*u;ans[2]+=px*u*n;ans[3]+=qx*u*n
   px*=1-u;qx*=1-u;decision='C'
  elif z==E:
   ans[0]+=px*w;ans[2]+=px*w*n;ans[3]+=qx*w*n
   px*=1-w;qx*=1-w;decision='C'
  else:decision=act(z)
  if px==qx==0:return
  if decision=='P':
   ans[1]+=qx;ans[2]+=px*n;ans[3]+=qx*n;counts[1]+=1
  elif decision=='Q':
   ans[0]+=px;ans[2]+=px*n;ans[3]+=qx*n;counts[1]+=1
  else:
   for i in range(3):walk(n+1,a+(i==0),b+(i==1),px*p[i],qx*q[i])
 walk(0,0,0,F(1),F(1))
 return tuple(ans),*counts
for w,aa,vv,qq in ((F(0),a0,v0,q0),(F(1),a1,v1,q1),(F(1,2),(a0+a1)/2,(v0+v1)/2,(q0+q1)/2)):
 row,nodes,leaves=literal(u0+du*w,w)
 assert row==(aa,aa,vv,qq) and row[2]>row[3]
 print('ORDERED_DFS_PASS',w,'nodes',nodes,'leaves',leaves,'moments',row)
print('PASS_STAGE110_INDEPENDENT_LITERAL')
