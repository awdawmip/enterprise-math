"""R600: exact rational companion to the uniform auxiliary-root theorem.
Only formal coefficient and rational inequality checks; no native BRC simulation.
Mathematical proof of all-index and complex-domain claims is in R600_PROOF.zh-CN.md.
"""
from fractions import Fraction as Q
from math import factorial

# For x=1/4, compare exact geometric majorants for cosh(x) and sinh(x).
x = Q(1, 4)
cosh_majorant = 1 + (x*x / 2) / (1 - Q(1, 192))
sinh_majorant = x / (1 - Q(1, 96))
assert cosh_majorant < Q(9, 8)
assert sinh_majorant < Q(3, 10)
assert Q(9, 8) > 0

# For |w|<=2, the ratios of subsequent absolute series terms are <=1/5.
plus_relative_tail = Q(1, 5) / (1 - Q(1, 5))
minus_relative_tail = Q(2, 3) / (1 - Q(1, 5))
assert plus_relative_tail == Q(1, 4) < 1
assert minus_relative_tail == Q(5, 6) < 2

# At a nonzero h_epsilon root with |w|=r>2: |h_epsilon'|>=r/3.
# Squaring is legitimate since both sides of sqrt(r^2-1)>=1+r/3 are positive.
# 9*(r^2-1) - (r+3)^2 = 8r^2-6r-18, increasing for r>=2.
assert 8 * 2**2 - 6 * 2 - 18 > 0
assert 16 * 2 - 6 > 0

# Strict uniform estimates on |u|<=1/4 near any zero in w:
sqrt5_half_majorant = Q(9, 8)  # sqrt(5)/2 <9/8
assert Q(5, 4) < sqrt5_half_majorant**2
sinh_second_derivative_factor = Q(9, 8) + sqrt5_half_majorant * Q(3, 10)
opposite_derivative_factor = sqrt5_half_majorant * Q(9, 8) + Q(3, 10) + Q(1, 2)
assert sinh_second_derivative_factor < 2
assert opposite_derivative_factor < 3
assert Q(1, 3) - Q(1, 4) > 0
assert 2 - 3 * Q(1, 4) > 0

# Formal power-series identity: 3*(sinh(w)^2-w^2)/w^4
#   = sum_{j>=0} 24*4^j*w^(2j)/(2j+4)!.
# The frozen R462 observer has F(z)=sum 24*(-8z)^j/(2j+4)!, w^2=-2z.
for j in range(101):
    reconstructed = 3 * sum(
        (Q(1, factorial(2*n+1)*factorial(2*(j+1-n)+1))
         for n in range(j+2)), Q(0)
    )
    expected = Q(24*4**j, factorial(2*j+4))
    assert reconstructed == expected, (j, reconstructed, expected)

print("R600_RATIONAL_RADIUS2_ROOT_EXCLUSION_PASS")
print("R600_RATIONAL_DERIVATIVE_AND_QUARTER_SPACING_CONSTANTS_PASS")
print("R600_FORMAL_SERIES_IDENTITY_PASS 101 of 101")
print("R600_UNIFORM_AUXILIARY_ROOT_GEOMETRY_COMPANION_PASS")
