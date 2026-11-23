"""PREFIX-1042: exact rational arithmetic checks for the conditional Beta cone proof.

This checker verifies only algebraic implications and inequality constants.
It does not run native BRC, Bessel integration or a classical reference model.
"""
from fractions import Fraction as F

U = 611856
EPS = F(1, 10000)
DATA = (
    (4, 5 * 10**14, F(1, 10**6), F(1, 2 * 10**6),
     104400, F(102), F(6371, 60), F(49, 12)),
    (16, 5 * 10**20, F(1, 10**9), F(1, 2 * 10**9),
     291700, F(9), F(919, 90), F(10, 9)),
)

assert F(U, 2**28) < F(1, 10)
for center, n, delta, a, holder, cap, lower_at_center, conclusion in DATA:
    assert a == 36 * delta / 72  # same ratio cone as PREFIX-1041
    assert a <= EPS / 2
    assert F(n) * EPS**2 > 30 * 2592  # Hoeffding exponent
    assert F(18, n) <= a  # every eligible n has nearest integer j
    q = F(324, n) + (a + F(36, n))**2
    assert F(holder**4) * q < cap**4
    assert lower_at_center - cap - F(1, 10) == conclusion
    n_old = 9 * (F(72) / delta)**2
    assert n_old / n == F(11664, 125)
    print("CENTER", center, "MIN_N", n, "D_LOWER", str(conclusion),
          "ORDER_REDUCTION", str(n_old / n))
print("PREFIX1042_EXACT_RATIONAL_IMPLICATIONS_PASSED")
