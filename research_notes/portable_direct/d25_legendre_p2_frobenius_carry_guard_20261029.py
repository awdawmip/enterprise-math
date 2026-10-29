#!/usr/bin/env python3
"""Exact D25 auxiliary Legendre p^2 Frobenius carry, evaluated at x^2=8/9.

The universal polynomial formula is proved in the accompanying note.
Finite integer checks do not replace native H0/B0 or all-prime Root2 proof.
"""
from math import comb


def check(p):
    assert p > 3 and p % 8 in (5, 7)
    e = (p-1)//4
    k = (p-1)//2
    n = p+e
    assert n % 2 == 0
    m = p*p
    y = 8*pow(9,-1,m)%m

    def add(u,v):return ((u[0]+v[0])%m,(u[1]+v[1])%m)
    def scalar(c,u):return (c*u[0]%m,c*u[1]%m)
    def multiply(u,v):
        return ((u[0]*v[0]+u[1]*v[1]*y)%m,(u[0]*v[1]+u[1]*v[0])%m)

    # Coefficients of A(T)^k and A(T)^p with A(T)=1-2*x*T+T^2.
    poly=[(1,0)];B=None
    for exponent in range(1,p+1):
        old=poly
        poly=[]
        for j in range(min(n,len(old)+1)+1):
            u=old[j] if j<len(old) else (0,0)
            if 1<=j<=len(old):u=add(u,multiply((0,-2),old[j-1]))
            if 2<=j<=len(old)+1:u=add(u,old[j-2])
            poly.append(u)
        if exponent==k:B=poly[:]
    xp=(0,pow(y,k,m))
    a0={0:(1,0),p:scalar(-2,xp)}
    Q=[]
    for j in range(n+1):
        d=add(poly[j],scalar(-1,a0.get(j,(0,0))))
        assert d[0]%p==d[1]%p==0, ('Frobenius integral',p,j)
        Q.append((d[0]//p,d[1]//p))

    def C(index):
        out=(0,0)
        for j in range(max(0,index-len(Q)+1),min(index,len(B)-1)+1):
            out=add(out,multiply(B[j],Q[index-j]))
        return out

    carry_kernel=add(C(n),scalar(3,multiply(xp,C(e))))
    from_binomial=add(multiply(xp,B[e]),scalar(-p*pow(2,-1,m),carry_kernel))

    # Independent ordinary Legendre P_(p+e) at x^2=8/9.
    r=n//2
    direct=sum((-1)**j*comb(2*r,j)*comb(4*r-2*j,2*r)*pow(y,r-j,m)
               for j in range(r+1))*pow(4**r,-1,m)%m
    assert from_binomial==(direct,0), ('Legendre p2 transport',p,from_binomial,direct)
    first=multiply(xp,B[e])[0]
    correction=(-p*pow(2,-1,m)*carry_kernel[0])%m
    assert (first+correction)%m==direct
    return {'p':p,'e':e,'legendre':direct,'first':first,'frobenius_carry':correction,
            'C_e_mod_p':tuple(t%p for t in C(e)),
            'C_pe_mod_p':tuple(t%p for t in C(n))}


def main():
    tested=[5,7,13,23,29,31,37,47,61,71,109,157,229,373]
    certs=[check(p) for p in tested]
    for x in certs:
        if x['p'] in (13,23,37,373):print('CASE',x)
    print('PASS_D25_LEGENDRE_FROBENIUS_CARRY_P2',len(certs),'exact prime checks')


if __name__=='__main__':main()
