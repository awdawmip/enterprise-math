#!/usr/bin/env python3
"""Exact checker of lower-ratio diagonal wedge using two rational eta=1/4 anchors."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import BASE_CERTIFICATES as high
Z,O=F(0),F(1)
anchors=json.loads((Path(__file__).parent/'ETA_QUARTER_CORNERS.json').read_text())

def parse_corner(key):
 ent=anchors[key]
 x=tuple(map(F,ent['source']));y=tuple(map(F,ent['target']))
 Q=[[Z]*7 for _ in range(7)]
 for i,j,v in ent['edges']:Q[i][j]=F(v)
 high.check_transport(x,y,Q)
 assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
 return x,y,Q
C0,C1=parse_corner('00'),parse_corner('11')
print('PASS_2_EXACT_ETA_QUARTER_DIAGONAL_CORNER_CERTIFICATES')
E0=(Z,)*7;E1=(O,Z,Z,Z,Z,Z,Z)
def mix(terms):return tuple(sum(c*f[k] for c,f in terms) for k in range(7))
def matmix(terms):return tuple(tuple(sum(c*M[i][j] for c,M in terms) for j in range(7)) for i in range(7))
def diag(x):
 m=high.mass(x)
 return tuple(tuple(m[i] if i==j else Z for j in range(7)) for i in range(7))
def lift(g,s,eta,t,theta,h):
 assert Z<=s<=g<=O and F(1,4)<=eta<=F(1,2) and all(Z<=v<=O for v in (t,theta,h))
 alpha=4*eta-O
 # eta=1/4 lower edge: interpolate only 00 and 11 along the physical diagonal
 cL=mix(((O-t,C0[0]),(t,C1[0])))
 yL=mix(((O-t,C0[1]),(t,C1[1])))
 QL=matmix(((O-t,C0[2]),(t,C1[2])))
 # eta=1/2 upper edge: four rational corners cover the entire rectangle
 cH,yH,QH=high.interpolated(t,t)
 c=mix(((O-alpha,cL),(alpha,cH)))
 y0=mix(((O-alpha,yL),(alpha,yH)))
 Q0=matmix(((O-alpha,QL),(alpha,QH)))
 cp=list(c);cp[4]+=F(1,10);cp[6]+=F(1,10);cp=tuple(cp)
 assert high.legal(cp) and high.residual(cp)==Z
 x=mix(((O-g,E0),(g-s,E1),(s*(O-theta),c),(s*theta,cp)))
 y=mix(((O-g,E0),(g-s,E1),(s*(O-theta),y0),(s*theta,cp)))
 Q=matmix(((O-g,diag(E0)),(g-s,diag(E1)),(s*(O-theta),Q0),(s*theta,diag(cp))))
 u=s*(F(13,40)+eta/80)*t
 w=s*(F(3,40)+F(21,80)*eta)*t
 z=s*theta/10
 assert x==(g,s,eta*s,u,F(9,40)*eta*s+z,w,z)
 assert high.residual(x)==F(9,10)*eta*s*s*(theta-O)
 assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
 high.check_transport(x,y,Q)
 xh=mix(((O-h,x),(h,y)))
 Qh=matmix(((O-h,Q),(h,diag(y))))
 high.check_transport(xh,y,Qh)
 for d in ((Z,)*7,(O,)*7,(Z,F(1,7),F(2,7),F(1,2),F(5,7),F(6,7),O)):
  my=high.mass(y);mx=high.mass(xh)
  dp=tuple(sum(Qh[i][j]*d[j] for j in range(7))/my[i] if my[i] else Z for i in range(7))
  assert all(Z<=v<=O for v in dp)
  assert sum(my[i]*dp[i] for i in range(7))==sum(mx[i]*d[i] for i in range(7))
  assert sum(high.R[i]*my[i]*dp[i] for i in range(7))==sum(high.R[i]*mx[i]*d[i] for i in range(7))
 return x,y
n=0
for g in (Z,F(1,2),O):
 for s in (Z,g/2,g):
  for eta,t,theta,h in product((Z,F(1,2),O),repeat=4):
   lift(g,s,F(1,4)+eta/4,t,theta,h);n+=1
assert n==729
print('PASS_729_EXACT_G_S_ETA_T_THETA_H_DIAGONAL_WEDGE_CHECKS',n)
x,y=lift(O,O,F(3,8),F(1,2),F(1,2),Z)
print('ETA_3_8_DIAGONAL_SOURCE',','.join(map(str,x)))
print('ETA_3_8_DIAGONAL_TARGET',','.join(map(str,y)))
print('ETA_3_8_DIAGONAL_STOP_TIMES',','.join(map(str,high.times(x))))
print('ETA_3_8_DIAGONAL_RESIDUAL',high.residual(x))
print('PASS_R5_LOWER_RATIO_DIAGONAL_ALL_REAL_BLACKWELL_WEDGE')
