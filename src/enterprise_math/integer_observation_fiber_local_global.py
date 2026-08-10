"""Local-global and bounded finite certificates for exact observation fibers.

For integer observation ``O:Z^n->Z^m`` and two states x,y, exact agreement is

    O(x-y)=0.

The image ``im(O)`` is free abelian, so the FIBER-side quotient has no torsion
precision axis.  If O is nonzero, exact equality requires only one kind of
unbounded resource: a modular family that separates nonzero integers.

In particular, for any base R>1,

    O(x)=O(y) over Z
      iff
    O(x)==O(y) (mod R^e) for every e>=1.

No finite modular family is uniformly complete on unbounded states unless O=0.
This is the closed-but-not-open kernel theorem.

An independent state bound finite-izes the test.  If every coordinate obeys
``|x_i|,|y_i|<=H``, then

    |O_j(x-y)| <= 2 H ||O_j||_1.

Hence any modulus D strictly larger than

    B = 2 H max_j ||O_j||_1

turns modular output equality into exact output equality on the whole bounded
state box.

This is the FIBER-side analogue of the bounded free-cokernel IMAGE certificate:
a closed exact property becomes finitely decidable once an independent height
bound restricts the admissible lifts.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_observation_profinite_fiber import apply_observation
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


def observation_needs_unbounded_precision(
    observation_matrix: Sequence[Sequence[int]],
) -> bool:
    O = _matrix(observation_matrix)
    return integer_smith_precision_profile(O).rational_rank > 0


def power_ladder_uniformly_certifies_exact_fiber(
    observation_matrix: Sequence[Sequence[int]],
    base: int,
) -> bool:
    O = _matrix(observation_matrix)
    if isinstance(base, bool) or not isinstance(base, int):
        raise TypeError("base must be an integer")
    if base <= 0:
        raise ValueError("base must be positive")
    return not observation_needs_unbounded_precision(O) or base > 1


def bounded_state_box_certificate_modulus(
    observation_matrix: Sequence[Sequence[int]],
    state_abs_bound: int,
) -> int:
    O = _matrix(observation_matrix)
    if isinstance(state_abs_bound, bool) or not isinstance(state_abs_bound, int):
        raise TypeError("state_abs_bound must be an integer")
    if state_abs_bound < 0:
        raise ValueError("state_abs_bound must be nonnegative")
    max_l1 = max(sum(abs(value) for value in row) for row in O)
    output_difference_bound = 2 * state_abs_bound * max_l1
    return output_difference_bound + 1


def exact_observation_equal(
    observation_matrix: Sequence[Sequence[int]],
    left_state: Sequence[int],
    right_state: Sequence[int],
) -> bool:
    return apply_observation(observation_matrix, left_state) == apply_observation(
        observation_matrix,
        right_state,
    )


def modular_observation_equal(
    observation_matrix: Sequence[Sequence[int]],
    left_state: Sequence[int],
    right_state: Sequence[int],
    modulus: int,
) -> bool:
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    left = apply_observation(observation_matrix, left_state)
    right = apply_observation(observation_matrix, right_state)
    return all(
        (a - b) % modulus == 0
        for a, b in zip(left, right, strict=True)
    )


def bounded_state_box_certificate_holds(
    observation_matrix: Sequence[Sequence[int]],
    left_state: Sequence[int],
    right_state: Sequence[int],
    state_abs_bound: int,
) -> bool:
    O = _matrix(observation_matrix)
    left = tuple(left_state)
    right = tuple(right_state)
    if len(left) != len(O[0]) or len(right) != len(O[0]):
        raise ValueError("state dimension must match observation width")
    if any(abs(value) > state_abs_bound for value in (*left, *right)):
        raise ValueError("state lies outside declared absolute-value bound")
    modulus = bounded_state_box_certificate_modulus(O, state_abs_bound)
    exact = exact_observation_equal(O, left, right)
    modular = modular_observation_equal(O, left, right, modulus)
    if exact != modular:
        raise AssertionError("bounded FIBER certificate disagreed with exact equality")
    return modular


@dataclass(frozen=True)
class FiberLocalGlobalRequirement:
    observation_rational_rank: int
    unbounded_free_separation_required: bool
    torsion_prime_depths_required: tuple[tuple[int, int], ...]


def fiber_local_global_requirement(
    observation_matrix: Sequence[Sequence[int]],
) -> FiberLocalGlobalRequirement:
    O = _matrix(observation_matrix)
    rank = integer_smith_precision_profile(O).rational_rank
    return FiberLocalGlobalRequirement(
        observation_rational_rank=rank,
        unbounded_free_separation_required=rank > 0,
        torsion_prime_depths_required=(),
    )
