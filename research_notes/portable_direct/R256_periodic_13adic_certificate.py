"""R256 infinite-horizon exact certificate, s=67/169, frozen pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34."""
from fractions import Fraction as F
from math import lcm
S=F(67,169); T=989553240; J=1184397599; K=3805974000
W=[144,576,1440,4320,17280,86400,518400]
t=(1691*S-2615)/(2615*S-3539)
a=[F(1,5),F(1,4),F(3,10),F(9,20),S,F(2,3),t]
b=[F(13,60)]+[F(5,18)*abs(F(1,2)-a[i]) for i in range(1,7)]
pi=[b[i]/(1-a[i]) for i in range(7)]; assert sum(pi)==1
z=sum(b[i]/(1-a[i])**2 for i in range(7))
rho=[b[i]/(z*(1-a[i])**2) for i in range(7)]
assert lcm(*(x.denominator for x in a+b))==13*T

def mask(m): return [0]+[i+1 for i in range(6) if m>>i&1]
def mul(f,x):
 g=[F(0)]*(len(f)+1)
 for i,y in enumerate(f): g[i]-=x*y;g[i+1]+=y
 return g
def poly(ix):
 c=[F(1)]
 for i in ix:c=mul(c,a[i])
 for i in ix:
  d=[F(1)]
  for j in ix:
   if i!=j:d=mul(d,a[j])
  for j,x in enumerate(d):c[j]-=b[i]*x
 return c
def initial(ix,w):
 v=[F(1)]*len(ix);out=[]
 for k in range(len(ix)+3):
  h=w*sum(rho[i]*v[j] for j,i in enumerate(ix))
  if k>=3:
   q=J*T**k*h/K
   assert q.denominator==1
   out.append(int(q))
  c=sum(pi[i]*v[j] for j,i in enumerate(ix))
  v=[a[i]*v[j]+(1-a[i])*c for j,i in enumerate(ix)]
 return out
def orbit(c,q,p):
 state=tuple(x%p for x in q); seen={};values=[];d=len(q)
 for step in range(100000):
  if state in seen:return seen[state],step-seen[state],values
  seen[state]=step;values.append(state[0])
  nxt=-sum(c[j]*state[j] for j in range(d))%p
  state=state[1:]+(nxt,)
 raise AssertionError('orbit bound exceeded')
C=[];Q=[]
for m in range(63):
 ix=mask(m);d=len(ix)
 scaled=[x*T**(d-j) for j,x in enumerate(poly(ix))]
 assert all(x.denominator==1 for x in scaled)
 C.append(list(map(int,scaled)));Q.append(initial(ix,W[m.bit_count()]))
assert sum(map(len,Q))==249
assert J==lcm(*((W[m.bit_count()]*rho[i]).denominator for m in range(63) for i in mask(m)))
for p,m in [(2,3),(3,17),(5,2),(7,2),(70481,32),(904811,0)]:
 c=[v%p for v in C[m]];d=len(Q[m]);u=(-c[-2])%p
 assert c[:-2]==[0]*(d-1) and c[-1]==1 and u and all(v%p for v in Q[m])
for p,m,L in [(11,4,10),(17,32,8)]:
 start,period,values=orbit(C[m],Q[m],p)
 assert start==0 and period==L and all(values)
periods=[];values=[];L=1
for m in range(63):
 start,period,seq=orbit(C[m],Q[m],13)
 assert start==0
 periods.append(period);values.append(seq);L=lcm(L,period)
assert L==2184
zeros=[];cover=[9,26,10,13]
for i in range(L):
 active=lambda m:values[m][i%periods[m]]!=0
 if not any(active(m) for m in range(63)):zeros.append(i+3)
 else:assert any(active(m) for m in cover)
assert zeros==[1093,2185]
start,L169,seq=orbit(C[9],Q[9],169)
assert start==0 and L169==2184
assert [seq[(k-3)%L169] for k in zeros]==[143,26]
print('PASS: 63 masks, 249 exact integer bases, 9 prime witnesses')
print('p=13 periodicity=',L,'exceptional k mod 2184=',zeros,
      'R256 formula: LCM=J*T^k/K / (13 iff k mod 1092=1) for all k>=3')
