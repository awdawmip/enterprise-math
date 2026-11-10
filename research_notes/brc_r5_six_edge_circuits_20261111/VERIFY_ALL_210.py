#!/usr/bin/env python3
"""Frozen R5 exact 30-arc positive physical point and all 210 residual circuit directions.
Requires adjacent WITNESS.txt; computed with Fraction, rank with exact SymPy.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from sympy import Matrix, Rational

r=tuple(map(F,('1/10','1/2','3/4','1','5/4','3/2','19/10')))
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if (j not in (0,6) or i==j))
assert len(D)==30

def mass(x):
 g,a,b,u,v,w,z=x
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
         F(13,40)*a+b/80-u,(g-a)/2,
         1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
         (g-b)/2,F(3,40)*a+F(21,80)*b-w,
         u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(x):
 g,a,b,u,v,w,z=x
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
         1+g+(a+b)/2+u+v+w)
def slacks(x):
 g,a,b,u,v,w,z=x
 return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
         w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def q21(x,y):
 m,n=mass(y),mass(x)
 return m+n+tuple(r[j]*n[j] for j in range(7))
def coupling21(e):
 q=[F(0)]*21
 for (i,j),v in e.items():
  q[i]+=v;q[7+j]+=v;q[14+j]+=r[i]*v
 return tuple(q)
def col(i,j):
 a=[F(0)]*21
 a[i]=1;a[7+j]=1;a[14+j]=r[i]-r[j]
 return a

data=dict(line.split('=',1) for line in Path(__file__).with_name('WITNESS.txt').read_text().splitlines())
p=tuple(map(F,data['PHYS'].split(',')))
x,y=p[:7],p[7:]
e=dict(zip(D,map(F,data['ARCS'].split(','))))
m=F(data['MARGIN'])
assert len(p)==14 and len(e)==30 and m>0
assert x[0]==x[2] and y[0]==1 and y[6]==y[1]/10 and times(x)==times(y)
assert len(slacks(x)+slacks(y))==26 and all(t>=0 for t in slacks(x)+slacks(y))
assert all(v>=m for v in e.values()) and min(e.values())==m
assert all(v>=0 for v in mass(x)+mass(y)) and sum(mass(x))==sum(mass(y))==1
assert mass(x)[4]==0 # source port 4 is unavailable
assert coupling21(e)==q21(x,y)
assert sum(e.values())==1
C=Matrix.hstack(*(Matrix([Rational(v.numerator,v.denominator) for v in col(*arc)]) for arc in D))
assert C.shape==(21,30) and C.rank()==15
# Every K_{2,3} circuit can be perturbed at the same strictly physical x,y.
eps=m/4
count=0
for ja,jb in combinations((1,2,3,5),2):
 for target in combinations(range(7),3):
  a,b,c=target
  h=(r[b]-r[c],r[c]-r[a],r[a]-r[b])
  delta={(i,ja):v for i,v in zip(target,h)}
  delta.update({(i,jb):-v for i,v in zip(target,h)})
  assert len(delta)==6 and all(v!=0 for v in delta.values())
  plus={arc:base+eps*delta.get(arc,0) for arc,base in e.items()}
  minus={arc:base-eps*delta.get(arc,0) for arc,base in e.items()}
  assert all(v>0 for v in plus.values()) and all(v>0 for v in minus.values())
  assert plus!=minus and coupling21(plus)==coupling21(minus)==q21(x,y)
  count+=1
assert count==210
print('FROZEN_R5_ORIGINAL_PHYSICAL_EQUALITIES',5,'PASS')
print('FROZEN_R5_ORIGINAL_CAPACITY_SLACKS',26,'ALL_NONNEGATIVE')
print('FROZEN_R5_ORIGINAL_BLACKWELL_EQUATIONS',21,'PASS')
print('ALLOWED_ARCS',len(D),'ALL_STRICTLY_POSITIVE')
print('MIN_ARC_MASS',m)
print('OBSERVER_EXACT_RANK',C.rank(),'NULLITY',30-C.rank())
print('COMMON_CIRCUIT_PERTURBATION_EPSILON',eps)
print('PHYSICALLY_REALIZABLE_MINIMAL_CIRCUIT_TYPES',count)
print('PASS_EXACT_PHYSICAL_15D_OBSERVER_FIBER_AND_210_CIRCUITS')
