#!/usr/bin/env python3
"""PREFIX352: exact static auxiliary five-port no-source certificate."""
from fractions import Fraction as Q
from math import isqrt
from itertools import product

A=[[(4,0),(4,0),(0,0)],[(0,0),(-4,0),(4,0)],[(-5,3),(0,0),(-3,1)],[(-2,-2),(4,4),(2,2)],[(-2,0),(0,0),(5,2)]]
s=[(4,0),(5,-2),(7,-4)]
q0=[Q(2125,3721),Q(200,3721),Q(29125,29768),Q(5825,7442),Q(31525,59536)]
q1=[Q(4),Q(1),Q(1),Q(1),Q(1)]
b=[(-5,-9),(-3,-7),(0,-8),(2,0)]
beta=[(Q(46,53),Q(61,212)),(Q(19,212),-Q(13,212)),(Q(245,424),-Q(123,424))]
K=[Q(37577,44944*58),Q(530,44944*64),Q(75154,179776*4)]
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x):return (x[0],-x[1])
def summ(xs):
 z=(0,0)
 for x in xs:z=add(z,x)
 return z
def divide(x,y):
 d=y[0]**2+y[1]**2
 return ((x[0]*y[0]+x[1]*y[1])/d,(x[1]*y[0]-x[0]*y[1])/d)
def q(t):return [(1-t)*u+t*v for u,v in zip(q0,q1)]
B=10**18
def sqrt_bounds(v):
 assert v>=0
 n=isqrt((v.numerator*B*B)//v.denominator)
 lo,hi=Q(n,B),Q(n+1,B)
 assert lo*lo<=v<hi*hi
 return lo,hi

# Ordered source/port provenance, exact Gaussian identities.
raw=[];count=0
for j in range(5):
 z=[mul(A[j][k],s[k]) for k in range(3)]
 u=summ(mul(z[k],conj(z[l])) for k,l in product(range(3),repeat=2))
 assert u[1]==0
 raw.append(u[0]);count+=9
assert count==45 and raw==[1360,128,2330,1864,1261]
assert all(q0[j]==Q(10,61)**2*Q(raw[j],64) for j in range(5))
assert all(summ(mul(b[j],A[j][k]) for j in range(4))==(0,0) for k in range(3))
assert all(summ(mul(beta[j],A[j+1][k]) for j in range(3))==A[4][k] for k in range(3))
assert all((beta[i][0]**2+beta[i][1]**2)/(b[i+1][0]**2+b[i+1][1]**2)==K[i] for i in range(3))
assert tuple(424*58*x for x in divide(beta[0],b[1]))==(-1958,2210)
assert tuple(424*8*x for x in divide(beta[1],b[2]))==(26,38)
assert tuple(424*2*x for x in divide(beta[2],b[3]))==(245,-123)
assert all(q1[j]>q0[j] for j in range(5))

# Right tail: g=L1-L2-L3-L4 is increasing on [2/5,1].
assert q1[0]-q0[0]>Q(17,5) and 106*q1[0]<21**2
assert 58*q(Q(2,5))[1]>25 and 64*q(Q(2,5))[2]>49
assert 4*q(Q(2,5))[3]>Q(9,5)**2
assert q1[1]-q0[1]<1 and q1[2]-q0[2]<Q(1,40) and q1[3]-q0[3]<Q(1,4)
gprime_lower=Q(901,105)-Q(29,5)-Q(4,35)-Q(5,18)
assert gprime_lower>0
L=Q(497,1250);R=Q(470271288588,10**12);N=1024
qr=q(R)
gR=sqrt_bounds(106*qr[0])[0]-sum(sqrt_bounds(c*qr[j])[1] for j,c in [(1,58),(2,64),(3,4)])
assert gR>0

# Each rational interval bounds every real t it contains (not sampling).
min_gap=None
for h in range(N):
 l=L+(R-L)*h/N;r=L+(R-L)*(h+1)/N
 ql,qr=q(l),q(r)
 upL=[sqrt_bounds(c*qr[j])[1] for j,c in [(1,58),(2,64),(3,4)]]
 D=sum(upL)-sqrt_bounds(106*ql[0])[0]
 if D<0:continue # polygon obstruction
 S=sum(K[i]*upL[i] for i in range(3))
 al,ah=sqrt_bounds(ql[1]/58)[0],sqrt_bounds(qr[1]/58)[1]
 cl,ch=sqrt_bounds(ql[2])[0],sqrt_bounds(qr[2])[1]
 dl,dh=sqrt_bounds(ql[3])[0],sqrt_bounds(qr[3])[1]
 real_lo=(-1958*ah+26*cl+245*dl)/424
 imag_lo=(2210*al+38*cl-123*dh)/424
 real_hi=(-1958*al+26*ch+245*dh)/424
 imag_hi=(2210*ah+38*ch-123*dl)/424
 assert real_lo>0 and imag_lo>0
 V=sqrt_bounds(real_hi**2+imag_hi**2)[1]
 E=sqrt_bounds(2*D*S)[1]
 gap=ql[4]-(V+E)**2
 assert gap>0,(h,gap)
 if min_gap is None or gap<min_gap:min_gap=gap
assert min_gap is not None
print('PASS_AUTHOR_SIDE_EXACT_FIVE_PORT_STABILITY_EXCLUSION')
print('1024 closed parameter intervals; strict minimum gap:',min_gap)
print('g(R)>0:',gR,'g derivative lower:',gprime_lower)
