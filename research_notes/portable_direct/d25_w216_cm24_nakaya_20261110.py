#!/usr/bin/env python3
"""Exact arithmetic tests for the level-3 Fricke / CM(-24) J_p identity.

No native H0/B0 calculation. General proof uses Nakaya and Deuring theorems.
Only Python standard library; all finite-field calculations are exact.
"""
from math import comb


def primes_upto(n):
    flags = bytearray(b'\x01') * (n+1)
    flags[:2] = b'\x00\x00'
    for k in range(2, int(n**0.5)+1):
        if flags[k]:
            flags[k*k:n+1:k] = b'\x00' * (((n-k*k)//k)+1)
    return [k for k in range(2,n+1) if flags[k]]


def j_original_mod_p(p):
    assert p > 3 and p % 6 == 1
    m = (p-1)//6
    b = total = 1
    for k in range(1,m+1):
        b = (b*(6*k-5)*(3*k-2)*pow(36*k*k,-1,p))%p
        total=(total+b)%p
    return total


def j_binomial_mod_p(p):
    m=(p-1)//6
    return sum(comb(m,k)*comb(2*m,k)*pow(2,-k,p)
               for k in range(m+1))%p


def add(a,b,p):
    return ((a[0]+b[0])%p,(a[1]+b[1])%p)


def mul(a,b,p):
    return ((a[0]*b[0]+2*a[1]*b[1])%p,
            (a[0]*b[1]+a[1]*b[0])%p)


def inverse(a,p):
    norm=(a[0]*a[0]-2*a[1]*a[1])%p
    assert norm != 0
    t=pow(norm,-1,p)
    return (a[0]*t%p,-a[1]*t%p)


def cm24_hasse(p):
    """Coefficient [x^(p-1)](x^3+a*x+b)^((p-1)/2) in Fp[T]/(T^2-2)."""
    assert p % 24 in (13,19)
    j=(2417472%p,-1707264%p)
    d=add(j,(-1728%p,0),p)
    a=mul(mul((-3%p,0),j,p),inverse(d,p),p)
    b=mul(mul((-2%p,0),j,p),inverse(d,p),p)
    n=(p-1)//2
    ap=[(1,0)]
    bp=[(1,0)]
    for _ in range(n):
        ap.append(mul(ap[-1],a,p))
        bp.append(mul(bp[-1],b,p))
    ans=(0,0)
    for u in range((n+1)//2,(2*n)//3+1):
        v=2*n-3*u
        w=2*u-n
        z=mul(ap[v],bp[w],p)
        c=comb(n,u)*comb(n-u,v)%p
        ans=add(ans,(c*z[0]%p,c*z[1]%p),p)
    return ans


def main():
    ps=primes_upto(10000)
    group=[p for p in ps if p%6==1]
    target=[p for p in group if p%24 in (13,19)]
    cross=hasse=0
    for p in group:
        r=j_original_mod_p(p)
        if p<=1000:
            assert r == j_binomial_mod_p(p),(p,r)
            cross+=1
        assert (r==0)==(p%24 in (13,19)),(p,r)
    for p in target:
        if p<=1000:
            assert cm24_hasse(p)==(0,0),(p,cm24_hasse(p))
            hasse+=1
    assert (len(group),len(target),hasse)==(611,312,45)
    print("J recurrence p<=10000: 611 primes, 312 target roots, 299 nonroots")
    print(f"Independent finite binomial checks: {cross}; CM Hasse checks: {hasse}")
    print("p=373 J",j_original_mod_p(373),"CM Hasse",cm24_hasse(373))


if __name__=="__main__":
    main()
