#!/usr/bin/env python3
"""R581: exact, non-floating reciprocal moments p5..p8 of frozen R462 auxiliary Q_k.

Input definition from R580_PROOF.zh-CN.md; only checks auxiliary scalar roots.
Uses Python standard library for independent finite arithmetic and sympy for
an all-k symbolic rational-identity checker.
"""
from fractions import Fraction
from math import comb
import sympy as sp


def cat(n):
    return comb(2*n, n)//(n+1)


def direct_h(k, s):
    return comb(2*k+1+s,2*s)*sum(
        comb(s-1,2*q)*4**q*cat(k-q)
        for q in range(min(k,(s-1)//2)+1))


def moments_direct(k, bound=8):
    d=2*k-1
    bound=min(bound,d)
    e=[Fraction(1)]
    for j in range(1,bound+1):
        e.append(Fraction(direct_h(k,2*k+1-j),direct_h(k,2*k+1)))
    p=[Fraction(0)]
    for m in range(1,bound+1):
        p.append(sum((-1)**(j-1)*e[j]*p[m-j] for j in range(1,m))
                 +(-1)**(m-1)*m*e[m])
    return p


def formula_pairs(k):
    return {
      5:(2*(504*k**4-5396*k**3+8038*k**2-1729*k-1312), (4*k-1)*(4*k+1)**2),
      6:(2*(14784*k**6-251104*k**5+655384*k**4-461328*k**3-103114*k**2+120328*k+26817),(4*k-3)*(4*k-1)*(4*k+1)**3),
      7:(4*(13728*k**6-344224*k**5+1190908*k**4-1194414*k**3-85942*k**2+401380*k+84813),(4*k-3)*(4*k-1)*(4*k+1)**3),
      8:(6589440*k**9-247773440*k**8+1362233856*k**7-2748270080*k**6+1830380224*k**5+637741792*k**4-779517536*k**3-192226656*k**2+41362252*k+10253895,(4*k-5)*(4*k-3)*(4*k-1)**2*(4*k+1)**4),
    }


def symbolic_proof():
    k=sp.symbols('k',integer=True,positive=True)
    ratio=[sp.Integer(1)]
    for ell in range(1,9):
        n=2*k+2-ell
        ratio.append(sp.cancel(ratio[-1]*(n+1)/(2*(2*n-1))))
    e=[sp.Integer(1)]
    p=[sp.Integer(0)]
    for j in range(1,9):
        pref=sp.prod(4*k+2-j-r for r in range(j))/sp.factorial(j)
        ej=sp.cancel(pref*sum(sp.binomial(j,ell)*(-2)**ell*ratio[ell] for ell in range(j+1)))
        e.append(ej)
        pj=sp.factor(sp.cancel(sum((-1)**(r-1)*e[r]*p[j-r] for r in range(1,j)) + (-1)**(j-1)*j*e[j]))
        p.append(pj)
        if j >= 5:
            num,den=formula_pairs(k)[j]
            assert sp.cancel(pj - num/den)==0
            lim=sp.limit(pj/(2*k-1),k,sp.oo)
            assert sp.simplify(lim-sp.binomial(2*j,j)/2**j)==0
            print('symbolic m=',j,'exact rational function and limit PASS; limit=',lim)


def main():
    symbolic_proof()
    counter=0
    for k in range(2,91):
        p=moments_direct(k)
        for m in range(5,min(8,2*k-1)+1):
            assert p[m]==Fraction(*formula_pairs(k)[m]), (k,m)
            counter+=1
    assert counter==sum(max(0,min(8,2*k-1)-4) for k in range(2,91))
    print('independent integer/Fraction checks k=2..90, m=5..min(8,2k-1):',counter,'PASS')
    print('R581_RECIPROCAL_P5_P8_EXACT_PASS')

if __name__=='__main__':
    main()
