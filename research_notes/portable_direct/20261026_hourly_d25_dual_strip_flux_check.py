#!/usr/bin/env python3
"""Author exact checks: dual corrected-Clausen finite-strip flux (not native CM)."""
from math import factorial

def primes(limit):
    for p in range(7,limit+1,6):
        if all(p%d for d in range(2,int(p**.5)+1)):
            yield p

def product(a,b,q):
    n=len(a)
    c=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b[:n-i]):
            c[i+j]=(c[i+j]+x*y)%q
    return c

def jets(p,degree=4):
    m=(p-1)//6; q=p*p; ph=p*pow(2,-1,q)%q
    u=[[1]+[0]*degree]
    for n in range(1,p):
        a=n-1-m; b=n-1-2*m; inv=pow(n-ph,-1,q)
        den=[inv*pow(3*inv,k,q)*pow(n,-1,q)%q for k in range(degree+1)]
        numer=[a*b,-2*a-b,2]+[0]*(degree-2)
        u.append(product(product(u[-1],numer,q),den,q))
    return u

def operator(u,p,index,lo,hi):
    m=(p-1)//6; q=p*p; ph=p*pow(2,-1,q)%q
    terms={}
    for r in range(lo,hi+1):
        def jet(k):return u[r][k] if k>=0 else 0
        f=jet(index); g=jet(index-1); h=jet(index-2)
        terms[r]=(terms.get(r,0)+r*(r-ph)*f-3*r*g)%q
        terms[r+1]=(terms.get(r+1,0)-(r-m)*(r-2*m)*f
                    +(3*r-4*m)*g-2*h)%q
    return {r:x for r,x in terms.items() if x%q}

def check(p):
    m=(p-1)//6; q=p*p; J=2*m; K=p-J; u=jets(p)
    for a in range(5):
        low=(2*m*m*(a==0)+4*m*(a==1)+2*(a==2))%q
        high=((2*m*u[J][a-1] if a>=1 else 0)
              -(2*u[J][a-2] if a>=2 else 0))%q
        expect={i:x for i,x in [(1,low),(J+1,high)] if x%q}
        assert operator(u,p,a,1,J)==expect,(p,'low',a)
    for b in range(5):
        BK=(K-1-m)*(K-1-2*m); CK=3*(K-1)-4*m
        BP=(p-1-m)*(p-1-2*m); CP=3*(p-1)-4*m
        Lam=(BK*u[K-1][b]-(CK*u[K-1][b-1] if b>=1 else 0)
             +(2*u[K-1][b-2] if b>=2 else 0))%q
        cut=(-BP*u[p-1][b]+(CP*u[p-1][b-1] if b>=1 else 0)
             -(2*u[p-1][b-2] if b>=2 else 0))%q
        expect={i:x for i,x in [(K,Lam),(p,cut)] if x%q}
        assert operator(u,p,b,K,p-1)==expect,(p,'high',b)
    factu=2*(-1)**m*factorial(m)*factorial(2*m)*factorial(3*m-1)*factorial(2*m-1)*pow(factorial(4*m),-2,p)%p
    assert u[4*m][2]%p==factu
    Lam2=6*m*m*u[4*m][2]%p
    assert Lam2!=0
    cut2=-(p-1-m)*(p-1-2*m)*u[p-1][2]%p
    assert cut2==(p-2)%p
    def H(n):return sum(pow(i,-1,p) for i in range(1,n+1))%p
    for r in range(2*m+1,p):
        E=(H(m)-H(r-m-1)+2*H(2*m)-2*H(r-2*m-1)+3*H(r))%p
        assert u[r][3]%p==u[r][2]*E%p,(p,'harmonic',r)
    E=(H(m)-H(3*m-1)+pow(m,-1,p)+3*H(4*m))%p
    Lam3=(6*m*m*u[4*m][3]-8*m*u[4*m][2])%p
    assert Lam3==u[4*m][2]*(6*m*m*E-8*m)%p
    assert (Lam3==0)==(E==4*pow(3*m,-1,p)%p)
    return Lam2,cut2

if __name__=='__main__':
    results={p:check(p) for p in primes(997)}
    assert len(results)==80
    print('PASS: 80 target primes; 5 Hasse ranks; both strip identities, factorial and harmonic flux')
    print('p=13:',results[13])
