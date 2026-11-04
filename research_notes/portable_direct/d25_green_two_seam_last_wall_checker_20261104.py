#!/usr/bin/env python3
"""Check last-crossed-wall Green theorem and p^3 two-seam compression.
Only Python standard library. Source families rebuilt from ORIGINAL ratios.
"""
from math import comb, isqrt
from fractions import Fraction

def prime_list(limit=2000):
    sieve=bytearray(b'\x01')*(limit+1)
    sieve[:2]=b'\x00\x00'
    for d in range(2,isqrt(limit)+1):
        if sieve[d]:
            sieve[d*d::d]=b'\x00'*((limit-d*d)//d+1)
    return [p for p in range(7,limit+1) if sieve[p] and p%6==1]

def check_mod(p):
    mod=p**3
    a=[1]*p; b=[1]*p
    rho=[0]*(p-1); f=[0]*(p-1)
    for j in range(p-1):
        inv=pow(j+1,-3,mod)
        rho[j]=(4*j+1)*(4*j+2)*(4*j+3)*inv*pow(576,-1,mod)%mod
        gamma=(2*j+1)*(56*j*(j+1)+13)*inv*pow(288,-1,mod)%mod
        a_step=(2*j+1)*(3*j+1)*(3*j+2)*inv*pow(36,-1,mod)%mod
        assert (rho[j]+gamma)%mod==a_step
        f[j]=a[j]*gamma%mod
        a[j+1]=a[j]*a_step%mod
        b[j+1]=b[j]*rho[j]%mod
    if p in (13,19,97,373):
        for j in range(p):
            assert a[j]==comb(2*j,j)**2*comb(3*j,j)*pow(216,-j,mod)%mod
            assert b[j]==comb(2*j,j)**2*comb(4*j,2*j)*pow(2304,-j,mod)%mod
    h=(p-1)//2
    L=p//4+1; M=h+1; R=3*p//4+1
    walls={L,M,R}
    assert {n for n in range(1,p) if rho[n-1]%p==0}==walls
    km=[[0]*(p-1) for _ in range(3)]
    for j in range(p-2,-1,-1):
        if j==p-2:
            km[0][j]=6*(p-1)+1
            continue
        z=int(j+2 in walls)
        rr=rho[j+1]
        km[0][j]=(6*(j+1)+1+(rr*km[0][j+1] if z==0 else 0))%mod
        for m in (1,2):
            km[m][j]=(rr*km[m-z][j+1] if m>=z else 0)%mod
    C1=sum(f[j]*km[1][j] for j in range(p-1))%mod
    C2=sum(f[j]*km[2][j] for j in range(p-1))%mod
    G0=sum(f[j]*km[0][j] for j in range(p-1))%mod
    def tail(start,stop):
        product=1
        result=0
        for n in range(start,stop):
            result=(result+(6*n+1)*product)%mod
            if n+1<stop:
                product=product*rho[n]%mod
        return result
    T0=tail(L,M); T1=tail(M,R)
    E0=(a[L-1]*rho[L-1]-b[L])%mod
    E1=(a[h]*rho[h]-b[M])%mod
    chi=1 if pow(6,h,p)==1 else -1
    assert E0%p==0 and E1%(p*p)==0
    assert E1//(p*p)%p == (2*chi-1)*pow(36,-1,p)%p
    S0=E0*T0%mod; S1=E1*T1%mod
    assert (C1+C2-S0-S1)%mod==0
    Q=2*sum(n*b[n] for n in range(p))%mod
    original=sum((6*n+1)*a[n]-(8*n+1)*b[n] for n in range(p))%mod
    assert (G0+S0+S1-Q-original)%mod==0
    if p in (13,19,97,373):
        print(p,dict(cross=(C1+C2)%mod,seam0=S0,seam1=S1,
                     zero=G0,quartic_moment=Q,direct=original,
                     tail0=T0%p,tail1=T1%p))
    return original

def check_exact(p):
    a=[Fraction(1)];b=[Fraction(1)];rho=[];f=[]
    for j in range(p-1):
        r=Fraction((4*j+1)*(4*j+2)*(4*j+3),576*(j+1)**3)
        g=Fraction((2*j+1)*(56*j*(j+1)+13),288*(j+1)**3)
        rho.append(r);f.append(a[-1]*g)
        a.append(a[-1]*(r+g));b.append(b[-1]*r)
    cuts=[p//4+1,(p+1)//2,3*p//4+1]
    direct=Fraction(0)
    for j in range(p-1):
        prod=Fraction(1)
        for n in range(j+1,p):
            if n>j+1:prod*=rho[n-1]
            if any(j<=cut-2 and n>=cut for cut in cuts):
                direct+=f[j]*(6*n+1)*prod
    seams=Fraction(0)
    for i,cut in enumerate(cuts):
        prod=Fraction(1);tail=Fraction(0)
        end=cuts[i+1] if i+1<len(cuts) else p
        for n in range(cut,end):
            if n>cut:prod*=rho[n-1]
            tail+=(6*n+1)*prod
        seams+=rho[cut-1]*(a[cut-1]-b[cut-1])*tail
    assert direct==seams

if __name__=="__main__":
    ps=prime_list()
    for p in ps:check_mod(p)
    for p in (7,13):check_exact(p)
    print("PASS",len(ps),"primes: modular last-wall and 2-seam; exact rational p=7,13")
