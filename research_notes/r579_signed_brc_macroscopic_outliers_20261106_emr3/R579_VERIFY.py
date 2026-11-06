#!/usr/bin/env python3
"""Exact finite checks for R579: frozen signed-BRC auxiliary scalar Q_k.
Scientific input: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f,
normalization: R576@05de5b8b08acaa53243bf91bc7a2fac70c2408a6.
This verifies examples; infinite-parameter claims use the separate analytic proof.
"""
from fractions import Fraction
from math import comb, factorial
import sympy as sp


def catalan(n):
    return comb(2*n, n)//(n+1)


def H(k, s):
    r=2*k+1
    return comb(r+s, 2*s)*sum(comb(s-1, 2*q)*4**q*catalan(k-q)
                              for q in range(min(k,(s-1)//2)+1))


def coeffs(k):
    d=2*k-1
    h2=H(k,2)
    assert h2>0
    return [Fraction(1)] + [Fraction(H(k,j+2),h2) for j in range(1,d+1)]


def evaluate_q(k, t):
    # exact Horner for Q_k(t)=t^d - A_1*t^(d-1)+... - A_d
    v=Fraction(1)
    for j,a in enumerate(coeffs(k)[1:],1):
        v=v*t+(-1)**j*a
    return v


def evaluate_Fk(k,z):
    # normalized reciprocal polynomial F_k(z)=sum (-1)^j A_j(z/k^2)^j
    v=Fraction(0)
    x=Fraction(z,k*k)
    for j,a in enumerate(coeffs(k)):
        v+=(-1)**j*a*x**j
    return v


def f_coeff(j):
    return Fraction((-1)**j*24*8**j,factorial(2*j+4))


def main():
    for k in range(2,19):
        d=2*k-1
        a=coeffs(k)
        assert len(a)==d+1 and all(v>0 for v in a)
        assert evaluate_q(k,0) == -a[-1] < 0
        # Exact coefficient formula Q_k(-x) = -sum_j A_j*x^(d-j)
        for x in (0,1,2,5,10):
            actual=evaluate_q(k,-x)
            expected=-sum(a[j]*x**(d-j) for j in range(d+1))
            assert actual==expected<0
        # By F_k(z)=(z/k^2)^d Q_k(k^2/z), direct identity at rational z
        for z in (Fraction(1,10),Fraction(1),Fraction(7,3),Fraction(-2)):
            q=evaluate_q(k, Fraction(k*k,1)/z)
            assert evaluate_Fk(k,z)==(z/Fraction(k*k,1))**d*q
    x=sp.symbols('x')
    counts=[]
    for k in range(2,21):
        a=coeffs(k)
        poly=sp.Poly(sum((-1)**j*sp.Rational(c.numerator,c.denominator)*x**(len(a)-1-j)
                         for j,c in enumerate(a)),x)
        assert sp.gcd(poly,poly.diff()).degree()==0  # exact squarefree check
        count=poly.count_roots(-sp.oo,sp.oo)  # exact Sturm-based count
        assert count==1, (k,count)
        counts.append((k,int(count)))
    print('Sturm exact real-root counts:',counts)
    # Coefficient convergence (finite snapshots, not universal proof)
    for j in range(1,6):
        examples=[]
        for k in (12,24,48):
            a=coeffs(k)[j]
            v=((-1)**j*a/Fraction(k*k)**j)/f_coeff(j)
            examples.append(str(v))
        print('j=',j,'coefficient_ratio_to_limit for k=12,24,48:',', '.join(examples))
    print('R579_SCALED_REAL_ROOT_EXACT_FINITE_CHECK_PASS')

if __name__=='__main__':main()
