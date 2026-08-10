"""Traditional coarse probability/rate quantities as optional shadows of fine counts.

For block capacities m_i and nonnegative coarse totals c_i, the number of labeled
fine occupancy states is M(c)=product_i H_(m_i)(c_i).  At fixed grand total C,
these multiplicities sum exactly to H_M(C) with M=sum_i m_i; this is the LEGO
fiber decomposition under grouping fine slots.

Only after adding a semantic assumption that fine occupancy states are sampled
equally may the pair (M(c),H_M(C)) be rendered as a traditional macro
probability.  Likewise the integer coarse-transfer witness incidence divided by
source fiber count gives an averaged outgoing rate under conditional-uniform
mixing; without such mixing, coarse totals are generally not a future-safe Markov
state and occupancy histograms are required.
"""

from __future__ import annotations

from itertools import product
from math import gcd

from .causal_coarse_transfer_incidence import (
    coarse_state_fine_lift_count,
    coarse_transfer_witness_count,
    fiber_count,
    transferred_coarse_state,
)

Capacities = tuple[int, ...]
Totals = tuple[int, ...]


def coarse_totals_with_grand_total(block_count: int, grand_total: int) -> tuple[Totals, ...]:
    if isinstance(block_count, bool) or not isinstance(block_count, int) or block_count < 1:
        raise ValueError("block_count must be positive")
    if isinstance(grand_total, bool) or not isinstance(grand_total, int) or grand_total < 0:
        raise ValueError("grand_total must be non-negative")
    states = []

    def build(prefix, remaining_blocks, remaining_total):
        if remaining_blocks == 1:
            states.append(tuple(prefix + [remaining_total]))
            return
        for value in range(remaining_total + 1):
            build(prefix + [value], remaining_blocks - 1, remaining_total - value)

    build([], block_count, grand_total)
    return tuple(states)


def total_fine_occupancy_count(capacities: Capacities, grand_total: int) -> int:
    return fiber_count(sum(capacities), grand_total)


def macro_multiplicity(capacities: Capacities, totals: Totals) -> int:
    return coarse_state_fine_lift_count(capacities, totals)


def grouped_fiber_decomposition_identity(capacities: Capacities, grand_total: int) -> bool:
    states = coarse_totals_with_grand_total(len(capacities), grand_total)
    grouped = sum(macro_multiplicity(capacities, totals) for totals in states)
    return grouped == total_fine_occupancy_count(capacities, grand_total)


def uniform_fine_state_probability_pair(capacities: Capacities, totals: Totals) -> tuple[int, int]:
    """Exact numerator/denominator only; no probability ontology is assumed."""
    grand_total = sum(totals)
    return (
        macro_multiplicity(capacities, totals),
        total_fine_occupancy_count(capacities, grand_total),
    )


def reduced_uniform_probability_pair(capacities: Capacities, totals: Totals) -> tuple[int, int]:
    numerator, denominator = uniform_fine_state_probability_pair(capacities, totals)
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor


def averaged_transfer_rate_pair(
    capacities: Capacities,
    totals: Totals,
    receiver_block: int,
    donor_block: int,
) -> tuple[int, int]:
    """Witness incidence / source-fiber count, as an exact rational pair."""
    numerator = coarse_transfer_witness_count(
        capacities, totals, receiver_block, donor_block
    )
    denominator = macro_multiplicity(capacities, totals)
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor


def averaged_transfer_rate_closed_pair(
    capacities: Capacities,
    totals: Totals,
    receiver_block: int,
    donor_block: int,
) -> tuple[int, int]:
    m_receiver = capacities[receiver_block]
    m_donor = capacities[donor_block]
    c_donor = totals[donor_block]
    if c_donor <= 0:
        return 0, 1
    numerator = m_receiver * m_donor * c_donor
    denominator = c_donor + m_donor - 1
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor


def averaged_rate_closed_form_identity(
    capacities: Capacities,
    totals: Totals,
    receiver_block: int,
    donor_block: int,
) -> bool:
    return averaged_transfer_rate_pair(
        capacities, totals, receiver_block, donor_block
    ) == averaged_transfer_rate_closed_pair(
        capacities, totals, receiver_block, donor_block
    )


def averaged_rate_detailed_balance_identity(
    capacities: Capacities,
    totals: Totals,
    receiver_block: int,
    donor_block: int,
) -> bool:
    if totals[donor_block] <= 0:
        return True
    target = transferred_coarse_state(totals, receiver_block, donor_block)
    forward_rate = averaged_transfer_rate_pair(
        capacities, totals, receiver_block, donor_block
    )
    reverse_rate = averaged_transfer_rate_pair(
        capacities, target, donor_block, receiver_block
    )
    source_weight = macro_multiplicity(capacities, totals)
    target_weight = macro_multiplicity(capacities, target)
    return (
        source_weight * forward_rate[0] * reverse_rate[1]
        == target_weight * reverse_rate[0] * forward_rate[1]
    )
