#!/usr/bin/env python3
"""Author exact check of corrected-Clausen p^4 three-channel residues and polar inverse.
Not native CM, formal verification or independent review.
"""
from collections import defaultdict
from math import comb

def primes(limit):
    for p in range(7, limit+1, 6):
        if all(p%d for d in range(2,int(p**.5)+1)): yield p

def mul(a,b,q):
    z=[0]*4
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<4:z[i+j]=(z[i+j]+x*y)%q
    return z

def jets(p):
    m=(p-1)//6;q=p*p;ph=p*pow(2,-1,q)%q
    u=[[1,0,0,0]]
    for n in range(p-1):
        a=n-m;b=n-2*m
        inv=pow(((n+1-ph)*(n+1))%q,-1,q)
        t=(3*(n+1)*inv)%q
        den=[inv*pow(t,k,q)%q for k in range(4)]
        u.append(mul(mul(u[-1],[a*b,-2*a-b,2,0],q),den,q))
    return u

def original(p):
    q4=p**4;r=[1]
    for n in range(p-1):
        r.append(r[-1]*(6*n+1)*(3*n+1)*pow(36*(n+1)**2,-1,q4)%q4)
    Q=sum((6*(a+b)+1)*r[a]*r[b]
          for a in range(p) for b in range(p-a,p))%q4
    assert Q%(p*p)==0
    return Q//(p*p)

def channel(u,p,a,b):
    m=(p-1)//6;q=p*p;c=defaultdict(int)
    v=[0]+[u[j][a]*pow(2,-j,q)%q for j in range(1,2*m+1)]
    g=[0]+[u[p-ell][b]*pow(2,ell,q)%q for ell in range(1,2*m+1)]
    for j in range(1,2*m+1):
        for ell in range(1,2*m+1):
            n=ell-j;c[n]=(c[n]+v[j]*g[ell])%q
    A=sum(c.values())%q;B=sum(n*x for n,x in c.items())%q
    I0=sum(x for n,x in c.items() if n>0)%q
    I1=sum((6*n-1)*x for n,x in c.items() if n>0)%q
    U=sum(x for n,x in c.items() if n<=0)%q
    T=sum((1-6*n)*x for n,x in c.items() if n<=0)%q
    assert U==(A-I0)%q and T==(A-6*B+I1)%q
    P=J=I0p=I1p=0
    for ell in range(1,2*m+1):
        I0p+=g[ell]*P
        I1p+=g[ell]*((6*ell-1)*P-6*J)
        P+=v[ell];J+=ell*v[ell]
    assert (I0,I1)==(I0p%q,I1p%q)
    Udirect=Tdirect=0
    for j in range(1,2*m+1):
        for ell in range(1,j+1):
            w=v[j]*g[ell]
            Udirect+=w;Tdirect+=(6*(j-ell)+1)*w
    assert (U,T)==(Udirect%q,Tdirect%q)
    return A,B,I0,I1,U,T

def polar(u,p,a,b,s):
    m=(p-1)//6;q=p*p;N=4*m-1;n0=1-2*m
    X=[0]*N;cells=[]
    for j in range(1,2*m+1):
        for ell in range(1,2*m+1):
            w=(j**s)*u[j][a]*u[p-ell][b]
            X[ell-j-n0]=(X[ell-j-n0]+w)%q
            cells.append((j,ell,w))
    beta=[(-1)**k*sum(w*comb(4*m+ell-j,k) for j,ell,w in cells)%q for k in range(N)]
    d=[sum(comb(2*m+h,h)*beta[k-h] for h in range(k+1))%q for k in range(N)]
    Y=[(-1)**r*sum(comb(k,r)*d[k] for k in range(r,N))%q for r in range(N)]
    assert X==Y,(p,a,b,s)
    return Y

def check(p):
    q=p*p;u=jets(p)
    o={ch:channel(u,p,*ch) for ch in [(0,2),(1,2),(0,3)]}
    A02,B02,C002,C102,U02,T02=o[(0,2)]
    A12,B12,C012,C112,U12,T12=o[(1,2)]
    A03,B03,C003,C103,U03,T03=o[(0,3)]
    scale=pow(2,-p,q)*pow(18,-1,q)%q
    direct=scale*(T02+p*(6*U02-(T12+T03)*pow(6,-1,q)))%q
    source=scale*(A02-6*B02+C102
        +p*(6*(A02-C002)-(A12-6*B12+C112+A03-6*B03+C103)*pow(6,-1,q)))%q
    actual=original(p)
    assert source==direct==actual,(p,source,direct,actual)
    return actual

def witness(m=3):
    js=[m+1,m+2,m+3];ells=[1,2,3];delta=[1,-2,1]
    assert m>=3 and all(1<=j<=2*m for j in js)
    assert len(set(e-j for j,e in zip(js,ells)))==1
    assert sum(delta)==sum(x*j for x,j in zip(delta,js))==0
    assert sum(x*(j+e) for x,j,e in zip(delta,js,ells))==0
    assert sum(x*j*j for x,j in zip(delta,js))==2
    assert sum(x*(j-1-m)*(j-1-2*m) for x,j in zip(delta,js))==2

if __name__=="__main__":
    checks=[(p,check(p)) for p in primes(997)]
    for p in primes(211):
        u=jets(p)
        for ch in [(0,2),(1,2),(0,3)]:
            for s in [0,1,2]:polar(u,p,*ch,s)
    witness()
    print("PASS: 80 original p^4 / corrected three-channel residues; 22 primes x 3 channels x 3 rank polar inverses; quadratic rank witness")
    print("p=13:",dict(checks)[13])
