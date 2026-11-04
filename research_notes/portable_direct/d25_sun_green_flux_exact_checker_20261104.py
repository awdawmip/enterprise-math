#!/usr/bin/env python3
"""Independent mod-p polynomial check of exact Sun Green-flux conservation."""
from math import isqrt
import json
def primes(n):
    s=[True]*(n+1);s[0]=s[1]=False
    for a in range(2,isqrt(n)+1):
        if s[a]:
            for j in range(a*a,n+1,a):s[j]=False
    return [p for p in range(5,n+1) if s[p]]
def mul(A,B,p):
    Z=[0]*(len(A)+len(B)-1)
    for j,a in enumerate(A):
        if a:
            for k,b in enumerate(B):Z[j+k]=(Z[j+k]+a*b)%p
    return Z
def add(*A,p):
    Z=[0]*max(map(len,A))
    for a in A:
        for j,b in enumerate(a):Z[j]=(Z[j]+b)%p
    while Z and not Z[-1]:Z.pop()
    return Z
def deriv(A,p):return [j*A[j]%p for j in range(1,len(A))]
def scale(A,b,p):return [v*b%p for v in A]
def check(p,d):
    C=(d-1)*pow(d*d,-1,p)%p
    c=[1]
    for k in range(p-1):
        c.append(c[-1]*(k*(k+1)+C)*pow(k+1,-2,p)%p)
    m=p//d
    J=(m-1 if p%d==1 else m) if d==3 else (2*m-1 if p%d==1 else 2*m+1)
    q=[0]
    for n in range(J):
        forcing=(2-6*C*pow(n+1,-1,p))*c[n]%p
        prev=q[n-1] if n else 0
        t=forcing+(2*n+1)*(n*(n+1)+2*C)*q[n]-n*(n*n-1+4*C)*prev
        q.append(t*pow(n+1,-3,p)%p)
    f=mul(c,c,p);f1=deriv(f,p);f2=deriv(f1,p)
    q1=deriv(q,p);q2=deriv(q1,p)
    u=[0,1,p-1];v=[1,p-2]
    B=add(mul(mul(u,u,p),add(mul(f,q2,p),scale(mul(f1,q1,p),-1,p),mul(f2,q,p),p=p),p),
          mul(mul(u,v,p),add(mul(f,q1,p),mul(f1,q,p),p=p),p),
          scale(mul(u,mul(f,q,p),p),-4*C,p),p=p)
    rhs=add([2]+[0]*(p-1)+[-2%p],scale(mul([1,p-1],mul(f,c,p),p),-2,p),p=p)
    assert B==rhs,(p,d,'flux')
    return (p,d,J)
if __name__=='__main__':
    results=[check(p,d) for p in sorted(set(primes(151)+[373])) for d in (3,4)]
    print(json.dumps({'cases':len(results),'failures':0,'sample':[r for r in results if r[0] in (13,19,139,373)]}))
