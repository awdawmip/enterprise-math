"""Exact stable recurrent Weighted-BRC invariant/response tools.

This module is a Foundation extraction of main-backed PRs #1130/#1131.
It reuses :mod:`brc_weighted_recurrent` for finite rational stability and star
construction.  Logarithms remain symbolic BRC LN readouts.

Scope: finite non-negative rational total-mass matrices and explicit positive
rational branch coordinates.  Signed/amplitude and infinite-state recurrence
are outside this module.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from fractions import Fraction
from typing import TypeAlias

from .brc_logarithm import LnExpr, ln
from .exact_arithmetic import division
from .brc_weighted_recurrent import (
    RationalInput,
    RationalMatrixInput,
    finite_recurrent_mass_analysis,
)

ExplicitBranch: TypeAlias = tuple[int, int, RationalInput]


def _determinant(matrix: Sequence[Sequence[Fraction | int]]) -> Fraction:
    n = len(matrix)
    if n == 0:
        return Fraction(1, 1)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be square")
    work = [[Fraction(value) for value in row] for row in matrix]
    out = Fraction(1, 1)
    sign = 1
    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col] != 0), None)
        if pivot is None:
            return Fraction(0, 1)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign *= -1
        pivot_value = work[col][col]
        out *= pivot_value
        for row in range(col + 1, n):
            factor = work[row][col] / pivot_value
            for j in range(col, n):
                work[row][j] -= factor * work[col][j]
    return sign * out


def _stable_analysis(matrix: RationalMatrixInput):
    analysis = finite_recurrent_mass_analysis(matrix)
    if not analysis.stable or analysis.star is None or analysis.canonical_potential is None:
        raise ValueError("recurrent invariant is defined here only on the stable finite rational phase")
    return analysis


def recurrent_loop_zeta(matrix: RationalMatrixInput) -> Fraction:
    """Return exact ``Z_loop=1/det(I-W)=det((I-W)^-1)`` on the stable phase."""
    analysis = _stable_analysis(matrix)
    assert analysis.star is not None
    value = _determinant(analysis.star)
    if value < 1:
        raise AssertionError("positive recurrent loop zeta must be at least one")
    return value


def recurrent_loop_surplus_expr(matrix: RationalMatrixInput) -> LnExpr:
    """Return symbolic BRC ``LN(Z_loop)`` without floating log evaluation."""
    zeta = recurrent_loop_zeta(matrix)
    return ln(division(zeta.numerator, zeta.denominator))


@dataclass(frozen=True)
class RecurrentEqualSlackCertificate:
    """Pure integer equal-slack form of a stable rational recurrence."""

    common_denominator: int
    integer_mass_matrix: tuple[tuple[int, ...], ...]
    determinant_slack: int
    integer_potential: tuple[int, ...]
    loop_zeta: Fraction

    def verify(self) -> bool:
        d = self.common_denominator
        delta = self.determinant_slack
        h = self.integer_potential
        if d <= 0 or delta <= 0 or any(value <= 0 for value in h):
            return False
        n = len(h)
        if len(self.integer_mass_matrix) != n:
            return False
        for i, row in enumerate(self.integer_mass_matrix):
            if len(row) != n:
                return False
            lhs = sum(row[j] * h[j] for j in range(n))
            if lhs != d * h[i] - delta:
                return False
        return self.loop_zeta == Fraction(d**n, delta)


def recurrent_equal_slack_certificate(matrix: RationalMatrixInput) -> RecurrentEqualSlackCertificate:
    """Return the canonical integer ray ``B h0 = det(B) 1``.

    If ``W=A/D`` and ``B=DI-A``, the returned potential is
    ``h0=adj(B)1``.  We recover it exactly from the already computed canonical
    rational potential and verify the integer equal-slack law.
    """
    analysis = _stable_analysis(matrix)
    assert analysis.canonical_potential is not None
    d = analysis.common_denominator
    a = analysis.integer_mass_matrix
    n = len(a)
    b = tuple(
        tuple((d if i == j else 0) - a[i][j] for j in range(n))
        for i in range(n)
    )
    delta_fraction = _determinant(b)
    if delta_fraction.denominator != 1 or delta_fraction <= 0:
        raise AssertionError("stable cleared recurrent determinant must be a positive integer")
    delta = delta_fraction.numerator
    h_values: list[int] = []
    for value in analysis.canonical_potential:
        scaled = value * delta / d
        if scaled.denominator != 1 or scaled <= 0:
            raise AssertionError("canonical equal-slack potential did not clear to a positive integer")
        h_values.append(scaled.numerator)
    certificate = RecurrentEqualSlackCertificate(
        common_denominator=d,
        integer_mass_matrix=a,
        determinant_slack=delta,
        integer_potential=tuple(h_values),
        loop_zeta=Fraction(d**n, delta),
    )
    if not certificate.verify():
        raise AssertionError("equal-slack recurrent certificate verification failed")
    if certificate.loop_zeta != recurrent_loop_zeta(matrix):
        raise AssertionError("integer determinant zeta disagrees with recurrent star determinant")
    return certificate


def _explicit_branch(
    matrix: RationalMatrixInput,
    source: int,
    target: int,
    branch_weight: RationalInput,
):
    analysis = _stable_analysis(matrix)
    n = len(analysis.mass_matrix)
    if isinstance(source, bool) or isinstance(target, bool):
        raise TypeError("source/target must be integer indices")
    if not (isinstance(source, int) and isinstance(target, int) and 0 <= source < n and 0 <= target < n):
        raise ValueError("source/target out of range")
    weight = Fraction(branch_weight)
    if isinstance(branch_weight, bool) or not isinstance(branch_weight, (int, Fraction)):
        raise TypeError("branch_weight must be int or Fraction")
    if weight <= 0:
        raise ValueError("branch_weight must be positive")
    if weight > analysis.mass_matrix[source][target]:
        raise ValueError("explicit branch weight cannot exceed the total mass entry")
    assert analysis.star is not None
    return analysis, weight


def recurrent_edge_response(
    matrix: RationalMatrixInput,
    source: int,
    target: int,
    branch_weight: RationalInput,
) -> Fraction:
    """Return exact log-weight response ``R_e=q_e (I-W)^-1[target,source]``."""
    analysis, weight = _explicit_branch(matrix, source, target, branch_weight)
    assert analysis.star is not None
    return weight * analysis.star[target][source]


def recurrent_edge_multiplicative_radius(
    matrix: RationalMatrixInput,
    source: int,
    target: int,
    branch_weight: RationalInput,
) -> Fraction | None:
    """Return ``1+1/R_e``; ``None`` denotes infinite transient-edge radius."""
    response = recurrent_edge_response(matrix, source, target, branch_weight)
    return None if response == 0 else Fraction(1, 1) + Fraction(1, 1) / response


def recurrent_edge_deletion_zeta_factor(
    matrix: RationalMatrixInput,
    source: int,
    target: int,
    branch_weight: RationalInput,
) -> Fraction:
    """Return the exact zeta ratio ``exp(Gamma(W)-Gamma(W-e))=1+R_e``."""
    return Fraction(1, 1) + recurrent_edge_response(matrix, source, target, branch_weight)


def recurrent_log_response_hessian(
    matrix: RationalMatrixInput,
    branches: Sequence[ExplicitBranch],
) -> tuple[tuple[Fraction, ...], ...]:
    """Return exact Hessian of ``Gamma`` in declared log branch-weight coordinates."""
    analysis = _stable_analysis(matrix)
    assert analysis.star is not None
    n = len(analysis.mass_matrix)
    normalized: list[tuple[int, int, Fraction]] = []
    totals: dict[tuple[int, int], Fraction] = {}
    for source, target, raw_weight in branches:
        if isinstance(source, bool) or isinstance(target, bool):
            raise TypeError("branch endpoints must be integer indices")
        if not (isinstance(source, int) and isinstance(target, int) and 0 <= source < n and 0 <= target < n):
            raise ValueError("branch endpoint out of range")
        if isinstance(raw_weight, bool) or not isinstance(raw_weight, (int, Fraction)):
            raise TypeError("branch weights must be int or Fraction")
        weight = Fraction(raw_weight)
        if weight <= 0:
            raise ValueError("branch weights must be positive")
        normalized.append((source, target, weight))
        totals[(source, target)] = totals.get((source, target), Fraction(0, 1)) + weight
    for (source, target), total in totals.items():
        if total > analysis.mass_matrix[source][target]:
            raise ValueError("declared explicit parallel branches exceed the total mass entry")

    out: list[list[Fraction]] = []
    for i, (a, b, q_e) in enumerate(normalized):
        row: list[Fraction] = []
        response_e = q_e * analysis.star[b][a]
        for j, (c, d, q_f) in enumerate(normalized):
            value = q_e * q_f * analysis.star[b][c] * analysis.star[d][a]
            if i == j:
                value += response_e
            row.append(value)
        out.append(row)
    # Exact symmetry is a theorem-level regression guard.
    for i in range(len(out)):
        for j in range(len(out)):
            if out[i][j] != out[j][i]:
                raise AssertionError("recurrent log-response Hessian lost symmetry")
    return tuple(tuple(row) for row in out)
