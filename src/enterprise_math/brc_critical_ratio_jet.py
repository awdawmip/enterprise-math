"""Exact powered critical gauges and finite branch-ratio jets for Weighted-BRC.

Foundation extraction of WBRC-T45..T48.  All accumulation is exact rational /
integer arithmetic.  The module deliberately exposes polynomial/root-selector
response states instead of floating Perron eigenvalues or eigenvectors.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
from typing import Sequence, TypeAlias

from .brc_critical_degeneracy import (
    CriticalDegeneracyAnalysis,
    CriticalRootSelector,
    critical_degeneracy_analysis,
    criticality_polynomial,
    smallest_positive_root_selector,
)

RationalInput: TypeAlias = int | Fraction
ExplicitBranch: TypeAlias = tuple[int, int, RationalInput]
IntMatrix: TypeAlias = tuple[tuple[int, ...], ...]
RationalMatrix: TypeAlias = tuple[tuple[Fraction, ...], ...]


def _sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j]
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def _irreducible(matrix: IntMatrix) -> bool:
    n = len(matrix)
    reach = [[matrix[i][j] > 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        reach[i][i] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    return all(reach[i][j] for i in range(n) for j in range(n))


def _critical_components(n: int, edges: Sequence[tuple[int, int]]) -> tuple[tuple[int, ...], ...]:
    states = sorted({state for edge in edges for state in edge})
    edge_set = set(edges)
    reach = [[False for _ in range(n)] for _ in range(n)]
    for state in range(n):
        reach[state][state] = True
    for source, target in edge_set:
        reach[source][target] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    remaining = set(states)
    out: list[tuple[int, ...]] = []
    while remaining:
        root = min(remaining)
        component = tuple(sorted(v for v in remaining if reach[root][v] and reach[v][root]))
        out.append(component)
        remaining.difference_update(component)
    return tuple(out)


def _normalized_branches(state_count: int, branches: Sequence[ExplicitBranch]) -> tuple[tuple[int, int, Fraction], ...]:
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


def _cell_map(branches: Sequence[tuple[int, int, Fraction]]) -> dict[tuple[int, int], tuple[Fraction, ...]]:
    cells: dict[tuple[int, int], list[Fraction]] = defaultdict(list)
    for source, target, weight in branches:
        cells[(source, target)].append(weight)
    return {cell: tuple(values) for cell, values in cells.items()}


@dataclass(frozen=True)
class PoweredCriticalGauge:
    analysis: CriticalDegeneracyAnalysis
    components: tuple[tuple[int, ...], ...]
    roots: tuple[tuple[int, int], ...]
    potentials: tuple[tuple[int, Fraction], ...]

    @property
    def potential_map(self) -> dict[int, Fraction]:
        return dict(self.potentials)

    @property
    def root_map(self) -> dict[int, int]:
        return dict(self.roots)


@dataclass(frozen=True)
class CriticalRatioJet:
    analysis: CriticalDegeneracyAnalysis
    ratios: tuple[Fraction, ...]
    layers: tuple[IntMatrix, ...]

    def moment(self, order: int) -> RationalMatrix:
        if isinstance(order, bool) or not isinstance(order, int) or order < 0:
            raise ValueError("order must be a non-negative integer")
        n = self.analysis.state_count
        return tuple(
            tuple(
                sum(
                    ((ratio**order) * self.layers[index][i][j] for index, ratio in enumerate(self.ratios)),
                    Fraction(0, 1),
                )
                for j in range(n)
            )
            for i in range(n)
        )


@dataclass(frozen=True)
class FullPoweredRatioJet:
    gauge: PoweredCriticalGauge
    ratios: tuple[Fraction, ...]
    layers: tuple[IntMatrix, ...]

    @property
    def critical_matrix(self) -> IntMatrix:
        return self.layers[0]

    def normalized_moment(self, powered_step: int) -> RationalMatrix:
        if isinstance(powered_step, bool) or not isinstance(powered_step, int) or powered_step < 0:
            raise ValueError("powered_step must be a non-negative integer")
        n = self.gauge.analysis.state_count
        return tuple(
            tuple(
                sum(
                    ((ratio**powered_step) * self.layers[index][i][j] for index, ratio in enumerate(self.ratios)),
                    Fraction(0, 1),
                )
                for j in range(n)
            )
            for i in range(n)
        )


@dataclass(frozen=True)
class CriticalRatioResponseState:
    critical_matrix: IntMatrix
    first_layer: IntMatrix
    p0: tuple[int, ...]
    p1: tuple[int, ...]
    root: CriticalRootSelector
    ratio: Fraction
    remainder_ratio: Fraction


def powered_critical_gauge(state_count: int, branches: Sequence[ExplicitBranch]) -> PoweredCriticalGauge:
    normalized = _normalized_branches(state_count, branches)
    analysis = critical_degeneracy_analysis(state_count, normalized)
    r0 = analysis.reference_cycle_length
    q0 = analysis.reference_cycle_product
    dominant = analysis.dominant_mass_matrix
    critical = set(analysis.critical_edges)
    components = _critical_components(state_count, analysis.critical_edges)

    h: dict[int, Fraction] = {}
    roots: dict[int, int] = {}
    for component in components:
        root = min(component)
        h[root] = Fraction(1, 1)
        for vertex in component:
            roots[vertex] = root
        changed = True
        while changed:
            changed = False
            for source, target in sorted(critical):
                if source not in component or target not in component or source not in h:
                    continue
                candidate = q0 * h[source] / (dominant[source][target] ** r0)
                if target not in h:
                    h[target] = candidate
                    changed = True
                elif h[target] != candidate:
                    raise AssertionError("powered critical potential lost path independence")
        if any(vertex not in h for vertex in component):
            raise AssertionError("powered critical potential did not reach the whole SCC")

    for source, target in critical:
        if dominant[source][target] ** r0 * h[target] != q0 * h[source]:
            raise AssertionError("powered critical edge equation failed")

    return PoweredCriticalGauge(
        analysis=analysis,
        components=components,
        roots=tuple(sorted(roots.items())),
        potentials=tuple(sorted(h.items())),
    )


def critical_ratio_jet(state_count: int, branches: Sequence[ExplicitBranch]) -> CriticalRatioJet:
    normalized = _normalized_branches(state_count, branches)
    analysis = critical_degeneracy_analysis(state_count, normalized)
    cells = _cell_map(normalized)
    histograms: dict[tuple[int, int], dict[Fraction, int]] = {}
    ratio_set: set[Fraction] = set()
    for edge in analysis.critical_edges:
        weights = cells[edge]
        maximum = max(weights)
        hist: dict[Fraction, int] = {}
        for weight in weights:
            ratio = weight / maximum
            hist[ratio] = hist.get(ratio, 0) + 1
            ratio_set.add(ratio)
        histograms[edge] = hist
    ratios = tuple(sorted(ratio_set, reverse=True))
    if not ratios or ratios[0] != 1:
        raise AssertionError("critical ratio jet lost dominant layer")
    layers: list[IntMatrix] = []
    for ratio in ratios:
        matrix = [[0 for _ in range(state_count)] for _ in range(state_count)]
        for (source, target), hist in histograms.items():
            matrix[source][target] = hist.get(ratio, 0)
        layers.append(tuple(tuple(row) for row in matrix))
    if layers[0] != analysis.critical_matrix:
        raise AssertionError("critical ratio dominant layer disagrees with K")
    return CriticalRatioJet(analysis, ratios, tuple(layers))


def full_powered_ratio_jet(state_count: int, branches: Sequence[ExplicitBranch]) -> FullPoweredRatioJet:
    normalized = _normalized_branches(state_count, branches)
    gauge = powered_critical_gauge(state_count, normalized)
    analysis = gauge.analysis
    K = analysis.critical_matrix
    if not _irreducible(K):
        raise ValueError("full powered ratio jet currently requires irreducible critical K")
    h = gauge.potential_map
    if set(h) != set(range(state_count)):
        raise ValueError("irreducible full jet requires a powered potential on every state")
    r0 = analysis.reference_cycle_length
    q0 = analysis.reference_cycle_product
    critical = set(analysis.critical_edges)
    cells = _cell_map(normalized)

    branch_ratios: list[tuple[int, int, Fraction]] = []
    for source, target, weight in normalized:
        ratio = (weight**r0) * h[target] / (q0 * h[source])
        if not 0 < ratio <= 1:
            raise AssertionError("powered branch ratio left (0,1]")
        dominant_critical = (
            (source, target) in critical
            and weight == max(cells[(source, target)])
        )
        if (ratio == 1) != dominant_critical:
            raise AssertionError("powered ratio one did not match critical dominant branch")
        branch_ratios.append((source, target, ratio))

    ratios = tuple(sorted({ratio for _, _, ratio in branch_ratios}, reverse=True))
    layers: list[IntMatrix] = []
    for ratio in ratios:
        matrix = [[0 for _ in range(state_count)] for _ in range(state_count)]
        for source, target, branch_ratio in branch_ratios:
            if branch_ratio == ratio:
                matrix[source][target] += 1
        layers.append(tuple(tuple(row) for row in matrix))
    if not layers or layers[0] != K:
        raise AssertionError("full powered jet dominant layer disagrees with K")
    return FullPoweredRatioJet(gauge, ratios, tuple(layers))


def _determinant_first_derivative(K: IntMatrix, L: IntMatrix) -> tuple[int, ...]:
    n = len(K)
    max_degree = n
    out = [0 for _ in range(max_degree + 1)]
    for perm in permutations(range(n)):
        sign = _sign(tuple(perm))
        for chosen in range(n):
            row = chosen
            col = perm[chosen]
            if L[row][col] == 0:
                continue
            factors: list[tuple[int, int]] = []  # constant, z coefficient
            alive = True
            for i, j in enumerate(perm):
                if i == chosen:
                    factors.append((0, -L[i][j]))
                elif i == j:
                    factors.append((1, -K[i][j]))
                elif K[i][j]:
                    factors.append((0, -K[i][j]))
                else:
                    alive = False
                    break
            if not alive:
                continue
            poly = [sign]
            for constant, linear in factors:
                nxt = [0 for _ in range(len(poly) + 1)]
                for degree, value in enumerate(poly):
                    nxt[degree] += value * constant
                    nxt[degree + 1] += value * linear
                poly = nxt
            for degree, value in enumerate(poly):
                out[degree] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def critical_ratio_first_response(jet: FullPoweredRatioJet | CriticalRatioJet) -> CriticalRatioResponseState:
    if len(jet.ratios) < 2:
        raise ValueError("ratio jet has no strict layer")
    K = jet.layers[0]
    if not _irreducible(K):
        raise ValueError("first spectral response currently requires irreducible K")
    L1 = jet.layers[1]
    p0 = criticality_polynomial(K)
    p1 = _determinant_first_derivative(K, L1)
    root = smallest_positive_root_selector(p0)
    ratio = jet.ratios[1]
    second = jet.ratios[2] if len(jet.ratios) >= 3 else Fraction(0, 1)
    remainder = max(second, ratio * ratio)
    if not 0 <= remainder < ratio < 1:
        raise AssertionError("invalid ratio-jet response ordering")
    return CriticalRatioResponseState(K, L1, p0, p1, root, ratio, remainder)
