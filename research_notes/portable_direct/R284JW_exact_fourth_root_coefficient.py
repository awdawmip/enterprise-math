import sympy as S
from math import comb, factorial
from fractions import Fraction as F
x,s,t,h=S.symbols('x s t h'); K=4

def P(v):return S.Poly(v,x,s,domain=S.QQ)
Z=P(0); O=P(1)
def add(a,b):return [u+v for u,v in zip(a,b)]
def mul(a,b):return [sum((a[i]*b[j-i] for i in range(j+1)),Z) for j in range(K+1)]
def inv(a):
    assert a[0].total_degree()==0
    b=[O/a[0].as_expr()]
    b=[P(b[0])]
    for j in range(1,K+1):b.append(P(-sum((a[i]*b[j-i] for i in range(1,j+1)),Z).as_expr()/a[0].as_expr()))
    return b

def series(a):return [P(S.expand(a).coeff(h,j)) for j in range(K+1)]
def logR(lam,end):
    out=[0]*(K+1)
    a=s*(1-t)/lam; b=s*(1+t)/lam; c=3*s/lam
    for j in range(1,K+2):
        f=(-1)**(j+1)*a**j/S.Integer(j)
        for m in range((j+1)//2,j+1):f-=(-1)**(m+1)*S.Integer(comb(m,j-m))*b**(2*m-j)*c**(j-m)/m
        for (m,),coef in S.Poly(f,t).terms():
            for ell in range(min(m,K-j+1)+1):
                if j-1+ell<=K:
                    out[j-1+ell]+=coef*S.binomial(m+1,ell)*S.bernoulli(ell,0)*end**(m+1-ell)/(m+1)
    return [P(z) for z in out]
def expR(log):
    b=[O]
    for j in range(1,K+1):b.append(sum((i*log[i]*b[j-i] for i in range(1,j+1)),Z).mul_ground(S.Rational(1,j)))
    return b

y=1-x; phi=x*x+y*y/2
logs=add(logR(1,x),logR(2,y));assert logs[0]==P(-s*phi)
r=expR(logs)
v=mul(r,series((x+h)*(y+h)))
b=mul(mul(r,series((x+h)*y)),mul(series(1+s*h*(1+y)/2+s*h*h),inv(series(1+s*h*(1-y)/2+s*h*h/2))))
a=mul(add(v,b),mul(series((1+s*h*(1-x))*(1+s*h*(1+x)+2*s*h*h)),inv(series(2*(1+s*h)*(2+2*s*h+s*h*h)))))
# EM sum of h times weights, represented as integral polynomials and endpoint polys (x=0,1)
def deriv(p):return p.diff(x)-p*P(s*S.diff(phi,x))
def em(seq):
    ans=[]
    for j in range(K+1):
        f=seq[j]; ep0=ep1=Z
        if j>=1:
            ep0+=seq[j-1].mul_ground(S.Rational(1,2));ep1+=seq[j-1].mul_ground(S.Rational(1,2))
        for n in (2,4):
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
# evaluate at s via exact interval rational; compute all integral moments for exp(-s*phi), n<=max x degree.  Taylor alternating since 0<=s*phi<=1.
# interval operations using rational endpoints
class IV:
    def __init__(self,a,b=None):self.a=F(a);self.b=F(a if b is None else b)
    def __add__(u,v):
        v=asiv(v);return IV(u.a+v.a,u.b+v.b)
    __radd__=__add__
    def __neg__(u):return IV(-u.b,-u.a)
    def __sub__(u,v):return u+-asiv(v)
    def __rsub__(u,v):return asiv(v)+-u
    def __mul__(u,v):
        v=asiv(v);p=[u.a*v.a,u.a*v.b,u.b*v.a,u.b*v.b];return IV(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(u,v):
        v=asiv(v);assert v.a*v.b>0;return u*IV(1/v.b,1/v.a)
    def __pow__(u,n):
        if n<0:return IV(1)/(u**(-n))
        r=IV(1)
        for i in range(n):r=r*u
        return r
    def __repr__(u):return str((float(u.a),float(u.b)))
def asiv(v):return v if isinstance(v,IV) else IV(v)
# derivatives up to 3 via Taylor coefficients in s; d/ds exp factor -phi

def ds(triple):
    p,l,r=triple
    return p.diff(s)-P(phi)*p,l.diff(s)-l.mul_ground(S.Rational(1,2)),r.diff(s)-r
from functools import lru_cache
# Cache polynomial powers first (avoid expanding repeatedly)
phis=[S.Poly(1,x)]
for j in range(1,33):phis.append(phis[-1]*S.Poly(phi,x))
@lru_cache(None)
def mom(n,j):return sum((F(c)/(n+k+1) for (k,),c in phis[j].terms()),F(0))
def evaluator(si):
    sp=[si**j for j in range(40)]
    @lru_cache(None)
    def moment(n):
        # sum through 31; alternating next term bounds true moment for 0<s<1.
        r=sum((sp[j]*F((-1)**j,factorial(j))*mom(n,j) for j in range(32)),IV(0));up=r+sp[32]*F(1,factorial(32))*mom(n,32);return IV(r.a,up.b)
    def exp(c):
        r=sum((sp[j]*F((-1)**j,factorial(j))*c**j for j in range(32)),IV(0));up=r+sp[32]*F(1,factorial(32))*c**32;return IV(r.a,up.b)
    ex0=exp(F(1,2));ex1=exp(F(1))
    def evalpoly(p,integral):return sum((sp[j]*F(c)*(moment(i) if integral else 1) for (i,j),c in p.terms()),IV(0))
    def ev(tr):return evalpoly(tr[0],True)+evalpoly(tr[1],False)*ex0+evalpoly(tr[2],False)*ex1
    return ev
# series in h with Taylor in s around s0, represented as 4x5 rectangular list
J=3
def jet(obs,ev):
    result=[]
    for tr in obs:
        row=[]
        for j in range(J+1):row.append(ev(tr)/factorial(j));tr=ds(tr)
        result.append(row)
    return result
def jadd(a,b):return [[u+v for u,v in zip(ar,br)] for ar,br in zip(a,b)]
def jscale(a,c):return [[u*c for u in ar] for ar in a]
def jmul(a,b):return [[sum((a[i][k]*b[n-i][j-k] for i in range(n+1) for k in range(j+1)),IV(0)) for j in range(J+1)] for n in range(K+1)]
def jp(expr,si):
    out=[]
    for p in series(expr):
        row=[]
        for j in range(J+1):row.append(sum((F(c)*si**k for (_,k),c in p.terms()),IV(0))/factorial(j));p=p.diff(s)
        out.append(row)
    return out

def compute(si):
    ev=evaluator(si);V,B,A,E=[jet(obs,ev) for obs in (v,b,a,e)]
    p=jp(4+s*(3*h+h*h),si);r=jp(3+s*(h+h*h),si);w=jadd(A,jmul(jp(s*h*h,si),jadd(V,B)))
    out=jadd(jscale(jmul(jmul(p,p),jmul(jadd(A,E),B)),3),jscale(jmul(r,jmul(w,w)),-32))
    return out[1:]
# use s root bracket inferred from exact L check at endpoints. narrow rational bracket from previous numerical alpha; no dependence on floating point for certification.
lo=F(937181823342286298624673,10**24);hi=lo+F(1,10**24)
# direct exact L sign from integral polynomials
I=(P(x*y),Z,Z);Jj=(P(x*(1-s*y*y)),Z,Z)
for point,sign in ((lo,-1),(hi,1)):
    ev=evaluator(IV(point));lv=28*point*ev(I)**2-12*ev(I)*ev(Jj);print('endpoint',point,lv,flush=True);assert (lv.b<0 if sign<0 else lv.a>0)
si=IV(lo,hi);L,M,N,P3=compute(si)
print('L',L,'M',M,'N',N,'P3',P3,flush=True)
a1=-M[0]/L[1];a2=-(N[0]+M[1]*a1+L[2]*a1**2)/L[1];a3=-(P3[0]+N[1]*a1+M[1]*a2+M[2]*a1**2+2*L[2]*a1*a2+L[3]*a1**3)/L[1]
beta=-a1/si**2;gamma=a1**2/si**3-a2/si**2;delta=-a1**3/si**4+2*a1*a2/si**3-a3/si**2
print('beta',beta,'gamma',gamma,'delta',delta,flush=True)
assert F('10.2559198987')<delta.a<=delta.b<F('10.2559198988')
assert F('-12.5336350561')<gamma.a<=gamma.b<F('-12.5336350560')
print('Certified delta and gamma intervals; all assertions passed.')
