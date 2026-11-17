"""Exact rational checks for a conditional support-gap robustness theorem.

The original R5 Bellman support identity is a cited input, not recomputed here.
These finite checks verify arithmetic identities and exact branch mass envelopes;
the all-real perturbation inequality follows from the written proof.
"""
from fractions import Fraction as F
from itertools import product

CASES = [
    (F(1, 4), F(1, 8)),
    (F(1, 8), F(1, 4)),
    (F(1, 6), F(1, 3)),
    (F(1, 10), F(1, 5)),
    (F(1, 4), F(1, 4)),
]

for a0, a1 in CASES:
    assert F(0) < a0 < F(1, 2) and F(0) < a1 < F(1, 2)
    s, d = (a0 + a1)/2, abs(a0 - a1)
    c = F(3, 4) + F(1, 2)/s
    # Q at optional stage-2 routes is a_i per route, origin mass 1/2.
    weights = (a0/2, a0/2, a1/2, a1/2)
    m = sum(weights)
    assert m == a0 + a1 == 2*s
    for a in (a0, a1):
        q = (a, 1 - 2*a, a)
        p = (a/2, 1 - 2*a, 3*a/2)
        assert min(q) > 0 and min(p) > 0
        assert sum(q) == sum(p) == 1
    original_gap = d/(4*s)
    assert 2*c == F(3, 2) + 1/s
    assert 2*c*m == 3*s + 2
    assert (d == 0) or (original_gap/(2*c*m) == d/(4*s*(3*s + 2)))
    # Exact envelope over 81 reach combinations and 16 signed error changes.
    eps = F(1, 16)
    maximum = F(0)
    for reach in product((F(0), F(1, 2), F(1)), repeat=4):
        for signs in product((-1, 1), repeat=4):
            change = sum(w * r * sign * eps for w, r, sign in zip(weights, reach, signs))
            assert abs(change) <= m*eps
            maximum = max(maximum, abs(change))
    assert maximum == m*eps
    print(f"alpha0={a0} alpha1={a1} s={s} Qmerger_mass_cap={m} "
          f"baseline_H_gap={original_gap} worst_Qerror_change={maximum}")

a0, a1 = F(1, 4), F(1, 8)
s = (a0 + a1)/2
d = abs(a0 - a1)
c = F(3, 4) + F(1, 2)/s
m = 2*s
assert s == F(3, 16) and c == F(41, 12) and m == F(3, 8)
assert d/(4*s) == F(1, 6)
# Integer support direction J = 12 H = 41 e_Q - 12 T_Q.
assert 12*d/(4*s) == 2
assert 2 * 41 * m == F(123, 4)
threshold_local = d/(4*s*(3*s + 2))
threshold_global = d/(6*s + 4)
assert threshold_local == F(8, 123)
assert threshold_global == F(1, 41)
for eps, gap, dist in [
    (F(1, 16), F(5, 64), F(5, 3392)),
    (F(1, 32), F(133, 128), F(133, 6784)),
]:
    lower = 2 - 2 * 41 * m * eps
    assert lower == gap and lower/53 == dist and lower > 0
    print(f"eps={eps} Jgap_lower={lower} Linfty_distance_lower={lower/53}")
print(f"localized_epsilon_threshold={threshold_local} all_terminal_threshold={threshold_global}")
print("PASS_EXACT_R5_MERGER_Q_ERROR_ROBUSTNESS")
