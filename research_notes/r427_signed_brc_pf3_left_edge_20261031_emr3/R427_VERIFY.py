#!/usr/bin/env python3
"""R427 exact signed-BRC left-edge and complete finite-order-3 Toeplitz checks.

Python standard library; all integer/Fraction arithmetic. Test coverage:
  - general left-edge factorization from r=4 through 512 (not a universal proof);
  - for each 5<=r<=24, every 1x1, every relevant 2x2 and every
    relevant 3x3 Toeplitz minor, using proved support reduction.
Analytic infinite-parameter result is proved in R427_PROOF.zh-CN.md.
"""
from fractions import Fraction
from math import comb
import json
import hashlib
from pathlib import Path


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def signed_delta(r, s):
    assert 2 <= s <= r
    return sum(choose(r-s, j) * (choose(2*s, r-2*j) - choose(2*s, r-2*j-1))
               for j in range(r-s+1))


def catalan(j):
    return comb(2*j, j) // (j+1)


def alternate_delta(r, s):
    assert 2 <= s <= r
    ans = 0
    for ell in range(s):
        if r - 1 - ell >= 0 and (r-1-ell) % 2 == 0:
            ans += choose(s-1, ell) * (2**ell) * catalan((r-1-ell)//2)
    return ans


def row(r):
    return [comb(r+s, 2*s)*signed_delta(r,s) for s in range(2,r+1)]


def det3(a,b,c,d,e,f,g,h,i):
    return a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h


def left_edge(a):
    a0,a1,a2,a3=(a+[0,0,0,0])[:4]
    return a1**3 - 2*a0*a1*a2 + a0*a0*a3


def formula(r):
    assert r>=4
    if r%2==0:
        k = r//2
        F = 24*k**4 - 36*k**3 - 56*k**2 -31*k -6
        return Fraction((k-1)*(2*k+3)*F, 23625)
    k=(r-1)//2
    G = 192*k**5 +1392*k**4 +5330*k**3 +10253*k**2 +10246*k +4087
    return Fraction((k+2)*G, 94500)


def complete_finite(r):
    a=row(r)
    n=len(a)-1
    def val(k):
        return a[k] if 0<=k<=n else 0
    assert all(v>0 for v in a)
    # Ordered matching lemma: nonzero determinant implies j_l-i_l in [0,n].
    # Row gap > n splits the minor into ordered blocks (or determinant zero).
    count2=pos2=zero2=0
    for gap in range(1,n+1):
        for j0 in range(n+1):
            for j1 in range(max(gap,j0+1),gap+n+1):
                D=val(j0)*val(j1-gap)-val(j1)*val(j0-gap)
                count2+=1
                if D<0: raise AssertionError(('PF2',r,gap,j0,j1,D))
                if D:pos2+=1
                else:zero2+=1
    count3=pos3=zero3=0
    for g1 in range(1,n+1):
        i1=g1
        for g2 in range(1,n+1):
            i2=g1+g2
            for j0 in range(n+1):
                A=val(j0);D=val(j0-i1);G=val(j0-i2)
                for j1 in range(max(i1,j0+1),i1+n+1):
                    B=val(j1);E=val(j1-i1);H=val(j1-i2)
                    for j2 in range(max(i2,j1+1),i2+n+1):
                        X=det3(A,B,val(j2),D,E,val(j2-i1),G,H,val(j2-i2))
                        count3+=1
                        if X<0:raise AssertionError(('PF3',r,(0,i1,i2),(j0,j1,j2),X))
                        if X:pos3+=1
                        else:zero3+=1
    return {'r':r,'n':n,'two_checked':count2,'two_positive':pos2,'two_zero':zero2,
            'three_checked':count3,'three_positive':pos3,'three_zero':zero3}



def verify_polynomial_identities():
    """Certified seven-point identities: both sides polynomial in k of degree <=6."""
    for k in range(2,9):
        b1=Fraction(2*(k-1)*(2*k+3),15)
        b2=Fraction((k-1)*(k+2)*(2*k+3)*(8*k-9),420)
        b3=Fraction((k-2)*(k-1)*(k+2)*(2*k+3)*(2*k+5)*(4*k-3),4725)
        assert b1**3-2*b1*b2+b3 == formula(2*k)
        b1=Fraction((k+2)*(4*k+1),15)
        b2=Fraction((k-1)*(k+2)*(2*k+5)*(8*k+5),420)
        b3=Fraction((k-1)*(k+2)*(k+3)*(2*k+5)*(32*k*k-16*k-33),18900)
        assert b1**3-2*b1*b2+b3 == formula(2*k+1)
    # All displayed b_i and formula sides are rational polynomials in k of degree <= 6.
    # Seven distinct exact integer equalities establish each identity identically.
    print('R427_POLYNOMIAL_IDENTITY_CERTIFIED',2,7,'degree_bound_6')

def run():
    verify_polynomial_identities()
    for r in range(4,513):
        a=[comb(r+s,2*s)*signed_delta(r,s) if s<=r else 0 for s in range(2,6)]
        assert left_edge(a)==a[0]**3*formula(r),('left formula',r)
        for s in range(2,min(8,r+1)):
            assert signed_delta(r,s)==alternate_delta(r,s),('Catalan',r,s)
    assert left_edge(row(4))==-1568
    results=[]
    for r in range(5,25):
        item=complete_finite(r)
        results.append(item)
        print('R427_FINITE_PASS',r,item['two_checked'],item['three_checked'],flush=True)
    summary={'schema':'R427_EXACT_EVIDENCE_V1',
       'analytic_formula_numerical_checks':'r=4..512 inclusive',
       'catalan_checks':'s=2..min(r,7), r=4..512',
       'r4_negative_left_edge':-1568,
       'complete_pf3_range':'5<=r<=24',
       'support_reduction':'Rows gaps <= n=r-2 plus sorted nonzero diagonal; other gaps factor into lower-order minors',
       'checks':results,
       'total_two_checked':sum(x['two_checked'] for x in results),
       'total_three_checked':sum(x['three_checked'] for x in results)}
    body=json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    with Path(__file__).with_name('R427_EVIDENCE.json').open('w', encoding='utf-8') as out:out.write(body)
    print('R427_EXACT_PASS',summary['total_two_checked'],summary['total_three_checked'],
          hashlib.sha256(body.encode()).hexdigest())

if __name__=='__main__':run()
