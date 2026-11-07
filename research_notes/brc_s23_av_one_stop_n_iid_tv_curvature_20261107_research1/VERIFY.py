"""Exact certificate: one AV stop cannot reconstruct n fresh binary trials."""
from fractions import Fraction as F
from math import comb

Z0, Z1, Z2 = F(1, 4), F(11, 32), F(7, 16)


def d(n, r):
    def bern(z):
        return z**r * (1-z)**(n-r)
    return bern(Z0) - 2*bern(Z1) + bern(Z2)


def bound(n):
    vals = [d(n, r) for r in range(n+1)]
    assert sum(comb(n, r)*vals[r] for r in range(n+1)) == 0
    return sum(comb(n, r)*abs(vals[r]) for r in range(n+1)) / 8


assert Z1 * 2 == F(11, 16)
assert Z1 * 2 == (Z0*2 + Z2*2)/2
assert [d(3, r) for r in range(4)] == [F(567, 16384), F(-279, 16384), F(-9, 16384), F(297, 16384)]
assert bound(2) == F(9, 1024)
assert bound(3) == F(27, 2048)
assert bound(3) > F(3, 16384)
assert bound(1) == 0
assert all(bound(n) <= bound(n+1) for n in range(1, 20))
for n in (2,3,10,100,500,1000):
    b=bound(n)
    print(f"n={n} lower={b if n<=3 else '(exact fraction computed)'} approx={float(b):.12f}")
print('PASS_S23_ONE_STOP_TO_N_IID_TV_SECOND_DIFFERENCE_20261107')
