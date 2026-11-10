#!/usr/bin/env python3
"""Exact 4,5,6-edge global Blackwell minima in pinned 7-LR P/Q–BRC observer.
Scientific pins GK a01383f825ef9d43b4b754254303298c64041568
EM 86149263e38c22292c9def1e0f69092efa1be77e.
"""
from fractions import Fraction as F
import sympy as S
R=tuple(F(q) for q in '1/10 1/2 3/4 1 5/4 3/2 19/10'.split())
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)
assert len(D)==30

def mass(x):
 g,a,b,u,v,w,z=x
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
 F(13,40)*a+b/80-u,(g-a)/2,
 1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
 (g-b)/2,F(3,40)*a+F(21,80)*b-w,
 u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def slacks(x):
 g,a,b,u,v,w,z=x
 return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,w,
 F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def times(x):
 g,a,b,u,v,w,z=x
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
 1+g+(a+b)/2+u+v+w)
def restrictions(p):
 x,y=p[:7],p[7:]
 return (x[0]-x[2],y[0]-1,y[6]-y[1]/10,*(a-b for a,b in zip(times(x),times(y))))
def col(i,j):
 z=[F(0)]*21; z[j]=1;z[7+i]=1;z[14+j]=R[i]
 return S.Matrix(z)
# Operator has 21 rows in target μ / source ν / source-ratio moment order.
C=S.Matrix.hstack(*(col(i,j) for i,j in D))
# A global exact nonnegative separation: equality of the two marginals,
# plus martingale, forces zero offdiagonal squared LR distance.
Y=S.Matrix(list(r*r for r in R)+list(r*r for r in R)+list(-2*r for r in R))
assert (Y.T*C)==S.Matrix([[(R[i]-R[j])**2 for i,j in D]])
assert all(R[i]!=R[j] for i,j in D if i!=j)
examples=[
 ('FOUR', (F(1),F(1),F(1),F(27,80),F(1,10),F(1,4),F(1,10)), (0,3,5,6)),
 ('FIVE', (F(1),F(1),F(1),F(1,4),F(1,10),F(1,4),F(1,10)), (0,1,3,5,6)),
 ('SIX', (F(1),F(1,2),F(1),F(1,10),F(1,10),F(1,10),F(1,20)), (0,1,2,3,5,6)),
]
for name,x,supp in examples:
 m=mass(x)
 assert restrictions(x+x)==(F(0),)*5
 assert len(slacks(x)+slacks(x))==26 and all(s>=0 for s in slacks(x)+slacks(x))
 assert sum(m)==1 and all(z>=0 for z in m)
 assert tuple(i for i,t in enumerate(m) if t>0)==supp
 assert all((i,i) in D for i in supp)
 e=S.Matrix([m[i] if i==j else F(0) for i,j in D])
 q=S.Matrix(list(m)+list(m)+[R[j]*m[j] for j in range(7)])
 assert C*e==q
 assert (Y.T*q)[0]==0
 assert sum(e[k]*(R[i]-R[j])**2 for k,(i,j) in enumerate(D))==0
 assert sum(e)==1 and len([z for z in e if z>0])==len(supp)
 print(name,'SUPPORT',','.join(map(str,supp)), 'MASSES',','.join(str(m[i]) for i in supp))
 print(name,'ALL_5_PHYSICAL_EQUALITIES_TRUE','ALL_26_CAPACITY_SLACKS_NONNEGATIVE',True)
 print(name,'ALL_21_BLACKWELL_ROWS_TRUE','ALL_30_ARC_GLOBAL_DIAGONAL_UNIQUENESS_TRUE')
print('SQUARED_DISTANCE_CERTIFICATE','Y=(r^2,r^2,-2r); Y^T*C_(i,j)=(r_i-r_j)^2; Y^T*q=0')
print('PASS_EXACT_GLOBAL_MINIMUM_N_4_5_6_UNIQUE_DIAGONAL_COUPLINGS')
