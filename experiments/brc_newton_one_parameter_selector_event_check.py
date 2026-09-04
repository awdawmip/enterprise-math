#!/usr/bin/env python3
"""Exact checker for one-parameter selector-event chamber constancy."""
from __future__ import annotations

from fractions import Fraction

from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
Poly = tuple[Fraction, ...]


def p_mul(a: Poly, b: Poly) -> Poly:
    return cd._p_mul(a, b)


def p_eval(poly: Poly, x: Fraction) -> Fraction:
    return cd._p_eval(poly, x)


def cauchy_left(poly: Poly, probe: Fraction) -> Fraction:
    lead = abs(poly[-1])
    bound = max((abs(c) / lead for c in poly[:-1]), default=Q(0))
    return -max(abs(probe) + 2, bound + 2)


def root_rank(poly: Poly, probe: Fraction) -> int:
    if p_eval(poly, probe) == 0:
        raise ValueError("probe is a polynomial root")
    left = cauchy_left(poly, probe)
    return cd._root_count(cd._sturm_sequence(poly), left, probe)


def smallest_real(poly: Poly, root: Fraction):
    if p_eval(poly, root) == 0:
        return None
    return root_rank(poly, root) == 0


def zero_right_rank(poly: Poly) -> int:
    had_zero = False
    work = poly
    while len(work) > 1 and p_eval(work, Q(0)) == 0:
        work = cd._p_div_exact(work, (Q(0), Q(1)))
        had_zero = True
    if len(work) <= 1:
        return int(had_zero)
    return root_rank(work, Q(0)) + int(had_zero)


def smallest_positive(poly: Poly, root: Fraction):
    if root <= 0:
        raise ValueError("positive selector root must be positive")
    if p_eval(poly, root) == 0:
        return None
    return root_rank(poly, root) == zero_right_rank(poly)


def quadratic_family(t: Fraction) -> Poly:
    return (Q(1), t, Q(1))


def depressed_cubic_family(t: Fraction) -> Poly:
    return (t, Q(-3), Q(0), Q(1))


def one_real_cubic_family(t: Fraction) -> Poly:
    return (t, Q(1), Q(0), Q(1))


def degree_five_family(t: Fraction) -> Poly:
    return p_mul(p_mul((Q(1), Q(0), Q(1)), (Q(-1), Q(-1), Q(1))), (Q(-t), Q(1)))


def assert_interval_constant(family, selector, root, groups, expected):
    checks = 0
    statuses = []
    for group, wanted in zip(groups, expected):
        values = []
        for t in group:
            state = selector(family(t), root)
            assert state is not None
            values.append(state)
            assert state is wanted
            checks += 1
        assert len(set(values)) == 1
        statuses.append(values[0])
        checks += 1
    return tuple(statuses), checks


def quadratic_smallest_real_regression():
    groups = (
        (Q(-4), Q(-3), Q(-5, 2)),
        (Q(-3, 2), Q(0), Q(3, 2)),
        (Q(5, 2), Q(3), Q(4)),
    )
    statuses, checks = assert_interval_constant(
        quadratic_family,
        smallest_real,
        Q(-1),
        groups,
        (True, True, False),
    )
    # Event at -2 is non-minimal: state remains true across it.
    assert statuses[0] == statuses[1]
    # Event at +2 is genuine; t=2 is also a declared-root collision.
    assert smallest_real(quadratic_family(Q(2)), Q(-1)) is None
    checks += 2
    return statuses, checks


def quadratic_smallest_positive_regression():
    groups = (
        (Q(-4), Q(-3), Q(-5, 2)),
        (Q(-3, 2), Q(0), Q(3, 2)),
        (Q(5, 2), Q(3), Q(4)),
    )
    statuses, checks = assert_interval_constant(
        quadratic_family,
        smallest_positive,
        Q(1),
        groups,
        (False, True, True),
    )
    assert smallest_positive(quadratic_family(Q(-2)), Q(1)) is None
    # Discriminant event at +2 is non-minimal for this selector.
    assert statuses[1] == statuses[2]
    checks += 2
    return statuses, checks


def cubic_smallest_real_regression():
    groups = (
        (Q(-4), Q(-3), Q(-5, 2)),
        (Q(-3, 2), Q(0), Q(3, 2)),
        (Q(5, 2), Q(3), Q(4)),
    )
    statuses, checks = assert_interval_constant(
        depressed_cubic_family,
        smallest_real,
        Q(-2),
        groups,
        (True, True, False),
    )
    assert statuses[0] == statuses[1]
    assert smallest_real(depressed_cubic_family(Q(2)), Q(-2)) is None
    checks += 2
    return statuses, checks


