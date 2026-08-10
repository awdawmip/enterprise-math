"""Finite modular certification for all affine targets: exact iff full row rank.

Fix ``A:Z^n->Z^m`` and ask for one **finite** family of moduli that decides
exact reachability of ``A x=b`` correctly for every integer target b.

Such a family exists iff A has full row rank over Q, equivalently iff
``coker(A)`` has no free part.

### Positive direction

If ``rank_Q(A)=m``, the cokernel is finite.  Its exponent E is the least uniform
certificate modulus: ``A x=b`` is exactly solvable iff it is solvable modulo E,
for every b.

### Negative direction

If ``rank_Q(A)<m``, choose a nonzero integer left-null row ``q A=0`` and one
coordinate i with ``q_i != 0``.  For any finite tested modulus family with lcm D,
set

    b = D e_i.

Then b is zero modulo every tested modulus, so x=0 is a modular solution for all
those experiments.  But

    q b = D q_i != 0,

so b is not even in the rational image of A and is therefore not exactly
reachable.

Thus a free cokernel direction defeats every finite uniform modular test family.
A target-height bound or a rational-image promise is not merely convenient; it
is structurally necessary once free cokernel directions are admitted.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import lcm
from typing import Sequence

from .integer_affine_fiber_diagnostic import (
    integrally_reachable,
    modularly_reachable,
    rationally_reachable,
)
from .integer_affine_local_global import (
    cokernel_torsion_exponent,
    integer_left_nullspace_rows,
)
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


def _moduli(values: Sequence[int]) -> tuple[int, ...]:
    moduli = tuple(values)
    if not moduli:
        raise ValueError("modulus family must be nonempty")
    for value in moduli:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("moduli must be integers")
        if value <= 0:
            raise ValueError("moduli must be positive")
    return moduli


def finite_uniform_all_target_certificate_exists(
    matrix: Sequence[Sequence[int]],
) -> bool:
    A = _matrix(matrix)
    return integer_smith_precision_profile(A).rational_rank == len(A)


def least_uniform_all_target_certificate_modulus(
    matrix: Sequence[Sequence[int]],
) -> int | None:
    A = _matrix(matrix)
    return (
        cokernel_torsion_exponent(A)
        if finite_uniform_all_target_certificate_exists(A)
        else None
    )


@dataclass(frozen=True)
class FreeCokernelFiniteFamilyFalsePositive:
    tested_moduli: tuple[int, ...]
    lcm_ceiling: int
    left_null_witness: Vector
    witness_coordinate: int
    target: Vector
    rationally_reachable: bool
    integrally_reachable: bool
    modularly_reachable_all_tests: bool


def free_cokernel_finite_family_false_positive(
    matrix: Sequence[Sequence[int]],
    tested_moduli: Sequence[int],
) -> FreeCokernelFiniteFamilyFalsePositive:
    """Construct an all-tests modular false positive for every rank-deficient A."""
    A = _matrix(matrix)
    moduli = _moduli(tested_moduli)
    if finite_uniform_all_target_certificate_exists(A):
        raise ValueError("matrix has no free cokernel direction")

    left_rows = integer_left_nullspace_rows(A)
    if not left_rows:
        raise AssertionError("rank-deficient matrix lost rational left-nullspace")
    witness = left_rows[0]
    coordinate = next((index for index, value in enumerate(witness) if value), None)
    if coordinate is None:
        raise AssertionError("left-null witness was zero")

    ceiling = 1
    for modulus in moduli:
        ceiling = lcm(ceiling, modulus)
    target = tuple(
        ceiling if index == coordinate else 0
        for index in range(len(A))
    )

    q_dot_b = sum(
        coefficient * value
        for coefficient, value in zip(witness, target, strict=True)
    )
    if q_dot_b == 0:
        raise AssertionError("free-cokernel false-positive target lost obstruction")

    q_reachable = rationally_reachable(A, target)
    z_reachable = integrally_reachable(A, target)
    modular_all = all(
        modularly_reachable(A, target, modulus) for modulus in moduli
    )
    if q_reachable or z_reachable or not modular_all:
        raise AssertionError("finite-family free-cokernel no-go construction failed")

    return FreeCokernelFiniteFamilyFalsePositive(
        tested_moduli=moduli,
        lcm_ceiling=ceiling,
        left_null_witness=witness,
        witness_coordinate=coordinate,
        target=target,
        rationally_reachable=q_reachable,
        integrally_reachable=z_reachable,
        modularly_reachable_all_tests=modular_all,
    )
