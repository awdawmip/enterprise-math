#!/usr/bin/env python3
"""Exact sanity checks for the nonblind R5 single-price support lemma.
Finite enumeration is not the universal proof; see adjacent Markdown note.
"""
from fractions import Fraction as F
from itertools import product


def positive(x):
    return max(F(0), x)


def support_gap(gains, s):
    a, b, c, d = gains
    m = sum(gains, F(0)) / 4
    f_a = (positive(a - s) + positive(b - s)) / 2 - s
    f_b = (positive(c - s) + positive(d - s)) / 2 - s
    return (positive(f_a) + positive(f_b)) / 2 - positive(m - 2*s)


def same_support_ray(gains):
    a, b, c, d = gains
    return (a + b == c + d and
            max(a, b) <= 3 * min(a, b) and
            max(c, d) <= 3 * min(c, d))


values = [F(k, 20) for k in range(7)]
count = 0
for gains in product(values, repeat=4):
    m = sum(gains, F(0)) / 4
    s0 = m / 2
    d0 = support_gap(gains, s0)
    assert (d0 == 0) == same_support_ray(gains), (gains, d0)
    for i in range(17):
        s = F(i, 40)
        gap = support_gap(gains, s)
        assert gap >= 0, (gains, s, gap)
        if same_support_ray(gains):
            assert gap == 0, (gains, s, gap)
    count += 1

Y = (F(1, 10), F(99, 100), F(101, 100), F(19, 10))


def kernel(p):
    return (p, F(1, 2)-p, F(1, 2)-p, p)


def gain(p):
    K = kernel(p)
    assert all(k > 0 for k in K)
    assert sum(K) == 1
    assert sum(k*y for k, y in zip(K, Y)) == 1
    return 1 - sum(k*min(y, F(1)) for k, y in zip(K, Y))


parameters = (F(79, 178), F(11, 178), F(45, 178), F(45, 178))
gains = tuple(gain(p) for p in parameters)
assert gains == (F(2, 5), F(3, 50), F(23, 100), F(23, 100))
s0 = sum(gains, F(0)) / 8
assert s0 == F(23, 200)
assert support_gap(gains, s0) == F(11, 800)
print(f"EXACT_GRID_CERT: {count} gain quadruples, 17 price samples each; no counterexamples")
print("THEOREM_MODE: mathematical proof is in adjacent Markdown; finite grid only sanity")
print("TERMINAL_Y:", Y)
print("KERNEL_PARAMETERS:", parameters)
print("GAINS:", gains)
print("S0:", s0, "LR_MIN:", 1+s0, "FULL_MIN:", 1+s0-support_gap(gains, s0))
print("STRICT_GAP:", support_gap(gains, s0))
