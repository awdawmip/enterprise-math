"""Exact aliasing of checkpoint geometries under pair-collision J2.

For a final-observing Barlow checkpoint schedule with segment lengths ell_j,

    M2 = product_j C(2 ell_j, ell_j)
    J2 = (M2 - 2^N)/2.

Different segment multisets can have the same product.  The first such alias in
the finite segment-multiset search by total length occurs at N=21,m=4:

    (1,5,5,10) and (2,2,6,11).

They have identical J2 but different image size, J3, maximum fiber, and complete
fiber profile.  Thus pair ambiguity is not an identifying statistic for the
checkpoint geometry even when N and m are fixed.
"""

from __future__ import annotations

from math import comb, prod

from .p022_barlow_fiber_convolution import (
    profile_collision_count,
    profile_from_segments,
    profile_image_size,
)

SegmentMultiset = tuple[int, ...]


def _require_segments(segments: SegmentMultiset) -> None:
    if not isinstance(segments, tuple) or not segments or any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in segments
    ):
        raise ValueError("segments must be a nonempty tuple of positive integers")


def central_binomial_factor(segment_length: int) -> int:
    if isinstance(segment_length, bool) or not isinstance(segment_length, int) or segment_length <= 0:
        raise ValueError("segment_length must be positive")
    return comb(2 * segment_length, segment_length)


def pair_moment_from_segments(segments: SegmentMultiset) -> int:
    """Ordered equal-observation pair moment M2."""
    _require_segments(segments)
    return prod(central_binomial_factor(length) for length in segments)


def pair_collision_from_segments(segments: SegmentMultiset) -> int:
    """P011 J2 for a final-observing segment schedule."""
    _require_segments(segments)
    length = sum(segments)
    moment = pair_moment_from_segments(segments)
    difference = moment - 2 ** length
    if difference < 0 or difference % 2:
        raise AssertionError("pair moment must split into diagonal plus reversed pairs")
    return difference // 2


def first_pair_collision_alias() -> tuple[SegmentMultiset, SegmentMultiset]:
    """Exact N=21,m=4 alias used by the theorem note."""
    return (1, 5, 5, 10), (2, 2, 6, 11)


def verify_first_alias_identity() -> dict[str, int]:
    """Return exact invariants of the N=21 alias and verify the identity."""
    left, right = first_pair_collision_alias()
    left_m2 = pair_moment_from_segments(left)
    right_m2 = pair_moment_from_segments(right)
    if left_m2 != right_m2:
        raise AssertionError("declared central-binomial product identity failed")

    left_profile = profile_from_segments(left)
    right_profile = profile_from_segments(right)
    if left_profile == right_profile:
        raise AssertionError("pair alias must not collapse the complete profile")

    return {
        "length": sum(left),
        "checkpoint_count": len(left),
        "M2": left_m2,
        "J2": pair_collision_from_segments(left),
        "left_image": profile_image_size(left_profile),
        "right_image": profile_image_size(right_profile),
        "left_J3": profile_collision_count(left_profile, 3),
        "right_J3": profile_collision_count(right_profile, 3),
    }


def cleaner_three_segment_alias() -> tuple[SegmentMultiset, SegmentMultiset]:
    """A slightly later but algebraically simpler N=22,m=3 alias."""
    return (1, 4, 17), (2, 2, 18)
