#!/usr/bin/env python3
"""R570 k=29: exact rational Rouche disks and bounded-denominator phase exclusion.
Frozen signed-BRC auxiliary Toeplitz-Hessenberg scalar source R462 commit
18783e01e3646c72b7aab3b16d3f565e83e6446f; R569 author-side continuation
2279846fb5743b64b2da4c50d8c601c49f824ee9.
Numerical nroots only proposes rational centers; all accepting inequalities exact.
"""
from fractions import Fraction as F
from math import comb, lcm
import platform, sympy as S

K=29
r=2*K+1
d=2*K-1
eps=F(1,10**22)
C=lambda j: comb(2*j,j)//(j+1)
def choose(n,j): return comb(n,j) if 0<=j<=n else 0
def H(t):
    if not 2<=t<=r: return 0
    return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*C(K-q) for q in range(min(K,(t-1)//2)+1))
def raw(t):
    if not 2<=t<=r: return 0
    return comb(r+t,2*t)*sum(comb(r-t,q)*(choose(2*t,r-2*q)-choose(2*t,r-2*q-1)) for q in range(r-t+1))
def add(a,b): return a[0]+b[0],a[1]+b[1]
def mul(a,b): return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def n2(a): return a[0]**2+a[1]**2
def up(a): return abs(a[0])+abs(a[1])
def low(a): return max(abs(a[0]),abs(a[1]))
def atan_interval(x,n):
    assert F(0)<=x<F(1)
    t=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
    err=x**(2*n+1)/F(2*n+1)
    return t-err,t+err

print('R570_ENV',platform.python_version(),S.__version__,flush=True)
assert all(H(t)==raw(t) for t in range(2,r+1))
print('R570_H_EQ_PASS',r-1,flush=True)
h=H(2)
a=[(-1)**(j-1)*F(H(j+2),h) for j in range(1,d+1)]
fc=[F(1)]+[-v for v in a]
L=lcm(*(v.denominator for v in fc))
P=[int(v*L) for v in fc]
x=S.symbols('x')
print('R570_POLY_DEG',d,'h',h,'L',L,flush=True)
roots=S.nroots(S.Poly.from_list(P,gens=x),n=65,maxsteps=1000)
roots=sorted(roots,key=lambda z:(-float(S.Abs(z)),-float(S.im(z))))
cc=[(F(str(S.re(z))),F(0) if abs(float(S.im(z)))<1e-55 else F(str(S.im(z)))) for z in roots]
assert cc[0][0]==cc[1][0] and cc[0][1]==-cc[1][1] and cc[0][1]>0
rat=[]
for idx,c in enumerate(cc):
    coef=[]
    for p in P:
        w=[(F(p),F(0))]+[(F(0),F(0))]*len(coef)
        for j,z in enumerate(coef):
            w[j]=add(w[j],mul(c,z));w[j+1]=add(w[j+1],z)
        coef=w
    lhs=low(coef[1])*eps
    rhs=up(coef[0])+sum((up(coef[j])*eps**j for j in range(2,d+1)),F(0))
    assert lhs>rhs,('rouche',idx,float(rhs/lhs))
    rat.append(rhs/lhs)
assert all(n2((cc[i][0]-cc[j][0],cc[i][1]-cc[j][1]))>4*eps**2 for i in range(d) for j in range(i+1,d))
assert all(n2(cc[0])>n2(c)+4*eps*(1+sum(map(abs,cc[0]))+sum(map(abs,c))) for c in cc[2:])
assert all(n2(cc[2])>=n2(c) for c in cc[3:])
print('R570_ROUCHE_PASS',d,'disks',d*(d-1)//2,'pairs','dominant',float(S.Abs(roots[0])),'next',float(S.Abs(roots[2])),'max_ratio',float(max(rat)),flush=True)
re,im=cc[0]
r0=(re-eps)/(im+eps)
r1=(re+eps)/(im-eps)
assert F(0)<r0<r1<F(1)
alo=atan_interval(r0,200)[0]
ahi=atan_interval(r1,200)[1]
L5,U5=atan_interval(F(1,5),65)
L239,U239=atan_interval(F(1,239),25)
pi0=16*L5-4*U239
pi1=16*U5-4*L239
lo=(pi0/2-ahi)/pi1
hi=(pi1/2-alo)/pi0
assert F(1,4)<lo<hi<F(1,3)
lim=d*(d-1)
qmax=2*lim**2
assert hi-lo<F(1,qmax*qmax)
cf=((lo+hi)/2).limit_denominator(qmax)
assert cf<=lo or cf>=hi
print('R570_CF_PHASE_EXCLUSION_PASS','max_denominator',qmax,'nearest_num',cf.numerator,'nearest_den',cf.denominator,'nearest_in_interval',lo<cf<hi,flush=True)
print('R570_PHASE_PASS','phi_bound',lim,'q_bound',qmax,'theta_over_pi',float((lo+hi)/2),'width',float(hi-lo),flush=True)
b=[(-1)**(j-1)*H(j+2)*h**(j-1) for j in range(1,d+1)]
v=[1]
for m in range(1,1025):
    v.append(sum(b[j-1]*v[m-j] for j in range(1,min(d,m)+1)))
for m in range(1,13):
    assert S.Matrix([[raw(3+i-j) for j in range(m)] for i in range(m)]).det(method='bareiss')==v[m]
print('R570_RECURRENCE_PASS','positive',sum(z>0 for z in v),'negative',sum(z<0 for z in v),'zeros',sum(z==0 for z in v),'sign_changes',sum(v[j]*v[j-1]<0 for j in range(1,len(v))),'raw_determinants',12,flush=True)
print('R570_K29_HALF_DENSITY_AUTHOR_CERT_PASS',flush=True)
