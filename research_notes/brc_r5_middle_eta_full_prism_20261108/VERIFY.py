#!/usr/bin/env python3
"""Exact Fraction certificates and all-real constructive interpolation for R5."""
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

R=tuple(map(F, ('1/10','1/2','3/4','1','5/4','3/2','19/10')))
Z=F(0)
O=F(1)
ETA0=F(33,1000)
ETA1=F(1,30)

def mass(v):
 g,a,b,u,vv,w,z=v
 return (
  F(509,900)*u+F(47,180)*z+F(67,162)*(vv-z)+w/100,
  F(13,40)*a+b/80-u,
  (g-a)/2,
  1-g+a/10+F(9,40)*b-vv+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(vv-z),
  (g-b)/2,
  F(3,40)*a+F(21,80)*b-w,
  u/100+F(47,180)*z+F(67,162)*(vv-z)+F(509,900)*w,
 )

def stop(v):
 g,a,b,u,vv,w,z=v
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+vv+F(3,2)*w,
         1+g+(a+b)/2+u+vv+w)

def legal(v):
 g,a,b,u,vv,w,z=v
 return (0<=g<=1 and 0<=a<=g and 0<=b<=g and
         0<=u<=F(13,40)*a+b/80 and
         0<=w<=F(3,40)*a+F(21,80)*b and
         0<=z<=a/10 and 0<=vv-z<=F(9,40)*b)

def source(theta,p,q,eta=ETA1):
 return (O,O,eta,(F(13,40)+eta/80)*p,
         F(9,40)*eta+theta/10,
         (F(3,40)+F(21,80)*eta)*q,theta/10)

def diag(v):
 m=mass(v)
 return tuple(tuple(m[i] if i==j else Z for j in range(7)) for i in range(7))

def check(x,y,Q,face=None):
 assert legal(x),('illegal source',x)
 assert legal(y),('illegal target',y)
 if face=='G':assert y[2]==0 and y[4]==y[6]
 if face=='F':assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
 assert y[2]*9*y[6]==4*y[1]*(y[4]-y[6]), 'not seedless'
 mx=mass(x);my=mass(y)
 assert sum(mx,Z)==sum(my,Z)==1
 assert sum((r*m for r,m in zip(R,mx)),Z)==1
 assert sum((r*m for r,m in zip(R,my)),Z)==1
 for i in range(7):
  assert all(Q[i][j]>=0 for j in range(7))
  assert sum(Q[i],Z)==my[i],('row',i)
 for j in range(7):
  assert sum((Q[i][j] for i in range(7)),Z)==mx[j],('col',j)
  assert sum((R[i]*Q[i][j] for i in range(7)),Z)==R[j]*mx[j],('P col',j)
 assert stop(x)==stop(y),'stop mismatch'
 for d in [tuple(F(i==j) for i in range(7)) for j in range(7)]:
  mapped=tuple(sum((Q[i][j]*d[j] for j in range(7)),Z)/my[i] if my[i] else Z for i in range(7))
  assert all(0<=v<=1 for v in mapped)
  assert sum((mx[j]*d[j] for j in range(7)),Z)==sum((my[i]*mapped[i] for i in range(7)),Z)
  assert sum((R[j]*mx[j]*d[j] for j in range(7)),Z)==sum((R[i]*my[i]*mapped[i] for i in range(7)),Z)

def mix(triples, weights):
 assert all(t>=0 for t in weights) and sum(weights,Z)==1,weights
 x=tuple(sum((w*tri[0][k] for tri,w in zip(triples,weights)),Z) for k in range(7))
 y=tuple(sum((w*tri[1][k] for tri,w in zip(triples,weights)),Z) for k in range(7))
 Q=tuple(tuple(sum((w*tri[2][i][j] for tri,w in zip(triples,weights)),Z) for j in range(7)) for i in range(7))
 return x,y,Q

