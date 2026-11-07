#!/usr/bin/env python3
"""Exact Fraction checker of four sparse seven-key R5 Blackwell matrices and their interpolation."""
from fractions import Fraction as F
from itertools import product
z,o=F(0),F(1)
r=tuple(map(F,('1/10','1/2','3/4','1','5/4','3/2','19/10')))
U,W=F(1571,4960),F(951,4960)
# Rows target y, columns source x.
E=(
 ((0,0,'67/1440'),(0,1,'9/868'),(0,3,'361/128340'),(0,4,'70111/8983800'),(1,1,'1571/4960'),(3,3,'1981/18600'),(4,3,'361/35650'),(4,4,'661903/3208500'),(4,5,'1171/34875'),(5,1,'9/2170'),(5,4,'70111/1953000'),(5,5,'169283/1116000'),(6,5,'1171/55800'),(6,6,'67/1440')),
 ((0,0,'1007339/4464000'),(0,1,'1/124'),(0,3,'721/128340'),(0,4,'9373/1283400'),(3,1,'1/155'),(3,3,'508981/2232000'),(3,5,'1/155'),(4,3,'721/35650'),(4,4,'16383/71300'),(5,5,'951/4960'),(6,4,'721/55800'),(6,5,'1/124'),(6,6,'221839/4464000')),
 ((0,0,'216259/4464000'),(0,1,'27/2852'),(0,3,'10643/1283400'),(0,5,'1/310'),(1,1,'1571/4960'),(3,3,'363097/2232000'),(3,4,'7033/279000'),(4,1,'18/3565'),(4,3,'10643/356500'),(4,4,'1667/7750'),(6,4,'541/55800'),(6,5,'7/620'),(6,6,'691759/4464000')),
 ((0,0,'507949/2232000'),(0,1,'7/620'),(0,3,'361/55800'),(0,5,'1/310'),(3,3,'359711/1116000'),(4,4,'1/4'),(6,1,'1/310'),(6,3,'361/55800'),(6,5,'7/620'),(6,6,'352949/2232000')))
def matrix(edges):
 q=[[z]*7 for _ in range(7)]
 for i,j,v in edges:q[i][j]=F(v)
 return tuple(map(tuple,q))
C=tuple(matrix(q) for q in E)
def X(u,w):return (o,o,F(1,2),u,F(9,80),w,z)
def Y(u,w):return (F(89,93),F(89,93),F(85,186),u,F(1477,7440),w,F(89,930))
def legal(q):
 g,a,b,u,v,w,s=q
 return 0<=a<=g<=1 and 0<=b<=g and 0<=u<=F(13,40)*a+b/80 and 0<=w<=F(3,40)*a+F(21,80)*b and 0<=s<=a/10 and 0<=v-s<=F(9,40)*b
def m(q):
 g,a,b,u,v,w,s=q
 c0=F(13,40)*a+b/80;c1=a/10+F(9,40)*b;c2=F(3,40)*a+F(21,80)*b
 return (F(509,900)*u+F(47,180)*s+F(67,162)*(v-s)+w/100,c0-u,(g-a)/2,1-g+c1-v+F(191,450)*(u+w)+F(43,90)*s+F(14,81)*(v-s),(g-b)/2,c2-w,u/100+F(47,180)*s+F(67,162)*(v-s)+F(509,900)*w)
def T(q):
 g,a,b,u,v,w,s=q
 return (o+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,o+g+(a+b)/2+u+v+w)
def R(q):
 g,a,b,u,v,w,s=q
 return 9*b*s-4*a*(v-s)
def verify(q,x,y):
 mx,my=m(x),m(y)
 assert all(v>=0 for row in q for v in row)
 assert sum(mx)==sum(my)==sum(r[i]*mx[i] for i in range(7))==sum(r[i]*my[i] for i in range(7))==o
 for i in range(7):assert sum(q[i])==my[i]
 for j in range(7):
  assert sum(q[i][j] for i in range(7))==mx[j]
  assert sum(r[i]*q[i][j] for i in range(7))==r[j]*mx[j]
corners=((z,z),(U,z),(z,W),(U,W))
for (u,w),q in zip(corners,C):
 x,y=X(u,w),Y(u,w)
 assert legal(x) and legal(y) and T(x)==T(y) and R(x)==-F(9,20) and R(y)==0
 verify(q,x,y)
print('PASS_FOUR_EXACT_CORNER_TRANSPORT_CERTIFICATES',tuple(map(len,E)))
assert U>F(503,1600) and W>F(32383,175840)
assert F(13,40)*F(89,93)+F(85,186)/80==U
assert F(3,40)*F(89,93)+F(21,80)*F(85,186)==W
count=0
for pu,pw,t in product((z,F(1,4),F(1,2),F(3,4),o),repeat=3):
 u,w=U*pu,W*pw
 x,y=X(u,w),Y(u,w)
 h=((1-pu)*(1-pw),pu*(1-pw),(1-pu)*pw,pu*pw)
 q=tuple(tuple(sum(h[c]*C[c][i][j] for c in range(4)) for j in range(7)) for i in range(7))
 assert legal(x) and legal(y) and T(x)==T(y)
 verify(q,x,y)
 xt=tuple((1-t)*x[i]+t*y[i] for i in range(7))
 my=m(y)
 qt=tuple(tuple((1-t)*q[i][j]+(t*my[i] if i==j else z) for j in range(7)) for i in range(7))
 assert legal(xt) and T(xt)==T(y) and R(xt)==-3*(t-1)*(8*t-93)/620
 verify(qt,xt,y)
 for d in ((z,)*7,(o,)*7,tuple(F(j,7) for j in range(7))):
  k=tuple(sum(qt[i][j]*d[j] for j in range(7))/my[i] if my[i] else z for i in range(7))
  assert all(z<=v<=o for v in k)
  assert sum(my[i]*k[i] for i in range(7))==sum(m(xt)[j]*d[j] for j in range(7))
  assert sum(r[i]*my[i]*k[i] for i in range(7))==sum(r[j]*m(xt)[j]*d[j] for j in range(7))
 count+=1
print('PASS_125_EXACT_RATIONAL_REGRESSIONS',count)
print('NEW_SOURCE_LIMITS',U,W)
print('OLD_SOURCE_LIMITS',F(503,1600),F(32383,175840))
print('SEEDLESS_BASE',','.join(map(str,Y(z,z))))
print('PASS_ALL_REAL_EXPANDED_3_PARAM_LOW_SLACK_BLACKWELL_BOX_BY_BILINEAR_INTERPOLATION')
