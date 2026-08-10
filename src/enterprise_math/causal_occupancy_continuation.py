"""Anonymous occupancy histograms as future-relevant state beyond coarse totals.

A coarse block of capacity m contains m fine slots and total c indistinguishable
units.  The total alone does not determine primitive transfer continuation:
(3,0,0) and (1,1,1) both have total 3 but one versus three nonempty donor slots.

If fine slots inside a block are anonymous, labeled occupancy vectors may first
collapse by slot permutations.  The orbit state is the occupancy histogram
n_q=#slots carrying q units, with sum n_q=m and sum q*n_q=c.  Cross-block one-unit
transfers act locally on these histograms and their fine endpoint multiplicity is
exactly (#receiver slots of occupancy p)*(#donor slots of occupancy q).

This is an exact finite causal continuation state for permutation-invariant
primitive transfer relations.  Whether it is globally minimal for a larger future
language remains a future-context quotient question.
"""

from __future__ import annotations

from collections import Counter
from math import factorial

Occupancy = tuple[int, ...]
Histogram = tuple[tuple[int, int], ...]  # sorted (occupancy, slot_count)


def occupancy_histogram(occupancy: Occupancy) -> Histogram:
    if not occupancy or any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in occupancy):
        raise ValueError("occupancy must be a nonempty tuple of non-negative integers")
    return tuple(sorted(Counter(occupancy).items()))


def histogram_capacity(histogram: Histogram) -> int:
    return sum(count for _, count in histogram)


def histogram_total(histogram: Histogram) -> int:
    return sum(level * count for level, count in histogram)


def histogram_count_at(histogram: Histogram, level: int) -> int:
    return dict(histogram).get(level, 0)


def histogram_labeled_multiplicity(histogram: Histogram) -> int:
    """Number of labeled fine occupancy vectors in one anonymous histogram orbit."""
    capacity = histogram_capacity(histogram)
    denominator = 1
    for _, count in histogram:
        denominator *= factorial(count)
    return factorial(capacity) // denominator


def histogram_from_counts(counts: dict[int, int]) -> Histogram:
    return tuple(sorted((level, count) for level, count in counts.items() if count > 0))


def transfer_histogram_update(
    receiver: Histogram,
    donor: Histogram,
    receiver_level: int,
    donor_level: int,
) -> tuple[Histogram, Histogram, int]:
    """One cross-block unit transfer conditioned on endpoint occupancy levels.

    Returns `(new_receiver,new_donor,fine_endpoint_multiplicity)`.
    """
    if donor_level <= 0:
        raise ValueError("donor occupancy level must be positive")
    receiver_count = histogram_count_at(receiver, receiver_level)
    donor_count = histogram_count_at(donor, donor_level)
    if receiver_count <= 0 or donor_count <= 0:
        raise ValueError("declared endpoint occupancy level is absent")

    receiver_counts = dict(receiver)
    receiver_counts[receiver_level] -= 1
    receiver_counts[receiver_level + 1] = receiver_counts.get(receiver_level + 1, 0) + 1

    donor_counts = dict(donor)
    donor_counts[donor_level] -= 1
    donor_counts[donor_level - 1] = donor_counts.get(donor_level - 1, 0) + 1

    multiplicity = receiver_count * donor_count
    return (
        histogram_from_counts(receiver_counts),
        histogram_from_counts(donor_counts),
        multiplicity,
    )


def coarse_transfer_histogram_profile(
    receiver: Histogram,
    donor: Histogram,
) -> dict[tuple[Histogram, Histogram], int]:
    """Aggregate all fine endpoint choices into next anonymous histogram states."""
    profile: dict[tuple[Histogram, Histogram], int] = {}
    for receiver_level, receiver_count in receiver:
        for donor_level, donor_count in donor:
            if donor_level <= 0:
                continue
            new_receiver, new_donor, multiplicity = transfer_histogram_update(
                receiver, donor, receiver_level, donor_level
            )
            key = (new_receiver, new_donor)
            profile[key] = profile.get(key, 0) + multiplicity
    return profile


def total_outgoing_endpoint_multiplicity(receiver: Histogram, donor: Histogram) -> int:
    """Fine endpoint count for one coarse donor->receiver block pair."""
    receiver_slots = histogram_capacity(receiver)
    nonempty_donor_slots = sum(count for level, count in donor if level > 0)
    return receiver_slots * nonempty_donor_slots


def total_only_is_one_step_sufficient(
    left_histogram: Histogram,
    right_histogram: Histogram,
) -> bool:
    """Same total/capacity implies same coarse outgoing endpoint count iff support counts match."""
    if histogram_capacity(left_histogram) != histogram_capacity(right_histogram):
        return False
    if histogram_total(left_histogram) != histogram_total(right_histogram):
        return False
    left_nonempty = sum(count for level, count in left_histogram if level > 0)
    right_nonempty = sum(count for level, count in right_histogram if level > 0)
    return left_nonempty == right_nonempty
