#!/usr/bin/env python3
"""Exact arithmetic check of the S23/AV four-point reorder theorem."""
from fractions import Fraction as F
lo=F(545569623581288298975349314,10**26)
hi=F(545569623581288298975349315,10**26)
def logs(x):
 s=sum((x**(2*i+1)/F(2*i+1) for i in range(45)),F())
 return 2*s,2*(s+x**91/(F(91)*(1-x*x)))
a,b=logs(F(1,3));c,d=logs(F(1,15));e,f=logs(F(3,17))
assert lo<(3*a-d)/f<(3*b-c)/e<hi
P,D=2074774,380295;u=(79,431);w=(D,P);M=P+D
q2=(u[0]+2*D,u[1]+2*P);q3=(u[0]+3*D,u[1]+3*P)
h0=sum(q2);h1=sum(q3);h2=sum(u)+4*M
assert (M,h0,h1,h2)==(2455069,4910648,7365717,9820786)
for r in (lo,hi):
 eps=79*r-431;eta=P-D*r
 assert 0<eta<eps<2*eta and 2*eps>3*eta
# Feasible discrepancies with A>0,B>0 through the last horizon.
negative=[]
for B in range(1,(h2-1)//M+1):
 for A in range(1,(h2-1-M*B)//510+1):
  if all(A*(79*r-431)-B*(P-D*r)<0 for r in (lo,hi)):
   negative.append((A,B))
assert negative==[(1,2),(1,3)]
print('PASS_RATIONAL_INVERSION_CLASSES',negative)

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def inside(p,h):return min(p)>=0 and sum(p)<=h

def correction(p,h,u,w):
 q=add(u,(2*w[0],2*w[1]));q3=add(q,w)
 h0=sum(q);h1=sum(q3)
 if h<h0:return p
 s=h-h0
 if h<h1:
  if inside(p,s):return add(p,q)
  if inside(sub(p,q),s):return sub(p,q)
  return p
 t=h-h1
 if inside(p,t):return add(p,w)
 if inside(sub(p,w),t):return add(p,q)
 if inside(sub(p,q3),t):return sub(p,w)
 if inside(sub(p,q),t):return sub(p,q)
 if inside(p,s):return add(p,q)
 if inside(sub(p,q),s):return sub(p,q)
 return p

# Complete exact small-model oracle for every horizon in the theorem window.
u0=(1,1);w0=(2,3);r=F(61,44)
assert F(3,2)<(r-1)/(3-2*r)<2
for h in range(22):
 S=[(v,j) for v in range(h+1) for j in range(h-v+1)]
 L=sorted(S,key=lambda p:(3*p[0]-2*p[1],-p[0]))
 T=sorted(S,key=lambda p:r*p[0]-p[1])
 assert [correction(p,h,u0,w0) for p in L]==T,h
print('PASS_EXHAUSTIVE_SCALED_MODEL_H_0_TO_21')

# Actual giant H: certify each four-point adjacent pair of integer-key fibers.
for H in (h1,h1+1,h1+510,h2-1):
 t=H-h1;s=H-h0
 count=lambda n:(n+1)*(n+2)//2
 assert count(s)>=2*count(t)
 for y in {(0,0),(min(1,t),0),(0,min(1,t)),(t,0),(0,t)}:
  A=add(y,w);B=y;C=add(y,q3);E=add(y,q2)
  assert inside(C,H)
  assert [correction(p,H,u,w) for p in (A,B,C,E)]==[C,A,E,B]
  for rr in (lo,hi):assert rr*C[0]-C[1]<rr*A[0]-A[1]<rr*E[0]-E[1]<rr*B[0]-B[1]
 print('H',H,'BLOCKS',count(t),'ISOLATED_SWAPS',count(s)-2*count(t),'INVERSIONS',count(s)+count(t))
print('PASS_S23_AV_FOUR_POINT_ROTATION_H7365717_TO_H9820785')
