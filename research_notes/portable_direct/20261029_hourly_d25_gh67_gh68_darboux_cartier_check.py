#!/usr/bin/env python3
"""Finite exact verification of GH-67/68 author formulas; standard library only."""
from math import comb, isqrt

def ps(limit):
    sv=bytearray(b'\x01')*limit
    sv[:2]=b'\x00\x00'
    for i in range(2,isqrt(limit-1)+1):
        if sv[i]:
            sv[i*i:limit:i]=b'\x00'*(((limit-1-i*i)//i)+1)
    return [p for p in range(11,limit) if sv[p] and p%8==3]

def add(a,b,p,k=1):
    z=[0]*max(len(a),len(b))
    for i,v in enumerate(a): z[i]=(z[i]+v)%p
    for i,v in enumerate(b): z[i]=(z[i]+k*v)%p
    return z

def mul(a,b,p):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): z[i+j]=(z[i+j]+v*w)%p
    return z

def der(a,p):
    return [(i*a[i])%p for i in range(1,len(a))] or [0]

def taylor(a,x,p):
    z=[0]*len(a)
    for j,v in enumerate(a):
        for n in range(j+1):
            z[n]=(z[n]+v*comb(j,n)*pow(x,j-n,p))%p
    return z

def binomial_series(b,e,p,N,step=1):
    assert b%p
    out=[]
    for n in range(N+1):
        if e>=0:
            v=comb(e,n)*pow(b,e-n,p)*pow(step,n,p) if n<=e else 0
        else:
            s=-e
            v=comb(s+n-1,n)*pow(-step,n,p)*pow(b,-s-n,p)
        out.append(v%p)
    return out

def inv(a,p,N):
    assert a[0]%p
    z=[pow(a[0],-1,p)]
    for n in range(1,N):
        acc=sum(a[j]*z[n-j] for j in range(1,min(n,len(a)-1)+1))
        z.append(-acc*z[0]%p)
    return z

def fg(p):
    m=(p-3)//8
    D=comb(3*m+1,m)%p
    f=[comb(m,r)*comb(3*m+1,m-r)*pow(D,-1,p)%p for r in range(m+1)]
    g=[(16*r+5)*v%p for r,v in enumerate(f)]
    return m,D,f,g

def check():
    N=0
    for p in ps(2000):
        m,D,f,g=fg(p)
        ff=mul(f,f,p); gg=mul(g,g,p); fg0=mul(f,g,p)
        t=add(mul(der(f,p),g,p),mul(f,der(g,p),p),p)
        lhs=add(mul([5,-1],ff,p),mul([1,-1],gg,p),p,-1)
        lhs=add(lhs,mul([-4,12],fg0,p),p,-1)
        lhs=add(lhs,mul([0,16,-16],t,p),p)
        assert not any(lhs),(p,"GH67")
        ny=add(mul([0,16,-16],der(g,p),p),mul([1,7],g,p),p,-1)
        assert not any(add(ny,mul([-5,1],f,p),p,-1)),(p,"GH68")
        g5=sum(v*pow(5,i,p) for i,v in enumerate(g))%p
        gd5=sum(i*v*pow(5,i-1,p) for i,v in enumerate(g) if i)%p
        assert (80*gd5+9*g5)%p==0,(p,"apparent")
        N+=1
    print("PASS_GH67_68_CLEARED_DARBOUX",N,"primes<2000")
    charts=roots=0
    for p in ps(200):
        m,D,f,g=fg(p)
        for a in (2,5,9):
            a%=p
            gt=taylor(g,a,p)
            e=next(i for i,v in enumerate(gt) if v)
            roots+=bool(e)
            n=p-1+2*e
            za=binomial_series(a,-2*m-2,p,n)
            ba=binomial_series((1-a)%p,4*m,p,n,step=-1)
            q0=mul(za,ba,p)[:n+1]
            q=[((5-a)*q0[i]-(q0[i-1] if i else 0))%p for i in range(n+1)]
            iz=inv(gt[e:],p,n+1)
            iz2=mul(iz,iz,p)[:n+1]
            got=sum(q[i]*iz2[n-i] for i in range(n+1))%p
            assert got==(-D*D*pow(a,-1,p))%p,(p,a,e,got)
            charts+=1
    print("PASS_GH67_CARTIER_CHARTS",charts,"Laurent_G_roots",roots)

if __name__=="__main__":
    check()
