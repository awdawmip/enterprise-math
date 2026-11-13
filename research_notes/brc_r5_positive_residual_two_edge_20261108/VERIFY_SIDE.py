#!/usr/bin/env python3
"""Exact finite rational Blackwell certificate for the uncovered low-slack R5 side witness."""
from fractions import Fraction as F
r=tuple(map(F,('1/10','1/2','3/4','1','5/4','3/2','19/10')))
Z=F(0);ONE=F(1)
x=(ONE,ONE,F(1,2),Z,F(9,80),Z,Z)
y=(F(39,40),F(19,20),F(9,20),Z,F(3,16),Z,F(57,628))

def legal(q):
 g,a,b,u,v,w,z=q
 return 0<=a<=g<=1 and 0<=b<=g and 0<=u<=F(13,40)*a+b/80 and 0<=w<=F(3,40)*a+F(21,80)*b and 0<=z<=a/10 and 0<=v-z<=F(9,40)*b

def masses(q):
 g,a,b,u,v,w,z=q
 c0=F(13,40)*a+b/80;c1=a/10+F(9,40)*b;c2=F(3,40)*a+F(21,80)*b
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,c0-u,(g-a)/2,
 1-g+c1-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
 (g-b)/2,c2-w,u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def times(q):
 g,a,b,u,v,w,z=q
 return (ONE+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,ONE+g+(a+b)/2+u+v+w)

def residual(q):
 g,a,b,u,v,w,z=q
 return 9*b*z-4*a*(v-z)

Q=[
 ['67/1440','27113/4044320','0','28949/5199840','0','971/197820','0'],
 ['0','503/1600','0','0','0','0','0'],
 ['0','43271/4333200','0','0','5447/2166600','0','0'],
 ['0','0','0','35357/376800','0','0','0'],
 ['0','0','0','28949/1444400','175103/722200','0','0'],
 ['0','22459/121329600','0','0','5447/1083300','32383/175840','0'],
 ['0','0','0','0','0','971/56520','67/1440']
]
Q=tuple(tuple(F(q) for q in row) for row in Q)
mx,my=masses(x),masses(y)
assert legal(x) and legal(y) and times(x)==times(y)==(F(14,5),F(229,80))
assert residual(x)==-F(9,20) and residual(y)==0
assert all(q>=0 for row in Q for q in row)
for i in range(7):assert sum(Q[i])==my[i]
for j in range(7):
 assert sum(Q[i][j] for i in range(7))==mx[j]
 assert sum(r[i]*Q[i][j] for i in range(7))==r[j]*mx[j]
assert sum(mx)==sum(my)==1 and sum(mx[i]*r[i] for i in range(7))==sum(my[i]*r[i] for i in range(7))==1
print('PASS_LOW_SLACK_EXACT_7X7_BLACKWELL_CERTIFICATE')

# The original point falls outside the earlier H_slack join: a=g=1 and z=0
# forces all mixture components to have a=g=1 and z=0. Then F is excluded;
# H_slack requires g>=a+a/10 and is excluded; C requires a=b and is excluded.
assert x[1]==x[0]==1 and x[6]==0 and x[1]!=x[2]
assert x[0]+x[6] < max(x[1],x[2])+x[1]/10
assert x[0]-max(x[1],x[2])< -residual(x)/(9*x[2])
print('PASS_OUTSIDE_PREDECESSOR_C_F_HSLACK_JOIN_AND_NEGATIVE_SHIFT')

for t in [Z,F(1,7),F(1,3),F(1,2),F(2,3),ONE]:
 q=tuple((1-t)*a+t*b for a,b in zip(x,y))
 J=tuple(tuple((1-t)*Q[i][j]+(t*my[i] if i==j else Z) for j in range(7)) for i in range(7))
 assert legal(q) and times(q)==times(y)
 assert all(z>=0 for row in J for z in row)
 mm=masses(q)
 for i in range(7):assert sum(J[i])==my[i]
 for j in range(7):
  assert sum(J[i][j] for i in range(7))==mm[j]
  assert sum(r[i]*J[i][j] for i in range(7))==r[j]*mm[j]
 for d in [(Z,)*7,(ONE,)*7,(Z,F(1,7),F(2,7),F(1,2),F(5,7),F(6,7),ONE)]:
  kd=tuple(sum(J[i][j]*d[j] for j in range(7))/my[i] if my[i]>0 else Z for i in range(7))
  assert all(Z<=a<=ONE for a in kd)
  assert sum(my[i]*kd[i] for i in range(7))==sum(mm[j]*d[j] for j in range(7))
  assert sum(r[i]*my[i]*kd[i] for i in range(7))==sum(r[j]*mm[j]*d[j] for j in range(7))
print('PASS_WHOLE_REAL_SEGMENT_BY_AFFINE_INTERPOLATION_SIX_RATIONAL_REGRESSIONS')
print('SOURCE',','.join(map(str,x)))
print('SEEDLESS',','.join(map(str,y)))
print('SOURCE_QMASSES',','.join(map(str,mx)))
print('SEEDLESS_QMASSES',','.join(map(str,my)))
print('PASS_R5_LOW_SLACK_NEGATIVE_RESIDUAL_EXACT_SIDE_WITNESS')
