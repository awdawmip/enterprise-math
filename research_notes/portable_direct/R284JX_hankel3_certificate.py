# Frozen JW recurrence, extended through order 8. Exact outward rational interval arithmetic.
import sympy as S
from math import comb,factorial
from fractions import Fraction as F
from functools import lru_cache
x,s,t,h=S.symbols('x s t h');K=8;J=7
def P(v):return S.Poly(v,x,s,domain=S.QQ)
Z=P(0);O=P(1)
def add(a,b):return [u+v for u,v in zip(a,b)]
def mul(a,b):return [sum((a[i]*b[j-i] for i in range(j+1)),Z) for j in range(K+1)]
def inv(a):
    assert a[0].total_degree()==0
    b=[P(1/a[0].as_expr())]
    for j in range(1,K+1):b.append(P(-sum((a[i]*b[j-i] for i in range(1,j+1)),Z).as_expr()/a[0].as_expr()))
    return b
def series(a):return [P(S.expand(a).coeff(h,j)) for j in range(K+1)]
def logR(lam,end):
    out=[0]*(K+1);a=s*(1-t)/lam;b=s*(1+t)/lam;c=3*s/lam
    for j in range(1,K+2):
        f=(-1)**(j+1)*a**j/S.Integer(j)
        for m in range((j+1)//2,j+1):f-=(-1)**(m+1)*S.Integer(comb(m,j-m))*b**(2*m-j)*c**(j-m)/m
        for (m,),coef in S.Poly(f,t).terms():
            for ell in range(min(m,K-j+1)+1):out[j-1+ell]+=coef*S.binomial(m+1,ell)*S.bernoulli(ell,0)*end**(m+1-ell)/(m+1)
    return [P(z) for z in out]
def expR(log):
    b=[O]
    for j in range(1,K+1):b.append(sum((i*log[i]*b[j-i] for i in range(1,j+1)),Z).mul_ground(S.Rational(1,j)))
    return b
y=1-x;phi=x*x+y*y/2
logs=add(logR(1,x),logR(2,y));assert logs[0]==P(-s*phi)
r=expR(logs)
v=mul(r,series((x+h)*(y+h)))
b=mul(mul(r,series((x+h)*y)),mul(series(1+s*h*(1+y)/2+s*h*h),inv(series(1+s*h*(1-y)/2+s*h*h/2))))
a=mul(add(v,b),mul(series((1+s*h*(1-x))*(1+s*h*(1+x)+2*s*h*h)),inv(series(2*(1+s*h)*(2+2*s*h+s*h*h)))))
def deriv(p):return p.diff(x)-p*P(s*S.diff(phi,x))
def em(seq):
    ans=[]
    for j in range(K+1):
        f=seq[j];ep0=ep1=Z
        if j>=1:ep0+=seq[j-1].mul_ground(S.Rational(1,2));ep1+=seq[j-1].mul_ground(S.Rational(1,2))
        for n in (2,4,6,8):
            if j>=n:
                p=seq[j-n]
                for _ in range(n-1):p=deriv(p)
                p=p.mul_ground(S.bernoulli(n)/factorial(n));ep0-=p;ep1+=p
        ans.append((f,P(ep0.as_expr().subs(x,0)),P(ep1.as_expr().subs(x,1))))
    return ans
v,b,a=map(em,(v,b,a))
re=expR(logR(1,S.Integer(1)))
ee=mul(re,mul(series(h*h*(2+3*h)*(2+s*h+2*s*h*h)),inv(series(2*(2+2*s*h+s*h*h)*(8+4*s*h+2*s*h*h)))))
e=[(Z,Z,p) for p in ee]
B=10**80
class IV:
    def __init__(self,a,b=None):
        a=F(a);b=a if b is None else F(b)
        self.a=a.numerator*B//a.denominator;self.b=-((-b.numerator*B)//b.denominator)
    @classmethod
    def raw(cls,a,b):
        r=object.__new__(cls);r.a=a;r.b=b;return r
    def __add__(u,v):
        v=asiv(v);return IV.raw(u.a+v.a,u.b+v.b)
    __radd__=__add__
    def __neg__(u):return IV.raw(-u.b,-u.a)
    def __sub__(u,v):return u+-asiv(v)
    def __rsub__(u,v):return asiv(v)+-u
    def __mul__(u,v):
        v=asiv(v);p=[u.a*v.a,u.a*v.b,u.b*v.a,u.b*v.b];return IV.raw(min(p)//B,-((-max(p))//B))
    __rmul__=__mul__
    def __truediv__(u,v):
        v=asiv(v);assert v.a*v.b>0;return u*IV(F(B,v.b),F(B,v.a))
    def __pow__(u,n):
        if n<0:return IV(1)/(u**(-n))
        r=IV(1)
        for _ in range(n):r=r*u
        return r
    def __repr__(u):return str((float(F(u.a,B)),float(F(u.b,B))))
    def inside(u,lo,hi):return F(lo)<F(u.a,B)<=F(u.b,B)<F(hi)
def asiv(v):return v if isinstance(v,IV) else IV(v)
def ds(tr):
    p,l,r=tr;return p.diff(s)-P(phi)*p,l.diff(s)-l.mul_ground(S.Rational(1,2)),r.diff(s)-r
phis=[S.Poly(1,x)]
for j in range(1,33):phis.append(phis[-1]*S.Poly(phi,x))
@lru_cache(None)
def mom(n,j):return sum((F(c)/(n+k+1) for (k,),c in phis[j].terms()),F(0))
def evaluator(si):
    sp=[si**j for j in range(64)]
    @lru_cache(None)
    def moment(n):
        r=sum((sp[j]*F((-1)**j,factorial(j))*mom(n,j) for j in range(32)),IV(0));up=r+sp[32]*F(1,factorial(32))*mom(n,32);return IV.raw(r.a,up.b)
    def exp(c):
        r=sum((sp[j]*F((-1)**j,factorial(j))*c**j for j in range(32)),IV(0));up=r+sp[32]*F(1,factorial(32))*c**32;return IV.raw(r.a,up.b)
    ex0=exp(F(1,2));ex1=exp(F(1))
    def ep(p,integral):return sum((sp[j]*F(c)*(moment(i) if integral else 1) for (i,j),c in p.terms()),IV(0))
    return lambda tr:ep(tr[0],True)+ep(tr[1],False)*ex0+ep(tr[2],False)*ex1
def jet(obs,ev):
    result=[]
    for i,tr in enumerate(obs):
        row=[]
        for j in range(J+1):row.append(ev(tr)/factorial(j) if i+j<=K else IV(0));tr=ds(tr)
        result.append(row)
    return result
def jadd(a,b):return [[u+v for u,v in zip(ar,br)] for ar,br in zip(a,b)]
def jscale(a,c):return [[u*c for u in ar] for ar in a]
def jmul(a,b):return [[sum((a[i][k]*b[n-i][j-k] for i in range(n+1) for k in range(j+1)),IV(0)) if n+j<=K else IV(0) for j in range(J+1)] for n in range(K+1)]
def jp(expr,si):
    out=[]
    for i,p in enumerate(series(expr)):
        row=[]
        for j in range(J+1):row.append(sum((F(c)*si**k for (_,k),c in p.terms()),IV(0))/factorial(j) if i+j<=K else IV(0));p=p.diff(s)
        out.append(row)
    return out
def compute(si):
    ev=evaluator(si);V,B,A,E=[jet(obs,ev) for obs in (v,b,a,e)]
    p=jp(4+s*(3*h+h*h),si);r=jp(3+s*(h+h*h),si);w=jadd(A,jmul(jp(s*h*h,si),jadd(V,B)))
    return jadd(jscale(jmul(jmul(p,p),jmul(jadd(A,E),B)),3),jscale(jmul(r,jmul(w,w)),-32))[1:]
lo=F(937181823342286298624673,10**24);hi=lo+F(1,10**24)
I=(P(x*y),Z,Z);Jj=(P(x*(1-s*y*y)),Z,Z)
for point,sign in ((lo,-1),(hi,1)):
    ev=evaluator(IV(point));lv=28*point*ev(I)**2-12*ev(I)*ev(Jj);print('endpoint',point,lv,flush=True);assert (lv.b<0 if sign<0 else lv.a>0)
si=IV(lo,hi);coeff=compute(si);print('f coefficients',*[row[0] for row in coeff],flush=True)
def pmul(a,b,n):return [sum((a[i]*b[j-i] for i in range(j+1)),IV(0)) for j in range(n+1)]
root=[IV(0)]*8
for n in range(1,8):
    powers=[[IV(1)]+[IV(0)]*n]
    for j in range(1,n+1):powers.append(pmul(powers[-1],root[:n+1],n))
    residual=sum((coeff[i][j]*powers[j][n-i] for i in range(n+1) for j in range(n-i+1)),IV(0))
    root[n]=-residual/coeff[0][1]
u=[si]+root[1:];invu=[IV(1)/si]
for n in range(1,8):invu.append(-sum((u[i]*invu[n-i] for i in range(1,n+1)),IV(0))/si)
alpha,beta,gamma,delta,eps,zeta,theta,iota=invu;H=delta*zeta-eps**2
H3=delta*(zeta*iota-theta**2)-eps*(eps*iota-zeta*theta)+zeta*(eps*theta-zeta**2)
for label,value in zip(('alpha','beta','gamma','delta','epsilon','zeta','theta','iota','Hankel','Hankel3'),invu+[H,H3]):print(label,value,'exact_scaled_interval',value.a,value.b,flush=True)
assert gamma.inside('-12.5336350561','-12.5336350560')
assert delta.inside('10.2559198987','10.2559198988')
assert H.a>0 or H.b<0
assert H3.a>0 or H3.b<0
print('All exact interval assertions passed.',flush=True)
