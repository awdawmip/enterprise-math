#!/usr/bin/env python3
"""Exact integer verification: D25 Clausen ports = sextic character moments.
Author evidence only, not a native Source/CLAIM/review.
"""
import math

def prime(n):
    if n<2:return False
    return all(n%q for q in range(2,math.isqrt(n)+1))

def direct(p):
    m=(p-1)//6
    A=B=0
    for k in range(m+1):
        v=math.comb(m,k)*math.comb(2*m,k)*pow(2,-k*(p-2),p)%p
        # since 2^(-k) = (2^{-1})^k, use direct inverse instead
        v=math.comb(m,k)*math.comb(2*m,k)*pow(pow(2,-1,p),k,p)%p
        A=(A+v)%p
        B=(B+(1+12*k)*v)%p
    return A,B

def character(p):
    m=(p-1)//6
    Sa=Sb=Sinv=checks=fix=0
    for t in range(p):
        if (t*t+4*t+2)%p==0: fix+=1
        if t in (0,p-1,p-2):continue
        u=(t+1)*(t+2)**2*pow(t,-1,p)%p
        x=pow(u,m,p)
        w=(2-3*t)*pow(t+2,-1,p)%p
        Sa=(Sa+x)%p
        Sb=(Sb+x*w)%p
        Sinv=(Sinv+pow(x,-1,p))%p
        tt=(-2*(t+1)*pow(t+2,-1,p))%p
        assert tt not in (0,p-1,p-2)
        assert (-2*(tt+1)*pow(tt+2,-1,p))%p==t
        ut=(tt+1)*(tt+2)**2*pow(tt,-1,p)%p
        assert u*ut%p==2
        assert ((2-3*tt)*pow(tt+2,-1,p))%p==(4*t+5)%p
        checks+=1
    assert Sa == pow(2,m,p)*Sinv%p
    assert fix==(2 if pow(2,(p-1)//2,p)==1 else 0)
    c=(-pow(2,-2*m,p))%p
    return c*Sa%p,c*Sb%p,checks,fix

def test(bound=2500):
    n=tot=0
    for p in range(7,bound+1):
        if not (p%6==1 and prime(p)):continue
        a,b=direct(p)
        c,d,checked,fixed=character(p)
        assert (a,b)==(c,d), (p,a,b,c,d)
        assert fixed==(2 if pow(2,(p-1)//2,p)==1 else 0)
        if p in (7,13,19,157,373,1009,2089):
            print("witness",p,a,b,fixed)
        n+=1
        tot+=checked
    assert n==178 and tot==204412
    print("PASS: 178 primes; 204412 T involution comparisons; 178 two-port matches")

if __name__=="__main__":test()
