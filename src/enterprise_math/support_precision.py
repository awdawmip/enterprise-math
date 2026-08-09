"""E001.3 finite-support collision certificates over P018 observation fibers.

P018 already supplies finite observation partitions and refinement.  E001.3
lifts that machinery from one point state to a finite support relation.

For a body support S and one observation block F, retain only three facts:

* EMPTY: F ∩ S is empty;
* FULL: F is contained in S;
* PARTIAL: F meets S but is not contained in S.

Equivalently, one observation produces two finite block sets:

* MAY(S): blocks that intersect S;
* MUST(S): blocks wholly contained in S.

Then ``MUST(S) <= MAY(S)``.  For two supports A,B:

* disjoint MAY sets certify separation;
* ``MUST(A)∩MAY(B)`` or ``MAY(A)∩MUST(B)`` certifies a real shared terminal state;
* the remaining MAY/MAY overlap is unresolved and refines.

An identity terminal observation decides exact finite support intersection.  This
shows that the multi-scale certificate logic needs no new precision primitive
beyond P018; the additional geometric datum is the body's finite
support/admissible-target relation itself.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable
from dataclasses import dataclass

from .precision_system import FALSE, TRUE, UNRESOLVED, observation_partition, refinement_projection

EMPTY = "EMPTY"
FULL = "FULL"
PARTIAL = "PARTIAL"
SupportStatus = str
Certificate = str


@dataclass(frozen=True)
class SupportAbstraction:
    """Finite may/must image of one support under one P018 observation."""

    may_blocks: frozenset[Hashable]
    must_blocks: frozenset[Hashable]


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


def support_abstraction(
    states: list[Hashable],
    observation: Callable[[Hashable], Hashable],
    support: frozenset[Hashable],
) -> SupportAbstraction:
    """Return the exact finite MAY/MUST block image of one terminal support."""
    statuses = support_block_statuses(states, observation, support)
    may = frozenset(key for key, status in statuses.items() if status != EMPTY)
    must = frozenset(key for key, status in statuses.items() if status == FULL)
    if not must.issubset(may):
        raise AssertionError("MUST support blocks escaped MAY support blocks")
    return SupportAbstraction(may_blocks=may, must_blocks=must)


def support_overlap_certificate(
    states: list[Hashable],
    observation: Callable[[Hashable], Hashable],
    left_support: frozenset[Hashable],
    right_support: frozenset[Hashable],
) -> Certificate:
    """Three-valued collision certificate from MAY/MUST support images."""
    left = support_abstraction(states, observation, left_support)
    right = support_abstraction(states, observation, right_support)

    may_overlap = left.may_blocks.intersection(right.may_blocks)
    if not may_overlap:
        return FALSE
    if left.must_blocks.intersection(right.may_blocks):
        return TRUE
    if left.may_blocks.intersection(right.must_blocks):
        return TRUE
    return UNRESOLVED


def support_refinement_consistency(
    states: list[Hashable],
    coarse_observation: Callable[[Hashable], Hashable],
    fine_observation: Callable[[Hashable], Hashable],
    support: frozenset[Hashable],
) -> dict[str, object]:
    """Check exact MAY coverage and monotone MUST evidence under refinement.

    The P018 projection sends every fine observation key to its unique coarse key.
    Projecting the fine MAY set recovers the coarse MAY set exactly.  Every coarse
    MUST block is also the projection of at least one fine MUST block; fine
    refinement may additionally make previously PARTIAL coarse regions locally
    FULL, so projected fine MUST can be larger.
    """
    projection = refinement_projection(states, coarse_observation, fine_observation)
    coarse = support_abstraction(states, coarse_observation, support)
    fine = support_abstraction(states, fine_observation, support)
    projected_fine_may = frozenset(projection[key] for key in fine.may_blocks)
    projected_fine_must = frozenset(projection[key] for key in fine.must_blocks)
    if projected_fine_may != coarse.may_blocks:
        raise AssertionError("fine MAY blocks did not project exactly to coarse MAY")
    if not coarse.must_blocks.issubset(projected_fine_must):
        raise AssertionError("coarse MUST evidence was lost under refinement")
    return {
        "coarse": coarse,
        "fine": fine,
        "projected_fine_may": projected_fine_may,
        "projected_fine_must": projected_fine_must,
    }


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
