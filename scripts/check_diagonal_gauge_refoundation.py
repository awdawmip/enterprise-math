#!/usr/bin/env python3
"""Exact-integer regression checker for Diagonal Gauge Refoundation.

This checker validates the algebraic candidate only.  It does NOT promote the
candidate to N0 and does NOT establish a global three-generator native path
language.  Balanced-triad word counts are reported conditionally.
"""

from itertools import product, permutations
from math import comb
import hashlib
import json

BOUND = 8
KERNEL_BOUND = 3
CHART_BOUND = 20
ASSOC_BOUND = 3


def can(z):
    m = min(z)
    return tuple(v - m for v in z)


def diag_equiv(x, y):
    d = tuple(a - b for a, b in zip(x, y))
    return d[0] == d[1] == d[2]


def chart(z):
    a, b, c = z
    return (a - c, b - c)


def decode(rs):
    r, s = rs
    m = min(r, s, 0)
    return (r - m, s - m, -m)


def add(x, y):
    return can(tuple(a + b for a, b in zip(x, y)))


def inv(x):
    return can(tuple(-a for a in x))


def qdir(x):
    y = can(x)
    return sum(v * v for v in y)


def delta(x):
    a, b, c = x
    return a * a + b * b + c * c - a * b - b * c - c * a


def main():
    checks = {}

    # Canonical section and common-diagonal invariance.
    count = 0
    for z in product(range(-BOUND, BOUND + 1), repeat=3):
        cz = can(z)
        assert min(cz) == 0 and all(v >= 0 for v in cz)
        for k in range(-BOUND, BOUND + 1):
            assert can(tuple(v + k for v in z)) == cz
        count += 1
    checks["canonical_section_lifts"] = count

    # can(x)=can(y) iff x-y is a common diagonal shift.
    vals = list(product(range(-KERNEL_BOUND, KERNEL_BOUND + 1), repeat=3))
    count = 0
    for x in vals:
        for y in vals:
            assert (can(x) == can(y)) == diag_equiv(x, y)
            count += 1
    checks["kernel_iff_pairs"] = count

    # The current Stage-2 decoder is exactly the quotient section in Z^2 chart.
    count = 0
    for r in range(-CHART_BOUND, CHART_BOUND + 1):
        for s in range(-CHART_BOUND, CHART_BOUND + 1):
            d = decode((r, s))
            assert min(d) == 0 and all(v >= 0 for v in d)
            assert chart(d) == (r, s)
            assert d == can((r, s, 0))
            count += 1
    checks["stage2_decoder_chart_pairs"] = count

    # Transport the quotient-group law to the min-zero section.
    A = [z for z in product(range(BOUND + 1), repeat=3) if min(z) == 0]
    count = 0
    for x in A:
        assert add(x, (0, 0, 0)) == x
        assert add(x, inv(x)) == (0, 0, 0)
        assert inv(inv(x)) == x
        M = max(x)
        assert inv(x) == tuple(M - v for v in x)
        for y in A:
            assert add(x, y) == add(y, x)
            cx, cy = chart(x), chart(y)
            assert chart(add(x, y)) == (cx[0] + cy[0], cx[1] + cy[1])
            raw = tuple(a + b for a, b in zip(x, y))
            m = min(raw)
            assert add(x, y) == tuple(v - m for v in raw)
            count += 1
    checks["group_pair_laws"] = count

    Aassoc = [
        z for z in product(range(ASSOC_BOUND + 1), repeat=3) if min(z) == 0
    ]
    count = 0
    for x in Aassoc:
        for y in Aassoc:
            for z in Aassoc:
                assert add(add(x, y), z) == add(x, add(y, z))
                count += 1
    checks["associativity_triples"] = count

    # Exact integer certificate underlying the current directed-gauge triangle law.
    count = 0
    for x in A:
        qx = qdir(x)
        for y in A:
            qy = qdir(y)
            raw = tuple(a + b for a, b in zip(x, y))
            c = add(x, y)
            assert all(ci <= ri for ci, ri in zip(c, raw))
            assert qdir(c) <= sum(v * v for v in raw)
            dot = sum(a * b for a, b in zip(x, y))
            assert dot * dot <= qx * qy
            count += 1
    checks["directed_gauge_triangle_cert_pairs"] = count

    # S3/cyclic covariance and the historical quadratic form's gauge invariance.
    count = 0
    for x in A:
        for p in permutations(range(3)):
            px = tuple(x[i] for i in p)
            assert can(px) == px
            assert qdir(px) == qdir(x)
            assert delta(px) == delta(x)
            assert inv(px) == tuple(inv(x)[i] for i in p)
            count += 1
    checks["S3_covariance_cases"] = count

    count = 0
    for z in vals:
        for k in range(-10, 11):
            assert delta(tuple(v + k for v in z)) == delta(z)
            count += 1
    checks["Delta_diagonal_invariance_cases"] = count

    # Quadratic metric fork.  Any S3-invariant quadratic has form
    # alpha*sum(x_i^2)+beta*sum_{i<j}x_ix_j.  Diagonal-gauge invariance forces
    # alpha+beta=0; unit-axis calibration forces alpha=1, hence Delta uniquely.
    alpha, beta = 1, -1
    assert alpha + beta == 0
    e1, e2, e3 = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    assert delta(e1) == 1
    assert delta(add(e1, e2)) == 1
    assert qdir(e1) == 1
    assert qdir(add(e1, e2)) == 2
    checks["quadratic_metric_fork_symbolic_conditions"] = 4

    # Frozen Stage-2 examples and the displacement-only balanced triad relation.
    assert inv((1, 0, 0)) == (0, 1, 1)
    assert qdir((1, 0, 0)) == 1 and qdir(inv((1, 0, 0))) == 2
    assert inv((3, 4, 0)) == (1, 0, 4)
    assert qdir((3, 4, 0)) == 25 and qdir(inv((3, 4, 0))) == 17
    assert add(e1, e2) == inv(e3)
    assert add(add(e1, e2), e3) == (0, 0, 0)
    assert can((1, 1, 1)) == (0, 0, 0)
    checks["current_examples_and_triad_displacement"] = 9

    # Conditional word counts only.  These do not assert that a global native
    # three-generator trace language is frozen.
    balanced = {
        str(m): comb(3 * m, m) * comb(2 * m, m) for m in range(1, 11)
    }
    checks["conditional_balanced_word_count_levels"] = len(balanced)

    payload = {
        "status": "PASS",
        "bounds": {
            "BOUND": BOUND,
            "KERNEL_BOUND": KERNEL_BOUND,
            "CHART_BOUND": CHART_BOUND,
            "ASSOC_BOUND": ASSOC_BOUND,
        },
        "checks": checks,
        "conditional_balanced_word_counts": balanced,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["report_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
