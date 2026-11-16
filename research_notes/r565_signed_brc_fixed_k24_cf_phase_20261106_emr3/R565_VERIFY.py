#!/usr/bin/env python3
"""R565: k=24 certified root discs and irrational dominant phase for frozen signed BRC auxiliary scalar model.
Source: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f and prior R564@3d67eed1cd2993fc461086cab515e366ad22ee4f.
Root centers from numerical solver are only proposals; acceptance inequalities exact.
"""
from fractions import Fraction as F
from math import comb,lcm
import sys,platform,hashlib
import sympy as S
K=24; d=2*K-1; eps=F(1,10**22); r=2*K+1
C=lambda j: comb(2*j,j)//(j+1)
def H(t):
 if not 2<=t<=r:return 0
 return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*C(K-q) for q in range(min(K,(t-1)//2)+1))
def raw(t):
 if not 2<=t<=r:return 0
 return comb(r+t,2*t)*sum(comb(r-t,q)*((comb(2*t,r-2*q) if 0<=r-2*q<=2*t else 0)-(comb(2*t,r-2*q-1) if 0<=r-2*q-1<=2*t else 0)) for q in range(r-t+1))
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def n2(a):return a[0]**2+a[1]**2
def up(a):return abs(a[0])+abs(a[1])
def low(a):return max(abs(a[0]),abs(a[1]))
def atan(x,n):
 assert 0<=x<1
 y=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(n)),F(0));e=x**(2*n+1)/F(2*n+1)
 return y-e,y+e
print('R565_ENV',platform.python_version(),S.__version__,flush=True)
assert all(H(t)==raw(t) for t in range(2,r+1))
print('R565_H_EQ_PASS',r-1,flush=True)
h=H(2);a=[(-1)**(j-1)*F(H(j+2),h) for j in range(1,d+1)]
f=[F(1)]+[-v for v in a];L=lcm(*(v.denominator for v in f));P=[int(v*L) for v in f]
x=S.symbols('x')
print('R565_POLY_DEG',d,'h',h,'L',L,flush=True)
rr=S.nroots(S.Poly.from_list(P,gens=x),n=65,maxsteps=1000)
rr=sorted(rr,key=lambda z:(-float(S.Abs(z)),-float(S.im(z))))
cc=[(F(str(S.re(z))),F(0) if abs(float(S.im(z)))<1e-55 else F(str(S.im(z)))) for z in rr]
assert cc[0][0]==cc[1][0] and cc[0][1]==-cc[1][1] and cc[0][1]>0
rat=[]
for k,c in enumerate(cc):
 v=[]
 for p in P:
  w=[(F(p),F(0))]+[(F(0),F(0))]*len(v)
  for j,z in enumerate(v):w[j]=add(w[j],mul(c,z));w[j+1]=add(w[j+1],z)
  v=w
 lhs=low(v[1])*eps;rhs=up(v[0])+sum((up(v[j])*eps**j for j in range(2,d+1)),F(0))
 assert lhs>rhs,('rouche',k,float(rhs/lhs))
 rat.append(rhs/lhs)
assert all(n2((cc[i][0]-cc[j][0],cc[i][1]-cc[j][1]))>4*eps**2 for i in range(d) for j in range(i+1,d))
assert all(n2(cc[0])>n2(c)+4*eps*(1+sum(map(abs,cc[0]))+sum(map(abs,c))) for c in cc[2:])
assert all(n2(cc[2])>=n2(c) for c in cc[3:])
assert max(rat)<F(1,1000)
print('R565_ROUCHE_PASS',d,'disks',d*(d-1)//2,'pairs','dominant',float(S.Abs(rr[0])),'next',float(S.Abs(rr[2])),'maximum_ratio',float(max(rat)),flush=True)
re,im=cc[0];r0=(re-eps)/(im+eps);r1=(re+eps)/(im-eps)
assert F(0)<r0<r1<F(1)
A=atan(r0,200)[0];B=atan(r1,200)[1]
L5,U5=atan(F(1,5),65);L239,U239=atan(F(1,239),25)
pi0=16*L5-4*U239;pi1=16*U5-4*L239
lo=(pi0/2-B)/pi1;hi=(pi1/2-A)/pi0
assert F(1,4)<lo<hi<F(1,3) and hi-lo<F(1,10**18)
lim=d*(d-1);qmax=2*lim**2
assert hi-lo < F(1,qmax*qmax)
mid=(lo+hi)/2
candidate=mid.limit_denominator(qmax)
assert candidate<=lo or candidate>=hi
print('R565_CF_PHASE_EXCLUSION_PASS','max_denominator',qmax,'nearest_num',candidate.numerator,'nearest_den',candidate.denominator,'nearest_in_interval',lo<candidate<hi,flush=True)
print('R565_PHASE_PASS','phi_bound',lim,'q_bound',qmax,'theta_over_pi',float((lo+hi)/2),'width',float(hi-lo),flush=True)
b=[(-1)**(j-1)*H(j+2)*h**(j-1) for j in range(1,d+1)];v=[1]
for m in range(1,1025):v.append(sum(b[j-1]*v[m-j] for j in range(1,min(d,m)+1)))
for m in range(1,13):assert S.Matrix([[raw(3+i-j) for j in range(m)] for i in range(m)]).det(method='berkowitz')==v[m]
print('R565_RECURRENCE_PASS','positive',sum(a>0 for a in v),'negative',sum(a<0 for a in v),'zeros',sum(a==0 for a in v),'sign_changes',sum(v[j]*v[j-1]<0 for j in range(1,len(v))),'raw_determinants',12,flush=True)
print('R565_K24_HALF_DENSITY_AUTHOR_CERT_PASS',flush=True)
