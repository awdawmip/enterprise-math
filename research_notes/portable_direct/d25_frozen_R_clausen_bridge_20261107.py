#!/usr/bin/env python3
"""Finite exact checks of frozen reflected R versus independent Clausen K; author-side."""
from math import isqrt

def primes_below(limit):
    sieve=bytearray(b'\x01')*limit
    sieve[:2]=b'\x00\x00'
    for i in range(2,isqrt(limit-1)+1):
        if sieve[i]: sieve[i*i::i]=b'\x00'*len(sieve[i*i::i])
    return [n for n in range(limit) if sieve[n]]

def check(p):
    assert p>3 and p%6==1
    m=(p-1)//6; mod=p**3
    B=[1]; A=[1]
    for k in range(p-1):
        B.append(B[-1]*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,mod)%mod)
        A.append(A[-1]*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,mod)%mod)
    g=sum(B)%mod
    h=sum((12*k+1)*b for k,b in enumerate(B))%mod
    W=sum((6*k+1)*a for k,a in enumerate(A))%mod
    c=pow(10,-1,p); sc=sr=0; R=0
    t=pow(10,-1,p); K=0; alpha=beta=0; Kdirect=0
    for i in range(1,m+1):
        if i>1:
            ell=i-1
            c=c*36*ell*ell*pow((6*ell+5)*(3*ell+2),-1,p)%p
            t=t*18*ell*ell*pow((6*ell+5)*(3*ell+2),-1,p)%p
        sc=(sc+c)%p; sr=(sr+i*c)%p
        R=(R+2*B[i]*((6*i+1)*sc-6*sr))%p
        assert c==pow(2,i-1,p)*t%p
        alpha=(alpha+pow(2,i,p)*t)%p
        beta=(beta+i*pow(2,i,p)*t)%p
        K=(K+B[i]*((6*i+1)*alpha-6*beta))%p
        if p<=373:
            hi=pow(10,-1,p); subtotal=0
            for ell in range(1,i+1):
                if ell>1:
                    e=ell-1
                    hi=hi*18*e*e*pow((6*e+5)*(3*e+2),-1,p)%p
                subtotal+=(6*(i-ell)+1)*pow(2,ell,p)*hi
            Kdirect=(Kdirect+B[i]*subtotal)%p
    if p<=373: assert K==Kdirect,(p,'Kdouble',K,Kdirect)
    assert R==K,(p,R,K)
    assert (g*h-W)%mod==(p*p*R)%mod,(p,'tail',g*h%mod,W,R)
    if p%24 in (13,19):
        assert g%p==0,(p,'g')
        G=(g//p)%(p*p)
        assert G*h%p==1,(p,'UR')
        Delta=((G*h%(p*p))-1)//p%p
        Z=((W-p)%mod//(p*p))%p
        assert Delta==(R+Z)%p,(p,Delta,R,Z)
        return p,R,K,Delta,Z,W
    return p,R,K,None,None,W

def main():
    all_p=[p for p in primes_below(5000) if p%6==1]
    results={p:check(p) for p in all_p}
    target=[p for p in all_p if p%24 in (13,19)]
    assert len(all_p)==330 and len(target)==166
    print('ALL',len(all_p),'R=K; gh-W=p²R PASS')
    print('TARGET',len(target),'Delta-R=(W-p)/p² PASS')
    for p in (13,19,37,43,61,67,373):
        print('WITNESS',results[p])
if __name__=='__main__':main()
