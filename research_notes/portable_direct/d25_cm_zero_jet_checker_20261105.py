#!/usr/bin/env python3
"""Exact F_(p²) CM-zero Green reciprocal checks, p<=5000; no native benchmark."""
from math import isqrt
def primes(N):
    for p in range(5,N+1):
        if all(p%d for d in range(2,isqrt(p)+1)): yield p
def check(p,d):
    inv=lambda a:pow(a%p,-1,p)
    add=lambda a,b:((a[0]+b[0])%p,(a[1]+b[1])%p)
    mul=lambda a,b:((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    scl=lambda a,b:(a[0]*b%p,a[1]*b%p)
    def val(seq,x):
        z=(0,0)
        for c in reversed(seq):z=add(mul(z,x),(c,0))
        return z
    n=p//d; C=(d-1)*inv(d*d)%p
    c=[1]
    for j in range(n):c.append(c[-1]*(j*(j+1)+C)*inv((j+1)**2)%p)
    assert (n*(n+1)+C)%p==0 and c[-1]!=0
    ck=[1]
    for j in range(n):ck.append(ck[-1]*(j-n)*(j+n+1)*inv((j+1)**2)%p)
    assert c==ck # Legendre P_n(1-2X)
    jmax=(n-1 if p%3==1 else n) if d==3 else (2*n-1 if p%4==1 else 2*n+1)
    Q=[0]
    for j in range(jmax):
        cj=c[j] if j<len(c) else 0
        f=(2-6*C*inv(j+1))*cj%p
        term=f+(2*j+1)*(j*(j+1)+2*C)*Q[j]
        if j:term-=j*(j*j-1+4*C)*Q[j-1]
        Q.append(term*inv((j+1)**3)%p)
    x=scl((2,1),inv(4)) if d==3 else scl((3,2),inv(6))
    a=val(c,x);b=val([i*c[i]%p for i in range(1,len(c))],x)
    E=scl(mul(add((1,0),scl(x,-1)),val(Q,x)),C)
    assert a==(0,0) and b!=(0,0) and E!=(0,0),(p,d,a,b,E)
    target=16*inv(9)%p if d==3 else 27*inv(4)%p
    assert mul(E,mul(b,b))==(target,0),(p,d,E,b)
    assert E[1]==0 and mul(b,b)[1]==0
    assert (b[0]==0 if n%2==0 else b[1]==0)
    return (p,d,n,E[0],b)
def main():
    rows=[check(p,d) for p in primes(5000) if p%24 in (13,19) for d in (3,4)]
    print('model_cases=',len(rows),'target_primes=',len(rows)//2,'failures=0')
    for p in (13,19,139,373):print(p,[r for r in rows if r[0]==p])
if __name__=='__main__':main()
