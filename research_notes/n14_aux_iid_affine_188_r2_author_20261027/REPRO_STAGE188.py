#!/usr/bin/env python3
"""Stage188 exact independent reference replay. Positive-rational IID model only."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6)); N=14
K=F(39993714743501421,226849611128761)
L=F(39205434834768424,226849611128761)
H=F(552023450050793309312530706424493,4142313307078339047903008391168)
R=(5,2,0); X=(8,0,1)
A187=F(47564236941933996508186187,135753377754634620902572032)
V187=F(47526009692613945133124984819,4344108088148307868882305024)
def child(s,i):
 n,a,b=s
 return n+1,a+(i==0),b+(i==1)
@lru_cache(None)
def bell(s):
 n,a,b=s
 opts=[("P",K*F(2**(a+b),3**a)),("Q",L)]
 if n<N:opts.append(("C",1+sum(P[i]*bell(child(s,i))[0] for i in range(3))))
 v=min(v for _,v in opts)
 return v,tuple(act for act,x in opts if x==v),tuple(x-v for _,x in opts if x>v)
states=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
ties={s:bell(s)[1] for s in states if len(bell(s)[1])>1}
gaps=[z for s in states for z in bell(s)[2]]
assert len(states)==680 and ties=={R:("P","C"),X:("Q","C")}
assert len(gaps)==1238 and min(gaps)==F(1858369546682908,55124455504288923)
assert bell((0,0,0))[0]==H
def O(r,x):
 @lru_cache(None)
 def dp(s):
  if s==R:return weighted((F(0),F(1),F(0),F(0)), cont(s),r)
  if s==X:return weighted((F(1),F(0),F(0),F(0)), cont(s),x)
  act=bell(s)[1]
  assert len(act)==1
  if act[0]=="P":return F(0),F(1),F(0),F(0)
  if act[0]=="Q":return F(1),F(0),F(0),F(0)
  return cont(s)
 def cont(s):
  vs=[dp(child(s,i)) for i in range(3)]
  return tuple(sum((P if j%2==0 else Q)[i]*vs[i][j] for i in range(3))+(j>=2) for j in range(4))
 return dp((0,0,0))
def weighted(a,b,r):return tuple(r*v+(1-r)*u for v,u in zip(a,b))
corner={(r,x):O(F(r),F(x)) for r,x in product([0,1],repeat=2)}
B=corner[0,0]
DR=tuple(corner[1,0][i]-B[i] for i in range(4))
DX=tuple(corner[0,1][i]-B[i] for i in range(4))
C=tuple(corner[1,1][i]-corner[1,0][i]-corner[0,1][i]+B[i] for i in range(4))
assert C==(F(0),)*4 and R[1]>X[1] and R[0]<X[0]
base_policy={s:bell(s)[1][0] for s in states}
DEN=24**N
def dfs(rc,xc):
 total=[0,0,0,0]; nodes=0; counts=[0,0]
 def visit(n,a,b,p,q):
  nonlocal nodes
  nodes+=1;s=(n,a,b)
  if s==R:counts[0]+=1
  if s==X:counts[1]+=1
  action=base_policy[s]
  if s==R:action="P" if rc else "C"
  if s==X:action="Q" if xc else "C"
  if action!="C":
   scale=24**(N-n)
   if action=="Q":total[0]+=p*scale
   if action=="P":total[1]+=q*scale
   total[2]+=n*p*scale;total[3]+=n*q*scale
  else:
   assert n<N
   visit(n+1,a+1,b,3*p,2*q)
   visit(n+1,a,b+1,p,2*q)
   visit(n+1,a,b,20*p,20*q)
 visit(0,0,0,1,1)
 return tuple(F(t,DEN) for t in total),nodes,counts
nodes=0
for r,x in product([0,1],repeat=2):
 o,n,h=dfs(r,x)
 assert o==corner[r,x]
 print("corner",r,x,"nodes",n,"R/X hits",h)
 nodes+=n
assert nodes==765520
d0=B[0]-B[1];dr=DR[0]-DR[1];dx=DX[0]-DX[1]
r0=-d0/dr; slope=-dx/dr
assert r0==F(1085148487960651,12688037270560000)
assert slope==F(280862064000,79300232941)
xstar=(1-r0)/slope
assert xstar==F(1289209864733261,4993103360000000) and 0<xstar<1
def obs(x):
 r=r0+slope*x
 return tuple(B[i]+DR[i]*r+DX[i]*x for i in range(4))
start=obs(F(0));end=obs(xstar)
assert start[0]==A187 and start[2]==V187 and start[0]==start[1]
assert end[0]==F(9370003598922725167379,26711406663770723844096)
assert end[2]==F(1153476444134184737662789,106845626655082895376384)
assert end[0]==end[1] and end[2]>end[3] and start[2]>start[3]
assert end[0]>start[0] and end[2]<start[2]
assert end[2]+K*end[1]+L*end[0]==H
assert end[0]-start[0]==F(292456756478102828004390419621,706073590206266022084331922522112)
print("stage188",end[0],end[2],"nodes",nodes)
print("STAGE188_REPRO_PASS")
