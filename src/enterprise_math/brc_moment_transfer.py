"""Exact integer-moment and rational length-marker BRC transfer tools.

Production extraction of WBRC-T33..T35.  Formal rational-function identities
are represented operationally by exact evaluation at rational z where the
required inverses exist; coefficientwise walk data is available without a
convergence assumption through exact matrix powers.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Sequence

from .brc_histogram import RationalInput

RationalMatrix = tuple[tuple[Fraction, ...], ...]
WeightedEdge = tuple[int, int, RationalInput]


def _nonnegative_int(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be non-negative")
    return value


def _positive_fraction(name: str, value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be int or Fraction")
    result = Fraction(value)
    if result <= 0:
        raise ValueError(f"{name} must be positive")
    return result


def _fraction(name: str, value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be int or Fraction")
    return Fraction(value)


def _identity(n: int) -> RationalMatrix:
    return tuple(tuple(Fraction(int(i == j), 1) for j in range(n)) for i in range(n))


def _matrix(matrix: Sequence[Sequence[RationalInput]]) -> RationalMatrix:
    rows = tuple(tuple(_fraction("matrix entry", value) for value in row) for row in matrix)
    if any(len(row) != len(rows) for row in rows):
        raise ValueError("matrix must be square")
    return rows


def _add(left: RationalMatrix, right: RationalMatrix) -> RationalMatrix:
    if len(left) != len(right) or any(len(left[i]) != len(right[i]) for i in range(len(left))):
        raise ValueError("matrix shape mismatch")
    return tuple(tuple(left[i][j] + right[i][j] for j in range(len(left[i]))) for i in range(len(left)))


def _scale(matrix: RationalMatrix, scalar: Fraction) -> RationalMatrix:
    return tuple(tuple(scalar * value for value in row) for row in matrix)


def _multiply(left: RationalMatrix, right: RationalMatrix) -> RationalMatrix:
    if not left or not right:
        return ()
    if len(left[0]) != len(right):
        raise ValueError("matrix dimension mismatch")
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction(0, 1))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def _inverse(matrix: RationalMatrix) -> RationalMatrix:
    n = len(matrix)
    if n == 0:
        return ()
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be square")
    work = [list(row) + list(_identity(n)[i]) for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col] != 0), None)
        if pivot is None:
            raise ValueError("matrix is singular")
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
        pivot_value = work[col][col]
        work[col] = [value / pivot_value for value in work[col]]
        for row in range(n):
            if row == col:
                continue
            factor = work[row][col]
            if factor:
                work[row] = [work[row][j] - factor * work[col][j] for j in range(2 * n)]
    return tuple(tuple(work[i][n:]) for i in range(n))


def _submatrix(matrix: RationalMatrix, rows: Sequence[int], cols: Sequence[int]) -> RationalMatrix:
    return tuple(tuple(matrix[i][j] for j in cols) for i in rows)


def moment_transition_matrix(state_count: int, edges: Iterable[WeightedEdge], order: int) -> RationalMatrix:
    """Return ``W^(m)`` from explicit positive-rational branch edges."""
    state_count = _nonnegative_int("state_count", state_count)
    if state_count == 0:
        raise ValueError("state_count must be positive")
    order = _nonnegative_int("order", order)
    out = [[Fraction(0, 1) for _ in range(state_count)] for _ in range(state_count)]
    for source, target, raw_weight in edges:
        if isinstance(source, bool) or isinstance(target, bool):
            raise TypeError("edge endpoints must be integer indices")
        if not isinstance(source, int) or not isinstance(target, int):
            raise TypeError("edge endpoints must be integer indices")
        if not (0 <= source < state_count and 0 <= target < state_count):
            raise ValueError("edge endpoint out of range")
        weight = _positive_fraction("edge weight", raw_weight)
        out[source][target] += weight**order
    return tuple(tuple(row) for row in out)


def moment_matrix_power(matrix: Sequence[Sequence[RationalInput]], exponent: int) -> RationalMatrix:
    base = _matrix(matrix)
    exponent = _nonnegative_int("exponent", exponent)
    result = _identity(len(base))
    while exponent:
        if exponent & 1:
            result = _multiply(result, base)
        exponent >>= 1
        if exponent:
            base = _multiply(base, base)
    return result


def moment_walk_series_coefficients(
    state_count: int,
    edges: Iterable[WeightedEdge],
    order: int,
    max_length: int,
) -> tuple[RationalMatrix, ...]:
    """Exact coefficient matrices through ``z^max_length``."""
    max_length = _nonnegative_int("max_length", max_length)
    matrix = moment_transition_matrix(state_count, tuple(edges), order)
    coefficients = [_identity(state_count)]
    current = _identity(state_count)
    for _ in range(max_length):
        current = _multiply(current, matrix)
        coefficients.append(current)
    return tuple(coefficients)


@dataclass(frozen=True)
class FiniteMomentSignature:
    max_parallel_multiplicity: int
    matrices: tuple[RationalMatrix, ...]


def finite_moment_signature(state_count: int, edges: Iterable[WeightedEdge]) -> FiniteMomentSignature:
    """Return the WBRC-T34 finite primitive moment matrix signature W^0..W^R."""
    edge_tuple = tuple(edges)
    counts: dict[tuple[int, int], int] = {}
    for source, target, _ in edge_tuple:
        if isinstance(source, bool) or isinstance(target, bool) or not isinstance(source, int) or not isinstance(target, int):
            raise TypeError("edge endpoints must be integer indices")
        counts[(source, target)] = counts.get((source, target), 0) + 1
    maximum = max(counts.values(), default=0)
    matrices = tuple(moment_transition_matrix(state_count, edge_tuple, order) for order in range(maximum + 1))
    return FiniteMomentSignature(maximum, matrices)


def moment_star_at_z(matrix: Sequence[Sequence[RationalInput]], z: RationalInput) -> RationalMatrix:
    """Exact rational evaluation of ``(I-zW)^-1`` when nonsingular."""
    moment_matrix = _matrix(matrix)
    z_value = _fraction("z", z)
    n = len(moment_matrix)
    operator = tuple(
        tuple(Fraction(int(i == j), 1) - z_value * moment_matrix[i][j] for j in range(n))
        for i in range(n)
    )
    return _inverse(operator)


def moment_port_kernel_at_z(
    matrix: Sequence[Sequence[RationalInput]],
    internal_indices: Sequence[int],
    z: RationalInput,
) -> RationalMatrix:
    """Evaluate ``E_m(z)=zB+z^2 Y(I-zA)^-1 X`` exactly."""
    full = _matrix(matrix)
    n = len(full)
    if n == 0:
        raise ValueError("matrix must be nonempty")
    internal = tuple(sorted(internal_indices))
    if not internal or len(internal) >= n or len(set(internal)) != len(internal):
        raise ValueError("internal_indices must be a nonempty proper subset")
    if any(isinstance(i, bool) or not isinstance(i, int) or i < 0 or i >= n for i in internal):
        raise ValueError("internal state index out of range")
    boundary = tuple(i for i in range(n) if i not in set(internal))
    z_value = _fraction("z", z)
    a = _submatrix(full, internal, internal)
    x = _submatrix(full, internal, boundary)
    y = _submatrix(full, boundary, internal)
    b = _submatrix(full, boundary, boundary)
    hidden_star = moment_star_at_z(a, z_value)
    excursion = _multiply(_multiply(y, hidden_star), x)
    return _add(_scale(b, z_value), _scale(excursion, z_value * z_value))


def equal_loop_moment_critical_z(loop_count: int, loop_weight: RationalInput, order: int) -> Fraction:
    loop_count = _nonnegative_int("loop_count", loop_count)
    if loop_count == 0:
        raise ValueError("loop_count must be positive")
    order = _nonnegative_int("order", order)
    weight = _positive_fraction("loop_weight", loop_weight)
    return Fraction(1, 1) / (loop_count * (weight**order))
