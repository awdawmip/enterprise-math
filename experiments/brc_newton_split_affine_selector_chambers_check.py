#!/usr/bin/env python3
"""Exact checker for complete split-affine Newton root-selector chambers."""
from __future__ import annotations

from fractions import Fraction
from itertools import product

from enterprise_math import brc_critical_degeneracy as cd
from enterprise_math.brc_newton_schedule_strata import RationalAffineForm

Q = Fraction
Poly = tuple[Fraction, ...]


def form(const=0, *linear) -> RationalAffineForm:
    return RationalAffineForm((Q(const),) + tuple(Q(value) for value in linear))


def order_form(branch: RationalAffineForm, threshold: Fraction) -> RationalAffineForm:
    constant = RationalAffineForm.constant(-threshold, branch.parameter_count)
    return branch.add(constant)


def noncollision(root: Fraction, branches, parameters) -> bool:
    return all(branch.evaluate(parameters) != root for branch, _ in branches)


def smallest_real_certificate(root: Fraction, branches, parameters) -> bool:
    return noncollision(root, branches, parameters) and all(
        order_form(branch, root).evaluate(parameters) > 0 for branch, _ in branches
    )


def smallest_positive_certificate(root: Fraction, branches, parameters) -> bool:
    if root <= 0 or not noncollision(root, branches, parameters):
        return False
    for branch, _ in branches:
        value = branch.evaluate(parameters)
        if not (value <= 0 or value > root):
            return False
    return True


