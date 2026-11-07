#!/usr/bin/env python3
"""Exact standalone Blackwell lift of FULL_HIST maximal-u negative-residual corner."""
from fractions import Fraction as F
from itertools import product
R=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
x=(F(1),F(1),F(1),F(27,80),F(9,40),F(0),F(0))
y=(F(686,705),F(686,705),F(659,705),F(1233,3760),F(347,1128),F(0),F(343,3525))
def masses(x):
 g,a,b,u,v,w,z=x
 c0=F(13,40)*a+b/80
 c1=a/10+F(9,40)*b
 c2=F(3,40)*a+F(21,80)*b
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
         0<=u<=F(13,40)*a+b/80 and 0<=w<=F(3,40)*a+F(21,80)*b and
         0<=z<=a/10 and 0<=v-z<=F(9,40)*b)
def res(x):
 g,a,b,u,v,w,z=x
 return 9*b*z-4*a*(v-z)
assert legal(x) and legal(y)
assert res(x)==-F(9,10) and res(y)==0
assert times(x)==times(y)==(F(543,160),F(57,16))
mx,my=masses(x),masses(y)
assert mx==(F(20443,72000),F(0),F(0),F(10157,36000),F(0),F(27,80),F(6943,72000))
assert my==(F(1007929,3384000),F(0),F(0),F(421271,1692000),F(9,470),F(1197,3760),F(391429,3384000))
Q=[[F(0) for _ in range(7)] for _ in range(7)]
Q[0][0]=F(20443,72000);Q[0][3]=F(9977,1184400);Q[0][5]=F(16277,2961000)
Q[3][3]=F(421271,1692000);Q[4][3]=F(9,470)
Q[5][3]=F(3677,658000);Q[5][5]=F(102899,329000)
Q[6][5]=F(16277,846000);Q[6][6]=F(6943,72000)
assert all(v>=0 for row in Q for v in row)
assert sum(mx)==sum(my)==1
assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==1
for i in range(7):assert sum(Q[i])==my[i]
for j in range(7):
 assert sum(Q[i][j] for i in range(7))==mx[j]
 assert sum(R[i]*Q[i][j] for i in range(7))==R[j]*mx[j]
K=[[Q[i][j]/my[i] if my[i] else (F(1) if i==j else F(0)) for j in range(7)] for i in range(7)]
assert all(sum(row)==1 for row in K)
for d in product((F(0),F(1)),repeat=7):
 dp=[sum(K[i][j]*d[j] for j in range(7)) for i in range(7)]
 assert all(0<=v<=1 for v in dp)
 assert sum(mx[j]*d[j] for j in range(7))==sum(my[i]*dp[i] for i in range(7))
 assert sum(R[j]*mx[j]*d[j] for j in range(7))==sum(R[i]*my[i]*dp[i] for i in range(7))
print('FULL',x,'RESIDUAL',res(x))
print('SEEDLESS',y,'RESIDUAL',res(y))
print('TIMES',times(x))
for i in range(7):print('Q_ROW',i,','.join(f'{j}:{v}' for j,v in enumerate(Q[i]) if v))
print('PASS_R5_U_MAX_CORNER_ALL_SEVEN_REAL_DECLARATIONS_EXACT')
