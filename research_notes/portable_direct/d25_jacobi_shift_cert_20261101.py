#!/usr/bin/env python3
"""D25: exact p^2 two-shift Jacobi certificate, author-side and unreviewed."""
from math import isqrt, factorial

def primes(n):
    z=bytearray(b'\x01')*(n+1); z[:2]=b'\x00\x00'
    for i in range(2,isqrt(n)+1):
        if z[i]: z[i*i:n+1:i]=b'\x00'*((n-i*i)//i+1)
    return [p for p in range(11,n+1) if z[p] and p%8==5]

def K(n,x,p):
    m=p*p; t=s=1
    for k in range(1,n+1):
        t=t*(n-k+1)*(x-k+1)*pow(9*k*k,-1,m)%m
        s=(s+t)%m
    return s

def G(p,order=2):
    m=p**order; t=s=1
    for k in range(p-1):
        t=t*(8*k+1)*(8*k+3)*pow(576*(k+1)**2,-1,m)%m
        s=(s+t)%m
    return s

def verify(limit=3000):
    n=sharp=0
    for p in primes(limit):
        a=(5*p-1)//8; b=(7*p-3)//8; m=p*p
        j=K(a,b,p); assert j==K(b,a,p)
        x=K(b,a+p,p); y=K(a,b+p,p); g=G(p)
        assert (x-j)%p==(y-j)%p==0
        assert (8*g-20*j+5*x+7*y)%m==0
        if p%24==13:
            n+=1
            assert j%p==0 and g==0 # finite regression, NOT universal theorem
            q=G(p,3)
            assert q%m==0
            sharp+=q!=0
        else: assert p%24==5 and g%p!=0
        if p in (13,37,373):
            # independently evaluate factorial/Pochhammer numerator modulo p^3
            mm=p**3; num=fac=den=1; total=0
            for k in range(p):
                if k:
                    num*=(8*k-7)*(8*k-5); fac*=k; den*=576
                total=(total+num*pow(den*fac*fac,-1,mm))%mm
            assert total==G(p,3)
            print(dict(p=p,J=j,Kb=x,Ka=y,G2=g,G3=total,third_digit=total//m))
    print('PASS',len(primes(limit)),'p=5 mod8;',n,'p=13 mod24;',sharp,'third-digit nonzero')
if __name__=='__main__': verify()
