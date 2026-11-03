#!/usr/bin/env python3
"""Finite exact source checker for D25 p-k reflection and 216 H2 transport."""
from math import factorial

def primes(bound):
    sieve=[True]*(bound+1)
    sieve[0]=sieve[1]=False
    for n in range(2,int(bound**0.5)+1):
        if sieve[n]:
            for m in range(n*n,bound+1,n):
                sieve[m]=False
    return [n for n in range(5,bound+1) if sieve[n]]

def check(p):
    f=[1]*p
    for i in range(1,p): f[i]=f[i-1]*i%p
    inv=[pow(z,-1,p) for z in f]
    b=[0]*p; c=[0]*p
    vals=[None]*p
    for k in range(p):
        a,x=divmod(2*k,p);d,y=divmod(3*k,p);e,z=divmod(4*k,p)
        vals[k]=(a,d,e)
        b[k]=(-1)**(a+d)*factorial(a)*factorial(d)*f[x]*f[y]*pow(inv[k],5,p)*pow(216,-k,p)%p
        c[k]=(-1)**e*factorial(e)*f[z]*pow(inv[k],4,p)*pow(2304,-k,p)%p
    for k in range(1,p):
        a,d,e=vals[k]
        fb=-(-1)**(a+d)*factorial(d)*factorial(2-d)*pow(36*k**3,-1,p)%p
        fc=-(-1)**e*factorial(e)*factorial(3-e)*pow(576*k**3,-1,p)%p
        assert b[k]*b[p-k]%p==fb,(p,k,"216")
        assert c[k]*c[p-k]%p==fc,(p,k,"2304")
        assert (6*k+1)*(6*(p-k)+1)*fb%p==(1-36*k*k)*fb%p
        assert (8*k+1)*(8*(p-k)+1)*fc%p==(1-64*k*k)*fc%p
        ar,dr,er=vals[p-k]
        assert a+d+ar+dr==3 and e+er==3
        assert (a+d+er,e+ar+dr)==(3+a+d-e,3-a-d+e)
    if p%6==1:
        r=(p-1)//6
        high=sum((6*k+1)*b[k] for k in range(3*r+1,4*r+1))%p
        low=sum((6*j-1)*pow(216,j-1,p)*pow(f[j-1],5,p)
                *inv[2*j-1]*inv[3*j-p-1] for j in range(2*r+1,3*r+1))%p
        assert high==low,(p,"H2")
        return high
    return None

if __name__=="__main__":
    ps=primes(2000)
    hs={}
    for p in ps:
        k=check(p)
        if p in (7,13,19,37,373): hs[p]=k
    print("PASS",len(ps),"primes",sum(p-1 for p in ps),"indices",
          sum(p%6==1 for p in ps),"H2 cases",hs)
