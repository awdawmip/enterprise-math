#!/usr/bin/env python3
"""Independent exact-rational R5 physical marginal affine-hull certificate.
Based on PR #1894 frozen 7-LR mass and physical time formulas.
Requires only Python standard library. No numerical LP or float.
"""
from fractions import Fraction as F

def q(s): return tuple(map(F,s.split()))
R=q('1/10 1/2 3/4 1 5/4 3/2 19/10')
Z=F(0)

def mass(v):
 g,a,b,u,vv,w,z=v
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(vv-z)+w/100,
  F(13,40)*a+b/80-u,(g-a)/2,
  1-g+a/10+F(9,40)*b-vv+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(vv-z),
  (g-b)/2,F(3,40)*a+F(21,80)*b-w,
  u/100+F(47,180)*z+F(67,162)*(vv-z)+F(509,900)*w)

def times(v):
 g,a,b,u,vv,w,z=v
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+vv+F(3,2)*w,
         1+g+(a+b)/2+u+vv+w)

def slacks(v):
 g,a,b,u,vv,w,z=v
 return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
         w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,vv-z,z+F(9,40)*b-vv)

def restrictions(p):
 x,y=p[:7],p[7:]
 return (x[0]-x[2],y[0]-1,y[6]-y[1]/10,
         *(a-b for a,b in zip(times(x),times(y))))

def observe(p):return mass(p[7:])+mass(p[:7])

def jac(fun):
 o=(Z,)*14; f0=fun(o)
 return [[fun(tuple(F(i==j) for i in range(14)))[k]-f0[k]
          for j in range(14)] for k in range(len(f0))]

def rref(a):
 m=[[F(x) for x in row] for row in a]
 piv=[];h=len(m);w=len(m[0]);i=0
 for j in range(w):
  z=next((k for k in range(i,h) if m[k][j]),None)
  if z is None:continue
  m[i],m[z]=m[z],m[i];aij=m[i][j];m[i]=[v/aij for v in m[i]]
  for k in range(h):
   if k!=i and m[k][j]:
    t=m[k][j];m[k]=[x-t*y for x,y in zip(m[k],m[i])]
  piv.append(j);i+=1
  if i==h:break
 return m,piv

def rank(a):return len(rref(a)[1])

def determinant(a):
 n=len(a);assert all(len(row)==n for row in a)
 m=[[F(x) for x in row] for row in a];d=F(1)
 for j in range(n):
  i=next((k for k in range(j,n) if m[k][j]),None)
  if i is None:return Z
  if i!=j:m[i],m[j]=m[j],m[i];d=-d
  w=m[j][j];d*=w
  for k in range(j+1,n):
   if m[k][j]:
    t=m[k][j]/w
    for z in range(j,n):m[k][z]-=t*m[j][z]
 return d

def basis_null(a):
 red,piv=rref(a);free=[j for j in range(len(a[0])) if j not in piv]
 return [tuple(-red[piv.index(k)][j] if k in piv else F(k==j)
               for k in range(len(a[0]))) for j in free]

Jc=jac(restrictions);Jm=jac(observe)
assert rank(Jc)==5
N=basis_null(Jc)
assert len(N)==9
B=[[sum(Jm[i][k]*v[k] for k in range(14)) for v in N] for i in range(14)]
assert rank(B)==8
rows=(0,1,2,3,4,7,8,9)
cols=(0,1,2,4,5,6,7,8)
d=determinant([[B[i][j] for j in cols] for i in rows])
assert d==F(-19799371,47239200)

# Two exact affine laws additional to normalization, LR conservation, nu_4=0.
def extra_a(m):return 36*m[0]+28*m[1]+23*m[2]+18*m[3]+13*m[4]+8*m[5]
def extra_b(m):return (-36*m[0]-36*m[1]-31*m[2]-18*m[3]-5*m[4]
                        +36*m[7]+36*m[8]+31*m[9]+18*m[10])
Jextra=[[extra_a(tuple(Jm[i][k] for i in range(14))) for k in range(14)],
        [extra_b(tuple(Jm[i][k] for i in range(14))) for k in range(14)]]
