#!/usr/bin/env python3
"""R602 exact rational certificate for a first dyadic moving-window pair.
All load-bearing comparisons are integer/Fraction operations.  No roots or
native BRC trajectories are numerically simulated.
"""
from fractions import Fraction as Q
from math import factorial

k = 1 << 42
L = 64
X = Q(113, 8)  # R+1/8 with R=14; 8X=113.
assert k >= 2 * L

# Analytic log(2) interval from log 2 = 2*sum 3^(-(2m+1))/(2m+1).
log2_lower = Q(56, 81)
log2_upper = Q(25, 36)
assert (42 * log2_lower) ** 2 > 64 * 13
assert (42 * log2_upper) ** 2 < 64 * 14
assert (41 * log2_upper) ** 2 < 64 * 13

# Uniform low-degree coefficient-ratio bound from the exact R590 product.
S = Q(3 * L, 2 * k) + Q(L * (L + 1) * (L + 5), 12 * k * k)
B = Q(3 * (L + 1), 2 * (2 * k - L))
E = S + B
assert 0 < E < 1
assert 6 * k > L * (L + 3)  # p_h>1 for h<=L
low = 24 * 3**11 * E / (1 - E)  # sqrt(113)<11, exp(11)<3**11.

# All-degree bound a_(k,j) < 21(k+1)(2k+1)a_j and exact factorial tail.
assert Q(113, 132 * 131) < Q(1, 100)
tail = 24 * (1 + 21 * (k + 1) * (2 * k + 1)) * Q(100, 99) * Q(113**65, factorial(130))
U = low + tail
assert U < Q(1, 6720)
assert U < Q(1, 48 * 56)  # 14^(3/2) < 56.
assert 336 * U < Q(1, 20)  # delta = 6*14^(3/2)*U <336 U.

# Ancillary exact identities from the declared auxiliary entire function.
for j in range(65):
    a = Q(24 * 8**j, factorial(2*j+4))
    assert a <= Q(24 * 8**j, factorial(2*j))

print('R602_INPUT k=2^42 L=64 R=14 X=113/8 c=1/64')
print('R602_LOG_WINDOW_CERTIFICATE_PASS: 13 < c(log k)^2 < 14; dyadic 2^41 below 13')
print('R602_EXACT_LOW_BOUND_PASS', 'E<1', 'low<1/6720')
print('R602_EXACT_TAIL_BOUND_PASS', 'tail<1/6720')
print('R602_TOTAL_ERROR_STRICTLY_LT_1_OVER_6720_PASS')
print('R602_MATCHING_DISPLACEMENT_STRICTLY_LT_1_OVER_20_PASS')
print('R602_ALL_EXACT_CERTIFICATES_PASS')
