#!/usr/bin/env python3
"""GH-122: marked CM Hasse covariance and R non-homogeneity, exact F_3347^2."""
from d25_gh121_marked_cm_fiber_exact import (
    p, P, T, rows, evaluate, mul, power, div, C
)

H0 = evaluate(P, T)
assert H0 == C(783)
assert p == 3347
out = []
for i, (alpha, c2, lam, Tp, zp, Rp) in enumerate(rows):
    H = evaluate(P, Tp)
    w = power(lam, p-1)
    assert H != C(0)
    assert mul(H, w) == H0  # Ha_new=lambda^(-(p-1))*Ha_old.
    ratio = div(Rp, power(H, 2))
    assert ratio != C(0)
    out.append((i,H,w,ratio))

assert out == [
    (0,(841,1147),(249,1905),(1346,1788)),
    (1,(49,1370),(902,259),(3227,128))
]
print('PASS_GH122_HASSE_COVARIANCE_AND_TAIL_NONHOMOGENEITY')
print('original Ha_p(T) =', H0, '; original R_p(9) =', C(0))
for i,H,w,ratio in out:
    print('alternate',i,'Ha',H,'lambda^(p-1)',w,'R/Ha^2',ratio)
print('CHECKED: H_new * lambda^(p-1) == H_original for both true isomorphisms')
print('OBSERVED: R is not any homogeneous nonzero-weight tensor under these marked changes')
