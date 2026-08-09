"""Task-relative state compression for higher-channel quotient-path lift counts.

The exact local-radix sequence of a hyperoctahedral quotient path can contain
more information than its total fiber cardinality.  But for the future language
that asks only total lift counts of later coarse extensions, the pair

    (current chamber state, current total lift count)

is an exact Markov state: extending by p->r multiplies the count by the local
transition multiplicity m(p,r).

Rank three already supplies two same-horizon, same-endpoint paths with equal
total lift count 192 but different local-radix histories.  Thus the compressed
state is sufficient for future total counts but not for mechanism-history
queries.
"""

from __future__ import annotations

from .p022_barlow_higher_channel_repair import (
    ChamberPath,
    ChamberState,
    path_lift_count,
    path_lift_factors,
    transition_multiplicity,
)

LiftCountState = tuple[ChamberState, int]


def lift_count_state(path: ChamberPath) -> LiftCountState:
    """Current coarse chamber plus exact microscopic lift cardinality."""
    if not path:
        raise ValueError("path must contain at least one chamber state")
    return path[-1], path_lift_count(path)


def extend_lift_count_state(state: LiftCountState, next_state: ChamberState) -> LiftCountState:
    """Exact one-step update ``F' = F*m(p,r)``."""
    current, count = state
    if isinstance(count, bool) or not isinstance(count, int) or count <= 0:
        raise ValueError("lift count must be a positive integer")
    multiplicity = transition_multiplicity(current, next_state)
    if multiplicity <= 0:
        raise ValueError("next_state is not a legal coarse successor")
    return next_state, count * multiplicity


def extend_lift_count_along_path(
    state: LiftCountState, continuation: tuple[ChamberState, ...]
) -> LiftCountState:
    """Apply a common coarse continuation using only the compressed state."""
    output = state
    for next_state in continuation:
        output = extend_lift_count_state(output, next_state)
    return output


def rank_three_same_state_count_mechanism_alias() -> tuple[
    ChamberPath, ChamberPath, tuple[int, ...], tuple[int, ...], LiftCountState
]:
    """Two paths with same endpoint/count but different radix histories."""
    first: ChamberPath = (
        (1, 1, 1),
        (0, 0, 0),
        (1, 1, 1),
        (0, 2, 2),
    )
    second: ChamberPath = (
        (1, 1, 1),
        (0, 0, 2),
        (1, 1, 3),
        (0, 2, 2),
    )
    first_factors = path_lift_factors(first)
    second_factors = path_lift_factors(second)
    first_state = lift_count_state(first)
    second_state = lift_count_state(second)
    if first_factors != (8, 1, 8, 3):
        raise AssertionError("first alias radix sequence changed")
    if second_factors != (8, 3, 4, 2):
        raise AssertionError("second alias radix sequence changed")
    if first_state != second_state or first_state != ((0, 2, 2), 192):
        raise AssertionError("alias paths must share endpoint and total lift count")
    return first, second, first_factors, second_factors, first_state


def common_extension_preserves_count_alias(
    first: ChamberPath,
    second: ChamberPath,
    continuation: tuple[ChamberState, ...],
) -> tuple[LiftCountState, LiftCountState]:
    """If two paths share compressed state, every common legal extension does too."""
    first_state = lift_count_state(first)
    second_state = lift_count_state(second)
    if first_state != second_state:
        raise ValueError("paths do not begin the continuation in the same compressed state")
    first_final = extend_lift_count_along_path(first_state, continuation)
    second_final = extend_lift_count_along_path(second_state, continuation)
    if first_final != second_final:
        raise AssertionError("compressed lift-count state must be future-stable")
    return first_final, second_final
