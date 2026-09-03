#!/usr/bin/env python3
"""Exact first-Newton-edge checker for multiple critical Perron roots."""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb, factorial

import brc_critical_ratio_spectral_response_check as rsp
import brc_global_powered_strict_gauge_reducible_check as red
import brc_unique_winner_root_active_characteristic_jet_check as win
from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
Branch = tuple[int, int, Fraction]
Poly = tuple[Fraction, ...]


def branches_from_assignment(cells, assignment) -> tuple[Branch, ...]:
    return tuple((u, v, q) for (u, v), weights in zip(cells, assignment) for q in weights)


def peval(poly: Poly, x: Fraction) -> Fraction:
    value = Q(0)
    for coefficient in reversed(poly):
        value = value * x + coefficient
    return value


def derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (Q(0),)
    values = tuple(Q(i) * poly[i] for i in range(1, len(poly)))
    while len(values) > 1 and values[-1] == 0:
        values = values[:-1]
    return values


def vanishes(p0: Poly, poly: Poly, selector) -> bool:
    return win.vanishes_at_selector(p0, poly, selector)


def vanish_order(p0: Poly, poly: Poly, selector) -> int:
    current = poly
    order = 0
    while current != (Q(0),) and vanishes(p0, current, selector):
        current = derivative(current)
        order += 1
    if current == (Q(0),):
        return 10**6
    return order


def compare_scales(left: tuple[Fraction, int], right: tuple[Fraction, int]) -> int:
    eta1, d1 = left
    eta2, d2 = right
    lhs = eta1**d2
    rhs = eta2**d1
    return (lhs > rhs) - (lhs < rhs)


def same_scale(left: tuple[Fraction, int], right: tuple[Fraction, int]) -> bool:
    return compare_scales(left, right) == 0


def max_scale(candidates: list[tuple[Fraction, int]]) -> tuple[Fraction, int]:
    best = candidates[0]
    for candidate in candidates[1:]:
        if compare_scales(candidate, best) > 0:
            best = candidate
    return best


def taylor_coefficient(poly: Poly, root: Fraction, order: int) -> Fraction:
    return sum(
        (poly[j] * comb(j, order) * (root ** (j - order)) for j in range(order, len(poly))),
        Q(0),
    )


def validate_multiple_sample(n: int, branches: tuple[Branch, ...]):
    try:
        data = red.global_strict_gauge(n, branches)
    except ValueError:
        return None
    gauge, _, _, _, records, _, _, _ = data
    K = gauge.analysis.critical_matrix
    levels, layers = win.levels_layers(n, records)
    expansion = rsp.determinant_exponential_expansion(levels, layers)
    p0_int = cd.criticality_polynomial(K)
    p0 = tuple(Q(value) for value in p0_int)
    selector = cd.smallest_positive_root_selector(p0_int)
    if win.selector_simple(p0, selector):
        return None

    r = vanish_order(p0, p0, selector)
    assert 2 <= r < 10**6
    candidates: list[tuple[Fraction, int, Poly, int]] = []
    contact_checks = 0
    for eta, poly in expansion.items():
        if eta == 1:
            continue
        q = vanish_order(p0, poly, selector)
        if q < r:
            candidates.append((eta, r - q, poly, q))
        contact_checks += 1

    if not candidates:
        return (r, 0, 0, contact_checks, 0, 0)

    best = max_scale([(eta, d) for eta, d, _, _ in candidates])
    edge = [record for record in candidates if same_scale((record[0], record[1]), best)]
    assert edge

    dominance_checks = 0
    # Every strict local Taylor term with order < r has candidate scale <= best.
    for eta, poly in expansion.items():
        if eta == 1:
            continue
        current = poly
        for k in range(r):
            if not vanishes(p0, current, selector):
                assert compare_scales((eta, r - k), best) <= 0
                dominance_checks += 1
            current = derivative(current)

    rational_edge_checks = 0
    if selector.is_rational:
        assert selector.exact_root is not None
        root = selector.exact_root
        edge_coeff: dict[int, Fraction] = {r: taylor_coefficient(p0, root, r)}
        assert edge_coeff[r] != 0
        for eta, _, poly, q in edge:
            value = taylor_coefficient(poly, root, q)
            assert value != 0
            edge_coeff[q] = edge_coeff.get(q, Q(0)) + value
        assert edge_coeff[r] != 0
        rational_edge_checks += len(edge_coeff)

        # Verify exact survival rule term-by-term.  Let best=(eta0,d0), so
        # theta^d0=eta0.  A local term eta^s x^k survives exactly when
        # eta*theta^k = theta^r.
        eta0, d0 = best
        for eta, poly in expansion.items():
            current = poly
            for k in range(0, max(r + 1, len(poly))):
                value = taylor_coefficient(poly, root, k) if k < len(poly) else Q(0)
                if value == 0:
                    continue
                if eta == 1:
                    equality = (k == r)
                elif k < r:
                    equality = eta**d0 == eta0 ** (r - k)
                else:
                    equality = False
                if equality:
                    assert k == r or any(
                        e == eta and q == k and same_scale((e, d), best)
                        for e, d, _, q in edge
                    )
                rational_edge_checks += 1

    return (r, len(candidates), len(edge), contact_checks, dominance_checks, rational_edge_checks)


