#!/usr/bin/env python3
"""Independent finite-ring checks for a CM(-24) cubic-Hasse selector.

No floating point and no native H0/B0 or Source checkpoint is performed.
For each p=1 mod6, all ring work is in F_p[t]/(2t^2-1), even when t
is already in F_p. The p-adic research's infinite statement relies on
the proof using Sun (2013) Eq.(1.5) and the CM reduction theorem.
"""
from math import comb, factorial
from collections import Counter


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n+1)
    sieve[0:2] = b'\x00\x00'
    for d in range(2, int(n**0.5)+1):
        if sieve[d]:
            sieve[d*d::d] = b'\x00' * ((n - d*d)//d + 1)
    return [p for p in range(7,n+1) if sieve[p] and p%6==1]


def run(p):
    inv2 = pow(2,-1,p)
    def add(x,y): return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def scale(c,x): return (c*x[0]%p,c*x[1]%p)
    def mul(x,y): return ((x[0]*y[0]+inv2*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def power(x,k):
        y=(1,0)
        while k:
            if k&1: y=mul(y,x)
            x=mul(x,x); k//=2
        return y

    r=(p-1)//6
    m=3*r; n=2*r
    T=(0,1)
    P0=(1,0);P1=T
    for index in range(1,n):
        # recurrence for P_{index+1}; all denominators are p-units.
        numerator=add(scale(2*index+1,mul(T,P1)),scale(-index,P0))
        P0,P1=P1,scale(pow(index+1,-1,p),numerator)
    P=P1

    # Independent 2F1 reduction at z=1/2, terminating at k=r.
    y=sum(comb(r,k)*comb(2*r,k)*pow(inv2,k,p) for k in range(r+1))%p
    assert P == (y,0),(p,'Legendre-Gauss mismatch',P,y)

    # Direct cubic Hasse coefficient [X^(p-1)](X^3+aX+b)^((p-1)/2)
    a=(-15%p,12%p)
    b=(24%p,-28%p)
    fact=[1]*(m+1)
    for i in range(1,m+1):fact[i]=fact[i-1]*i%p
    inv_fact=[pow(v,-1,p) for v in fact]
    H=(0,0)
    for i in range(m+1):
        j=p-1-3*i
        k=m-i-j
        if j<0 or k<0: continue
        c=fact[m]*inv_fact[i]*inv_fact[j]*inv_fact[k]%p
        H=add(H,scale(c,mul(power(a,j),power(b,k))))
    assert P==H,(p,'cubic Hasse mismatch',P,H)

    # Check nonsingularity after t^2=1/2: 4a^3+27b^2=-108(4t+3).
    disc=add(scale(4,power(a,3)),scale(27,power(b,2)))
    assert disc == (-324%p,-432%p)
    assert disc != (0,0)

    # Direct, independent unweighted truncated 3F2 sum at z=1/2 mod p^2.
    # Ratio is ((2k+1)(3k+1)(3k+2)) / (36(k+1)^3).
    pp=p*p
    term=1
    U=1
    for k in range(p-1):
        numerator=(2*k+1)*(3*k+1)*(3*k+2)
        denominator=36*(k+1)**3
        term=term*numerator*pow(denominator,-1,pp)%pp
        U=(U+term)%pp

    # ( -6/p ) determines ordinary/supersingular in CM field Q(sqrt(-6)).
    chi=pow(-6%p,(p-1)//2,p)
    chi= -1 if chi==p-1 else chi
    assert chi in (-1,1)
    assert (P==(0,0)) == (chi==-1), (p,'CM mismatch',P,chi)
    if chi==-1:
        assert U==0,(p, 'unweighted 3F2 did not vanish mod p^2', U)
    return p,chi,y,P,H,U


def main():
    ps=primes_upto(3000)
    counts=Counter()
    witnesses={}
    for p in ps:
        ans=run(p)
        counts[(p%24,ans[1])]+=1
        if p in [7,13,19,31,37,43,61,73,109,373]:
            witnesses[p]=(ans[1],ans[2],ans[3],ans[4],ans[5])
    print('CHECK: PASS; count:',len(ps),'p<=3000 and p=1 mod6')
    for key,count in sorted(counts.items()):print('class,chi,count:',key,count)
    for p,values in sorted(witnesses.items()):print('witness:',p,values)
    print('EXACT_STATUS: Hasse/CM and target-class unweighted 3F2 mod p^2 finite checks; infinite theorem uses cited classical results and prior Clausen cutoff theorem.')

if __name__=='__main__':main()
