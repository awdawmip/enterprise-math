#!/usr/bin/env python3
"""R448: exact arithmetic spot-checks of the analytic fifth-root PF3 window theorem.

The universal theorem is proved by inequalities in R448_PROOF.zh-CN.md.
These computations check identities and sampled instances only, not infinitely many r.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import json

def fall(x, n):
    p = 1
    for k in range(n):
        p *= x-k
    return p

def rho(r, h):
    """Exact signed BRC H(r,r-h)/C_r for r>=2h+2."""
    if h < 0: return Q(0)
    total = sum((Q(comb(h, q) * fall(r, 2*q) * fall(r, 2*h-2*q)
                   * (4*q-2*h+1), r-2*h+2*q+1)
                 for q in range(h+1)), Q(0))
    return Q((r+1)*fall(2*r-h, h), factorial(h)*fall(2*r, 2*h)) * total

def original_h(r, h):
    """Independent direct signed binomial convolution."""
    s = r-h
    def c(n, k): return comb(n, k) if 0 <= k <= n else 0
    return c(r+s, 2*s)*sum(c(h, q)*(c(2*s, r-2*q)-c(2*s, r-2*q-1))
                            for q in range(h+1))

def F(r, h, q):
    assert h >= 1 and 0 <= q <= h and r >= 8*h*h
    return (Q(r+1, r-2*h+2*q+1)
            * Q(fall(2*r-h, h), (2*r)**h)
            * Q(fall(r, 2*q)*fall(r, 2*h-2*q), r**(2*h))
            * Q((2*r)**(2*h), fall(2*r, 2*h)))

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def det3(A):
    a,b,c=A
    return a[0]*b[1]*c[2]+a[1]*b[2]*c[0]+a[2]*b[0]*c[1] \
        -a[2]*b[1]*c[0]-a[1]*b[0]*c[2]-a[0]*b[2]*c[1]

def scaled_det(r, columns, ratios):
    m = len(columns)
    A = [[Q(factorial(j), r**(j-i))*ratios[j-i] if j>=i else Q(0)
          for j in columns] for i in range(m)]
    if m == 1: return A[0][0]
    if m == 2: return det2(A)
    return det3(A)

def main():
    original_checks=[]
    for r, maxh in [(9,3),(17,7),(99,8),(343,8)]:
        catalan=comb(2*r,r)//(r+1)
        for h in range(maxh+1):
            assert r >= 2*h+2
            assert Q(original_h(r,h),catalan)==rho(r,h),(r,h)
            original_checks.append((r,h))
    summary_rows=[]
    total_minor_checks=0
    total_F_checks=0
    total_adjacent_checks=0
    for L in range(1,9):
        r=652*L**5+1
        assert r>=8*L*L
        ratios=[rho(r,h) for h in range(L+1)]
        for h in range(1,L+1):
            f=[F(r,h,q) for q in range(h+1)]
            E=sum((Q(comb(h,q),2**h)*(4*q-2*h+1)*f[q]
                   for q in range(h+1)),Q(0))
            assert E==ratios[h]*factorial(h)/r**h
            assert abs(E-1)<=Q(31*h*h,r)
            for q in range(h+1):
                assert abs(f[q]-1)<=Q(7*h*h,r)
                total_F_checks+=1
            for q in range(h):
                ratio=Q((r-2*q)*(r-2*q-1),
                         (r-2*h+2*q+2)*(r-2*h+2*q+3))
                assert f[q+1] == f[q]*ratio
                assert abs(f[q+1]-f[q]) <= Q(24*h,r)
                total_adjacent_checks+=1
        counts={}
        for m in range(1,min(3,L+1)+1):
            count=0
            for cols in combinations(range(L+1),m):
                D=scaled_det(r,cols,ratios)
                V=1
                for i in range(m):
                    for j in range(i+1,m):
                        V*=cols[j]-cols[i]
                assert D>0,(L,m,cols,D)
                eps=Q(31*L*L,r)
                bound={1:eps,2:6*L*eps,3:42*(L**3)*eps}[m]
                assert abs(D-V)<=bound,(L,m,cols,D,V,bound)
                assert bound<({1:1,2:1,3:2}[m])
                count+=1
            counts[str(m)]=count
            total_minor_checks+=count
        summary_rows.append({'L':L,'odd_r':r,'orders':counts})
    evidence={
      'schema':'R448_SIGNED_BRC_GROWING_PF3_WINDOW_AUTHOR_CHECKS_V1',
      'theorem':'for every integer L>=1 and odd r>=652 L^5: all contiguous-row order<=3 Toeplitz minors with columns in [0,L] are strictly positive',
      'analytic_bounds':{
          'F_deviation':'abs(F_hq-1)<=7 h^2/r for r>=8h^2',
          'F_adjacent':'abs(F_(q+1)-F_q)<=24 h/r',
          'signed_binomial_stein':'abs(h! rho_h/r^h-1)<=31 h^2/r',
          'matrix_error_m1':'<=31 L^2/r',
          'matrix_error_m2':'<=186 L^3/r',
          'matrix_error_m3':'<=1302 L^5/r',
          'Vandermonde_lower_m3':'2',
          'theorem_threshold':'r>=652 L^5 (m3 error<2; m2 error<1; m1 error<1)'
      },
      'original_signed_convolution_checks':len(original_checks),
      'original_test_pairs':[list(p) for p in original_checks],
      'exact_F_checks':total_F_checks,
      'exact_adjacent_ratio_checks':total_adjacent_checks,
      'exact_sample_minor_checks':total_minor_checks,
      'sample_summary':summary_rows,
      'math_status':'AUTHOR_SIDE_ANALYTIC_PROOF; COMPUTATIONAL_SPOT_CHECKS; UNREVIEWED; NOT_ADMITTED',
      'limitations':['does not prove whole half-infinite PF3','does not reach proportional j/r windows',
                     'test samples are not a substitute for the analytic proof','no native X6 or physical-model transfer'],
    }
    outfile=Path(__file__).with_name('R448_EVIDENCE.json')
    outfile.write_text(json.dumps(evidence,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('R448_PASS '+json.dumps({k:evidence[k] for k in ('original_signed_convolution_checks','exact_F_checks','exact_adjacent_ratio_checks','exact_sample_minor_checks','sample_summary')},ensure_ascii=False))

if __name__=='__main__': main()
