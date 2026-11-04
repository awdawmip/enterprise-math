#!/usr/bin/env python3
"""D25: exact original-source weighted shells, no floating point; author-side checker."""
from math import isqrt

def primes_to(n):
    b=bytearray(b'\x01')*(n+1)
    b[0:2]=b'\x00\x00'
    for i in range(2,isqrt(n)+1):
        if b[i]: b[i*i:n+1:i]=b'\x00'*(((n-i*i)//i)+1)
    return [p for p in range(5,n+1) if b[p]]

def original(p,model):
    m=p**3
    c=1; total=half=0
    for k in range(p):
        term=(6*k+1 if model=="A" else 8*k+1)*c % m
        total=(total+term)%m
        if k<=(p-1)//2: half=(half+term)%m
        if k<p-1:
            if model=="A":
                num=(2*k+1)*(2*k+2)*(3*k+1)*(3*k+2)*(3*k+3)
                den=216*(k+1)**5
            else:
                num=(4*k+1)*(4*k+2)*(4*k+3)*(4*k+4)
                den=2304*(k+1)**4
            c=c*num*pow(den,-1,m)%m
    return total,half

def shell(p,model):
    fac=[1]*p
    for k in range(1,p): fac[k]=fac[k-1]*k%p
    s=0
    if model=="A":
        for j in range(p//3+1,(p-1)//2+1):
            den=fac[2*j-1]*fac[3*j-p-1]%p
            s+=(6*j-1)*pow(216,j-1,p)*pow(fac[j-1],5,p)*pow(den,-1,p)
    else:
        for j in range(p//4+1,(p-1)//2+1):
            s+=2*(8*j-1)*pow(2304,j-1,p)*pow(fac[j-1],4,p)*pow(fac[4*j-p-1],-1,p)
    return s%p

if __name__=="__main__":
    ps=primes_to(2000); nonzero_a=0
    witness={}
    for p in ps:
        a,ah=original(p,"A"); b,bh=original(p,"B")
        ta=shell(p,"A"); tb=shell(p,"B")
        assert (a-ah)%(p**3)==p*p*ta
        assert (b-bh)%(p**3)==p*p*tb
        target=(p if p%3==1 else -p)%(p**3)
        assert b==target and bh==target   # published 2019 theorem, regression
        assert a==target                  # finite observation only
        assert tb==0
        nonzero_a+=(ta!=0)
        if p in {5,13,19,139,373}: witness[p]={"T_A":ta,"T_B":tb}
    print({"primes":len(ps),"failures":0,"A_shell_nonzero":nonzero_a,"witness":witness})
