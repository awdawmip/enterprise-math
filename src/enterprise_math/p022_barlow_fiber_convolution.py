"""Multiplicative convolution algebra of Barlow checkpoint fiber profiles.

For a segment of length ell, each represented imbalance has microscopic fiber
size C(ell,j).  Record only the size distribution

    B_ell(s) = #{j : C(ell,j)=s}.

Independent checkpoint segments multiply fiber sizes, so complete fiber-size
profiles compose by finite Dirichlet/multiplicative convolution.  Power moments
are multiplicative characters of this convolution, explaining the generalized
binomial power-sum factorization used by the higher-collision layer.
"""

from __future__ import annotations

from math import comb

from .p022_barlow_precision_fibers import selected_segment_lengths

FiberProfile = tuple[tuple[int, int], ...]  # (fiber_size, number_of_observation_fibers)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def segment_binomial_fiber_profile(segment_length: int) -> FiberProfile:
    """Complete fiber-size profile of one observed prefix-imbalance segment."""
    _require_positive("segment_length", segment_length)
    counts: dict[int, int] = {}
    for plus_count in range(segment_length + 1):
        size = comb(segment_length, plus_count)
        counts[size] = counts.get(size, 0) + 1
    return tuple(sorted(counts.items()))


def multiplicative_profile_convolution(
    left: FiberProfile, right: FiberProfile
) -> FiberProfile:
    """Finite multiplicative/Dirichlet convolution of two fiber profiles."""
    counts: dict[int, int] = {}
    for left_size, left_count in left:
        for right_size, right_count in right:
            size = left_size * right_size
            counts[size] = counts.get(size, 0) + left_count * right_count
    return tuple(sorted(counts.items()))


def profile_from_segments(segments: tuple[int, ...]) -> FiberProfile:
    """Complete fiber-size distribution for final-observing segment lengths."""
    if not isinstance(segments, tuple) or any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in segments
    ):
        raise ValueError("segments must be a tuple of positive integers")
    profile: FiberProfile = ((1, 1),)
    for segment in segments:
        profile = multiplicative_profile_convolution(
            profile, segment_binomial_fiber_profile(segment)
        )
    return profile


def scale_profile_fiber_sizes(profile: FiberProfile, factor: int) -> FiberProfile:
    """Multiply every represented fiber size by one positive integer factor."""
    _require_positive("factor", factor)
    return tuple((size * factor, count) for size, count in profile)


def profile_from_selected_layers(
    length: int, selected_layers: tuple[int, ...]
) -> FiberProfile:
    """Complete selected-layer fiber profile, including an unobserved tail."""
    segments, tail = selected_segment_lengths(length, selected_layers)
    profile = profile_from_segments(segments) if segments else ((1, 1),)
    if tail:
        profile = scale_profile_fiber_sizes(profile, 2 ** tail)
    return profile


def profile_image_size(profile: FiberProfile) -> int:
    """Number of observable quotient states."""
    return sum(count for _, count in profile)


def profile_domain_size(profile: FiberProfile) -> int:
    """Number of microscopic states reconstructed by the fiber profile."""
    return sum(size * count for size, count in profile)


def profile_power_moment(profile: FiberProfile, order: int) -> int:
    """M_order=sum_s c_s s^order; a character of multiplicative convolution."""
    _require_positive("order", order)
    return sum(count * (size ** order) for size, count in profile)


def profile_collision_count(profile: FiberProfile, order: int) -> int:
    """P011 J_order directly from the complete fiber-size profile."""
    _require_positive("order", order)
    return sum(
        count * comb(size, order)
        for size, count in profile
        if size >= order
    )


def profile_character_product_identity(
    left: FiberProfile, right: FiberProfile, order: int
) -> tuple[int, int]:
    """Return both sides of M_r(f *_x g)=M_r(f)M_r(g)."""
    convolution = multiplicative_profile_convolution(left, right)
    lhs = profile_power_moment(convolution, order)
    rhs = profile_power_moment(left, order) * profile_power_moment(right, order)
    if lhs != rhs:
        raise AssertionError("power moments must be multiplicative characters")
    return lhs, rhs