for v in N:
 assert all(sum(row[k]*v[k] for k in range(14))==0 for row in Jextra)
I=[[F(j<7) for j in range(14)], [F(j>=7) for j in range(14)],
   [R[j] if j<7 else -R[j-7] for j in range(14)],
   [F(j==11) for j in range(14)]]
Eraw=[[F(z) for z in (36,28,23,18,13,8,0,0,0,0,0,0,0,0)],
      [F(z) for z in (-36,-36,-31,-18,-5,0,0,36,36,31,18,0,0,0)]]
assert rank(I)==4 and rank(I+Eraw)==6

# A nonzero physical change invisible to both source and target margins.
gauge=tuple(map(F,(-98800,-98800,-98800,-33345,264290,-33345,591026,
                   0,0,0,0,0,0,0)))
assert all(sum(row[k]*gauge[k] for k in range(14))==0 for row in Jc+Jm)
assert len(basis_null(B))==1

# Source input at frozen PR #1894 exact rational witness.
X0=q('999/1000 1/6 999/1000 1/20 29/240 11/160 1/120')
Y0=q('1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200')
H=F(17774559,17507527960)
X=X0[:6]+(X0[6]+H/2,)
DY=q('0 1 0 -1/4 -1/4 0 1/10')
Y=tuple(y+F(1,100000)*t for y,t in zip(Y0,DY))
p=X+Y;m=observe(p);mu=m[:7];nu=m[7:]
assert restrictions(p)==(Z,)*5 and all(a==0 for a in (slacks(X)[4],slacks(Y)[2],slacks(Y)[10]))
assert all(s>0 for k,s in enumerate(slacks(X)) if k!=4)
assert all(s>0 for k,s in enumerate(slacks(Y)) if k not in (2,10))
assert extra_a(m)==18 and extra_b(m)==0
assert nu[4]==0 and all(nu[j]>mu[j] for j in (1,2,3,5))
assert sum(mu)==sum(nu)==1 and sum(R[i]*(mu[i]-nu[i]) for i in range(7))==0
# Reconstruct PR #1894 strictly positive 30-edge rational Blackwell coupling.
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)
SB=((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),(0,3),(1,3),(3,3),(4,3),(5,3),(4,5),(5,5),(6,5),(6,6))
PIV=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
def edge_col(edge):
 i,j=edge;col=[Z]*21;col[i]=1;col[7+j]=1;col[14+j]=R[i];return col
C={e:edge_col(e) for e in D};rhs=mu+nu+tuple(R[j]*nu[j] for j in range(7))
tau=F(1,10**7); residual=[rhs[i]-tau*sum(C[e][i] for e in D) for i in range(21)]
mat=[[C[e][i] for e in SB] for i in PIV]
assert determinant(mat)==F(-299,1600)
aug=[row+[residual[i]] for row,i in zip(mat,PIV)]
red,piv=rref(aug)
assert piv==list(range(15))
weights=[row[-1] for row in red]
E={e:tau for e in D}
for edge,val in zip(SB,weights):E[edge]+=val
assert min(E.values())==tau
assert all(sum(E[e]*C[e][i] for e in D)==rhs[i] for i in range(21))
# Positivity+right inverse to A imply a relative 8D open feasible marginal region.
print('PASS_AFFINE_CONSTRAINT_RANK',rank(Jc),'RAW_PARAMETERS',14,'FREE_PARAMETERS',len(N))
print('PASS_PHYSICAL_MARGINAL_AFFINE_DIM',rank(B),'EXACT_8_MINOR',d)
print('PASS_TWO_EXTRA_AFFINE_INVARIANTS',18,0,'RELATIONS_RANK',rank(I+Eraw))
print('PASS_NONZERO_PHYSICAL_OBSERVER_KERNEL',gauge[:7],'KERNEL_DIM',len(basis_null(B)))
print('PASS_PHYSICAL_INTERIOR', 'min_transport',min(E.values()), 'strict_deficits',tuple(nu[j]-mu[j] for j in (1,2,3,5)))
print('THEOREM_8D_PHYSICAL_FEASIBLE_CHAMBER_AND_GENERIC_MIN_SUPPORT_AT_LEAST_13')
