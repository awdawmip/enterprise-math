#!/usr/bin/env python3
"""Exact checker for root-active characteristic jets with a simple critical Perron root."""
from __future__ import annotations

from fractions import Fraction
from itertools import product

import brc_critical_ratio_spectral_response_check as rsp
import brc_global_powered_strict_gauge_reducible_check as red
from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
Branch = tuple[int, int, Fraction]
IntMatrix = tuple[tuple[int, ...], ...]
Poly = tuple[Fraction, ...]


def branches_from_assignment(cells, assignment) -> tuple[Branch, ...]:
    return tuple(
        (u, v, q)
        for (u, v), weights in zip(cells, assignment)
        for q in weights
    )


def levels_layers(n: int, records):
    levels = tuple(sorted({lam for _, _, lam, _ in records}, reverse=True))
    layers = []
    for level in levels:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for u, v, lam, _ in records:
            if lam == level:
                matrix[u][v] += 1
        layers.append(tuple(tuple(row) for row in matrix))
    return levels, tuple(layers)


def peval(poly: Poly, value: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (Q(0),)
    values = tuple(Q(i) * poly[i] for i in range(1, len(poly)))
    while len(values) > 1 and values[-1] == 0:
        values = values[:-1]
    return values


def selector_simple(p0: Poly, selector) -> bool:
    dp = derivative(p0)
    if selector.is_rational:
        assert selector.exact_root is not None
        return peval(dp, selector.exact_root) != 0
    seq = cd._sturm_sequence(dp)
    return cd._root_count(seq, selector.lower, selector.upper) == 0


def vanishes_at_selector(p0: Poly, poly: Poly, selector) -> bool:
    if poly == (Q(0),):
        return True
    if selector.is_rational:
        assert selector.exact_root is not None
        return peval(poly, selector.exact_root) == 0
    gcd = cd._p_gcd(p0, poly)
    if len(gcd) <= 1:
        return False
    seq = cd._sturm_sequence(gcd)
    return cd._root_count(seq, selector.lower, selector.upper) > 0


def active_sign(p0: Poly, poly: Poly, p0_int: tuple[int, ...]) -> int:
    # Refine until neither the active polynomial nor p0' has another zero in
    # the root-selector interval; then midpoint signs certify beta>0.
    dp = derivative(p0)
    for power in range(12, 28):
        selector = cd.smallest_positive_root_selector(p0_int, max_width=Q(1, 2**power))
        if selector.is_rational:
            assert selector.exact_root is not None
            z = selector.exact_root
            a = peval(poly, z)
            b = peval(dp, z)
            assert a != 0 and b != 0 and a * b > 0
            return 3
        seq_a = cd._sturm_sequence(poly)
        seq_b = cd._sturm_sequence(dp)
        if (
            cd._root_count(seq_a, selector.lower, selector.upper) == 0
            and cd._root_count(seq_b, selector.lower, selector.upper) == 0
        ):
            midpoint = (selector.lower + selector.upper) / 2
            a = peval(poly, midpoint)
            b = peval(dp, midpoint)
            assert a != 0 and b != 0 and a * b > 0
            return 5
    raise AssertionError("could not isolate active-response sign")


def evaluate_expansion(expansion: dict[Fraction, Poly], step: int, z: Fraction) -> Fraction:
    return sum(
        ((base**step) * peval(poly, z) for base, poly in expansion.items()),
        Q(0),
    )


def direct_det(levels, layers, step: int, z: Fraction) -> Fraction:
    matrix = red.mat_jet(levels, layers, step) if hasattr(red, "mat_jet") else None
    if matrix is None:
        n = len(layers[0])
        matrix = tuple(
            tuple(
                sum(((level**step) * layers[k][i][j] for k, level in enumerate(levels)), Q(0))
                for j in range(n)
            )
            for i in range(n)
        )
    n = len(matrix)
    total = Q(0)
    from itertools import permutations
    for perm in permutations(range(n)):
        term = Q(rsp.sign_of_permutation(tuple(perm)))
        for i, j in enumerate(perm):
            if i == j:
                term *= Q(1) - z * matrix[i][j]
            else:
                term *= -z * matrix[i][j]
        total += term
    return total


def validate(n: int, branches: tuple[Branch, ...], sign_check: bool):
    try:
        data = red.global_strict_gauge(n, branches)
    except ValueError:
        return None
    gauge, _, _, _, records, _, _, _ = data
    K = gauge.analysis.critical_matrix
    if rsp.irreducible(K):
        return None  # this checker targets the genuinely reducible frontier

    levels, layers = levels_layers(n, records)
    expansion = rsp.determinant_exponential_expansion(levels, layers)
    p0_int = cd.criticality_polynomial(K)
    p0 = tuple(Q(value) for value in p0_int)
    assert expansion.get(Q(1)) == p0
    selector = cd.smallest_positive_root_selector(p0_int)
    simple = selector_simple(p0, selector)
    if not simple:
        return (False, 1, 0, 0, 0)

    strict = sorted((base for base in expansion if base < 1), reverse=True)
    active_base = None
    active_poly = None
    inactive = 0
    for base in strict:
        poly = expansion[base]
        if vanishes_at_selector(p0, poly, selector):
            inactive += 1
            continue
        active_base = base
        active_poly = poly
        break

    reconstruction = 0
    for step in (0, 1, 2, 4):
        for z in (Q(0), Q(1, 5), Q(2, 3)):
            assert evaluate_expansion(expansion, step, z) == direct_det(levels, layers, step, z)
            reconstruction += 1

    sign_checks = 0
    if active_base is not None and sign_check:
        assert active_poly is not None
        sign_checks = active_sign(p0, active_poly, p0_int)

    return (True, 1, inactive, reconstruction, sign_checks)


def exhaustive_regression():
    simple_samples = multiple_root_boundaries = inactive_layers = reconstruction = sign_checks = 0

    catalog2 = [(), (Q(1, 4),), (Q(1, 2),), (Q(1, 2), Q(1, 2))]
    cells2 = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for index, assignment in enumerate(product(catalog2, repeat=4)):
        result = validate(2, branches_from_assignment(cells2, assignment), sign_check=True)
        if result is None:
            continue
        if result[0]:
            simple_samples += 1
            inactive_layers += result[2]
            reconstruction += result[3]
            sign_checks += result[4]
        else:
            multiple_root_boundaries += 1

    catalog3 = [(), (Q(1, 3),), (Q(1, 2),)]
    cells3 = [(i, j) for i in range(3) for j in range(3)]
    for index, assignment in enumerate(product(catalog3, repeat=9)):
        result = validate(
            3,
            branches_from_assignment(cells3, assignment),
            sign_check=(index % 31 == 0),
        )
        if result is None:
            continue
        if result[0]:
            simple_samples += 1
            inactive_layers += result[2]
            reconstruction += result[3]
            sign_checks += result[4]
        else:
            multiple_root_boundaries += 1

    return simple_samples, multiple_root_boundaries, inactive_layers, reconstruction, sign_checks


def special_examples():
    checks = 0
    # Feed-forward strict edge is completely root-inactive.
    K = ((2, 0), (0, 1))
    levels = (Q(1), Q(1, 2))
    layers = (K, ((0, 1), (0, 0)))
    expansion = rsp.determinant_exponential_expansion(levels, layers)
    assert set(expansion) == {Q(1)}
    checks += 1

    # Closed excursion gives active base ab=1/4 and beta=1/2.
    levels = (Q(1), Q(1, 2))
    layers = (K, ((0, 1), (1, 0)))
    # Both cross edges at the same layer produce determinant base (1/2)^2.
    expansion = rsp.determinant_exponential_expansion(levels, layers)
    assert Q(1, 4) in expansion
    p0 = tuple(Q(value) for value in cd.criticality_polynomial(K))
    g = expansion[Q(1, 4)]
    z = Q(1, 2)
    beta = peval(g, z) / (z * peval(derivative(p0), z))
    assert beta == Q(1, 2)
    checks += 2

    # Tied winner: smallest positive root is multiple; ordinary response forbidden.
    tied = ((1, 0), (0, 1))
    p_tied_int = cd.criticality_polynomial(tied)
    selector = cd.smallest_positive_root_selector(p_tied_int)
    assert selector.exact_root == 1
    assert not selector_simple(tuple(Q(v) for v in p_tied_int), selector)
    checks += 2
    return checks


def main() -> int:
    simple, multiple, inactive, reconstruction, signs = exhaustive_regression()
    special = special_examples()
    assert simple > 100
    assert multiple > 0
    print("BRC unique-winner root-active characteristic jet checker: PASS")
    print(f"reducible_simple_root_samples={simple}")
    print(f"multiple_root_boundaries={multiple}")
    print(f"root_inactive_strict_layers={inactive}")
    print(f"exact_characteristic_reconstruction_checks={reconstruction}")
    print(f"sampled_positive_response_sign_checks={signs}")
    print(f"special_checks={special}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
