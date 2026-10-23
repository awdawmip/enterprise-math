#!/usr/bin/env python3
"""Exact p=211 D25 endpoint certificate (factorial path; author-side only)."""
from functools import lru_cache
from math import factorial

p, m = 211, 35
P2, P3, P4 = p*p, p**3, p**4

@lru_cache(None)
def fact_vu(n):
    v, u = 0, 1
    for x in range(1,n+1):
        while x % p == 0:
            x //= p
            v += 1
        u = u*x % P4
    return v, u

def R(n):
    # R_n = (4m+2n)!(2m)!^2(3n)! / [216^n (2m+n)!^2(4m+n)!(n!)^2].
    aa, bb, cc = fact_vu(4*m+2*n), fact_vu(2*m), fact_vu(3*n)
    dd, ee, ff = fact_vu(2*m+n), fact_vu(4*m+n), fact_vu(n)
    v = aa[0]+2*bb[0]+cc[0]-2*dd[0]-ee[0]-2*ff[0]
    up = aa[1]*pow(bb[1],2,P4)*cc[1] % P4
    dn = pow(216,n,P4)*pow(dd[1],2,P4)*ee[1]*pow(ff[1],2,P4) % P4
    return v, up*pow(dn,-1,P4) % P4

terms=[R(n) for n in range(4*m+2)]
assert [v for v,_ in terms[:m+1]]==[0]*(m+1)
assert [v for v,_ in terms[m+1:]]==[1]*(3*m+1)
def term(n):
    v,u=terms[n]
    return (p**v)*u % P4

def k(n):
    num=(2*p+1-3*n)*(6*n+2*p+3)
    den=(3*n+p+2)*(3*n+2*p+1)
    assert den%p
    return num*pow(den,-1,P2) % P2

low=sum(k(n)*term(n) for n in range(m+1))%P2
high_a=sum(k(n)*term(n) for n in range(m+1,2*m))%P2
high_b=sum(k(n)*term(n) for n in range(2*m+1,4*m))%P2
T2,T4=terms[2*m][1]%P2,terms[4*m][1]%P2
seam2=(p+2)*(4*p+1)*pow(3*(2*p+1),-1,P2)*T2%P2
seam4term=(3-2*p)*T4%P2
K=(low+high_a+high_b+seam2+seam4term)%P2
G=(-1)**m*pow(factorial(2*m),3,P2)*pow(factorial(3*m),-2,P2)%P2
assert (low,high_a,high_b,seam2,seam4term,K,G)==(2272,18779,7807,16799,36779,37915,37915)

W=sum((6*n+2*p-1)*term(n) for n in range(4*m+1))%P4
normal=factorial(p-1)*pow(pow(3,p-1,P4)*pow(factorial(2*m),3,P4)%P4,-1,P4)%P4
S=normal*W%P4
target=p*pow(4,p-1,P4)*pow(pow(3,p-1,P4),-1,P4)%P4
assert (W,normal,S,target)==(1567392611,842237293,1220721510,384661651)
assert W%p==0 and (W//p)%P2==K
assert (S-target)%P4==89*P3
print('PASS p=211: K=G=37915 (mod 44521); exact v_211(S-target)=3; digit=',89)
