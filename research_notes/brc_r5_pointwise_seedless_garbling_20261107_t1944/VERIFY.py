#!/usr/bin/env python3
from fractions import Fraction as F
R=list(map(F,['1/10','1/2','3/4','1','5/4','3/2','19/10']))
def m(x):
 g,a,b,u,v,w,z=x
 return [F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
  F(13,40)*a+b/80-u,(g-a)/2,
  1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
  (g-b)/2,F(3,40)*a+F(21,80)*b-w,
  u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w]
def t(x):
 g,a,b,u,v,w,z=x
 return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,1+g+(a+b)/2+u+v+w
def check(x,y,J):
 g,a,b,u,v,w,z=y
 assert 0<=a<=g<=1 and 0<=b<=g and 0<=u<=F(13,40)*a+b/80
 assert 0<=w<=F(3,40)*a+F(21,80)*b and 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
 assert 9*b*z==4*a*(v-z) and t(x)==t(y)
 X,Y=m(x),m(y)
 assert all(q>=0 for q in X+Y) and sum(X)==sum(Y)==1
 assert sum(r*q for r,q in zip(R,X))==sum(r*q for r,q in zip(R,Y))==1
 assert all(q>=0 for row in J for q in row)
 for i in range(7): assert sum(J[i])==Y[i]
 for j in range(7):
  assert sum(J[i][j] for i in range(7))==X[j]
  assert sum(R[i]*J[i][j] for i in range(7))==R[j]*X[j]
 for k in range(3):
  d=[F((13*j+7*k+1)%37,37) for j in range(7)]
  dd=[sum(J[i][j]*d[j] for j in range(7))/Y[i] if Y[i] else F(0) for i in range(7)]
  assert all(0<=q<=1 for q in dd)
  assert sum(X[i]*d[i] for i in range(7))==sum(Y[i]*dd[i] for i in range(7))
  assert sum(R[i]*X[i]*d[i] for i in range(7))==sum(R[i]*Y[i]*dd[i] for i in range(7))
def lift(x):
 g,a,b,u,v,w,z=x; rad=9*b*z-4*a*(v-z)
 if rad>=0:
  c=a/10+F(9,40)*b;zs=a*v/(10*c) if c else F(0)
  y=(g,a,b,u,v,w,zs);d=F(247,1620)*(z-zs)
  J=[[F(0)]*7 for _ in range(7)]
  for i in range(7):J[i][i]=m(y)[i]
  for i in [0,6]:J[i][i]-=d;J[i][3]+=d
 else:
  assert (g,a,b,u,w)==(1,1,1,0,0)
  D=4*v-13*z;h=D/20;y=(F(1),1-h,1-h,F(0),v+h,F(0),F(4,13)*(v+h))
  A=F(107,16200);C=F(27,1600);B=F(1,40);E=F(1909,64800)
  assert [r-l for l,r in zip(m(x),m(y))]==[A*D,-C*D,B*D,-E*D,B*D,-C*D,A*D]
  al=F(5,13)*C;be=F(8,13)*C;ga=A-al;et=B-be
  assert min(al,be,ga,et)>=0 and al+be==C and 2*(ga+et)==E
  J=[[F(0)]*7 for _ in range(7)]
  for i in [0,6]:J[i][i]=m(x)[i]
  for i in [1,3,5]:J[i][i]=m(y)[i]
  J[0][1]=J[6][5]=al*D;J[0][3]=J[6][3]=ga*D
  J[2][1]=J[4][5]=be*D;J[2][3]=J[4][3]=et*D
 check(x,y,J)
 return y
# Affine identity holds for all v,z since it holds at a basis of Q^2.
for v,z in [(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]:
 x=(F(1),F(1),F(1),F(0),v,F(0),z);D=4*v-13*z;h=D/20
 y=(F(1),1-h,1-h,F(0),v+h,F(0),F(4,13)*(v+h))
 assert [r-l for l,r in zip(m(x),m(y))]==[F(107,16200)*D,-F(27,1600)*D,D/40,-F(1909,64800)*D,D/40,-F(27,1600)*D,F(107,16200)*D]
 assert t(x)==t(y)
print('PASS_AFFINE_COEFFICIENT_IDENTITIES')
counts=[0,0]
for g in [F(0),F(1,2),F(1)]:
 for aa in [F(0),F(1,2),F(1)]:
  for bb in [F(0),F(1,2),F(1)]:
   a=g*aa;b=g*bb
   for A in [F(0),F(1,2),F(1)]:
    for B in [F(0),F(1,2),F(1)]:
     u=(F(13,40)*a+b/80)*A;w=(F(3,40)*a+F(21,80)*b)*B
     for p in [F(0),F(1,2),F(1)]:
      for q in [F(0),F(1,2),F(1)]:
       z=p*a/10;v=z+q*F(9,40)*b
       if 9*b*z>=4*a*(v-z):lift((g,a,b,u,v,w,z));counts[0]+=1
for z in [F(0),F(1,100),F(1,20),F(1,10)]:
 for vadd in [F(0),F(1,50),F(9,80),F(9,40)]:
  x=(F(1),F(1),F(1),F(0),z+vadd,F(0),z)
  lift(x);counts[1]+=1
print('PASS_EXACT_TRANSPORT_AND_DECLARATION_CHECKS',counts)
print('WITNESS_POS',lift((F(1),F(1),F(1),F(0),F(1,10),F(0),F(1,10))))
print('WITNESS_NEG',lift((F(1),F(1),F(1),F(0),F(9,40),F(0),F(0))))
print('PASS_R5_EXPLICIT_SEEDLESS_NONCONVEX_LIFT')
