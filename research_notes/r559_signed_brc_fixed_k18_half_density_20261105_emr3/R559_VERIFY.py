#!/usr/bin/env python3
"""R559 k=18: numerical centers are candidates only; all accepting tests are exact Fraction arithmetic."""
from fractions import Fraction as F
from math import comb,lcm
import sympy as S
K=18; d=35; eps=F(1,10**22)
def C(k):return comb(2*k,k)//(k+1)
def H(t):
 r=2*K+1
 if not 2<=t<=r:return 0
 return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*C(K-q) for q in range(min(K,(t-1)//2)+1))
def Hraw(t):
 r=2*K+1
 if not 2<=t<=r:return 0
 return comb(r+t,2*t)*sum(comb(r-t,q)*((comb(2*t,r-2*q) if 0<=r-2*q<=2*t else 0)-(comb(2*t,r-2*q-1) if 0<=r-2*q-1<=2*t else 0)) for q in range(r-t+1))
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def norm2(a):return a[0]*a[0]+a[1]*a[1]
def up(a):return abs(a[0])+abs(a[1])
def low(a):return max(abs(a[0]),abs(a[1]))
def atan(x,n):
 assert 0<=x<1
 y=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(n)),F(0));e=x**(2*n+1)/F(2*n+1)
 return y-e,y+e
def signedatan(x,n):
 if x>=0:return atan(x,n)
 l,h=atan(-x,n);return -h,-l
assert C(K)==477638700 and all(H(t)==Hraw(t) for t in range(2,38))
h=H(2);assert h==39286260713700
a=[(-1)**(j-1)*F(H(j+2),h) for j in range(1,d+1)]
f=[F(1)]+[-v for v in a];L=lcm(*(v.denominator for v in f));P=[int(v*L) for v in f]
x=S.symbols('x');rr=S.nroots(S.Poly.from_list(P,gens=x),n=65,maxsteps=500)
rr=sorted(rr,key=lambda z:(-float(S.Abs(z)),-float(S.im(z))))
cc=[(F(str(S.re(z))),F('0') if abs(float(S.im(z)))<1e-55 else F(str(S.im(z)))) for z in rr]
assert len(cc)==d and cc[0][0]==cc[1][0] and cc[0][1]==-cc[1][1] and cc[0][1]>0
rat=[]
for k,c in enumerate(cc):
 v=[]
 for p in P:
  w=[(F(p),F(0))]+[(F(0),F(0))]*len(v)
  for j,z in enumerate(v):w[j]=add(w[j],mul(c,z));w[j+1]=add(w[j+1],z)
  v=w
 lhs=low(v[1])*eps;rhs=up(v[0])+sum((up(v[j])*eps**j for j in range(2,d+1)),F(0))
 assert lhs>rhs,('Rouche',k)
 rat.append(rhs/lhs)
assert all(norm2((cc[i][0]-cc[j][0],cc[i][1]-cc[j][1]))>4*eps**2 for i in range(d) for j in range(i+1,d))
assert norm2(cc[0])>(30+eps)**2 and all(norm2(c)<(11-eps)**2 for c in cc[2:]) and max(rat)<F(1,1000)
print('R559_K18_ROUCHE_PASS 35 disks 595 pairs dominant>30 others<11',flush=True)
re,im=cc[0];r0=(re-eps)/(im+eps);r1=(re+eps)/(im-eps)
assert F(7,10)<r0<r1<F(4,5)
t0=(4*r0-3)/(4+3*r0);t1=(4*r1-3)/(4+3*r1)
assert -F(1,20)<t0<t1<F(1,20)
A,B=atan(F(1,3),65);tl,_=signedatan(t0,30);_,th=signedatan(t1,30)
L5,U5=atan(F(1,5),65);L239,U239=atan(F(1,239),25)
pi0=16*L5-4*U239;pi1=16*U5-4*L239
lo=(pi0/2-2*B-th)/pi1;hi=(pi1/2-2*A-tl)/pi0
assert F(1,4)<lo<hi<F(1,3) and hi-lo<F(1,10**18)
lim=d*(d-1);qmax=2*lim**2
phi=list(range(qmax+1))
for i in range(2,qmax+1):
 if phi[i]==i:
  for j in range(i,qmax+1,i):phi[j]-=phi[j]//i
count=0
for q in range(2,qmax+1):
 if phi[q]>lim:continue
 count+=1
 assert -(-q*lo.numerator//lo.denominator)>q*hi.numerator//hi.denominator,('torsion',q)
print('R559_K18_PHASE_PASS phi<=%d q<=%d candidates=%d'%(lim,qmax,count),flush=True)
b=[(-1)**(j-1)*H(j+2)*h**(j-1) for j in range(1,d+1)];vv=[1]
for m in range(1,1025):vv.append(sum(b[j-1]*vv[m-j] for j in range(1,min(d,m)+1)))
for m in range(1,13):
 assert S.Matrix([[Hraw(3+i-j) for j in range(m)] for i in range(m)]).det(method='berkowitz')==vv[m]
print('R559_K18_RECURRENCE_PASS',sum(v>0 for v in vv),sum(v<0 for v in vv),sum(v==0 for v in vv),sum(vv[j]*vv[j-1]<0 for j in range(1,len(vv))),'raw_det=12',flush=True)
print('R559_K18_HALF_DENSITY_AUTHOR_CERT_PASS',flush=True)
