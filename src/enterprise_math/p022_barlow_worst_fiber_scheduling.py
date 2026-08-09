"""Exact minimax checkpoint scheduling for selected-layer Barlow precision.

For a final-observing checkpoint schedule with positive segment lengths
ell_1,...,ell_m, the largest observation fiber is

    product_j C(ell_j, floor(ell_j/2)).

Unlike image size and pair-collision J2, the minimizer is not ordinary equal
spacing at small parity scales.  The exact rule is to distribute *pairs* of
extra units as evenly as possible, leaving at most one unpaired unit.  This
produces an odd-balanced (pair-balanced) segment family.
"""

from __future__ import annotations

from math import comb

from .p022_barlow_higher_collision_precision import checkpoint_layers_from_segments
from .p022_barlow_precision_fibers import selected_segment_lengths


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def central_fiber_factor(segment_length: int) -> int:
    """Largest binomial fiber contributed by one observed segment."""
    _require_positive("segment_length", segment_length)
    return comb(segment_length, segment_length // 2)


def maximum_fiber_from_segments(segments: tuple[int, ...]) -> int:
    """Largest microscopic fiber for a final-observing segment decomposition."""
    if not isinstance(segments, tuple) or not segments:
        raise ValueError("segments must be a nonempty tuple")
    result = 1
    for segment in segments:
        result *= central_fiber_factor(segment)
    return result


def maximum_fiber_from_checkpoint_layers(
    length: int, selected_layers: tuple[int, ...]
) -> int:
    """Largest fiber of a schedule, requiring the final layer to be selected."""
    _require_positive("length", length)
    segments, tail = selected_segment_lengths(length, selected_layers)
    if tail != 0 or not segments:
        raise ValueError("minimax theorem requires the final layer to be observed")
    return maximum_fiber_from_segments(segments)


def odd_pair_increment_factor(pair_index: int) -> tuple[int, int]:
    """Reduced exact factor for odd length ``2j-1 -> 2j+1``.

    The ratio of central fibers is

        C(2j+1,j) / C(2j-1,j-1)
        = 2(2j+1)/(j+1)
        = 4 - 2/(j+1).

    Return the unreduced integer numerator/denominator pair.  The value is
    strictly increasing with j and always less than four.
    """
    _require_positive("pair_index", pair_index)
    j = pair_index
    return 2 * (2 * j + 1), j + 1


def odd_to_even_increment_factor() -> int:
    """Every odd-to-next-even central-fiber increment costs exactly factor 2."""
    return 2


def minimax_pair_allocation(length: int, checkpoint_count: int) -> tuple[int, int, int]:
    """Return ``(base_pairs, high_pair_segments, leftover_single)``.

    Start all m segments at length one.  Let E=N-m be extra units.  In a
    minimizer at most one extra unit remains unpaired, because replacing two
    single odd->even increments (cost 4) by one additional odd->odd pair costs
    ``4-2/(j+1)<4``.

    The remaining P=floor(E/2) pairs are distributed as evenly as possible,
    because their marginal factors ``4-2/(j+1)`` strictly increase with the
    number of pairs already assigned to one segment.
    """
    _require_positive("length", length)
    _require_positive("checkpoint_count", checkpoint_count)
    if checkpoint_count > length:
        raise ValueError("checkpoint_count cannot exceed length")
    extra = length - checkpoint_count
    pairs, leftover = divmod(extra, 2)
    base_pairs, high_pair_segments = divmod(pairs, checkpoint_count)
    return base_pairs, high_pair_segments, leftover


def minimax_segment_multisets(
    length: int, checkpoint_count: int
) -> tuple[tuple[int, ...], ...]:
    """All distinct sorted segment multisets minimizing the maximum fiber.

    Without a leftover single, the minimizer is unique up to segment order.
    With one leftover unit, multiplying any odd segment by the same factor two
    is cost-neutral.  If both low-pair and high-pair segment classes exist,
    adding the unit to either class produces two distinct minimizing multisets.
    """
    base_pairs, high_count, leftover = minimax_pair_allocation(
        length, checkpoint_count
    )
    low_count = checkpoint_count - high_count
    low_length = 1 + 2 * base_pairs
    high_length = low_length + 2
    base = [low_length] * low_count + [high_length] * high_count
    if leftover == 0:
        return (tuple(sorted(base)),)

    candidates = set()
    for index in range(len(base)):
        changed = list(base)
        changed[index] += 1
        candidates.add(tuple(sorted(changed)))
    return tuple(sorted(candidates))


def minimum_possible_maximum_fiber(length: int, checkpoint_count: int) -> int:
    """Closed minimax value for the worst observation fiber.

    Let E=N-m, P=floor(E/2)=qm+r and e=E mod 2. Then

      M_min = 2^e
              C(2q+1,q)^(m-r)
              C(2q+3,q+1)^r.
    """
    q, r, leftover = minimax_pair_allocation(length, checkpoint_count)
    low = comb(2 * q + 1, q)
    high = comb(2 * q + 3, q + 1)
    return (2 ** leftover) * (low ** (checkpoint_count - r)) * (high ** r)


def minimax_checkpoint_layer_families(
    length: int, checkpoint_count: int
) -> tuple[tuple[int, ...], ...]:
    """Canonical layer schedules for the distinct minimax segment multisets."""
    return tuple(
        checkpoint_layers_from_segments(segments)
        for segments in minimax_segment_multisets(length, checkpoint_count)
    )


def collision_free_above_maximum_fiber(maximum_fiber: int) -> int:
    """First P011 collision order guaranteed to vanish and all higher orders too."""
    _require_positive("maximum_fiber", maximum_fiber)
    return maximum_fiber + 1
