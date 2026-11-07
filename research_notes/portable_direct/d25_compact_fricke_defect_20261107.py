#!/usr/bin/env python3
"""D25 source-labelled p^3 A/B defect audit. Portable exact finite-ring check."""
from math import isqrt
from d25_a_short_overflow_20261107 import data as adata,carry as acarry,compact as acompact

def primes(n):
    for p in range(7,n):
        if p%24 in (13,19) and all(p%d for d in range(2,isqrt(p)+1)):yield p

def series(p,mod,params,stop):
    out=[1];den=1
    for a,b in params:den*=a
    for i in range(stop):
        num=1
        for a,b in params:num*=a*i+b
        out.append(out[-1]*num*pow(den*(i+1)**len(params),-1,mod)%mod)
    return out

def weighted(u,x,c,mod):
    r=0;xp=1
    for i,a in enumerate(u):r=(r+(1+c*i)*a*xp)%mod;xp=xp*x%mod
    return r

def lowjet(u,p,x,c,mod,euler):
    sq=[0]*p
    for i,a in enumerate(u):
        for j,b in enumerate(u):
            if i+j<p:sq[i+j]=(sq[i+j]+a*b)%mod
    if euler:sq=[(sq[i]-(sq[i-1] if i else 0))%mod for i in range(p)]
    return weighted(sq,x,c,mod)

def compact_b(p):
    k=(p-3)//8 if p%8==3 else (p-5)//8
    inv=lambda a:pow(a%p,-1,p)
    q=[1]
    for i in range(k):q.append(q[-1]*(k-i)*(3*k+1-i)*inv((i+1)**2)%p)
    r=[3*inv(64*(k+1)*(3*k+2))%p]
    J=5*k if p%8==3 else 5*k+2
    for j in range(J):r.append(r[-1]*(j+1)**2*inv((k+j+2)*(3*k+j+3))%p)
    h=[]
    for ell in range(k+1):
        v=sum(q[j+ell+1]*r[j] for j in range(k-ell)) if ell<k else 0
        if p%8==5:v-=sum(q[j+ell]*r[j] for j in range(k-ell+1))
        h.append(v%p)
    x=pow(9,-1,p)
    assert sum(v*pow(x,i,p) for i,v in enumerate(q))%p==0
    dq=sum(i*v*pow(x,i,p) for i,v in enumerate(q))%p
    rx=sum(v*pow(x,p-1-j,p) for j,v in enumerate(r))%p
    hx=sum(v*pow(x,i,p) for i,v in enumerate(h))%p
    dh=sum(i*v*pow(x,i,p) for i,v in enumerate(h))%p
    return (16*(1-x if p%8==5 else 1)*dq*rx-2*x*(hx+8*dh))%p

def run(p):
    mod=p**3;m=(p-1)//6;k=(p-3)//8 if p%8==3 else (p-5)//8
    xa=pow(2,-1,mod);xb=pow(9,-1,mod)
    W=weighted(series(p,mod,[(2,1),(3,1),(3,2)],p-1),xa,6,mod)
    V=weighted(series(p,mod,[(4,1),(2,1),(4,3)],p-1),xb,8,mod)
    f=series(p,mod,[(6,1),(3,1)],2*m)
    g=series(p,mod,([(8,1),(8,3)] if p%8==3 else [(8,5),(8,7)]),3*k+1)
    GA=lowjet(f,p,xa,6,mod,False)
    GB=lowjet(g,p,xb,8,mod,p%8==5)
    _,q,r=adata(p)
    EA=acompact(p,q,r,acarry(p,q,r),pow(2,-1,p))[0]
    EB=compact_b(p)
    assert (W-GA)%mod==p*p*EA%mod and (V-GB)%mod==p*p*EB%mod
    assert (GA-GB)% (p*p)==0
    gamma=((GA-GB)%mod)//(p*p)
    assert W==V==p and (gamma+EA-EB)%p==0,(p,W,V,gamma,EA,EB)
    return gamma,EA,EB

def main():
    samples={}
    P=list(primes(2500))
    for p in P:
        z=run(p)
        if p in(13,19,43,67,373,997):samples[p]=z
    assert len(P)==94 and samples[373]==(219,1,220)
    print("PASS finite p^3 source split",len(P),"target primes p<2500")
    print(samples)
if __name__=="__main__":main()
