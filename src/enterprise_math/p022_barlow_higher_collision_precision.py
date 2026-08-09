"""Higher collision structure of selected-layer Barlow precision.

A length-N stacking word is observed only through prefix imbalances at selected
layers. The observation fibers factor over the induced positive segment
lengths, with an arbitrary unobserved tail. Ordered equal-observation tuple
counts therefore factor through generalized binomial power sums, and the P011
collision spectrum follows by the signed Stirling transform.

Balancing checkpoint segments maximizes the number of observable states and
minimizes pair collisions, but it does not componentwise minimize the full
higher-collision spectrum. The pair-vs-four-way conflict persists as an exact
infinite family, and the shortest nontrivial balancing exchange changes its
power-moment direction exactly between orders four and five.
"""

from __future__ import annotations

from functools import lru_cache
from math import comb, factorial

from .p022_barlow_precision_fibers import selected_segment_lengths


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def generalized_binomial_power_sum(length: int, order: int) -> int:
    """Return F_order(length)=sum_j C(length,j)^order."""
    _require_natural("length", length)
    _require_positive("order", order)
    return sum(comb(length, index) ** order for index in range(length + 1))


def ordered_equal_observation_tuple_count(
    length: int, selected_layers: tuple[int, ...], order: int
) -> int:
    """Ordered microscopic ``order``-tuples sharing one observation.

    If selected layers induce segment lengths ell_1,...,ell_m and leave an
    unobserved tail u, then

        M_order = 2^(order*u) product_j F_order(ell_j).

    This counts all ordered tuples, including repeated microscopic words.
    """
    _require_positive("order", order)
    segments, tail = selected_segment_lengths(length, selected_layers)
    result = 2 ** (order * tail)
    for segment in segments:
        result *= generalized_binomial_power_sum(segment, order)
    return result


@lru_cache(maxsize=None)
def signed_stirling_first_kind(order: int, power: int) -> int:
    """Signed Stirling number s(order,power) in falling-factorial convention."""
    _require_natural("order", order)
    _require_natural("power", power)
    if order == 0:
        return 1 if power == 0 else 0
    if power == 0 or power > order:
        return 0
    return signed_stirling_first_kind(order - 1, power - 1) - (
        order - 1
    ) * signed_stirling_first_kind(order - 1, power)


def selected_collision_count(
    length: int, selected_layers: tuple[int, ...], collision_order: int
) -> int:
    """P011 J_k for the selected-layer observation quotient."""
    _require_positive("collision_order", collision_order)
    numerator = sum(
        signed_stirling_first_kind(collision_order, power)
        * ordered_equal_observation_tuple_count(length, selected_layers, power)
        for power in range(1, collision_order + 1)
    )
    denominator = factorial(collision_order)
    if numerator < 0 or numerator % denominator:
        raise AssertionError("Stirling transform must produce an integer collision count")
    return numerator // denominator


def maximum_selected_fiber_size(
    length: int, selected_layers: tuple[int, ...]
) -> int:
    """Largest microscopic fiber under the declared checkpoint language."""
    segments, tail = selected_segment_lengths(length, selected_layers)
    result = 2 ** tail
    for segment in segments:
        result *= comb(segment, segment // 2)
    return result


def selected_collision_spectrum(
    length: int, selected_layers: tuple[int, ...]
) -> tuple[int, ...]:
    """Complete finite P011 collision spectrum J_1,...,J_M."""
    maximum = maximum_selected_fiber_size(length, selected_layers)
    return tuple(
        selected_collision_count(length, selected_layers, order)
        for order in range(1, maximum + 1)
    )


def balanced_segment_lengths(length: int, checkpoint_count: int) -> tuple[int, ...]:
    """Most-even positive segment lengths summing to length."""
    _require_natural("length", length)
    _require_natural("checkpoint_count", checkpoint_count)
    if checkpoint_count == 0:
        if length == 0:
            return ()
        raise ValueError("positive length needs at least one final checkpoint")
    if checkpoint_count > length:
        raise ValueError("checkpoint_count cannot exceed length")
    base, remainder = divmod(length, checkpoint_count)
    return (base,) * (checkpoint_count - remainder) + (base + 1,) * remainder


def checkpoint_layers_from_segments(segments: tuple[int, ...]) -> tuple[int, ...]:
    """Convert positive segment lengths to cumulative checkpoint layers."""
    if not isinstance(segments, tuple) or any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in segments
    ):
        raise ValueError("segments must be a tuple of positive integers")
    running = 0
    layers = []
    for segment in segments:
        running += segment
        layers.append(running)
    return tuple(layers)


