#!/usr/bin/env python3
"""W216 p^3 six-port verifier. Integer modular arithmetic only."""
from math import comb, isqrt

def primes(n):
    z=bytearray([1])*(n+1)
    z[0]=z[1]=0
    for t in range(2,isqrt(n)+1):
        if z[t]:
            z[t*t::t]=bytes([0])*len(z[t*t::t])
    return [p for p in range(7,n+1) if z[p] and p%6==1]

def verify(p):
    assert p%6==1
    r=(p-1)//6; h=4*r; mod=p**3
    i2=pow(2,-1,mod); i3=pow(3,-1,mod)
    f=[1]*(h+1)
    for i in range(1,h+1):f[i]=f[i-1]*i%mod
    fi=[1]*(h+1)
    fi[h]=pow(f[h],-1,mod)
    for ii in range(h,0,-1): fi[ii-1]=fi[ii]*ii%mod
    H=[0]*(h+1)
    for ii in range(1,h+1): H[ii]=(H[ii-1]+pow(ii,-1,mod))%mod
    p2=[pow(i2,k,mod) for k in range(h+1)]
    a=1; direct=[0,0,0]
    for k in range(h+1):
        b=0 if k<=2*r else 1 if k<=3*r else 2
        direct[b]=(direct[b]+(6*k+1)*a)%mod
        if k<h:
            a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,mod)%mod
    low=mid=high=0; S0=S1=S2=0
    L=Qsum=0
    for k in range(2*r+1):
        if k:
            j=k-1
            vals=[pow(2*(j-3*r),-1,mod),pow(3*(j-2*r),-1,mod),2*pow(3*(j-4*r),-1,mod)]
            L=(L+sum(vals))%mod
            Qsum=(Qsum+sum(v*v for v in vals))%mod
        T=(-1 if k%2 else 1)*p2[k]*comb(3*r,k)*comb(2*r,k)*comb(4*r,k)%mod
        Q=(L*L-Qsum)*i2%mod
        v=(6*k+1)*T%mod
        S0=(S0+v)%mod
        S1=(S1+v*L)%mod
        S2=(S2+v*Q)%mod
        low=(low+v*(1+p*L+p*p*Q))%mod
    for k in range(2*r+1,3*r+1):
        T=f[2*r]*f[k-2*r-1]*f[3*r]*f[4*r]*i3*p2[k]%mod
        T=T*fi[k]**3*fi[3*r-k]*fi[4*r-k]%mod
        ell=(-i2*(H[3*r]-H[3*r-k])
             +i3*(-H[2*r]+H[k-2*r-1])
             -2*i3*(H[4*r]-H[4*r-k]))%mod
        v=(6*k+1)*T%mod
        S1=(S1+v)%mod; S2=(S2+v*ell)%mod
        mid=(mid+p*v*(1+p*ell))%mod
    for k in range(3*r+1,4*r+1):
        T=(-1 if (r+k)%2 else 1)*f[3*r]*f[k-3*r-1]*f[2*r]*f[k-2*r-1]*f[4*r]*pow(6,-1,mod)*p2[k]%mod
        T=T*fi[k]**3*fi[4*r-k]%mod
        v=(6*k+1)*T%mod
        S2=(S2+v)%mod
        high=(high+p*p*v)%mod
    total=(low+mid+high)%mod
    assert [low,mid,high]==direct,(p,[low,mid,high],direct)
    assert total==(S0+p*S1+p*p*S2)%mod,(p,total)
    return total, [low,mid,high],(S0,S1,S2)

if __name__=="__main__":
    pp=primes(3000)
    for p in pp:
        total, bands, ports=verify(p)
        assert total==p%p**3,(p,total)
    print("all",len(pp),"prime checks passed, exact band and six-port tests")
    for p in (13,19,373):
        print(p,verify(p))
