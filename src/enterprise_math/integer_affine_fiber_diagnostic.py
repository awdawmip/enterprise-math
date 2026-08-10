"""Exact integer/modular diagnostic for affine equation fibers.

For an integer homomorphism

    A : Z^n -> Z^m

and target b, the affine fiber ``A x = b`` separates three different structures.

### 1. Free IMAGE/COKERNEL obstruction

If ``b`` is not in the rational column span of A, no nonzero integer multiple of
b can enter ``im_Z(A)``.  The obstruction has a free cokernel component.

### 2. Finite torsion IMAGE obstruction

If ``b`` lies in ``span_Q(A) cap Z^m`` but not in ``im_Z(A)``, its class lies in
the finite saturation quotient

    (span_Q(A) cap Z^m) / im_Z(A).

The least positive ``s`` with ``s b in im_Z(A)`` is the order of this target
class.  It divides the saturation index / maximal determinantal divisor of A.

### 3. FIBER

If b is integrally reachable, the exact solution set is one affine coset of
``ker_Z A ~= Z^(n-rank_Q A)``.

Modulo positive M, first test image membership

    b in im_Z(A) + M Z^m.

If false, the modular affine fiber is empty.  If true, every solution set is one
coset of ``ker(A mod M)`` and therefore has exactly

    M^(n-r) * product_i gcd(d_i,M)

states, where d_i are the nonzero Smith factors of A.

This is the reusable exact-sequence core behind critical denominators, integer
reachability, and dynamic affine model-agreement fibers.  Smith/Hermite theory
and affine congruences are standard prior mathematics.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, prod, isqrt
from typing import Sequence

from .integer_action_module_closure import integer_row_hermite_basis
from .integer_future_smith_precision import integer_smith_precision_profile


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def _matrix(values: Sequence[Sequence[int]]) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError("matrix must contain at least one row")
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise ValueError("matrix rows must have one common positive width")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("matrix entries must be integers")
    return rows


def _target(values: Sequence[int], row_count: int) -> Vector:
    result = tuple(values)
    if len(result) != row_count:
        raise ValueError("target must have one entry per matrix row")
    for value in result:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("target entries must be integers")
    return result


def _column_generators(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(matrix[row][column] for row in range(len(matrix)))
        for column in range(len(matrix[0]))
    )


def _row_lattice_contains(
    generators: Sequence[Sequence[int]],
    target: Sequence[int],
) -> bool:
    vector = tuple(target)
    rows = tuple(tuple(row) for row in generators)
    if not vector:
        raise ValueError("target vector must be nonempty")
    if any(len(row) != len(vector) for row in rows):
        raise ValueError("generator dimension must match target")
    if not rows:
        return all(value == 0 for value in vector)
    return (
        integer_row_hermite_basis(rows)
        == integer_row_hermite_basis(rows + (vector,))
    )


def _divisors(value: int) -> tuple[int, ...]:
    if value <= 0:
        raise ValueError("divisor source must be positive")
    small = []
    large = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor == 0:
            small.append(divisor)
            partner = value // divisor
            if partner != divisor:
                large.append(partner)
    return tuple(small + list(reversed(large)))


def rationally_reachable(matrix: Sequence[Sequence[int]], target: Sequence[int]) -> bool:
    A = _matrix(matrix)
    b = _target(target, len(A))
    rank_A = integer_smith_precision_profile(A).rational_rank
    augmented = tuple(
        tuple((*row, b_value))
        for row, b_value in zip(A, b, strict=True)
    )
    rank_augmented = integer_smith_precision_profile(augmented).rational_rank
    return rank_A == rank_augmented


def integrally_reachable(matrix: Sequence[Sequence[int]], target: Sequence[int]) -> bool:
    A = _matrix(matrix)
    b = _target(target, len(A))
    return _row_lattice_contains(_column_generators(A), b)


def target_class_order_in_saturation(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
) -> int | None:
    """Least s>0 with s*b in im_Z(A); None for a free rational obstruction."""
    A = _matrix(matrix)
    b = _target(target, len(A))
    if integrally_reachable(A, b):
        return 1
    if not rationally_reachable(A, b):
        return None

    profile = integer_smith_precision_profile(A)
    saturation_index = prod(profile.smith_invariant_factors)
    if saturation_index <= 1:
        raise AssertionError("rational-but-not-integral target had trivial saturation index")
    columns = _column_generators(A)
    for candidate in _divisors(saturation_index):
        if candidate == 1:
            continue
        multiple = tuple(candidate * value for value in b)
        if _row_lattice_contains(columns, multiple):
            return candidate
    raise AssertionError("target class order failed to divide saturation index")


def modularly_reachable(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
    modulus: int,
) -> bool:
    A = _matrix(matrix)
    b = _target(target, len(A))
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    row_count = len(A)
    generators = _column_generators(A) + tuple(
        tuple(modulus if row == column else 0 for column in range(row_count))
        for row in range(row_count)
    )
    return _row_lattice_contains(generators, b)


def modular_kernel_size(matrix: Sequence[Sequence[int]], modulus: int) -> int:
    A = _matrix(matrix)
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    profile = integer_smith_precision_profile(A)
    return (
        modulus ** profile.hidden_free_rank
        * prod(gcd(factor, modulus) for factor in profile.smith_invariant_factors)
    )


@dataclass(frozen=True)
class IntegerAffineFiberReport:
    row_count: int
    state_dimension: int
    rational_rank: int
    smith_factors: tuple[int, ...]
    rationally_reachable: bool
    integrally_reachable: bool
    target_class_order: int | None
    exact_fiber_free_rank: int | None
    obstruction_kind: str


@dataclass(frozen=True)
class ModularAffineFiberReport:
    modulus: int
    state_dimension: int
    solvable: bool
    solution_count: int
    total_state_count: int
    kernel_size_if_solvable: int
    smith_factors: tuple[int, ...]

    @property
    def empty(self) -> bool:
        return not self.solvable


def integer_affine_fiber_report(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
) -> IntegerAffineFiberReport:
    A = _matrix(matrix)
    b = _target(target, len(A))
    profile = integer_smith_precision_profile(A)
    q_reachable = rationally_reachable(A, b)
    z_reachable = integrally_reachable(A, b)
    if z_reachable and not q_reachable:
        raise AssertionError("integer reachability failed to imply rational reachability")
    order = target_class_order_in_saturation(A, b)
    if z_reachable:
        obstruction = "NONE"
        fiber_rank = profile.hidden_free_rank
    elif q_reachable:
        obstruction = "TORSION_IMAGE"
        fiber_rank = None
        if order is None or order <= 1:
            raise AssertionError("torsion image obstruction lacked nontrivial order")
    else:
        obstruction = "FREE_COKERNEL"
        fiber_rank = None
        if order is not None:
            raise AssertionError("free cokernel obstruction unexpectedly had finite order")
    return IntegerAffineFiberReport(
        row_count=len(A),
        state_dimension=len(A[0]),
        rational_rank=profile.rational_rank,
        smith_factors=profile.smith_invariant_factors,
        rationally_reachable=q_reachable,
        integrally_reachable=z_reachable,
        target_class_order=order,
        exact_fiber_free_rank=fiber_rank,
        obstruction_kind=obstruction,
    )


def modular_affine_fiber_report(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
    modulus: int,
) -> ModularAffineFiberReport:
    A = _matrix(matrix)
    b = _target(target, len(A))
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    profile = integer_smith_precision_profile(A)
    kernel_size = modular_kernel_size(A, modulus)
    solvable = modularly_reachable(A, b, modulus)
    total = modulus ** len(A[0])
    return ModularAffineFiberReport(
        modulus=modulus,
        state_dimension=len(A[0]),
        solvable=solvable,
        solution_count=kernel_size if solvable else 0,
        total_state_count=total,
        kernel_size_if_solvable=kernel_size,
        smith_factors=profile.smith_invariant_factors,
    )
