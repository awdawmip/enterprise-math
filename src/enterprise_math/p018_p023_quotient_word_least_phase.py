"""Least-alphabet phase diagram for bounded quotient-word languages.

This module refines the bounded quotient-word generator bridge by separating
three different inclusion orders:

* one-step semantic actions;
* finite-horizon primitive quotient generators;
* the forced-generator core shared by every separating primitive alphabet.

For root order ``r>=2`` and exact states ``0,...,N``:

* horizon 1 has a unique least primitive alphabet: every nontrivial
  ``r``-power-free boundary ``2<=b<=N``;
* every horizon ``h>=2`` has forced-generator core exactly the primes ``p<=N``;
* therefore a least alphabet exists for ``h>=2`` iff the prime alphabet itself
  separates at that horizon;
* equivalently, with ``L_r(N)=max Omega(b)`` over bounded positive
  ``r``-power-free boundaries, the intermediate regime ``2<=h<L_r(N)`` has no
  least separating alphabet, while ``h>=L_r(N)`` has the primes as its unique
  least alphabet.

The key omission witness is elementary. Start from the complete nontrivial
power-free one-step basis and delete one composite ``g``. If ``g`` is not a
required power-free boundary, nothing changes. If it is required, write
``g=a*b`` with ``a,b>1``; both proper factors are again power-free and remain in
the alphabet, so the two-letter word ``(a,b)`` recovers the deleted boundary.

Prime factorization, power-free arithmetic, and inclusion-minimal set systems
are prior mathematics. This file is only the executable quotient-root
specialization of the finite-horizon phase diagram.
"""

from __future__ import annotations

from .p018_p023_power_free_action_basis import minimal_root_quotient_action_basis
from .p018_p023_quotient_word_basis import (
    prime_generator_basis,
    prime_generator_required_horizon,
)


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_root_exp(root_exp: int) -> None:
    if isinstance(root_exp, bool) or not isinstance(root_exp, int) or root_exp < 2:
        raise ValueError("root_exp must be an integer at least 2")


def nontrivial_power_free_word_basis(
    max_state: int, root_exp: int
) -> tuple[int, ...]:
    """Return the exact horizon-one primitive alphabet.

    Denominator one is supplied by the empty word/current observation, so it is
    removed from the canonical one-step action basis.
    """
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    return tuple(
        b
        for b in minimal_root_quotient_action_basis(max_state, root_exp)
        if b >= 2
    )


def forced_generator_core_at_horizon(
    max_state: int, root_exp: int, horizon: int
) -> tuple[int, ...]:
    """Return the intersection of all separating primitive alphabets.

    For horizon one every required nontrivial power-free boundary is forced.
    For every horizon at least two, exactly the bounded primes are forced.
    """
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    _require_natural("horizon", horizon)
    if horizon == 0:
        raise ValueError("forced core is only defined here for positive horizons")
    if horizon == 1:
        return nontrivial_power_free_word_basis(max_state, root_exp)
    return prime_generator_basis(max_state)


def least_primitive_generator_alphabet_at_horizon(
    max_state: int, root_exp: int, horizon: int
) -> tuple[int, ...] | None:
    """Return the unique least separating primitive alphabet, if it exists.

    ``None`` means that no least separating alphabet exists at the requested
    horizon (either because there is no separator at all, or because separating
    alphabets form incomparable alternatives).
    """
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    _require_natural("horizon", horizon)
    if horizon == 0:
        # For r>=2, current observation alone separates 0,...,N exactly only
        # on the trivial domain N<=1.
        return () if max_state <= 1 else None
    if horizon == 1:
        return nontrivial_power_free_word_basis(max_state, root_exp)
    required = prime_generator_required_horizon(max_state, root_exp)
    if horizon >= required:
        return prime_generator_basis(max_state)
    return None


def least_alphabet_phase(
    max_state: int, root_exp: int, horizon: int
) -> str:
    """Classify the finite-horizon inclusion phase."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    _require_natural("horizon", horizon)
    if horizon == 0:
        return "TRIVIAL_CURRENT_ONLY" if max_state <= 1 else "NO_SEPARATOR"
    if horizon == 1:
        return "ONE_STEP_POWER_FREE_LEAST"
    required = prime_generator_required_horizon(max_state, root_exp)
    if horizon >= required:
        return "PRIME_LEAST"
    return "NO_LEAST"


def composite_omission_witness_alphabet(
    max_state: int, root_exp: int, omitted: int
) -> tuple[int, ...]:
    """Return a horizon-two separating candidate that omits one composite.

    The theorem applies to every composite ``2<=omitted<=N``. If ``omitted``
    is itself a required power-free boundary, its two proper factors remain in
    this alphabet and their two-letter product recovers it. If it is not
    power-free, it was never a required boundary in the first place.
    """
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    _require_natural("omitted", omitted)
    if omitted < 4 or omitted > max_state:
        raise ValueError("omitted must be a composite integer in 4,...,max_state")
    if _is_prime(omitted):
        raise ValueError("omitted must be composite")
    return tuple(
        b
        for b in nontrivial_power_free_word_basis(max_state, root_exp)
        if b != omitted
    )


def deleted_composite_two_factor_word(omitted: int) -> tuple[int, int]:
    """Return two proper factors whose product is the composite ``omitted``."""
    _require_natural("omitted", omitted)
    if omitted < 4 or _is_prime(omitted):
        raise ValueError("omitted must be composite")
    divisor = 2
    while omitted % divisor != 0:
        divisor += 1
    return divisor, omitted // divisor


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def omission_witness_is_structurally_valid(
    max_state: int, root_exp: int, omitted: int
) -> bool:
    """Check the elementary two-factor omission theorem without word search."""
    alphabet = set(
        composite_omission_witness_alphabet(max_state, root_exp, omitted)
    )
    # Non-power-free omitted values were never required boundaries.
    canonical = set(minimal_root_quotient_action_basis(max_state, root_exp))
    if omitted not in canonical:
        return omitted not in alphabet
    left, right = deleted_composite_two_factor_word(omitted)
    return (
        omitted not in alphabet
        and left in alphabet
        and right in alphabet
        and left * right == omitted
    )
