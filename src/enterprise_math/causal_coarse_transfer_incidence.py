"""Exact fine-witness incidence behind coarse conservative transfer dynamics.

A coarse block alpha contains m_alpha indistinguishable fine slots and carries a
nonnegative total c_alpha.  Fine occupancy lifts are weak compositions counted by
H_m(c)=C(c+m-1,m-1).

For a coarse one-unit transfer beta->alpha, a fine witness chooses:
- one fine source occupancy;
- one nonempty donor slot inside beta;
- one receiver slot inside alpha.

Summing over all fine lifts gives the exact integer incidence

    W_(alpha<-beta)(c)
      = m_alpha H_malpha(c_alpha)
        * m_beta H_mbeta(c_beta-1)
        * product_other H_mgamma(c_gamma).

Reversing each fine edge is a bijection between forward witnesses from c and
reverse witnesses from c'=c+e_alpha-e_beta, hence W(c->c')=W(c'->c) as raw
integer incidence.  A traditional detailed-balance probability/rate statement
appears only after an additional sampling/normalization semantics.
"""

from __future__ import annotations

from math import comb

Capacities = tuple[int, ...]
Totals = tuple[int, ...]


def fiber_count(capacity: int, total: int) -> int:
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity <= 0:
        raise ValueError("capacity must be a positive integer")
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        raise ValueError("total must be a non-negative integer")
    return comb(total + capacity - 1, capacity - 1)


def coarse_state_fine_lift_count(capacities: Capacities, totals: Totals) -> int:
    if not capacities or len(capacities) != len(totals):
        raise ValueError("capacities and totals must be equal-length nonempty tuples")
    result = 1
    for capacity, total in zip(capacities, totals):
        result *= fiber_count(capacity, total)
    return result


def total_positive_slot_incidence(capacity: int, total: int) -> int:
    """Sum over all weak compositions of `total` of the number of positive slots."""
    if total == 0:
        return 0
    return capacity * fiber_count(capacity, total - 1)


def coarse_transfer_witness_count(
    capacities: Capacities,
    totals: Totals,
    receiver_block: int,
    donor_block: int,
) -> int:
    if not capacities or len(capacities) != len(totals):
        raise ValueError("capacities and totals must be equal-length nonempty tuples")
    if receiver_block == donor_block:
        raise ValueError("coarse transfer requires distinct receiver and donor blocks")
    if any(index < 0 or index >= len(capacities) for index in (receiver_block, donor_block)):
        raise ValueError("block index outside state")
    if totals[donor_block] <= 0:
        return 0
    result = 1
    for index, (capacity, total) in enumerate(zip(capacities, totals)):
        if index == receiver_block:
            result *= capacity * fiber_count(capacity, total)
        elif index == donor_block:
            result *= total_positive_slot_incidence(capacity, total)
        else:
            result *= fiber_count(capacity, total)
    return result


def transferred_coarse_state(
    totals: Totals,
    receiver_block: int,
    donor_block: int,
) -> Totals:
    if receiver_block == donor_block:
        raise ValueError("coarse transfer requires distinct blocks")
    if totals[donor_block] <= 0:
        raise ValueError("donor block must contain at least one unit")
    result = list(totals)
    result[receiver_block] += 1
    result[donor_block] -= 1
    return tuple(result)


def reverse_witness_balance_identity(
    capacities: Capacities,
    totals: Totals,
    receiver_block: int,
    donor_block: int,
) -> bool:
    if totals[donor_block] <= 0:
        return True
    target = transferred_coarse_state(totals, receiver_block, donor_block)
    forward = coarse_transfer_witness_count(
        capacities, totals, receiver_block, donor_block
    )
    reverse = coarse_transfer_witness_count(
        capacities, target, donor_block, receiver_block
    )
    return forward == reverse


def mean_fine_move_multiplicity_per_source_lift(
    capacities: Capacities,
    totals: Totals,
    receiver_block: int,
    donor_block: int,
) -> tuple[int, int]:
    """Exact rational pair `(witness_count, source_fiber_count)`; no division performed."""
    return (
        coarse_transfer_witness_count(capacities, totals, receiver_block, donor_block),
        coarse_state_fine_lift_count(capacities, totals),
    )


def simplified_source_ratio_factors(
    capacities: Capacities,
    totals: Totals,
    receiver_block: int,
    donor_block: int,
) -> tuple[int, int]:
    """Reduced exact ratio for average outgoing witnesses per fine source state.

    W/M = m_receiver * m_donor * c_donor / (c_donor+m_donor-1).
    The returned pair is numerator/denominator before gcd reduction; it remains an
    exact integer ratio and is not interpreted as probability without extra
    sampling semantics.
    """
    m_receiver = capacities[receiver_block]
    m_donor = capacities[donor_block]
    c_donor = totals[donor_block]
    if c_donor <= 0:
        return 0, 1
    return (
        m_receiver * m_donor * c_donor,
        c_donor + m_donor - 1,
    )
