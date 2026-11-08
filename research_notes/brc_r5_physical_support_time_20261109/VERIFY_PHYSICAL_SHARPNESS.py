#!/usr/bin/env python3
"""Exact physical 14-edge witness and the eight-dimensional observer minor."""
from fractions import Fraction as F
R=tuple(map(F,('1/10','1/2','3/4','1','5/4','3/2','19/10')))
C=tuple(map(F,('2','2','31/18','1','5/18','0','0')))

def mass(x):
 g,a,b,u,v,w,z=x
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
         F(13,40)*a+b/80-u,(g-a)/2,
         1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
         (g-b)/2,F(3,40)*a+F(21,80)*b-w,
         u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def tp(x):
 g,a,b,u,v,w,z=x
 return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w
def tq(x):
 g,a,b,u,v,w,z=x
 return 1+g+(a+b)/2+u+v+w
def hinges(x):
 m=mass(x)
 return tuple(sum(max(F(0),rr-k)*mi for rr,mi in zip(R,m)) for k in R[1:-1])
def target(x,G,A,B):
 P,Q=tp(x),tq(x)
 U=-F(17,40)*A-F(19,80)*B-G/2-P+F(3,2)*Q-F(1,2)
 W=-F(7,40)*A-F(39,80)*B-G/2+P-Q/2-F(1,2)
 return (G,A,B,U,A/10+F(9,40)*B,W,A/10)
def lawful(x):
 g,a,b,u,v,w,z=x
 assert 0<=a<=g<=1 and 0<=b<=g
 assert 0<=u<=F(13,40)*a+b/80
 assert 0<=w<=F(3,40)*a+F(21,80)*b
 assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
 m=mass(x)
 assert all(t>=0 for t in m) and sum(m)==1
 assert sum(rr*mi for rr,mi in zip(R,m))==1

def physical_map(v):
 g,a,u,vx,w,G,A,B=v
 x=(g,a,g,u,vx,w,F(1,120))
 y=target(x,G,A,B)
 return mass(y)[:5]+mass(x)[:3]

def determinant(mat):
 mat=[list(row) for row in mat]
 n=len(mat);out=F(1)
 for j in range(n):
  p=next((i for i in range(j,n) if mat[i][j]),None)
  if p is None:return F(0)
  if p!=j:mat[p],mat[j]=mat[j],mat[p];out=-out
  pivot=mat[j][j];out*=pivot
  for i in range(j+1,n):
   if mat[i][j]:
    c=mat[i][j]/pivot
    for k in range(j+1,n):mat[i][k]-=c*mat[j][k]
    mat[i][j]=F(0)
 return out

zero=(F(0),)*8
base=physical_map(zero)
cols=[]
for j in range(8):
 unit=tuple(F(i==j) for i in range(8))
 cols.append([v-b for v,b in zip(physical_map(unit),base)])
M=[[cols[j][i] for j in range(8)] for i in range(8)]
det=determinant(M)
assert det==F(-1111424393,139968000000)
print('PASS_EXACT_AFFINE_PHYSICAL_OBSERVER_8x8_MINOR',det)

x=tuple(map(F,('999/1000','1/6','999/1000','1/20','29/240','11/160','1/120')))
y=tuple(map(F,('871/1000','9/40','5/6','273/4000','21/100','143/1000','9/400')))
assert y==target(x,F(871,1000),F(9,40),F(5,6))
lawful(x);lawful(y)
assert x[0]==x[2] and x[0]<1
assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])
assert tp(x)==tp(y) and tq(x)==tq(y)
delta=tuple(a-b for a,b in zip(hinges(y),hinges(x)))
assert all(d>0 for d in delta)
assert all(m>0 for i,m in enumerate(mass(x)) if i!=4)
assert all(m>0 for m in mass(y))
assert mass(x)[4]==0 and mass(x)[1]>mass(y)[1]
assert sum(c*m for c,m in zip(C,mass(x)))==sum(c*m for c,m in zip(C,mass(y)))
assert 10*delta[0]+16*delta[1]==16*delta[3]+10*delta[4]
print('PASS_LAWFUL_PHYSICAL_G_EQ_B_STRICT_CHAMBER_SEEDLESS_TARGET')
print('STRICT_INTERIOR_DEFICIT_NODE1',mass(x)[1]-mass(y)[1])
print('FIVE_POSITIVE_HINGE_GAPS',*map(str,delta))
print('PASS_TIME_HINGE_BALANCE_AND_FULL_DIMENSION_WITNESS')

EDGES = [
 (0,0,'33553/432000'), (0,1,'763/720000'),
 (1,1,'367/24000'), (6,1,'109/360000'),
 (0,2,'25909/993600'), (2,2,'323/1000'),
 (3,2,'14339/216000'), (4,2,'13/18400'),
 (3,3,'3298/16875'),
 (0,5,'926327/49680000'), (4,5,'5003/276000'),
 (5,5,'741/8000'), (6,5,'82717/1080000'),
 (6,6,'38053/432000')
]
E = [[F(0) for j in range(7)] for i in range(7)]
for i,j,v in EDGES:
 assert E[i][j]==0 and F(v)>0
 E[i][j]=F(v)
assert len(EDGES)==14
assert all(sum(E[i][j] for j in range(7))==mass(y)[i] for i in range(7))
assert all(sum(E[i][j] for i in range(7))==mass(x)[j] for j in range(7))
assert all(sum(R[i]*E[i][j] for i in range(7))==R[j]*mass(x)[j] for j in range(7))
print('PASS_EXACT_14_EDGE_LAWFUL_PHYSICAL_SEEDLESS_BLACKWELL_COUPLING')
print('MIN_EDGE',min(F(v) for _,_,v in EDGES))
