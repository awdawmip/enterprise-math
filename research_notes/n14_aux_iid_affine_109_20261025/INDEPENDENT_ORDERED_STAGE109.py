#!/usr/bin/env python3
"""Independent top-down Bellman plus literal ordered ternary-history DFS. Author-side."""
from fractions import Fraction as F
from functools import lru_cache
p=(F(1,8),F(1,24),F(5,6));q=(F(1,12),F(1,12),F(5,6))
K=F(491857029,506348);L=F(116416632,126587)
A=(10,3,0);D=(10,3,3)
u0=F(159404052982303,211315200000000); d=F(22757603,10565760000)
a0=F(13084095824621807507,37682150988866125824)
a1=F(13084102500820187507,37682150988866125824)
v0=F(1934483126570299962385,150728603955464503296)
v1=F(1934432626777903782385,150728603955464503296)
q0=F(38346074856588751535,3140179249072177152)
q1=F(115034081136642114605,9420537747216531456)
@lru_cache(None)
def dp(n,a,b):
 opts={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<14:opts['C']=1+sum((p[i]*dp(n+1,a+(i==0),b+(i==1))[0] for i in range(3)),F(0))
 v=min(opts.values());return v,tuple(s for s,t in opts.items() if t==v)
assert { (n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1) if len(dp(n,a,b)[1])>1}=={A,D}
def decision(z):return 'C' if z in (A,D) else dp(*z)[1][0]
reached={A:[0,F(0),F(0)],D:[0,F(0),F(0)]}
def visit(n,a,b,p_weight,q_weight):
 z=n,a,b
 if z in reached:
  reached[z][0]+=1;reached[z][1]+=p_weight;reached[z][2]+=q_weight;return
 if decision(z)!='C':return
 for i in range(3):visit(n+1,a+(i==0),b+(i==1),p_weight*p[i],q_weight*q[i])
visit(0,0,0,F(1),F(1))
assert reached[A]==[120,F(390625,5971968),F(390625,20155392)]
assert reached[D]==[2051,F(1281875,9172942848),F(1281875,3869835264)]
def literal(u,w):
 out=[F(0)]*4;nodes=0;leaves=0
 def walk(n,a,b,px,qx):
  nonlocal nodes,leaves
  nodes+=1;z=n,a,b
  if z==A:
   out[1]+=qx*u;out[2]+=px*u*n;out[3]+=qx*u*n
   px*=1-u;qx*=1-u;act='C'
  elif z==D:
   out[0]+=px*w;out[2]+=px*w*n;out[3]+=qx*w*n
   px*=1-w;qx*=1-w;act='C'
  else:act=decision(z)
  if px==qx==0:return
  if act=='P':out[1]+=qx;out[2]+=px*n;out[3]+=qx*n;leaves+=1
  elif act=='Q':out[0]+=px;out[2]+=px*n;out[3]+=qx*n;leaves+=1
  else:
   for i in range(3):walk(n+1,a+(i==0),b+(i==1),px*p[i],qx*q[i])
 walk(0,0,0,F(1),F(1))
 return tuple(out),nodes,leaves
for z, aa,vv,qq in ((F(0),a0,v0,q0),(F(1),a1,v1,q1),
                      (F(1,2),(a0+a1)/2,(v0+v1)/2,(q0+q1)/2)):
 u=u0+d*z
 out,nodes,leaves=literal(u,z)
 assert out==(aa,aa,vv,qq)
 assert vv>qq
 print('DFS_PASS','w=',z,'u=',u,'nodes=',nodes,'leaves=',leaves,'moments=',*[str(x) for x in out])
print('PASS_INDEPENDENT_LITERAL_STAGE109')
