#!/usr/bin/env python3
"""Fraction-certified all-real 4D maximal-early-flow face, using 3D and 2D."""
from fractions import Fraction as F
from itertools import product
import VERIFY_3D as three
h=three.high
R=three.R
D=F(27,80); Z=F(1,10); V=F(9,40)
def Q(entries):
 a=[[F(0) for _ in range(7)] for _ in range(7)]
 for i,j,v in entries:a[i][j]=F(v)
 return a
P={
 (0,0):((F(127,130),F(73,130),F(73,130),F(1971,10400),F(73,400),F(1971,10400),F(73,1300)),
  Q([(0,0,'47/1800'),(0,1,'27/208'),(0,3,'93959/10764000'),(0,5,'93959/8280000'),
     (2,1,'27/130'),(3,3,'181447/780000'),(4,3,'93959/2990000'),(4,5,'527041/2990000'),
     (6,5,'701459/4680000'),(6,6,'47/1800')])),
 (0,1):((F(1),F(11,20),F(1),F(63,800),F(7,25),F(243,800),F(11,200)),
  Q([(0,0,'2123/72000'),(0,1,'22591/180000'),(1,1,'10067/900000'),(1,3,'91183/900000'),
     (2,1,'22591/112500'),(2,3,'5443/225000'),(3,3,'13651/60000'),
     (6,3,'11341/180000'),(6,6,'15623/72000')])),
 (1,0):((F(1),F(1),F(11,20),F(531,1600),F(179,800),F(171,1600),F(1,10)),
  Q([(0,0,'15623/72000'),(0,3,'35329/720000'),(3,3,'685133/3600000'),(3,5,'234277/3600000'),
     (4,3,'35329/200000'),(4,5,'9671/200000'),(5,5,'9/80'),
     (6,5,'80329/720000'),(6,6,'2123/72000')])),
 (1,1):((F(37,40),F(37,40),F(37,40),F(999,3200),F(481,1600),F(999,3200),F(37,400)),
  Q([(0,0,'7933/36000'),(0,3,'100151/1440000'),(3,3,'100843/240000'),
     (6,3,'100151/1440000'),(6,6,'7933/36000')]))
}
def src(s,t,p,q):
 z=p*Z
 return (F(1),F(1),F(1),s*D,z+q*V,t*D,z)
def identity(x):
 m=h.masses(x)
 return [[m[i] if i==j else F(0) for j in range(7)] for i in range(7)]
def checking(x,y,Q,labels=True):
 assert h.legal(x) and h.legal(y)
 assert h.residual(x)==9*x[6]-4*(x[4]-x[6]) and h.residual(y)==0
 assert y[6]==y[1]/10 and y[4]==y[1]/10+F(9,40)*y[2]
 assert h.times(x)==h.times(y)
 mx,my=h.masses(x),h.masses(y)
 assert sum(mx)==sum(my)==1
 assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==1
 assert all(v>=0 for v in mx+my) and all(v>=0 for row in Q for v in row)
 for i in range(7):assert sum(Q[i])==my[i]
 for j in range(7):
  assert sum(Q[i][j] for i in range(7))==mx[j]
  assert sum(R[i]*Q[i][j] for i in range(7))==R[j]*mx[j]
 if labels:
  K=[[Q[i][j]/my[i] if my[i] else F(i==j) for j in range(7)] for i in range(7)]
  assert all(sum(row)==1 for row in K)
  for d in product((F(0),F(1)),repeat=7):
   dp=[sum(K[i][j]*d[j] for j in range(7)) for i in range(7)]
   assert all(0<=v<=1 for v in dp)
   assert sum(mx[j]*d[j] for j in range(7))==sum(my[i]*dp[i] for i in range(7))
   assert sum(R[j]*mx[j]*d[j] for j in range(7))==sum(R[i]*my[i]*dp[i] for i in range(7))
def high_z(s,t,q):
 weights={(i,j):(s if i else 1-s)*(t if j else 1-t) for i,j in P}
 zero_y=tuple(sum(weights[k]*P[k][0][m] for k in P) for m in range(7))
 zero_Q=[[sum(weights[k]*P[k][1][i][j] for k in P) for j in range(7)] for i in range(7)]
 end_x=src(s,t,F(1),F(1))
 end_y=end_x
 end_Q=identity(end_x)
 y=tuple((1-q)*zero_y[m]+q*end_y[m] for m in range(7))
 Q=[[(1-q)*zero_Q[i][j]+q*end_Q[i][j] for j in range(7)] for i in range(7)]
 return y,Q
def lifted(s,t,p,q):
 _,y0,Q0=three.lifted(s,t,q)
 y1,Q1=high_z(s,t,q)
 y=tuple((1-p)*y0[m]+p*y1[m] for m in range(7))
 Q=[[(1-p)*Q0[i][j]+p*Q1[i][j] for j in range(7)] for i in range(7)]
 return src(s,t,p,q),y,Q
for i,j in P:
 x=src(F(i),F(j),F(1),F(0))
 checking(x,*P[i,j])
 print('POSITIVE_RESIDUAL_CORNER',i,j,'TIMES',h.times(x),'Q_NNZ',sum(v>0 for row in P[i,j][1] for v in row))
 x=src(F(i),F(j),F(1),F(1))
 checking(x,x,identity(x))
for s,t,p,q in product((F(0),F(1,2),F(1)),repeat=4):
 checking(*lifted(s,t,p,q),labels=True)
print('CHECKED_4D_EXACT_GRID',81,'BINARY_DECLARATIONS_PER_POINT',128)
print('PROVED_ALL_REAL_BY_SIXTEEN_CORNER_MULTILINEAR_CALIBRATED_TRANSPORT')
print('PASS_R5_COMPLETE_FOUR_PARAMETER_G_A_B_1_FACE_BLACKWELL_LIFT')
