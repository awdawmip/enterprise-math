#!/usr/bin/env python3
"""Independent exact-integer certificate for RS-DIAGONAL-GAUGE-REFOUNDATION-INDEPENDENT-REVIEW.

This checker independently validates the algebraic core of the frozen candidate.
It deliberately does not assert a total endpoint-displacement functor on bare
PF PATH objects, because PF PATH endpoints are packet/cell states while the
frozen R061 Stage-2 displacement decoder is typed on integer coordinate
vertices / line endpoints.
"""

from itertools import product, permutations
import hashlib
import json

LIFT_BOUND = 4
SHIFT_BOUND = 5
CHART_BOUND = 30
CANONICAL_BOUND = 6
ASSOC_BOUND = 3


def can(z):
    m = min(z)
    return tuple(v - m for v in z)


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
    return sum(v * v for v in can(x))


def delta(x):
    a, b, c = x
    return a * a + b * b + c * c - a * b - b * c - c * a


def main():
    checks = {}

    lifts = list(product(range(-LIFT_BOUND, LIFT_BOUND + 1), repeat=3))

    count = 0
    for z in lifts:
        cz = can(z)
        assert min(cz) == 0
        assert all(v >= 0 for v in cz)
        assert can(cz) == cz
        for k in range(-SHIFT_BOUND, SHIFT_BOUND + 1):
            assert can(tuple(v + k for v in z)) == cz
            count += 1
    checks["canonical_section_and_shift_invariance"] = count

    count = 0
    for x in lifts:
        for y in lifts:
            d = tuple(a - b for a, b in zip(x, y))
            diag_equiv = d[0] == d[1] == d[2]
            assert (can(x) == can(y)) == diag_equiv
            count += 1
    checks["kernel_iff_pairs"] = count

    count = 0
    for r in range(-CHART_BOUND, CHART_BOUND + 1):
        for s in range(-CHART_BOUND, CHART_BOUND + 1):
            d = decode((r, s))
            assert d == can((r, s, 0))
            assert chart(d) == (r, s)
            count += 1
    checks["stage2_decoder_chart_pairs"] = count

    A = [
        z
        for z in product(range(CANONICAL_BOUND + 1), repeat=3)
        if min(z) == 0
    ]
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
        z
        for z in product(range(ASSOC_BOUND + 1), repeat=3)
        if min(z) == 0
    ]
    count = 0
    for x in Aassoc:
        for y in Aassoc:
            for z in Aassoc:
                assert add(add(x, y), z) == add(x, add(y, z))
                count += 1
    checks["associativity_triples"] = count

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
    checks["directed_gauge_triangle_integer_certificate_pairs"] = count

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
    for z in lifts:
        for k in range(-10, 11):
            assert delta(tuple(v + k for v in z)) == delta(z)
            count += 1
    checks["Delta_diagonal_invariance_cases"] = count

    # Symbolic coefficient conditions for an S3-invariant homogeneous quadratic:
    # Q = alpha * sum x_i^2 + beta * sum_{i<j} x_i x_j.
    # Diagonal-shift invariance forces alpha + beta = 0.
    # Unit-axis calibration forces alpha = 1.
    alpha, beta = 1, -1
    assert alpha + beta == 0
    checks["quadratic_metric_fork_symbolic_conditions"] = 2

    e1, e2, e3 = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    assert inv(e1) == (0, 1, 1)
    assert qdir(e1) == 1
    assert qdir(inv(e1)) == 2
    assert inv((3, 4, 0)) == (1, 0, 4)
    assert qdir((3, 4, 0)) == 25
    assert qdir((1, 0, 4)) == 17
    assert add(add(e1, e2), e3) == (0, 0, 0)
    assert can((1, 1, 1)) == (0, 0, 0)
    assert delta((1, 1, 0)) == 1
    assert qdir((1, 1, 0)) == 2
    checks["required_examples_and_metric_fork"] = 10

    payload = {
        "status": "PASS_WITH_REQUIRED_TYPING_NARROWING",
        "primary_verdict": "DGR_INDEPENDENT_NARROW_TYPED_CORRECTION",
        "bounds": {
            "LIFT_BOUND": LIFT_BOUND,
            "SHIFT_BOUND": SHIFT_BOUND,
            "CHART_BOUND": CHART_BOUND,
            "CANONICAL_BOUND": CANONICAL_BOUND,
            "ASSOC_BOUND": ASSOC_BOUND,
        },
        "checks": checks,
        "typing_narrowing": {
            "bare_pf_path_to_stage2_displacement": "NOT_TOTAL_WITHOUT_AN_EXPLICIT_ENDPOINT_ANCHOR_OR_DECORATION",
            "safe_path_domain": "ENDPOINT_ANCHORED_TRANSLATED_LINE_REALIZATIONS_OR_EXPLICITLY_DECORATED_PATH_CATEGORY",
            "canonical_section_type": "USE_A_D_DISPLACEMENT_SECTION_DISTINCT_FROM_A_E_POINT_OR_SECTOR_ADDRESS_TYPE_EVEN_WHEN_THE_UNDERLYING_MIN_ZERO_TRIPLES_COINCIDE",
            "endpoint_pushforward_multiplication": "USE_START_TARGET_TYPED_ACTION_GROUPOID_OR_CATEGORY_ALGEBRA_UNLESS_AN_EXPLICIT_TRANSLATION_IDENTIFICATION_IS_DECLARED",
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["report_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
