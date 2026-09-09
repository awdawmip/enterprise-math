"""Exact domain experiment for X6 coherent index arithmetic; not a new tool family.

Run: python experiments/x6_coherent_arithmetic_20260909/verify.py
Requires SymPy. Uses its column-lattice Hermite normal form unchanged.
Only bounded regression assertions are executed; the accompanying note supplies proofs.
"""
from __future__ import annotations
from collections import Counter
from functools import lru_cache
from itertools import product
from math import gcd, isqrt, lcm
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form as hnf

D = 6
I = sp.eye(D)


def integral(a: sp.MatrixBase) -> bool:
    return all(x.is_Integer for x in a)


def intersect(a: sp.MatrixBase, b: sp.MatrixBase) -> sp.ImmutableMatrix:
    """Full-rank integer column lattices, using (L cap M)* = L* + M*."""
    da, db = abs(int(a.det())), abs(int(b.det()))
    if not da or not db or not integral(a) or not integral(b):
        raise ValueError('full-rank integral bases required')
    scale = lcm(da, db)
    dual_generators = (scale*a.inv().T).row_join(scale*b.inv().T)
    if not integral(dual_generators):
        raise AssertionError('invalid common denominator')
    h = hnf(sp.Matrix(dual_generators.rows, dual_generators.cols, [int(x) for x in dual_generators]))
    c = scale*h.inv().T
    if not integral(c):
        raise AssertionError('intersection failed to be integral')
    out = sp.ImmutableMatrix(hnf(sp.Matrix(c.rows, c.cols, [int(x) for x in c])))
    assert integral(a.inv()*out) and integral(b.inv()*out)
    return out


@lru_cache(None)
def gaussian_block(p: int) -> sp.ImmutableMatrix:
    if not sp.isprime(p) or not (p == 2 or p % 4 == 1):
        raise ValueError('prime must be 2 or 1 mod 4')
    for a in range(isqrt(p)+1):
        b = isqrt(p-a*a)
        if a*a+b*b == p:
            return sp.ImmutableMatrix([[a,-b],[b,a]])
    raise AssertionError('two-square representation missing')


def local_basis(p: int, k: int) -> sp.ImmutableMatrix:
    if k < 0 or not sp.isprime(p):
        raise ValueError('prime and nonnegative exponent required')
    if p == 2 or p % 4 == 1:
        r,s = divmod(k,3)
        b = gaussian_block(p)
        return sp.ImmutableMatrix(sp.diag(*(b**(r+int(j<s)) for j in range(3))))
    r,s = divmod(k,6)
    return sp.ImmutableMatrix(sp.diag(*(p**(r+int(j<s)) for j in range(6))))


def closure_period(p: int) -> int:
    return 3 if p == 2 or p % 4 == 1 else 6


@lru_cache(None)
def basis(n: int) -> sp.ImmutableMatrix:
    """Declared basis section. Prefer a similarity basis at closure milestones.

    The local choices and axis pairing are explicit extra structure, not intrinsic.
    """
    if n < 1:
        raise ValueError('positive index required')
    factors = sorted((int(p),int(k)) for p,k in sp.factorint(n).items())
    if all(k % closure_period(p) == 0 for p,k in factors):
        c = I
        for p,k in factors:
            c = c*local_basis(p,k)
        out = sp.ImmutableMatrix(c)
    else:
        out = sp.ImmutableMatrix(I)
        for p,k in factors:
            out = intersect(out,local_basis(p,k))
    assert abs(out.det()) == n
    for p,k in factors:
        assert integral(local_basis(p,k).inv()*out)
    return out


def relative(n: int, m: int) -> sp.ImmutableMatrix:
    """Right-coordinate transport from index n to index n*m."""
    t = sp.ImmutableMatrix(basis(n).inv()*basis(n*m))
    assert integral(t) and abs(t.det()) == m
    return t


def delta(a: sp.MatrixBase) -> int:
    g = a.T*a
    return int(6*sp.trace(g*g)-sp.trace(g)**2)


