#!/usr/bin/env python3
"""Exact finite survey: auxiliary D25 Clausen ports, p^2 and exceptional p^4."""
from math import isqrt, comb

def primes(n):
    a=bytearray([1])*(n+1);a[0:2]=b'\0\0'
    for j in range(2,isqrt(n)+1):
        if a[j]: a[j*j:n+1:j]=bytes((n-j*j)//j+1)
    return [j for j in range(5,n+1) if a[j]]

def ports(m,e,p,r):
    N=p**r
    inv=[0]*(m+1)
    if m: inv[1]=1
    for k in range(2,m+1): inv[k]=(-(N//k)*inv[N%k])%N
    half=pow(2,-1,N); term=1; A=1; B=(1-6*e)%N
    for k in range(1,m+1):
        term=term*(m-k+1)*(2*m+e-k+1)*inv[k]*inv[k]*half%N
        A=(A+term)%N; B=(B+(1-6*e+12*k)*term)%N
    return A,B

def direct(m,e,p,r):
    N=p**r;h=pow(2,-1,N);z=1;A=B=0
    for k in range(m+1):
        term=comb(m,k)*comb(2*m+e,k)*z%N
        A=(A+term)%N;B=(B+(1-6*e+12*k)*term)%N
        z=z*h%N
    return A,B

if __name__=='__main__':
    anomalies=[];cnt={'A':0,'B':0};total=0
    for p in primes(50000):
        e=0 if p%6==1 else 1;m=(p-1-4*e)//6
        A,B=ports(m,e,p,2)
        a0=A%p==0;b0=B%p==0
        assert a0 != b0,(p,A,B)
        chi=1 if pow(-6%p,(p-1)//2,p)==1 else -1
        assert a0==(chi==-1),(p,A,B,chi)
        label='A' if a0 else 'B';cnt[label]+=1
        if (A if a0 else B)==0: anomalies.append((p,e,m,label))
        total+=1
    assert total==5131 and cnt=={'A':2583,'B':2548}
    assert anomalies==[(149,1,24,'B'),(211,0,35,'A')]
    evidence=[]
    for p,e,m,label in anomalies:
        A,B=ports(m,e,p,4)
        assert (A,B)==direct(m,e,p,4)
        z=A if label=='A' else B
        assert z%(p*p)==0 and z%(p*p*p)!=0
        evidence.append((p,label,A,B,(z//(p*p))%p))
    assert evidence==[(149,'B',217514219,278267334,18),
                      (211,'A',1294715201,1472225574,174)]
    print('PASS',total,cnt,anomalies,evidence)
