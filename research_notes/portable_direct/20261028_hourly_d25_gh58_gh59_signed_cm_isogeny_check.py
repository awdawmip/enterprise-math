#!/usr/bin/env python3
"""GH58-59: independent F_(p^2) point/trace and isogeny checks, finite evidence."""
from math import comb, isqrt

def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))
def add(x,y,p): return ((x[0]+y[0])%p,(x[1]+y[1])%p)
def neg(x,p): return (-x[0]%p,-x[1]%p)
def sub(x,y,p): return add(x,neg(y,p),p)
def mul(x,y,p): return ((x[0]*y[0]+2*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def scale(x,k,p): return ((x[0]*k)%p,(x[1]*k)%p)
def const(k,p): return (k%p,0)
def inv(x,p):
    n=(x[0]**2-2*x[1]**2)%p
    return scale((x[0],-x[1]),pow(n,-1,p),p)
def div(x,y,p): return mul(x,inv(y,p),p)
def Ct(p): return (9*pow(2,-1,p)%p,-3%p)
def f(x,C,p): return mul(x,add(sub(mul(x,x,p),scale(x,6,p),p),C,p),p)
def psi(P,C,u,p):
    if P is None: return None
    x,y=P
    if x==(0,0):
        assert y==(0,0)
        return None
    xx=scale(sub(add(x,div(C,x,p),p),const(6,p),p),-pow(2,-1,p),p)
    yy=scale(mul(y,sub(const(1,p),div(C,mul(x,x,p),p),p),p),-pow(2*u,-1,p),p)
    return xx,yy

def double(P,C,p):
    if P is None or P[1]==(0,0): return None
    x,y=P
    lam=div(add(sub(scale(mul(x,x,p),3,p),scale(x,12,p),p),C,p),scale(y,2,p),p)
    xx=add(sub(mul(lam,lam,p),scale(x,2,p),p),const(6,p),p)
    return xx,sub(mul(lam,sub(x,xx,p),p),y,p)
def pointneg(P,p): return None if P is None else (P[0],neg(P[1],p))
def frob(P,p): return None if P is None else ((P[0][0],-P[0][1]%p),(P[1][0],-P[1][1]%p))

def trace(p):
    C=Ct(p)
    chi=[0 if i==0 else (1 if pow(i,(p-1)//2,p)==1 else -1) for i in range(p)]
    total=0
    for a in range(p):
        for b in range(p):
            z=f((a,b),C,p)
            total+=chi[(z[0]*z[0]-2*z[1]*z[1])%p]
    return -total

def Hasse(p):
    C=Ct(p);r=(p-1)//2;h=(0,0);v=(1,0)
    for i in range(r//2+1):
        h=add(h,scale(v,comb(r,i)*comb(r-i,i)*pow(-6,r-2*i,p),p),p)
        v=mul(v,C,p)
    return h

def legendre(p):
    n=(p-3)//4;t=(0,2*pow(3,-1,p)%p)
    a,b=(1,0),t
    if n==0: return a
    for k in range(1,n):
        a,b=b,scale(sub(scale(mul(t,b,p),2*k+1,p),scale(a,k,p),p),pow(k+1,-1,p),p)
    return b

def Fvalue(p):
    m=(p-3)//8;s=0;term=1;z=1
    for r in range(m+1):
        s=(s+term*z)%p
        if r<m:
            term=term*(r-m)**2*pow((r+1)*(2*m+2+r),-1,p)%p
            z=z*9%p
    return s

def represent(p):
    return [(x,y) for x in range(isqrt(p//2)+1) for y in range(isqrt(p//3)+1) if 2*x*x+3*y*y==p]

def verify_points(p,limit=24):
    C=Ct(p);Cp=sub(const(9,p),C,p)
    u=next(a for a in range(1,p) if a*a%p==(-2)%p)
    squares={}
    for a in range(p):
        for b in range(p):
            z=(a,b);squares.setdefault(mul(z,z,p),z)
    checked=0
    for a in range(p):
        for b in range(p):
            x=(a,b);y=squares.get(f(x,C,p))
            if y is None: continue
            point=(x,y)
            q=psi(point,C,u,p)
            if q is not None: assert mul(q[1],q[1],p)==f(q[0],Cp,p)
            back=psi(q,Cp,u,p)
            minus2=pointneg(double(point,C,p),p)
            assert back==minus2,(p,point,back,minus2)
            phi=psi(frob(point,p),Cp,u,p)
            phi2=psi(frob(phi,p),Cp,u,p)
            assert phi2==minus2,(p,point,phi2,minus2)
            checked+=1
            if checked>=limit: return checked
    raise AssertionError('not enough points')

def main():
    ps=[p for p in range(11,200) if p%8==3 and prime(p)]
    samples=[];num=0
    for p in ps:
        m=(p-3)//8;h=Hasse(p);P=legendre(p)
        sign=1 if pow(-6%p,(p-1)//2,p)==1 else -1
        assert h==scale(P,sign,p) and h[1]==0,(p,h,P)
        assert (comb(3*m+1,m)*Fvalue(p)-pow(9,m,p)*P[0])%p==0
        aq=trace(p)
        assert aq%p == h[0]**2%p,(p,aq,h)
        if p%24==19:
            rep=None;expected=2*p;assert h==(0,0)
        else:
            reps=represent(p);assert len(reps)==1,(p,reps)
            x,y=reps[0];rep=(x,y)
            expected=2*(3*y*y-2*x*x)
            assert P[0]**2%p==(-8*x*x)%p
        assert aq==expected,(p,aq,expected)
        num+=verify_points(p)
        samples.append((p,p%24,aq,rep,h[0]))
    print('PASS_GH58_SIGNED_2_ISOGENY_AND_FROBENIUS:',len(ps),'primes;',num,'point checks')
    print('PASS_GH59_CM_TRACE_AND_SPECIAL_F_MAGNITUDE:',len(ps),'primes')
    for v in samples: print(v)

if __name__=='__main__': main()