def cubic_smallest_positive_regression():
    groups = (
        (Q(-4), Q(-3), Q(-5, 2)),
        (Q(-7, 4), Q(-1), Q(-1, 4)),
        (Q(1, 4), Q(1), Q(3)),
    )
    statuses, checks = assert_interval_constant(
        one_real_cubic_family,
        smallest_positive,
        Q(1),
        groups,
        (True, False, True),
    )
    assert smallest_positive(one_real_cubic_family(Q(-2)), Q(1)) is None
    # At t=0 a zero competitor is harmless and starts the right stable chamber.
    assert smallest_positive(one_real_cubic_family(Q(0)), Q(1)) is True
    checks += 2
    return statuses, checks


def degree_five_regression():
    # alpha=(1-sqrt5)/2 lies in (-1,-1/2), beta=(1+sqrt5)/2 in (3/2,2).
    event_quad: Poly = (Q(-1), Q(-1), Q(1))
    seq = cd._sturm_sequence(event_quad)
    assert cd._root_count(seq, Q(-1), Q(-1, 2)) == 1
    assert cd._root_count(seq, Q(3, 2), Q(2)) == 1

    groups = (
        (Q(-3), Q(-2), Q(-1)),
        (Q(-1, 2), Q(-1, 4)),
        (Q(1, 4), Q(1, 2), Q(3, 4)),
        (Q(5, 4), Q(3, 2)),
        (Q(2), Q(3), Q(4)),
    )
    statuses, checks = assert_interval_constant(
        degree_five_family,
        smallest_positive,
        Q(1),
        groups,
        (True, True, False, True, True),
    )
    # Moving-root collision with the declared root at t=1.
    assert smallest_positive(degree_five_family(Q(1)), Q(1)) is None
    # Root crossing zero at t=0 changes unsafe/safe status across the event.
    assert smallest_positive(degree_five_family(Q(0)), Q(1)) is True
    # Irrational discriminant events alpha,beta are both non-minimal selector events.
    assert statuses[0] == statuses[1]
    assert statuses[3] == statuses[4]
    checks += 6
    return statuses, checks


def explicit_event_polynomial_checks():
    checks = 0
    for t in (Q(-4), Q(-3), Q(-1), Q(0), Q(1), Q(3), Q(4)):
        # quadratic real: (t^2-4)(2-t)
        e_qr = (t * t - 4) * (2 - t)
        # quadratic positive: (t^2-4)(t+2)
        e_qp = (t * t - 4) * (t + 2)
        # depressed cubic real, irrelevant nonzero constant omitted
        e_cr = (4 - t * t) * (t - 2)
        # one-real cubic positive
        e_cp = (-4 - 27 * t * t) * (t + 2) * t
        # degree-five positive, fixed nonzero constants omitted
        e_5 = (t * t + 1) ** 2 * (t * t - t - 1) ** 2 * (1 - t) * t
        # Away from the listed rational event values these are nonzero.
        if t not in (Q(-2), Q(2)):
            assert e_qr != 0 and e_qp != 0 and e_cr != 0
        if t not in (Q(-2), Q(0)):
            assert e_cp != 0
        if t not in (Q(0), Q(1)) and t * t - t - 1 != 0:
            assert e_5 != 0
        checks += 5
    return checks


def main() -> int:
    qr = quadratic_smallest_real_regression()
    qp = quadratic_smallest_positive_regression()
    cr = cubic_smallest_real_regression()
    cp = cubic_smallest_positive_regression()
    d5 = degree_five_regression()
    events = explicit_event_polynomial_checks()
    print("BRC one-parameter selector event theorem checker: PASS")
    print(f"quadratic_real_interval_states={qr[0]}")
    print(f"quadratic_real_checks={qr[1]}")
    print(f"quadratic_positive_interval_states={qp[0]}")
    print(f"quadratic_positive_checks={qp[1]}")
    print(f"cubic_real_interval_states={cr[0]}")
    print(f"cubic_real_checks={cr[1]}")
    print(f"cubic_positive_interval_states={cp[0]}")
    print(f"cubic_positive_checks={cp[1]}")
    print(f"degree_five_interval_states={d5[0]}")
    print(f"degree_five_checks={d5[1]}")
    print(f"explicit_event_polynomial_checks={events}")
    print("event_boundary_overapproximation_witnesses=4")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
