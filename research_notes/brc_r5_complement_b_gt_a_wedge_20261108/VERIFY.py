#!/usr/bin/env python3
"""Exact R5 seven-node Blackwell certificate checker. Standard library only."""
import json, random, pathlib, base64, zlib
from fractions import Fraction as F
from itertools import product

R=tuple(map(F,('1/10','1/2','3/4','1','5/4','3/2','19/10')))
PATH=pathlib.Path(__file__).with_name('CERTIFICATES.json.zlib.b64')
D=json.loads(zlib.decompress(base64.b64decode(PATH.read_text())).decode())

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

def lawful(f):
 g,a,b,u,v,w,z=f
 return (0<=g<=1 and 0<=a<=g and 0<=b<=g and
  0<=u<=F(13,40)*a+b/80 and
  0<=w<=F(3,40)*a+F(21,80)*b and
  0<=z<=a/10 and 0<=v-z<=F(9,40)*b and
  all(m>=0 for m in mass(f)))

def src(g,a,b,theta,kappa,p,q):
 return (g,a,b,(F(13,40)*a+b/80)*p,
  a*theta/10+F(9,40)*b*kappa,
  (F(3,40)*a+F(21,80)*b)*q,a*theta/10)

def check(x,y,Q):
 assert lawful(x) and lawful(y)
 assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])
 assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
 assert len(Q)==7 and all(len(row)==7 for row in Q)
 assert all(v>=0 for row in Q for v in row)
 mx,my=mass(x),mass(y)
 assert sum(mx)==sum(my)==1
 assert sum(r*m for r,m in zip(R,mx))==sum(r*m for r,m in zip(R,my))==1
 assert all(sum(Q[i])==my[i] for i in range(7))
 assert all(sum(Q[i][j] for i in range(7))==mx[j] for j in range(7))
 assert all(sum(R[i]*Q[i][j] for i in range(7))==R[j]*mx[j] for j in range(7))
 assert tp(x)==tp(y) and tq(x)==tq(y)

C={}
for e in D['certificates']:
 key=(F(e['a']),e['theta'],e['kappa'],e['p'],e['q'])
 assert key not in C
 a,th,ka,p,q=key
 x=src(F(1),a,F(1),F(th),F(ka),F(p),F(q))
 y=tuple(F(v) for v in e['y'])
 Q=[[F(0) for j in range(7)] for i in range(7)]
 for i,j,v in e['Q']:
  assert Q[i][j]==0
  Q[i][j]=F(v)
 Q=tuple(tuple(row) for row in Q)
 check(x,y,Q)
 C[key]=(x,y,Q)
assert set(C)=={(a,th,ka,p,q) for a in (F(1,5),F(1)) for th,ka,p,q in product((0,1),repeat=4)}
print('EXACT_32_F_FACE_CORNER_CERTIFICATES_PASS')

def mix(triples,weights):
 assert len(triples)==len(weights) and sum(weights)==1 and all(w>=0 for w in weights)
 xs,ys,qs=zip(*triples)
 return (tuple(sum(w*x[i] for x,w in zip(xs,weights)) for i in range(7)),
  tuple(sum(w*y[i] for y,w in zip(ys,weights)) for i in range(7)),
  tuple(tuple(sum(w*Q[i][j] for Q,w in zip(qs,weights)) for j in range(7)) for i in range(7)))

def identity(f):
 m=mass(f)
 return (f,f,tuple(tuple(m[i] if i==j else F(0) for j in range(7)) for i in range(7)))

def lift(g,s,xi,theta,kappa,p,q,h):
 assert 0<=s<=g<=1 and F(1,5)<=xi<=1 and all(0<=v<=1 for v in (theta,kappa,p,q,h))
 def at_a(a):
  terms=[];wt=[]
  for th,ka,pp,qq in product((0,1),repeat=4):
   ww=(theta if th else 1-theta)*(kappa if ka else 1-kappa)*(p if pp else 1-p)*(q if qq else 1-q)
   if ww:terms.append(C[(a,th,ka,pp,qq)]);wt.append(ww)
  return mix(terms,wt)
 lam=(xi-F(1,5))/(1-F(1,5))
 middle=mix([at_a(F(1,5)),at_a(F(1))],[1-lam,lam])
 E1=identity(src(F(1),F(0),F(0),F(0),F(0),F(0),F(0)))
 E0=identity(src(F(0),F(0),F(0),F(0),F(0),F(0),F(0)))
 x,y,Q=mix([middle,E1,E0],[s,g-s,1-g])
 assert x==src(g,s*xi,s,theta,kappa,p,q)
 xh,y,Qh=mix([(x,y,Q),identity(y)],[1-h,h])
 check(xh,y,Qh)
 return x,y,Q

rng=random.Random(20261108)
for k in range(256):
 vals=[F(rng.randint(0,16),16) for _ in range(7)]
 g=vals[0];s=g*vals[1];xi=F(1,5)+F(4,5)*vals[2]
 lift(g,s,xi,*vals[3:7],F((k*37)%101,101))
lift(F(9,10),F(4,5),F(3,5),F(2,7),F(5,7),F(3,8),F(7,9),F(2,3))
print('EXACT_257_ALL_REAL_INTERPOLATION_REGRESSION_PASS')
print('PASS_R5_COMPLEMENT_B_GT_A_FULL_F_FACE_PHYSICAL_WEDGE')
