"""Smith-invariant profiles of A3 hidden guard quotient modules.

For r integer guard scores and hidden image lattice L <= Z^r, the coarse
predicate information space is the finitely generated abelian group

    Q = Z^r / L.

If L has rank d, Q has free rank r-d. Its torsion invariant factors are obtained
from the determinantal divisors of any integer generator matrix of L:

    Delta_j = gcd of all j x j minors,
    s_j = Delta_j / Delta_(j-1).

This research reference computes those invariants directly. It is intended for
small/medium theorem checks, not as a replacement for a production Smith-normal-
form implementation.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import gcd

from .guard_image_lattice import GuardFamily, IntMatrix, guard_kernel_image_generators, integer_matrix_rank
from .linear_relation_quotient import Partition


@dataclass(frozen=True)
class GuardQuotientModuleProfile:
    guard_count: int
    hidden_rank: int
    free_rank: int
    smith_invariant_factors: tuple[int, ...]
    torsion_factors: tuple[int, ...]
    torsion_order: int


def _determinant_bareiss(matrix: tuple[tuple[int, ...], ...]) -> int:
    if not matrix:
        return 1
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("matrix must be square")
    data = [list(row) for row in matrix]
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if data[pivot_index][pivot_index] == 0:
            swap = next(
                (
                    row
                    for row in range(pivot_index + 1, size)
                    if data[row][pivot_index] != 0
                ),
                None,
            )
            if swap is None:
                return 0
            data[pivot_index], data[swap] = data[swap], data[pivot_index]
            sign = -sign
        pivot = data[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    data[row][column] * pivot
                    - data[row][pivot_index] * data[pivot_index][column]
                )
                if numerator % previous != 0:
                    raise AssertionError("Bareiss exact division failed")
                data[row][column] = numerator // previous
        previous = pivot
    return sign * data[-1][-1]


def _require_generators(
    generators: IntMatrix, guard_count: int | None
) -> int:
    if not isinstance(generators, tuple):
        raise ValueError("generators must be a tuple")
    if generators:
        width = len(generators[0])
        if width == 0:
            raise ValueError("generator rows must have positive width")
        if any(not isinstance(row, tuple) or len(row) != width for row in generators):
            raise ValueError("generator rows must have a common width")
        if any(
            isinstance(value, bool) or not isinstance(value, int)
            for row in generators
            for value in row
        ):
            raise ValueError("generator entries must be integers")
        if guard_count is not None and guard_count != width:
            raise ValueError("guard_count does not match generator width")
        return width
    if guard_count is None:
        raise ValueError("guard_count is required for an empty hidden lattice")
    if isinstance(guard_count, bool) or not isinstance(guard_count, int) or guard_count <= 0:
        raise ValueError("guard_count must be a positive integer")
    return guard_count


def determinantal_divisor(
    generators: IntMatrix, order: int, guard_count: int | None = None
) -> int:
    """Gcd of all order x order minors; Delta_0=1."""
    width = _require_generators(generators, guard_count)
    if isinstance(order, bool) or not isinstance(order, int) or order < 0:
        raise ValueError("order must be a non-negative integer")
    if order == 0:
        return 1
    if order > min(len(generators), width):
        return 0
    divisor = 0
    for row_indices in combinations(range(len(generators)), order):
        for column_indices in combinations(range(width), order):
            minor = tuple(
                tuple(generators[row][column] for column in column_indices)
                for row in row_indices
            )
            divisor = gcd(divisor, abs(_determinant_bareiss(minor)))
    return divisor


def guard_quotient_module_profile(
    generators: IntMatrix, guard_count: int | None = None
) -> GuardQuotientModuleProfile:
    """Return free/torsion invariants of Z^r / <generators>."""
    width = _require_generators(generators, guard_count)
    hidden_rank = integer_matrix_rank(generators, column_count=width)
    previous = 1
    factors = []
    for order in range(1, hidden_rank + 1):
        current = determinantal_divisor(generators, order, guard_count=width)
        if current <= 0 or current % previous != 0:
            raise AssertionError("determinantal divisors must form an exact divisibility chain")
        factor = current // previous
        if factor <= 0:
            raise AssertionError("Smith invariant factors must be positive")
        if factors and factor % factors[-1] != 0:
            raise AssertionError("Smith invariant factors must divide the next factor")
        factors.append(factor)
        previous = current

    torsion = tuple(factor for factor in factors if factor > 1)
    torsion_order = 1
    for factor in torsion:
        torsion_order *= factor
    return GuardQuotientModuleProfile(
        guard_count=width,
        hidden_rank=hidden_rank,
        free_rank=width - hidden_rank,
        smith_invariant_factors=tuple(factors),
        torsion_factors=torsion,
        torsion_order=torsion_order,
    )


def guard_partition_quotient_profile(
    guards: GuardFamily, partition: Partition
) -> GuardQuotientModuleProfile:
    """Compute Q_A=Z^r/W(K_A) invariants directly from guards and partition."""
    generators = guard_kernel_image_generators(guards, partition)
    return guard_quotient_module_profile(generators, guard_count=len(guards))
