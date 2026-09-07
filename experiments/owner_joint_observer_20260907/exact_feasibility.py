"""Certificate-producing rational feasibility for ``A x = b, x >= 0``.

This is standard Phase-I simplex with Bland's anti-cycling rule, implemented
for the finite raw X6 observer consumer. It is not new Enterprise mathematics,
a new BRC family, a uniqueness test, or a polynomial-time algorithm claim.
The consumer retains the native coordinates and checks its BRC marginals.

For each row let d_i be -1 if b_i < 0, otherwise 1. Phase I minimizes
``sum(a_i)`` subject to ``D A x + a = D b``, ``x, a >= 0``. Artificial
variables give an initial feasible basis even with dependent/zero rows.
Every pivot preserves that equality and nonnegativity. At value zero the
original x is feasible. At a positive optimum, the exact simplex multiplier
pi gives ``y = -D pi``, hence ``A.T y >= 0`` and ``b.T y < 0``. These are
mutually exclusive, independently checked certificates for the original
system. No row removal, guessed rank, or Phase-II optimization is needed.

Bland's rule chooses the smallest indexed improving nonbasic variable and,
among minimum-ratio rows, the smallest indexed leaving basic variable. Its
standard anti-cycling theorem prohibits a repeated basis, including at
degenerate pivots. There are at most binomial(n+m, m) bases, so this rational
finite-dimensional algorithm terminates: the Phase-I objective is bounded
below by zero and an improving unbounded direction is impossible. The bound
is exponential; Fraction bit lengths and the dense m-by-(n+m) tableau can
also be expensive. Resource exhaustion is an execution failure, never an
infeasibility certificate.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Literal


@dataclass(frozen=True)
class FeasibilityCertificate:
    """Exactly one original-system witness; pivots is diagnostic only."""

    status: Literal["FEASIBLE", "INFEASIBLE"]
    primal: tuple[Fraction, ...] | None = None
    dual: tuple[Fraction, ...] | None = None
    pivots: int = 0


def _rational(value: int | Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("entries must be exact int or Fraction, never float or bool")
    return Fraction(value)


def _system(
    matrix: Iterable[Iterable[int | Fraction]],
    rhs: Iterable[int | Fraction],
    n_variables: int | None,
) -> tuple[tuple[tuple[Fraction, ...], ...], tuple[Fraction, ...], int]:
    rows = tuple(tuple(_rational(value) for value in row) for row in matrix)
    target = tuple(_rational(value) for value in rhs)
    if len(rows) != len(target):
        raise ValueError("matrix row count and rhs length disagree")
    if n_variables is not None and (type(n_variables) is not int or n_variables < 0):
        raise ValueError("n_variables must be a nonnegative integer")
    width = len(rows[0]) if rows else (n_variables if n_variables is not None else 0)
    if any(len(row) != width for row in rows):
        raise ValueError("matrix rows must have equal length")
    if n_variables is not None and width != n_variables:
        raise ValueError("n_variables disagrees with matrix width")
    return rows, target, width


def verify_certificate(
    matrix: Iterable[Iterable[int | Fraction]],
    rhs: Iterable[int | Fraction],
    certificate: FeasibilityCertificate,
    *,
    n_variables: int | None = None,
) -> bool:
    """Check only original A,b and a witness; never run or trust the solver.

    Malformed systems/certificates fail closed. Infeasibility uses the sign
    convention ``A.T y >= 0, b.T y < 0``. No tableau, pivot history, stored
    objective, or reported iteration count participates in verification.
    """
    try:
        rows, target, width = _system(matrix, rhs, n_variables)
        if not isinstance(certificate, FeasibilityCertificate):
            return False
        if certificate.status == "FEASIBLE":
            if certificate.primal is None or certificate.dual is not None:
                return False
            point = tuple(_rational(value) for value in certificate.primal)
            return (
                len(point) == width
                and all(value >= 0 for value in point)
                and all(sum(a * x for a, x in zip(row, point)) == b
                        for row, b in zip(rows, target))
            )
        if certificate.status == "INFEASIBLE":
            if certificate.dual is None or certificate.primal is not None:
                return False
            separator = tuple(_rational(value) for value in certificate.dual)
            return (
                len(separator) == len(rows)
                and sum(b * y for b, y in zip(target, separator)) < 0
                and all(sum(row[j] * y for row, y in zip(rows, separator)) >= 0
                        for j in range(width))
            )
        return False
    except (TypeError, ValueError, OverflowError):
        return False


def solve_nonnegative(
    matrix: Iterable[Iterable[int | Fraction]],
    rhs: Iterable[int | Fraction],
    *,
    n_variables: int | None = None,
) -> FeasibilityCertificate:
    """Return a checked exact primal solution or Farkas separator.

    An empty matrix has zero columns by default. For zero constraints and a
    positive number of variables pass ``n_variables`` explicitly. Inputs may
    have zero columns, negative rhs, redundant rows, or arbitrary rational
    signed coefficients. They must be finite iterables of int/Fraction.
    """
    rows, target, width = _system(matrix, rhs, n_variables)
    height = len(rows)
    augmented_width = width + height
    signs = [Fraction(-1 if value < 0 else 1) for value in target]
    # Rows are [B^-1 (D A | I), B^-1 D b]. The artificial block therefore
    # always records B^-1, including when an artificial variable leaves.
    tableau = [
        [signs[i] * value for value in row]
        + [Fraction(i == j) for j in range(height)]
        + [signs[i] * target[i]]
        for i, row in enumerate(rows)
    ]
    basis = list(range(width, augmented_width))
    reduced_cost = [-sum(row[j] for row in tableau) for j in range(width)] + [Fraction(0)] * height
    objective = sum((row[-1] for row in tableau), Fraction(0))
    pivots = 0

    while objective:
        entering = next((j for j, cost in enumerate(reduced_cost) if cost < 0), None)
        if entering is None:
            break
        eligible = [i for i, row in enumerate(tableau) if row[entering] > 0]
        if not eligible:
            raise ArithmeticError("Phase-I invariant failure: improving unbounded direction")
        leaving = min(eligible, key=lambda i: (tableau[i][-1] / tableau[i][entering], basis[i]))
        pivot = tableau[leaving][entering]
        tableau[leaving] = [value / pivot for value in tableau[leaving]]
        pivot_row = tableau[leaving]
        for i, row in enumerate(tableau):
            if i != leaving and row[entering]:
                multiplier = row[entering]
                tableau[i] = [value - multiplier * coefficient
                              for value, coefficient in zip(row, pivot_row)]
        improvement = reduced_cost[entering]
        reduced_cost = [cost - improvement * coefficient
                        for cost, coefficient in zip(reduced_cost, pivot_row)]
        objective += improvement * pivot_row[-1]
        basis[leaving] = entering
        pivots += 1
        if objective < 0 or any(row[-1] < 0 for row in tableau):
            raise ArithmeticError("Phase-I invariant failure: negative objective or basic mass")

    if objective == 0:
        point = [Fraction(0)] * width
        for i, variable in enumerate(basis):
            if variable < width:
                point[variable] = tableau[i][-1]
        result = FeasibilityCertificate("FEASIBLE", primal=tuple(point), pivots=pivots)
    else:
        # pi_j = sum_i c_B[i] (B^-1)[i,j], where c_B is 1 precisely for
        # artificial basic variables. Convert normalized-row pi back to A,b.
        separator = tuple(
            -signs[j] * sum((tableau[i][width + j] for i, variable in enumerate(basis)
                             if variable >= width), Fraction(0))
            for j in range(height)
        )
        result = FeasibilityCertificate("INFEASIBLE", dual=separator, pivots=pivots)
    if not verify_certificate(rows, target, result, n_variables=width):
        raise ArithmeticError("Phase-I output failed independent original-system verification")
    return result
