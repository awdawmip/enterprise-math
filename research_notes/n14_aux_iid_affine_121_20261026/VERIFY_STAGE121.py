"""Portable exact Stage121 reproducer; external auxiliary iid model only."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict

N=14; P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
PN=(3,1,20); QN=(1,1,10)
K=F(320913819,414584); L=F(37979256,51823)
A=(9,3,0); G=(13,6,4); O=(0,0,0)
a120=F(2573764724900518487425,7411551152237344456704)
v120=F(378361860665073597077285,29646204608949377826816)
def nxt(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
V={};pol={};gaps=[];ties={}
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b); c=[K*F(2**(a+b),3**a),L]
   if n<N:c.append(F(1)+sum(P[j]*V[v] for j,v in enumerate(nxt(s))))
   low=min(c);V[s]=low
   cs=[i for i,t in enumerate(c) if t==low]
   if len(cs)>1:ties[s]=cs
   pol[s]=cs[0];gaps.extend(t-low for t in c if t>low)
assert len(V)==680 and len(gaps)==1238 and ties=={A:[0,2],G:[1,2]}
assert min(gaps)==F(110828719979,9903529525248)
assert V[O]==v120+(K+L)*a120
def moment(y,z):
 @lru_cache(None)
 def calc(s):
  if s==A:return combine(y,(F(0),F(1),F(0),F(0)),follow(s))
  if s==G:return combine(z,(F(1),F(0),F(0),F(0)),follow(s))
  a=pol[s]
  if a==0:return (F(0),F(1),F(0),F(0))
  if a==1:return (F(1),F(0),F(0),F(0))
  return follow(s)
 def combine(t,a,b):return tuple(t*x+(1-t)*q for x,q in zip(a,b))
 def follow(s):
  c=[calc(q) for q in nxt(s)]
  return (sum(P[j]*c[j][0] for j in range(3)),sum(Q[j]*c[j][1] for j in range(3)),F(1)+sum(P[j]*c[j][2] for j in range(3)),F(1)+sum(Q[j]*c[j][3] for j in range(3)))
 return calc(O)
m00=moment(F(0),F(0));m10=moment(F(1),F(0))
m01=moment(F(0),F(1));m11=moment(F(1),F(1))
da=tuple(m10[i]-m00[i] for i in range(4))
dg=tuple(m01[i]-m00[i] for i in range(4))
assert m11==tuple(m00[i]+da[i]+dg[i] for i in range(4))
def err(m):return m[0]-m[1]
y0=-err(m00)/err(da);slope=-err(dg)/err(da)
assert y0==F(665568609544933,2909391744000000)
assert slope==F(911009,20781369600)
def mix(z):
 y=y0+slope*z
 return y,tuple(m00[i]+da[i]*y+dg[i]*z for i in range(4))
corners={}
for y in (0,1):
 for z in (0,1):
  hits=defaultdict(lambda:[0,0,0]);values=[0,0,0,0];visits=[0]
  def dfs(q,pw,qw):
   visits[0]+=1;n,a,b=q
   if q in (A,G):
    h=hits[q];h[0]+=1;h[1]+=pw*24**(N-n);h[2]+=qw*12**(N-n)
   move=(0 if y else 2) if q==A else (1 if z else 2) if q==G else pol[q]
   if move<2:
    p=pw*24**(N-n);qmass=qw*12**(N-n)
    if move==1:values[0]+=p
    else:values[1]+=qmass
    values[2]+=n*p;values[3]+=n*qmass
    return
   for j,t in enumerate(nxt(q)):dfs(t,pw*PN[j],qw*QN[j])
  dfs(O,1,1)
  observed=(F(values[0],24**N),F(values[1],12**N),F(values[2],24**N),F(values[3],12**N))
  assert observed==moment(F(y),F(z))
  corners[y,z]=visits[0]
  if (y,z)==(0,0):
   assert hits[A][0]==84 and hits[G][0]==15058
   assert F(hits[A][1],24**N)==F(109375,1990656)
   assert F(hits[G][2],12**N)==F(941125,6687075336192)
assert [corners[k] for k in [(0,0),(0,1),(1,0),(1,1)]]==[885985,840811,880945,835771]
yend,mend=mix(F(1));ystart,mstart=mix(F(0))
assert 0<y0<yend<1
assert mstart[0]==mstart[1]==a120 and mstart[2]==v120
assert mend[0]==mend[1]==F(2573764738946831699425,7411551152237344456704)
assert mend[2]==F(378361775997993165503285,29646204608949377826816)
assert mend[0]-mstart[0]==F(48771920875,25734552611935223808)
for m in (mstart,mend):assert m[2]>m[3] and m[2]+(K+L)*m[0]==V[O]
print("PASS Stage121, 680 states, 1238 strict positive gaps, full real interval by endpoint affinity, integer DFS crosscheck", corners)
