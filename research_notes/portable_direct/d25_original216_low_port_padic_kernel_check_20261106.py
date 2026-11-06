#!/usr/bin/env python3
"""Exact integer-only low-port 216/CM transfer checker; no native H0/B0 claims."""
from math import comb, isqrt
import json

def primes(n):
    return [p for p in range(7,n+1) if all(p%d for d in range(2,isqrt(p)+1))]

def check(p):
    m=(p-1)//6; mod=p**6; q=p*p
    b=[0]*(p+1); b[0]=1
    for n in range(1,p):
        b[n]=b[n-1]*6*(6*n-5)*(3*n-2)*pow(n*n,-1,mod)%mod
    assert b[p-1]%p**2==0
    bp=b[p-1]//p**2*6*(6*p-5)*(3*p-2)%p**3
    a=[comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,q)%q for k in range(2*m+1)]
    h=[0]*(2*m+1); s=[0]*(2*m+1)
    h[1]=108*pow(5,-1,q)%q
    for k in range(1,2*m):
        s[k+1]=(s[k]-2*pow(k,-1,q)+6*pow(6*k+5,-1,q)+3*pow(3*k+2,-1,q))%q
        h[k+1]=h[k]*36*k*k*pow((6*k+5)*(3*k+2),-1,q)%q
    beta=3*pow(2,-1,p)*sum(k*a[k]*h[k] for k in range(1,2*m+1))%p
    assert (bp-6)%p==0 and beta==((bp-6)//p)%p
    shift=beta*pow(6,-1,q)+27*pow(10,-1,q)
    for k in range(1,2*m+1):
        predicted=h[k]*(1+p*(shift+s[k]))%q
        actual=pow(216,k,q)*(b[p-k]//p**2)%q
        assert predicted==actual,(p,k,predicted,actual)
        t=comb(2*k,k)**2*comb(3*k,k)*b[p-k]//p**2%q
        assert a[k]*predicted%q==t
    return {'p':p,'beta':beta,'lambda_1':h[1]*(1+p*shift)%q,
            'lambda_m':pow(216,m,q)*(b[p-m]//p**2)%q,
            'lambda_2m':pow(216,2*m,q)*(b[p-2*m]//p**2)%q}

if __name__=='__main__':
    result=[check(p) for p in primes(997) if p%6==1]
    assert len(result)==80
    print(json.dumps({'count':len(result),'all_pass':True,
      'beta_zero_count':sum(r['beta']==0 for r in result),
      'samples':[r for r in result if r['p'] in (13,19,67,373)]},indent=2))