def verify() -> dict:
    out: dict = {'status':'PASS', 'arithmetic':'exact integers/rationals',
                 'sympy_version':sp.__version__, 'dimension':D}
    # All 12 signed primitive moves on [-1,1]^6 (not only selected examples).
    radial_cases = 0
    for v in product((-1,0,1),repeat=D):
        q = sum(x*x for x in v)
        ell = sum(abs(x) for x in v)
        for j in range(D):
            for sign in (-1,1):
                w = list(v); w[j] += sign
                dq = sum(x*x for x in w)-q
                dl = sum(abs(x) for x in w)-ell
                assert dq != 0 and (dq>0) == (dl==1)
                radial_cases += 1
    out['radial_local_cases'] = radial_cases
    # HNF and the similarity basis need not be the same transport.
    for n in range(1,181):
        basis(n)
    out['all_index_bases_checked'] = [1,180]
    primes = (2,3,5,7)
    diamonds = 0
    for n in range(1,25):
        for p in primes:
            for q in primes:
                a = relative(n,p)*relative(n*p,q)
                b = relative(n,q)*relative(n*q,p)
                assert a == b == relative(n,p*q)
                diamonds += 1
    out['exact_multiplication_diamonds'] = diamonds
    # All gcds, not merely coprime factors: the nested local filtration gives lcm.
    intersections = 0
    for m in range(1,25):
        for n in range(1,25):
            assert intersect(basis(m),basis(n)) == hnf(basis(lcm(m,n)))
            intersections += 1
    out['lcm_intersections_checked'] = intersections
    milestones = (8,64,125,512,729,1000,5832,15625,91125)
    out['similarity_milestones'] = []
    for n in milestones:
        a = basis(n); g = a.T*a
        assert delta(a) == 0 and g == g[0,0]*I and int(g[0,0])**3 == n
        out['similarity_milestones'].append({'index':n,'q':int(g[0,0])})
    # One concrete 2/3 diamond with a convenient (non-HNF) local frame.
    b = sp.diag(sp.Matrix([[1,-1],[1,1]]),sp.eye(4))
    d3 = sp.diag(3,1,1,1,1,1)
    corrected3 = b.inv()*d3*b
    assert integral(corrected3) and corrected3[:2,:2] == sp.Matrix([[2,-1],[-1,2]])
    assert b*corrected3 == d3*b and b*d3 != d3*b
    out['two_three_correction_block'] = [[int(x) for x in row] for row in corrected3[:2,:2].tolist()]
    # An S6-invariant index-2 lattice need not have an S6-equivariant transporter.
    out['s6_centralizer_formula'] = 'a I + b J; determinant = a^5(a+6b)'
    assert not any(abs(a**5*(a+6*b0)) == 2 for a in range(-10,11) for b0 in range(-10,11))
    # Rank-one affine model: arithmetic compatibility does not ensure isotropy.
    pmat = sp.zeros(D); pmat[0,:] = sp.ones(1,D)
    zero = I-pmat
    rank1_cases=0
    for m in range(13):
        am = I+(m-1)*pmat
        for n in range(13):
            an=I+(n-1)*pmat
            assert am*an == I+(m*n-1)*pmat
            assert am+an-zero == I+(m+n-1)*pmat
            assert am.det()==m
            rank1_cases+=1
    out['rank_one_semiring_pairs'] = rank1_cases
    # Add-one determinant obstruction, rational span and exact CRT fibers.
    successor_cases=0
    for n in range(1,31):
        s = basis(n).inv()*basis(n+1)
        assert abs(s.det()) == sp.Rational(n+1,n)
        if n>1:
            assert not integral(s)
        assert intersect(basis(n),basis(n+1)) == hnf(basis(n*(n+1)))
        successor_cases+=1
    out['successor_refinement_spans'] = successor_cases
    # Two split local templates at the same stage must have their prime identity retained.
    # Results are certificates for the declared construction, not unique native dynamics.
    out['boundaries'] = ['no Foundation admission','no unique selector',
                         'no global equidistribution','no factorization speedup',
                         'no scalar-only or history-free future quotient']
    return out

if __name__ == '__main__':
    result = verify()
    payload = json.dumps(result,indent=2,ensure_ascii=False)+'\n'
    Path(__file__).with_name('results.json').write_text(payload,encoding='utf-8')
    print(payload)
