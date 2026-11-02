#!/usr/bin/env python3
"""Source-preserving arbitrary Euler-polynomial observer on Clausen defect.
Author-side exact Z/p^3Z execution; no native Source experiment.
"""
from math import comb, isqrt

def primes(bound):
    sieve=bytearray(b'\x01')*(bound+1); sieve[0]=sieve[1]=0
    for a in range(2,isqrt(bound)+1):
        if sieve[a]: sieve[a*a::a]=b'\x00'*(((bound-a*a)//a)+1)
    return [p for p in range(7,bound+1) if sieve[p] and p%6==1]

def check(p, degree=4):
    r=(p-1)//6; m3=p**3; inv2=pow(2,-1,m3); inv18=pow(18,-1,m3)
    h=[1]*p; a=[1]*p; powers=[1]*p
    for k in range(1,p):
        invk=pow(k,-1,m3); powers[k]=powers[k-1]*inv2%m3
        h[k]=h[k-1]*(6*k-5)*(3*k-2)*inv18*invk**2%m3
        a[k]=a[k-1]*(2*k-1)*(3*k-2)*(3*k-1)*inv18*invk**3%m3
    H=[sum((k**d)*h[k]*powers[k] for k in range(p))%m3 for d in range(degree+1)]
    F=[sum((k**d)*a[k]*powers[k] for k in range(p))%m3 for d in range(degree+1)]
    direct=[]
    for d in range(degree+1):
        delta=(sum(comb(d,t)*H[t]*H[d-t] for t in range(d+1))-F[d])%m3
        assert delta%(p*p)==0,(p,d)
        direct.append(delta//(p*p))
    suffix=[[0]*(r+2) for _ in range(degree+1)]
    for j in range(r,0,-1):
        w=h[j]*pow(2,-j,p)%p
        for t in range(degree+1):suffix[t][j]=(suffix[t][j+1]+pow(j,t,p)*w)%p
    c=pow(18*(r+1)*(2*r+1),-1,p)
    quick=[0]*(degree+1)
    for s in range(1,r+1):
        w=c*pow(2,s,p)%p
        for d in range(degree+1):
            inner=sum(comb(d,t)*pow(-s,d-t,p)*suffix[t][s] for t in range(d+1))%p
            quick[d]=(quick[d]+w*inner)%p
        if s<r:c=c*s*s*pow((r+s+1)*(2*r+s+1),-1,p)%p
    assert direct==quick,(p,direct,quick)
    return quick

def main():
    ps=primes(3000)
    for p in ps:check(p)
    print('PASS: all',len(ps),'p=1(mod6) primes <=3000, Euler degrees d=0,1,2,3,4; independent product derivative and suffix moments mod p^3')
    for p in [7,13,19,31,37,43,61,373,1171]:print('CERT',p,'D0..D4',check(p))
    print('RESEARCH STATUS: AUTHOR-DERIVED / EXACT-PROVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING')
if __name__=='__main__':main()
