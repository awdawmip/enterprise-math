#!/usr/bin/env python3
"""Exact author check: signed critical polar-jet Pascal bridge (stdlib only).
Rational and F_p algebra; no native CM computation or independent review.
"""
from fractions import Fraction
from math import comb, factorial

def ftable(m,p):
    if p is None:return None
    f=[1]*(4*m+1)
    for i in range(1,len(f)):f[i]=f[i-1]*i%p
    v=[1]*len(f);v[-1]=pow(f[-1],-1,p)
    for i in range(len(f)-1,0,-1):v[i-1]=v[i]*i%p
    return f,v

def choose(n,k,p=None,t=None):
    if k<0 or k>n:return 0
    if p is None:return comb(n,k)
    f,v=t
    return f[n]*v[k]*v[n-k]%p

def sources(m,p=None):
    L,U,n0,N=m+1,2*m,1-2*m,3*m-1
    E=[0]*N;D=[0]*N;J=[0]*N;S=0;C=0
    if p is None:
        a={j:Fraction((-1)**(j-L)*factorial(m)*factorial(j-m-1)*factorial(2*m),
                     factorial(2*m-j)*factorial(j)**2) for j in range(L,U+1)}
        h={l:Fraction(2*factorial(m)*factorial(2*m)*factorial(l-1)**2,
                     factorial(l+m)*factorial(l+2*m)) for l in range(1,U+1)}
    else:
        f,v=ftable(m,p)
        a={j:(-1)**(j-L)*f[m]*f[j-m-1]*f[2*m]*v[2*m-j]*v[j]**2%p
           for j in range(L,U+1)}
        h={l:2*f[m]*f[2*m]*f[l-1]**2*v[l+m]*v[l+2*m]%p
           for l in range(1,U+1)}
    for j,aj in a.items():
        for l,hl in h.items():
            r=l-j-n0;x=aj*hl
            twopow=Fraction(2)**(l-j) if p is None else pow(2,l-j,p)
            if l<=j:S+=(6*(j-l)+1)*twopow*x
            else:C+=(6*(l-j)-1)*twopow*x
            E[r]+=x;D[r]+=(j+l)*x;J[r]+=j*x
            if p:E[r]%=p;D[r]%=p;J[r]%=p
    S=-S/216 if p is None else -S*pow(216,-1,p)%p
    if p:C%=p
    return E,D,J,S,C

def forward(X,m,p=None):
    N=3*m-1;t=ftable(m,p)
    b=[]
    for k in range(N):
        s=(-1)**k*sum(choose(m+1+r,k,p,t)*X[r] for r in range(N))
        b.append(s%p if p else s)
    return b

def inverse(b,m,p=None):
    N=3*m-1;t=ftable(m,p);c=[]
    for k in range(N):
        s=sum(choose(m+q,q,p,t)*b[k-q] for q in range(k+1))
        c.append(s%p if p else s)
    out=[]
    for r in range(N):
        s=(-1)**r*sum(choose(k,r,p,t)*c[k] for k in range(r,N))
        out.append(s%p if p else s)
    return out

def observers(E,m,p=None):
    n0=1-2*m
    tp=(lambda n:Fraction(2)**n) if p is None else (lambda n:pow(2,n,p))
    S=-sum((1-6*(n0+r))*tp(n0+r)*e for r,e in enumerate(E) if n0+r<=0)
    C=sum((6*(n0+r)-1)*tp(n0+r)*e for r,e in enumerate(E) if n0+r>0)
    if p:return S*pow(216,-1,p)%p,C%p
    return S/216,C

def test(m,p=None):
    E,D,J,S,C=sources(m,p)
    b=forward(E,m,p);d=forward(D,m,p)
    Er=inverse(b,m,p);Dr=inverse(d,m,p)
    assert (E,D)==(Er,Dr),(m,p,'unimodular inverse')
    n0=1-2*m
    if p:
        j=[(Dr[r]-(n0+r)*Er[r])*pow(2,-1,p)%p for r in range(len(E))]
    else:
        j=[(Dr[r]-(n0+r)*Er[r])/2 for r in range(len(E))]
    assert J==j,(m,p,'first-rank moment')
    assert observers(Er,m,p)==(S,C),(m,p,'both signed observers')
    for k in [3*m-1,3*m]:
        t=ftable(m,p)
        lhs=(-1)**k*sum(choose(m+1+r,k,p,t)*D[r] for r in range(len(D)))
        rhs=(-1)**k*sum(choose(m+1+r,k,p,t)*Dr[r] for r in range(len(D)))
        assert (lhs-rhs)%p==0 if p else lhs==rhs,(m,p,'Laurent extension')
    return b,d,S,C

def primes(limit):
    for p in range(7,limit+1):
        if p%6==1 and all(p%d for d in range(2,int(p**.5)+1)):yield p

def main():
    for m in range(1,16):test(m)
    ps=list(primes(997))
    for p in ps:test((p-1)//6,p)
    b,d,S,C=test(2)
    assert (S,C)==(Fraction(-87161,32659200),Fraction(1,630))
    assert S.numerator*pow(S.denominator,-1,13)%13==2
    assert C.numerator*pow(C.denominator,-1,13)%13==11
    print('PASS: rational m=1..15; mod p for',len(ps),'primes <=997')
    print('m=2 product high poles:',b,'\\nm=2 W poles:',d)
    print('S_13:',S,'; infinity:',C,'; modulo 13: 2,11')

if __name__=='__main__':main()