def balanced_checkpoint_layers(length: int, checkpoint_count: int) -> tuple[int, ...]:
    """Final-observing near-uniform checkpoint schedule."""
    return checkpoint_layers_from_segments(
        balanced_segment_lengths(length, checkpoint_count)
    )


def central_binomial_exchange_products(longer: int, shorter: int) -> tuple[int, int]:
    """Pair-collision moment before/after one balancing exchange."""
    _require_positive("longer", longer)
    _require_positive("shorter", shorter)
    if longer < shorter + 2:
        raise ValueError("exchange requires a gap of at least two")
    before = comb(2 * longer, longer) * comb(2 * shorter, shorter)
    after = comb(2 * (longer - 1), longer - 1) * comb(
        2 * (shorter + 1), shorter + 1
    )
    if not after < before:
        raise AssertionError("balancing must strictly reduce the pair moment")
    return before, after


def one_three_to_two_two_moment_difference(order: int) -> int:
    """M_order(2,2)-M_order(1,3) for the shortest balancing exchange.

    The exact difference is

        4*(4^(r-1)+2^r-3^r).

    It is zero for r=1, negative for r=2,3,4, and positive for every r>=5.
    """
    _require_positive("order", order)
    direct = generalized_binomial_power_sum(2, order) ** 2 - (
        generalized_binomial_power_sum(1, order)
        * generalized_binomial_power_sum(3, order)
    )
    closed = 4 * (4 ** (order - 1) + 2 ** order - 3 ** order)
    if direct != closed:
        raise AssertionError("closed exchange difference must match power sums")
    return closed


def one_three_exchange_phase(order: int) -> int:
    """Return -1,0,+1 according to the balancing-moment direction."""
    difference = one_three_to_two_two_moment_difference(order)
    return (difference > 0) - (difference < 0)


def near_dense_pair_fourway_tradeoff(checkpoint_count: int) -> dict[str, object]:
    """Exact infinite family at total length N=m+2, m>=2 checkpoints.

    Up to segment order compare

      balanced:   (2,2,1,...,1)
      concentrated:(3,1,...,1).

    Length-one segments have two singleton fibers and therefore only multiply
    fiber *counts*.  The resulting complete nontrivial fiber profiles are

      balanced:    c_1=2^m, c_2=2^m, c_4=2^(m-2)
      concentrated:c_1=2^m, c_3=2^m.

    Hence balanced has larger image and smaller J2, both have the same J3,
    while concentrated kills J4 completely.
    """
    _require_positive("checkpoint_count", checkpoint_count)
    if checkpoint_count < 2:
        raise ValueError("tradeoff family requires at least two checkpoints")
    m = checkpoint_count
    length = m + 2
    balanced_segments = (1,) * (m - 2) + (2, 2)
    concentrated_segments = (1,) * (m - 1) + (3,)
    balanced_layers = checkpoint_layers_from_segments(balanced_segments)
    concentrated_layers = checkpoint_layers_from_segments(concentrated_segments)
    return {
        "length": length,
        "balanced_segments": balanced_segments,
        "concentrated_segments": concentrated_segments,
        "balanced_layers": balanced_layers,
        "concentrated_layers": concentrated_layers,
        "balanced_image": 9 * (2 ** (m - 2)),
        "concentrated_image": 8 * (2 ** (m - 2)),
        "balanced_J1_J4": (
            2 ** length,
            5 * (2 ** (m - 1)),
            2 ** m,
            2 ** (m - 2),
        ),
        "concentrated_J1_J4": (
            2 ** length,
            3 * (2 ** m),
            2 ** m,
            0,
        ),
    }


def minimal_spectrum_tradeoff() -> dict[str, object]:
    """The m=2 member of :func:`near_dense_pair_fourway_tradeoff`."""
    return near_dense_pair_fourway_tradeoff(2)
