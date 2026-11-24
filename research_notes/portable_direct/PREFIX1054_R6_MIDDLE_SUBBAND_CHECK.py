# Exact middle-band certificate; all claim-bearing arithmetic integer/rational.
import sympy as s
from fractions import Fraction as F
from math import prod,comb,lcm,ceil
Y,t,n,z=s.symbols('Y t n z')
a=[-Y**2*(Y-6),-Y**2*(31*Y**2-516*Y+1020),-6*Y**2*(15*Y**3-406*Y**2+2078*Y-1152),-Y**3*(65*Y**3-2408*Y**2+19836*Y-27648),-5*Y**4*(3*Y**3-140*Y**2+1568*Y-3456),-Y**5*(Y-36)*(Y-16)*(Y-4)]
A=[s.Poly(x.subs(Y,16+t),t) for x in a]
def fall(x,k):return prod(x-i for i in range(k))
def pe(p,x):
 v=0
 for a in reversed(p):v=v*x+a
 return v
def rec(r,N):
 w=[s.Poly(s.expand(sum(A[d].nth(k-4+d)*fall(n-k,d) for d in range(6) if k-4+d>=0)*r**k),n) for k in range(8)]
 lim=[-s.LC(x)/s.LC(w[0]) for x in w[1:]]
 assert s.expand(1-sum(lim[k-1]*z**k for k in range(1,8))-(1+F(r,12)*z)*(1+F(r,16)*z)**5*(1-F(r,20)*z))==0
 K=1/((1-F(r,12))*(1-F(r,16))**5*(1-F(r,20)))
 D=s.Poly(w[0].as_expr().subs(n,n+N),n);sg=s.sign(D.LC());D=D.mul_ground(sg);assert all(D.nth(i)>0 for i in range(6))
 e=F(sum(max(abs(d.nth(i))/D.nth(i) for i in range(6)) for d in [s.Poly((-w[k].as_expr()-lim[k-1]*w[0].as_expr()).subs(n,n+N),n).mul_ground(sg) for k in range(1,8)]))
 assert K*e<1
 d=lcm(*(int(c.q) for p in w for c in p.all_coeffs()));p=[[int(x.nth(i)*d) for i in range(6)] for x in w]
 return p,K,F(sum(abs(x) for x in lim))+e,e
# Fixed-point approximation at radius 9; prove rounding residual at radius 5.
r0,N0=5,300;r,N=9,30000
p0,K0,L0,e0=rec(r0,N0);p,K,L,e=rec(r,N)
# In units 1/M the rescaled local rounding residual is <=1 at radius 5.
E=[0]*4
for i in range(4,N0):
 d=abs(pe(p0[0],i)); E.append(1+(sum(abs(pe(p0[k],i))*E[i-k] for k in range(1,min(7,i)+1))+d-1)//d)
E0=max(max(E),ceil(K0*(L0*max(E[-7:])+1)/(1-K0*e0)))
# Bound all finite prefix coefficient errors at radius 9 by delta, uniform across bases.
M=10**10000;delta=F(1,10**100)
assert E0*9**N*10**100 < M*5**N
Dcut=200;ell=F(17,2);q=ell/r
assert q*F(Dcut+2,Dcut+1)<1
# polynomial arithmetic in x=(16-y)/ell
H=s.Poly((Y**2*(36-Y)**2).subs(Y,16-ell*t),t)
Hp=s.Poly(s.diff(Y**2*(36-Y)**2,Y).subs(Y,16-ell*t),t)
P=s.Poly((Y*(Y-36)*(17*Y-91)).subs(Y,16-ell*t),t)
def polylist(p):return [F(p.nth(i)) for i in range(p.degree()+1)]
def add(*xs):return [sum((a[i] if i<len(a) else 0) for a in xs) for i in range(max(map(len,xs)))]
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def sc(a,k):return [x*k for x in a]
def contrast(f):
 df=[-F(i,1)/ell*f[i] for i in range(1,len(f))]
 integ=mul([F(10),-ell],f);v=[F(0)]+[-ell*x/(i+1) for i,x in enumerate(integ)]
 return add(sc(mul(polylist(Hp),f),4),sc(mul(polylist(H),df),4),sc(mul(polylist(P),f),-2),sc(mul([F(27),-ell],v),12))
def bern(a):
 d=len(a)-1; den=lcm(*(x.denominator for x in a)); C=[comb(d,i) for i in range(d+1)];cd=lcm(*C)
 A=[int(x*den)*(cd//C[i]) for i,x in enumerate(a)]
 b=[sum(A[i]*comb(k,i) for i in range(k+1)) for k in range(d+1)]
 return F(min(b),den*cd),F(max(b),den*cd)
# uniform real bounds for multiplier polynomials on y in [7.5,16]
# |H|<=36^4, |H'|<=4*36^3, |P|<=36^2*(17*36+91), |11+y|<=47.
# |v error|<=ell*10*sup f error (y-6 in [1.5,10]).
Qlo=[326281872,-73882460,2998263,-148957];Qhi=[326281873,-73882459,2998264,-148956]
Q=[F(x+y,2*10**6) for x,y in zip(Qlo,Qhi)];qe=F(1,2*10**6)
v0=F(-24327338758-24327338757,2*10**6)
# all basis polynomials same length
basis=[];errs=[]
# Precompute exact recurrence integer coefficients once.
R=[[pe(pk,i) for pk in p] for i in range(4,N)]
for j in range(4):
 c=[int(i==j)*r**i*M for i in range(4)]
 for i,row in enumerate(R,4):c.append(-sum(row[k]*c[i-k] for k in range(1,min(7,i)+1))//row[0])
 B=F(max(abs(x) for x in c[-7:]),M)+delta
 T=K*L*B/(1-K*e)
 # for all n>Dcut use max certified finite coeff envelope and infinite tail
 T=max(T,F(max(abs(x) for x in c[Dcut+1:]),M)+delta)
 # approximate finite coeffs to 10^-50 then bound error in f and f'
 W=10**50;u=[F((x*W)//M,W)*(-q)**i for i,x in enumerate(c[:Dcut+1])]
 eta=delta+F(1,W)
 ferr=eta/(1-q)+T*q**(Dcut+1)/(1-q)
 derr=(eta*q/(1-q)**2+T*q**(Dcut+1)*(F(Dcut+1)/(1-q)+q/(1-q)**2))/ell
 err=4*(4*36**3*ferr+36**4*derr)+2*36**2*(17*36+91)*ferr+12*47*ell*10*ferr
 b=contrast(u);basis.append(b);errs.append(err)
 print('basis',j,'tail envelope',float(T),'contrast error',float(err),'bern',tuple(map(float,bern(b))),flush=True)
combined=add(*[sc(b,Q[j]) for j,b in enumerate(basis)],[324*v0,-12*ell*v0])
lo,hi=bern(combined)
err=sum(abs(Q[j])*errs[j]+qe*(max(abs(x) for x in bern(basis[j]))+errs[j]) for j in range(4))+12*47*qe
print('middle normalized 5g/c polynomial bern',float(lo),float(hi),'error',float(err),'certified lower',float(lo-err),flush=True)
assert lo-err>2993000
print('PREFIX1054_MIDDLE_SUBBAND_CERTIFICATE_PASSED',flush=True)
