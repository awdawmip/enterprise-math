"""Exact rational quadrature for the two- and three-reading Haar tail constants."""
from fractions import Fraction as F


def integrate_polynomial(coefficients, lo, hi):
    return sum(F(a, k+1) * (hi**(k+1)-lo**(k+1))
               for k,a in enumerate(coefficients))


half=F(1,2)
# After integrating s, the quadrant r,s >= 0 is split at s=r and r=1/2.
# In the first interval combine s in [0,r] and [r,1-r].
first=[F(1,3),F(-1,3),F(-2),F(4),F(-2)]
second=[F(2,3),F(-8,3),F(4),F(-8,3),F(2,3)]
i3=4*(integrate_polynomial(first,F(0),half)
      +integrate_polynomial(second,half,F(1)))
assert i3==F(23,60)
# Integral of the union of two opposite primitive-direction collision boxes.
b2=F(7,4)
b3=F(7,4)*i3
assert b3==F(161,240)
# Divide by two for signed primitive directions, then use zeta(2)=pi^2/6.
assert b2*3==F(21,4)
assert b3*3==F(161,80)
print('I_3 =',i3)
print('F_2(a) = 1 - (21/4)/(pi^2*a), a >= 1')
print('F_3(a) = 1 - (161/80)/(pi^2*a), a >= 1/2')
endpoint_coefficient=F(21,8)
triple_coefficient=F(161,80)
assert endpoint_coefficient-triple_coefficient==F(49,80)
assert triple_coefficient/endpoint_coefficient==F(23,30)
assert 1-triple_coefficient/endpoint_coefficient==F(7,30)
print('With the same outer endpoints, collision probability is reduced by 7/30.')
