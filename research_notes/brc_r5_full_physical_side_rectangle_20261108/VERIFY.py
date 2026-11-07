#!/usr/bin/env python3
"""Exact rational 7-key certificates for the complete legal two-side-flow R5 rectangle."""
from fractions import Fraction as F
from itertools import product
Z,O=F(0),F(1)
r=tuple(map(F,('1/10','1/2','3/4','1','5/4','3/2','19/10')))
U,W=F(53,160),F(33,160)
E=(
 ((0,0,'67/1440'),(0,1,'9/868'),(0,3,'361/128340'),(0,4,'70111/8983800'),(1,1,'1571/4960'),(3,3,'1981/18600'),(4,3,'361/35650'),(4,4,'661903/3208500'),(4,5,'1171/34875'),(5,1,'9/2170'),(5,4,'70111/1953000'),(5,5,'169283/1116000'),(6,5,'1171/55800'),(6,6,'67/1440')),
 ((0,0,'33677/144000'),(0,3,'54439/5580000'),(1,3,'159443/40300000'),(1,5,'20833/10075000'),(2,4,'627/124000'),(3,3,'147469781/725400000'),(3,5,'635563/90675000'),(4,3,'17343/403000'),(4,4,'388579/1612000'),(5,5,'11361/62000'),(6,4,'627/161200'),(6,5,'1010557/72540000'),(6,6,'7177/144000')),
 ((0,0,'6997/144000'),(0,1,'2547/173600'),(0,3,'11216/1220625'),(1,1,'1204/3875'),(2,3,'1173/124000'),(3,3,'56948923/390600000'),(3,4,'2133289/48825000'),(4,3,'923099/21700000'),(4,4,'509647/2712500'),(5,1,'2547/434000'),(5,4,'2277/868000'),(6,4,'88141/5580000'),(6,6,'23497/144000')),
 ((0,0,'16987/72000'),(0,3,'3787/320850'),(0,4,'664/802125'),(2,4,'9/620'),(3,3,'327311/1116000'),(4,3,'3787/89125'),(4,4,'19788/89125'),(6,4,'881/69750'),(6,6,'11987/72000')))
def matrix(edges):
 q=[[Z]*7 for _ in range(7)]
 for i,j,v in edges:
  assert q[i][j]==Z
  q[i][j]=F(v)
 return tuple(map(tuple,q))
C=tuple(matrix(e) for e in E)
YC=(
 tuple(map(F,('89/93','89/93','85/186','0','1477/7440','0','89/930'))),
 tuple(map(F,('183601/186000','4543/4650','974/2325','1571/4960','4463/23250','0','4543/46500'))),
 tuple(map(F,('177799/186000','4357/4650','1151/2325','0','19073/93000','951/4960','4357/46500'))),
 tuple(map(F,('917/930','89/93','85/186','1571/4960','1477/7440','951/4960','89/930'))))
def X(u,w):return (O,O,F(1,2),u,F(9,80),w,Z)
def legal(q):
 g,a,b,u,v,w,s=q
 return 0<=a<=g<=1 and 0<=b<=g and 0<=u<=F(13,40)*a+b/80 and 0<=w<=F(3,40)*a+F(21,80)*b and 0<=s<=a/10 and 0<=v-s<=F(9,40)*b
def masses(q):
 g,a,b,u,v,w,s=q
 c0=F(13,40)*a+b/80;c1=a/10+F(9,40)*b;c2=F(3,40)*a+F(21,80)*b
 return (F(509,900)*u+F(47,180)*s+F(67,162)*(v-s)+w/100,c0-u,(g-a)/2,1-g+c1-v+F(191,450)*(u+w)+F(43,90)*s+F(14,81)*(v-s),(g-b)/2,c2-w,u/100+F(47,180)*s+F(67,162)*(v-s)+F(509,900)*w)
def times(q):
 g,a,b,u,v,w,s=q
 return (O+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,O+g+(a+b)/2+u+v+w)
def residual(q):
 g,a,b,u,v,w,s=q
 return 9*b*s-4*a*(v-s)
def cert(Q,x,y):
 mx,my=masses(x),masses(y)
 assert sum(mx)==sum(my)==O
 assert sum(r[i]*mx[i] for i in range(7))==sum(r[i]*my[i] for i in range(7))==O
 assert all(v>=0 for row in Q for v in row)
 for i in range(7):assert sum(Q[i])==my[i],('row',i)
 for j in range(7):
  assert sum(Q[i][j] for i in range(7))==mx[j],('Qcol',j)
  assert sum(r[i]*Q[i][j] for i in range(7))==r[j]*mx[j],('Pcol',j)
for (u,w),y,Q in zip(((Z,Z),(U,Z),(Z,W),(U,W)),YC,C):
 x=X(u,w)
 assert legal(x) and legal(y) and times(x)==times(y)
 assert residual(x)==-F(9,20) and residual(y)==Z
 assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
 cert(Q,x,y)
print('PASS_EXACT_FULL_CAPACITY_FOUR_CORNER_BLACKWELL',tuple(map(len,E)))
count=0
for p,q,t in product((Z,F(1,4),F(1,2),F(3,4),O),repeat=3):
 u,w=U*p,W*q; h=((1-p)*(1-q),p*(1-q),(1-p)*q,p*q)
 x=X(u,w)
 y=tuple(sum(h[c]*YC[c][i] for c in range(4)) for i in range(7))
 Q=tuple(tuple(sum(h[c]*C[c][i][j] for c in range(4)) for j in range(7)) for i in range(7))
 assert legal(x) and legal(y) and times(x)==times(y)
 assert residual(x)==-F(9,20) and residual(y)==Z
 assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
 cert(Q,x,y)
 xt=tuple((1-t)*x[i]+t*y[i] for i in range(7))
 my=masses(y)
 Qt=tuple(tuple((1-t)*Q[i][j]+(t*my[i] if i==j else Z) for j in range(7)) for i in range(7))
 assert legal(xt) and times(xt)==times(y)
 cert(Qt,xt,y)
 for d in ((Z,)*7,(O,)*7,tuple(F(j,7) for j in range(7))):
  k=tuple(sum(Qt[i][j]*d[j] for j in range(7))/my[i] if my[i]>0 else Z for i in range(7))
  assert all(Z<=a<=O for a in k)
  assert sum(my[i]*k[i] for i in range(7))==sum(masses(xt)[j]*d[j] for j in range(7))
  assert sum(r[i]*my[i]*k[i] for i in range(7))==sum(r[j]*masses(xt)[j]*d[j] for j in range(7))
 count+=1
print('PASS_125_RATIONAL_P_Q_T_TRIPLES',count)
print('FULL_SOURCE_SIDE_CAPS',str(U),str(W))
print('TARGET_CORNER_FULL_U',','.join(map(str,YC[1])))
print('TARGET_CORNER_FULL_W',','.join(map(str,YC[2])))
print('TARGET_CORNER_FULL_UW',','.join(map(str,YC[3])))
print('PASS_ALL_REAL_FULL_PHYSICAL_SIDE_RECTANGLE_BLACKWELL_LIFT')
