#!/usr/bin/env python3
"""Independent exact verifier for R5 positive-residual theta extension.
Needs R5_CERTIFICATES.json in same directory. Python standard library only.
No numerical optimizer is imported or used for verification.
"""
import json, base64, zlib
from fractions import Fraction as F
from itertools import product
from pathlib import Path
R = (F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
TAU=F(4,5)
KAPPA=F(3,4)

def mass(f):
 g,a,b,u,v,w,z=f
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
         F(13,40)*a+b/80-u,(g-a)/2,
         1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
         (g-b)/2,F(3,40)*a+F(21,80)*b-w,
         u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def tp(f):
 g,a,b,u,v,w,z=f
 return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w

def tq(f):
 g,a,b,u,v,w,z=f
 return 1+g+(a+b)/2+u+v+w

def source(t,p,q,theta):
 return (F(1),t,F(1),(F(13,40)*t+F(1,80))*p,t*theta/10+F(27,160),(F(3,40)*t+F(21,80))*q,t*theta/10)

def target(y):
 g,a,b,u,w=y;z=TAU*a/10
 return (g,a,b,u,z+F(9,40)*TAU*b,w,z)

def check(x,y,Q):
 g,a,b,u,v,w,z=y
 assert 0<=a<=g<=1 and 0<=b<=g
 assert 0<=u<=F(13,40)*a+b/80
 assert 0<=w<=F(3,40)*a+F(21,80)*b
 assert z==TAU*a/10 and v-z==F(9,40)*TAU*b
 assert 9*b*z==4*a*(v-z)
 mx,my=mass(x),mass(y)
 assert all(v>=0 for v in mx+my) and all(v>=0 for v in Q.values())
 assert sum(mx)==sum(my)==1
 assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==1
 for i in range(7):
  assert sum(Q.get((i,j),F(0)) for j in range(7))==my[i]
 for j in range(7):
  assert sum(Q.get((i,j),F(0)) for i in range(7))==mx[j]
  assert sum(R[i]*Q.get((i,j),F(0)) for i in range(7))==R[j]*mx[j]
 assert tp(x)==tp(y) and tq(x)==tq(y)

def load():
 raw=json.loads(zlib.decompress(base64.b64decode(Path(__file__).with_name('CERTIFICATES.zlib.b64').read_text())).decode())
 data={}
 for k,rec in raw.items():
  t,p,q,theta=map(F,k.split('|'))
  y=tuple(map(F,rec['target']))
  Q={tuple(map(int,pair.split(','))):F(v) for pair,v in rec['edges'].items()}
  data[(t,p,q,theta)]=(y,Q)
 return data

def main():
 vertices=load()
 assert len(vertices)==16
 edgecount=0
 for coord,(yv,Q) in vertices.items():
  t,p,q,theta=coord
  check(source(t,p,q,theta),target(yv),Q)
  edgecount+=len(Q)
 print('EXACT_16_ENDPOINT_CERTIFICATES_PASS',edgecount)
 for k in range(601):
  t=F(1,100)+(F(1,5)-F(1,100))*F(k,600)
  p=F((7*k+13)%601,601)
  q=F((11*k+29)%601,601)
  theta=F(3,4)+F(1,4)*F((17*k+23)%601,601)
  a=(t-F(1,100))/(F(1,5)-F(1,100)); b=4*(theta-F(3,4))
  weights={coord:(a if coord[0]==F(1,5) else 1-a)*
             (p if coord[1] else 1-p)*
             (q if coord[2] else 1-q)*
             (b if coord[3]==F(1) else 1-b)
           for coord in vertices}
  assert sum(weights.values())==1 and min(weights.values())>=0
  x=source(t,p,q,theta)
  for z in range(7):
   assert sum(weights[coord]*source(*coord)[z] for coord in vertices)==x[z]
  yv=tuple(sum(weights[coord]*vertices[coord][0][i] for coord in vertices) for i in range(5))
  Q={(i,j):sum(weights[coord]*vertices[coord][1].get((i,j),F(0)) for coord in vertices)
     for i in range(7) for j in range(7)}
  check(x,target(yv),Q)
 print('EXACT_601_MULTIAFFINE_INTERIOR_CHECKS_PASS')
 print('ALL_REAL_PRISM_PROOF_VIA_NONNEGATIVE_16_VERTEX_MULTIAFFINE_INTERPOLATION')
 print('DOMAIN: 1/100 <= t <= 1/5; 0 <= p,q <= 1; 3/4 <= theta <= 1; kappa=3/4')
 print('SOURCE_SEEDLESS_INTERPOLANT_FOLLOW_BY_DIAGONAL_KERNEL_MIXTURE')
if __name__=='__main__':main()
