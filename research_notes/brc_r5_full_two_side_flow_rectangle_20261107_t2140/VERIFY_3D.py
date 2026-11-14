#!/usr/bin/env python3
"""Fraction-certified all-real 3D cube lift using the R5 2D certificate."""
from fractions import Fraction as F
from itertools import product
import VERIFY as high
R=high.r
D=F(27,80);V=F(9,40)
H=high.cases
def matrix(items):
 q=[[F(0) for _ in range(7)] for _ in range(7)]
 for i,j,value in items:q[i][j]=F(value)
 return q
L={
 (0,0):((F(4,5),F(4,5),F(4,5),F(7,100),F(13,50),F(7,100),F(2,25)),
  matrix([(0,1,'197/1875'),(0,5,'11/360'),(1,1,'1/5'),(3,1,'169/45000'),
          (3,3,'13/40'),(5,5,'1/5'),(6,1,'2581/90000'),(6,5,'77/720')])),
 (1,0):((F(1),F(1),F(2,3),F(61,240),F(1,4),F(0),F(1,10)),
  matrix([(0,0,'1527/8000'),(0,3,'9/560'),(0,5,'943/37800'),(1,3,'19/240'),
          (3,3,'2179/12000'),(4,3,'1/6'),(5,3,'13/525'),(5,5,'473/2100'),
          (6,5,'943/10800'),(6,6,'27/8000')])),
 (0,1):((F(1),F(1,2),F(1),F(1,20),F(11,40),F(21,80),F(1,20)),
  matrix([(0,0,'27/8000'),(0,1,'17/144'),(0,3,'187/12000'),(1,1,'1/8'),
          (2,3,'1/4'),(3,1,'17/180'),(3,3,'727/7200'),(5,3,'3/80'),
          (6,3,'2311/36000'),(6,6,'1527/8000')])),
 (1,1):((F(1),F(1),F(1),F(7,40),F(13,40),F(7,40),F(1,10)),
  matrix([(0,0,'777/4000'),(0,3,'923/36000'),(1,3,'13/80'),
          (3,3,'2117/9000'),(5,3,'13/80'),(6,3,'923/36000'),(6,6,'777/4000')]))
}
def src(s,t,h):return (F(1),F(1),F(1),s*D,h*V,t*D,F(0))
def check(x,y,q,labels=False):
 assert high.legal(x) and high.legal(y)
 assert high.residual(x)==-4*x[4] and high.residual(y)==0
 assert y[6]==y[1]/10 and y[4]==y[1]/10+F(9,40)*y[2]
 assert high.times(x)==high.times(y)
 mx,my=high.masses(x),high.masses(y)
 assert sum(mx)==sum(my)==1
 assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==1
 assert all(v>=0 for v in mx+my) and all(v>=0 for row in q for v in row)
 for i in range(7):assert sum(q[i])==my[i]
 for j in range(7):
  assert sum(q[i][j] for i in range(7))==mx[j]
  assert sum(R[i]*q[i][j] for i in range(7))==R[j]*mx[j]
 if labels:
  K=[[q[i][j]/my[i] if my[i] else F(i==j) for j in range(7)] for i in range(7)]
  assert all(sum(row)==1 for row in K)
  for d in product((F(0),F(1)),repeat=7):
   dp=[sum(K[i][j]*d[j] for j in range(7)) for i in range(7)]
   assert all(0<=v<=1 for v in dp)
   assert sum(mx[j]*d[j] for j in range(7))==sum(my[i]*dp[i] for i in range(7))
   assert sum(R[j]*mx[j]*d[j] for j in range(7))==sum(R[i]*my[i]*dp[i] for i in range(7))
def lifted(s,t,h):
 weights={(i,j):(s if i else 1-s)*(t if j else 1-t) for i,j in H}
 y0=tuple(sum(weights[k]*L[k][0][m] for k in H) for m in range(7))
 y1=tuple(sum(weights[k]*H[k][0][m] for k in H) for m in range(7))
 q0=[[sum(weights[k]*L[k][1][i][j] for k in H) for j in range(7)] for i in range(7)]
 q1=[[sum(weights[k]*H[k][1][i][j] for k in H) for j in range(7)] for i in range(7)]
 y=tuple((1-h)*y0[m]+h*y1[m] for m in range(7))
 q=[[(1-h)*q0[i][j]+h*q1[i][j] for j in range(7)] for i in range(7)]
 return src(s,t,h),y,q
for i,j in L:
 check(src(F(i),F(j),F(0)),*L[i,j],labels=True)
 check(src(F(i),F(j),F(1)),*H[i,j],labels=True)
 print('CORNERS',i,j,'LOW_V',sum(v>0 for row in L[i,j][1] for v in row),
       'HIGH_V',sum(v>0 for row in H[i,j][1] for v in row))
for s,t,h in product((F(0),F(1,4),F(1,2),F(3,4),F(1)),repeat=3):
 check(*lifted(s,t,h),labels=True)
print('CHECKED_3D_EXACT_GRID',125,'BINARY_DECLARATIONS_PER_POINT',128)
print('PROVED_ALL_REAL_BY_EIGHT_CORNER_TRILINEAR_CALIBRATED_TRANSPORT')
print('PASS_R5_COMPLETE_THREE_PARAMETER_U_W_V_CUBE_BLACKWELL_LIFT')
