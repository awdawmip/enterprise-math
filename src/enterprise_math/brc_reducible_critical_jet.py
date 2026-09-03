"""Exact reducible-critical powered gauges and characteristic/Newton jets.

Foundation extraction of WBRC-T49..T51.  This module keeps finite positive-
rational branch data exact and reuses the existing smallest-positive-root
selector.  It does not implement floating eigenvalue or full Puiseux solvers.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations
from typing import Sequence, TypeAlias

from .brc_critical_degeneracy import (
    CriticalDegeneracyAnalysis,
    CriticalRootSelector,
    _p_gcd,
    _root_count,
    _sturm_sequence,
    criticality_polynomial,
    smallest_positive_root_selector,
)
from .brc_critical_ratio_jet import PoweredCriticalGauge, powered_critical_gauge

RationalInput: TypeAlias = int | Fraction
ExplicitBranch: TypeAlias = tuple[int, int, RationalInput]
IntMatrix: TypeAlias = tuple[tuple[int, ...], ...]
Poly: TypeAlias = tuple[Fraction, ...]


def _sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j]
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def _trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def _p_add(left: Poly, right: Poly) -> Poly:
    n = max(len(left), len(right))
    return _trim(tuple(
        (left[i] if i < len(left) else Fraction(0, 1))
        + (right[i] if i < len(right) else Fraction(0, 1))
        for i in range(n)
    ))


def _p_mul(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0, 1) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return _trim(tuple(out))


def _p_eval(poly: Poly, value: Fraction) -> Fraction:
    result = Fraction(0, 1)
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def _derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (Fraction(0, 1),)
    return _trim(tuple(Fraction(i, 1) * poly[i] for i in range(1, len(poly))))


def _normalize_branches(state_count: int, branches: Sequence[ExplicitBranch]) -> tuple[tuple[int, int, Fraction], ...]:
    if isinstance(state_count, bool) or not isinstance(state_count, int) or state_count <= 0:
        raise ValueError("state_count must be a positive integer")
    out: list[tuple[int, int, Fraction]] = []
    for source, target, raw in branches:
        if isinstance(source, bool) or isinstance(target, bool):
            raise TypeError("branch endpoints must be integer indices")
        if not (
            isinstance(source, int)
            and isinstance(target, int)
            and 0 <= source < state_count
            and 0 <= target < state_count
        ):
            raise ValueError("branch endpoint out of range")
        if isinstance(raw, bool) or not isinstance(raw, (int, Fraction)):
            raise TypeError("branch weights must be int or Fraction")
        weight = Fraction(raw)
        if weight <= 0:
            raise ValueError("branch weights must be positive")
        out.append((source, target, weight))
    return tuple(out)


def _cells(branches: Sequence[tuple[int, int, Fraction]]) -> dict[tuple[int, int], tuple[Fraction, ...]]:
    values: dict[tuple[int, int], list[Fraction]] = defaultdict(list)
    for source, target, weight in branches:
        values[(source, target)].append(weight)
    return {cell: tuple(weights) for cell, weights in values.items()}


def _simple_cycles(weight: Sequence[Sequence[Fraction]]) -> tuple[tuple[int, ...], ...]:
    n = len(weight)
    out: list[tuple[int, ...]] = []
    for length in range(1, n + 1):
        for subset in combinations(range(n), length):
            first = subset[0]
            for perm in permutations(subset):
                if perm[0] != first:
                    continue
                if all(weight[perm[i]][perm[(i + 1) % length]] > 0 for i in range(length)):
                    out.append(tuple(perm))
    return tuple(out)


def _cycle_product(cycle: Sequence[int], weight: Sequence[Sequence[Fraction]]) -> Fraction:
    value = Fraction(1, 1)
    for index, source in enumerate(cycle):
        value *= weight[source][cycle[(index + 1) % len(cycle)]]
    return value


def _critical_classes(state_count: int, components: Sequence[Sequence[int]]) -> tuple[tuple[tuple[int, ...], ...], tuple[int, ...]]:
    classes: list[tuple[int, ...]] = []
    class_of = [-1 for _ in range(state_count)]
    for component in components:
        index = len(classes)
        normalized = tuple(sorted(component))
        classes.append(normalized)
        for vertex in normalized:
            class_of[vertex] = index
    for vertex in range(state_count):
        if class_of[vertex] < 0:
            class_of[vertex] = len(classes)
            classes.append((vertex,))
    return tuple(classes), tuple(class_of)


def _max_simple_path_products(weight: Sequence[Sequence[Fraction]]) -> tuple[Fraction, ...]:
    n = len(weight)
    output: list[Fraction] = []
    for start in range(n):
        best = Fraction(1, 1)

        def visit(current: int, seen: frozenset[int], value: Fraction) -> None:
            nonlocal best
            if value > best:
                best = value
            for target in range(n):
                edge = weight[current][target]
                if edge <= 0 or target in seen:
                    continue
                visit(target, seen | {target}, value * edge)

        visit(start, frozenset({start}), Fraction(1, 1))
        output.append(best)
    return tuple(output)


@dataclass(frozen=True)
class PoweredBranchRatio:
    source: int
    target: int
    ratio: Fraction
    critical_dominant: bool


@dataclass(frozen=True)
class GlobalStrictPoweredGauge:
    base: PoweredCriticalGauge
    classes: tuple[tuple[int, ...], ...]
    class_of: tuple[int, ...]
    potentials: tuple[Fraction, ...]
    contraction_rate: Fraction
    branch_ratios: tuple[PoweredBranchRatio, ...]

    @property
    def critical_matrix(self) -> IntMatrix:
        return self.base.analysis.critical_matrix


@dataclass(frozen=True)
class CharacteristicJetLayer:
    base: Fraction
    polynomial: tuple[int, ...]


@dataclass(frozen=True)
class CharacteristicRatioJetState:
    critical_matrix: IntMatrix
    root: CriticalRootSelector
    layers: tuple[CharacteristicJetLayer, ...]

    @property
    def p0(self) -> tuple[int, ...]:
        for layer in self.layers:
            if layer.base == 1:
                return layer.polynomial
        raise AssertionError("characteristic jet lost base-one layer")


@dataclass(frozen=True)
class RootActiveLayer:
    base: Fraction
    polynomial: tuple[int, ...]
    root: CriticalRootSelector


@dataclass(frozen=True)
class NewtonCandidateScale:
    base: Fraction
    degree: int
    contact_order: int
    polynomial: tuple[int, ...]


@dataclass(frozen=True)
class NewtonScaleState:
    root: CriticalRootSelector
    root_multiplicity: int
    representative_base: Fraction
    representative_degree: int
    candidates: tuple[NewtonCandidateScale, ...]
    first_edge_layers: tuple[NewtonCandidateScale, ...]
    rational_edge_polynomial: tuple[Fraction, ...] | None


def global_strict_powered_gauge(state_count: int, branches: Sequence[ExplicitBranch]) -> GlobalStrictPoweredGauge:
    normalized = _normalize_branches(state_count, branches)
    base = powered_critical_gauge(state_count, normalized)
    analysis = base.analysis
    h0 = [Fraction(1, 1) for _ in range(state_count)]
    for vertex, value in base.potentials:
        h0[vertex] = value
    classes, class_of = _critical_classes(state_count, base.components)
    quotient_size = len(classes)
    quotient = [[Fraction(0, 1) for _ in range(quotient_size)] for _ in range(quotient_size)]
    cell_map = _cells(normalized)
    critical_edges = set(analysis.critical_edges)
    r0 = analysis.reference_cycle_length
    q0 = analysis.reference_cycle_product

    for source, target, weight in normalized:
        dominant_critical = (
            (source, target) in critical_edges
            and weight == max(cell_map[(source, target)])
        )
        raw = (weight**r0) * h0[target] / (q0 * h0[source])
        if dominant_critical:
            if raw != 1 or class_of[source] != class_of[target]:
                raise AssertionError("critical dominant branch lost equality class")
            continue
        a, b = class_of[source], class_of[target]
        if raw > quotient[a][b]:
            quotient[a][b] = raw

    quotient_matrix = tuple(tuple(row) for row in quotient)
    cycles = _simple_cycles(quotient_matrix)
    for cycle in cycles:
        product_value = _cycle_product(cycle, quotient_matrix)
        if not Fraction(0, 1) < product_value < 1:
            raise AssertionError("strict quotient cycle is not subunit")

    if cycles:
        epsilon = min(
            (Fraction(1, 1) - _cycle_product(cycle, quotient_matrix)) / (2 * len(cycle))
            for cycle in cycles
        )
        contraction = Fraction(1, 1) - epsilon
    else:
        contraction = Fraction(1, 2)
    scaled = tuple(
        tuple(value / contraction if value else Fraction(0, 1) for value in row)
        for row in quotient_matrix
    )
    class_scale = _max_simple_path_products(scaled)
    for a in range(quotient_size):
        for b in range(quotient_size):
            if quotient_matrix[a][b]:
                if not quotient_matrix[a][b] * class_scale[b] <= contraction * class_scale[a] < class_scale[a]:
                    raise AssertionError("quotient strict-potential inequality failed")

    potentials = tuple(
        h0[vertex] * class_scale[class_of[vertex]]
        for vertex in range(state_count)
    )
    ratios: list[PoweredBranchRatio] = []
    for source, target, weight in normalized:
        dominant_critical = (
            (source, target) in critical_edges
            and weight == max(cell_map[(source, target)])
        )
        ratio = (weight**r0) * potentials[target] / (q0 * potentials[source])
        if (ratio == 1) != dominant_critical:
            raise AssertionError("global strict powered ratio equality classification failed")
        if not dominant_critical and not Fraction(0, 1) < ratio < 1:
            raise AssertionError("global strict powered ratio did not become strict")
        ratios.append(PoweredBranchRatio(source, target, ratio, dominant_critical))

    return GlobalStrictPoweredGauge(
        base=base,
        classes=classes,
        class_of=class_of,
        potentials=potentials,
        contraction_rate=contraction,
        branch_ratios=tuple(ratios),
    )


def _ratio_layers(gauge: GlobalStrictPoweredGauge) -> tuple[tuple[Fraction, ...], tuple[IntMatrix, ...]]:
    n = gauge.base.analysis.state_count
    ratios = tuple(sorted({record.ratio for record in gauge.branch_ratios}, reverse=True))
    layers: list[IntMatrix] = []
    for ratio in ratios:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for record in gauge.branch_ratios:
            if record.ratio == ratio:
                matrix[record.source][record.target] += 1
        layers.append(tuple(tuple(row) for row in matrix))
    if not layers or layers[0] != gauge.critical_matrix:
        raise AssertionError("reducible ratio representative lost K as dominant layer")
    return ratios, tuple(layers)


def _determinant_exponential_layers(ratios: tuple[Fraction, ...], layers: tuple[IntMatrix, ...]) -> tuple[CharacteristicJetLayer, ...]:
    n = len(layers[0])
    total: dict[Fraction, Poly] = {}
    for perm in permutations(range(n)):
        states: dict[Fraction, Poly] = {Fraction(1, 1): (Fraction(_sign(tuple(perm)), 1),)}
        for row, col in enumerate(perm):
            factors: dict[Fraction, Poly] = {}
            baseline = (
                (Fraction(1, 1), Fraction(-layers[0][row][col], 1))
                if row == col
                else (Fraction(0, 1), Fraction(-layers[0][row][col], 1))
            )
            if baseline != (Fraction(0, 1),):
                factors[Fraction(1, 1)] = _trim(baseline)
            for ratio, layer in zip(ratios[1:], layers[1:]):
                if layer[row][col]:
                    factors[ratio] = (Fraction(0, 1), Fraction(-layer[row][col], 1))
            if not factors:
                states = {}
                break
            next_states: dict[Fraction, Poly] = {}
            for base_a, poly_a in states.items():
                for base_b, poly_b in factors.items():
                    base_value = base_a * base_b
                    poly_value = _p_mul(poly_a, poly_b)
                    next_states[base_value] = _p_add(
                        next_states.get(base_value, (Fraction(0, 1),)),
                        poly_value,
                    )
            states = next_states
        for base_value, poly_value in states.items():
            total[base_value] = _p_add(
                total.get(base_value, (Fraction(0, 1),)),
                poly_value,
            )
    output: list[CharacteristicJetLayer] = []
    for base_value in sorted(total, reverse=True):
        poly = total[base_value]
        if poly == (Fraction(0, 1),):
            continue
        if any(value.denominator != 1 for value in poly):
            raise AssertionError("characteristic layer polynomial lost integer coefficients")
        output.append(CharacteristicJetLayer(base_value, tuple(value.numerator for value in poly)))
    return tuple(output)


def characteristic_ratio_jet(state_count: int, branches: Sequence[ExplicitBranch]) -> CharacteristicRatioJetState:
    gauge = global_strict_powered_gauge(state_count, branches)
    ratios, layers = _ratio_layers(gauge)
    characteristic_layers = _determinant_exponential_layers(ratios, layers)
    p0 = criticality_polynomial(gauge.critical_matrix)
    if not characteristic_layers or characteristic_layers[0].base != 1 or characteristic_layers[0].polynomial != p0:
        raise AssertionError("characteristic jet base-one layer disagrees with p_K")
    root = smallest_positive_root_selector(p0)
    return CharacteristicRatioJetState(gauge.critical_matrix, root, characteristic_layers)


def _root_vanishes(p0: tuple[int, ...], poly: tuple[int, ...], root: CriticalRootSelector) -> bool:
    rational_poly = tuple(Fraction(value, 1) for value in poly)
    if rational_poly == (Fraction(0, 1),):
        return True
    if root.is_rational:
        assert root.exact_root is not None
        return _p_eval(rational_poly, root.exact_root) == 0
    gcd = _p_gcd(tuple(Fraction(value, 1) for value in p0), rational_poly)
    if len(gcd) <= 1:
        return False
    sequence = _sturm_sequence(gcd)
    return _root_count(sequence, root.lower, root.upper) > 0


def _root_order(p0: tuple[int, ...], poly: tuple[int, ...], root: CriticalRootSelector) -> int:
    current = tuple(Fraction(value, 1) for value in poly)
    order = 0
    while current != (Fraction(0, 1),):
        integer_current = tuple(value.numerator for value in current) if all(value.denominator == 1 for value in current) else None
        if integer_current is None:
            raise AssertionError("contact polynomial lost integer coefficients")
        if not _root_vanishes(p0, integer_current, root):
            return order
        current = _derivative(current)
        order += 1
    return 10**9


def first_root_active_layer(state: CharacteristicRatioJetState) -> RootActiveLayer | None:
    p0 = state.p0
    derivative = _derivative(tuple(Fraction(value, 1) for value in p0))
    derivative_int = tuple(value.numerator for value in derivative)
    if _root_vanishes(p0, derivative_int, state.root):
        raise ValueError("selected critical root is multiple; use first_newton_edge_state")
    for layer in state.layers:
        if layer.base == 1:
            continue
        if not _root_vanishes(p0, layer.polynomial, state.root):
            return RootActiveLayer(layer.base, layer.polynomial, state.root)
    return None


def _compare_scale(left: tuple[Fraction, int], right: tuple[Fraction, int]) -> int:
    eta_left, degree_left = left
    eta_right, degree_right = right
    lhs = eta_left**degree_right
    rhs = eta_right**degree_left
    return (lhs > rhs) - (lhs < rhs)


def first_newton_edge_state(state: CharacteristicRatioJetState) -> NewtonScaleState:
    p0 = state.p0
    root_multiplicity = _root_order(p0, p0, state.root)
    if root_multiplicity < 2 or root_multiplicity >= 10**9:
        raise ValueError("selected critical root is not a finite multiple root")

    candidates: list[NewtonCandidateScale] = []
    for layer in state.layers:
        if layer.base == 1:
            continue
        contact = _root_order(p0, layer.polynomial, state.root)
        if contact < root_multiplicity:
            candidates.append(
                NewtonCandidateScale(
                    base=layer.base,
                    degree=root_multiplicity - contact,
                    contact_order=contact,
                    polynomial=layer.polynomial,
                )
            )
    if not candidates:
        raise ValueError("no strict layer enters the first Newton edge")

    representative = candidates[0]
    for candidate in candidates[1:]:
        if _compare_scale((candidate.base, candidate.degree), (representative.base, representative.degree)) > 0:
            representative = candidate
    edge_layers = tuple(
        candidate
        for candidate in candidates
        if _compare_scale((candidate.base, candidate.degree), (representative.base, representative.degree)) == 0
    )

    edge_poly: tuple[Fraction, ...] | None = None
    if state.root.is_rational:
        assert state.root.exact_root is not None
        z = state.root.exact_root
        coefficients = [Fraction(0, 1) for _ in range(root_multiplicity + 1)]
        p0_fraction = tuple(Fraction(value, 1) for value in p0)
        current = p0_fraction
        for _ in range(root_multiplicity):
            current = _derivative(current)
        coefficients[root_multiplicity] = _p_eval(current, z) / 1
        # current is r-th derivative; divide by r! via product.
        factorial_value = 1
        for value in range(2, root_multiplicity + 1):
            factorial_value *= value
        coefficients[root_multiplicity] /= factorial_value
        for candidate in edge_layers:
            poly = tuple(Fraction(value, 1) for value in candidate.polynomial)
            current = poly
            for _ in range(candidate.contact_order):
                current = _derivative(current)
            factorial_contact = 1
            for value in range(2, candidate.contact_order + 1):
                factorial_contact *= value
            coefficient = _p_eval(current, z) / factorial_contact
            coefficients[candidate.contact_order] += coefficient
        edge_poly = _trim(tuple(coefficients))

    return NewtonScaleState(
        root=state.root,
        root_multiplicity=root_multiplicity,
        representative_base=representative.base,
        representative_degree=representative.degree,
        candidates=tuple(candidates),
        first_edge_layers=edge_layers,
        rational_edge_polynomial=edge_poly,
    )
