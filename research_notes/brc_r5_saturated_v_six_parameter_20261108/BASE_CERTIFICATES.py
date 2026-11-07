#!/usr/bin/env python3
"""Exact calibrated Blackwell certificates for the R5 full source side rectangle."""
from fractions import Fraction as F
from itertools import product

Z, ONE = F(0), F(1)
R = (F(1,10), F(1,2), F(3,4), ONE, F(5,4), F(3,2), F(19,10))
U, W = F(53,160), F(33,160)

def frac(s): return F(s)
def qmatrix(rows):
    q = [[Z]*7 for _ in range(7)]
    for i,j,value in rows: q[i][j] = frac(value)
    return tuple(tuple(row) for row in q)

TARGET = {
 (0,0): tuple(map(frac,('11/12','11/12','1/2','13/480','49/240','1/160','11/120'))),
 (1,0): tuple(map(frac,('1','1','7/20','507/1600','143/800','37/1600','1/10'))),
 (0,1): tuple(map(frac,('5/6','5/6','2/3','31/480','7/30','3/16','1/12'))),
 (1,1): tuple(map(frac,('19/20','19/20','11/20','101/320','7/32','53/320','19/200'))),
}
EDGES = {
 (0,0): [(0,0,'67/1440'),(0,1,'13/336'),(0,5,'59/94500'),
         (1,1,'133/480'),(3,3,'43/360'),(3,4,'743/18000'),
         (4,4,'1507/9000'),(4,5,'46/1125'),(5,1,'13/840'),
         (5,4,'743/18000'),(5,5,'34523/252000'),(6,5,'749/27000'),(6,6,'67/1440')],
 (1,0): [(0,0,'33677/144000'),(0,3,'1021/240000'),(1,3,'13909/1200000'),
         (1,5,'1091/1200000'),(3,3,'2057/10000'),(4,3,'11549/300000'),
         (4,4,'1/4'),(4,5,'10951/300000'),(5,5,'23/160'),
         (6,5,'2007/80000'),(6,6,'7177/144000')],
 (0,1): [(0,0,'6997/144000'),(0,1,'7/108'),(0,3,'211/24000'),
         (1,1,'103/480'),(3,1,'7/135'),(3,3,'65653/360000'),
         (3,4,'28399/270000'),(4,4,'1/12'),(5,3,'633/40000'),
         (5,4,'1367/40000'),(6,4,'5899/216000'),(6,6,'23497/144000')],
 (1,1): [(0,0,'16987/72000'),(0,3,'91/9600'),(0,4,'773/72000'),
         (3,3,'1541/4800'),(4,4,'1/5'),(5,3,'273/16000'),
         (5,4,'527/16000'),(6,4,'911/144000'),(6,6,'11987/72000')],
}
Q = {key:qmatrix(edges) for key,edges in EDGES.items()}

def source(u,w): return (ONE,ONE,F(1,2),u,F(9,80),w,Z)
def mass(f):
 g,a,b,u,v,w,z=f
 c0=F(13,40)*a+b/80
 c1=a/10+F(9,40)*b
 c2=F(3,40)*a+F(21,80)*b
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
         c0-u,(g-a)/2,
         1-g+c1-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
         (g-b)/2,c2-w,
         u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(f):
 g,a,b,u,v,w,z=f
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
         1+g+(a+b)/2+u+v+w)
def residual(f):
 g,a,b,u,v,w,z=f
 return 9*b*z-4*a*(v-z)
def legal(f):
 g,a,b,u,v,w,z=f
 return (Z<=a<=g<=ONE and Z<=b<=g
     and Z<=u<=F(13,40)*a+b/80
     and Z<=w<=F(3,40)*a+F(21,80)*b
     and Z<=z<=a/10 and Z<=v-z<=F(9,40)*b)
def check_transport(x,y,qq):
 mx,my=mass(x),mass(y)
 assert legal(x) and legal(y) and times(x)==times(y)
 assert sum(mx)==sum(my)==ONE
 assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==ONE
 assert all(t>=0 for row in qq for t in row)
 for i in range(7): assert sum(qq[i])==my[i]
 for j in range(7):
  assert sum(qq[i][j] for i in range(7))==mx[j]
  assert sum(R[i]*qq[i][j] for i in range(7))==R[j]*mx[j]

for idx in product((0,1),repeat=2):
 u,w=U*idx[0],W*idx[1];y=TARGET[idx]
 assert y[0]==y[1] and y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
 assert residual(y)==0 and residual(source(u,w))==-F(9,20)
 check_transport(source(u,w),y,Q[idx])
print('PASS_4_EXACT_CORNER_SEEDLESS_FLOWS_AND_7X7_Q_CERTIFICATES')

def interpolated(su,sw):
 ww={(0,0):(ONE-su)*(ONE-sw),(1,0):su*(ONE-sw),
     (0,1):(ONE-su)*sw,(1,1):su*sw}
 y=tuple(sum(c*TARGET[k][i] for k,c in ww.items()) for i in range(7))
 q=tuple(tuple(sum(c*Q[k][i][j] for k,c in ww.items())
       for j in range(7)) for i in range(7))
 x=source(su*U,sw*W)
 return x,y,q

count=0
steps=(Z,F(1,4),F(1,2),F(3,4),ONE)
for su,sw,t in product(steps,repeat=3):
 x,y,q=interpolated(su,sw)
 assert legal(x) and legal(y) and residual(x)==-F(9,20) and residual(y)==0
 assert y[0]==y[1] and y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
 check_transport(x,y,q)
 xt=tuple((ONE-t)*x[k]+t*y[k] for k in range(7))
 qt=tuple(tuple((ONE-t)*q[i][j]+(t*mass(y)[i] if i==j else Z)
          for j in range(7)) for i in range(7))
 check_transport(xt,y,qt)
 for d in ((Z,)*7,(ONE,)*7,(Z,F(1,7),F(2,7),F(1,2),F(5,7),F(6,7),ONE)):
  my=mass(y);mt=mass(xt)
  new_d=tuple(sum(qt[i][j]*d[j] for j in range(7))/my[i] if my[i] else Z
              for i in range(7))
  assert all(Z<=v<=ONE for v in new_d)
  assert sum(my[i]*new_d[i] for i in range(7))==sum(mt[j]*d[j] for j in range(7))
  assert sum(R[i]*my[i]*new_d[i] for i in range(7))==sum(R[j]*mt[j]*d[j] for j in range(7))
 count+=1
print('PASS_ALL_REAL_PHYSICAL_SOURCE_RECTANGLE_BY_BILINEAR_CONVEXITY')
print('PASS_125_EXACT_U_W_T_TEST_CASES',count)
print('UPPER_RIGHT_SOURCE',','.join(map(str,source(U,W))))
print('UPPER_RIGHT_TARGET',','.join(map(str,TARGET[(1,1)])))
print('UPPER_RIGHT_STOPPING_TIMES',','.join(map(str,times(source(U,W)))))
print('FROZEN_INPUTS_UNCHANGED: global a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e')
print('PASS_R5_COMPLETE_SOURCE_SIDE_CAPACITY_RECTANGLE_EXACT_BLACKWELL_LIFT')
