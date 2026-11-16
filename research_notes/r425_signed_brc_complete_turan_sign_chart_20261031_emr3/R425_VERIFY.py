#!/usr/bin/env python3
"""R425 exact signed-BRC edge classification, standard-library-only.

Checks symbolic-polynomial identity with explicit degree bound and independently
checks the Catalan projection against original signed coefficient extraction.
Finite grids are diagnostics, NOT proofs of the unbounded s>=3 domain.
"""
import argparse
from math import comb
from fractions import Fraction
import json
from pathlib import Path


def C(n, k):
    return comb(n, k) if 0 <= k <= n and n >= 0 else 0


def cat(n):
    return C(2*n, n)//(n+1) if n >= 0 else 0


def delta_raw(r, q):
    """Original signed (1-t) coefficient, retaining subtraction/cancellation."""
    n = r-q
    assert 0 <= q <= r
    return sum(C(n, j)*(C(2*q, r-2*j)-C(2*q, r-2*j-1))
               for j in range(n+1))


def delta_catalan(r, q):
    assert 1 <= q <= r
    return sum(C(q-1, j)*2**(q-1-j)*cat((r-q+j)//2)
               for j in range(q) if (r-q+j) % 2 == 0)


def H(r, q):
    assert 0 <= q <= r
    return C(r+q, 2*q)*(delta_raw(r, q) if q == 0 else delta_catalan(r, q))


def D(r, s):
    return H(r, s)**2 - H(r, s-1)*H(r, s+1)


def predicted_sign(r, s):
    if s == 1 and r % 2 == 0:
        return -1
    if (r, s) in ((3, 2), (5, 2)):
        return -1
    return 1


def test_polynomial_identity():
    """Clear denominators of the s=2 odd-r formula.

    The resulting integer polynomial T(k) has degree at most 11, so 12
    distinct exact integer roots imply T is identically zero. This is a
    complete symbolic identity certificate, not a numerical extrapolation.
    """
    def term(k):
        a = 1
        for j in range(4): a *= 2*k+j  # 24 A
        b = (2*k+1)*(2*k+2)  # 2 B
        c = 1
        for j in range(-1, 5): c *= 2*k+j  # 720 C
        f = 2*k*k - 3*k - 4
        return 5*a*a*(2*k-1)*5*k*(2*k+3) - \
            2*b*c*(4*k+1)*5*k*(2*k+3) - 5*a*a*(2*k-1)*f
    for k in range(1, 13):
        assert term(k) == 0, (k, term(k))
    return 12


def verify(rmax=144, raw_rmax=70, edge_kmax=512):
    assert rmax >= 7 and raw_rmax <= rmax
    degree_points = test_polynomial_identity()
    raw_checks = 0
    for r in range(2, raw_rmax+1):
        for q in range(1, r+1):
            assert delta_raw(r, q) == delta_catalan(r, q), (r, q)
            raw_checks += 1
    finite_grid = 0
    positives = 0
    negatives = []
    for r in range(2, rmax+1):
        for s in range(1, r):
            d = D(r, s)
            assert d != 0, (r, s)
            assert (1 if d > 0 else -1) == predicted_sign(r, s), (r, s, d)
            finite_grid += 1
            if d > 0: positives += 1
            else: negatives.append({'r':r,'s':s,'D':str(d)})
    edge_identity = 0
    for k in range(1, edge_kmax+1):
        r_odd=2*k+1
        c=cat(k)
        a=C(2*k+3,4)
        b=C(2*k+2,2)
        cc=C(2*k+4,6)
        assert D(r_odd,1) == c*c*(b*b + (2*k+1)*a)
        r_even=2*k
        assert D(r_even,1) == -2*C(2*k,k)*C(2*k+2,4)*cat(k-1)
        assert D(r_odd,2) == Fraction(c*c*a*a*(2*k*k-3*k-4),5*k*(2*k+3))
        if k >= 2:
            assert D(r_even,2) == (2*C(2*k+2,4)*cat(k-1))**2
        edge_identity += 3 + (k>=2)
    return {'status':'R425_EXACT_PASS','symbolic_identity_degree_bound':11,
            'distinct_integer_roots_checked':degree_points,
            'signed_raw_to_catalan_checks':raw_checks,
            'finite_grid_r_max':rmax,'finite_grid_pairs':finite_grid,
            'finite_grid_positive_pairs':positives,
            'finite_grid_negative_count':len(negatives),
            'finite_grid_negative_first':negatives[:6],
            'finite_grid_negative_last':negatives[-6:],
            'edge_formula_direct_checks':edge_identity,
            'edge_formula_k_max':edge_kmax,
            'exact_negative_exceptions_s2':{'r3':str(D(3,2)),'r5':str(D(5,2))},
            'scope':'finite raw/closed-form verification plus degree-bound identity; unbounded s>=3 uses R404-R418,R424 author-side certificates'}


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--rmax',type=int,default=144)
    p.add_argument('--raw-rmax',type=int,default=70)
    p.add_argument('--edge-kmax',type=int,default=512)
    p.add_argument('--out',default='R425_EVIDENCE.json')
    a=p.parse_args()
    res=verify(a.rmax,a.raw_rmax,a.edge_kmax)
    Path(a.out).write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(res['status'],res['distinct_integer_roots_checked'],res['signed_raw_to_catalan_checks'],res['finite_grid_pairs'],res['finite_grid_negative_count'],res['edge_formula_direct_checks'])
