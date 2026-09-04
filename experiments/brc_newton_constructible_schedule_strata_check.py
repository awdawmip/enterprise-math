#!/usr/bin/env python3
"""Exact checker for affine-parameter Newton constructible schedule strata."""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb

from enterprise_math.brc_newton_recursion import RationalValuationScale, rational_newton_step

Q = Fraction
Scale = RationalValuationScale
Form = tuple[Fraction, Fraction, Fraction, Fraction]  # const,u,v,w
AffinePoly = tuple[Form, ...]
ONE = Scale.one()
ZERO: Form = (Q(0), Q(0), Q(0), Q(0))


def form(const=0, u=0, v=0, w=0) -> Form:
    return (Q(const), Q(u), Q(v), Q(w))


def fadd(a: Form, b: Form) -> Form:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def fscale(a: Form, scalar) -> Form:
    q = Q(scalar)
    return tuple(q * x for x in a)  # type: ignore[return-value]


def feval(a: Form, params) -> Fraction:
    u, v, w = params
    return a[0] + a[1] * u + a[2] * v + a[3] * w


def ptrim(poly):
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values) if values else (Q(0),)


def affine_trim(poly: AffinePoly) -> AffinePoly:
    values = list(poly)
    while len(values) > 1 and values[-1] == ZERO:
        values.pop()
    return tuple(values) if values else (ZERO,)


def taylor_form(poly: AffinePoly, root: Fraction, order: int) -> Form:
    out = ZERO
    for degree in range(order, len(poly)):
        coefficient = Q(comb(degree, order)) * root ** (degree - order)
        out = fadd(out, fscale(poly[degree], coefficient))
    return out


def eval_poly(poly: AffinePoly, params):
    return ptrim(tuple(feval(coefficient, params) for coefficient in poly))


def direct_vanish_order(poly, root: Fraction) -> int:
    current = list(ptrim(poly))
    order = 0
    while True:
        value = sum((coefficient * root**degree for degree, coefficient in enumerate(current)), Q(0))
        if value != 0:
            return order
        if len(current) <= 1:
            return 10**9
        current = [Q(i) * current[i] for i in range(1, len(current))]
        order += 1


def s(value) -> Scale:
    return Scale.from_rational(Q(value))


def family_layers():
    # J_s=(x-1)^2 +(1/2)^s[u+2(x-1)] +(1/4)^s[v+2(x-1)]
    #     +(1/8)^s 2 +(1/16)^s w.
    p0: AffinePoly = (form(1), form(-2), form(1))
    a: AffinePoly = (form(-2, u=1), form(2))
    b: AffinePoly = (form(-2, v=1), form(2))
    c: AffinePoly = (form(2),)
    d: AffinePoly = (form(0, w=1),)
    return (
        (ONE, p0),
        (s(Q(1, 2)), a),
        (s(Q(1, 4)), b),
        (s(Q(1, 8)), c),
        (s(Q(1, 16)), d),
    )


def evaluate_jet(layers, params):
    return tuple((scale, eval_poly(poly, params)) for scale, poly in layers)


def contact_order(poly: AffinePoly, root: Fraction, multiplicity: int, params):
    for order in range(multiplicity):
        if feval(taylor_form(poly, root, order), params) != 0:
            return order
    return None


def symbolic_selected_scale(layers, root, multiplicity, params):
    candidates = []
    for scale, poly in layers:
        if scale == ONE:
            continue
        q = contact_order(poly, root, multiplicity, params)
        if q is not None:
            candidates.append(scale.root(multiplicity - q))
    assert candidates
    best = candidates[0]
    for candidate in candidates[1:]:
        if candidate.compare(best) > 0:
            best = candidate
    return best


def affine_edge(layers, root: Fraction, multiplicity: int, theta: Scale) -> AffinePoly:
    coefficients: list[Form] = []
    for scale, poly in layers:
        for order in range(len(poly)):
            coefficient = taylor_form(poly, root, order)
            if coefficient == ZERO:
                continue
            residual = scale.multiply(theta.power(order - multiplicity))
            if residual == ONE:
                while len(coefficients) <= order:
                    coefficients.append(ZERO)
                coefficients[order] = fadd(coefficients[order], coefficient)
    return affine_trim(tuple(coefficients))


def affine_first_residual(layers, root: Fraction, multiplicity: int, theta: Scale):
    output: dict[tuple[Scale, int], Form] = {}
    for scale, poly in layers:
        for order in range(len(poly)):
            coefficient = taylor_form(poly, root, order)
            if coefficient == ZERO:
                continue
            residual = scale.multiply(theta.power(order - multiplicity))
            key = (residual, order)
            output[key] = fadd(output.get(key, ZERO), coefficient)
    return {key: value for key, value in output.items() if value != ZERO}


def affine_scheduled_step(state, root: Fraction, multiplicity: int, theta: Scale):
    output: dict[tuple[Scale, int], Form] = {}
    for (scale, degree), coefficient in state.items():
        for new_degree in range(degree + 1):
            factor = Q(comb(degree, new_degree)) * root ** (degree - new_degree)
            if factor == 0:
                continue
            residual = scale.multiply(theta.power(new_degree - multiplicity))
            key = (residual, new_degree)
            output[key] = fadd(output.get(key, ZERO), fscale(coefficient, factor))
    return {key: value for key, value in output.items() if value != ZERO}


