#!/usr/bin/env python3
"""Exact rational R5 certificate: generic physical 15-edge minimum, 2026-11-10."""
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm
def q(s):return tuple(map(F,s.split()))
r=q('1/10 1/2 3/4 1 5/4 3/2 19/10')
J=(1,2,3,5)
a=(36,28,23,18,13,8,0)
b=(-36,-36,-31,-18,-5,0,0)
c=(36,36,31,18,0,0,0)
D=((0,0),(6,6))+tuple((i,j) for j in J for i in range(7))
def rr(M):
 M=[[F(t) for t in row] for row in M]
 h=len(M);w=len(M[0]);p=[];k=0
 for j in range(w):
  z=next((i for i in range(k,h) if M[i][j]),None)
  if z is None:continue
  M[k],M[z]=M[z],M[k]
  f=M[k][j];M[k]=[x/f for x in M[k]]
  for i in range(h):
   if i!=k and M[i][j]:
    f=M[i][j];M[i]=[x-f*y for x,y in zip(M[i],M[k])]
  p.append(j);k+=1
  if k==h:break
 return M,p
def rankcols(V):return len(rr(list(map(list,zip(*V))))[1])
def kernel(M):
 R,P=rr(M);free=[j for j in range(len(M[0])) if j not in P]
 return [tuple(-R[P.index(i)][j] if i in P else F(i==j) for i in range(len(M[0]))) for j in free]
def C(e):
 i,j=e;v=[F(0)]*21
 v[i]=1;v[7+j]=1;v[14+j]=r[i]
 return tuple(v)
def A(e):return F(a[e[0]]-18)
def B(e):return F(b[e[0]]+c[e[1]])
def H(e):
 i,j=e
 return tuple(r[i]-r[j] if j==k else F(0) for k in J)
def canon(x,y):
 if x==y==0:return None
 z=lcm(x.denominator,y.denominator);u,v=int(x*z),int(y*z)
 g=gcd(u,v);u//=g;v//=g
 return (-u,-v) if u<0 or (u==0 and v<0) else (u,v)
def mass(x):
 g,aa,bb,u,v,w,z=x
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
  F(13,40)*aa+bb/80-u,(g-aa)/2,
  1-g+aa/10+F(9,40)*bb-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
  (g-bb)/2,F(3,40)*aa+F(21,80)*bb-w,
  u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def time(x):
 g,aa,bb,u,v,w,z=x
 return (1+g+F(3,8)*aa+F(5,8)*bb+u/2+v+F(3,2)*w,
  1+g+(aa+bb)/2+u+v+w)
def constraints(p):
 x,y=p[:7],p[7:]
 return (x[0]-x[2],y[0]-1,y[6]-y[1]/10,*[u-v for u,v in zip(time(x),time(y))])
def observe(p):return mass(p[7:])+mass(p[:7])
def rhs(m):return m+tuple(r[j]*m[7+j] for j in range(7))
def jac(fun):
 zero=(F(0),)*14;f0=fun(zero)
 return [[fun(tuple(F(i==j) for i in range(14)))[k]-f0[k] for j in range(14)] for k in range(len(f0))]
N=kernel(jac(constraints));assert len(N)==9
Jm=jac(observe)
X=q('999/1000 1/6 999/1000 1/20 29/240 11/160 1/120')
Y0=q('1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200')
Hstar=F(17774559,17507527960)
X=X[:6]+(X[6]+Hstar/2,)
DY=q('0 1 0 -1/4 -1/4 0 1/10')
Y=tuple(y+z/100000 for y,z in zip(Y0,DY))
p=X+Y
assert constraints(p)==(F(0),)*5
W=[rhs(observe(p))]+[rhs(tuple(sum(Jm[i][k]*n[k] for k in range(14)) for i in range(14))) for n in N]
assert rankcols(W)==9 and rankcols(W[1:])==8
assert rankcols([C(e) for e in D])==15
assert rankcols([H(e)+(A(e),B(e)) for e in D])==6
m=observe(p)
assert all(m[7+j]>m[j] for j in J)
def slacks(x):
 g,aa,bb,u,v,w,z=x
 return (aa,g-aa,1-g,bb,g-bb,u,F(13,40)*aa+bb/80-u,
  w,F(3,40)*aa+F(21,80)*bb-w,z,aa/10-z,v-z,z+F(9,40)*bb-v)
