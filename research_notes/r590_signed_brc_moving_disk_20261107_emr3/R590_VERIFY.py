"""Exact author-side checks for the R590 auxiliary moving-disk coefficient theorem.
No native BRC trajectory calculation or spectral admission is claimed.
"""
from fractions import Fraction
from math import comb, factorial, ceil, log

def catalan(n):
    return comb(2*n, n) // (n + 1)

def H_raw(k, s):
    return comb(2*k+1+s, 2*s) * sum(
        comb(s-1, 2*q) * 4**q * catalan(k-q)
        for q in range(min(k, (s-1)//2)+1)
    )

def relative_factor_factored(k, j):
    P = Fraction(1)
    for h in range(1, j+1):
        P *= Fraction(2*k+h+3, 2*k)*Fraction(2*k-h, 2*k)
    weighted = Fraction(0)
    for q in range((j+1)//2 + 1):
        weighted += comb(j+1, 2*q)*Fraction(4**q*catalan(k-q), catalan(k))
    return P * weighted/Fraction(2**j)

def relative_factor_raw(k, j):
    H2 = H_raw(k,2)
    A = Fraction(H_raw(k,j+2),H2)
    return A * Fraction(factorial(2*j+4), 24*8**j*k**(2*j))

all_count=0
for k in range(2,47):
    for j in range(2*k):
        got = relative_factor_factored(k,j)
        assert got == relative_factor_raw(k,j), (k,j)
        assert got > 0
        all_count += 1
print('R590_EXACT_FACTORIZATION_PASS',all_count,'pairs k=2..46 all degrees')

upper_count=0
for k in range(2,47):
    for j in range(2*k):
        value = relative_factor_factored(k,j)
        assert value <= 21*(k+1)*(2*k+1), (k,j)
        upper_count += 1
print('R590_GLOBAL_COEFFICIENT_ENVELOPE_PASS',upper_count,'pairs')

low_count=0
for k in [256,512,1024,2048]:
    L=ceil(10*log(k))
    assert L <= k//4
    S = Fraction(3*L, 2*k) + Fraction(L*(L+1)*(L+5), 12*k*k)
    B = Fraction(3*(L+1), 2*(k-1))
    E = S+B
    assert E < 1
    rational_upper = E/(1-E)
    for j in range(L+1):
        value=relative_factor_factored(k,j)
        assert abs(value-1) <= rational_upper, (k,j)
        low_count+=1
print('R590_LOW_DEGREE_EXACT_BOUND_PASS',low_count,'pairs k=256..2048')
print('R590_MOVING_DISK_COEFFICIENT_CERTIFICATE_PASS')
