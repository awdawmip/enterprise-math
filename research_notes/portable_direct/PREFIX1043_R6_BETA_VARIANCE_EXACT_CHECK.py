"""PREFIX-1043: exact rational checks for auxiliary Beta positivity cones.

Checks the new implications only. It does not independently establish the
inherited scalar density, critical-point bounds, or native BRC attribution.
"""
from fractions import Fraction as F

U = 611856
EPS = F(1, 10000)
TAIL_CAP = F(1, 100)
DATA = (
    # center, uniform_min_n, delta, local_holder, cap, g_lower, margin,
    # exact-center_pointwise_n, exact-center_j
    (4, 160000000000000, F(1, 10**6), 104400, F(106),
     F(6371, 60), F(13, 75), 126000000000000, 14000000000000),
    (16, 300000000000000000000, F(1, 10**9), 291700, F(10),
     F(919, 90), F(181, 900),
     243000000000000000000, 108000000000000000000),
)


def uniform_q(n, c, a):
    p = F(c, 36)
    b = a / 36
    return F(1296) * (p * (1-p) + b + (p+b)/n) / (n+2) + (a + F(36, n))**2


def exact_q(n, j, c):
    return F(1296 * j * (n-j+1), (n+1)**2 * (n+2)) + (F(36*j, n+1)-c)**2


assert F(U, 2**28) < TAIL_CAP  # p < 2^-29 implies 2Up < U/2^28
for c, n, delta, L, C, lower, margin, n_point, j in DATA:
    a = delta/2
    assert a <= EPS / 2
    assert F(n) * EPS**2 > F(30*2592)
    assert F(18, n) <= a  # at least the nearest-grid ratio in every eligible row
    assert F(L**4) * uniform_q(n, c, a) < C**4
    assert lower - C - TAIL_CAP == margin

    assert n_point >= 8*10**12
    assert F(j, n_point) == F(c,36)
    assert F(L**4)*exact_q(n_point, j, c) < C**4
    assert F(n_point)*EPS**2 > F(30*2592)
    print("CENTER", c, "UNIFORM_MIN_N", n, "MARGIN", margin,
          "POINTWISE_N", n_point, "POINTWISE_M", j-1,
          "POINTWISE_K", n_point-j)

assert F(5*10**14, 160000000000000) == F(25,8)
assert F(5*10**20, 300000000000000000000) == F(5,3)
print("PREFIX1043_EXACT_RATIONAL_IMPLICATIONS_PASSED")
