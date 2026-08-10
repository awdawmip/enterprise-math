"""Profinite topology of exact integer observation fibers.

For an integer observation map

    O : Z^n -> Z^m

let ``K=ker_Z(O)``.  Because the codomain is torsion-free, K is saturated:
``r x in K`` implies ``O(x)=0``.  Therefore

    Z^n / K ~= im(O)

is free abelian.

Consequences in the congruence/profinite topology:

* K is always closed;
* K is open iff the quotient is finite;
* a free abelian quotient is finite iff it is zero;
* hence K is open iff ``O=0`` and K is the whole state lattice.

Thus every proper exact observation fiber is closed but not open.  Infinite
modular refinement can separate every state difference outside K, but no fixed
finite modular family decides exact observation equality uniformly on all
unbounded integer states.

Sharp finite-family witness: let D be the lcm of the tested moduli and choose a
coordinate e_j with ``O e_j !=0``.  The states

    x=0,    y=D e_j

have identical observation outputs modulo every tested modulus, while their exact
outputs differ by the nonzero vector ``D O e_j``.

This is the FIBER-side topological counterpart of the IMAGE result.  IMAGE
subgroups can be nontrivially open when their cokernel is finite; proper kernels
of maps into free integer observations cannot.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import lcm
from typing import Sequence

from .integer_future_smith_precision import integer_smith_precision_profile


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def _matrix(values: Sequence[Sequence[int]]) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError("observation matrix must contain at least one row")
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise ValueError("observation rows must have one common positive width")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("observation entries must be integers")
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


def observation_kernel_is_saturated(
    observation_matrix: Sequence[Sequence[int]],
) -> bool:
    _matrix(observation_matrix)
    return True


def observation_kernel_is_profinite_closed(
    observation_matrix: Sequence[Sequence[int]],
) -> bool:
    _matrix(observation_matrix)
    return True


def observation_kernel_is_profinite_open(
    observation_matrix: Sequence[Sequence[int]],
) -> bool:
    O = _matrix(observation_matrix)
    return integer_smith_precision_profile(O).rational_rank == 0


def apply_observation(
    observation_matrix: Sequence[Sequence[int]],
    state: Sequence[int],
) -> Vector:
    O = _matrix(observation_matrix)
    x = tuple(state)
    if len(x) != len(O[0]):
        raise ValueError("state dimension must match observation width")
    for value in x:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("state entries must be integers")
    return tuple(
        sum(coefficient * value for coefficient, value in zip(row, x, strict=True))
        for row in O
    )


@dataclass(frozen=True)
class FiniteModularFiberFalsePositive:
    tested_moduli: tuple[int, ...]
    lcm_ceiling: int
    witness_coordinate: int
    left_state: Vector
    right_state: Vector
    left_exact_output: Vector
    right_exact_output: Vector

    @property
    def exact_outputs_differ(self) -> bool:
        return self.left_exact_output != self.right_exact_output


def finite_modular_family_fiber_false_positive(
    observation_matrix: Sequence[Sequence[int]],
    tested_moduli: Sequence[int],
) -> FiniteModularFiberFalsePositive:
    """Construct exact-unequal states that every tested modular output identifies."""
    O = _matrix(observation_matrix)
    moduli = _moduli(tested_moduli)
    if observation_kernel_is_profinite_open(O):
        raise ValueError("zero observation has no exact-inequality witness")

    dimension = len(O[0])
    coordinate = next(
        (
            column
            for column in range(dimension)
            if any(O[row][column] != 0 for row in range(len(O)))
        ),
        None,
    )
    if coordinate is None:
        raise AssertionError("nonzero observation lost a visible coordinate")

    ceiling = 1
    for modulus in moduli:
        ceiling = lcm(ceiling, modulus)
    left = tuple(0 for _ in range(dimension))
    right = tuple(
        ceiling if column == coordinate else 0
        for column in range(dimension)
    )
    left_output = apply_observation(O, left)
    right_output = apply_observation(O, right)
    if left_output == right_output:
        raise AssertionError("finite-fiber witness failed exact separation")
    for modulus in moduli:
        if any(
            (left_value - right_value) % modulus != 0
            for left_value, right_value in zip(left_output, right_output, strict=True)
        ):
            raise AssertionError("finite-fiber witness was visible at a tested modulus")

    return FiniteModularFiberFalsePositive(
        tested_moduli=moduli,
        lcm_ceiling=ceiling,
        witness_coordinate=coordinate,
        left_state=left,
        right_state=right,
        left_exact_output=left_output,
        right_exact_output=right_output,
    )


@dataclass(frozen=True)
class ProfiniteFiberPrecisionReport:
    state_dimension: int
    observation_rational_rank: int
    exact_hidden_free_rank: int
    saturated_kernel: bool
    profinitely_closed: bool
    profinitely_open: bool


def profinite_fiber_precision_report(
    observation_matrix: Sequence[Sequence[int]],
) -> ProfiniteFiberPrecisionReport:
    O = _matrix(observation_matrix)
    profile = integer_smith_precision_profile(O)
    rank = profile.rational_rank
    return ProfiniteFiberPrecisionReport(
        state_dimension=len(O[0]),
        observation_rational_rank=rank,
        exact_hidden_free_rank=len(O[0]) - rank,
        saturated_kernel=True,
        profinitely_closed=True,
        profinitely_open=rank == 0,
    )
