"""Guarded contact-word normal form with an exact additive future witness.

The coarse E001/P024 contact compiler sends one literal word to a guarded
partial-affine profile ``p=(Delta,H)``.  The cycle-witness repair layer declares
an additive readout ``C j`` of cumulative contact-action counts ``j``.

This module combines them without re-expanding literal words.  A witnessed
profile is

    (p, w),       w = C j,

and acts on exact extended state ``(r,z)`` by

    (r,z) -> (r+Delta, z+w)

on the same causal domain carried by ``H``.

Concatenation is exact:

    (p,w) * (q,v) = (p*q, w+v).

Hence zero-score-shift cycle profiles form the product of the causal-domain
idempotent semilattice with the additive witness lattice.  If the witness state
is an exact integer lattice, such a profile is idempotent iff its witness shift
is zero.  A coarse cycle can therefore stabilize after one traversal while an
exact declared witness continues changing linearly forever.

For incidence B and additive witness C, the static factorization condition

    ker_Z B subseteq ker_Z C

is exactly the condition that every cycle-lattice word has zero witness shift.
So the P023 factorization test and the dynamic guarded-operation test are the
same boundary viewed from state and operation sides.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .contact_cycle_witness_repair import apply_integer_matrix
from .contact_guarded_word_normal_form import (
    ContactGuardedOutcome,
    ContactGuardedWordProfile,
    apply_contact_guarded_profile,
    compose_contact_guarded_profiles,
    contact_guarded_profile_power,
    contact_guarded_word_profile,
    contact_profile_separating_state,
    contact_word_action_counts,
    empty_contact_guarded_profile,
)


Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _vector(values: Iterable[int], size: int, *, name: str) -> Vector:
    result = tuple(values)
    if len(result) != size:
        raise ValueError(f"{name} must have length {size}")
    for value in result:
        _require_int(name, value)
    return result


def _witness_matrix(
    values: Sequence[Sequence[int]] | Iterable[Sequence[int]],
    edge_count: int,
) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError("witness_matrix must contain at least one row")
    if any(len(row) != edge_count for row in rows):
        raise ValueError("witness_matrix width must equal contact count")
    for row in rows:
        for value in row:
            _require_int("witness entry", value)
    return rows


def _add(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ValueError("witness dimensions must agree")
    return tuple(a + b for a, b in zip(left, right, strict=True))


@dataclass(frozen=True)
class WitnessedContactGuardedProfile:
    coarse_profile: ContactGuardedWordProfile
    witness_shift: Vector

    @property
    def dimension(self) -> int:
        return self.coarse_profile.dimension

    @property
    def witness_dimension(self) -> int:
        return len(self.witness_shift)

    @property
    def is_idempotent(self) -> bool:
        return (
            self.coarse_profile.is_partial_identity
            and all(value == 0 for value in self.witness_shift)
        )


@dataclass(frozen=True)
class WitnessedContactGuardedOutcome:
    defined: bool
    score_state: Vector | None
    witness_state: Vector | None


def contact_guarded_witness_profile(
    coupling: Sequence[Sequence[int]],
    witness_matrix: Sequence[Sequence[int]],
    word: Iterable[int],
) -> WitnessedContactGuardedProfile:
    actions = tuple(word)
    coarse = contact_guarded_word_profile(coupling, actions)
    witness = _witness_matrix(witness_matrix, coarse.dimension)
    counts = contact_word_action_counts(actions, coarse.dimension)
    return WitnessedContactGuardedProfile(
        coarse_profile=coarse,
        witness_shift=apply_integer_matrix(witness, counts),
    )


def apply_contact_guarded_witness_profile(
    score_state: Sequence[int],
    witness_state: Sequence[int],
    profile: WitnessedContactGuardedProfile,
) -> WitnessedContactGuardedOutcome:
    witness = _vector(
        witness_state,
        profile.witness_dimension,
        name="witness_state",
    )
    coarse_outcome: ContactGuardedOutcome = apply_contact_guarded_profile(
        score_state,
        profile.coarse_profile,
    )
    if not coarse_outcome.defined:
        return WitnessedContactGuardedOutcome(False, None, None)
    assert coarse_outcome.state is not None
    return WitnessedContactGuardedOutcome(
        True,
        coarse_outcome.state,
        _add(witness, profile.witness_shift),
    )


def compose_contact_guarded_witness_profiles(
    first: WitnessedContactGuardedProfile,
    second: WitnessedContactGuardedProfile,
) -> WitnessedContactGuardedProfile:
    if first.witness_dimension != second.witness_dimension:
        raise ValueError("witness dimensions must agree")
    return WitnessedContactGuardedProfile(
        coarse_profile=compose_contact_guarded_profiles(
            first.coarse_profile,
            second.coarse_profile,
        ),
        witness_shift=_add(first.witness_shift, second.witness_shift),
    )


def contact_guarded_witness_profile_power(
    profile: WitnessedContactGuardedProfile,
    exponent: int,
) -> WitnessedContactGuardedProfile:
    _require_int("exponent", exponent)
    if exponent < 0:
        raise ValueError("exponent must be non-negative")
    return WitnessedContactGuardedProfile(
        coarse_profile=contact_guarded_profile_power(
            profile.coarse_profile,
            exponent,
        ),
        witness_shift=tuple(
            exponent * value for value in profile.witness_shift
        ),
    )


def empty_contact_guarded_witness_profile(
    contact_dimension: int,
    witness_dimension: int,
) -> WitnessedContactGuardedProfile:
    _require_int("witness_dimension", witness_dimension)
    if witness_dimension <= 0:
        raise ValueError("witness_dimension must be positive")
    return WitnessedContactGuardedProfile(
        coarse_profile=empty_contact_guarded_profile(contact_dimension),
        witness_shift=(0,) * witness_dimension,
    )


def witnessed_profile_separating_state(
    left: WitnessedContactGuardedProfile,
    right: WitnessedContactGuardedProfile,
) -> tuple[Vector, Vector]:
    """Construct an extended state distinguishing two distinct profiles."""
    if left.dimension != right.dimension:
        raise ValueError("contact dimensions must agree")
    if left.witness_dimension != right.witness_dimension:
        raise ValueError("witness dimensions must agree")
    if left == right:
        raise ValueError("equal profiles have no separating state")

    if left.coarse_profile != right.coarse_profile:
        score = contact_profile_separating_state(
            left.coarse_profile,
            right.coarse_profile,
        )
    else:
        score = tuple(
            0 if requirement is None else -requirement - 1
            for requirement in left.coarse_profile.requirements
        )
    return score, (0,) * left.witness_dimension


def zero_shift_witness_product(
    left: WitnessedContactGuardedProfile,
    right: WitnessedContactGuardedProfile,
) -> WitnessedContactGuardedProfile:
    if (
        not left.coarse_profile.is_partial_identity
        or not right.coarse_profile.is_partial_identity
    ):
        raise ValueError("zero-shift product requires coarse partial identities")
    return compose_contact_guarded_witness_profiles(left, right)
