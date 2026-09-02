"""Exact recurrent-loop observables for finite positive Weighted-BRC systems.

This layer sits above :mod:`brc_weighted_recurrent`.  It exposes the
main-backed determinant/loop-zeta, edge-response, Hessian and uniform
criticality results from PRs #1130-#1131 using only integer/Fraction arithmetic.
Logarithms remain symbolic BRC LN readouts.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import lcm
from typing import Sequence

from .brc_logarithm import LnExpr, ln
from .brc_weighted_recurrent import (
    RationalInput,
    RationalMatrix,
    RationalMatrixInput,
    RationalVector,
    finite_recurrent_mass_analysis,
)
from .exact_arithmetic import division

ExplicitEdge = tuple[int, int, RationalInput]


def _fraction(value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("value must be int or Fraction")
    return Fraction(value)


def _mass_matrix(matrix: RationalMatrixInput) -> RationalMatrix:
    rows = tuple(tuple(_fraction(value) for value in row) for row in matrix)
    n = len(rows)
    if n == 0 or any(len(row) != n for row in rows):
        raise ValueError("matrix must be nonempty and square")
    if any(value < 0 for row in rows for value in row):
        raise ValueError("mass matrix entries must be non-negative")
    return rows


def _determinant(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    rows = [list(map(Fraction, row)) for row in matrix]
    n = len(rows)
    if n == 0:
        return Fraction(1, 1)
    if any(len(row) != n for row in rows):
        raise ValueError("matrix must be square")
    sign = 1
    result = Fraction(1, 1)
    for col in range(n):
        pivot = next((row for row in range(col, n) if rows[row][col] != 0), None)
        if pivot is None:
            return Fraction(0, 1)
        if pivot != col:
            rows[col], rows[pivot] = rows[pivot], rows[col]
            sign *= -1
        pivot_value = rows[col][col]
        result *= pivot_value
        for row in range(col + 1, n):
            factor = rows[row][col] / pivot_value
            if factor != 0:
                for j in range(col, n):
                    rows[row][j] -= factor * rows[col][j]
    return sign * result


def _aggregate_edges(vertex_count: int, edges: Sequence[ExplicitEdge]) -> RationalMatrix:
    if isinstance(vertex_count, bool) or not isinstance(vertex_count, int) or vertex_count <= 0:
        raise ValueError("vertex_count must be a positive integer")
    rows = [[Fraction(0, 1) for _ in range(vertex_count)] for _ in range(vertex_count)]
    for edge in edges:
        if len(edge) != 3:
            raise ValueError("each edge must be (source,target,weight)")
        source, target, weight = edge
        if (
            isinstance(source, bool)
            or isinstance(target, bool)
            or not isinstance(source, int)
            or not isinstance(target, int)
            or not 0 <= source < vertex_count
            or not 0 <= target < vertex_count
        ):
            raise ValueError("edge endpoints must be valid vertex indices")
        value = _fraction(weight)
        if value <= 0:
            raise ValueError("explicit branch weights must be positive")
        rows[source][target] += value
    return tuple(tuple(row) for row in rows)


def recurrent_loop_zeta_ratio(matrix: RationalMatrixInput) -> Fraction:
    """Return ``det(I-W)^-1 = det(W^star)`` on the stable phase."""
    analysis = finite_recurrent_mass_analysis(matrix)
    if not analysis.stable or analysis.star is None:
        raise ValueError("finite recurrent loop-zeta is defined only on stable total mass")
    result = _determinant(analysis.star)
    if result <= 0:
        raise AssertionError("stable recurrent star must have positive determinant")
    return result


def recurrent_loop_surplus_expr(matrix: RationalMatrixInput) -> LnExpr:
    """Return symbolic BRC ``LN(Z_loop)`` without floating logarithms."""
    ratio = recurrent_loop_zeta_ratio(matrix)
    return ln(division(ratio.numerator, ratio.denominator))


def recurrent_total_susceptibility(matrix: RationalMatrixInput) -> Fraction:
    """Return ``chi=tr((I-W)^-1-I)`` exactly on the stable phase."""
    analysis = finite_recurrent_mass_analysis(matrix)
    if not analysis.stable or analysis.star is None:
        raise ValueError("susceptibility is finite only on stable total mass")
    return sum(
        (analysis.star[i][i] - 1 for i in range(len(analysis.star))),
        Fraction(0, 1),
    )


def recurrent_edge_responses(
    vertex_count: int,
    edges: Sequence[ExplicitEdge],
) -> tuple[Fraction, ...]:
    """Return exact edge-loop responses ``R_e=q_e*S[target,source]``."""
    mass = _aggregate_edges(vertex_count, edges)
    analysis = finite_recurrent_mass_analysis(mass)
    if not analysis.stable or analysis.star is None:
        raise ValueError("edge responses require a stable recurrent mass matrix")
    star = analysis.star
    return tuple(
        _fraction(weight) * star[target][source]
        for source, target, weight in edges
    )


def recurrent_response_hessian(
    vertex_count: int,
    edges: Sequence[ExplicitEdge],
) -> tuple[tuple[Fraction, ...], ...]:
    """Return the exact log-weight loop-response Hessian."""
    mass = _aggregate_edges(vertex_count, edges)
    analysis = finite_recurrent_mass_analysis(mass)
    if not analysis.stable or analysis.star is None:
        raise ValueError("response Hessian requires a stable recurrent mass matrix")
    star = analysis.star
    result: list[tuple[Fraction, ...]] = []
    normalized = tuple((a, b, _fraction(q)) for a, b, q in edges)
    for e_index, (a, b, q_e) in enumerate(normalized):
        row: list[Fraction] = []
        for f_index, (c, d, q_f) in enumerate(normalized):
            value = q_e * q_f * star[b][c] * star[d][a]
            if e_index == f_index:
                value += q_e * star[b][a]
            row.append(value)
        result.append(tuple(row))
    return tuple(result)


def _integer_matrix_multiply(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    n = len(left)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(n)) for j in range(n))
        for i in range(n)
    )


def _integer_identity(n: int) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def _integer_trace(matrix: tuple[tuple[int, ...], ...]) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


def _critical_polynomial_coefficients(
    integer_mass: tuple[tuple[int, ...], ...], denominator: int
) -> tuple[int, ...]:
    """Return coefficients of ``det(DI-tA)`` low degree first.

    Newton identities compute elementary symmetric coefficients of ``A`` using
    exact integer traces; the divisions by ``k`` are exact for integer matrices.
    """
    n = len(integer_mass)
    traces = [0]
    power = _integer_identity(n)
    for _ in range(1, n + 1):
        power = _integer_matrix_multiply(power, integer_mass)
        traces.append(_integer_trace(power))

    elementary = [1]
    for k in range(1, n + 1):
        numerator = 0
        for i in range(1, k + 1):
            numerator += (-1) ** (i - 1) * elementary[k - i] * traces[i]
        if numerator % k != 0:
            raise AssertionError("Newton identity lost exact integrality")
        elementary.append(numerator // k)

    return tuple(
        ((-1) ** k) * elementary[k] * denominator ** (n - k)
        for k in range(n + 1)
    )


@dataclass(frozen=True)
class RecurrentCriticalityPolynomial:
    """Exact integer polynomial ``p(t)=det(DI-tA)``."""

    common_denominator: int
    integer_mass_matrix: tuple[tuple[int, ...], ...]
    coefficients: tuple[int, ...]  # low degree first

    def evaluate(self, scale: RationalInput) -> Fraction:
        value = _fraction(scale)
        if value < 0:
            raise ValueError("scale must be non-negative")
        result = Fraction(0, 1)
        for coefficient in reversed(self.coefficients):
            result = result * value + coefficient
        return result

    def derivative_value(self, scale: RationalInput) -> Fraction:
        value = _fraction(scale)
        if value < 0:
            raise ValueError("scale must be non-negative")
        result = Fraction(0, 1)
        for degree in range(len(self.coefficients) - 1, 0, -1):
            result = result * value + degree * self.coefficients[degree]
        return result


def recurrent_criticality_polynomial(
    matrix: RationalMatrixInput,
) -> RecurrentCriticalityPolynomial:
    """Build the exact integer criticality polynomial ``det(DI-tA)``."""
    mass = _mass_matrix(matrix)
    denominator = 1
    for row in mass:
        for value in row:
            denominator = lcm(denominator, value.denominator)
    integer_mass = tuple(
        tuple(int(value * denominator) for value in row)
        for row in mass
    )
    return RecurrentCriticalityPolynomial(
        common_denominator=denominator,
        integer_mass_matrix=integer_mass,
        coefficients=_critical_polynomial_coefficients(integer_mass, denominator),
    )


def recurrent_critical_susceptibility(
    matrix: RationalMatrixInput,
    scale: RationalInput,
) -> Fraction:
    """Return exact ``-t p'(t)/p(t)`` at a stable rational scale."""
    t = _fraction(scale)
    if t < 0:
        raise ValueError("scale must be non-negative")
    mass = _mass_matrix(matrix)
    scaled = tuple(tuple(t * value for value in row) for row in mass)
    analysis = finite_recurrent_mass_analysis(scaled)
    if not analysis.stable:
        raise ValueError("critical susceptibility is finite only at stable scale")
    polynomial = recurrent_criticality_polynomial(mass)
    p = polynomial.evaluate(t)
    if p <= 0:
        raise AssertionError("stable scale must lie in positive determinant chamber")
    exact = -t * polynomial.derivative_value(t) / p
    if analysis.star is None:
        raise AssertionError("stable analysis lost its star")
    trace_readout = sum(
        (analysis.star[i][i] - 1 for i in range(len(analysis.star))),
        Fraction(0, 1),
    )
    if exact != trace_readout:
        raise AssertionError("polynomial and star susceptibility disagree")
    return exact


def rational_critical_scale_lower_bound(
    matrix: RationalMatrixInput,
    potential: Sequence[RationalInput],
) -> Fraction | None:
    """Return certified ``1/alpha(h)``; ``None`` denotes an infinite bound.

    The caller supplies a positive rational potential.  This function does not
    claim that the supplied ray is an optimal Collatz/Perron ray.
    """
    mass = _mass_matrix(matrix)
    h = tuple(_fraction(value) for value in potential)
    if len(h) != len(mass) or any(value <= 0 for value in h):
        raise ValueError("potential must be positive and dimension-matched")
    ratios = tuple(
        sum((mass[i][j] * h[j] for j in range(len(mass))), Fraction(0, 1)) / h[i]
        for i in range(len(mass))
    )
    alpha = max(ratios)
    if alpha == 0:
        return None
    return Fraction(1, 1) / alpha
