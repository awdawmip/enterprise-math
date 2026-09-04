#!/usr/bin/env python3
"""Exact checker for the one-parameter resultant selector-event generator."""
from __future__ import annotations

from fractions import Fraction

from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
TPoly = tuple[Fraction, ...]          # ascending t powers
XPoly = tuple[TPoly, ...]            # ascending x powers, coefficients in Q[t]
ZERO: TPoly = (Q(0),)
ONE: TPoly = (Q(1),)


def t_trim(poly: TPoly) -> TPoly:
    values = list(poly) if poly else [Q(0)]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def t_const(value) -> TPoly:
    return (Q(value),)


def t_add(a: TPoly, b: TPoly) -> TPoly:
    n = max(len(a), len(b))
    return t_trim(tuple((a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0)) for i in range(n)))


def t_scale(poly: TPoly, scalar) -> TPoly:
    return t_trim(tuple(Q(scalar) * value for value in poly))


def t_mul(a: TPoly, b: TPoly) -> TPoly:
    out = [Q(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return t_trim(tuple(out))


def t_eval(poly: TPoly, value: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def t_divmod(a: TPoly, b: TPoly):
    a, b = t_trim(a), t_trim(b)
    if b == ZERO:
        raise ZeroDivisionError
    if len(a) < len(b):
        return ZERO, a
    quotient = [Q(0) for _ in range(len(a) - len(b) + 1)]
    remainder = list(a)
    while len(remainder) >= len(b) and any(remainder):
        degree = len(remainder) - len(b)
        factor = remainder[-1] / b[-1]
        quotient[degree] += factor
        for j, coefficient in enumerate(b):
            remainder[degree + j] -= factor * coefficient
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return t_trim(tuple(quotient)), t_trim(tuple(remainder))


def t_div_exact(a: TPoly, b: TPoly) -> TPoly:
    q, r = t_divmod(a, b)
    assert r == ZERO
    return q


def x_trim(poly: XPoly) -> XPoly:
    values = list(poly)
    while len(values) > 1 and t_trim(values[-1]) == ZERO:
        values.pop()
    return tuple(t_trim(value) for value in values)


def x_derivative(poly: XPoly) -> XPoly:
    poly = x_trim(poly)
    if len(poly) <= 1:
        return (ZERO,)
    return x_trim(tuple(t_scale(poly[i], i) for i in range(1, len(poly))))


def x_eval(poly: XPoly, value: Fraction) -> TPoly:
    out = ZERO
    power = Q(1)
    for coefficient in poly:
        out = t_add(out, t_scale(coefficient, power))
        power *= value
    return out


def x_mul(a: XPoly, b: XPoly) -> XPoly:
    out = [ZERO for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = t_add(out[i + j], t_mul(x, y))
    return x_trim(tuple(out))


def determinant_poly_matrix(matrix: tuple[tuple[TPoly, ...], ...]) -> TPoly:
    n = len(matrix)
    assert n > 0 and all(len(row) == n for row in matrix)
    dp: dict[int, TPoly] = {0: ONE}
    for row in range(n):
        nxt: dict[int, TPoly] = {}
        for mask, partial in dp.items():
            assert mask.bit_count() == row
            for column in range(n):
                if mask & (1 << column):
                    continue
                entry = matrix[row][column]
                if entry == ZERO:
                    continue
                inversions_with_prior = (mask >> (column + 1)).bit_count()
                term = t_mul(partial, entry)
                if inversions_with_prior % 2:
                    term = t_scale(term, -1)
                target = mask | (1 << column)
                nxt[target] = t_add(nxt.get(target, ZERO), term)
        dp = nxt
    return t_trim(dp.get((1 << n) - 1, ZERO))


def sylvester_resultant(p: XPoly, q: XPoly) -> TPoly:
    p, q = x_trim(p), x_trim(q)
    if p == (ZERO,) or q == (ZERO,):
        return ZERO
    m, n = len(p) - 1, len(q) - 1
    size = m + n
    if size == 0:
        return ONE
    p_desc = tuple(reversed(p))
    q_desc = tuple(reversed(q))
    rows: list[tuple[TPoly, ...]] = []
    for shift in range(n):
        row = [ZERO for _ in range(size)]
        for j, coefficient in enumerate(p_desc):
            row[shift + j] = coefficient
        rows.append(tuple(row))
    for shift in range(m):
        row = [ZERO for _ in range(size)]
        for j, coefficient in enumerate(q_desc):
            row[shift + j] = coefficient
        rows.append(tuple(row))
    return determinant_poly_matrix(tuple(rows))


def resultant_event_factor(poly: XPoly) -> TPoly:
    return sylvester_resultant(poly, x_derivative(poly))


def generated_event(poly: XPoly, root: Fraction, *, positive: bool) -> TPoly:
    event = t_mul(resultant_event_factor(poly), x_eval(poly, root))
    if positive:
        event = t_mul(event, x_eval(poly, Q(0)))
    return t_trim(event)


def real_root_count(poly: TPoly) -> int:
    poly = t_trim(poly)
    if poly == ZERO:
        raise ValueError("identically zero event polynomial")
    derivative = cd._p_derivative(poly)
    gcd = cd._p_gcd(poly, derivative)
    sf = cd._p_div_exact(poly, gcd) if len(gcd) > 1 else poly
    lead = abs(sf[-1])
    bound = Q(2) + max((abs(c) / lead for c in sf[:-1]), default=Q(0))
    return cd._root_count(cd._sturm_sequence(sf), -bound, bound)


def low_degree_resultants():
    t: TPoly = (Q(0), Q(1))
    checks = 0

    quadratic: XPoly = (ONE, t, ONE)
    result_q = resultant_event_factor(quadratic)
    assert result_q == (Q(4), Q(0), Q(-1))
    checks += 1

    degree_drop: XPoly = (ONE, ONE, t)
    result_drop = resultant_event_factor(degree_drop)
    assert result_drop == (Q(0), Q(-1), Q(4))  # t(4t-1)
    assert t_eval(result_drop, Q(0)) == 0
    assert t_eval(result_drop, Q(1, 4)) == 0
    checks += 3

    depressed: XPoly = (t, t_const(-3), ZERO, ONE)
    result_dep = resultant_event_factor(depressed)
    assert result_dep == (Q(-108), Q(0), Q(27))
    checks += 1

    one_real: XPoly = (t, ONE, ZERO, ONE)
    result_one = resultant_event_factor(one_real)
    assert result_one == (Q(4), Q(0), Q(27))
    assert real_root_count(result_one) == 0
    checks += 2

    return checks, quadratic, depressed, one_real


def generated_low_degree_events(quadratic: XPoly, depressed: XPoly, one_real: XPoly):
    checks = 0
    q_real = generated_event(quadratic, Q(-1), positive=False)
    q_pos = generated_event(quadratic, Q(1), positive=True)
    dep_real = generated_event(depressed, Q(-2), positive=False)
    one_pos = generated_event(one_real, Q(1), positive=True)

    assert real_root_count(q_real) == 2
    assert real_root_count(q_pos) == 2
    assert real_root_count(dep_real) == 2
    assert real_root_count(one_pos) == 2
    checks += 4

    # Exact expected real event values.
    for event in (q_real, q_pos, dep_real):
        assert t_eval(event, Q(-2)) == 0
        assert t_eval(event, Q(2)) == 0
        checks += 2
    assert t_eval(one_pos, Q(-2)) == 0
    assert t_eval(one_pos, Q(0)) == 0
    checks += 2
    return checks


def degree_five_resultant():
    t: TPoly = (Q(0), Q(1))
    x2p1: XPoly = (ONE, ZERO, ONE)
    x2mxm1: XPoly = (t_const(-1), t_const(-1), ONE)
    moving: XPoly = (t_scale(t, -1), ONE)
    family = x_mul(x_mul(x2p1, x2mxm1), moving)
    assert len(family) - 1 == 5

    result = resultant_event_factor(family)
    ft = t_mul((Q(1), Q(0), Q(1)), (Q(-1), Q(-1), Q(1)))
    ft2 = t_mul(ft, ft)
    quotient = t_div_exact(result, ft2)
    assert len(quotient) == 1 and quotient[0] != 0

    event = generated_event(family, Q(1), positive=True)
    expected_real_factor = t_mul(t_mul(t, (Q(-1), Q(1))), (Q(-1), Q(-1), Q(1)))
    quotient_event = t_div_exact(event, t_mul(ft2, t_mul(t, (Q(-1), Q(1)))))
    assert len(quotient_event) == 1 and quotient_event[0] != 0
    assert real_root_count(event) == 4
    assert real_root_count(expected_real_factor) == 4
    for value in (Q(0), Q(1)):
        assert t_eval(event, value) == 0
    checks = 8
    return checks


def repeated_factor_boundary():
    t: TPoly = (Q(0), Q(1))
    moving: XPoly = (t_scale(t, -1), ONE)
    repeated = x_mul(moving, moving)
    assert resultant_event_factor(repeated) == ZERO
    return 1


def sylvester_specialization_checks():
    # Independent low-size specialization check: for a rational t0, the
    # polynomial-in-t resultant must equal the Fraction resultant of the
    # specialized x-polynomial and derivative.
    t: TPoly = (Q(0), Q(1))
    families = (
        (ONE, t, ONE),
        (t, t_const(-3), ZERO, ONE),
        (ONE, ONE, t),
    )
    checks = 0
    for family in families:
        result = resultant_event_factor(family)
        for t0 in (Q(-2), Q(-1, 2), Q(0), Q(1, 4), Q(1), Q(3)):
            specialized = tuple((t_const(t_eval(coefficient, t0))) for coefficient in family)
            specialized_result = resultant_event_factor(specialized)
            assert len(specialized_result) == 1
            assert specialized_result[0] == t_eval(result, t0)
            checks += 1
    return checks


def main() -> int:
    low = low_degree_resultants()
    generated = generated_low_degree_events(low[1], low[2], low[3])
    degree5 = degree_five_resultant()
    repeated = repeated_factor_boundary()
    specialization = sylvester_specialization_checks()
    print("BRC resultant selector-event generator checker: PASS")
    print(f"low_degree_resultant_checks={low[0]}")
    print(f"generated_low_degree_event_checks={generated}")
    print(f"degree_five_resultant_checks={degree5}")
    print(f"generic_repeated_factor_boundary_checks={repeated}")
    print(f"sylvester_specialization_checks={specialization}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
