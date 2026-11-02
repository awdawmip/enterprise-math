#!/usr/bin/env python3
"""Exact author-side Vandermonde source-jet check, not a native H0/B0 run."""
from math import comb, isqrt
import json
def primes(limit):
    q=bytearray(b'\x01')*(limit+1);q[:2]=b'\x00\x00'
    for k in range(2,isqrt(limit)+1):
        if q[k]:q[k*k::k]=b'\x00'*((limit-k*k)//k+1)
    return [p for p in range(7,limit+1) if q[p] and p%6==1]
def inverses(p):
    x=[0]*p;x[1]=1
    for k in range(2,p):x[k]=-(p//k)*x[p%k]%p
    return x
def reflect(coefficients,p):
    h=[]
    for a in reversed(coefficients):
        t=[0]*(len(h)+1)
        for k,b in enumerate(h):t[k]=(t[k]+b)%p;t[k+1]=(t[k+1]-b)%p
        t[0]=(t[0]+a)%p;h=t
    return h
def verify(p):
    r=(p-1)//6;u=3*r;iv=inverses(p)
    a=[1]
    for n in range(2*r):
        a.append(a[-1]*(2*n+1)*(3*n+1)*(3*n+2)*iv[18%p]*pow(iv[n+1],3,p)%p)
    s=[(9*n+4)*a[n]*iv[36%p]%p for n in range(2*r+1)]
    d=reflect(s,p)
    fact=[1]
    for k in range(1,2*r+2):fact.append(fact[-1]*k%p)
    inverse_factorial=[pow(v,-1,p) for v in fact]
    rho=[1]
    for k in range(r):rho.append(rho[-1]*(r-k)*(2*r-k)*iv[3*r-k]%p)
    B=comb(3*r,r)%p
    moments=[]
    for k in range(2*r+2):
        total=0
        for i in range(max(0,k-r),min(k,r)+1):
            j=k-i
            total=(total+fact[k]*inverse_factorial[i]*inverse_factorial[j]*rho[i]*rho[j])%p
        moments.append(total)
    predicted=[]
    for k in range(2*r+1):
        v=(B*B*iv[36%p]*inverse_factorial[k]*((4+9*k)*moments[k]+9*moments[k+1]))%p
        predicted.append((-v)%p if k%2 else v)
    assert d==predicted,(p,'source coefficients')
    J=sum(d[k]*pow(2,-k,p)*iv[u-k] for k in range(2*r+1))%p
    ds1=sum(n*s[n] for n in range(1,2*r+1))%p
    omega_prime=ds1*iv[u-1]%p
    assert omega_prime==8*B*B*iv[729%p]%p,(p,'endpoint derivative')
    return {'p':p,'r':r,'B':B,'J':J,'omega_prime_1':omega_prime}
def main():
    rows=[verify(p) for p in primes(2000)]
    out={'schema':'D25_VANDERMONDE_JET_AUTHOR_CHECK_V1',
         'range':'7<=p<=2000, p%6=1', 'checked':len(rows),
         'all_source_coefficients':'PASS','endpoint_derivative':'PASS',
         'samples':[x for x in rows if x['p'] in (7,13,19,31,37,43,73,181,373,1171)],
         'native_H0_B0':'NOT_EXECUTED','admission':'UNREVIEWED_NOT_ADMITTED'}
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
