"""Multiplicative convolution algebra of Barlow checkpoint fiber profiles.

For a segment of length ell, each represented imbalance has microscopic fiber
size C(ell,j). Record only the size distribution

    B_ell(s) = #{j : C(ell,j)=s}.

Independent checkpoint segments multiply fiber sizes, so complete fiber-size
profiles compose by finite Dirichlet/multiplicative convolution. Power moments
are multiplicative characters of this convolution.

The complete selected-layer profile also determines the checkpoint geometry up
to segment order: its smallest fiber recovers the fully unobserved tail length,
and a triangular peeling algorithm recovers the multiset of observed segment
lengths.
"""

from __future__ import annotations

from math import comb

from .p022_barlow_precision_fibers import selected_segment_lengths

FiberProfile = tuple[tuple[int, int], ...]


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _exact_power_of_two_exponent(value: int) -> int:
    _require_positive("value", value)
    if value & (value - 1):
        raise ValueError("value must be an exact positive power of two")
    return value.bit_length() - 1


def segment_binomial_fiber_profile(segment_length: int) -> FiberProfile:
    _require_positive("segment_length", segment_length)
    counts: dict[int, int] = {}
    for plus_count in range(segment_length + 1):
        size = comb(segment_length, plus_count)
        counts[size] = counts.get(size, 0) + 1
    return tuple(sorted(counts.items()))


def multiplicative_profile_convolution(
    left: FiberProfile, right: FiberProfile
) -> FiberProfile:
    counts: dict[int, int] = {}
    for left_size, left_count in left:
        for right_size, right_count in right:
            size = left_size * right_size
            counts[size] = counts.get(size, 0) + left_count * right_count
    return tuple(sorted(counts.items()))


def profile_from_segments(segments: tuple[int, ...]) -> FiberProfile:
    if not isinstance(segments, tuple) or not segments or any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in segments
    ):
        raise ValueError("segments must be a nonempty tuple of positive integers")
    profile: FiberProfile = ((1, 1),)
    for segment in segments:
        profile = multiplicative_profile_convolution(
            profile, segment_binomial_fiber_profile(segment)
        )
    return profile


def scale_profile_fiber_sizes(profile: FiberProfile, factor: int) -> FiberProfile:
    _require_positive("factor", factor)
    return tuple((size * factor, count) for size, count in profile)


def profile_from_selected_layers(
    length: int, selected_layers: tuple[int, ...]
) -> FiberProfile:
    segments, tail = selected_segment_lengths(length, selected_layers)
    profile = profile_from_segments(segments) if segments else ((1, 1),)
    if tail:
        profile = scale_profile_fiber_sizes(profile, 2 ** tail)
    return profile


def profile_image_size(profile: FiberProfile) -> int:
    return sum(count for _, count in profile)


def profile_domain_size(profile: FiberProfile) -> int:
    return sum(size * count for size, count in profile)


def profile_power_moment(profile: FiberProfile, order: int) -> int:
    _require_positive("order", order)
    return sum(count * (size ** order) for size, count in profile)


def profile_collision_count(profile: FiberProfile, order: int) -> int:
    _require_positive("order", order)
    return sum(
        count * comb(size, order)
        for size, count in profile
        if size >= order
    )


def profile_character_product_identity(
    left: FiberProfile, right: FiberProfile, order: int
) -> tuple[int, int]:
    convolution = multiplicative_profile_convolution(left, right)
    lhs = profile_power_moment(convolution, order)
    rhs = profile_power_moment(left, order) * profile_power_moment(right, order)
    if lhs != rhs:
        raise AssertionError("power moments must be multiplicative characters")
    return lhs, rhs


def segment_minimal_nontrivial_multiplicity(segment_length: int) -> int:
    """Multiplicity of fiber size ``segment_length`` in one segment profile."""
    if segment_length < 2:
        raise ValueError("nontrivial segment length must be at least two")
    return 1 if segment_length == 2 else 2


def recover_segment_multiset_from_profile(profile: FiberProfile) -> tuple[int, ...]:
    """Recover a final-observing segment-length multiset exactly."""
    if not isinstance(profile, tuple) or not profile:
        raise ValueError("profile must be a nonempty finite fiber profile")
    profile_map = dict(profile)
    singleton_count = profile_map.get(1, 0)
    segment_count = _exact_power_of_two_exponent(singleton_count)
    total_length = _exact_power_of_two_exponent(profile_domain_size(profile))

    if segment_count == 0:
        if profile != ((1, 1),) or total_length != 0:
            raise ValueError("zero-segment normalized profile must be ((1,1),)")
        return ()
    if segment_count > total_length:
        raise ValueError("profile is incompatible with positive final-observing segments")

    known_profile: FiberProfile = ((1, 1),)
    known_segment_count = 0
    recovered: dict[int, int] = {}

    for segment_length in range(2, total_length + 1):
        known_map = dict(known_profile)
        known_contribution = known_map.get(segment_length, 0) * (
            2 ** (segment_count - known_segment_count)
        )
        residual = profile_map.get(segment_length, 0) - known_contribution
        beta = segment_minimal_nontrivial_multiplicity(segment_length)
        denominator = beta * (2 ** (segment_count - 1))
        if residual < 0 or residual % denominator:
            raise ValueError("profile violates triangular binomial segment structure")
        count = residual // denominator
        if count:
            recovered[segment_length] = count
            for _ in range(count):
                known_profile = multiplicative_profile_convolution(
                    known_profile,
                    segment_binomial_fiber_profile(segment_length),
                )
            known_segment_count += count
            if known_segment_count > segment_count:
                raise ValueError("profile encodes too many nontrivial segments")

    one_count = segment_count - known_segment_count
    if one_count < 0:
        raise ValueError("profile has negative residual length-one segment count")
    recovered[1] = one_count

    segments = tuple(
        sorted(
            segment_length
            for segment_length, count in recovered.items()
            for _ in range(count)
        )
    )
    if sum(segments) != total_length or len(segments) != segment_count:
        raise ValueError("recovered segment multiset has inconsistent total size")
    if profile_from_segments(segments) != profile:
        raise ValueError("profile is not exactly reproduced by recovered segments")
    return segments


def recover_selected_geometry_from_profile(
    profile: FiberProfile,
) -> tuple[tuple[int, ...], int]:
    """Recover ``(observed_segment_multiset, unobserved_tail_length)``.

    The normalized constrained-segment profile always contains singleton fibers.
    A tail of length u multiplies every fiber size by 2^u, so the smallest
    represented fiber size is exactly 2^u.  Divide out that scale and apply the
    triangular final-observing recovery.
    """
    if not isinstance(profile, tuple) or not profile:
        raise ValueError("profile must be nonempty")
    minimum_size = min(size for size, _ in profile)
    tail = _exact_power_of_two_exponent(minimum_size)
    scale = 2 ** tail
    normalized_items = []
    for size, count in profile:
        if size % scale:
            raise ValueError("profile fiber sizes do not share one tail scale")
        normalized_items.append((size // scale, count))
    normalized = tuple(normalized_items)
    segments = recover_segment_multiset_from_profile(normalized)

    original_length = _exact_power_of_two_exponent(profile_domain_size(profile))
    if sum(segments) + tail != original_length:
        raise ValueError("recovered geometry does not match microscopic domain length")
    return segments, tail
