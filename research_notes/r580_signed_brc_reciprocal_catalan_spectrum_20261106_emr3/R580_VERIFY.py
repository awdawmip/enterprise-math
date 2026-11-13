#!/usr/bin/env python3
"""R580 exact cross-checks for frozen R462 signed-BRC auxiliary scalar Q_k.
Source: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f.
Mathematical proof is in R580_PROOF.zh-CN.md; this script independently checks its identities.
Requires Python >=3.10 standard library only (integer and Fraction arithmetic).
"""
from math import comb, factorial
from fractions import Fraction


def cat(n):
    return comb(2*n, n)//(n+1) if n >= 0 else 0


def H(k, s):
    assert 2 <= s <= 2*k+1
    return comb(2*k+1+s, 2*s)*sum(
        comb(s-1, 2*q)*4**q*cat(k-q)
        for q in range(min(k, (s-1)//2)+1)
    )


def trailing_h(k,j):
    # Independent coefficient extraction / Catalan finite-difference formula.
    assert 0 <= j <= 2*k-1
    return comb(4*k+2-j, j)*sum(
        comb(j, ell)*(-2)**ell*cat(2*k+1-ell)
        for ell in range(j+1)
    )


def p_inverses_from_end(k, mmax):
    e = [Fraction(1)] + [Fraction(H(k, 2*k+1-j), H(k, 2*k+1)) for j in range(1,mmax+1)]
    p = [Fraction(0)]
    for m in range(1, mmax+1):
        p.append(sum((-1)**(j-1)*e[j]*p[m-j] for j in range(1,m))
                 +(-1)**(m-1)*m*e[m])
    return p


def exact_formulas(k):
    return [None,
        Fraction(2*k-1),
        Fraction(12*k*k-20*k+1, 4*k+1),
        Fraction(2*(2*k-1)*(5*k-16), 4*k+1),
        Fraction(560*k**4-3696*k**3+3320*k*k-96*k-337,
                 (4*k-1)*(4*k+1)**2)]


def main():
    total=0
    for k in range(2,41):
        endpoint=H(k, 2*k+1)
        assert endpoint == cat(2*k+1)
        for j in range(2*k):
            assert H(k,2*k+1-j) == trailing_h(k,j), (k,j)
            total += 1
    print('Full Catalan finite-difference identities: k=2..40, j=0..2k-1, checks=',total)
    for k in range(2,181):
        assert H(k,2*k+1) == cat(2*k+1)
        assert H(k,2) == comb(2*k+3,4)*cat(k)
        mmax=min(4,2*k-1)
        p=p_inverses_from_end(k,mmax)
        assert p[1:] == exact_formulas(k)[1:mmax+1], (k,p)
        for j in range(mmax+1):
            assert H(k,2*k+1-j)==trailing_h(k,j), (k,j)
    print('Exact reciprocal Newton-moment formulas (m<=min(4,2k-1)) and endpoint determinant: k=2..180')
    for k in (2,5,10,20,50,100,180):
        d=2*k-1
        P=p_inverses_from_end(k,min(4,d))
        A=Fraction(cat(2*k+1), comb(2*k+3,4)*cat(k))
        print('k=',k,'det-product=',str(A)[:55], 'inverse_moments_per_degree=',
              [round(float(P[m]/d),8) for m in range(1,min(4,d)+1)],
              'geomean_abs_root=',round(float(A)**(1/d),9))
    print('R580_CATALAN_REVERSE_COEFFICIENT_AND_RECIPROCAL_MOMENTS_EXACT_PASS')

if __name__ == '__main__':
    main()
