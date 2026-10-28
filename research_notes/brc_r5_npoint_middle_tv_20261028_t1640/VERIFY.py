#!/usr/bin/env python3
"""Exact rational checks for R5 n-point successor likelihood-ratio TV theorem.

Pure finite regression tests; the all-real statement is proved in RESEARCH.md.
"""
from fractions import Fraction as F
from itertools import combinations


def tv(a, b):
    return sum((abs(x - y) for x, y in zip(a, b)), F(0)) / 2


def mean(s, q):
    return sum((x * y for x, y in zip(s, q)), F(0))


def compositions_pos(n, total):
    for cuts in combinations(range(1, total), n - 1):
        vals = (0,) + cuts + (total,)
        yield tuple(F(vals[i + 1] - vals[i], total) for i in range(n))


def verify_pairs(s, denominator):
    n = len(s)
    groups = {}
    for q in compositions_pos(n, denominator):
        r = mean(s, q)
        groups.setdefault(r, []).append(q)
    pair_count = 0
    for r, kernels in groups.items():
        for q1, q2 in combinations(kernels, 2):
            d_q = tv(q1, q2)
            assert d_q > 0
            p1 = tuple(s[i] * q1[i] / r for i in range(n))
            p2 = tuple(s[i] * q2[i] / r for i in range(n))
            assert sum(p1) == sum(p2) == 1
            d_p = tv(p1, p2)
            v = tuple(q1[i] - q2[i] for i in range(n))
            assert sum(v) == mean(s, v) == 0
            m = sum((s[i] * abs(v[i]) for i in range(n)), F(0)) / sum(map(abs, v))
            assert d_p / d_q == m / r
            assert s[1] <= m <= s[-2]
            pair_count += 1
    return len(groups), pair_count


def exact_family():
    s = (F(1, 2), F(1), F(2), F(3))
    r = F(3, 2)
    base = (F(1, 4), F(1, 4), F(3, 8), F(1, 8))
    eps = F(1, 100)
    # Unit-TV zero-mass and zero-first-moment circuits: {s1,s2,s4}, {s1,s3,s4}.
    u_lo = (F(4, 5), -F(1), F(0), F(1, 5))
    u_hi = (F(2, 5), F(0), -F(1), F(3, 5))
    assert mean(s, base) == r
    for u in (u_lo, u_hi):
        assert sum(u) == mean(s, u) == 0
        assert sum(map(abs, u)) / 2 == 1
    for theta in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
        u = tuple((1 - theta) * u_lo[i] + theta * u_hi[i] for i in range(4))
        qa = tuple(base[i] + eps * u[i] for i in range(4))
        qb = tuple(base[i] - eps * u[i] for i in range(4))
        pa = tuple(s[i] * qa[i] / r for i in range(4))
        pb = tuple(s[i] * qb[i] / r for i in range(4))
        assert all(z > 0 for z in qa + qb + pa + pb)
        assert sum(qa) == sum(qb) == sum(pa) == sum(pb) == 1
        assert mean(s, qa) == mean(s, qb) == r
        dq = tv(qa, qb)
        dp = tv(pa, pb)
        target_m = (1 - theta) * s[1] + theta * s[-2]
        assert dq == F(1, 50)
        assert dp == dq * target_m / r
        print(f"theta={theta}; TV_Q={dq}; TV_P={dp}; ratio={dp / dq}; common_signed_mean={target_m}")


def main():
    exact_family()
    total = 0
    for s, denominator in (
        ((F(1, 2), F(1), F(2), F(3)), 14),
        ((F(1, 3), F(2, 3), F(1), F(2), F(4)), 11),
        ((F(1, 4), F(1, 2), F(1), F(3, 2), F(5, 2), F(4)), 12),
    ):
        groups, pairs = verify_pairs(s, denominator)
        total += pairs
        print(f"n={len(s)} denominator={denominator} distinct_r={groups} tested_distinct_kernel_pairs={pairs}")
    assert total >= 100
    print(f"TOTAL_EXACT_PAIRS={total}")
    print("ALL EXACT N-POINT TV MIDDLE-RATIO CHECKS PASSED")


if __name__ == "__main__":
    main()
