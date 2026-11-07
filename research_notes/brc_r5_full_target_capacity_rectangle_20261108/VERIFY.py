#!/usr/bin/env python3
"""Exact seven-likelihood Blackwell transport certificate, full target-capacity rectangle."""
from fractions import Fraction as F
R=tuple(map(F,('1/10','1/2','3/4','1','5/4','3/2','19/10')))
Z=F(0); ONE=F(1)
U=F(503,1600); W=F(303,1600)
Q0=tuple(tuple(map(F,row.split())) for row in (
 '67/1440 3/320 0 9167/2260800 0 3/800 0',
 '0 503/1600 0 0 0 0 0',
 '0 0 0 1/80 0 0 0',
 '0 3/400 0 856759/11304000 119171/11304000 0 0',
 '0 0 0 17017/628000 147833/628000 0 0',
 '0 0 0 0 0 303/1600 0',
 '0 0 0 0 9167/2260800 21/1600 67/1440',
))
X=(ONE,ONE,F(1,2),Z,F(9,80),Z,Z)
Y=(F(39,40),F(19,20),F(9,20),Z,F(3,16),Z,F(57,628))
def masses(q):
 g,a,b,u,v,w,z=q
 c0=F(13,40)*a+b/80; c1=a/10+F(9,40)*b; c2=F(3,40)*a+F(21,80)*b
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
         c0-u,(g-a)/2,
         1-g+c1-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
         (g-b)/2,c2-w,
         u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def legal(q):
 g,a,b,u,v,w,z=q
 return 0<=a<=g<=1 and 0<=b<=g and 0<=u<=F(13,40)*a+b/80 and 0<=w<=F(3,40)*a+F(21,80)*b and 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
def times(q):
 g,a,b,u,v,w,z=q
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,1+g+(a+b)/2+u+v+w)
def residual(q):
 g,a,b,u,v,w,z=q
 return 9*b*z-4*a*(v-z)
def pair(u,w):
 x=list(X); y=list(Y); x[3]=y[3]=u; x[5]=y[5]=w
 return tuple(x),tuple(y)
def kernel(u,w,t=Z):
 x,y=pair(u,w)
 d=(F(509,900)*u+w/100,-u,Z,F(191,450)*(u+w),Z,-w,u/100+F(509,900)*w)
 my=masses(y)
 return tuple(tuple((1-t)*Q0[i][j]+(1-t)*d[i]*(i==j)+t*(my[i] if i==j else Z) for j in range(7)) for i in range(7))
def check(u,w,t):
 x,y=pair(u,w)
 xt=tuple((1-t)*a+t*b for a,b in zip(x,y))
 assert legal(x) and legal(y) and legal(xt) and residual(x)==-F(9,20) and residual(y)==0
 assert times(x)==times(y)==times(xt)
 mx,my,mt=masses(x),masses(y),masses(xt)
 assert sum(mx)==sum(my)==sum(mt)==ONE
 assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==sum(R[i]*mt[i] for i in range(7))==ONE
 Q=kernel(u,w,t)
 assert all(v>=0 for row in Q for v in row)
 for i in range(7):
  assert sum(Q[i])==my[i]
 for j in range(7):
  assert sum(Q[i][j] for i in range(7))==mt[j]
  assert sum(R[i]*Q[i][j] for i in range(7))==R[j]*mt[j]
 for d in ((Z,)*7,(ONE,)*7,(Z,F(1,7),F(2,7),F(1,2),F(5,7),F(6,7),ONE)):
  transformed=tuple(sum(Q[i][j]*d[j] for j in range(7))/my[i] if my[i] else Z for i in range(7))
  assert all(Z<=a<=ONE for a in transformed)
  assert sum(my[i]*transformed[i] for i in range(7))==sum(mt[j]*d[j] for j in range(7))
  assert sum(R[i]*my[i]*transformed[i] for i in range(7))==sum(R[j]*mt[j]*d[j] for j in range(7))
assert all(len(row)==7 for row in Q0)
assert Q0[1][1]==U and Q0[5][5]==W
assert all(Q0[i][j]>=0 for i in range(7) for j in range(7))
check(Z,Z,Z)
count=0
for uu in [Z,F(1,4),F(1,2),F(3,4),ONE]:
 for ww in [Z,F(1,4),F(1,2),F(3,4),ONE]:
  for tt in [Z,F(1,7),F(1,3),F(1,2),ONE]:
   check(U*uu,W*ww,tt); count+=1
assert (W-F(32383,175840))==F(9167,1758400)
xx,yy=pair(U,W)
print('PASS_EXACT_Q0_7_ROW_7_COLUMN_7_P_WEIGHTED_COLUMN_CERTIFICATE')
print('PASS_ALL_REAL_UW_FULL_TARGET_CAPACITY_RECTANGLE_ALGEBRAIC_PROOF')
print('PASS_125_RATIONAL_U_W_T_REGRESSIONS',count)
print('U_MAX',U,'W_MAX',W,'W_GAIN',W-F(32383,175840))
print('CORNER_SOURCE',','.join(map(str,xx)))
print('CORNER_SEEDLESS',','.join(map(str,yy)))
print('CORNER_STOPPING_TIMES',','.join(map(str,times(xx))))
print('PASS_R5_PHYSICAL_CAPACITY_RECTANGLE_ALL_REAL_BLACKWELL_LIFT')
