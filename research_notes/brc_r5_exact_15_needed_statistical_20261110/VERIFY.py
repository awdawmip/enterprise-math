#!/usr/bin/env python3
"""Exact rational 15-support necessity certificate for R5 seven-LR Blackwell observer.
Static statistical face only; the perturbed witness is not asserted physically g=b.
All verification is Python standard-library Fraction arithmetic.
"""
from fractions import Fraction as Q
from math import factorial, lcm

R=tuple(map(Q,'1/10 1/2 3/4 1 5/4 3/2 19/10'.split()))
def vec(s): return tuple(map(Q,s.split()))
X0=vec('999/1000 1/6 999/1000 1/20 29/240 11/160 1/120')
Y0=vec('1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200')
H=Q('17774559/17507527960')
X=X0[:6]+(X0[6]+H/2,)
Y=tuple(a+Q('1/100000')*b for a,b in zip(Y0,vec('0 1 0 -1/4 -1/4 0 1/10')))
def mass(f):
 g,a,b,u,v,w,z=f
 return (Q(509,900)*u+Q(47,180)*z+Q(67,162)*(v-z)+w/100,
         Q(13,40)*a+b/80-u,(g-a)/2,
         1-g+a/10+Q(9,40)*b-v+Q(191,450)*(u+w)+Q(43,90)*z+Q(14,81)*(v-z),
         (g-b)/2,Q(3,40)*a+Q(21,80)*b-w,
         u/100+Q(47,180)*z+Q(67,162)*(v-z)+Q(509,900)*w)
MU,NU=mass(Y),mass(X)
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)
assert len(D)==30
COL={e:tuple(Q(1) if k==e[0] or k==7+e[1] else R[e[0]] if k==14+e[1] else Q(0) for k in range(21)) for e in D}
def mv(M,v):return tuple(sum((a*b for a,b in zip(row,v)),Q(0)) for row in M)
def rref(mat):
 a=[list(map(Q,row)) for row in mat];n=len(a);m=len(a[0]);piv=[];h=0
 for k in range(m):
  p=next((i for i in range(h,n) if a[i][k]),None)
  if p is None:continue
  a[h],a[p]=a[p]
  d=a[h][k];a[h]=[x/d for x in a[h]]
  for i in range(n):
   if i!=h:
    d=a[i][k]
    if d:a[i]=[x-d*y for x,y in zip(a[i],a[h])]
  piv.append(k);h+=1
  if h==n:break
 return a,piv
def rank(mat):return len(rref(mat)[1])
def solve(A,b):
 n=len(b);m=[list(row)+[x] for row,x in zip(A,b)];det=Q(1)
 for k in range(n):
  p=next((i for i in range(k,n) if m[i][k]),None)
  assert p is not None
  if p!=k:m[k],m[p]=m[p],m[k];det=-det
  d=m[k][k];det*=d;m[k]=[v/d for v in m[k]]
  for i in range(n):
   if i!=k:
    d=m[i][k]
    if d:m[i]=[x-d*y for x,y in zip(m[i],m[k])]
 return tuple(row[-1] for row in m),det
B=((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),(0,3),(1,3),(3,3),(4,3),(5,3),(4,5),(5,5),(6,5),(6,6))
P=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
A=tuple(tuple(COL[e][k] for e in D) for k in range(21))
rhs=MU+NU+tuple(R[j]*NU[j] for j in range(7))
TAU=Q('1/10000000')
res=tuple(rhs[k]-TAU*sum((COL[e][k] for e in D),Q(0)) for k in range(21))
z,det=solve([[COL[e][k] for e in B] for k in P],tuple(res[k] for k in P))
assert det==Q(-299,1600)
E0={e:TAU for e in D}
for e,w in zip(B,z):E0[e]+=w
assert min(E0.values())==TAU
assert tuple(sum((E0[e]*COL[e][k] for e in D),Q(0)) for k in range(21))==rhs
assert all(MU[j]<NU[j] for j in (1,2,3,5))
print('BASE: 30 edges positive; all 21 exact Blackwell identities; four strict marginal deficits')

# Four source-column martingale defects and global total mass.
QMAT=tuple(tuple((R[i]-R[j]) if j==k else Q(0) for i,j in D) for k in (1,2,3,5))+(tuple(Q(1) for _ in D),)
rr,piv=rref(QMAT)
assert len(piv)==5
free=[k for k in range(len(D)) if k not in piv]
null=[]
for f in free:
 v=[Q(0)]*len(D);v[f]=Q(1)
 for i,p in enumerate(piv):v[p]=-rr[i][f]
 assert mv(QMAT,v)==(Q(0),)*5
 null.append(tuple(v))
