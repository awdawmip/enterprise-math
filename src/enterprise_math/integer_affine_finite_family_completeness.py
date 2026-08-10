"""Exact completeness criterion for a finite modular experiment family.

Let a finite nonempty family of tested moduli have lcm ceiling D and let

    G = coker(A) ~= Z^f direct_sum T,
    E = exp(T).

All local conditions from the family are equivalent to the single condition

    [b] in D G.

Therefore:

### Uniform over all integer targets

The family decides exact reachability for every b iff

    f=0  and  E | D.

The free condition is necessary because ``D Z^f`` is nonzero for every finite D.
The torsion condition is exactly ``D T=0``.

### Uniform over rationally reachable targets

The free component is promised zero, so the family is complete iff simply

    E | D.

Thus the number of experiments and their individual numerical sizes are not the
right resources.  Only the joint lcm precision and the free/torsion cokernel
profile matter.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import lcm
from typing import Sequence

from .integer_affine_local_global import cokernel_torsion_exponent
from .integer_future_smith_precision import integer_smith_precision_profile


Matrix = tuple[tuple[int, ...], ...]


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


def finite_family_lcm(moduli: Sequence[int]) -> int:
    values = tuple(moduli)
    if not values:
        raise ValueError("modulus family must be nonempty")
    result = 1
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("moduli must be integers")
        if value <= 0:
            raise ValueError("moduli must be positive")
        result = lcm(result, value)
    return result


def finite_family_complete_for_rational_image_targets(
    matrix: Sequence[Sequence[int]],
    moduli: Sequence[int],
) -> bool:
    A = _matrix(matrix)
    ceiling = finite_family_lcm(moduli)
    return ceiling % cokernel_torsion_exponent(A) == 0


def finite_family_complete_for_all_targets(
    matrix: Sequence[Sequence[int]],
    moduli: Sequence[int],
) -> bool:
    A = _matrix(matrix)
    profile = integer_smith_precision_profile(A)
    free_rank = len(A) - profile.rational_rank
    return (
        free_rank == 0
        and finite_family_complete_for_rational_image_targets(A, moduli)
    )


@dataclass(frozen=True)
class FiniteModularFamilyCompletenessReport:
    tested_moduli: tuple[int, ...]
    lcm_ceiling: int
    ambient_rank: int
    image_rational_rank: int
    free_cokernel_rank: int
    torsion_exponent: int
    rational_image_complete: bool
    all_target_complete: bool


def finite_modular_family_completeness_report(
    matrix: Sequence[Sequence[int]],
    moduli: Sequence[int],
) -> FiniteModularFamilyCompletenessReport:
    A = _matrix(matrix)
    values = tuple(moduli)
    ceiling = finite_family_lcm(values)
    profile = integer_smith_precision_profile(A)
    free_rank = len(A) - profile.rational_rank
    exponent = cokernel_torsion_exponent(A)
    rational_complete = ceiling % exponent == 0
    return FiniteModularFamilyCompletenessReport(
        tested_moduli=values,
        lcm_ceiling=ceiling,
        ambient_rank=len(A),
        image_rational_rank=profile.rational_rank,
        free_cokernel_rank=free_rank,
        torsion_exponent=exponent,
        rational_image_complete=rational_complete,
        all_target_complete=(free_rank == 0 and rational_complete),
    )
