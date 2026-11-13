"""R636 compact reproducible exact signed BRC rank-two reference witness."""
from math import comb
from itertools import permutations,combinations

def b(n,k):return comb(n,k) if 0<=k<=n else 0
def norm(a):
 a=list(a)
 while len(a)>1 and not a[-1]:a.pop()
 return a
def add(*rows):
 z=[0]*max(map(len,rows))
 for r in rows:
  for i,v in enumerate(r):z[i]+=v
 return norm(z)
def mul(x,y):
 z=[0]*(len(x)+len(y)-1)
 for i,a in enumerate(x):
  for j,b in enumerate(y):z[i+j]+=a*b
 return norm(z)
def prod(rows):
 p=[1]
 for x in rows:p=mul(p,x)
 return p
def shift(x,n):return [0]*n+list(x)
def scale(x,k):return norm([v*k for v in x])
def sub(x,y):return add(x,scale(y,-1))
def divint(x,d):
 assert d and all(v%d==0 for v in x)
 return norm([v//d for v in x])
def ord5(x):return next((i for i,v in enumerate(x) if v%5),10**9)
def K(i):
 ds=(-b(4,i)+b(2,i-1),b(5,i-1)-b(5,i-2),b(7,i-2),-b(9,i-3))
 return add(*([shift([-v*b(i+1-j,q) for q in range(i+2-j)],i-1) for j,v in enumerate(ds,1) if v and i+1-j>=0] or [[0]]))

c=(0,5,1,2,3,4); P=[K(i) for i in range(1,13,2)]; M=[K(i) for i in range(2,13,2)]
U=[P[j][2*j:] for j in range(6)];V=[M[j][2*j+1:] for j in range(6)]
assert [x[0] for x in U]==[2,-8,6,106,83,9]
assert [x[0] for x in V]==[-1,-11,53,119,36,1]
W=scale(prod([z for j in range(6) for z in (U[j],V[j])]),12)
checks=0
for a in (1,2,4):
 v=[a+2*j for j in range(6)]; C=[shift(W,k) for k in v]
 for r in range(6):
  p,q=[j for j in range(6) if j!=r][-2:];d=c[p]-c[r]
  assert 12%d==0 and d%5 and (c[q]-c[r])%5
  T=divint(sub(C[p],C[q]),d)
  for x in range(6):
   k=q if x==p else p if x==q else x
   h=scale(T,c[x]-c[r]);Z=sub(C[x],h)
   F=add(shift([d],v[x]),shift([c[r]-c[x]],v[p]),shift([c[x]-c[r]],v[q]))
   assert not any(F[:v[k]])
   Ap=shift(mul(divint(prod([z for j in range(6) for typ,z in enumerate((U[j],V[j])) if (j,typ)!=(k,0)]),1),divint(F[v[k]:],1)),a)
   Am=shift(mul(prod([z for j in range(6) for typ,z in enumerate((U[j],V[j])) if (j,typ)!=(k,1)]),F[v[k]:]),a-1)
   factor=12//d
   Ap=scale(Ap,factor); Am=scale(Am,factor)
   assert ord5(Ap)==a and ord5(Am)==a-1
   assert add(mul(Ap,P[k]),h)==C[x]==add(mul(Am,M[k]),h)
   checks+=2
  assert scale(T,c[r]-c[r])==[0]
 H0=[7,0,3,1];H1=[-2,4,0,5]
 B=[add(H0,scale(H1,z)) for z in c]
 Q=[mul(shift([1,j+1],a),P[j]) for j in range(6)]
 for r,s in combinations(range(6),2):
  h1=divint(sub(B[s],B[r]),c[s]-c[r]);h0=sub(B[r],scale(h1,c[r]))
  assert h0==H0 and h1==H1
  for pi in permutations(range(6)):
   sig=[ord5(Q[pi[x]]) for x in range(6)]
   inferred=tuple(5 if z>a+8 else (z-a)//2 for z in sig)
   assert inferred==pi
   checks+=1
print('R636_COMPACT_REPRODUCE_PASS',checks)
