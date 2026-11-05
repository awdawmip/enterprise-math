#!/usr/bin/env python3
"""D25 independent terminating 4F3 shell validation over F_q."""
from math import isqrt

def primes_to(n):
    a=bytearray([1])*(n+1)
    a[0]=a[1]=0
    for k in range(2,isqrt(n)+1):
        if a[k]:
            for j in range(k*k,n+1,k):a[j]=0
    return [i for i in range(n+1) if a[i]]

def shell_factorial(q):
    eps=1 if q%6==1 else -1; m=(q-eps)//6; d=(1-eps)//2
    a,b,c=2*m-d,3*m-d,4*m-d
    f=[1]*q;fi=[1]*q
    for j in range(1,q):f[j]=f[j-1]*j%q
    fi[-1]=pow(f[-1],-1,q)
    for j in range(q-1,0,-1):fi[j-1]=fi[j]*j%q
    def C(n,k):
        return f[n]*fi[k]%q*fi[n-k]%q
    ans=0; z=pow(-2,-(a+1),q)
    for j in range(a+1,b+1):
        s=(-1 if (j-a-1)%2 else 1)*f[a]*f[j-a-1]*fi[j]%q
        ans=(ans+(6*j+1)*z*s*C(b,j)*C(c,j))%q
        z=z*pow(-2,-1,q)%q
    return ans

def shell_4f3(q):
    eps=1 if q%6==1 else -1; m=(q-eps)//6; d=(1-eps)//2
    a,b,c=2*m-d,3*m-d,4*m-d
    def C(n,k):
        out=1
        for i in range(1,k+1):out=out*(n-i+1)*pow(i,-1,q)%q
        return out
    E0=(-1 if (a+1)%2 else 1)*pow(2,-(a+1),q)*pow(a+1,-1,q)*C(b,a+1)*C(c,a+1)%q
    h=1; tot=0
    for t in range(m):
        tot=(tot+(6*(a+1+t)+1)*h)%q
        if t<m-1:
            h=h*(t+1)*(m-1-t)*(2*m-1-t)*pow(2,-1,q)*pow(a+2+t,-3,q)%q
    return E0*tot%q

if __name__=='__main__':
    primes=[q for q in primes_to(3000) if q>=5]
    assert len(primes)==428
    for q in primes:assert shell_4f3(q)==shell_factorial(q),q
    print('428/428 PASS; independent 4F3 recurrence versus factorial binomial shell')
    print({q:shell_4f3(q) for q in (5,7,11,13,17,19,373,1009,2003)})
