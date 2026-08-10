"""Anonymous occupancy state as a complete slot-collision spectrum.

For fine slot occupancies x_i>=0 define

    K_t = sum_i C(x_i,t).

Equivalently, if n_q is the occupancy histogram, K_t=sum_q n_q C(q,t).  The full
finite sequence is invertible:

    n_q = sum_{t>=q} (-1)^(t-q) C(t,q) K_t.

Thus K_0=capacity and K_1=coarse total; higher K_t are exactly the hidden clustering
relations required to recover the anonymous occupancy continuation state.

A one-unit transfer from donor occupancy q to receiver occupancy p changes each
collision coordinate by the Pascal rule

    Delta K_t = C(p,t-1) - C(q-1,t-1).

In particular K_1 is conserved while higher collision coordinates move.  This is
an exact integer dynamics on P011-style collision coordinates, not a statistical
moment approximation.
"""

from __future__ import annotations

from math import comb

from .causal_occupancy_continuation import Histogram, histogram_capacity, histogram_total, occupancy_histogram

Occupancy = tuple[int, ...]
Spectrum = tuple[int, ...]


def occupancy_collision_coordinate(occupancy: Occupancy, order: int) -> int:
    if not occupancy or any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in occupancy):
        raise ValueError("occupancy must be a nonempty tuple of nonnegative integers")
    if isinstance(order, bool) or not isinstance(order, int) or order < 0:
        raise ValueError("order must be non-negative")
    if order == 0:
        return len(occupancy)
    return sum(comb(value, order) for value in occupancy if value >= order)


def occupancy_collision_spectrum(occupancy: Occupancy, maximum_order: int | None = None) -> Spectrum:
    total = sum(occupancy)
    limit = total if maximum_order is None else maximum_order
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("maximum_order must be non-negative")
    return tuple(occupancy_collision_coordinate(occupancy, order) for order in range(limit + 1))


def histogram_collision_spectrum(histogram: Histogram, maximum_order: int | None = None) -> Spectrum:
    total = histogram_total(histogram)
    limit = total if maximum_order is None else maximum_order
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("maximum_order must be non-negative")
    coordinates = []
    for order in range(limit + 1):
        if order == 0:
            coordinates.append(histogram_capacity(histogram))
        else:
            coordinates.append(
                sum(count * comb(level, order) for level, count in histogram if level >= order)
            )
    return tuple(coordinates)


def histogram_from_collision_spectrum(spectrum: Spectrum) -> Histogram:
    if not spectrum:
        raise ValueError("spectrum must contain at least K_0")
    maximum = len(spectrum) - 1
    counts = {}
    for level in range(maximum, -1, -1):
        value = sum(
            ((-1) ** (order - level)) * comb(order, level) * spectrum[order]
            for order in range(level, maximum + 1)
        )
        if value < 0:
            raise ValueError("spectrum is not a valid finite occupancy collision transform")
        if value:
            counts[level] = value
    histogram = tuple(sorted(counts.items()))
    if histogram_capacity(histogram) != spectrum[0]:
        raise ValueError("K_0 does not match reconstructed capacity")
    return histogram


def collision_spectrum_recovers_histogram(occupancy: Occupancy) -> bool:
    spectrum = occupancy_collision_spectrum(occupancy)
    return histogram_from_collision_spectrum(spectrum) == occupancy_histogram(occupancy)


def nonempty_slot_count_from_spectrum(spectrum: Spectrum) -> int:
    """Support count = K1-K2+K3-... by binomial inversion at occupancy level zero."""
    if not spectrum:
        raise ValueError("spectrum must be nonempty")
    empty_count = sum(((-1) ** order) * spectrum[order] for order in range(len(spectrum)))
    return spectrum[0] - empty_count


def transfer_collision_delta(receiver_level: int, donor_level: int, order: int) -> int:
    if receiver_level < 0 or donor_level <= 0:
        raise ValueError("receiver level must be nonnegative and donor level positive")
    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError("order must be positive")
    receive = comb(receiver_level, order - 1) if receiver_level >= order - 1 else 0
    donate = comb(donor_level - 1, order - 1) if donor_level - 1 >= order - 1 else 0
    return receive - donate


def apply_unit_transfer_to_occupancy(
    occupancy: Occupancy,
    receiver_slot: int,
    donor_slot: int,
) -> Occupancy:
    if receiver_slot == donor_slot or any(index < 0 or index >= len(occupancy) for index in (receiver_slot, donor_slot)):
        raise ValueError("transfer endpoints must be distinct valid slots")
    if occupancy[donor_slot] <= 0:
        raise ValueError("donor slot must be nonempty")
    result = list(occupancy)
    result[receiver_slot] += 1
    result[donor_slot] -= 1
    return tuple(result)


def transfer_collision_spectrum_identity(
    occupancy: Occupancy,
    receiver_slot: int,
    donor_slot: int,
) -> bool:
    before = occupancy_collision_spectrum(occupancy)
    after_occupancy = apply_unit_transfer_to_occupancy(occupancy, receiver_slot, donor_slot)
    after = occupancy_collision_spectrum(after_occupancy)
    p = occupancy[receiver_slot]
    q = occupancy[donor_slot]
    return all(
        after[order] - before[order] == transfer_collision_delta(p, q, order)
        for order in range(1, len(before))
    )
