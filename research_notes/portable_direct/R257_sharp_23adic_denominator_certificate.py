"""R257 all-horizon exact denominator certificate, s=770/1973, frozen pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34."""
from fractions import Fraction as F
from math import lcm
S=F(770,1973); T=153448180920; J=327870790093; K=166791501000
W=[144,576,1440,4320,17280,86400,518400]
t=(1691*S-2615)/(2615*S-3539)
a=[F(1,5),F(1,4),F(3,10),F(9,20),S,F(2,3),t]
b=[F(13,60)]+[F(5,18)*abs(F(1,2)-a[i]) for i in range(1,7)]
pi=[b[i]/(1-a[i]) for i in range(7)]; assert sum(pi)==1
z=sum(b[i]/(1-a[i])**2 for i in range(7))
rho=[b[i]/(z*(1-a[i])**2) for i in range(7)]
assert t==F(1285775,1656299)
assert lcm(*(x.denominator for x in a+b))==23*T

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
# All 249 base values are integral after this exact normalization.
from math import gcd
from functools import reduce
assert reduce(gcd,(abs(v) for row in Q for v in row))==1
assert sum(len(row)-1 for row in C)==249

# The minimal characteristic scaling is T; reducing any prime power fails.
for p in (2,3,5,23,31,101,1973):
    Tsmall=T//p
    assert any(any((v*Tsmall**(len(mask(m))-j)).denominator!=1
                   for j,v in enumerate(poly(mask(m))))
               for m in range(63))

# An eventually geometric witness preserves every prime factor of D_k.
geom=((2,3),(3,17),(5,2),(7,2),(23,42),
      (31,32),(101,32),(1973,8),(3061,0),(3469,0))
for p,m in geom:
    c=[v%p for v in C[m]];d=len(Q[m]);u=(-c[-2])%p
    assert c[:-2]==[0]*(d-1) and c[-1]==1
    assert u and all(v%p for v in Q[m])

# The two remaining primes are protected by short complete modular orbits.
for p,m,period_expected in ((11,4,10),(401,49,200)):
    start,period,values=orbit(C[m],Q[m],p)
    assert start==0 and period==period_expected and all(values)

# Direct Fraction propagation provides an independent finite crosscheck.
def direct(m,kmax):
    ix=mask(m);w=W[m.bit_count()]
    v=[F(1)]*len(ix);res=[]
    for k in range(kmax+1):
        res.append(w*sum(rho[i]*v[j] for j,i in enumerate(ix)))
        total=sum(pi[i]*v[j] for j,i in enumerate(ix))
        v=[a[i]*v[j]+(1-a[i])*total for j,i in enumerate(ix)]
    return res
fractions=[direct(m,16) for m in range(63)]
for k in (3,4,5,6,7,8,10,12,16):
    D=J*T**k//K
    assert J*T**k%K==0
    assert lcm(*(fractions[m][k].denominator for m in range(63)))==D

print("PASS R257: 63 labelled masks, 249 integral bases, 12 prime witnesses")
print("s=770/1973: exact common denominator J*T**k/K for all k>=3; no 23-adic dip")
