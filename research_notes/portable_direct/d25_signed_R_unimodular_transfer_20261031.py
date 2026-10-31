#!/usr/bin/env python3
"""Exact modular four-port transfer versus original signed double-sum R.
AUTHOR-SIDE / EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED.
Does not implement native H0/B0 or prove the full D25 supercongruence.
"""
from math import comb

def primes_upto(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for i in range(2,int(n**.5)+1):
        if sieve[i]:
            sieve[i*i:n+1:i]=b'\x00'*((n-i*i)//i+1)
    return [p for p in range(7,n+1) if sieve[p]]

def direct(p):
    ell=(p-1)//6
    c=[0]*(ell+1)
    c[1]=pow(10,-1,p)
    for a in range(1,ell):
        c[a+1]=c[a]*36*a*a*pow((6*a+5)*(3*a+2),-1,p)%p
    K=[0]*(ell+1)
    for i in range(1,ell+1):
        K[i]=sum((1+6*(i-a))*c[a] for a in range(1,i+1))%p
    g=[comb(ell,i)*comb(2*ell,i)*pow(2,-i,p)%p for i in range(ell+1)]
    R=2*sum(g[i]*K[i] for i in range(1,ell+1))%p
    return R,c,K,g

def transport(p):
    ell=(p-1)//6
    h=ell*ell*pow(10,-1,p)%p
    v=0
    d=h
    B=2*h%p
    states={1:(h,v,d,B)}
    for i in range(1,ell):
        r=36*i*i*pow((6*i+5)*(3*i+2),-1,p)%p
        q=(ell-i)*(2*ell-i)*pow(2*(i+1)**2,-1,p)%p
        hnew=q*(2*h-v+(5+r)*d)%p
        vnew=q*h%p
        dnew=q*r*d%p
        B=(B+2*hnew)%p
        h,v,d=hnew,vnew,dnew
        states[i+1]=(h,v,d,B)
    return B,states

def check(p):
    ell=(p-1)//6
    R,c,K,g=direct(p)
    T,states=transport(p)
    assert T==R,(p,'final R',T,R)
    for i in range(1,ell+1):
        H,V,C,B=states[i]
        assert H==g[i]*K[i]%p
        assert V==g[i]*K[i-1]%p
        assert C==g[i]*c[i]%p
        assert B==2*sum(g[j]*K[j] for j in range(1,i+1))%p
    D=lambda i:(6*i+5)*(3*i+2)
    E=lambda i:5*D(i)+36*i*i
    W=lambda i:(K[i+1]-2*K[i]+K[i-1])%p
    for i in range(1,ell-1):
        r=36*i*i*pow(D(i),-1,p)%p
        assert W(i)==(5+r)*c[i]%p
        assert D(i+1)*E(i)*W(i+1)%p==36*i*i*E(i+1)*W(i)%p
    degenerate=[i for i in range(1,ell-1) if E(i)%p==0]
    for i in degenerate:
        assert c[i]!=0 and W(i)==0
    return p,ell,R,degenerate

def main():
    out=[check(p) for p in primes_upto(1200) if p%6==1]
    target=sum(p%24 in (13,19) for p,*_ in out)
    singular=sum(bool(ids) for _,_,_,ids in out)
    print('ALL_PRIMES',len(out),'FROZEN_TARGET',target,'E_SINGULAR',singular)
    for p,ell,R,ids in out:
        if p in (7,13,19,37,43,67,103,211,373):
            print('ANCHOR',p,ell,R,ids)
    print('PASS_D25_SIGNED_R_UNIMODULAR_FOUR_PORT_TRANSFER')
if __name__=='__main__':main()
