from fractions import Fraction as F
from math import ceil,prod
import sympy as S
Y,x,n=S.symbols('Y x n')
a=[-Y**2*(Y-6),-Y**2*(31*Y**2-516*Y+1020),-6*Y**2*(15*Y**3-406*Y**2+2078*Y-1152),-Y**3*(65*Y**3-2408*Y**2+19836*Y-27648),-5*Y**4*(3*Y**3-140*Y**2+1568*Y-3456),-Y**5*(Y-36)*(Y-16)*(Y-4)]
A=[S.Poly((-1)**j*p.subs(Y,4-x),x) for j,p in enumerate(a)]
# Coefficients of x^alpha sum b_i x^i; scale d_i=2^i b_i.
r=F(2); N=2000; D=100; M=10**4000
K=1/((1-r/4)**5*(1-r/12)*(1-r/32))
def calc(alpha,initial):
    w=[S.Poly(S.expand(sum(A[j].nth(k-4+j)*prod(n+alpha-k-i for i in range(j)) for j in range(6) if k-4+j>=0)*r**k),n) for k in range(8)]
    lim=[-F(p.LC()/w[0].LC()) for p in w[1:]]
    z=S.Symbol('z'); assert S.expand(1-sum(l*z**(k+1) for k,l in enumerate(lim))-(1-r*z/4)**5*(1+r*z/12)*(1+r*z/32))==0
    den=S.Poly(w[0].as_expr().subs(n,n+N),n);sg=S.sign(den.LC());den=den.mul_ground(sg);assert all(den.nth(i)>0 for i in range(6))
    e=sum(max(F(abs(p.nth(i))/den.nth(i)) for i in range(6)) for p in [S.Poly((-w[k].as_expr()-lim[k-1]*w[0].as_expr()).subs(n,n+N),n).mul_ground(sg) for k in range(1,8)])
    assert K*e<1,(alpha,float(K*e));L=sum(map(abs,lim))+e
    from math import lcm
    den=lcm(*(int(c.q) for p in w for c in p.all_coeffs())); W=[[int(p.nth(i)*den) for i in range(6)] for p in w]
    def ev(p,i):return sum(c*i**j for j,c in enumerate(p))
    c=[int(F(v)*M) for v in initial]; assert all(F(v)*M==a for a,v in zip(c,initial)); E=[0]*len(c)
    for i in range(len(c),N):
        wv=[ev(p,i) for p in W];assert wv[0]!=0
        c.append(-sum(wv[k]*c[i-k] for k in range(1,min(7,i)+1))//wv[0])
        d=abs(wv[0]);E.append(1+(sum(abs(wv[k])*E[i-k] for k in range(1,min(7,i)+1))+d-1)//d)
    delta=F(max(E),M);assert delta<F(1,10**30)
    B=F(max(map(abs,c[-7:])),M)+delta
    T=max(K*L*B/(1-K*e),F(max(map(abs,c[D+1:])),M)+delta)
    print('alpha',alpha,'Ke',float(K*e),'T',float(T),'delta',float(delta),flush=True)
    return [F(v//(M//10**30),10**30)/r**i for i,v in enumerate(c[:D+1])],T,delta+F(1,10**30)
# Evaluate at s=sqrt(x), retain cusp and primitive separately via power coefficients.
rows=[calc(0,[int(i==j)*(-r)**i for i in range(4)]) for j in range(4)]+[calc(F(3,2),[1])]
# polynomial arithmetic exact
def add(*ps):return [sum(p[i] for p in ps if i<len(p)) for i in range(max(map(len,ps)))]
def mul(p,q):
 o=[F(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  if a:
   for j,b in enumerate(q):
    if b:o[i+j]+=a*b
 return o
def sc(p,c):return [v*c for v in p]
def poly(expr):
 p=S.Poly(expr,x);return [F(p.nth(i)) for i in range(p.degree()+1)]
y=4-x*x;H=poly(y*y*(36-y)**2);Hp=poly(2*y*(36-y)*(36-2*y));P=poly(y*(y-36)*(17*y-91));J=poly(11+y)
def contrast(b,shift):
 u=[F(0)]*(2*D+shift+1)
 for i,v in enumerate(b):u[2*i+shift]=v
 du=[-F(i,2)*u[i] for i in range(2,len(u))] # d/dy = -1/(2s)d/ds; missing i=1 is zero
 assert u[1]==0
 w=mul([0,4,0,2],u) # dU/ds=(y-6)*(-2s)u=(4s+2s^3)u
 v=[F(0)]+[c/(i+1) for i,c in enumerate(w)]
 return add(sc(mul(Hp,u),4),sc(mul(H,du),4),sc(mul(P,u),-2),sc(mul(J,v),12))
# S=5/4; x<=25/16; q=25/32. Error in rho basis and y derivative.
smax=F(5,4); X=smax*smax;q=X/r
ps=[];errs=[]
for j,(b,T,eta) in enumerate(rows):
 shift=3 if j==4 else 0
 ps.append(contrast(b,shift))
 # uniform error for analytic factor and derivative (n>=1) on x<=X
 e0=eta/(1-q)+T*q**(D+1)/(1-q)
 e1=(eta/(1-q)**2+T*q**D*((D+1)/(1-q)+q/(1-q)**2))/r
 if shift:
  e0,e1=smax**3*e0,smax**3*e1+F(3,2)*smax*e0
 # on [0,4], |H|<=36^4, etc; primitive variation <= X*6*e0
 errs.append(4*(4*36**3*e0+36**4*e1)+2*36**2*(17*36+91)*e0+12*47*X*6*e0)
boxes=[(235698,235702),(-44062,-44059),(6845,6848),(-1244,-1242),(-13500,-13500),(-5241077,-5241068)]
ps.append(sc(J,12));errs.append(F(0));mid=[F(a+b,200) for a,b in boxes];rad=[F(b-a,200) for a,b in boxes]
# fixed-point enclosure of polynomial coefficients then interval Horner on subintervals
W=10**30
def interval(p,l,h):
 lo=hi=0
 for a in reversed(p):
  vals=[lo*l,lo*h,hi*l,hi*h]
  lo=min(vals)//W+(a*W)//1
  hi=ceil(F(max(vals),W))+ceil(a*W)
 return F(lo,W),F(hi,W)
# x coordinate s interval grid exact because W divisible by 1024
base=add(*(sc(p,c) for p,c in zip(ps,mid)));err=sum((abs(c)+d)*e for c,d,e in zip(mid,rad,errs));lower=None
for i in range(256):
 l=int(W*smax*i/256);h=int(W*smax*(i+1)/256)
 lo,_=interval(base,l,h);er=err+sum(d*max(map(abs,interval(p,l,h))) for p,d in zip(ps,rad) if d)
 b=lo-er;lower=b if lower is None else min(lower,b)
print('lower 5g/c',float(lower),'tail err',float(err));assert lower>15390000
print('PREFIX1055_LOWER_BAND_CERTIFICATE_PASSED')
