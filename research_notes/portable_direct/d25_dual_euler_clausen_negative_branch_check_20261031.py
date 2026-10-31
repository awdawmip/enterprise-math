#!/usr/bin/env python3
"""Independent mod-p dual Euler–Clausen polynomial and CM-factor regression."""
from math import comb


def primes_below(limit: int):
    sieve = bytearray(b'\x01') * limit
    sieve[:2] = b'\x00\x00'
    for d in range(2, int(limit**0.5) + 1):
        if sieve[d]:
            sieve[d*d:limit:d] = b'\x00' * len(sieve[d*d:limit:d])
    return [p for p in range(5, limit) if sieve[p]]


def check(p):
    assert p%6==5
    m=(p-5)//6
    h=(p-1)//3
    # Exact original 216 coefficients, avoiding any use of Clausen in the checker.
    a=[1]
    for n in range(1,p):
        a.append((a[-1]*(2*n-1)*(3*n-2)*(3*n-1)*pow(36*n**3,-1,p))%p)
    g=[(comb(m,k)*comb(2*m+1,k))%p for k in range(m+1)]
    square=[0]*(2*m+1)
    for i,x in enumerate(g):
        for j,y in enumerate(g):
            square[i+j]=(square[i+j]+x*y)%p
    rhs=[0]*(2*m+2)
    for n in range(2*m+2):
        rhs[n]=((square[n] if n<len(square) else 0)-(square[n-1] if n else 0))%p
    for n in range(p):
        actual=(pow(2,n,p)*a[n])%p
        expected=rhs[n] if n<len(rhs) else 0
        assert actual==expected,(p,'polynomial',n,actual,expected)
    z=pow(2,-1,p)
    gv=sum(g[k]*pow(z,k,p) for k in range(len(g)))%p
    gd=sum(k*g[k]*pow(z,k-1,p) for k in range(1,len(g)))%p
    weighted=sum((6*n+1)*a[n] for n in range(p))%p
    assert weighted==(gv*(6*gd-5*gv)*pow(2,-1,p))%p,(p,'weighted factor')
    q=(6*gd-5*gv)%p
    return m,gv,q,weighted


def main():
    ps=[p for p in primes_below(4000) if p%6==5]
    table={}
    total=0
    for p in ps:
        m,g,q,w=check(p)
        total+=p
        assert (g==0) != (q==0), (p,'overlap or counterexample',g,q)
        kind='G_ZERO' if not g else 'ROBIN_ZERO'
        row=table.setdefault(p%24, {'G_ZERO':0,'ROBIN_ZERO':0})
        row[kind]+=1
        if p in (5,11,17,23,29,41,53):
            print('anchor',p,'m',m,'G',g,'robin',q,'A_mod_p',w)
    print('primes',len(ps),'direct_coefficient_comparisons',total,'residue_classes',table)
    print('PASS_D25_DUAL_EULER_CLAUSEN_P5_POLYNOMIAL_EXACT')


if __name__=='__main__':
    main()
