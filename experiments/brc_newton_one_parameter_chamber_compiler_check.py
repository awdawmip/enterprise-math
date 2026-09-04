#!/usr/bin/env python3
"""Exact checker for the one-parameter selector chamber compiler."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Callable

from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
Poly = tuple[Fraction, ...]
Labeler = Callable[[Fraction], bool | None]


def trim(poly: Poly) -> Poly:
    return cd._trim(poly)


def peval(poly: Poly, x: Fraction) -> Fraction:
    return cd._p_eval(poly, x)


def squarefree(poly: Poly) -> Poly:
    poly = trim(poly)
    if len(poly) <= 1:
        raise ValueError("event polynomial must be nonconstant")
    derivative = cd._p_derivative(poly)
    gcd = cd._p_gcd(poly, derivative)
    return cd._p_div_exact(poly, gcd) if len(gcd) > 1 else poly


def strict_cauchy_bound(poly: Poly) -> Fraction:
    poly = trim(poly)
    lead = abs(poly[-1])
    ratio = max((abs(c) / lead for c in poly[:-1]), default=Q(0))
    return Q(2) + ratio


def nonroot_split(poly: Poly, left: Fraction, right: Fraction) -> Fraction:
    for denominator in range(2, 40):
        for numerator in range(1, denominator):
            x = left + (right - left) * Q(numerator, denominator)
            if peval(poly, x) != 0:
                return x
    raise AssertionError("could not find rational non-root split")


@dataclass(frozen=True)
class EventRootInterval:
    lower: Fraction
    upper: Fraction


@dataclass(frozen=True)
class CompiledChambers:
    event_polynomial: Poly
    roots: tuple[EventRootInterval, ...]
    samples: tuple[Fraction, ...]
    labels: tuple[bool, ...]
    active_events: tuple[bool, ...]


def isolate_event_roots(poly: Poly, *, max_width: Fraction = Q(1, 4096)) -> tuple[EventRootInterval, ...]:
    sf = squarefree(poly)
    sequence = cd._sturm_sequence(sf)
    bound = strict_cauchy_bound(sf)
    left, right = -bound, bound
    assert peval(sf, left) != 0 and peval(sf, right) != 0
    total = cd._root_count(sequence, left, right)
    if total == 0:
        return ()

    leaves: list[tuple[Fraction, Fraction]] = []

    def split_interval(a: Fraction, b: Fraction, count: int) -> None:
        if count == 0:
            return
        if count == 1:
            leaves.append((a, b))
            return
        mid = nonroot_split(sf, a, b)
        left_count = cd._root_count(sequence, a, mid)
        right_count = cd._root_count(sequence, mid, b)
        assert left_count + right_count == count
        split_interval(a, mid, left_count)
        split_interval(mid, b, right_count)

    split_interval(left, right, total)
    assert len(leaves) == total

    refined: list[EventRootInterval] = []
    for a, b in leaves:
        assert cd._root_count(sequence, a, b) == 1
        while b - a > max_width:
            mid = nonroot_split(sf, a, b)
            left_count = cd._root_count(sequence, a, mid)
            if left_count == 1:
                b = mid
            else:
                assert left_count == 0
                assert cd._root_count(sequence, mid, b) == 1
                a = mid
        refined.append(EventRootInterval(a, b))

    refined.sort(key=lambda interval: interval.lower)
    for index, interval in enumerate(refined):
        assert peval(sf, interval.lower) != 0 and peval(sf, interval.upper) != 0
        assert cd._root_count(sequence, interval.lower, interval.upper) == 1
        if index:
            assert refined[index - 1].upper < interval.lower
    return tuple(refined)


def chamber_samples(poly: Poly, roots: tuple[EventRootInterval, ...]) -> tuple[Fraction, ...]:
    sf = squarefree(poly)
    if not roots:
        return (Q(0),) if peval(sf, Q(0)) != 0 else (Q(1),)
    samples = [roots[0].lower - 1]
    for left, right in zip(roots, roots[1:]):
        assert left.upper < right.lower
        samples.append((left.upper + right.lower) / 2)
    samples.append(roots[-1].upper + 1)
    assert all(peval(sf, sample) != 0 for sample in samples)
    return tuple(samples)


def compile_chambers(event_poly: Poly, labeler: Labeler) -> CompiledChambers:
    roots = isolate_event_roots(event_poly)
    samples = chamber_samples(event_poly, roots)
    labels = []
    for sample in samples:
        label = labeler(sample)
        if label is None:
            raise AssertionError("event-free chamber sample hit typed selector boundary")
        labels.append(label)
    labels_t = tuple(labels)
    active = tuple(labels_t[i] != labels_t[i + 1] for i in range(len(roots)))
    return CompiledChambers(squarefree(event_poly), roots, samples, labels_t, active)


def extra_samples(compiled: CompiledChambers) -> tuple[tuple[Fraction, Fraction], ...]:
    roots = compiled.roots
    if not roots:
        x = compiled.samples[0]
        return ((x - 1, x + 1),)
    output = [(roots[0].lower - 2, roots[0].lower - Q(1, 2))]
    for left, right in zip(roots, roots[1:]):
        gap = right.lower - left.upper
        assert gap > 0
        output.append((left.upper + gap / 3, left.upper + 2 * gap / 3))
    output.append((roots[-1].upper + Q(1, 2), roots[-1].upper + 2))
    return tuple(output)


def poly_rank_lt(poly: Poly, probe: Fraction) -> int:
    if peval(poly, probe) == 0:
        raise ValueError("probe is a polynomial root")
    lead = abs(poly[-1])
    bound = max((abs(c) / lead for c in poly[:-1]), default=Q(0))
    left = -max(abs(probe) + 2, bound + 2)
    return cd._root_count(cd._sturm_sequence(poly), left, probe)


def zero_right_rank(poly: Poly) -> int:
    work = trim(poly)
    had_zero = False
    while len(work) > 1 and peval(work, Q(0)) == 0:
        work = cd._p_div_exact(work, (Q(0), Q(1)))
        had_zero = True
    if len(work) <= 1:
        return int(had_zero)
    return poly_rank_lt(work, Q(0)) + int(had_zero)


def smallest_real_label(poly: Poly, root: Fraction) -> bool | None:
    if peval(poly, root) == 0:
        return None
    return poly_rank_lt(poly, root) == 0


def smallest_positive_label(poly: Poly, root: Fraction) -> bool | None:
    if root <= 0:
        raise ValueError("declared positive root must be positive")
    if peval(poly, root) == 0:
        return None
    return poly_rank_lt(poly, root) == zero_right_rank(poly)


def q_family(t: Fraction) -> Poly:
    return (Q(1), t, Q(1))


def depressed_cubic(t: Fraction) -> Poly:
    return (t, Q(-3), Q(0), Q(1))


def one_real_cubic(t: Fraction) -> Poly:
    return (t, Q(1), Q(0), Q(1))


def degree_five(t: Fraction) -> Poly:
    return cd._p_mul(cd._p_mul((Q(1), Q(0), Q(1)), (Q(-1), Q(-1), Q(1))), (Q(-t), Q(1)))


def validate_compilation(event: Poly, labeler: Labeler, expected_labels, expected_active):
    compiled = compile_chambers(event, labeler)
    assert compiled.labels == expected_labels
    assert compiled.active_events == expected_active
    checks = len(compiled.labels) + len(compiled.active_events)
    for index, pair in enumerate(extra_samples(compiled)):
        for sample in pair:
            assert peval(compiled.event_polynomial, sample) != 0
            label = labeler(sample)
            assert label == expected_labels[index]
            checks += 2
    # Repeated event factors must squarefree to the same chamber partition.
    repeated = cd._p_mul(event, event)
    repeated_compiled = compile_chambers(repeated, labeler)
    assert repeated_compiled.event_polynomial == compiled.event_polynomial
    assert len(repeated_compiled.roots) == len(compiled.roots)
    assert repeated_compiled.labels == compiled.labels
    assert repeated_compiled.active_events == compiled.active_events
    checks += 4
    return compiled, checks


def low_degree_regressions():
    e_pm2: Poly = (Q(-4), Q(0), Q(1))
    qr = validate_compilation(e_pm2, lambda t: smallest_real_label(q_family(t), Q(-1)), (True, True, False), (False, True))
    qp = validate_compilation(e_pm2, lambda t: smallest_positive_label(q_family(t), Q(1)), (False, True, True), (True, False))
    cr = validate_compilation(e_pm2, lambda t: smallest_real_label(depressed_cubic(t), Q(-2)), (True, True, False), (False, True))
    e_cpos: Poly = (Q(0), Q(2), Q(1))  # t(t+2)
    cp = validate_compilation(e_cpos, lambda t: smallest_positive_label(one_real_cubic(t), Q(1)), (True, False, True), (True, True))
    return qr, qp, cr, cp


def degree_five_regression():
    # t(1-t)(t^2-t-1) = -t^4+2t^3-t
    event: Poly = (Q(0), Q(-1), Q(0), Q(2), Q(-1))
    compiled, checks = validate_compilation(
        event,
        lambda t: smallest_positive_label(degree_five(t), Q(1)),
        (True, True, False, True, True),
        (False, True, True, False),
    )
    assert len(compiled.roots) == 4
    sequence = cd._sturm_sequence(squarefree(event))
    assert cd._root_count(sequence, Q(-1), Q(-1, 2)) == 1
    assert cd._root_count(sequence, Q(-1, 10), Q(1, 10)) == 1
    assert cd._root_count(sequence, Q(9, 10), Q(11, 10)) == 1
    assert cd._root_count(sequence, Q(3, 2), Q(2)) == 1
    checks += 4
    return compiled, checks


def isolation_integrity_catalog():
    events = (
        (Q(-4), Q(0), Q(1)),
        (Q(0), Q(2), Q(1)),
        (Q(0), Q(-1), Q(0), Q(2), Q(-1)),
        cd._p_mul((Q(-4), Q(0), Q(1)), (Q(-1), Q(-1), Q(1))),
        cd._p_mul((Q(0), Q(2), Q(1)), (Q(1), Q(0), Q(1))),
    )
    checks = roots = 0
    for event in events:
        sf = squarefree(event)
        intervals = isolate_event_roots(event)
        sequence = cd._sturm_sequence(sf)
        bound = strict_cauchy_bound(sf)
        total = cd._root_count(sequence, -bound, bound)
        assert total == len(intervals)
        assert sum(cd._root_count(sequence, item.lower, item.upper) for item in intervals) == total
        roots += total
        checks += len(intervals) + 2
    return len(events), roots, checks


def main() -> int:
    qr, qp, cr, cp = low_degree_regressions()
    d5 = degree_five_regression()
    isolation = isolation_integrity_catalog()
    print("BRC exact one-parameter selector chamber compiler checker: PASS")
    print(f"quadratic_real_labels={qr[0].labels}")
    print(f"quadratic_real_active={qr[0].active_events}")
    print(f"quadratic_positive_labels={qp[0].labels}")
    print(f"quadratic_positive_active={qp[0].active_events}")
    print(f"cubic_real_labels={cr[0].labels}")
    print(f"cubic_positive_labels={cp[0].labels}")
    print(f"low_degree_compiler_checks={qr[1]+qp[1]+cr[1]+cp[1]}")
    print(f"degree_five_labels={d5[0].labels}")
    print(f"degree_five_active={d5[0].active_events}")
    print(f"degree_five_checks={d5[1]}")
    print(f"isolation_catalog_event_polynomials={isolation[0]}")
    print(f"isolated_real_event_roots={isolation[1]}")
    print(f"isolation_integrity_checks={isolation[2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
