"""E001.3 finite-support collision certificates over P018 observation fibers.

P018 already supplies finite observation partitions and refinement.  E001.3
lifts that machinery from one point state to a finite support relation.

For a body support S and one observation block F, retain only three facts:

* EMPTY: F ∩ S is empty;
* FULL: F is contained in S;
* PARTIAL: F meets S but is not contained in S.

For two supports, a block with FULL/nonempty certifies a real shared terminal
state.  If no block is nonempty for both, separation is certified.  Shared
PARTIAL/PARTIAL blocks remain unresolved until a finer observation.  An identity
terminal observation therefore decides exact finite support intersection.

This shows that the multi-scale certificate logic needs no new precision
primitive beyond P018; the additional geometric datum is the body's finite
support/admissible-target relation itself.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable

from .precision_system import FALSE, TRUE, UNRESOLVED, observation_partition, refinement_projection

EMPTY = "EMPTY"
FULL = "FULL"
PARTIAL = "PARTIAL"
SupportStatus = str
Certificate = str


def _validate_support(states: list[Hashable], support: frozenset[Hashable]) -> None:
    if not support.issubset(states):
        raise ValueError("support must be a subset of terminal states")


def support_block_statuses(
    states: list[Hashable],
    observation: Callable[[Hashable], Hashable],
    support: frozenset[Hashable],
) -> dict[Hashable, SupportStatus]:
    """Classify every finite observation fiber as EMPTY, FULL, or PARTIAL."""
    _validate_support(states, support)
    partition = observation_partition(states, observation)
    result: dict[Hashable, SupportStatus] = {}
    for key, block in partition.items():
        block_set = frozenset(block)
        overlap = block_set.intersection(support)
        if not overlap:
            result[key] = EMPTY
        elif overlap == block_set:
            result[key] = FULL
        else:
            result[key] = PARTIAL
    return result


def support_overlap_certificate(
    states: list[Hashable],
    observation: Callable[[Hashable], Hashable],
    left_support: frozenset[Hashable],
    right_support: frozenset[Hashable],
) -> Certificate:
    """Three-valued collision certificate using only one observation partition."""
    left = support_block_statuses(states, observation, left_support)
    right = support_block_statuses(states, observation, right_support)
    unresolved = False
    for key in left:
        left_status = left[key]
        right_status = right[key]
        if left_status == EMPTY or right_status == EMPTY:
            continue
        if left_status == FULL or right_status == FULL:
            return TRUE
        unresolved = True
    return UNRESOLVED if unresolved else FALSE


def support_overlap_certificate_profile(
    states: list[Hashable],
    observations: list[Callable[[Hashable], Hashable]],
    left_support: frozenset[Hashable],
    right_support: frozenset[Hashable],
) -> list[Certificate]:
    """Return persistent support-overlap certificates along a refinement chain."""
    if not observations:
        raise ValueError("at least one observation is required")
    _validate_support(states, left_support)
    _validate_support(states, right_support)

    statuses: list[Certificate] = []
    decided: Certificate | None = None
    previous = observations[0]
    for observation in observations:
        refinement_projection(states, previous, observation)
        status = support_overlap_certificate(
            states, observation, left_support, right_support
        )
        if decided is not None and status != decided:
            raise AssertionError("a support-overlap certificate was overturned by refinement")
        if status != UNRESOLVED:
            decided = status
        statuses.append(status)
        previous = observation
    return statuses
