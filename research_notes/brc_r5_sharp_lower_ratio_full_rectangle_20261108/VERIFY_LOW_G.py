#!/usr/bin/env python3
"""Exact low-ratio eta<=1/40 saturated-v complete p/q rectangle in seedless b=0 face."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,io,contextlib
with contextlib.redirect_stdout(io.StringIO()): import VERIFY as b
Z,O=F(0),F(1)
ETA=F(1,40)
cards=json.loads((Path(__file__).parent/'ETA_1_40_BZERO_CORNERS.json').read_text())
E0=(Z,)*7
E1=(O,)+(Z,)*6
def source(eta,p,q):
 return (O,O,eta,(F(13,40)+eta/80)*p,F(9,40)*eta,(F(3,40)+F(21,80)*eta)*q,Z)
hi={}
for key,e in cards.items():
 x,y=tuple(map(F,e['source'])),tuple(map(F,e['target']))
 Q=[[Z]*7 for _ in range(7)]
 for i,j,v in e['edges']:Q[i][j]=F(v)
 b.check_transport(x,y,Q)
 assert y[2]==0 and y[4]==y[6]
 assert x==source(ETA,F(int(key[0])),F(int(key[1])))
 hi[key]=(x,y,tuple(map(tuple,Q)))
print('PASS_4_EXACT_ETA_1_40_B_ZERO_FACE_CERTIFICATES')
def lift(g,s,eta,p,q,h):
 assert Z<=s<=g<=O and Z<=eta<=ETA and all(Z<=t<=O for t in (p,q,h))
 t=eta/ETA
 weights={'00':(O-p)*(O-q),'10':p*(O-q),'01':(O-p)*q,'11':p*q}
 blocks=[]
 for key,w in weights.items():
  p0,q0=F(int(key[0])),F(int(key[1]))
  x0=source(Z,p0,q0)
  assert b.legal(x0) and b.residual(x0)==Z
  blocks.append(((O-t)*w,x0,x0,b.diag(x0)))
  x1,y1,Q1=hi[key]
  blocks.append((t*w,x1,y1,Q1))
 c=b.vecmix((wt,x) for wt,x,_,_ in blocks)
 y0=b.vecmix((wt,y) for wt,_,y,_ in blocks)
 QQ=b.matmix((wt,Q) for wt,_,_,Q in blocks)
 assert c==source(eta,p,q)
 assert y0[2]==0 and y0[4]==y0[6]
 x=b.vecmix(((O-g,E0),(g-s,E1),(s,c)))
 y=b.vecmix(((O-g,E0),(g-s,E1),(s,y0)))
 Q=b.matmix(((O-g,b.diag(E0)),(g-s,b.diag(E1)),(s,QQ)))
 assert x==(g,s,eta*s,s*(F(13,40)+eta/80)*p,F(9,40)*eta*s,s*(F(3,40)+F(21,80)*eta)*q,Z)
 assert y[2]==0 and y[4]==y[6] and b.residual(y)==Z
 b.check_transport(x,y,Q)
 xh=b.vecmix(((O-h,x),(h,y)))
 Qh=b.matmix(((O-h,Q),(h,b.diag(y))))
 b.check_transport(xh,y,Qh)
 for d in ((Z,)*7,(O,)*7,(Z,F(1,7),F(2,7),F(1,2),F(5,7),F(6,7),O)):
  mx,my=b.mass(xh),b.mass(y)
  trans=tuple(sum(Qh[i][j]*d[j] for j in range(7))/my[i] if my[i] else Z for i in range(7))
  assert all(Z<=di<=O for di in trans)
  assert sum(my[i]*trans[i] for i in range(7))==sum(mx[j]*d[j] for j in range(7))
  assert sum(b.R[i]*my[i]*trans[i] for i in range(7))==sum(b.R[j]*mx[j]*d[j] for j in range(7))
 return x,y
n=0
for g in (Z,F(1,2),O):
 for s in (Z,g/2,g):
  for t,p,q,h in product((Z,F(1,2),O), repeat=4):
   lift(g,s,ETA*t,p,q,h);n+=1
assert n==729
print('PASS_729_EXACT_ETA_0_TO_1_40_G_FACE_FULL_RECTANGLE_REGRESSION',n)
print('PASS_ALL_REAL_LOW_RATIO_B_ZERO_FACE_SATURATED_V_RECTANGLE')
