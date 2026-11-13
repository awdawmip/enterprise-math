#!/usr/bin/env python3
"""Exact Fraction checker for eight R5 7x7 Blackwell certificates and the interpolation."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
D=Path(__file__).resolve().parent
ZERO,ONE=F(0),F(1)
ETA0=F(46,705)
R=tuple(map(F, ('1/10','1/2','3/4','1','5/4','3/2','19/10')))
def mass(f):
 g,a,b,u,v,w,z=f
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
  F(13,40)*a+b/80-u,(g-a)/2,
  ONE-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
  (g-b)/2,F(3,40)*a+F(21,80)*b-w,
  u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(f):
 g,a,b,u,v,w,z=f
 return (ONE+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
         ONE+g+(a+b)/2+u+v+w)
def legal(f):
 g,a,b,u,v,w,z=f
 return (ZERO<=a<=g<=ONE and ZERO<=b<=g and
   ZERO<=u<=F(13,40)*a+b/80 and ZERO<=w<=F(3,40)*a+F(21,80)*b and
   ZERO<=z<=a/10 and ZERO<=v-z<=F(9,40)*b)
def residual(f):
 _,a,b,_,v,_,z=f
 return 9*b*z-4*a*(v-z)
def check_transport(x,y,Q):
 assert len(x)==len(y)==len(Q)==7 and all(len(row)==7 for row in Q)
 mx,my=mass(x),mass(y)
 assert legal(x) and legal(y) and times(x)==times(y)
 assert sum(mx)==sum(my)==ONE
 assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==ONE
 assert all(t>=0 for row in Q for t in row)
 for i in range(7): assert sum(Q[i])==my[i],('row',i)
 for j in range(7):
  assert sum(Q[i][j] for i in range(7))==mx[j],('Qcol',j)
  assert sum(R[i]*Q[i][j] for i in range(7))==R[j]*mx[j],('Pcol',j)
def parse(file):
 data=json.loads((D/file).read_text())
 out={}
 for k in ('00','10','01','11'):
  v=data[k];x=tuple(map(F,v['source']));y=tuple(map(F,v['target']))
  Q=[[ZERO]*7 for _ in range(7)]
  for i,j,s in v['edges']:
   assert Q[i][j]==ZERO
   Q[i][j]=F(s)
  Q=tuple(map(tuple,Q))
  check_transport(x,y,Q)
  assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2] and residual(y)==0
  out[k]=(x,y,Q)
 return out
LOW=parse('ETA_SHARP_CORNERS.json')
HIGH=parse('ETA_HALF_CORNERS.json')
for cert,eta in ((LOW,ETA0),(HIGH,F(1,2))):
 for key,value in cert.items():
  x=value[0];p,q=int(key[0]),int(key[1])
  assert x==(ONE,ONE,eta,(F(13,40)+eta/80)*p,F(9,40)*eta,(F(3,40)+F(21,80)*eta)*q,ZERO)
print('PASS_8_EXACT_7x7_RATIONAL_BLACKWELL_CORNER_CERTIFICATES')
def vecmix(weighted):
 weighted=list(weighted)
 return tuple(sum(w*v[i] for w,v in weighted) for i in range(7))
def matmix(weighted):
 weighted=list(weighted)
 return tuple(tuple(sum(w*Q[i][j] for w,Q in weighted) for j in range(7))for i in range(7))
def diag(x):
 m=mass(x)
 return tuple(tuple(m[i] if i==j else ZERO for j in range(7)) for i in range(7))
E0=(ZERO,)*7
E1=(ONE,)+(ZERO,)*6
def lift(g,s,eta,p,q,theta,h):
 assert ZERO<=s<=g<=ONE and ETA0<=eta<=F(1,2)
 assert all(ZERO<=z<=ONE for z in (p,q,theta,h))
 alpha=(eta-ETA0)/(F(1,2)-ETA0)
 weights={'00':(ONE-p)*(ONE-q),'10':p*(ONE-q),
          '01':(ONE-p)*q,'11':p*q}
 blocks=[]
 for cert,ratio in ((LOW,ONE-alpha),(HIGH,alpha)):
  for k in weights:
   x,y,Q=cert[k];blocks.append((ratio*weights[k],x,y,Q))
 c=vecmix((wt,x) for wt,x,_,_ in blocks)
 z=vecmix((wt,y) for wt,_,y,_ in blocks)
 K=matmix((wt,Q) for wt,_,_,Q in blocks)
 assert c==(ONE,ONE,eta,(F(13,40)+eta/80)*p,F(9,40)*eta,
   (F(3,40)+F(21,80)*eta)*q,ZERO)
 cp=list(c);cp[4]+=F(1,10);cp[6]+=F(1,10);cp=tuple(cp)
 assert legal(cp) and residual(cp)==ZERO
 x=vecmix(((ONE-g,E0),(g-s,E1),(s*(ONE-theta),c),(s*theta,cp)))
 y=vecmix(((ONE-g,E0),(g-s,E1),(s*(ONE-theta),z),(s*theta,cp)))
 Q=matmix(((ONE-g,diag(E0)),(g-s,diag(E1)),(s*(ONE-theta),K),(s*theta,diag(cp))))
 assert x==(g,s,eta*s,s*(F(13,40)+eta/80)*p,
            F(9,40)*eta*s+s*theta/10,s*(F(3,40)+F(21,80)*eta)*q,s*theta/10)
 assert residual(x)==F(9,10)*eta*s*s*(theta-ONE)
 assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
 check_transport(x,y,Q)
 xh=vecmix(((ONE-h,x),(h,y)))
 Qh=matmix(((ONE-h,Q),(h,diag(y))))
 check_transport(xh,y,Qh)
 for d in ((ZERO,)*7,(ONE,)*7,
           (ZERO,F(1,7),F(2,7),F(1,2),F(5,7),F(6,7),ONE)):
  my=mass(y);mx=mass(xh)
  dp=tuple(sum(Qh[i][j]*d[j] for j in range(7))/my[i] if my[i] else ZERO for i in range(7))
  assert all(ZERO<=v<=ONE for v in dp)
  assert sum(my[i]*dp[i] for i in range(7))==sum(mx[j]*d[j] for j in range(7))
  assert sum(R[i]*my[i]*dp[i] for i in range(7))==sum(R[j]*mx[j]*d[j] for j in range(7))
 return x,y
n=0
for g in (ZERO,F(1,2),ONE):
 for s in (ZERO,g/2,g):
  for z,p,q,theta,h in product((ZERO,F(1,2),ONE),repeat=5):
   eta=ETA0+(F(1,2)-ETA0)*z
   lift(g,s,eta,p,q,theta,h);n+=1
assert n==2187
print('PASS_2187_EXACT_REAL_PARAMETER_BRIDGE_REGRESSION_CHECKS',n)
def L(x):
 t1,t2=times(x)
 return -F(616,141)*(t1-ONE)+F(524,141)*(t2-ONE)
for eta in (ZERO,F(1,20),ETA0,F(1,10),F(1,4),F(1,2)):
 x=(ONE,ONE,eta,F(13,40)+eta/80,F(9,40)*eta,ZERO,ZERO)
 assert L(x)==ETA0-eta
for y in [LOW[k][1] for k in LOW]+[HIGH[k][1] for k in HIGH]:
 g,a,b,u,v,w,z=y
 assert L(y)==-F(92,141)*(g-a)-b-F(400,141)*w -F(72,47)*(F(13,40)*a+b/80-u)
 assert L(y)<=ZERO
print('PASS_EXACT_SHARP_FACE_BOUND_ETA_GE_46_OVER_705_FOR_P1_Q0')
print('SHARP_RATIO',ETA0)
print('PASS_R5_ALL_REAL_FULL_PHYSICAL_RECTANGLE_SHARP_FACE_LOWER_BRIDGE')
