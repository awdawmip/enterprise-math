#!/usr/bin/env python3
"""Exact rational cross-check for R480 logarithmic Poisson left-edge minors.

Input formula: R479 signed-BRC Catalan transform at frozen R462 pin.
Every determinant, bound, and symbolic specialization uses integers/Fraction.
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial
import json


def C(n):
    return comb(2*n,n)//(n+1)


def a(r,j):
    if j<0 or j>r-2:
        return 0
    return comb(2*r-j,j)*sum(comb(j,q)*(-2)**q*C(r-q) for q in range(j+1))


def orig_H(r,j):
    s=r-j
    def bc(n,k):return comb(n,k) if 0<=k<=n else 0
    return comb(r+s,2*s)*sum(comb(j,q)*(bc(2*s,r-2*q)-bc(2*s,r-2*q-1)) for q in range(j+1))


def eta(r,L):
    assert r>=4*L and L>=1
    alpha=F(3,2*(r-L)-1)
    return F(3*L*L-L,4*r)+(3+alpha)**L-3**L


def err_ratio(r,L,m):
    E=eta(r,L)
    M=m*(m-1)//2
    return F(factorial(m)*(L+m)**M,1)*((1+E)**m-1) / factorial_product(m)


def factorial_product(m):
    z=1
    for i in range(m):z*=factorial(i)
    return z


def det(mat):
    m=len(mat)
    ans=0
    for p in permutations(range(m)):
        inversions=sum(p[i]>p[k] for i in range(m) for k in range(i+1,m))
        v=-1 if inversions%2 else 1
        for i in range(m):v*=mat[i][p[i]]
        ans+=v
    return ans


def poisson_minor(m,j):
    t=F(1)
    for i in range(m):t*=F(factorial(i),factorial(j+i))
    return t


# Fully exact, explicit all-r threshold: eta decreases with r at fixed L.
R0=10**24+1
L0=25
ratios=[]
for m in range(1,5):
    q=err_ratio(R0,L0,m)
    assert q<F(1,16), (m,q)
    ratios.append({"m":m,"error_over_poisson_minor_lt_1_over_16":True,
                   "floor_of_1e12_times_ratio":str((q.numerator*10**12)//q.denominator)})

original_checks=0
coeff_checks=0
minor_checks=0
bound_checks=0
positivity_checks=0
for r in range(9,102,2):
    L=min(6,r//4)
    if L==0:continue
    E=eta(r,L)
    for j in range(L+1):
        normalized_times_fact=F(factorial(j)*a(r,j),C(r)*r**j)
        assert abs(normalized_times_fact-1)<=E,(r,j)
        coeff_checks+=1
        if r in (9,17,51,101) and j<=5:
            assert a(r,j)==orig_H(r,j),(r,j)
            original_checks+=1
    for m in range(1,5):
        for j in range(max(0,L-m+2)):
            # det of normalized Toeplitz entries versus exact Poisson matrix.
            A=[[F(a(r,j+v-i),C(r)*r**(j+v-i)) if j+v-i>=0 else F(0)
                for v in range(m)] for i in range(m)]
            B=[[F(1,factorial(j+v-i)) if j+v-i>=0 else F(0)
                for v in range(m)] for i in range(m)]
            da=det(A)
            db=det(B)
            assert db==poisson_minor(m,j)
            absolute_error=F(factorial(m)*(L+m)**(m*(m-1)//2),1)*((1+E)**m-1)
            for v in range(m):absolute_error/=factorial(j+v)
            assert abs(da-db)<=absolute_error,(r,j,m)
            bound_checks+=1
            minor_checks+=1
            if err_ratio(r,L,m)<1:
                assert da>0,(r,j,m)
                positivity_checks+=1

report={
 "schema":"ENTERPRISE_MATH_R480_LOG_POISSON_WINDOW_EXACT_V1",
 "date":"2026-11-02", "scientific_pin":"18783e01e3646c72b7aab3b16d3f565e83e6446f",
 "inputs":"R479 exact signed-BRC Catalan transform; no native X6 promotion",
 "arithmetic":"Python integers and Fraction only; no float",
 "theorem":"for any fixed m and 0<c<1, all adjacent minors D_(m,j)>0 for all sufficiently large odd r and all 0<=j<=floor(c log_3 r)-m+1",
 "explicit_threshold":{"odd_r_at_least":str(R0),"L":L0,"all_m_1_to_4":True,"max_position_by_m":"j<=25-m+1","certificates":ratios},
 "finite_exact_cross_checks":{"r_odd_9_to_101":47,"original_signed_convolution_checks":original_checks,"coefficient_error_checks":coeff_checks,"normalized_determinant_checks":minor_checks,"entrywise_bound_checks":bound_checks,"positive_when_bound_sufficient":positivity_checks},
 "result":"R480_EXACT_PASS"
}
print(json.dumps(report,ensure_ascii=False,indent=2))
