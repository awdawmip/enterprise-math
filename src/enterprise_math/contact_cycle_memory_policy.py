"""Finite and periodic memory policies for guarded contact-cycle witnesses.

A witnessed guarded contact macro already has exact state

    (coarse profile, witness shift w).

The exact additive witness state is torsion-free: a nonzero cycle witness keeps
accumulating under powers.  This module studies two *explicitly declared*
finite-memory policies without pretending either is an automatic material law.

1. Capacity guard.  For a nonnegative witness increment ``w``, current witness
   ``z`` and finite capacity ``c``, the macro is enabled on the witness side iff

       z + w <= c

   coordinatewise.  Its exact remaining witness lifetime is

       min_{w_i>0} floor((c_i-z_i)/w_i),

   with infinity when ``w=0``.  Combined with the already-compiled coarse
   repetition capacity, total macro lifetime is the minimum of the two.
   Every legal execution decrements any finite total lifetime by exactly one.
   Therefore, for a future language that observes only which powers remain
   defined, the coarsest horizon-h state is the capped scalar lifetime

       min(h, tau).

2. Componentwise modulo quotient.  If witness state is deliberately quotiented
   by ``Z/m_1 x ... x Z/m_q``, translation by ``w`` has exact period

       lcm_i m_i/gcd(m_i,w_i).

Capacity exhaustion and modulo periodicity are different world laws: one stops
at a boundary, the other wraps and cycles.  Neither behavior follows from the
exact additive witness by itself.

The intended E001/P024 use is a pressure test for finite material memory.  A
real damage/fatigue interpretation still requires an independently declared
nonnegative witness and capacity/quotient law.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, lcm
from typing import Iterable, Sequence

from .contact_guarded_witness_normal_form import (
    WitnessedContactGuardedOutcome,
    WitnessedContactGuardedProfile,
    apply_contact_guarded_witness_profile,
)
from .contact_guarded_word_normal_form import (
    contact_guarded_profile_repetition_capacity,
)


Vector = tuple[int, ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _vector(
    values: Sequence[int] | Iterable[int],
    *,
    name: str,
    length: int | None = None,
) -> Vector:
    result = tuple(values)
    if length is not None and len(result) != length:
        raise ValueError(f"{name} must have length {length}")
    if not result:
        raise ValueError(f"{name} must be nonempty")
    for value in result:
        _require_int(name, value)
    return result


def _nonnegative_vector(
    values: Sequence[int] | Iterable[int],
    *,
    name: str,
    length: int | None = None,
) -> Vector:
    result = _vector(values, name=name, length=length)
    if any(value < 0 for value in result):
        raise ValueError(f"{name} must be nonnegative")
    return result


def _minimum_capacity(
    left: int | None,
    right: int | None,
) -> int | None:
    """Minimum with ``None`` interpreted as positive infinity."""
    if left is None:
        return right
    if right is None:
        return left
    return min(left, right)


def witness_capacity_repetition_capacity(
    witness_state: Sequence[int] | Iterable[int],
    capacity: Sequence[int] | Iterable[int],
    increment: Sequence[int] | Iterable[int],
) -> int | None:
    """Exact number of further increments before a finite witness guard fails.

    ``None`` means unbounded.  This finite-resource policy deliberately requires
    a nonnegative additive increment; a signed witness is not silently re-read
    as monotone damage.
    """
    state = _nonnegative_vector(witness_state, name="witness_state")
    limits = _nonnegative_vector(
        capacity,
        name="capacity",
        length=len(state),
    )
    step = _nonnegative_vector(
        increment,
        name="increment",
        length=len(state),
    )
    if any(value > limit for value, limit in zip(state, limits, strict=True)):
        raise ValueError("witness_state must lie inside capacity")

    finite = [
        (limit - value) // delta
        for value, limit, delta in zip(state, limits, step, strict=True)
        if delta > 0
    ]
    return min(finite) if finite else None


def combined_witnessed_repetition_capacity(
    score_state: Sequence[int],
    witness_state: Sequence[int],
    capacity: Sequence[int],
    profile: WitnessedContactGuardedProfile,
) -> int | None:
    """Exact repeated-macro lifetime under coarse and witness guards."""
    if any(value < 0 for value in profile.witness_shift):
        raise ValueError(
            "finite witness capacity requires a nonnegative witness increment"
        )
    coarse = contact_guarded_profile_repetition_capacity(
        score_state,
        profile.coarse_profile,
    )
    witness = witness_capacity_repetition_capacity(
        witness_state,
        capacity,
        profile.witness_shift,
    )
    return _minimum_capacity(coarse, witness)


def apply_capacity_guarded_witness_profile(
    score_state: Sequence[int],
    witness_state: Sequence[int],
    capacity: Sequence[int],
    profile: WitnessedContactGuardedProfile,
) -> WitnessedContactGuardedOutcome:
    """Apply one macro only when both coarse and finite-witness guards allow it."""
    state = _nonnegative_vector(
        witness_state,
        name="witness_state",
        length=profile.witness_dimension,
    )
    limits = _nonnegative_vector(
        capacity,
        name="capacity",
        length=profile.witness_dimension,
    )
    if any(value > limit for value, limit in zip(state, limits, strict=True)):
        raise ValueError("witness_state must lie inside capacity")
    if any(value < 0 for value in profile.witness_shift):
        raise ValueError(
            "finite witness capacity requires a nonnegative witness increment"
        )
    if any(
        value + delta > limit
        for value, delta, limit in zip(
            state,
            profile.witness_shift,
            limits,
            strict=True,
        )
    ):
        return WitnessedContactGuardedOutcome(False, None, None)
    return apply_contact_guarded_witness_profile(
        score_state,
        state,
        profile,
    )


def capped_repetition_lifetime(
    lifetime: int | None,
    horizon: int,
) -> int:
    """Task-relative horizon state; ``None`` means infinite lifetime."""
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    if lifetime is None:
        return horizon
    _require_int("lifetime", lifetime)
    if lifetime < 0:
        raise ValueError("lifetime must be nonnegative")
    return min(lifetime, horizon)


def repeated_definedness_signature_from_lifetime(
    lifetime: int | None,
    horizon: int,
) -> tuple[bool, ...]:
    """Definedness of powers ``p^0,...,p^h`` from one lifetime coordinate."""
    capped = capped_repetition_lifetime(lifetime, horizon)
    return tuple(exponent <= capped for exponent in range(horizon + 1))


def repeated_definedness_signature(
    score_state: Sequence[int],
    witness_state: Sequence[int],
    capacity: Sequence[int],
    profile: WitnessedContactGuardedProfile,
    horizon: int,
) -> tuple[bool, ...]:
    lifetime = combined_witnessed_repetition_capacity(
        score_state,
        witness_state,
        capacity,
        profile,
    )
    return repeated_definedness_signature_from_lifetime(
        lifetime,
        horizon,
    )


def lifetime_separating_exponent(
    left_lifetime: int | None,
    right_lifetime: int | None,
    horizon: int,
) -> int:
    """Return a bounded power whose definedness separates unequal capped lifetimes."""
    left = capped_repetition_lifetime(left_lifetime, horizon)
    right = capped_repetition_lifetime(right_lifetime, horizon)
    if left == right:
        raise ValueError("equal capped lifetimes have no bounded separator")
    return min(left, right) + 1


def exact_additive_witness_period(
    increment: Sequence[int] | Iterable[int],
) -> int | None:
    """Period of exact integer translation: 1 only for zero shift, else infinite."""
    step = _vector(increment, name="increment")
    return 1 if all(value == 0 for value in step) else None


def componentwise_modulo_witness_period(
    increment: Sequence[int] | Iterable[int],
    moduli: Sequence[int] | Iterable[int],
) -> int:
    """Exact order of one translation in a product of finite cyclic groups."""
    step = _vector(increment, name="increment")
    mods = _vector(moduli, name="moduli", length=len(step))
    if any(modulus <= 0 for modulus in mods):
        raise ValueError("moduli must be positive")

    period = 1
    for delta, modulus in zip(step, mods, strict=True):
        coordinate_order = modulus // gcd(modulus, abs(delta))
        period = lcm(period, coordinate_order)
    return period


def modulo_witness_after_repetitions(
    witness_state: Sequence[int] | Iterable[int],
    increment: Sequence[int] | Iterable[int],
    moduli: Sequence[int] | Iterable[int],
    repetitions: int,
) -> Vector:
    state = _vector(witness_state, name="witness_state")
    step = _vector(increment, name="increment", length=len(state))
    mods = _vector(moduli, name="moduli", length=len(state))
    if any(modulus <= 0 for modulus in mods):
        raise ValueError("moduli must be positive")
    _require_int("repetitions", repetitions)
    if repetitions < 0:
        raise ValueError("repetitions must be nonnegative")
    return tuple(
        (value + repetitions * delta) % modulus
        for value, delta, modulus in zip(
            state,
            step,
            mods,
            strict=True,
        )
    )


@dataclass(frozen=True)
class CycleMemoryPolicyReport:
    exact_additive_period: int | None
    finite_capacity_lifetime: int | None
    modulo_period: int


def cycle_memory_policy_report(
    witness_state: Sequence[int],
    capacity: Sequence[int],
    increment: Sequence[int],
    moduli: Sequence[int],
) -> CycleMemoryPolicyReport:
    return CycleMemoryPolicyReport(
        exact_additive_period=exact_additive_witness_period(increment),
        finite_capacity_lifetime=witness_capacity_repetition_capacity(
            witness_state,
            capacity,
            increment,
        ),
        modulo_period=componentwise_modulo_witness_period(
            increment,
            moduli,
        ),
    )
