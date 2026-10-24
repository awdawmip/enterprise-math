#!/usr/bin/env python3
"""Exact author-side source-WZ p-adic unit-factor jets beyond the first nonunit index.
No native CM/DP experiment, floating-point operations, or nonunit inversions.
"""
from fractions import Fraction as F
from math import factorial, isqrt


def factor(a, c, exponent, M):
    """Multiply a truncated jet by (1+c*z)**exponent without dividing by degree."""
    D = len(a)
    for _ in range(abs(exponent)):
        if exponent > 0:
            for d in range(D-1, 0, -1):
                a[d] = (a[d] + c*a[d-1]) % M
        else:
            for d in range(1, D):
                a[d] = (a[d] - c*a[d-1]) % M
    return a


def modq(x, p, D):
    x = F(x)
    assert x.denominator % p, (p, D, x.denominator)
    M = p**D
    return x.numerator*pow(x.denominator, -1, M) % M


def unit_U(p, D):
    n, M = (p-1)//3, p**D
    t = (108**(p-1)-1)//p
    a = [1] + [0]*(D-1)
    factor(a, t % M, -1, M)
    for k in range(2, n+1):
        factor(a, modq(F(-1,k),p,D), 2, M)
    for j in range(1, p-1):
        factor(a, modq(F(1,j),p,D), 2, M)
    for j in range(1, n):
        factor(a, modq(F(1,j),p,D), -1, M)
    return a


def unit_sigma(p, D):
    n, M = (p-1)//3, p**D
    a = [1] + [0]*(D-1)
    for c, e in [(-1,-2),(2,-2),(5,-2),(8,-1),(11,-1)]:
        factor(a,modq(F(1,c),p,D),e,M)
    for base, e in [(2,-2),(3,-3)]:
        factor(a,((base**(p-1)-1)//p) % M,e,M)
    for j in range(1,n):
        factor(a,modq(F(-1,j),p,D),2,M)
    for j in range(1,p):
        factor(a,modq(F(1,j),p,D),2,M)
    for j in range(1,6):
        factor(a,modq(F(1,j),p,D),1,M)
    for j in range(1,5):
        factor(a,modq(F(2,j),p,D),1,M)
    factor(a,2,1,M)
    for j in range(1,3):
        factor(a,modq(F(1,j),p,D),-2,M)
    for j in range(1,n+5):
        factor(a,modq(F(1,j),p,D),-1,M)
    return a


def evaluate(a, p, D):
    M, s = p**D, 0
    for c in reversed(a):
        s = (s*p+c) % M
    return s


def C(p):
    return F((p+1)*(2*p-1)**2*(30*p*p+77*p+40),
             2*(p+2)*(2*p+1)*(4*p-1)*(4*p+5))


def R(k,p):
    return F((2*p+2*k+3)*(2*p+3*k-1)*(2*p+3*k),
             4*(2*p+3*k+1)*(p+k+2)*(4*p+3*k+11))


def B(p):
    s, q = F(0), F(1)
    for j in range(1,5):
        s += (6*p+6*j+7)*q
        if j<4:
            q *= R(j,p)
    return s


def V(r,t):
    return F(factorial(6*r)*factorial(4*r+2*t)*factorial(3*t),
             3**(6*r)*216**t*factorial(2*r)*factorial(t)**2
             *factorial(2*r+t)**2*factorial(4*r+t))


def W(r,t):
    return (6*t+12*r+1)*V(r,t)


def source_quotient(p):
    m = (p-1)//6
    return (sum((W(m+1,t) for t in range(4*m+5)),F(0))
            - sum((W(m,t) for t in range(4*m+1)),F(0)))/p


def source_U(p):
    n=(p-1)//3
    v=F(n,108**(p-1))
    for k in range(2,n+1):
        v *= (1-F(p,k))**2
    for j in range(1,p-1):
        v *= (1+F(p,j))**2
    for j in range(1,n):
        v /= (1+F(p,j))
    return v


def check(p,D):
    assert p>=13 and p%6==1 and D>p
    assert all(p%d for d in range(2,isqrt(p)+1))
    m=(p-1)//6
    M=p**D
    up=(2*m*evaluate(unit_U(p,D),p,D))%M
    sigma=(modq(F(3,220),p,D)*evaluate(unit_sigma(p,D),p,D))%M
    assert up==modq(source_U(p),p,D)
    assert sigma==modq(V(m+1,4*m+1)/p**2,p,D)
    projected=(up*modq(C(p),p,D)+p*sigma*modq(B(p),p,D))%M
    exact=modq(source_quotient(p),p,D)
    assert projected==exact
    print("PASS p=%d D=%d quotient residue digits=%d modulus digits=%d"%(p,D,len(str(exact)),len(str(M))))
    if D<=40:
        print(" quotient residue =",exact)


if __name__=="__main__":
    for p,D in [(13,15),(19,21),(31,33),(37,39),(13,171)]:
        check(p,D)
