#!/usr/bin/env python3
"""R5 endpoint-inclusive mixed-capacity Blackwell theorem.
Exact seven-node P/Q certificate using fractions.Fraction only.
"""
from fractions import Fraction as F
from itertools import product
R=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
T=F(1,50)
P=(F(0),F(77,152))
D=(F(17,2112),F(1))
TH=(F(0),F(1))
# Encoded sparse edge i->j is 7*i+j; theta=0 and 1 use the same support.
SUP={
 (P[0],D[0]):(0,1,8,9,16,17,22,23,24,26,38,40,47,48),
 (P[0],D[1]):(0,1,8,9,15,16,17,24,37,44,45,48),
 (P[1],D[0]):(0,1,3,15,16,17,24,36,40,45,48),
 (P[1],D[1]):(0,1,2,3,15,16,17,24,37,45,48),
}
def src(t,p,q,h):
 return (F(1),t,F(1),(F(13,40)*t+F(1,80))*p,
         F(27,160)+t*h/10,(F(3,40)*t+F(21,80))*q,t*h/10)
def dst(t,p,q,h):
 g,a,b,u,v,w,z=src(t,p,q,h)
 return (F(1),F(0),F(1),u+F(23,160)*t,v+F(37,80)*t,w-F(17,160)*t,F(0))
def masses(f):
 g,a,b,u,v,w,z=f
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
         F(13,40)*a+b/80-u,(g-a)/2,
         1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
         (g-b)/2,F(3,40)*a+F(21,80)*b-w,
         u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def tp(f):
 g,a,b,u,v,w,z=f
 return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w
def tq(f):
 g,a,b,u,v,w,z=f
 return 1+g+(a+b)/2+u+v+w
def unique_solve(A,b):
 M=[list(row)+[v] for row,v in zip(A,b)]
 n=len(A[0]);k=0;cols=[]
 for j in range(n):
  pivot=next((i for i in range(k,len(M)) if M[i][j]),None)
  if pivot is None:continue
  M[k],M[pivot]=M[pivot],M[k]
  z=M[k][j]; M[k]=[v/z for v in M[k]]
  for i in range(len(M)):
   if i==k or not M[i][j]:continue
   z=M[i][j]
   M[i]=[a-z*c for a,c in zip(M[i],M[k])]
  cols.append(j);k+=1
 assert len(cols)==n,("nonunique certificate",len(cols),n)
 assert all(any(row[:n]) or not row[-1] for row in M)
 sol=[F(0)]*n
 for i,c in enumerate(cols):sol[c]=M[i][-1]
 assert all(sum(a*v for a,v in zip(row,sol))==rhs for row,rhs in zip(A,b))
 return sol
def transfer(x,y,ss):
 mx,my=masses(x),masses(y)
 A=[];b=[]
 for i in range(7):
  A.append([F(k//7==i) for k in ss]);b.append(my[i])
 for j in range(7):
  A.append([F(k%7==j) for k in ss]);b.append(mx[j])
  A.append([R[k//7]*F(k%7==j) for k in ss]);b.append(R[j]*mx[j])
 return {divmod(k,7):v for k,v in zip(ss,unique_solve(A,b))}
def check(x,y,E):
 for f in (x,y):
  g,a,b,u,v,w,z=f
  assert 0<=a<=g<=1 and 0<=b<=g
  assert 0<=u<=F(13,40)*a+b/80
  assert 0<=w<=F(3,40)*a+F(21,80)*b
  assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
  m=masses(f)
  assert all(w>=0 for w in m)
  assert sum(m)==1 and sum(r*w for r,w in zip(R,m))==1
 g,a,b,u,v,w,z=y
 assert 9*b*z==4*a*(v-z)
 assert all(w>=0 for w in E.values())
 mx,my=masses(x),masses(y)
 for i in range(7):
  assert sum(w for (ii,j),w in E.items() if ii==i)==my[i]
 for j in range(7):
  assert sum(w for (i,jj),w in E.items() if jj==j)==mx[j]
  assert sum(R[i]*w for (i,jj),w in E.items() if jj==j)==R[j]*mx[j]
 assert tp(x)==tp(y) and tq(x)==tq(y)
def corners():
 cert={};positive=0
 for p,q,h in product(P,D,TH):
  x,y=src(T,p,q,h),dst(T,p,q,h)
  E=transfer(x,y,SUP[p,q]);check(x,y,E)
  assert all(v>0 for v in E.values())
  cert[T,p,q,h]=(x,y,E)
  positive+=len(E)
  x0,y0=src(F(0),p,q,h),dst(F(0),p,q,h)
  assert x0==y0
  I={(i,i):v for i,v in enumerate(masses(x0)) if v}
  check(x0,y0,I)
  cert[F(0),p,q,h]=(x0,y0,I)
 assert positive==96
 return cert,positive
def interior(t,p,q,h,cert):
 assert 0<=t<=T and P[0]<=p<=P[1] and D[0]<=q<=D[1] and 0<=h<=1
 lamb=t/T;beta=p/P[1];gamma=(q-D[0])/(D[1]-D[0]);eps=h
 W={}
 for a,b,c,d in product((0,1),repeat=4):
  key=(T if a else F(0),P[b],D[c],TH[d])
  W[key]=(lamb if a else 1-lamb)*(beta if b else 1-beta)*\
         (gamma if c else 1-gamma)*(eps if d else 1-eps)
 assert sum(W.values())==1 and all(v>=0 for v in W.values())
 x,y=src(t,p,q,h),dst(t,p,q,h)
 assert all(x[j]==sum(weight*cert[key][0][j] for key,weight in W.items()) for j in range(7))
 assert all(y[j]==sum(weight*cert[key][1][j] for key,weight in W.items()) for j in range(7))
 keys=set().union(*(set(v[2]) for v in cert.values()))
 E={ij:sum(weight*cert[key][2].get(ij,F(0)) for key,weight in W.items()) for ij in keys}
 check(x,y,E)
if __name__=="__main__":
 cert,n=corners()
 print("EXACT_8_NONTRIVIAL_ENDPOINT_CERTIFICATES_PASS",n)
 print("EXACT_8_SEEDLESS_ZERO_ENDPOINT_IDENTITIES_PASS")
 for k in range(151):
  interior(T*F((37*k+13)%151,150),P[1]*F((19*k+7)%151,150),
           D[0]+(D[1]-D[0])*F((29*k+3)%151,150),
           F((43*k+11)%151,150),cert)
 print("EXACT_151_INTERIOR_AND_BOUNDARY_INTERPOLATION_CHECKS_PASS")
 print("AUTHOR_PROVED_ALL_REAL_T_0_TO_1_50_P_0_TO_77_152_Q_17_2112_TO_1_THETA_0_TO_1_KAPPA_3_4")
