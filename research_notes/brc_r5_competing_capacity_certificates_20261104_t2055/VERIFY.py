#!/usr/bin/env python3
"""Integer-exact auxiliary competing-simplex support/hull verifier."""
from itertools import product
from fractions import Fraction as F
ZERO=(0,0); VECTORS=list(product((-1,0,1),repeat=2))
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(points):
 p=sorted(set(points))
 if len(p)<3:return p
 low=[];up=[]
 for q in p:
  while len(low)>=2 and cross(low[-2],low[-1],q)<=0:low.pop()
  low.append(q)
 for q in reversed(p):
  while len(up)>=2 and cross(up[-2],up[-1],q)<=0:up.pop()
  up.append(q)
 return low[:-1]+up[:-1]
def contains(h,p):
 n=len(h)
 if n==1:return h[0]==p
 if n==2:return cross(h[0],h[1],p)==0 and all(min(h[0][j],h[1][j])<=p[j]<=max(h[0][j],h[1][j]) for j in (0,1))
 return all(cross(h[i],h[(i+1)%n],p)>=0 for i in range(n))
def vertices(A,B,C):
 b=(ZERO,)+tuple(B);c=(ZERO,)+tuple(C)
 return b+tuple(plus(A,plus(i,j)) for i in b for j in c),b+tuple(plus(A,plus(i,j)) for i,j in zip(b,c))
def supports(A,B,C,n):
 a=dot(n,A);p=[dot(n,b) for b in B];q=[dot(n,c) for c in C]
 S=max([0]+p);Q=max([0]+q);T=max([0]+[u+v for u,v in zip(p,q)])
 D=S+Q-T;U=a+Q
 assert D>=0
 hF=S+max(0,U);hL=S+max(0,U-D)
 assert hF-hL==min(D,max(0,U))
 return hF,hL,D
N=0;EQUAL=0;DIFFERENT=0;MISMATCH=0
for A,B1,B2,C1,C2 in product(VECTORS,repeat=5):
 Fv,Lv=vertices(A,(B1,B2),(C1,C2))
 lh=hull(Lv)
 same=all(contains(lh,p) for p in Fv)
 for n in ((1,0),(-1,0),(0,1),(0,-1)):
  x,y,_=supports(A,(B1,B2),(C1,C2),n)
  assert x==max(dot(n,v) for v in Fv)
  assert y==max(dot(n,v) for v in Lv)
 N+=1;EQUAL+=same;DIFFERENT+=not same
 MISMATCH+=(same!=(hull(Fv)==lh))
assert N==59049 and MISMATCH==0
A=ZERO;B=((1,0),(0,1));C=((0,1),(1,0));n=(1,-1)
Fv,Lv=vertices(A,B,C)
hF,hL,D=supports(A,B,C,n);W=(2,0)
assert W in Fv and hF==dot(n,W)==2 and hL==1 and D==2 and not contains(hull(Lv),W)
A=(-2,0);B=((1,0),ZERO);C=(ZERO,(1,0))
Fv,Lv=vertices(A,B,C)
assert hull(Fv)==hull(Lv)==[(-2,0),(1,0)]
assert supports(A,B,C,(1,0))==(1,1,1)
assert supports(A,B,C,(-1,0))==(2,2,0)
assert (0,0) in [plus(A,plus(i,j)) for i in (ZERO,)+B for j in (ZERO,)+C]
assert max(plus(A,plus(i,j))[0] for i,j in zip((ZERO,)+B,(ZERO,)+C))==-1
B=((F(1),F(0)),(F(0),F(1)));C=((F(0),F(1)),(F(1),F(0)))
checks=0
for x,y1,y2 in product((F(0),F(1,4),F(1,2),F(3,4),F(1)),repeat=3):
 if y1+y2>1:continue
 z1=x*y1;z2=x*y2
 assert z1+z2<=x
 obs=(y1*B[0][0]+y2*B[1][0]+z1*C[0][0]+z2*C[1][0],
      y1*B[0][1]+y2*B[1][1]+z1*C[0][1]+z2*C[1][1])
 assert obs[0]-obs[1]<=F(1)
 checks+=1
print('EXACT_COMPETING_SIMPLEX_CENSUS',N,EQUAL,DIFFERENT,'mismatches',MISMATCH)
print('STRICT_SEPARATION hF=2 hL=1 gap=1 W=(2,0) dist_inf>=1/2')
print('HIDDEN_LABEL_MISMATCH scalar_hull=[-2,1] x1_F_max=0 x1_L_max=-1')
print('RATIONAL_LR_SAMPLES',checks)
print('PASS_EXACT_R5_COMPETING_SIMPLEX_FINITE_HULL_AND_SUPPORT')
