"""Stage124 exact Fraction Bellman/observer proof checker, author implementation."""
from fractions import Fraction as F
from functools import lru_cache
import json
N=14;P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(1245231873,1658336);L=F(36440256,51823)
A=(9,3,0);T=(14,7,4);ROOT=(0,0,0)
kids=lambda s:((s[0]+1,s[1]+1,s[2]),(s[0]+1,s[1],s[2]+1),(s[0]+1,s[1],s[2]))
V={};ACT={};TIES={};GAPS=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);ratio=F(2**(a+b),3**a)
   costs={'P':K*ratio,'Q':L}
   if n<N:costs['C']=1+sum(P[j]*V[t] for j,t in enumerate(kids(s)))
   best=min(costs.values());V[s]=best
   options=[name for name,c in costs.items() if c==best];ACT[s]=options[0]
   if len(options)>1:TIES[s]=options
   GAPS.extend(c-best for c in costs.values() if c>best)
assert len(V)==680 and len(GAPS)==1238
assert TIES=={A:['P','C'],T:['P','Q']}
assert min(GAPS)==F(294166217221,39614118100992)
assert V[ROOT]==F(5878829162353591081475135,11355563791072559628288)
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
mul=lambda v,k:tuple(k*x for x in v)
@lru_cache(None)
def m(s,y,z):
 def cont():
  vs=[m(child,y,z) for child in kids(s)]
  return (sum(P[j]*vs[j][0] for j in range(3)),
   sum(Q[j]*vs[j][1] for j in range(3)),
   1+sum(P[j]*vs[j][2] for j in range(3)),
   1+sum(Q[j]*vs[j][3] for j in range(3)))
 if s==A:return add(mul((F(0),F(1),F(0),F(0)),y),mul(cont(),1-y))
 if s==T:return add(mul((F(0),F(1),F(0),F(0)),1-z),mul((F(1),F(0),F(0),F(0)),z))
 if ACT[s]=='P':return (F(0),F(1),F(0),F(0))
 if ACT[s]=='Q':return (F(1),F(0),F(0),F(0))
 return cont()
base=m(ROOT,F(0),F(0));dA=sub(m(ROOT,F(1),F(0)),base)
dT=sub(m(ROOT,F(0),F(1)),base)
assert m(ROOT,F(1),F(1))==add(add(base,dA),dT)
assert dT==(F(165875,25048249270272),-F(165875,26748301344768),F(0),F(0))
err=lambda v:v[0]-v[1]
y0=-err(base)/err(dA);slope=-err(dT)/err(dA)
assert y0==F(151539326395319,415627392000000)
assert slope==F(160567,6927123200)
assert 0<y0<y0+slope<1
def point(z):
 y=y0+slope*z
 v=add(add(base,mul(dA,y)),mul(dT,z))
 assert v[0]==v[1] and v[2]>v[3]
 assert v[2]+(K+L)*v[0]==V[ROOT]
 return v
v0,v1=point(F(0)),point(F(1))
assert v0[0]==F(2573845365525582162925,7411551152237344456704)
assert v0[2]==F(377878052586265662571445,29646204608949377826816)
assert v1[0]==F(2573845372952647230925,7411551152237344456704)
assert v1[2]==F(377878009388672358128945,29646204608949377826816)
eta=v1[0]-v0[0]
assert eta==F(8596140125,8578184203978407936)
assert v0[2]-v1[2]==(K+L)*eta
print(json.dumps({'status':'PASS','states':len(V),'positive_gaps':len(GAPS),
 'minimum_positive_gap':str(min(GAPS)),'root':str(V[ROOT]),
 'ties':{str(s):actions for s,actions in TIES.items()},
 'base':list(map(str,base)),'dA':list(map(str,dA)),
 'dT':list(map(str,dT)),'balance_y0':str(y0),
 'balance_slope':str(slope),'eta124':str(eta),
 'alpha124':str(v1[0]),'V124':str(v1[2]),
 'time_margin_left':str(v0[2]-v0[3]),
 'time_margin_right':str(v1[2]-v1[3])},indent=2))