def pmul(left: Poly, right: Poly) -> Poly:
    out = [Q(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def ppow(poly: Poly, exponent: int) -> Poly:
    out: Poly = (Q(1),)
    for _ in range(exponent):
        out = pmul(out, poly)
    return out


def peval(poly: Poly, value: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def materialize_split_polynomial(root: Fraction, multiplicity: int, branches, parameters) -> tuple[Poly, tuple[Fraction, ...]]:
    if multiplicity < 1:
        raise ValueError("multiplicity must be positive")
    poly = ppow((-root, Q(1)), multiplicity)
    roots = [root] * multiplicity
    for branch, branch_multiplicity in branches:
        if branch_multiplicity < 1:
            raise ValueError("branch multiplicity must be positive")
        value = branch.evaluate(parameters)
        poly = pmul(poly, ppow((-value, Q(1)), branch_multiplicity))
        roots.extend([value] * branch_multiplicity)
    assert len(poly) - 1 == multiplicity + sum(m for _, m in branches)
    for value in set(roots):
        assert peval(poly, value) == 0
    return poly, tuple(roots)


def sturm_distinct_real_root_count(poly: Poly, roots: tuple[Fraction, ...]) -> int:
    bound = max((abs(value) for value in roots), default=Q(0)) + 2
    assert peval(poly, -bound) != 0 and peval(poly, bound) != 0
    return cd._root_count(cd._sturm_sequence(poly), -bound, bound)


def brute_smallest_real(root: Fraction, roots: tuple[Fraction, ...]) -> bool:
    return root == min(roots)


def brute_smallest_positive(root: Fraction, roots: tuple[Fraction, ...]) -> bool:
    positive = [value for value in roots if value > 0]
    return bool(positive) and root == min(positive)


def two_parameter_smallest_real_regression():
    root = Q(-1)
    branches = ((form(0, 1, 0), 1), (form(0, 0, 1), 1))  # u,v
    grid = (Q(-3), Q(-2), Q(-1), Q(-1, 2), Q(0), Q(1), Q(2))
    points = fixed_multiplicity = stable = collisions = sturm_checks = selector_checks = 0
    for parameters in product(grid, repeat=2):
        poly, roots = materialize_split_polynomial(root, 2, branches, parameters)
        distinct = len(set(roots))
        assert sturm_distinct_real_root_count(poly, roots) == distinct
        sturm_checks += 1
        valid = noncollision(root, branches, parameters)
        predicted = smallest_real_certificate(root, branches, parameters)
        brute = brute_smallest_real(root, roots)
        if valid:
            fixed_multiplicity += 1
            assert predicted == brute
            if predicted:
                stable += 1
                assert parameters[0] > -1 and parameters[1] > -1
        else:
            collisions += 1
            # Selector value may remain root at a collision, but the declared
            # multiplicity-2 schedule is invalid there.
            assert -1 in parameters
        selector_checks += 2
        points += 1
    assert points == 49
    assert fixed_multiplicity == 36
    assert collisions == 13
    assert stable == 16
    return points, fixed_multiplicity, collisions, stable, sturm_checks, selector_checks


def two_parameter_smallest_positive_regression():
    root = Q(1)
    branches = ((form(0, 1, 0), 1), (form(0, 0, 1), 1))
    grid = (Q(-2), Q(-1), Q(0), Q(1, 2), Q(1), Q(3, 2), Q(2))
    points = fixed_multiplicity = stable = collisions = sturm_checks = selector_checks = zero_boundary = 0
    for parameters in product(grid, repeat=2):
        poly, roots = materialize_split_polynomial(root, 2, branches, parameters)
        assert sturm_distinct_real_root_count(poly, roots) == len(set(roots))
        sturm_checks += 1
        valid = noncollision(root, branches, parameters)
        predicted = smallest_positive_certificate(root, branches, parameters)
        brute = brute_smallest_positive(root, roots)
        if valid:
            fixed_multiplicity += 1
            assert predicted == brute
            if predicted:
                stable += 1
                for value in parameters:
                    assert value <= 0 or value > 1
            if 0 in parameters:
                zero_boundary += 1
                # Zero is not positive and does not defeat the selected root.
                other = parameters[1] if parameters[0] == 0 else parameters[0]
                expected = other <= 0 or other > 1
                assert predicted == expected
        else:
            collisions += 1
            assert 1 in parameters
        selector_checks += 2
        points += 1
    assert points == 49
    assert fixed_multiplicity == 36
    assert collisions == 13
    assert stable == 25
    return points, fixed_multiplicity, collisions, stable, zero_boundary, sturm_checks, selector_checks


def one_parameter_boundary_sweep():
    real_root = Q(-1)
    positive_root = Q(1)
    t_branch = ((form(0, 1), 1),)
    grid = tuple(Q(n, 4) for n in range(-12, 13))
    real_stable = positive_stable = real_collisions = positive_collisions = checks = 0
    for (t,) in ((value,) for value in grid):
        real_poly, real_roots = materialize_split_polynomial(real_root, 2, t_branch, (t,))
        positive_poly, positive_roots = materialize_split_polynomial(positive_root, 2, t_branch, (t,))
        assert sturm_distinct_real_root_count(real_poly, real_roots) == len(set(real_roots))
        assert sturm_distinct_real_root_count(positive_poly, positive_roots) == len(set(positive_roots))

        real_valid = t != -1
        real_predicted = smallest_real_certificate(real_root, t_branch, (t,))
        if real_valid:
            assert real_predicted == (t > -1)
            assert real_predicted == brute_smallest_real(real_root, real_roots)
            real_stable += int(real_predicted)
        else:
            real_collisions += 1
            assert brute_smallest_real(real_root, real_roots)  # value stable, multiplicity not

        positive_valid = t != 1
        positive_predicted = smallest_positive_certificate(positive_root, t_branch, (t,))
        if positive_valid:
            assert positive_predicted == (t <= 0 or t > 1)
            assert positive_predicted == brute_smallest_positive(positive_root, positive_roots)
            positive_stable += int(positive_predicted)
        else:
            positive_collisions += 1
            assert brute_smallest_positive(positive_root, positive_roots)  # value stable, multiplicity not
        if t == 0:
            assert positive_predicted
        checks += 8
    assert real_collisions == 1 and positive_collisions == 1
    return len(grid), real_stable, positive_stable, real_collisions, positive_collisions, checks


def affine_order_form_checks():
    # h(u,v)=2+3u-2v.  Threshold comparisons remain affine exactly.
    h = form(2, 3, -2)
    above_minus_one = order_form(h, Q(-1))
    above_one = order_form(h, Q(1))
    assert above_minus_one.coefficients == (Q(3), Q(3), Q(-2))
    assert above_one.coefficients == (Q(1), Q(3), Q(-2))
    checks = 0
    for params in product((Q(-1), Q(0), Q(1)), repeat=2):
        value = h.evaluate(params)
        assert (above_minus_one.evaluate(params) > 0) == (value > -1)
        assert (above_one.evaluate(params) > 0) == (value > 1)
        checks += 2
    return checks


def main() -> int:
    real = two_parameter_smallest_real_regression()
    positive = two_parameter_smallest_positive_regression()
    sweep = one_parameter_boundary_sweep()
    affine = affine_order_form_checks()
    print("BRC split-affine selector chamber checker: PASS")
    print(f"smallest_real_grid_points={real[0]}")
    print(f"smallest_real_fixed_multiplicity_points={real[1]}")
    print(f"smallest_real_collision_points={real[2]}")
    print(f"smallest_real_stable_points={real[3]}")
    print(f"smallest_real_sturm_checks={real[4]}")
    print(f"smallest_real_selector_checks={real[5]}")
    print(f"smallest_positive_grid_points={positive[0]}")
    print(f"smallest_positive_fixed_multiplicity_points={positive[1]}")
    print(f"smallest_positive_collision_points={positive[2]}")
    print(f"smallest_positive_stable_points={positive[3]}")
    print(f"zero_boundary_points={positive[4]}")
    print(f"smallest_positive_sturm_checks={positive[5]}")
    print(f"smallest_positive_selector_checks={positive[6]}")
    print(f"one_parameter_boundary_points={sweep[0]}")
    print(f"one_parameter_smallest_real_stable={sweep[1]}")
    print(f"one_parameter_smallest_positive_stable={sweep[2]}")
    print(f"one_parameter_real_collisions={sweep[3]}")
    print(f"one_parameter_positive_collisions={sweep[4]}")
    print(f"one_parameter_boundary_checks={sweep[5]}")
    print(f"affine_order_form_checks={affine}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
