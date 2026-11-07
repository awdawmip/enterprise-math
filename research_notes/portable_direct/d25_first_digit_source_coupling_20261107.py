#!/usr/bin/env python3
"""Exact D25 first-digit Gauss/weighted-source coupling; portable, not native H0/B0."""
from math import comb

def primes(bound):
    sieve=bytearray(b'\x01')*(bound+1);sieve[:2]=b'\x00\x00'
    for q in range(2,int(bound**0.5)+1):
        if sieve[q]: sieve[q*q::q]=b'\x00'*((bound-q*q)//q+1)
    return [p for p in range(7,bound+1) if sieve[p] and p%24 in (13,19)]

def data(p,which):
    assert p%24 in (13,19)
    if which=='A':
        u,v,d,c1n,c2n,eps,xden,lam=(p-1)//6,(p-1)//3,6,1,2,0,2,6
    else:
        k=(p-3)//8 if p%8==3 else (p-5)//8
        u,v,d,c1n,c2n,eps,xden,lam=k,3*k+1,8,1,3,int(p%8==5),9,8
    mod=p*p;x=pow(xden,-1,mod)
    Q=sum(comb(u,i)*comb(v,i)*pow(x,i,mod) for i in range(u+1))%mod
    J=sum(i*comb(u,i)*comb(v,i)*pow(x,i,mod) for i in range(u+1))%p
    c1=c1n*pow(d,-1,mod)%mod;c2=c2n*pow(d,-1,mod)%mod
    gauss=0;term=1;xp=1
    for n in range(p):
        gauss=(gauss+term*xp)%mod
        if n+1<p:
            term=term*(n-u+c1*p)*(n-v+c2*p)*pow(n+1,-2,mod)%mod
            xp=xp*x%mod
    # Independent original weighted 3F2 coefficient recurrence.
    weight=0;term=1
    for n in range(p):
        weight=(weight+(lam*n+1)*term)%mod
        if n+1<p:
            num,den=((2*n+1)*(3*n+1)*(3*n+2),36) if which=='A' else ((4*n+1)*(2*n+1)*(4*n+3),288)
            term=term*num*pow(den*(n+1)**3,-1,mod)%mod
    assert Q%p==gauss%p==0,(p,which,'zero hypothesis failed')
    q=Q//p; f=((gauss-Q)%mod)//p;g=gauss//p
    assert (q+f-g)%p==0
    c=12 if which=='A' else (16 if eps==0 else 128*pow(9,-1,p)%p)
    low,first=c*J*q%p,c*J*f%p
    assert weight%p==0 and (low+first)%p==weight//p%p
    return (q%p,J,f,g,low,first,weight//p%p)

if __name__=='__main__':
    ps=primes(2000)
    assert len(ps)==77
    for p in ps:
        for which in 'AB':
            assert data(p,which)[-1]==1,(p,which)
    print('PASS',len(ps),'target primes and',2*len(ps),'Gauss/weighted pairs <=2000')
    expected={
      13:((7,7,4,11,3,11,1),(3,12,8,11,5,9,1)),
      19:((6,1,2,8,15,5,1),(10,7,18,9,18,2,1)),
      43:((4,20,27,31,14,30,1),(34,34,29,20,6,38,1)),
      67:((16,40,45,61,42,26,1),(11,35,3,14,63,5,1)),
      373:((340,294,57,24,325,49,1),(326,41,33,359,30,344,1))}
    for p,(ea,eb) in expected.items():
        assert (data(p,'A'),data(p,'B'))==(ea,eb)
        print(p,'A',ea,'B',eb)
