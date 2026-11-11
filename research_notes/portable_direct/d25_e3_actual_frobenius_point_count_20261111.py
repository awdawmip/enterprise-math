#!/usr/bin/env python3
"""Exact original-E3 geometric Frobenius checks at inert CM primes.

AUTHOR_SIDE / FINITE_EXACT_CERTIFICATE / UNREVIEWED / NOT_NATIVE_H0B0.
Fp2=Fp[T]/(T*T-2); curves are the Chisholm E3(t) with t=(2-T)/4.
Two character paths count EVERY x in Fp2; no floating point or oracle.
"""
from math import comb

PRIMES = (13, 19, 37, 43, 109, 139, 157, 373)

def mul(a, b, p):
    return ((a[0]*b[0]+2*a[1]*b[1])%p,
            (a[0]*b[1]+a[1]*b[0])%p)

def power(x, n, p):
    out=(1,0)
    while n:
        if n & 1:
            out=mul(out,x,p)
        x=mul(x,x,p)
        n//=2
    return out

def const_curve(p):
    inv108=pow(108,-1,p)
    a3=(2*inv108%p, -inv108%p)  # E3: y^2+xy+(t/27)y=x^3.
    assert pow(2,(p-1)//2,p)==p-1  # T^2=2 is irreducible.
    return a3

def point_count_norm(p):
    """Full character sum by norm Fp2 -> Fp, precomputed Legendre table."""
    a,b=const_curve(p)
    chi=[0]*p
    for n in range(1,p):
        chi[n]=1 if pow(n,(p-1)//2,p)==1 else -1
    total=0
    for u in range(p):
        for v in range(p):
            # D(x)=(x+a3)^2+4*x^3, x=u+vT
            x2_0=(u*u+2*v*v)%p
            x2_1=2*u*v%p
            x3_0=(x2_0*u+2*x2_1*v)%p
            x3_1=(x2_0*v+x2_1*u)%p
            d0=(4*x3_0+(u+a)**2+2*(v+b)**2)%p
            d1=(4*x3_1+2*(u+a)*(v+b))%p
            norm=(d0*d0-2*d1*d1)%p
            total+=chi[norm]
    return p*p+1+total

def point_count_power(p):
    """Independent point count by direct Fp2 exponent and generic ring products."""
    a3=const_curve(p)
    total=0
    for u in range(p):
        for v in range(p):
            x=(u,v)
            xa=((u+a3[0])%p,(v+a3[1])%p)
            x3=mul(mul(x,x,p),x,p)
            y=mul(xa,xa,p)
            d=((y[0]+4*x3[0])%p,(y[1]+4*x3[1])%p)
            if d==(0,0): continue
            c=power(d,(p*p-1)//2,p)
            assert c in ((1,0),(p-1,0)), (p,u,v,c)
            total+=1 if c==(1,0) else -1
    return p*p+1+total

def e3_formal_hasse_mod_p(p):
    """Independent original E3 fixed-z differential coefficient (Lemma 12)."""
    a3=const_curve(p)
    a=(1,0)
    accum=(0,0)
    n=p-1
    for j in range(n//3+1):
        c=comb(n-j,j)*comb(n-2*j,j)
        accum=((accum[0]+c*a[0])%p,(accum[1]+c*a[1])%p)
        a=mul(a,a3,p)
    return accum

def main():
    assert 1728*2798 == 4834944
    assert 1728**2*(1399**2-2*988**2) == 14670139392
    # From c4, Delta of E3, j(E3(t)) = 1728*(1399+988*T),
    # a root of Hilbert class polynomial D=-24.
    for p in PRIMES:
        assert p%24 in (13,19)
        n1=point_count_norm(p)
        n2=point_count_power(p)
        assert n1 == n2 == (p-1)**2, (p,n1,n2)
        assert e3_formal_hasse_mod_p(p) == (0,0)
        trace=p*p+1-n1
        assert trace==2*p
        print(f'p={p:>3}  q={p*p:>6}  #E(Fq)={n1:>6}  trace={trace:>4}  Hasse=(0,0)  PASS')
    print('PASS: all 8 complete norm and power character enumerations, original E3 Hasse coefficients')

if __name__=='__main__':main()
