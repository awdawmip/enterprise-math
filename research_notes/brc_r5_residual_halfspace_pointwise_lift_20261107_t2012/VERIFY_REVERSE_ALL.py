#!/usr/bin/env python3
"""Exact Blackwell kernel: a single seedless flow dominates all 7 labels of a FULL R<0 corner."""
from fractions import Fraction as F

R=[F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10)]
x=(F(1),F(1),F(1),F(0),F(9,40),F(0),F(0))
y=(F(1),F(19,20),F(19,20),F(0),F(11,40),F(0),F(11,130))

def masses(z):
 g,a,b,u,v,w,zz=z
 c0=F(13,40)*a+F(1,80)*b
 c1=a/F(10)+F(9,40)*b
 c2=F(3,40)*a+F(21,80)*b
 return (F(509,900)*u+F(47,180)*zz+F(67,162)*(v-zz)+w/F(100),
         c0-u,(g-a)/2,
         1-g+c1-v+F(191,450)*(u+w)+F(43,90)*zz+F(14,81)*(v-zz),
         (g-b)/2,c2-w,
         u/F(100)+F(47,180)*zz+F(67,162)*(v-zz)+F(509,900)*w)

def time(z):
 g,a,b,u,v,w,zz=z
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
         1+g+(a+b)/2+u+v+w)

mx,my=masses(x),masses(y)
assert mx==(F(67,720),F(27,80),F(0),F(5,36),F(0),F(27,80),F(67,720))
assert my==(F(121,1200),F(513,1600),F(1,40),F(257,2400),F(1,40),F(513,1600),F(121,1200))
assert time(x)==time(y)==(F(129,40),)*2
assert 9*x[2]*x[6]-4*x[1]*(x[4]-x[6])==-F(9,10)
assert 9*y[2]*y[6]-4*y[1]*(y[4]-y[6])==0

# Q[i][j] is Q-measure from seedless-y input key i to FULL-x output key j.
# All unspecified entries vanish.
Q=[[F(0) for j in range(7)] for i in range(7)]
for side in (0,1):
 tail=0 if side==0 else 6
 mid=1 if side==0 else 5
 near=2 if side==0 else 4
 # Preserve original extreme tail Q mass, preserve the direct mid node,
 # and send enough of remaining seedless tail+near mass to fill mid key.
 Q[tail][tail]=mx[tail]
 Q[mid][mid]=my[mid]
 gap=mx[mid]-my[mid]  # 27/1600
 p=F(5,13)*gap        # 0.1/0.75 mixture averages to LR 1/2
 q=F(8,13)*gap
 Q[tail][mid]=p
 Q[near][mid]=q
 # Remaining symmetric mass, together with original LR=1 mass, goes to LR=1.
 Q[tail][3]=my[tail]-mx[tail]-p
 Q[near][3]=my[near]-q
Q[3][3]=my[3]

for i in range(7):
 assert all(z>=0 for z in Q[i])
 assert sum(Q[i])==my[i],('row',i)
for j in range(7):
 assert sum(Q[i][j] for i in range(7))==mx[j],('column-Q',j)
 assert sum(R[i]*Q[i][j] for i in range(7))==R[j]*mx[j],('column-P',j)

K=[[z/my[i] if my[i]>0 else F(0) for z in Q[i]] for i in range(7)]
assert all(sum(row)==1 for row in K)
# Since K is a genuine channel, for every real d in [0,1]^7
# d'_i=sum_j K[i][j]*d_j gives matching W exactly. Check rational examples.
from itertools import product
for d in product((F(0),F(1)),repeat=7):
 dp=[sum(K[i][j]*d[j] for j in range(7)) for i in range(7)]
 assert all(0<=v<=1 for v in dp)
 eqx=sum(mx[j]*d[j] for j in range(7))
 eqy=sum(my[i]*dp[i] for i in range(7))
 epx=sum(R[j]*mx[j]*d[j] for j in range(7))
 epy=sum(R[i]*my[i]*dp[i] for i in range(7))
 assert eqx==eqy and epx==epy
print('SOURCE_R',-F(9,10),'TIMES',time(x))
print('SEEDLESS',y)
for i in range(7):
 print('K_ROW',i,','.join(f'{j}:{v}' for j,v in enumerate(K[i]) if v))
print('PASS_REVERSE_CORNER_SEVEN_KEY_ALL_REAL_BLACKWELL_LIFT')
