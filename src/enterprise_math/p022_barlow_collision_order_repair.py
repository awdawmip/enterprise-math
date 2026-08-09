"""Exact order-repair cardinality after collision-polynomial geometry recovery.

The complete P011 collision polynomial of a selected-layer Barlow quotient
recovers the observed segment-length *multiset* and hidden tail length exactly,
but commutative fiber convolution forgets the order of those segments.

For multiplicities t_ell of equal segment lengths, the remaining ordered
checkpoint-geometry fiber has exactly

    m! / product_ell t_ell!

distinct members.  This module keeps that last identifiability loss finite and
integer-valued.
"""

from __future__ import annotations

from collections import Counter
from math import comb, factorial

from .p022_barlow_collision_geometry import (
    CollisionCoefficients,
    collision_coefficients_from_selected_layers,
    recover_checkpoint_geometry_from_collision_coefficients,
)


def _require_segments(segments: tuple[int, ...]) -> None:
    if not isinstance(segments, tuple) or any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in segments
    ):
        raise ValueError("segments must be a tuple of positive integers")


def checkpoint_layers_from_ordered_segments(
    segments: tuple[int, ...], hidden_tail: int = 0
) -> tuple[int, ...]:
    """Convert one ordered segment sequence to its selected checkpoint layers."""
    _require_segments(segments)
    if isinstance(hidden_tail, bool) or not isinstance(hidden_tail, int) or hidden_tail < 0:
        raise ValueError("hidden_tail must be a non-negative integer")
    running = 0
    layers = []
    for segment in segments:
        running += segment
        layers.append(running)
    # The hidden tail changes total horizon but not the selected layer positions.
    _ = hidden_tail
    return tuple(layers)


def ordered_segment_geometry_fiber_size(segments: tuple[int, ...]) -> int:
    """Number of distinct ordered segment sequences with this multiset."""
    _require_segments(segments)
    multiplicities = Counter(segments)
    numerator = factorial(len(segments))
    denominator = 1
    for count in multiplicities.values():
        denominator *= factorial(count)
    if numerator % denominator:
        raise AssertionError("multiset permutation count must be integral")
    return numerator // denominator


def ordered_geometry_fiber_size_from_collision_coefficients(
    coefficients: CollisionCoefficients,
) -> int:
    """Remaining checkpoint-order ambiguity after complete P011 inversion."""
    segments, _hidden_tail = recover_checkpoint_geometry_from_collision_coefficients(
        coefficients
    )
    return ordered_segment_geometry_fiber_size(segments)


def complete_geometry_state_cardinality_from_collision(
    coefficients: CollisionCoefficients,
) -> tuple[tuple[int, ...], int, int]:
    """Return ``(segment multiset, hidden tail, order-repair cardinality)``."""
    segments, hidden_tail = recover_checkpoint_geometry_from_collision_coefficients(
        coefficients
    )
    return (
        segments,
        hidden_tail,
        ordered_segment_geometry_fiber_size(segments),
    )


def balanced_schedule_order_fiber_size(
    length: int, checkpoint_count: int
) -> int:
    """Order ambiguity of the ordinary balanced final-observing schedule.

    If ``N=q*m+r`` with ``0<=r<m``, balanced segment lengths are ``q`` repeated
    ``m-r`` times and ``q+1`` repeated ``r`` times.  Hence the number of
    distinct ordered placements is exactly ``C(m,r)``.  When ``r=0`` the
    collision polynomial identifies the unique equal-spacing schedule fully.
    """
    if isinstance(length, bool) or not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")
    if (
        isinstance(checkpoint_count, bool)
        or not isinstance(checkpoint_count, int)
        or checkpoint_count <= 0
        or checkpoint_count > length
    ):
        raise ValueError("checkpoint_count must lie in 1..length")
    _base, remainder = divmod(length, checkpoint_count)
    return comb(checkpoint_count, remainder)


def collision_coefficients_ignore_segment_order(
    segments: tuple[int, ...], hidden_tail: int = 0
) -> CollisionCoefficients:
    """Build collision coefficients from one ordered schedule for comparisons."""
    _require_segments(segments)
    if isinstance(hidden_tail, bool) or not isinstance(hidden_tail, int) or hidden_tail < 0:
        raise ValueError("hidden_tail must be a non-negative integer")
    selected_layers = checkpoint_layers_from_ordered_segments(segments, hidden_tail)
    total_length = sum(segments) + hidden_tail
    return collision_coefficients_from_selected_layers(total_length, selected_layers)