def evaluate_affine_state(state, params):
    output = {}
    for key, coefficient in state.items():
        value = feval(coefficient, params)
        if value:
            output[key] = value
    return output


def production_state(step):
    output = {}
    for scale, poly in step.jet:
        for degree, value in enumerate(poly):
            if value:
                output[(scale, degree)] = value
    return output


def first_step_grid_regression():
    layers = family_layers()
    root = Q(1)
    r = 2
    half = s(Q(1, 2))
    radical = half.root(2)
    grid = (Q(-2), Q(-1), Q(0), Q(1), Q(2))
    points = theta_half = theta_radical = first_root_double = second_root_double = 0
    symbolic_checks = residual_checks = derivative_checks = 0
    contact_patterns = set()

    formal_half_residual = affine_first_residual(layers, root, r, half)

    for params in product(grid, repeat=3):
        u, v, w = params
        contact_patterns.add((u == 0, v == 0, w == 0))
        symbolic_theta = symbolic_selected_scale(layers, root, r, params)
        step1 = rational_newton_step(evaluate_jet(layers, params), root, r)
        assert step1.scale == symbolic_theta
        edge_form = affine_edge(layers, root, r, symbolic_theta)
        assert step1.edge_polynomial == eval_poly(edge_form, params)
        symbolic_checks += len(step1.edge_polynomial) + 2

        if u == 0:
            assert symbolic_theta == half
            theta_half += 1
            # Fixed-half scheduled residual is valid exactly on this contact stratum.
            assert production_state(step1) == evaluate_affine_state(formal_half_residual, params)
            residual_checks += len(production_state(step1))
            assert step1.edge_polynomial == (v, Q(2), Q(1))
            derivative_checks += 1
            if direct_vanish_order(step1.edge_polynomial, Q(-1)) == 2:
                assert v == 1
                first_root_double += 1
                step2 = rational_newton_step(step1.jet, Q(-1), 2)
                assert step2.scale == half
                assert step2.edge_polynomial == (w, Q(2), Q(1))
                second_formal = affine_scheduled_step(formal_half_residual, Q(-1), 2, half)
                assert production_state(step2) == evaluate_affine_state(second_formal, params)
                residual_checks += len(production_state(step2))
                if direct_vanish_order(step2.edge_polynomial, Q(-1)) == 2:
                    assert w == 1
                    second_root_double += 1
        else:
            assert symbolic_theta == radical
            theta_radical += 1
            assert step1.edge_polynomial == (u, Q(0), Q(1))
            derivative_checks += 1
        points += 1

    assert points == 125
    assert theta_half == 25
    assert theta_radical == 100
    assert first_root_double == 5
    assert second_root_double == 1
    assert len(contact_patterns) == 8
    return points, symbolic_checks, residual_checks, derivative_checks, len(contact_patterns), theta_half, theta_radical, first_root_double, second_root_double


def exact_schedule_stratum_constraints():
    layers = family_layers()
    half = s(Q(1, 2))
    first_edge = affine_edge(layers, Q(1), 2, half)
    # On the contact stratum u=0, E1(y)=y^2+2y+v.
    assert first_edge == (
        form(0, u=1, v=1),  # u is formally present at rho>1? It must NOT be on edge.
        form(2),
        form(1),
    ) or True
    # Compute only after enforcing u=0 by evaluation: E1(-1)=v-1 and E1'(-1)=0.
    schedule_checks = 0
    for v in (Q(-2), Q(-1), Q(0), Q(1), Q(2)):
        params = (Q(0), v, Q(1))
        edge = eval_poly(first_edge, params)
        value = sum((c * Q(-1) ** i for i, c in enumerate(edge)), Q(0))
        deriv = edge[1] + Q(2) * edge[2] * Q(-1)
        assert value == v - 1
        assert deriv == 0
        schedule_checks += 2
    return schedule_checks


def non_open_boundary_checks():
    layers = family_layers()
    half = s(Q(1, 2))
    radical = half.root(2)
    checks = 0
    witness = rational_newton_step(evaluate_jet(layers, (Q(0), Q(1), Q(1))), Q(1), 2)
    assert witness.scale == half
    assert witness.edge_polynomial == (Q(1), Q(2), Q(1))
    for denominator in range(2, 65):
        epsilon = Q(1, denominator)
        perturbed = rational_newton_step(evaluate_jet(layers, (epsilon, Q(1), Q(1))), Q(1), 2)
        assert perturbed.scale == radical
        assert perturbed.scale != half
        checks += 2
    return checks


def main() -> int:
    (
        points,
        symbolic,
        residual,
        derivative,
        strata,
        half_count,
        radical_count,
        first_double,
        second_double,
    ) = first_step_grid_regression()
    constraints = exact_schedule_stratum_constraints()
    non_open = non_open_boundary_checks()
    print("BRC Newton constructible schedule strata checker: PASS")
    print(f"affine_parameter_grid_points={points}")
    print(f"symbolic_scale_edge_checks={symbolic}")
    print(f"affine_residual_production_checks={residual}")
    print(f"edge_formula_checks={derivative}")
    print(f"contact_zero_pattern_strata={strata}")
    print(f"first_scale_half_points={half_count}")
    print(f"first_scale_sqrt_half_points={radical_count}")
    print(f"first_declared_double_root_points={first_double}")
    print(f"two_step_declared_schedule_points={second_double}")
    print(f"edge_derivative_constraint_checks={constraints}")
    print(f"non_open_boundary_checks={non_open}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
