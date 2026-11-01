#!/usr/bin/env python3
"""D25 focused exact checks. Integer/modular arithmetic only; no native H0/B0."""
def primes(N):
    S=[True]*(N+1)
    S[0]=S[1]=False
    for i in range(2,int(N**.5)+1):
        if S[i]:
            for j in range(i*i,N+1,i): S[j]=False
    return [p for p in range(7,N+1) if S[p] and p%6==1]
def coeffs(p,M):
    u=[1]
    for n in range(1,p):
        u.append(u[-1]*(6*n-5)*(3*n-2)*pow(18*n*n,-1,M)%M)
    return u
def legendre_pair(n,p):
    inv2=pow(2,-1,p);a=(1,0);b=(0,1)
    if n==1:return b,a
    for k in range(1,n):
        xb=(b[1]*inv2%p,b[0])
        t=pow(k+1,-1,p)
        a,b=b,tuple(((2*k+1)*xb[j]-k*a[j])*t%p for j in range(2))
    return b,a
def run_prime(p):
    M=p**3;u=coeffs(p,M);half=pow(2,-1,M)
    s=d=0;term=1
    for n,v in enumerate(u):
        s=(s+v*term)%M;d=(d+n*v*term)%M;term=term*half%M
    r=(p-1)//6
    a=1;b=1
    for k in range(r+1):
        assert a==b,(p,k,a,b)
        if k<r:
            a=a*(6*k+1)*(3*k+1)*pow(18*(k+1)**2,-1,p)%p
            b=b*(k-r)*(2*r+2*k+1)*pow(2*(k+1)**2,-1,p)%p
    P,prev=legendre_pair(2*r,p)
    assert P[1]==0 and prev[0]==0
    B=prev[1]
    assert s%p==P[0] and d%p==r*(P[0]-B)%p
    if s%p!=0:return p%24,False,False
    assert d%p and B
    a0=(s//p)%p;a1=(s//(p*p))%p;d0=d%p;d1=(d//p)%p
    delta=(-a0*pow(2*d0,-1,p))%p
    carry=(a0+2*delta*d0)//p
    delta1=(-(carry+a1+2*delta*d1-delta*delta*d0)*pow(2*d0,-1,p))%p
    z=(half+p*delta+p*p*delta1)%M
    v=1;power=1;root=0
    for n in range(p):
        root=(root+u[n]*power)%M;power=power*z%M
    assert root==0
    # Original 216 cutoff (independently computed).
    v=1;power=1;W=0
    for n in range(p):
        W=(W+(6*n+1)*v*power)%M
        if n<p-1:
            v=v*(2*n+1)*(3*n+1)*(3*n+2)*pow(18*(n+1)**3,-1,M)%M
            power=power*half%M
    T=(s*s+12*s*d-W)%M
    assert T%(p*p)==0
    C=T//(p*p)
    first=(12*a0*d0-1)%p==0
    assert first==(W%(p*p)==p)
    assert first==((-24*delta*d0*d0-1)%p==0)
    if first:
        c2=(-24*delta*d0*d0-1)//p
        second=(c2-48*delta*d0*d1-24*delta1*d0*d0+16*delta*delta*d0*d0-C)%p
        assert (second==0)==(W==p)
    return p%24,True,W==p
def inverse_check(p):
    c=6*p-5; q=(c+6)*pow(c,-1,p)%p
    b=[pow(c,-1,p),(q-2)*pow(c,-1,p)%p]
    for d in range(2,p):b.append(36*pow(q,d-2,p)*pow(c,-3,p)%p)
    M=[[((6*(i+j)+1)*pow(2,-i-j,p)%p) if i+j<p else 0 for j in range(p)] for i in range(p)]
    V=[[(pow(2,i+j,p)*b[i+j-p+1])%p if i+j>=p-1 else 0 for j in range(p)] for i in range(p)]
    assert all(sum(M[i][j]*V[j][k] for j in range(p))%p==(i==k) for i in range(p) for k in range(p))
if __name__=="__main__":
    rows=[run_prime(p) for p in primes(3000)]
    for class24 in (1,7,13,19):
        q=[r for r in rows if r[0]==class24]
        print("CLASS",class24,"count",len(q),"zeros",sum(x[1] for x in q),"216-pass",sum(x[2] for x in q))
    for p in (7,13,19,37):inverse_check(p)
    print("PASS",len(rows),"prime Legendre/jet checks; 4 full inverse checks")