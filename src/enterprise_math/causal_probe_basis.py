"""Minimal future-probe generators for integer causal distinguishability.

A traditional vector-space basis is not assumed.  We start from concrete
integer observations and allowed future operations.  Each pulled-back future
observation is a concrete experiment.  A causal probe basis is a minimal set of
such experiments whose equality already implies equality under every allowed
finite future experiment.

The basis size equals the stable causal-visible rank from causal_future_module.
Rows are kept as actual integer probe rows; exact fraction-free rank is used only
to test whether a new probe adds a genuinely new distinguishable direction.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .causal_future_module import Matrix, RowFamily, Vector, row_dot


@dataclass(frozen=True)
class CausalProbe:
    observation_index: int
    pullback_word: tuple[int, ...]
    row: Vector


@dataclass(frozen=True)
class CausalProbeBasis:
    state_dimension: int
    probes: tuple[CausalProbe, ...]
    stable_depth: int

    @property
    def causal_dimension(self) -> int:
        return len(self.probes)


def _require_matrix(matrix: Matrix, size: int) -> None:
    if not isinstance(matrix, tuple) or len(matrix) != size:
        raise ValueError("operation matrix dimension mismatch")
    if any(not isinstance(row, tuple) or len(row) != size for row in matrix):
        raise ValueError("operation matrix must be square")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in matrix
        for value in row
    ):
        raise ValueError("operation matrix entries must be integers")


def _require_rows(rows: RowFamily) -> int:
    if not isinstance(rows, tuple) or not rows:
        raise ValueError("observations must be a non-empty tuple")
    width = len(rows[0])
    if width == 0:
        raise ValueError("observation rows must be non-empty")
    if any(not isinstance(row, tuple) or len(row) != width for row in rows):
        raise ValueError("observation rows must have a common width")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in rows
        for value in row
    ):
        raise ValueError("observation entries must be integers")
    return width


def _primitive(row: Vector) -> Vector:
    divisor = 0
    for value in row:
        divisor = gcd(divisor, abs(value))
    if divisor == 0:
        return tuple(0 for _ in row)
    result = tuple(value // divisor for value in row)
    first = next(value for value in result if value)
    if first < 0:
        result = tuple(-value for value in result)
    return result


def _rank(rows: tuple[Vector, ...], width: int) -> int:
    data = [list(_primitive(row)) for row in rows if any(row)]
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (index for index in range(pivot_row, len(data)) if data[index][column]),
            None,
        )
        if pivot is None:
            continue
        data[pivot_row], data[pivot] = data[pivot], data[pivot_row]
        pivot_value = data[pivot_row][column]
        for index in range(pivot_row + 1, len(data)):
            entry = data[index][column]
            if entry == 0:
                continue
            divisor = gcd(abs(pivot_value), abs(entry))
            left = pivot_value // divisor
            right = entry // divisor
            reduced = tuple(
                left * data[index][j] - right * data[pivot_row][j]
                for j in range(width)
            )
            data[index] = list(_primitive(reduced))
        pivot_row += 1
        if pivot_row == len(data):
            break
    return pivot_row


def _row_times_matrix(row: Vector, matrix: Matrix) -> Vector:
    return tuple(
        sum(row[index] * matrix[index][column] for index in range(len(row)))
        for column in range(len(row))
    )


def _greedy_independent(probes: tuple[CausalProbe, ...], width: int) -> tuple[CausalProbe, ...]:
    chosen = []
    rank = 0
    for probe in probes:
        candidate_rows = tuple(item.row for item in chosen) + (probe.row,)
        candidate_rank = _rank(candidate_rows, width)
        if candidate_rank > rank:
            chosen.append(probe)
            rank = candidate_rank
        if rank == width:
            break
    return tuple(chosen)


def causal_probe_basis(
    operations: tuple[Matrix, ...],
    observations: RowFamily,
) -> CausalProbeBasis:
    """Construct concrete future experiments generating all distinguishability.

    The routine never enumerates states.  At each depth, the currently selected
    probes span the full visible row space.  Pulling only those basis probes
    through each declared operation therefore spans every next-depth probe as
    well.  Stabilization occurs when no image adds row rank.
    """
    size = _require_rows(observations)
    if not isinstance(operations, tuple):
        raise ValueError("operations must be a tuple")
    for matrix in operations:
        _require_matrix(matrix, size)

    probes = tuple(
        CausalProbe(index, (), row)
        for index, row in enumerate(observations)
        if any(row)
    )
    basis = _greedy_independent(probes, size)
    current_rank = len(basis)
    depth = 0

    for _ in range(size + 1):
        candidates = list(basis)
        for probe in basis:
            for operation_index, matrix in enumerate(operations):
                candidates.append(
                    CausalProbe(
                        observation_index=probe.observation_index,
                        pullback_word=probe.pullback_word + (operation_index,),
                        row=_row_times_matrix(probe.row, matrix),
                    )
                )
        next_basis = _greedy_independent(tuple(candidates), size)
        next_rank = len(next_basis)
        if next_rank == current_rank:
            return CausalProbeBasis(
                state_dimension=size,
                probes=basis,
                stable_depth=depth,
            )
        if next_rank < current_rank:
            raise AssertionError("causal probe rank cannot decrease")
        basis = next_basis
        current_rank = next_rank
        depth += 1

    raise AssertionError("causal probe basis must stabilize within state rank")


def probe_signature(state: Vector, basis: CausalProbeBasis) -> tuple[int, ...]:
    """Integer outputs of the minimal causal probe generator family."""
    if len(state) != basis.state_dimension:
        raise ValueError("state dimension mismatch")
    return tuple(row_dot(probe.row, state) for probe in basis.probes)


def same_future_signature(
    left: Vector,
    right: Vector,
    basis: CausalProbeBasis,
) -> bool:
    """Whether the selected causal probe basis already identifies the states."""
    return probe_signature(left, basis) == probe_signature(right, basis)
