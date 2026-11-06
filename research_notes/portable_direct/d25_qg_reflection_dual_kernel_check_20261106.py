#!/usr/bin/env python3
"""Finite exact validator for D25 q/g anti-diagonal first integral.
Author-side arithmetic only, not original native H0/B0 execution."""
from math import isqrt

def ps_to(limit):
    return [n for n in range(7,limit+1) if n%6==1
            and all(n%d for d in range(2,isqrt(n)+1))]

def check(p):
    m=(p-1)//6
    assert p==6*m+1 and all(p%d for d in range(2,isqrt(p)+1))
    z=p**3
    a=[1]
    for n in range(1,p):
        a.append(a[-1]*(2*n-1)*(3*n-2)*(3*n-1)
                 *pow(36*n**3,-1,z)%z)
    q=[1]
    for j in range(1,m):
        q.append(q[-1]*3*j*(6*j+1)*(3*j+1)
                 *pow(4*(3*j+2)**3,-1,p*p)%(p*p))
    g=[1]
    for t in range(1,m):
        g.append(g[-1]*t*(6*t-1)*(6*t+1)
                 *pow(9*(2*t+1)**3,-1,p)%p)
    qtop=q[-1]%p
    a2=a[2*m]%p
    D=sum((2*j-1)*pow((3*j-1)**3*q[j-1],-1,p)
          for j in range(1,m+1))%p
    G=sum((6*t+4)*g[t] for t in range(m))%p
    for j in range(1,m+1):
        assert ((3*j-1)**3*q[j-1]*g[m-j]+27*pow(8,-1,p)*qtop)%p==0,(p,j)
        c=a[4*m+1-j]//p**2%p
        predicted=3*a2*qtop**2*pow(512*(3*j-1)**3*q[j-1],-1,p)%p
        assert c==predicted,(p,j,'C')
    assert a[4*m]//p**2%p==3*a2*qtop**2*pow(4096,-1,p)%p
    assert G==81*pow(8,-1,p)*qtop*D%p
    shell=sum((6*n+1)*a[n] for n in range(3*m+1,4*m+1))%z
    assert shell==(-9*p*p*a2*qtop*qtop*D*pow(512,-1,p))%z
    sig=Q0=Q1=0
    for j in range(m):
        if j:
            sig=(sig+2*pow(6*j+1,-1,p)+pow(3*j,-1,p)
                 +pow(3*j+1,-1,p)-3*pow(3*j+2,-1,p))%p
        Q0=(Q0+(6*j+5)*q[j])%(p*p)
        Q1=(Q1+q[j]*(2+(6*j+5)*(3*pow(2,-1,p)+sig)))%p
    prefix=sum((6*n+1)*a[n] for n in range(2*m+1))%z
    middle=p*a[2*m]*pow(32,-1,z)*(Q0+p*Q1)%z
    W=sum((6*n+1)*a[n] for n in range(p))%z
    assert W==(prefix+middle+shell)%z,(p,'W',W)
    return (p,m,qtop,a[4*m]//p**2%p,G,D,shell//p**2,W)

def main():
    primes=ps_to(1999)+[5113]
    assert len(primes)==149
    for p in primes:
        result=check(p)
        if p in (19,373,5113):print('WITNESS',result)
    print('ALL_PASS primes=149 pairs=',sum((p-1)//6 for p in primes))

if __name__=="__main__":main()
