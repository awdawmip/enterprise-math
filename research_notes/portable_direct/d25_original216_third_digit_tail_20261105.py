#!/usr/bin/env python3
"""D25 original-216 p^4 high-tail check (portable only; no native H0/B0)."""
from math import isqrt

def primes(n):
    for p in range(7,n+1):
        if p%6==1 and all(p%d for d in range(2,isqrt(p)+1)):
            yield p

def coeffs(p):
    mod=p**4
    b=[1]
    for k in range(p-1):
        b.append(b[-1]*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,mod)%mod)
    return b

def fast(p,b):
    m=(p-1)//6
    pp=p*p
    d=[0]+[b[p-r]//pp%pp for r in range(1,2*m+1)]
    low=[0]*3
    middle=[0]*3
    M0=M1=M2=0
    for i in range(1,2*m+1):
        di=d[i]
        M0=(M0+di)%pp
        M1=(M1+i*di)%pp
        M2=(M2+i*i*di)%pp
        S0=M0
        S1=(i*M0-M1)%pp
        S2=(i*i*M0-2*i*M1+M2)%pp
        if i<=m:
            bi=b[i]%pp
            low[0]=(low[0]+bi*S0)%pp
            low[1]=(low[1]+bi*(S1+p*S0))%pp
            low[2]=(low[2]+bi*(S2+2*p*S1))%pp
        else:
            ei=b[i]//p%p
            middle[0]=(middle[0]+ei*S0)%p
            middle[1]=(middle[1]+ei*S1)%p
            middle[2]=(middle[2]+ei*S2)%p
    lo=[2*x%pp for x in low]
    mi=[2*p*x%pp for x in middle]
    return [(lo[j]+mi[j])%pp for j in range(3)],lo,mi

def direct(p,b):
    mod=p**4
    t=[0,0,0]
    for i in range(p):
        for j in range(max(0,p-i),p):
            n=i+j
            prod=b[i]*b[j]%mod
            t[0]=(t[0]+prod)%mod
            t[1]=(t[1]+n*prod)%mod
            t[2]=(t[2]+n*n*prod)%mod
    assert all(v%(p*p)==0 for v in t)
    return [v//(p*p)%(p*p) for v in t]

def main():
    ct=0
    for p in primes(373):
        b=coeffs(p)
        f,lo,mi=fast(p,b)
        t=direct(p,b)
        assert f==t,(p,f,t)
        if p in (7,13,19,37,61,373):
            print(p,f,lo,mi,'weighted',(f[0]+6*f[1])%(p*p))
        ct+=1
    print("PASS",ct,"primes, exact modulo p^4 direct convolution and O(p) formula")

if __name__=="__main__":
    main()
