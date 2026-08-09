"""Task-relative finite precision for Barlow stacking words.

For root-to-one-target-layer distance plus shortest-path-count queries, the
literal order of close-packed interface choices is not required.  The exact
state is the integer prefix imbalance

    delta_k = (# effective + interfaces) - (# effective - interfaces).

The target layer k is part of the query context, so k and delta_k recover the
two cumulative interface counts.  This module exposes the exact normal form,
a moment-based recovery map proving minimality for the full target-layer count
language, and selected-layer precision vectors.
"""

from __future__ import annotations

from .p022_barlow_stacking import (
    LaurentPolynomial,
    StackingPattern,
    stacking_prefix_counts,
    stacking_prefix_imbalance,
    vertical_witness_polynomial,
    vertical_witness_polynomial_from_counts,
)


def _require_layer(layer: int) -> None:
    if isinstance(layer, bool) or not isinstance(layer, int):
        raise ValueError("layer must be an integer")


def _require_imbalance(vertical_length: int, imbalance: int) -> None:
    if isinstance(vertical_length, bool) or not isinstance(vertical_length, int) or vertical_length < 0:
        raise ValueError("vertical_length must be a non-negative integer")
    if isinstance(imbalance, bool) or not isinstance(imbalance, int):
        raise ValueError("imbalance must be an integer")
    if abs(imbalance) > vertical_length:
        raise ValueError("imbalance magnitude cannot exceed vertical length")
    if (vertical_length - imbalance) % 2 != 0:
        raise ValueError("vertical length and imbalance must have the same parity")


def counts_from_length_and_imbalance(
    vertical_length: int, imbalance: int
) -> tuple[int, int]:
    """Return ``(minus_count, plus_count)`` from ``(k,delta)`` exactly."""
    _require_imbalance(vertical_length, imbalance)
    minus_count = (vertical_length - imbalance) // 2
    plus_count = (vertical_length + imbalance) // 2
    return minus_count, plus_count


def barlow_prefix_normal_form(
    pattern: StackingPattern, target_layer: int
) -> tuple[int, int, int]:
    """Return ``(paired_opposites, drift_sign, drift_count)``.

    Because ``B_- B_+ = A+3`` and Laurent multiplication is commutative,

        P_k = (A+3)^paired * B_sign^drift_count.

    Here ``drift_sign`` is -1, 0, or +1.  The normal form is equivalent to the
    cumulative sign counts for the root-to-target-layer language.
    """
    _require_layer(target_layer)
    minus_count, plus_count = stacking_prefix_counts(pattern, target_layer)
    paired = min(minus_count, plus_count)
    if plus_count > minus_count:
        return paired, 1, plus_count - minus_count
    if minus_count > plus_count:
        return paired, -1, minus_count - plus_count
    return paired, 0, 0


def vertical_polynomial_from_imbalance(
    vertical_length: int, imbalance: int
) -> LaurentPolynomial:
    """Reconstruct the full vertical witness polynomial from the scalar state."""
    minus_count, plus_count = counts_from_length_and_imbalance(
        vertical_length, imbalance
    )
    return vertical_witness_polynomial_from_counts(minus_count, plus_count)


def vertical_polynomial_moments(
    polynomial: LaurentPolynomial,
) -> tuple[int, int, int]:
    """Return total mass and first q/r exponent moments of a Laurent polynomial."""
    if not polynomial:
        raise ValueError("polynomial must be nonempty")
    if any(
        isinstance(coefficient, bool)
        or not isinstance(coefficient, int)
        or coefficient < 0
        for coefficient in polynomial.values()
    ):
        raise ValueError("coefficients must be non-negative integers")
    mass = sum(polynomial.values())
    q_moment = sum(q * coefficient for (q, _), coefficient in polynomial.items())
    r_moment = sum(r * coefficient for (_, r), coefficient in polynomial.items())
    return mass, q_moment, r_moment


def recover_imbalance_from_vertical_polynomial(
    polynomial: LaurentPolynomial, vertical_length: int
) -> int:
    """Recover ``delta_k`` from the complete target-layer witness polynomial.

    Each interface polynomial has mass 3.  ``B_+`` has first q/r moment +1 and
    ``B_-`` has first q/r moment -1.  The product rule for first moments gives

        M(P_k)=3^k,
        Q(P_k)=R(P_k)=delta_k * 3^(k-1)    (k>0).

    Therefore the full target-layer count language cannot identify two
    different imbalance values: delta is recoverable from its t=0 coefficient
    function.
    """
    if isinstance(vertical_length, bool) or not isinstance(vertical_length, int) or vertical_length < 0:
        raise ValueError("vertical_length must be a non-negative integer")
    mass, q_moment, r_moment = vertical_polynomial_moments(polynomial)
    expected_mass = 3 ** vertical_length
    if mass != expected_mass:
        raise ValueError("polynomial mass is incompatible with vertical length")
    if vertical_length == 0:
        if q_moment != 0 or r_moment != 0:
            raise ValueError("zero-length vertical polynomial must have zero moment")
        return 0
    scale = 3 ** (vertical_length - 1)
    if q_moment != r_moment or q_moment % scale != 0:
        raise ValueError("polynomial moments are incompatible with a Barlow prefix")
    imbalance = q_moment // scale
    _require_imbalance(vertical_length, imbalance)
    return imbalance


def selected_layer_imbalance_state(
    pattern: StackingPattern, target_layers: tuple[int, ...]
) -> tuple[int, ...]:
    """Exact state for root-to-selected-layer metric+count languages.

    Layer indices are query context.  The returned coordinate at each selected
    layer is the only stacking-prefix scalar required to reconstruct that
    layer's complete vertical witness polynomial.
    """
    if not isinstance(target_layers, tuple):
        raise ValueError("target_layers must be a tuple")
    for layer in target_layers:
        _require_layer(layer)
    return tuple(stacking_prefix_imbalance(pattern, layer) for layer in target_layers)


def recover_upward_sign_word_from_full_trajectory(
    imbalances: tuple[int, ...]
) -> tuple[int, ...]:
    """Recover signs when every upward prefix layer 1..N is observed.

    With delta_0=0, the interface sign is exactly delta_j-delta_(j-1).  Thus
    preserving the full prefix-imbalance trajectory is equivalent to preserving
    the literal stacking word; compression only appears when the future
    language queries a strict subset of layers.
    """
    if not isinstance(imbalances, tuple):
        raise ValueError("imbalances must be a tuple")
    previous = 0
    signs = []
    for current in imbalances:
        if isinstance(current, bool) or not isinstance(current, int):
            raise ValueError("imbalance entries must be integers")
        step = current - previous
        if step not in (-1, 1):
            raise ValueError("full prefix trajectory must change by exactly one")
        signs.append(step)
        previous = current
    return tuple(signs)


def target_layer_polynomial_matches_scalar_state(
    pattern: StackingPattern, target_layer: int
) -> bool:
    """Executable audit of the scalar sufficient-state theorem."""
    _require_layer(target_layer)
    direct = vertical_witness_polynomial(pattern, target_layer)
    imbalance = stacking_prefix_imbalance(pattern, target_layer)
    reconstructed = vertical_polynomial_from_imbalance(abs(target_layer), imbalance)
    return direct == reconstructed
