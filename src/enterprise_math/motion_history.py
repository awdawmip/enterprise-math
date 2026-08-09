"""E001.5 exact small-instance frontier for multi-tick primitive motion histories.

E001.4 returns a finite relation of maximum-admission after-states for one tick.
This module composes that relation across an explicit *open-loop* integer action
schedule.  At each tick every body has one proposed primitive step; rejected
proposals become waits for that tick, and the next scheduled proposal is still
consumed on the next tick.  This is an explicit reference semantics, not a claim
that real dynamics should use open-loop control.

The resulting complete response history is a finite word of accepted-body-id
sets.  Such a history maps to exactly one terminal body configuration, so
ordinary functional fiber/history-merge language applies to the enumerated
history -> terminal-state map.  The simple binomial collision spectrum reported
here is therefore an engineering specialization of the existing P011/A1 fiber
construction, not a new mother theorem.

The oracle is exponential in branching and is intentionally for small exact
experiments only.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb
from collections.abc import Mapping, Sequence

from .engineering_collision import Body2D
from .motion_collapse import BodyMotion2D, Vector2D, maximum_conflict_free_outcomes

MotionHistory = tuple[frozenset[int], ...]
BodyState2D = tuple[Body2D, ...]
ScheduleTick = Mapping[int, Vector2D]


@dataclass(frozen=True)
class MotionHistoryReport:
    """Finite terminal fibers of an open-loop primitive response program."""

    ticks: int
    history_count: int
    terminal_state_count: int
    terminal_histories: tuple[tuple[BodyState2D, tuple[MotionHistory, ...]], ...]
    history_collision_spectrum: tuple[tuple[int, int], ...]


def _sorted_state(bodies: Sequence[Body2D]) -> BodyState2D:
    ids = [body.body_id for body in bodies]
    if len(ids) != len(set(ids)):
        raise ValueError("body ids must be unique")
    return tuple(sorted(bodies))


def _validate_tick(ids: frozenset[int], tick: ScheduleTick) -> None:
    if frozenset(tick) != ids:
        raise ValueError("every schedule tick must specify exactly one step per body id")


def _motions_for_state(state: BodyState2D, tick: ScheduleTick) -> list[BodyMotion2D]:
    return [BodyMotion2D(body, tick[body.body_id]) for body in state]


def _collision_spectrum_from_fibers(
    fibers: Mapping[BodyState2D, Sequence[MotionHistory]],
) -> tuple[tuple[int, int], ...]:
    max_size = max((len(histories) for histories in fibers.values()), default=0)
    return tuple(
        (
            order,
            sum(
                comb(len(histories), order)
                for histories in fibers.values()
                if len(histories) >= order
            ),
        )
        for order in range(1, max_size + 1)
    )


def run_open_loop_motion_program(
    initial_bodies: Sequence[Body2D],
    schedule: Sequence[ScheduleTick],
) -> MotionHistoryReport:
    """Enumerate every maximum-admission response history and terminal state.

    Histories that reach the same terminal state remain distinct witnesses in
    that state's fiber.  No history is deleted merely because its final state
    agrees with another history.
    """
    initial = _sorted_state(initial_bodies)
    ids = frozenset(body.body_id for body in initial)
    for tick in schedule:
        _validate_tick(ids, tick)

    frontier: dict[BodyState2D, list[MotionHistory]] = {initial: [()]}
    for tick in schedule:
        next_frontier: dict[BodyState2D, list[MotionHistory]] = {}
        for state, histories in frontier.items():
            motions = _motions_for_state(state, tick)
            outcomes = maximum_conflict_free_outcomes(motions)
            for outcome in outcomes:
                terminal = outcome.bodies
                target_histories = next_frontier.setdefault(terminal, [])
                for history in histories:
                    target_histories.append(history + (outcome.accepted_moving_ids,))
        frontier = next_frontier

    ordered_fibers = tuple(
        (
            state,
            tuple(
                sorted(
                    histories,
                    key=lambda history: tuple(tuple(sorted(ids)) for ids in history),
                )
            ),
        )
        for state, histories in sorted(frontier.items())
    )
    history_count = sum(len(histories) for _state, histories in ordered_fibers)
    spectrum = _collision_spectrum_from_fibers(
        {state: histories for state, histories in ordered_fibers}
    )
    return MotionHistoryReport(
        ticks=len(schedule),
        history_count=history_count,
        terminal_state_count=len(ordered_fibers),
        terminal_histories=ordered_fibers,
        history_collision_spectrum=spectrum,
    )
