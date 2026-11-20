"""Exact finite checks for Euler RR-11 joint clocks, shared kernel and finite-horizon bounds.
Standard-library Python 3.10+; model-level checks, not native BRC execution or independent replication.
"""
from fractions import Fraction as Q
from itertools import product

tests = 0
for vec in product((-1, 0, 1), repeat=8):
    for n in range(6):
        y3 = sum(map(Q, vec[n:n+3])) / 3
        y2 = sum(map(Q, vec[n+1:n+3])) / 2
        assert 3 * y3 - 2 * y2 == vec[n]
        tests += 1
assert tests == 39366

kernels = [
    ([Q(1, 3)] * 3, [Q(1, 2)] * 2),
    ([Q(1, 2), Q(1, 4), Q(1, 4)], [Q(2, 3), Q(1, 3)]),
    ([Q(0), Q(1, 3), Q(1, 3), Q(1, 3)], [Q(0), Q(1, 2), Q(1, 2)]),
]
residuals = []
for a, b in kernels:
    r = [3 * (a[k] if k < len(a) else 0)
         - 2 * (b[k-1] if 0 <= k-1 < len(b) else 0)
         - (1 if k == 0 else 0)
         for k in range(max(len(a), len(b)+1))]
    v = [1 if c > 0 else (-1 if c < 0 else 0) for c in r]
    err = 3 * sum(a[d] * v[d] for d in range(len(a))) \
        - 2 * sum(b[d] * v[1+d] for d in range(len(b))) - v[0]
    assert err == sum(abs(c) for c in r)
    residuals.append(err)
assert residuals == [Q(0), Q(7, 6), Q(2)]

omega = [(Q(1), Q(0)), (Q(0), Q(1)), (Q(-1), Q(-1))]
independent = [Q(0), Q(0)]
conditional = [Q(0), Q(0)]
distance = Q(0)
for j, d in product(range(3), repeat=2):
    phase = omega[(j-d) % 3]
    p, q = Q(1, 9), Q(1, 3) if j == d else Q(0)
    independent = [independent[k] + p * phase[k] for k in range(2)]
    conditional = [conditional[k] + q * phase[k] for k in range(2)]
    distance += abs(p-q)
assert independent == [0, 0] and conditional == [1, 0]
assert distance == Q(4, 3)

flip = Q(1, 20)
for n in range(60):
    actual = (1-2*flip)**n
    assert abs(1 - actual) <= 2*flip*n

print({"ternary_window_cases":tests,
       "kernel_sharp_bounds":[str(x) for x in residuals],
       "clock_joint_l1":str(distance),
       "markov_horizon_checks":60})
