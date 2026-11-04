#!/usr/bin/env python3
"""Exact modular wall-graded finite Green certificate; standard library only."""
from math import isqrt, comb

def primes_upto(limit):
    v=bytearray(b'\1')*(limit+1)
    v[:2]=b'\0\0'
    for j in range(2,isqrt(limit)+1):
        if v[j]:
            v[j*j::j]=b'\0'*((limit-j*j)//j+1)
    return [p for p in range(7,limit+1) if v[p] and p%6==1]

def ord_p(n,p):
    if not n: return 999
    v=0
    while n%p==0:
        n//=p;v+=1
    return v

def check_one(p,verbose=False):
    mod=p**3;N=p-1
    a=[1]+[0]*N;b=[1]+[0]*N;r=[0]*N;g=[0]*N
    inv36=pow(36,-1,mod);inv576=pow(576,-1,mod);inv288=pow(288,-1,mod)
    for j in range(N):
        u=pow(j+1,-3,mod)
        ar=(2*j+1)*(3*j+1)*(3*j+2)*u*inv36%mod
        r[j]=(4*j+1)*(4*j+2)*(4*j+3)*u*inv576%mod
        g[j]=(2*j+1)*(56*j*(j+1)+13)*u*inv288%mod
        a[j+1]=a[j]*ar%mod;b[j+1]=b[j]*r[j]%mod
        assert ar==(r[j]+g[j])%mod
    if p in (13,19,97,373):
        for j in range(p):
            assert a[j]==(comb(2*j,j)**2*comb(3*j,j)*pow(216,-j,mod))%mod
            assert b[j]==(comb(2*j,j)**2*comb(4*j,2*j)*pow(2304,-j,mod))%mod
    z1,z2,z3=p//4+1,p//2+1,3*p//4+1
    walls={z1,z2,z3}
    assert len(walls)==3
    for n in range(1,p):
        assert (r[n-1]%p==0)==(n in walls)
        assert ord_p((4*n-3)*(4*n-2)*(4*n-1),p)==int(n in walls)
    full=[0]*N; km=[[0]*N for _ in range(3)]
    for j in range(N-1,-1,-1):
        term=6*(j+1)+1
        if j==N-1:
            full[j]=term%mod;km[0][j]=term%mod
            continue
        q=r[j+1];z=int(j+2 in walls)
        full[j]=(term+q*full[j+1])%mod
        km[0][j]=(term+(q*km[0][j+1] if z==0 else 0))%mod
        for m in (1,2):
            km[m][j]=(q*km[m-z][j+1] if m>=z else 0)%mod
    es=[2*j//p+3*j//p+ord_p((2*j+1)*(56*j*(j+1)+13),p) for j in range(N)]
    C={(e,m):0 for e in range(3) for m in range(3-e)}
    for j,e in enumerate(es):
        f=a[j]*g[j]%mod
        if e<3:
            for m in range(3-e):
                C[e,m]=(C[e,m]+f*km[m][j])%mod
        assert f*(full[j]-sum(k[j] for k in km))%mod==0
        assert (a[j+1]-b[j+1]-r[j]*(a[j]-b[j])-f)%mod==0
    def prefix(B):
        P=[0]*B;P[B-1]=1
        for j in range(B-2,-1,-1):P[j]=r[j+1]*P[j+1]%mod
        return P
    P1,P2,P3=prefix(z1),prefix(z2),prefix(z3)
    def tail(start,stop):
        prod=1;total=0
        for n in range(start,stop):
            total=(total+(6*n+1)*prod)%mod
            if n<stop-1:prod=prod*r[n]%mod
        return total
    T0,T1,T2=tail(z1,z2),tail(z2,z3),tail(z3,p)
    early=sum(a[j]*g[j]*P2[j] for j in range(z1-1) if es[j]==0)%mod
    late=sum(a[j]*g[j]*P3[j] for j in range(z1-1,2*((p-1)//6)+1) if es[j]==0)%mod
    x10=sum(a[j]*g[j]*P1[j] for j in range(z1-1) if es[j]==1)%mod
    x11=sum(a[j]*g[j]*P2[j] for j in range(z1-1,z2-1) if es[j]==1)%mod
    J=z1-1;K=2*((p-1)//6)
    late_all=sum(a[j]*g[j]*P3[j] for j in range(J,K+1))%mod
    late_end=(a[K+1]*P3[K]-a[J]*r[J]*P3[J])%mod
    assert late==late_all==late_end==0
    early_all=sum(a[j]*g[j]*P2[j] for j in range(z1-1))%mod
    boundary=(a[z1-1]*P2[z1-2]-b[z2])%mod
    assert early==early_all==boundary
    assert C[0,2]==boundary*T1%mod
    assert C[1,1]==(x10*T0+x11*T1)%mod
    assert early%p**2==late%p**2==x10%p**2==x11%p**2==0
    Q=[2*sum(n*b[n] for n in range(p) if 4*n//p==e)%mod for e in range(3)]
    assert all(n*b[n]%mod==0 for n in range(p) if 4*n//p>=3)
    direct=sum((6*n+1)*a[n]-(8*n+1)*b[n] for n in range(p))%mod
    assert (sum(C.values())-sum(Q))%mod==direct
    assert (sum(a[j]*g[j]*full[j] for j in range(N))-sum(Q))%mod==direct
    if verbose:
        print("p",p,"walls",sorted(walls),"C02",C[0,2],"C11",C[1,1],
              "tails mod p",(T0%p,T1%p,T2%p),"W-V",direct)
    return direct

if __name__=="__main__":
    ps=primes_upto(2000)
    for p in ps:check_one(p,p in (13,19,97,373))
    print("PASS primes=%d wall_channels=6 exact_mod_p3=TRUE"%len(ps))
