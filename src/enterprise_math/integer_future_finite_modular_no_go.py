"""Finite modular experiments cannot certify free hidden state against deep torsion.

For any finite positive modulus family ``M_1,...,M_k``, let

    D = lcm(M_1,...,M_k).

Compare two integer observation maps on the same two-state / two-output interface:

    O_free   = diag(1,0),
    O_finite = diag(1,D).

For every declared modulus M_i, ``M_i | D`` and therefore

    O_free mod M_i = O_finite mod M_i

entrywise.  Hence the two models give exactly the same modular observation
signature for **every** state under every modulus in the finite experiment set.

Their exact integer structures are nevertheless different:

* ``O_free`` has rational rank one and one free hidden state direction;
* ``O_finite`` has full rational rank two, zero free hidden direction, and finite
  Smith torsion factor D.

Thus no finite collection of modular precision levels can prove that an observed
persistent hidden direction is genuinely free/unbounded rather than finite
torsion deeper than all tested moduli.  A finer modulus not annihilating D, or
exact integer access, can separate the models.

This is a sharp finite-precision identifiability no-go, not a probabilistic or
physical claim.  It is standard congruence/Smith arithmetic expressed in the
project's precision language.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import lcm
from typing import Sequence

from .integer_future_modular_precision import modular_observation_signature
from .integer_future_smith_precision import integer_smith_precision_profile


Matrix = tuple[tuple[int, ...], ...]


def _moduli(values: Sequence[int]) -> tuple[int, ...]:
    result = tuple(values)
    if not result:
        raise ValueError("at least one modulus is required")
    for value in result:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("moduli must be integers")
        if value <= 0:
            raise ValueError("moduli must be positive")
    return result


def finite_modular_free_torsion_models(
    moduli: Sequence[int],
) -> tuple[Matrix, Matrix, int]:
    values = _moduli(moduli)
    depth = 1
    for modulus in values:
        depth = lcm(depth, modulus)
    free = (
        (1, 0),
        (0, 0),
    )
    finite = (
        (1, 0),
        (0, depth),
    )
    return free, finite, depth


@dataclass(frozen=True)
class FiniteModularNoGoReport:
    moduli: tuple[int, ...]
    torsion_depth: int
    free_hidden_rank: int
    finite_hidden_rank: int
    finite_smith_factors: tuple[int, ...]
    modular_matrices_identical: bool

    @property
    def exact_integer_structures_differ(self) -> bool:
        return self.free_hidden_rank != self.finite_hidden_rank


def finite_modular_free_torsion_no_go(
    moduli: Sequence[int],
) -> FiniteModularNoGoReport:
    values = _moduli(moduli)
    free, finite, depth = finite_modular_free_torsion_models(values)
    modular_identical = all(
        tuple(tuple(value % modulus for value in row) for row in free)
        == tuple(tuple(value % modulus for value in row) for row in finite)
        for modulus in values
    )
    if not modular_identical:
        raise AssertionError("finite torsion model failed declared modular indistinguishability")

    free_profile = integer_smith_precision_profile(free)
    finite_profile = integer_smith_precision_profile(finite)
    if free_profile.hidden_free_rank != 1:
        raise AssertionError("free comparison model lost its hidden direction")
    if finite_profile.hidden_free_rank != 0:
        raise AssertionError("finite torsion comparison model was not full rank")

    # Mechanical all-state equality can be checked modulo each finite modulus by
    # the entrywise matrix equality above; this spot-checks the actual signature
    # function as an additional executable boundary.
    for modulus in values:
        for state in ((0, 0), (1, 0), (0, 1), (1, 1), (-2, 3)):
            if modular_observation_signature(free, state, modulus) != modular_observation_signature(finite, state, modulus):
                raise AssertionError("modular signature differed despite congruent matrices")

    return FiniteModularNoGoReport(
        moduli=values,
        torsion_depth=depth,
        free_hidden_rank=free_profile.hidden_free_rank,
        finite_hidden_rank=finite_profile.hidden_free_rank,
        finite_smith_factors=finite_profile.smith_invariant_factors,
        modular_matrices_identical=modular_identical,
    )
