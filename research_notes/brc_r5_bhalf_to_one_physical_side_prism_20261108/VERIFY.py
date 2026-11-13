#!/usr/bin/env python3
"""Exact eight-corner source certificates for 1/2 <= b <= 1, all real p,q,t.

The b=1/2 endpoint is current-branch sibling VERIFY.py; b=1 corner
matrices are literal rational coefficients from immutable 194f81437a86b5fa.
Python standard-library Fraction only; no float, no optimization at runtime.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import contextlib,io,runpy
root=Path(__file__).resolve().parent.parent
with contextlib.redirect_stdout(io.StringIO()):
 base=runpy.run_path(str(root/'brc_r5_full_physical_side_rectangle_20261108'/'VERIFY.py'))
Z,O,r=base['Z'],base['O'],base['r']
C,YC,E=base['C'],base['YC'],base['E']
matrix,legal,masses,times,R,verify_transport=(base[k] for k in ('matrix','legal','masses','times','R','verify_transport'))
# Prior independently published/executed exact four corner certificates at b=1.
E1=(
 ((0,0,'67/720'),(0,1,'8477/360000'),(1,1,'23/80'),(2,1,'1523/100000'),(2,3,'3477/100000'),(3,1,'20201/1800000'),(3,3,'31207/450000'),(3,5,'20201/1800000'),(4,3,'3477/100000'),(4,5,'1523/100000'),(5,5,'23/80'),(6,5,'8477/360000'),(6,6,'67/720')),
 ((0,0,'20443/72000'),(0,3,'9977/1184400'),(0,5,'16277/2961000'),(3,3,'421271/1692000'),(4,3,'9/470'),(5,3,'3677/658000'),(5,5,'102899/329000'),(6,5,'16277/846000'),(6,6,'6943/72000')),
 ((0,0,'6943/72000'),(0,1,'76/1875'),(1,1,'19/80'),(2,1,'169/3125'),(2,3,'287/6250'),(3,1,'101/18750'),(3,3,'67039/300000'),(6,3,'287/22500'),(6,6,'20443/72000')),
 ((0,0,'10343/36000'),(0,3,'22/1875'),(2,3,'1/30'),(3,3,'93019/270000'),(5,3,'1/30'),(6,3,'167/67500'),(6,6,'10343/36000')),
)
C1=tuple(matrix(e) for e in E1)
YC1=(
 tuple(map(F,('1','9/10','9/10','13/800','117/400','13/800','9/100'))),
 tuple(map(F,('686/705','686/705','659/705','1233/3760','347/1128','0','343/3525'))),
 tuple(map(F,('1','4/5','1','7/200','61/200','129/400','2/25'))),
 tuple(map(F,('1','14/15','1','379/1200','191/600','359/1200','7/75'))),
)

def side_caps(b):
 return F(13,40)+b/80, F(3,40)+F(21,80)*b

def source(b,p,q):
 U_b,W_b=side_caps(b)
 return (O,O,b,p*U_b,F(9,40)*b,q*W_b,Z)

def combine(b,p,q):
 theta=2*b-1
 h=((1-p)*(1-q),p*(1-q),(1-p)*q,p*q)
 yy0=tuple(sum(h[c]*YC[c][i] for c in range(4)) for i in range(7))
 yy1=tuple(sum(h[c]*YC1[c][i] for c in range(4)) for i in range(7))
 qq0=tuple(tuple(sum(h[c]*C[c][i][j] for c in range(4)) for j in range(7)) for i in range(7))
 qq1=tuple(tuple(sum(h[c]*C1[c][i][j] for c in range(4)) for j in range(7)) for i in range(7))
 y=tuple((1-theta)*yy0[i]+theta*yy1[i] for i in range(7))
 Q=tuple(tuple((1-theta)*qq0[i][j]+theta*qq1[i][j] for j in range(7)) for i in range(7))
 return y,Q

for b,oldY,oldC in ((F(1,2),YC,C),(O,YC1,C1)):
 for p,q,c in ((Z,Z,0),(O,Z,1),(Z,O,2),(O,O,3)):
  x=source(b,p,q)
  y,Q=oldY[c],oldC[c]
  assert legal(x) and legal(y) and times(x)==times(y)
  assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
  assert R(x)==-F(9,10)*b and R(y)==Z
  verify_transport(Q,x,y)
print('PASS_EIGHT_EXACT_RATIONAL_CORNER_CERTIFICATES',tuple(map(len,E)),tuple(map(len,E1)))
count=0
for b,p,q,t in product((F(1,2),F(5,8),F(3,4),F(7,8),O), (Z,F(1,4),F(1,2),F(3,4),O), (Z,F(1,4),F(1,2),F(3,4),O), (Z,F(1,4),F(1,2),F(3,4),O)):
 x=source(b,p,q)
 y,Q=combine(b,p,q)
 assert legal(x) and legal(y) and times(x)==times(y)
 assert R(x)==-F(9,10)*b and R(y)==Z
 assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
 verify_transport(Q,x,y)
 xt=tuple((1-t)*x[i]+t*y[i] for i in range(7))
 my=masses(y)
 Qt=tuple(tuple((1-t)*Q[i][j]+(t*my[i] if i==j else Z) for j in range(7)) for i in range(7))
 assert legal(xt) and times(xt)==times(y)
 verify_transport(Qt,xt,y)
 for d in ((Z,)*7,(O,)*7,tuple(F(j,7) for j in range(7))):
  k=tuple(sum(Qt[i][j]*d[j] for j in range(7))/my[i] if my[i] else Z for i in range(7))
  assert all(Z<=v<=O for v in k)
  assert sum(my[i]*k[i] for i in range(7))==sum(masses(xt)[j]*d[j] for j in range(7))
  assert sum(r[i]*my[i]*k[i] for i in range(7))==sum(r[j]*masses(xt)[j]*d[j] for j in range(7))
 count+=1
print('PASS_625_RATIONAL_B_P_Q_T_CASES',count)
print('CAPACITIES_AT_B_HALF',side_caps(F(1,2)))
print('CAPACITIES_AT_B_ONE',side_caps(O))
print('SAMPLE_MID_TARGET',','.join(map(str,combine(F(3,4),F(1,2),F(1,2))[0])))
print('PASS_ALL_REAL_B_HALF_TO_ONE_FOUR_PARAMETER_BLACKWELL_FULL_SIDE_BOX')