for x,forced in [(X,(4,)),(Y,(2,10))]:
 assert all(z==0 for k,z in enumerate(slacks(x)) if k in forced)
 assert all(z>0 for k,z in enumerate(slacks(x)) if k not in forced)
SB=((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),(0,3),(1,3),
    (3,3),(4,3),(5,3),(4,5),(5,5),(6,5),(6,6))
PIV=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
tau=F(1,10**7);base=rhs(m)
rem=[base[k]-tau*sum(C(e)[k] for e in D) for k in PIV]
mat=[[C(e)[k] for e in SB]+[z] for k,z in zip(PIV,rem)]
reduced,pivots=rr(mat)
assert pivots==list(range(15))
E={e:tau for e in D}
for e,row in zip(SB,reduced):E[e]+=row[-1]
assert min(E.values())==tau
assert all(sum(E[e]*C(e)[k] for e in D)==base[k] for k in range(21))
exceptions=set()
for j in J:
 for i,k in combinations(range(7),2):
  d1,d2=r[i]-r[j],r[k]-r[j]
  u=A((i,j))*d2-A((k,j))*d1
  v=B((i,j))*d2-B((k,j))*d1
  if u or v:exceptions.add(canon(-v,u))
 exceptions.add(canon(-B((j,j)),A((j,j))))
for e in ((0,0),(6,6)):exceptions.add(canon(-B(e),A(e)))
exceptions.discard(None)
assert len(exceptions)==20
def zero_sets(pair,j):
 l,m=pair;diag=((j,j),) if l*A((j,j))+m*B((j,j))==0 else ()
 groups={}
 for i in range(7):
  if i==j:continue
  z=-(l*A((i,j))+m*B((i,j)))/(r[i]-r[j])
  groups.setdefault(z,[]).append((i,j))
 largest=max(map(len,groups.values()))
 return [diag+tuple(v) for v in groups.values() if len(v)==largest]
def maximum(pair):
 l,m=pair
 endpoints=tuple(e for e in ((0,0),(6,6)) if l*A(e)+m*B(e)==0)
 options=[zero_sets(pair,j) for j in J]
 return len(endpoints)+sum(len(opt[0]) for opt in options), endpoints, options
assert (1,97) not in exceptions
assert maximum((1,97))[0]==6
scores={pair:maximum(pair)[0] for pair in exceptions}
assert max(scores.values())==14
assert [pair for pair,score in scores.items() if score==14]==[(0,1)]
assert sorted([score for score in scores.values() if score!=14])[-1]==12
n,endpoints,options=maximum((0,1))
assert n==14 and len(endpoints)==2 and [len(o) for o in options]==[1,1,3,1]
for combo in [(x,y,z,w) for x in options[0] for y in options[1] for z in options[2] for w in options[3]]:
 S=endpoints+sum(combo,())
 assert len(S)==14
 rankS=rankcols([C(e) for e in S])
 rankSW=rankcols([C(e) for e in S]+W)
 assert rankSW>rankS
 print('EXCEPTIONAL_14_CHART',tuple(i for i,j in combo[2] if j==3 and i!=3), 'rank',rankS,'rank_with_physical',rankSW)
print('PASS_PHYSICAL_AFFINE_DIM',rankcols(W)-1)
print('PASS_30_EDGE_RANK',rankcols([C(e) for e in D]))
print('PASS_PROJECTIVE_EXCEPTIONS',len(exceptions),'max',max(scores.values()),'generic',maximum((1,97))[0])
print('PASS_NO_SUPPORT_LE_14_CONTAINS_EIGHT_DIM_PHYSICAL_HULL')
print('THEOREM_GENERIC_PHYSICAL_MINIMUM_IS_15_WITHIN_STRICT_DEFICIT_CHAMBER')
