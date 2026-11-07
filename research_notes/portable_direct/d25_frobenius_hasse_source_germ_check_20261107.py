"""Portable Fricke source Frobenius/Hasse coefficient verifier. NOT native H0/B0."""
from math import comb
import sympy as sp

T=sp.symbols("t")
Z=108*T**2*(T+9)*(T+8)**2/(T+12)**6
W=256*T**3*(T+8)*(T+9)**3/(T**2+36*T+216)**4
R=sp.cancel(3*(T**2-72*T-648)*(T**2+16*T+72)/(2*(T+6)*(T+12)*(T**2-24*T-288)))
S=sp.sqrt(2)

def symbolic():
    for e in (1,-1):
        t0=e*6*S
        val=lambda f:sp.simplify(sp.radsimp(f.subs(T,t0)))
        assert val(Z)==sp.Rational(1,2) and val(W)==sp.Rational(1,9) and val(R)==4
        assert val(sp.diff(Z,T))==-1+e*3*S/4
        assert val(sp.diff(W,T))==sp.Rational(4,9)-e*8*S/27
        expected=[4,(-35+e*25*S)/3,sp.Rational(475,6)-e*sp.Rational(2015,36)*S,
                  -sp.Rational(19205,24)+e*sp.Rational(3395,6)*S]
        for k,x in enumerate(expected):
            assert sp.simplify(val(sp.diff(R,T,k))-x)==0
    assert sp.Rational(5,18)**2-2*sp.Rational(7,36)**2==sp.Rational(1,648)

def pa(x,y,p): return ((x[0]+y[0])%p,(x[1]+y[1])%p)
def pm(x,y,p): return ((x[0]*y[0]+2*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def pi(x,p):
    d=pow((x[0]**2-2*x[1]**2)%p,-1,p)
    return (x[0]*d%p,-x[1]*d%p)
def pp(x,k,p):
    out=(1,0)
    while k:
        if k&1:out=pm(out,x,p)
        k//=2
        if k:x=pm(x,x,p)
    return out

def check(p,e):
    n=p+2; zero=(0,0);one=(1,0)
    def c(x):return (x%p,0)
    def add(a,b):return [pa(x,y,p) for x,y in zip(a,b)]
    def scale(a,k):return [pm(x,c(k),p) for x in a]
    def mul(a,b):
        out=[zero]*n
        for i,x in enumerate(a):
            if x==zero:continue
            for j in range(n-i):
                if b[j]!=zero:out[i+j]=pa(out[i+j],pm(x,b[j],p),p)
        return out
    def inv(a):
        out=[pi(a[0],p)]+[zero]*(n-1)
        for i in range(1,n):
            v=zero
            for j in range(1,i+1):v=pa(v,pm(a[j],out[i-j],p),p)
            out[i]=pm(out[0],(-v[0]%p,-v[1]%p),p)
        return out
    def power(a,k):
        out=[one]+[zero]*(n-1)
        while k:
            if k&1:out=mul(out,a)
            k//=2
            if k:a=mul(a,a)
        return out
    def sub(a,b):return add(a,scale(b,-1))
    unit=[one]+[zero]*(n-1)
    t=[(0,6*e%p),one]+[zero]*(n-2)
    t2=mul(t,t)
    sh=lambda a,k:add(a,scale(unit,k))
    div=lambda a,b:mul(a,inv(b))
    z=div(scale(mul(mul(t2,sh(t,9)),power(sh(t,8),2)),108),power(sh(t,12),6))
    w=div(scale(mul(mul(power(t,3),sh(t,8)),power(sh(t,9),3)),256),
          power(add(add(t2,scale(t,36)),scale(unit,216)),4))
    r=div(scale(mul(sub(sub(t2,scale(t,72)),scale(unit,648)),
                    add(add(t2,scale(t,16)),scale(unit,72))),3),
          scale(mul(mul(sh(t,6),sh(t,12)),
                    sub(sub(t2,scale(t,24)),scale(unit,288))),2))
    cp=comb(2*p,p)**2*comb(3*p,p)*pow(108,-p,p)%p
    dp=comb(2*p,p)**2*comb(4*p,2*p)*pow(256,-p,p)%p
    assert cp==pow(9,-1,p) and dp==3*pow(32,-1,p)%p
    source=sub(scale(mul(r,power(w,p)),dp),scale(power(z,p),cp))
    smooth=sub(scale(r,pow(96,-1,p)),scale(unit,pow(18,-1,p)))
    defect=sub(source,smooth)
    assert defect[:p]==[zero]*p
    chi=1 if pow(2,(p-1)//2,p)==1 else -1
    expect=(5*pow(18,-1,p)%p,-e*chi*7*pow(36,-1,p)%p)
    assert defect[p]==expect,(p,e,defect[p],expect)
    next_coeff=pm(pm(c(dp),pp(w[1],p,p),p),r[1],p)
    assert defect[p+1]==next_coeff
    assert (expect[0]**2-2*expect[1]**2)%p==pow(648,-1,p)
    return defect[p],defect[p+1]

if __name__=="__main__":
    symbolic()
    for p in (5,7,11,13,19,373):
        for e in (1,-1):
            a,b=check(p,e)
            print(f"p={p} fiber={e}: u^p={a}, u^(p+1)={b}; PASS")
