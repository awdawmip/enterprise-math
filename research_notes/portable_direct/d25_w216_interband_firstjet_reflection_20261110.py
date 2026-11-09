#!/usr/bin/env python3
"""Exact W216 original grade1-grade2 reflected first jet; Python stdlib only."""
from math import comb

def primes(limit):
    sieve = bytearray(b"\x01") * (limit+1)
    sieve[:2] = b"\x00\x00"
    for n in range(2, int(limit**.5)+1):
        if sieve[n]:
            sieve[n*n:limit+1:n] = b"\x00" * ((limit-n*n)//n+1)
    return [p for p in range(7,limit+1) if sieve[p] and p%6==1]

def check(p):
    m=(p-1)//6
    modulus=p**4
    mod2=p**2
    a=[1]
    for k in range(p-1):
        num=(2*k+1)*(3*k+1)*(3*k+2)
        a.append(a[-1]*num*pow(36*(k+1)**3,-1,modulus)%modulus)
    k0=2*m+1
    c=((a[k0]//p)*(a[4*m]//(p*p)))%mod2
    assert c%p==3*pow(32,-1,p)%p
    e_sum=0
    w2_native=0
    w2_recovered=0
    for j in range(m):
        k=k0+j
        h=p-k
        assert 3*m+1<=h<=4*m
        assert a[k]%p==0 and a[h]%(p*p)==0
        L=a[k]//p%mod2
        H=a[h]//(p*p)%mod2
        rhs=c*pow(k0*pow(k,-1,mod2),3,mod2)*(1+p*e_sum)%mod2
        assert L*H%mod2==rhs, (p,j)
        recovered_H=rhs*pow(L,-1,mod2)%mod2
        assert H==recovered_H, (p,j,H,recovered_H)
        w2_native=(w2_native+(6*h+1)*H)%mod2
        w2_recovered=(w2_recovered+(6*h+1)*recovered_H)%mod2
        if p in (7,13,19,373):
            for idx in (k,h):
                original=comb(2*idx,idx)**2*comb(3*idx,idx)
                original=original*pow(216,-idx,modulus)%modulus
                assert original==a[idx],(p,idx)
        if j+1<m:
            e=(-3*pow(k,-1,p)+2*pow(2*k+1,-1,p)
               +3*pow(3*k+1,-1,p)+3*pow(3*k+2,-1,p))%p
            e_sum=(e_sum+e)%p
    assert w2_native==w2_recovered
    return m,c,w2_native

def main():
    ps=primes(2000)
    pairs=0
    for p in ps:
        m,c,w2=check(p)
        pairs+=m
        if p in (7,13,19,373,997,1999):
            print("p",p,"C",c,"W2/p²",w2)
    assert len(ps)==148 and pairs==22952
    print("PASS",len(ps),"primes",pairs,"paired coefficients; 136 independent original binomial coefficients mod p^4")

if __name__ == "__main__":
    main()
