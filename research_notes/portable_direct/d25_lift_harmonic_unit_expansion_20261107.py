#!/usr/bin/env python3
"""D25 p-unit harmonic second-digit formula; portable exact regression only."""
from math import isqrt
from fractions import Fraction

def primes(n):
    a=bytearray([1])*(n+1); a[:2]=b'\0\0'
    for k in range(2,isqrt(n)+1):
        if a[k]: a[k*k::k]=bytes(len(a[k*k::k]))
    return [p for p in range(7,n+1) if a[p] and p%24 in (13,19)]

def check(p):
    m=(p-1)//6; M=p**3
    f=[1]*p
    for k in range(1,p):f[k]=f[k-1]*k%M
    fi=[1]*p; fi[-1]=pow(f[-1],-1,M)
    for k in range(p-1,0,-1):fi[k-1]=fi[k]*k%M
    inv2=pow(2,-1,M); inv3=pow(3,-1,M); inv6=pow(6,-1,M)
    inv2pow=1; s1=s2=0; b=1
    A0=A1=A2=W=H0=H1=V=0
    for k in range(p):
        if k:
            r=k-1
            if r!=m:
                q=pow(6*(r-m),-1,M);s1=(s1+q)%M;s2=(s2+q*q)%M
            if r!=2*m:
                q=pow(3*(r-2*m),-1,M);s1=(s1+q)%M;s2=(s2+q*q)%M
            inv2pow=inv2pow*inv2%M
        if k<=m:
            C=f[m]*f[2*m]*fi[m-k]*fi[2*m-k]*fi[k]**2*inv2pow%M;e=0
        elif k<=2*m:
            C=(-1)**(m+k)*f[m]*f[2*m]*f[k-m-1]*fi[2*m-k]*fi[k]**2*inv2pow*inv6%M;e=1
        else:
            C=(-1)**m*f[m]*f[2*m]*f[k-m-1]*f[k-2*m-1]*fi[k]**2*inv2pow*inv6*inv3%M;e=2
        q2=(s1*s1-s2)*inv2%M
        assert (p**e*C*(1+p*s1+p*p*q2)-b)%M==0,(p,k)
        wt=12*k+1
        if e==0:
            A0=(A0+C)%M;A1=(A1+C*s1)%M;A2=(A2+C*q2)%M
            H0=(H0+wt*C)%M;H1=(H1+wt*C*s1)%M
        elif e==1:
            A1=(A1+C)%M;A2=(A2+C*s1)%M;V=(V+wt*C)%M
        else:W=(W+C)%M
        if k<p-1:b=b*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,M)%M
    assert A0%p==0
    X=(A0//p+A1)%(p*p);Y=(A2+W)%p;H=H0%(p*p);J=(H1+V)%p
    assert X*H%p==1
    K=((X*H-1)%(p*p))//p
    D=(K+X*J+Y*H)%p
    # Independent full, unexpanded finite B sum at modulo p^3.
    b=1;g=h=0
    for k in range(p):
        g=(g+b)%M;h=(h+(12*k+1)*b)%M
        if k<p-1:b=b*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,M)%M
    assert g%p==0 and (g//p)*h%p==1
    assert D==(((g//p)*h-1)%(p*p))//p
    return p,X%p,Y,H%p,J,K,D

def rational_check(p):
    b=Fraction(1);g=h=Fraction(0)
    for k in range(p):
        g+=b;h+=(12*k+1)*b
        if k<p-1:b*=Fraction((6*k+1)*(3*k+1),36*(k+1)**2)
    def residue(x):
        M=p*p;assert x.denominator%p
        return x.numerator*pow(x.denominator,-1,M)%M
    G=residue(g/p);H=residue(h)
    assert G*H%p==1
    return ((G*H-1)%(p*p))//p

def main():
    pp=primes(5000);assert len(pp)==166
    rows={p:check(p) for p in pp}
    for p in primes(100):assert rows[p][-1]==rational_check(p)
    print('166/166 termwise p^3 and Delta comparison: PASS')
    print('6/6 exact rational check: PASS')
    for p in (13,19,37,43,109,157,373):print(*rows[p])
    print('AUTHOR_SIDE_ONLY / NO_R_p_COMPARISON / NO_NATIVE_CHECKPOINT')

if __name__=="__main__":main()
