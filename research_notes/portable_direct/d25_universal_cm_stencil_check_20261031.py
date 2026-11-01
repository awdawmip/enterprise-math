#!/usr/bin/env python3
"""Author-side exact arithmetic; does not simulate native H0/B0."""
from fractions import Fraction
from math import comb, factorial

def primes_below(n):
    sieve=bytearray(b'\x01')*n
    sieve[0:2]=b'\x00\x00'
    for k in range(2,int(n**0.5)+1):
        if sieve[k]:
            sieve[k*k:n:k]=b'\x00'*((n-1-k*k)//k+1)
    return [p for p in range(n) if sieve[p]]

def universal_symbols(R=5):
    b=[Fraction(0), Fraction(1)]
    for n in range(R):
        b.append((-(n+1)*b[n+1]/2+(n*n+Fraction(n,2)+Fraction(1,18))*b[n])/((n+2)*(n+1)))
    h=[sum((b[k]*b[j-k] for k in range(j+1)), Fraction(0)) for j in range(R+2)]
    Bw=[((1+6*j)*h[j]+6*(j+1)*h[j+1])/4 for j in range(R+1)]
    c=[Fraction(0)]+[(-1)**r*sum((comb(r-1,j-1)*Bw[j] for j in range(1,r+1)),Fraction(0)) for r in range(1,R+1)]
    return [factorial(r)*c[r] for r in range(1,R+1)]

def original_coefficients(p,mod):
    a=[1]
    v=1
    for n in range(1,p):
        v=v*(2*n-1)*(3*n-1)*(3*n-2)*pow(36*n**3,-1,mod)%mod
        a.append(v)
    return a

def original_value(a,x,mod):
    acc=0
    power=1
    for n,v in enumerate(a):
        acc=(acc+(6*n+1)*v*power)%mod
        power=power*x%mod
    return acc

def gp_derivative(p):
    ell=(p-1)//6
    power=1
    total=0
    for k in range(1,ell+1):
        total=(total+k*comb(ell,k)*comb(2*ell,k)*power)%p
        power=power*pow(2,-1,p)%p
    return total

def main():
    symbols=universal_symbols()
    assert symbols==[Fraction(-3),Fraction(8),Fraction(-119,3),Fraction(2530,9),Fraction(-277057,108)]
    count=0
    checked=0
    res283=None
    anchors=[]
    for p in primes_below(1001):
        if p%24 not in (13,19): continue
        count+=1
        mod=p**7
        a=original_coefficients(p,mod)
        gp=gp_derivative(p)
        assert gp!=0
        if p in (13,19,37,283,373):
            for n in range(p):
                assert a[n]==comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,mod)%mod
        for t in (1,2):
            vals=[original_value(a,pow(1+j*p*t,-1,mod),mod) for j in range(6)]
            gotvalues=[]
            for r,k in enumerate(symbols,1):
                d=sum((-1)**(r-j)*comb(r,j)*vals[j] for j in range(r+1))%mod
                assert d%p**r==0
                got=d//p**r%p
                expected=k.numerator*pow(k.denominator,-1,p)*gp**2*pow(t,r,p)%p
                assert got==expected, (p,t,r,got,expected)
                gotvalues.append(got)
                checked+=1
                if p==283 and t==1 and r==5:
                    res283=(d//p**5%p,d//p**6%p)
            if t==1 and p in (13,19,37,283,373):
                anchors.append((p,gp,*gotvalues))
    assert res283==(0,7)
    print("PASS_D25_UNIVERSAL_CM_STENCILS_EXACT")
    print("symbols", [str(x) for x in symbols])
    print("primes",count,"stencils",checked,"exception283",res283)
    print("anchors",anchors)

if __name__=="__main__":
    main()