# Deterministically extract ten independent normalized statistical tangent images.
select=[];images=[];nrank=0
for v in null:
 image=mv(A,v)
 newrank=rank(list(zip(*(images+[image]))))
 if newrank>nrank:
  select.append(v);images.append(image);nrank=newrank
 if nrank==10:break
assert len(select)==10 and rank(list(zip(*images)))==10
print('TANGENTS: 10 independent exact mass-normalized conditional-martingale directions')

ZMAX=max(abs(x) for v in select for x in v)
ALPHA=min(E0.values())/(100*(1+ZMAX))
assert 10*ALPHA*ZMAX<min(E0.values())/2
base_deficit=min(NU[j]-MU[j] for j in (1,2,3,5))
assert 600*ALPHA*ZMAX<base_deficit

# Fifteen independent rows; after multiplying moment rows by 20, integral with |a|<=38.
I=(0,1,2,3,4,5,7,9,10,12,15,16,17,19,20)
assert rank([[COL[e][i] for e in D] for i in I])==15
row_scale=tuple(20 if i>=14 else 1 for i in I)
AI=tuple(tuple(int(COL[e][i]*scale) for e in D) for i,scale in zip(I,row_scale))
assert max(abs(c) for row in AI for c in row)<=38
WW=[tuple(sum((E0[e]*COL[e][i] for e in D),Q(0))*scale for i,scale in zip(I,row_scale))]
for v in select:
 WW.append(tuple(ALPHA*sum((v[k]*COL[e][i] for k,e in enumerate(D)),Q(0))*scale for i,scale in zip(I,row_scale)))
DEN=1
for w in WW:
 for t in w:DEN=lcm(DEN,t.denominator)
INT_W=tuple(tuple(int(t*DEN) for t in w) for w in WW)
T=max(abs(z) for w in INT_W for z in w)
BOUND=15*factorial(14)*(38**14)*T
N=BOUND+1
assert N>BOUND and N>1
print('INTEGER_BOUND: coeff_abs <=',BOUND,'digit_separation_denominator N=BOUND+1')
print('COMMON_DENOMINATOR_DIGITS:',len(str(DEN)),'N_DIGITS:',len(str(N)))

# Explicit rational witness E(1/N): 30 positive, normalized, martingale-compatible.
t=Q(1,N)
E={e:E0[e]+ALPHA*sum((t**(k+1)*select[k][ii] for k in range(10)),Q(0)) for ii,e in enumerate(D)}
assert len(E)==30 and min(E.values())>0 and sum(E.values())==1
mu=tuple(sum((E[(i,j)] for j in (0,1,2,3,5,6) if (i,j) in E),Q(0)) for i in range(7))
nu=tuple(sum((E[(i,j)] for i in range(7) if (i,j) in E),Q(0)) for j in range(7))
assert all(mu[j]<nu[j] for j in (1,2,3,5)) and nu[4]==0
assert all(sum(((R[i]-R[j])*E.get((i,j),Q(0)) for i in range(7)),Q(0))==0 for j in range(7))
assert sum(mu)==sum(nu)==1
assert rank(A)==15
# Universal certificate: each <=14-edge feasible S has rank(H_S)=4 (all four
# deficit columns must be non-diagonal); the mass row adds a fifth condition.
# Thus its normalized marginal tangent image has dimension <=|S|-5<=9.
# Every 14-independent-column extension S' misses one of the 10 tangent images.
# A 15x14 integral column matrix has a cofactor annihilator n with |n_i|<=14!38^14.
# Its integer polynomial n . [DEN*AI*E(t)] is nonzero and has |coeff|<=BOUND.
# At t=1/(BOUND+1), no nonzero integer polynomial with coefficients of modulus
# at most BOUND can vanish (take the highest nonzero coefficient modulo N).
# Therefore no <=14-edge solution exists. Rank(A)=15 gives a <=15-edge vertex.
print('PASS_RATIONAL_15_EDGE_NECESSITY_CERTIFICATE')
print('ALL_30_STRICTLY_POSITIVE_STATISTICAL_WITNESS')
print('NORMALIZED_MARGINAL_DIM 10; ADMISSIBLE_COUPLING_VERTEX_BOUND 15')
print('SCOPE: FULL STATISTICAL FACE; NOT A PHYSICALLY LAWFUL G_EQ_B_WITNESS')
