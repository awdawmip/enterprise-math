#!/usr/bin/env python3
"""D25 reciprocal Green critical-point residue audit; exact rationals and F_p."""
from fractions import Fraction as Q
from math import factorial, comb, isqrt

def exact(m):
    L, U = m + 1, 2*m
    a = {j: Q((-1)**(m+j+1)*factorial(m)*factorial(j-m-1)*factorial(2*m),
              factorial(2*m-j)*factorial(j)**2) for j in range(L, U+1)}
    h = {l: Q(2*factorial(m)*factorial(2*m)*factorial(l-1)**2,
              factorial(l+m)*factorial(l+2*m)) for l in range(1, U+1)}
    v = {j:a[j]/2**j for j in a}
    g = {l: h[l]*2**l for l in h}
    F0, G0 = sum(a.values(),Q(0)), sum(h.values(),Q(0))
    Fprime = -2*sum((j*a[j] for j in a),Q(0))
    Gprime = 2*sum((l*h[l] for l in h),Q(0))
    W0 = F0*Gprime - G0*Fprime
    WfromN = Q(2,3*m)*((2-U*U*h[U])*F0 + L*L*a[L]*G0)
    assert W0 == WfromN and W0 > 0
    assert F0 > 0 and G0 > 0 and 2-U*U*h[U] > 0
    lhs = U*U*g[U]*sum((v[j]*comb(3*m+U-j,3*m)/2**(U-j)
                         for j in range(L,U+1)),Q(0))
    rhs = L*L*v[L]*sum((g[l]*comb(3*m-L+l,3*m)/2**(l-L)
                         for l in range(L,U+1)),Q(0))
    assert lhs == rhs
    terms = {}
    def add(n,c):
        terms[n] = terms.get(n,Q(0))+c
    for j in range(L,U+1):
        add(3*m-j,4*v[j])
        add(3*m+U-j,-2*U*U*g[U]*v[j])
    for l in range(1,U+1):
        add(3*m-L+l,2*L*L*v[L]*g[l])
    qder = sum((c*comb(n,3*m)/2**(n-3*m)
                 for n,c in terms.items() if n>=3*m),Q(0))
    assert qder == 0
    return lhs, W0/Q(2**(3*m+1))

def primes_upto(n):
    for p in range(7,n+1):
        if p%6!=1:
            continue
        if all(p%d for d in range(2,isqrt(p)+1)):
            yield p

def mod_exact(p):
    m=(p-1)//6;L,U=m+1,2*m
    fact=[1]*p
    for k in range(1,p):
        fact[k]=fact[k-1]*k%p
    inv=lambda x: pow(x%p,-1,p)
    a={}
    for j in range(L,U+1):
        num=(-1)**(m+j+1)*fact[m]*fact[j-m-1]*fact[2*m]
        den=fact[2*m-j]*fact[j]**2
        a[j]=num*inv(den)%p
    h={}
    for l in range(1,U+1):
        num=2*fact[m]*fact[2*m]*fact[l-1]**2
        den=fact[l+m]*fact[l+2*m]
        h[l]=num*inv(den)%p
    v={j:a[j]*inv(pow(2,j,p))%p for j in a}
    g={l:h[l]*pow(2,l,p)%p for l in h}
    choose=lambda n,k:fact[n]*inv(fact[k]*fact[n-k])%p
    lhs=U*U*g[U]*sum(v[j]*choose(3*m+U-j,3*m)*inv(pow(2,U-j,p))
                       for j in range(L,U+1))%p
    rhs=L*L*v[L]*sum(g[l]*choose(3*m-L+l,3*m)*inv(pow(2,l-L,p))
                       for l in range(L,U+1))%p
    assert lhs==rhs,(p,lhs,rhs)
    F0=sum(a.values())%p; G0=sum(h.values())%p
    Fprime=-2*sum(j*a[j] for j in a)%p
    Gprime=2*sum(l*h[l] for l in h)%p
    w=(F0*Gprime-G0*Fprime)%p
    expected=2*inv(3*m)*((2-U*U*h[U])*F0+L*L*a[L]*G0)%p
    assert w==expected
    return w

