"""N14 Stage123 external auxiliary iid: exact arithmetic + literal ordered-path integer DFS."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
N=14;P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6));A=(9,3,0);B=(10,5,4);O=(0,0,0)
K=F(15175912302,20129609);L=F(14232343848,20129609)
alpha122=F(80432667641168459255,231610973507417014272)
V122=F(377878058477915699662445,29646204608949377826816)
y122=F(2367785183471,6494178000000)
def nxt(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
h={};pol={};gaps=[];ties={}
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v=[K*F(2**(a+b),3**a),L]
   if n<N:v.append(F(1)+sum(P[j]*h[q] for j,q in enumerate(nxt(s))))
   mv=min(v);h[s]=mv;opt=[j for j,x in enumerate(v) if x==mv]
   if len(opt)>1:ties[s]=opt
   pol[s]=opt[0];gaps.extend(x-mv for x in v if x>mv)
assert len(h)==680 and len(gaps)==1238 and ties=={A:[0,2],B:[1,2]}
assert min(gaps)==F(5078657746807,641138030936064)
assert h[O]==V122+(K+L)*alpha122
@lru_cache(None)
def moment(y,r):
 @lru_cache(None)
 def go(s):
  if s in (A,B):
   prop,term=(y,(F(0),F(1),F(0),F(0))) if s==A else (r,(F(1),F(0),F(0),F(0)))
   cont=forward(s)
   return tuple(prop*term[i]+(1-prop)*cont[i] for i in range(4))
  act=pol[s]
  if act==0:return(F(0),F(1),F(0),F(0))
  if act==1:return(F(1),F(0),F(0),F(0))
  return forward(s)
 def forward(s):
  ch=[go(t) for t in nxt(s)]
  return(sum(P[j]*ch[j][0] for j in range(3)),sum(Q[j]*ch[j][1] for j in range(3)),F(1)+sum(P[j]*ch[j][2] for j in range(3)),F(1)+sum(Q[j]*ch[j][3] for j in range(3)))
 return go(O)
m00=moment(F(0),F(0));m10=moment(F(1),F(0));m01=moment(F(0),F(1));m11=moment(F(1),F(1))
da=tuple(m10[i]-m00[i] for i in range(4));db=tuple(m01[i]-m00[i] for i in range(4));assert tuple(m00[i]+da[i]+db[i] for i in range(4))==m11
def diff(m):return m[0]-m[1]
y0=-diff(m00)/diff(da);dy=-diff(db)/diff(da)
rprev=(y122-y0)/dy
assert rprev in (F(0),F(1))
def balanced(r):
 y=y0+dy*r;return y,tuple(m00[i]+da[i]*y+db[i]*r for i in range(4))
ystart,mstart=balanced(rprev)
assert mstart[0]==mstart[1]==alpha122 and mstart[2]==V122
step=da[0]*dy+db[0]
rend=F(1) if step>0 else F(0)
if not 0<=y0+dy*rend<=1: rend=((F(1) if y0+dy*rend>1 else F(0))-y0)/dy
yend,mend=balanced(rend)
assert mend[0]>alpha122 and all(x>=0 for x in (rend,1-rend,yend,1-yend))
assert mstart[2]>mstart[3] and mend[2]>mend[3] and mend[2]+(K+L)*mend[0]==h[O]
assert y0==F(2367785183471,6494178000000)
assert dy==F(14328709,5541698560000)
assert yend==F(151539326395319,415627392000000)
assert step==F(37340424695,274501894527309053952)
assert mend[0]==F(2573845365525582162925,7411551152237344456704)
assert mend[2]==F(377878052586265662571445,29646204608949377826816)
PN=(3,1,20);QN=(1,1,10);pp=[24**i for i in range(15)];qq=[12**i for i in range(15)]
vis=[]
for y in (0,1):
 for r in (0,1):
  visits=[0];tot=[0,0,0,0];hits=defaultdict(lambda:[0,0,0])
  def dfs(s,pw,qw):
   visits[0]+=1;n,a,b=s
   if s in (A,B):
    z=hits[s];z[0]+=1;z[1]+=pw*pp[N-n];z[2]+=qw*qq[N-n]
   act=(0 if y else 2) if s==A else (1 if r else 2) if s==B else pol[s]
   if act<2:
    p=pw*pp[N-n];q=qw*qq[N-n]
    if act==0:tot[1]+=q
    else:tot[0]+=p
    tot[2]+=n*p;tot[3]+=n*q;return
   for j,t in enumerate(nxt(s)):dfs(t,pw*PN[j],qw*QN[j])
  dfs(O,1,1)
  measured=(F(tot[0],pp[N]),F(tot[1],qq[N]),F(tot[2],pp[N]),F(tot[3],qq[N]))
  assert measured==moment(F(y),F(r))
  assert hits[A][0]==84 and F(hits[A][1],pp[N])==F(109375,1990656) and F(hits[A][2],qq[N])==F(109375,6718464)
  assert hits[B][0]==371 and F(hits[B][1],pp[N])==F(1855,65229815808) and F(hits[B][2],qq[N])==F(1855,30958682112)
  vis.append(visits[0])
assert vis==[823333,815542,818293,810502]
print("PASS Stage123 exact 680-state/1238-gap Bellman, four ordered integer DFS corners",vis)
