#!/usr/bin/env python3
"""Exact Fraction certificate for the full two-side-flow all-real Blackwell rectangle."""
from fractions import Fraction as F
from itertools import product

r=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
D=F(27,80)
def full(u,w): return (F(1),F(1),F(1),u,F(9,40),w,F(0))
def masses(x):
 g,a,b,u,v,w,z=x
 c0=F(13,40)*a+b/80;c1=a/10+F(9,40)*b;c2=F(3,40)*a+F(21,80)*b
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
         c0-u,(g-a)/2,
         1-g+c1-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
         (g-b)/2,c2-w,
         u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(x):
 g,a,b,u,v,w,z=x
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
         1+g+(a+b)/2+u+v+w)
def legal(x):
 g,a,b,u,v,w,z=x
 return (0<=a<=g<=1 and 0<=b<=g<=1 and
         0<=u<=F(13,40)*a+b/80 and
         0<=w<=F(3,40)*a+F(21,80)*b and
         0<=z<=a/10 and 0<=v-z<=F(9,40)*b)
def residual(x):
 g,a,b,u,v,w,z=x
 return 9*b*z-4*a*(v-z)
def Q(entries):
 m=[[F(0) for _ in range(7)] for _ in range(7)]
 for i,j,v in entries: m[i][j]=F(v)
 return m
cases={
 (0,0):(
  (F(15,16),F(15,16),F(15,16),F(29,1280),F(39,128),F(29,1280),F(3,32)),
  Q([(0,0,'67/720'),(0,1,'1/32'),(0,5,'29/64000'),
     (1,1,'47/160'),(3,3,'5/36'),(3,5,'771/32000'),
     (5,1,'1/80'),(5,5,'9/32'),(6,5,'2029/64000'),(6,6,'67/720')])
 ),
 (1,0):(
  (F(686,705),F(686,705),F(659,705),F(1233,3760),F(347,1128),F(0),F(343,3525)),
  Q([(0,0,'20443/72000'),(0,3,'9977/1184400'),(0,5,'16277/2961000'),
     (3,3,'421271/1692000'),(4,3,'9/470'),
     (5,3,'3677/658000'),(5,5,'102899/329000'),
     (6,5,'16277/846000'),(6,6,'6943/72000')])
 ),
 (0,1):(
  (F(1),F(4,5),F(1),F(7,200),F(61,200),F(129,400),F(2,25)),
  Q([(0,0,'6943/72000'),(0,1,'76/1875'),
     (1,1,'34817/150000'),(1,3,'101/18750'),
     (2,1,'608/9375'),(2,3,'659/18750'),
     (3,3,'4577/20000'),(6,3,'287/22500'),(6,6,'20443/72000')])
 ),
 (1,1):(
  (F(29,30),F(29,30),F(29,30),F(261,800),F(377,1200),F(261,800),F(29,300)),
  Q([(0,0,'10343/36000'),(0,3,'5639/360000'),
     (3,3,'70931/180000'),(6,3,'5639/360000'),(6,6,'10343/36000')])
 ),
}
def check(x,y,q,all_labels=True):
 assert legal(x) and legal(y) and residual(x)==-F(9,10) and residual(y)==0
 assert y[6]==y[1]/10 and y[4]==y[1]/10+F(9,40)*y[2]
 assert times(x)==times(y)
 mx,my=masses(x),masses(y)
 assert sum(mx)==sum(my)==1
 assert sum(r[i]*mx[i] for i in range(7))==sum(r[i]*my[i] for i in range(7))==1
 assert all(v>=0 for v in mx+my) and all(v>=0 for row in q for v in row)
 for i in range(7): assert sum(q[i])==my[i]
 for j in range(7):
  assert sum(q[i][j] for i in range(7))==mx[j]
  assert sum(r[i]*q[i][j] for i in range(7))==r[j]*mx[j]
 if all_labels:
  K=[[q[i][j]/my[i] if my[i] else F(i==j) for j in range(7)] for i in range(7)]
  assert all(sum(row)==1 for row in K)
  for d in product((F(0),F(1)),repeat=7):
   dp=[sum(K[i][j]*d[j] for j in range(7)) for i in range(7)]
   assert all(0<=v<=1 for v in dp)
   assert sum(mx[j]*d[j] for j in range(7))==sum(my[i]*dp[i] for i in range(7))
   assert sum(r[j]*mx[j]*d[j] for j in range(7))==sum(r[i]*my[i]*dp[i] for i in range(7))
def mixed(s,t):
 weights={(0,0):(1-s)*(1-t),(1,0):s*(1-t),(0,1):(1-s)*t,(1,1):s*t}
 y=tuple(sum(weights[k]*cases[k][0][i] for k in cases) for i in range(7))
 q=[[sum(weights[k]*cases[k][1][i][j] for k in cases) for j in range(7)] for i in range(7)]
 return full(s*D,t*D),y,q
for (i,j),(y,q) in cases.items():
 x=full(i*D,j*D)
 check(x,y,q)
 print('CORNER',i,j,'SOURCE_TIMES',times(x),'SEEDLESS_FLOW',y,'NONZERO_Q',sum(v>0 for row in q for v in row))
for s,t in product((F(0),F(1,10),F(1,4),F(1,2),F(3,4),F(9,10),F(1)),repeat=2):
 check(*mixed(s,t))
print('CHECKED_EXACT_RATIONAL_GRID',49,'BINARY_LABELS_PER_POINT',128)
print('CERTIFIED_ANALYTIC_ALL_REAL_PARAMETERS_BY_BILINEAR_MIXING_OF_FOUR_EXACT_CORNERS')
print('PASS_R5_FULL_U_W_SIDE_FLOW_RECTANGLE_BLACKWELL_LIFT')