def finite_part_pairs(m):
    """Exact source-labelled complementary triangle (Theorem O)."""
    L,U=m+1,2*m
    a={j:Q((-1)**(m+j+1)*factorial(m)*factorial(j-m-1)*factorial(2*m),
           factorial(2*m-j)*factorial(j)**2) for j in range(L,U+1)}
    h={l:Q(2*factorial(m)*factorial(2*m)*factorial(l-1)**2,
           factorial(l+m)*factorial(l+2*m)) for l in range(1,U+1)}
    return Q((-1)**(3*m),2**(3*m))*sum(
        ((j+l)*comb(3*m+l-j,3*m)*a[j]*h[l]
          for j in range(L,U+1) for l in range(j,U+1)),Q(0))

def finite_part_via_jets(m):
    """Independent extraction via the derivative jet of F G' - G F'."""
    L,U=m+1,2*m
    a={j:Q((-1)**(m+j+1)*factorial(m)*factorial(j-m-1)*factorial(2*m),
           factorial(2*m-j)*factorial(j)**2) for j in range(L,U+1)}
    h={l:Q(2*factorial(m)*factorial(2*m)*factorial(l-1)**2,
           factorial(l+m)*factorial(l+2*m)) for l in range(1,U+1)}
    v={j:a[j]/2**j for j in a}
    g={l:h[l]*2**l for l in h}
    def generalized_binomial(e,r):
        q=1
        for k in range(r):
            q*=e-k
        return Q(q,factorial(r))
    n=3*m
    coefficient=Q(0)
    for r in range(n+1):
        jet=sum(((j+l)*v[j]*g[l]*generalized_binomial(l-j-1,r)
                 *Q(2)**(r-(l-j-1)) for j in a for l in h),Q(0))
        coefficient+=comb(n+1,n-r)*jet/Q(2**r)
    return Q((-1)**n,2**(n+1))*coefficient

def middle_reflection(m):
    """Original signed middle-rank port; NOT a Frobenius/CM Result."""
    L,U=m+1,2*m
    a={j:Q((-1)**(m+j+1)*factorial(m)*factorial(j-m-1)*factorial(2*m),
           factorial(2*m-j)*factorial(j)**2) for j in range(L,U+1)}
    h={l:Q(2*factorial(m)*factorial(2*m)*factorial(l-1)**2,
           factorial(l+m)*factorial(l+2*m)) for l in range(1,U+1)}
    v={j:a[j]/2**j for j in a}
    g={l:h[l]*2**l for l in h}
    return -sum((v[j]*sum(((6*(j-l)+1)*g[l] for l in range(1,j+1)),Q(0))
                 for j in range(L,U+1)),Q(0))/216

def rational_mod(x,p):
    return x.numerator*pow(x.denominator,-1,p)%p

if __name__=="__main__":
    for m in range(1,21):
        exact(m)
    for m in range(1,21):
        finite_part_pairs(m)
    for m in range(1,13):
        assert finite_part_via_jets(m)==finite_part_pairs(m)
    assert finite_part_pairs(2)==Q(23,115200)
    assert rational_mod(finite_part_pairs(2),13)==7
    assert rational_mod(middle_reflection(2),13)==2
    pp=list(primes_upto(997))
    wz={p:mod_exact(p) for p in pp}
    assert len(pp)==80
    print("PASS rational m=1..20; F_p primes=80 (7..997); finite-part jets m=1..12")
    print("Examples: m=1",exact(1),"; m=2",exact(2))
    print("sample W mod p:", {p:wz[p] for p in (7,13,19,31,373,997)})
    print("nonzero W among checked primes:",sum(w!=0 for w in wz.values()),"/",len(wz))
    print("p=13: finite-part",rational_mod(finite_part_pairs(2),13),"versus reflection middle",rational_mod(middle_reflection(2),13))