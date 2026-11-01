"""Finite exact integer checks for D25 truncated Clausen source conservation."""
from fractions import Fraction
from math import isqrt

def primes(mx):
    return [p for p in range(7,mx+1) if p%6==1 and all(p%d for d in range(2,isqrt(p)+1))]

def omitted(p):
    u=v=Fraction(1)
    for n in range(1,p+1):
        j=n-1
        u*=Fraction((6*j+1)*(3*j+1),18*n*n)
        v*=Fraction((2*j+1)*(3*j+1)*(3*j+2),18*n*n*n)
    gap=v-2*u
    assert gap.denominator%p
    return (gap.numerator*pow(gap.denominator,-1,p**3)%(p**3))//p**2

def check(p):
    m=p**4; d=pow(18,-1,m)
    u=[1]; v=[1]
    for n in range(1,p):
        j=n-1
        u.append(u[-1]*(6*j+1)*(3*j+1)*d*pow(n*n,-1,m)%m)
        v.append(v[-1]*(2*j+1)*(3*j+1)*(3*j+2)*d*pow(n**3,-1,m)%m)
    H=[0]*(2*p-1)
    for i,x in enumerate(u):
        for j,y in enumerate(u):
            H[i+j]=(H[i+j]+x*y)%m
    assert H[:p]==v
    K=[0]*len(H)
    K[p:]=H[p:]
    assert all(x%p**2==0 for x in K)
    e=-(6*p-5)*(3*p-2)*d*u[-1]%m
    assert u[-1]//p**2%p==pow(10,-1,p)
    assert e//p**2%p==-pow(18,-1,p)%p
    def L3(a,n):
        x=n**3*a[n] if n<len(a) else 0
        if 1<=n and n-1<len(a):
            x-=(2*n-1)*(3*n-2)*(3*n-1)*d*a[n-1]
        return x%m
    for n in range(2*p):
        expected=2*e*(3*n-2*p)*u[n-p]%m if p<=n<2*p else 0
        assert L3(H,n)==expected,(p,n,'symmetric-square')
        if n>p: assert L3(K,n)==expected,(p,n,'cutoff-high')
    assert L3(K,p+1)//p**2%p==-pow(54,-1,p)%p
    w=(6*(p-1)+1)*v[-1]%m
    terminal=-(6*p+1)*(6*p-5)*(2*p-1)*(3*p-2)*(3*p-1)*d*w%m
    assert terminal==5*pow(9,-1,m)*p**3%m
    assert (6*p-5)*(6*p+1)*(2*e*p-L3(K,p))%m==terminal
    if p in (7,13,19,37): assert omitted(p)==K[p]//p**2%p
    return (p,K[p]//p**2%p,L3(K,p+1)//p**2%p,terminal//p**3%p)

if __name__=="__main__":
    records=[check(p) for p in primes(397)]
    for row in records:
        if row[0] in (7,13,19,37,61,109,211,373): print("CERT",row)
    print("PASS_ALL",len(records),"primes p<=397; all coefficients, exact rational samples, modulo p^4")
