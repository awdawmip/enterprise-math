#!/usr/bin/env python3
"""R601 exact rational companion checks for the uniform local Rouche lemma.
Proof of the infinite-zero statement is in R601_PROOF.zh-CN.md.
All assertions here use exact integers/Fraction, with no floating-point test.
"""
from fractions import Fraction as Q
from math import factorial, isqrt

assert Q(9,10) * Q(16,17)**4 > Q(2,3)
assert Q(32,33) > Q(9,10)
assert 3*3 > 2*2*2
assert Q(1,8) * 2 == Q(1,4)
assert Q(1,3) - Q(1,8) == Q(5,24) > Q(1,5)
assert 2 - 3*Q(1,8) == Q(13,8) > Q(3,2)
assert Q(1,8) <= Q(2,16)
assert Q(1,8) <= Q(2,16)
assert Q(2,3) * Q(9,10) == Q(3,5)

# F(z) = 3(sinh(w)^2-w^2)/w^4; w^2=-2z.
# cosh(2w)-1 = 2sinh(w)^2.
for j in range(121):
    direct = Q(24 * (-8)**j, factorial(2*j+4))
    from_cosh = Q(3 * 2**(2*j+3) * (-2)**j, factorial(2*j+4))
    assert direct == from_cosh, (j, direct, from_cosh)

for R, eps in [(4,Q(1,10000)), (9,Q(1,100000)), (16,Q(1,1000000)),
               (25,Q(1,10000000)), (100,Q(1,100000000))]:
    R32 = Q(R * isqrt(R))
    assert R32*R32 == R**3
    delta = 6 * R32 * eps
    assert Q(0) < delta <= Q(1,8)
    assert delta/(5*R32) > eps
    print(f'R={R}, eps={eps}, delta={delta}: STRICT_ROUCHE_BOUND_PASS')
print('R601_EXACT_CONSTANTS_AND_121_COEFFICIENTS_PASS')