def exhaustive_regression():
    samples = contacts = dominance = rational_edges = candidate_layers = edge_layers = 0
    multiplicities: dict[int, int] = {}

    catalog2 = [(), (Q(1, 4),), (Q(1, 2),), (Q(1, 2), Q(1, 2))]
    cells2 = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for assignment in product(catalog2, repeat=4):
        result = validate_multiple_sample(2, branches_from_assignment(cells2, assignment))
        if result is None:
            continue
        r, cand, edge, c, d, e = result
        samples += 1
        multiplicities[r] = multiplicities.get(r, 0) + 1
        candidate_layers += cand
        edge_layers += edge
        contacts += c
        dominance += d
        rational_edges += e

    catalog3 = [(), (Q(1, 3),), (Q(1, 2),)]
    cells3 = [(i, j) for i in range(3) for j in range(3)]
    for assignment in product(catalog3, repeat=9):
        result = validate_multiple_sample(3, branches_from_assignment(cells3, assignment))
        if result is None:
            continue
        r, cand, edge, c, d, e = result
        samples += 1
        multiplicities[r] = multiplicities.get(r, 0) + 1
        candidate_layers += cand
        edge_layers += edge
        contacts += c
        dominance += d
        rational_edges += e

    return samples, multiplicities, candidate_layers, edge_layers, contacts, dominance, rational_edges


def special_examples():
    checks = 0
    # r=2, q=0: tied two-block cycle, E(y)=y^2-1.
    p0 = (Q(1), Q(-2), Q(1))
    g = (Q(0), Q(0), Q(-1))
    z = Q(1)
    assert taylor_coefficient(p0, z, 2) == 1
    assert taylor_coefficient(g, z, 0) == -1
    assert compare_scales((Q(1, 16), 2), (Q(1, 4), 1)) == 0  # both theta=1/4
    checks += 3

    # r=3 directed tied cycle: eta=a^3 with a=1/2 => theta=1/2.
    p03 = (Q(1), Q(-3), Q(3), Q(-1))
    g3 = (Q(0), Q(0), Q(0), Q(-1))
    assert taylor_coefficient(p03, Q(1), 3) == -1
    assert taylor_coefficient(g3, Q(1), 0) == -1
    assert same_scale((Q(1, 8), 3), (Q(1, 2), 1))
    checks += 3

    # q=1 contact: candidate theta=eta.
    gq = (Q(0), Q(-1), Q(1))  # -z(1-z)
    assert taylor_coefficient(gq, Q(1), 0) == 0
    assert taylor_coefficient(gq, Q(1), 1) == 1
    assert same_scale((Q(1, 2), 1), (Q(1, 2), 1))
    checks += 3

    # Smaller determinant base can dominate root scale:
    # (eta1=1/2,q1=1,r=2)->theta1=1/2;
    # (eta2=1/3,q2=0,r=2)->theta2=1/sqrt(3)>1/2.
    assert compare_scales((Q(1, 3), 2), (Q(1, 2), 1)) > 0
    checks += 1
    return checks


def main() -> int:
    samples, multiplicities, candidates, edge_layers, contacts, dominance, rational_edges = exhaustive_regression()
    special = special_examples()
    assert samples > 1000
    assert multiplicities.get(2, 0) > 0
    print("BRC multiple-root first Newton-edge checker: PASS")
    print(f"multiple_root_samples={samples}")
    print(f"root_multiplicity_histogram={multiplicities}")
    print(f"candidate_layers={candidates}")
    print(f"first_edge_layers={edge_layers}")
    print(f"contact_order_checks={contacts}")
    print(f"candidate_scale_dominance_checks={dominance}")
    print(f"rational_edge_survival_checks={rational_edges}")
    print(f"special_checks={special}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
