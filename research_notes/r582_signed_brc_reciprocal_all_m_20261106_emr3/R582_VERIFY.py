#!/usr/bin/env python3
"""R582: independent exact finite checks + analytic-asymptotic sanity checks.

The all-m result is proved analytically in R582_PROOF.zh-CN.md; the finite
program is a reproducible cross-check, not a substitute for endpoint analysis.
"""
from fractions import Fraction as F
from math import comb
from sympy import Rational, Symbol, sqrt, log, series, binomial, simplify


def catalan(n):
    assert n >= 0
    return comb(2*n, n) // (n+1)


def H_original(k, s):
    assert k >= 2 and 2 <= s <= 2*k+1
    return comb(2*k+1+s, 2*s)*sum(
        comb(s-1, 2*q)*4**q*catalan(k-q)
        for q in range(min(k, (s-1)//2)+1)
    )


def elementary(k, j):
    n = 2*k+1
    assert 0 <= j <= n-2
    return F(comb(2*n-j, j)*sum(
        comb(j, ell)*(-2)**ell*catalan(n-ell)
        for ell in range(j+1)
    ), catalan(n))


def inverse_power_sums(k, max_m):
    degree = 2*k-1
    assert max_m <= degree
    es = [F(1)] + [elementary(k, j) for j in range(1,max_m+1)]
    ps = [F(0)]*(max_m+1)
    for m in range(1,max_m+1):
        ps[m] = sum((-1)**(j-1)*es[j]*ps[m-j] for j in range(1,m)) + (-1)**(m-1)*m*es[m]
    return ps


def symbolic_constants(max_m):
    t = Symbol('t')
    s = sqrt(1-2*t)
    alpha = (1+s)/2
    H = alpha*sqrt(s)/(2*s-1)**Rational(3,2)
    leading = series(-2*log(alpha), t, 0, max_m+1).removeO().expand()
    correction = series(log(H), t, 0, max_m+1).removeO().expand()
    cs = {}
    for m in range(1,max_m+1):
        mu = binomial(2*m,m)/2**m
        assert simplify(m*leading.coeff(t,m)-mu) == 0
        cs[m] = (F(int(mu.p),int(mu.q)), F(int((-m*correction.coeff(t,m)).p),int((-m*correction.coeff(t,m)).q)))
    return cs


def main():
    checks = 0
    for k in range(2,13):
        n=2*k+1
        for j in range(n-1):
            assert elementary(k,j) == F(H_original(k,n-j),H_original(k,n))
            checks += 1
    print('R582_SOURCE_CATALAN_EJ_EXACT_CHECKS',checks)

    constants = symbolic_constants(12)
    print('R582_ALL_M_FORMAL_LEADING_12_CHECKS_PASS')
    for m in [1,2,3,4,5,6,7,8,9,10,11,12]:
        print(f'B_{m}={constants[m][1]}',end='; ')
    print()
    print('R582_FINITE_POWERS_AND_TWO_TERM_RESIDUALS')
    for k in (10,20,40,80):
        n=2*k+1
        ps=inverse_power_sums(k, 12)
        for m in (1,2,4,8,12):
            mu,B=constants[m]
            error=ps[m]-n*mu-B
            assert m<=n-2
            print(f'k={k} m={m} Tm/d={float(ps[m]/(n-2)):.12g} exact_error={float(error):.9g} k_error={float(k*error):.9g}')
        assert ps[1] == n-2
    print('R582_ALL_M_ANALYTIC_FORMULA_FINITE_CROSSCHECK_PASS')


if __name__=='__main__':
    main()
