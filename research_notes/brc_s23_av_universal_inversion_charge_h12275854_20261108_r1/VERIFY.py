#!/usr/bin/env python3
"""Exact certificate: universal inversion-charge ranks and S23/AV four-direction window."""
from fractions import Fraction as F
lo,hi=(F(i,10**26) for i in (545569623581288298975349314,545569623581288298975349315))
def logbounds(x):
 s=sum((x**(2*k+1)/F(2*k+1) for k in range(45)),F())
 return 2*s,2*(s+x**91/(91*(1-x*x)))
a,b=logbounds(F(1,3));c,d=logbounds(F(1,15));e,f=logbounds(F(3,17))
assert lo < (3*a-d)/f < (3*b-c)/e < hi
u=(79,431);w=(380295,2074774);M=sum(w)
assert u[0]*w[1]-u[1]*w[0]==1
for r in (lo,hi):
 eps,eta=79*r-431,w[1]-w[0]*r
 assert 0<eta<eps<2*eta and 2*eps>3*eta

def plus(x,y):return x[0]+y[0],x[1]+y[1]
def minus(x,y):return x[0]-y[0],x[1]-y[1]
def scale(n,x):return n*x[0],n*x[1]
def inside(x,H):return min(x)>=0 and sum(x)<=H
def vectors(H,u,w,eps,eta):
 return [(A,B,plus(scale(A,u),scale(B,w))) for B in range(1,H//sum(w)+1) for A in range(1,(H-B*sum(w))//sum(u)+1) if A*eps < B*eta]
def charge(p,H,ds):return sum(int(inside(plus(p,d),H))-int(inside(minus(p,d),H)) for d in ds)
# Complete independent comparison of full integer-key order with actual threshold order.
ut,wt,rt=(1,1),(2,3),F(61,44);eps,eta=rt-1,3-2*rt
assert F(3,2)<eps/eta<2
checked=0
for H in range(36):
 pts=[(v,j) for v in range(H+1) for j in range(H-v+1)]
 lex=sorted(pts,key=lambda p:(3*p[0]-2*p[1],-p[0]))
 true=sorted(pts,key=lambda p:rt*p[0]-p[1]);ranks={p:i for i,p in enumerate(true)}
 dd=[v for _,_,v in vectors(H,ut,wt,eps,eta)]
 for i,p in enumerate(lex):assert i+charge(p,H,dd)==ranks[p];checked+=1
 tri=lambda k:(k+1)*(k+2)//2
 inversions=sum(tri(H-sum(v)) for v in dd)
 brute=sum((rt*p[0]-p[1])>(rt*q[0]-q[1]) for i,p in enumerate(lex) for q in lex[i+1:])
 assert inversions==brute
print('PASS_EXHAUSTIVE_RANK_AND_INVERSION_COUNT_H0_TO_35',checked)
q=lambda A,B:plus(scale(A,u),scale(B,w))
H0,H1,H2,H3,H4=(sum(q(A,B)) for A,B in ((1,2),(1,3),(1,4),(2,4),(1,5)))
assert (H0,H1,H2,H3,H4)==(4910648,7365717,9820786,9821296,12275855)
for H,expected in ((H2-1,[(1,2),(1,3)]),(H2,[(1,2),(1,3),(1,4)]),(H3-1,[(1,2),(1,3),(1,4)]),(H3,[(1,2),(1,3),(1,4),(2,4)]),(H4-1,[(1,2),(1,3),(1,4),(2,4)])):
 a=vectors(H,u,w,79*lo-431,w[1]-w[0]*lo)
 b=vectors(H,u,w,79*hi-431,w[1]-w[0]*hi)
 assert [(A,B) for A,B,_ in a]==[(A,B) for A,B,_ in b]==expected
 tri=lambda k:(k+1)*(k+2)//2
 pairs=sum(tri(H-sum(d)) for _,_,d in a)
 print('H',H,'DIRECTIONS',expected,'INVERTED_PAIRS',pairs)
print('PASS_S23_AV_EXACT_RANK_SELECT_THROUGH_H12275854')
