"""Exact checks of selected elementary kernels; not a proof of paper main theorems."""
import json
from fractions import Fraction
from math import comb
from pathlib import Path
import sympy as sp


def shift_transpose(p):
    n = len(p)
    return [[p[j][i] - p[i][j] + (p[i-1][j] if i else 0)
             for j in range(n)] for i in range(n)]


def preimage(z, phi):
    ell = len(z) - 1
    p = [[0] * (ell + 1) for _ in range(ell + 1)]
    for m in range(2 * ell + 1):
        low, high = max(0, m - ell), min(ell, m)
        def rhs(a):
            b = m - a
            d = z[b-1][a+1] - (p[b-2][a+1] if b >= 2 else 0)
            return z[a+1][b] + z[b][a+1] + d
        if m % 2:
            k = (m + 1) // 2
            anchor = k - 1
            p[anchor][m-anchor] = z[k][k]
        elif m < ell:
            anchor = m
            p[m][0] = z[m+1][0] + z[0][m+1]
        else:
            anchor = m // 2
            p[anchor][anchor] = phi[anchor]
        for a in range(anchor-1, low-1, -1):
            p[a][m-a] = rhs(a) - p[a+1][m-a-1]
        for a in range(anchor+1, high+1):
            p[a][m-a] = rhs(a-1) - p[a-1][m-a+1]
    return p


def matrix_units(n):
    for a in range(n):
        for b in range(n):
            p = [[0] * n for _ in range(n)]
            p[a][b] = 1
            yield p


def flatten(p):
    return [v for row in p for v in row]


def checks():
    results = []
    for ell in range(2, 7):
        n = ell + 1
        positions = {(2*r, 0) for r in range(ell//2 + 1)}
        basis = list(matrix_units(n))
        for z in basis:
            p = preimage(z, [0]*n)
            tp = shift_transpose(p)
            assert all(tp[i][j] == z[i][j] for i in range(n) for j in range(n)
                       if (i, j) not in positions)
        for a in basis:
            phi = [a[i][i] if i >= (ell+1)//2 else 0 for i in range(n)]
            assert preimage(shift_transpose(a), phi) == a
        r2 = [0, 1] + list(range(2, n))
        for r in range(1, ell//2 + 1):
            coeffs = []
            for j in range(n):
                z = [[r2[i] if c == j else 0 for c in range(n)] for i in range(n)]
                tp = shift_transpose(preimage(z, [0]*n))
                coeffs.append(tp[2*r][0] - z[2*r][0])
            assert coeffs[2*r-1] == 1
            assert all(v == 0 for v in coeffs[2*r:])
        lin = sp.Matrix.hstack(*[sp.Matrix(flatten(shift_transpose(a))) for a in basis])
        rank = lin.rank()
        results.append({'ell':ell,'domain_dimension':n*n,'rank':rank,
                        'kernel_dimension':n*n-rank,'full_linear_basis_checks':len(basis),
                        'residual_coordinates':sorted(positions)})
    for ell in range(0, 9):
        for k in range(0, 20):
            b = [comb(k+ell-r, ell-r) for r in range(ell+1)]
            bp = [comb(k+1+ell-r, ell-r) for r in range(ell+1)]
            assert bp == [sum(b[r:]) for r in range(ell+1)]
        for lo in range(0, 6):
            for hi in range(lo, 12):
                total = [sum(comb(j+ell-r, ell-r) for j in range(lo,hi)) for r in range(ell+1)]
                delta = [comb(hi+ell+1-r, ell+1-r)-comb(lo+ell+1-r,ell+1-r)
                         for r in range(ell+2)]
                assert total == [delta[r]-delta[r+1] for r in range(ell+1)]
    return {'source_revision':'4a7bc8ab0bc7','scope':'FP Lemmas 7, 9, 13, 15, 16; exact finite checks',
            'status':'PASS','shift_transpose':results,
            'binomial_checks':{'ell':'0..8','unit_shift_k':'0..19','summation_lo':'0..5','summation_hi':'lo..11'}}


if __name__ == '__main__':
    result = checks()
    out = Path(__file__).with_name('check_learning_kernels.json')
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))