def load(path):
 d=json.loads(Path(path).read_text())
 assert d['ratio_interval']==['33/1000','1/30']
 assert d['scientific_input_pins']=={'global':'a01383f825ef9d43b4b754254303298c64041568','em':'86149263e38c22292c9def1e0f69092efa1be77e'}
 cert={}
 for c in d['certificates']:
  k=(F(c['eta']),c['face'],F(c['theta']),F(c['p']),F(c['q']))
  assert k not in cert
  x=source(k[2],k[3],k[4],k[0]);y=tuple(map(F,c['target']))
  Q=[[Z]*7 for _ in range(7)]
  for i,j,val in c['edges']:
   assert Q[i][j]==0
   Q[i][j]=F(val)
  tri=(x,y,tuple(tuple(row) for row in Q))
  check(*tri,face=c['face'])
  cert[k]=tri
 assert len(cert)==26
 return cert

def full_prism(cert,eta,theta,p,q,s=O,g=O,h=Z):
 assert ETA0<=eta<=ETA1
 ratio_weight=(eta-ETA0)/(ETA1-ETA0)
 def bracket(face,t,a,b):
  return mix([cert[(ETA0,face,t,a,b)],cert[(ETA1,face,t,a,b)]],[1-ratio_weight,ratio_weight])
 assert 0<=theta<=1 and 0<=p<=1 and 0<=q<=1 and 0<=h<=1 and 0<=s<=g<=1
 if theta<=F(1,2):
  face='G' if q<=p else 'F'
  if face=='G':
   vertices=[(Z,Z),(O,Z),(O,O)]
   weights=[1-p,p-q,q]
  else:
   vertices=[(Z,Z),(Z,O),(O,O)]
   weights=[1-q,q-p,p]
  w_theta=2*theta
  triples=[mix([bracket(face,Z,a,b),bracket(face,F(1,2),a,b)],[1-w_theta,w_theta]) for a,b in vertices]
  tri=mix(triples,weights)
 else:
  face='F'
  w_theta=2*theta-1
  vertices=[(Z,Z),(Z,O),(O,Z),(O,O)]
  weights=[(1-p)*(1-q),(1-p)*q,p*(1-q),p*q]
  triples=[]
  for a,b in vertices:
   low=bracket(face,F(1,2),a,b)
   identity=source(O,a,b,eta)
   high=(identity,identity,diag(identity))
   triples.append(mix([low,high],[1-w_theta,w_theta]))
  tri=mix(triples,weights)
 E1=(O,Z,Z,Z,Z,Z,Z)
 E0=(Z,Z,Z,Z,Z,Z,Z)
 scaled=mix([tri,(E1,E1,diag(E1)),(E0,E0,diag(E0))],[s,g-s,1-g])
 x,y,Q=scaled
 xh=tuple((1-h)*x[i]+h*y[i] for i in range(7))
 Qh=tuple(tuple((1-h)*Q[i][j]+(h*mass(y)[i] if i==j else Z) for j in range(7)) for i in range(7))
 direct=(g,s,s*eta,s*(F(13,40)+eta/80)*p,
         s*(F(9,40)*eta+theta/10),
         s*(F(3,40)+F(21,80)*eta)*q,s*theta/10)
 assert x==direct,('source mismatch',x,direct)
 check(xh,y,Qh,face)
 return xh,y,Qh

def main():
 c=load(Path(__file__).with_name('CERTIFICATES.json'))
 print('EXACT_ANCHOR_PASS',len(c),'SPARSE_EDGES',sum(sum(t>0 for row in tri[2] for t in row) for tri in c.values()))
 total=0
 points=tuple(map(F,['0','1/7','1/4','1/2','3/4','6/7','1']))
 for eta,theta,p,q in product((ETA0,F(1,30),F(199,6000),ETA1),points,points,points):
  full_prism(c,eta,theta,p,q)
  total+=1
 t=tuple(map(F,['0','1/3','2/3','1']))
 for eta,theta,p,q,s,g,h in product((ETA0,F(199,6000),ETA1),t,t,t,t,t,t):
  if s>g:continue
  full_prism(c,eta,theta,p,q,s,g,h)
  total+=1
 print('EXACT_GLUE_REGRESSION_PASS',total)
 print('PASS_R5_MIDDLE_ETA_INTERVAL_COMPLETE_PHYSICAL_PRISM_ALL_REAL_CONSTRUCTION')

if __name__=='__main__':main()
