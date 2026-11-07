#!/usr/bin/env python3
"""Exact modular verification of A/B p^3 Gauss-tail factorial kernels."""
def primes(limit):
    s=bytearray(b"\1")*(limit+1);s[:2]=b"\0\0"
    for i in range(2,int(limit**.5)+1):
        if s[i]:s[i*i::i]=b"\0"*(((limit-i*i)//i)+1)
    return [i for i in range(5,limit+1) if s[i]]

def factorial_mod(p):
    f=[1]*p
    for n in range(1,p):f[n]=f[n-1]*n%p
    return f

def check_A(p):
    m=(p-1)//6;f=factorial_mod(p);M=p**3;c=1;first=None;count=0
    for n in range(p):
        if n>=2*m+1:
            assert c%(p*p)==0
            v=c//(p*p)%p
            v1=(-1)**m*f[m]*f[2*m]*f[n-m-1]*f[n-2*m-1]*pow(18*f[n]*f[n],-1,p)%p
            assert v==v1,(p,n,v,v1)
            if first is None:first=v
            count+=1
        if n<p-1:c=c*(6*n+1)*(3*n+1)*pow(18*(n+1)**2,-1,M)%M
    return count,first

def check_B(p):
    k=(p-3)//8 if p%8==3 else (p-5)//8
    x,y=(1,3) if p%8==3 else (5,7)
    f=factorial_mod(p);M=p**3;c=1;first=None;count=0
    for n in range(p):
        if n>=3*k+2:
            assert c%(p*p)==0
            v=c//(p*p)%p
            v1=-3*f[k]*f[3*k+1]*f[n-k-1]*f[n-3*k-2]*pow(64*f[n]*f[n],-1,p)%p
            assert v==v1,(p,n,v,v1)
            if first is None:first=v
            count+=1
        if n<p-1:c=c*(8*n+x)*(8*n+y)*pow(64*(n+1)**2,-1,M)%M
    return count,first

if __name__=="__main__":
    ps=primes(2500);A=[p for p in ps if p%6==1];B=[p for p in ps if p%8 in (3,5)]
    for p in A:check_A(p)
    for p in B:check_B(p)
    cases={p:(check_A(p),check_B(p)) for p in [13,19,43,67,373]}
    assert cases=={13:((8,3),(8,9)),19:((12,7),(11,18)),43:((28,41),(26,6)),67:((44,16),(41,13)),373:((248,69),(233,342))}
    print("PASS",len(A),"A primes",len(B),"B primes; every normalized tail coefficient p<=2500")
    print(cases)
