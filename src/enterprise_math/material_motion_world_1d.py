"""Multi-tick sampled motion-budget automaton for the E001 material wall toy world.

State is only

    (center, next_signed_motion_budget).

At each tick the budget proposes one sampled displacement.  Under the declared
policy:

* ACCEPT/TRANSMIT keeps the same signed motion budget for the next tick;
* REBOUND replaces it by the returned integer budget in the opposite direction;
* MATERIAL_UNDERRESOLVED records the proposal and halts the represented history
  without inventing an after-state.

This persistence rule is an explicit engineering world policy, not Newton's law.
The automaton intentionally delegates primitive endpoint contact to another
future rule; the coarse-layer helper requires positive primitive pre/post gaps.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_collapse_world_1d import (
    ACCEPT,
    REBOUND,
    TRANSMIT,
    UNDERRESOLVED,
    CollapseMaterialWorldOutcome1D,
    collapse_material_wall_step,
)
from .material_response import MaterialCurveProfile
from .scale_tunneling_1d import Wall1D


@dataclass(frozen=True)
class MotionBudgetState1D:
    """One finite sampled world state."""

    center: int
    signed_motion_budget: int

    def __post_init__(self) -> None:
        for name, value in (
            ("center", self.center),
            ("signed_motion_budget", self.signed_motion_budget),
        ):
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError(f"{name} must be an integer")


@dataclass(frozen=True)
class MotionBudgetTransition1D:
    """One sampled proposal/outcome and optional next motion state."""

    before: MotionBudgetState1D
    proposed_end_center: int
    wall_outcome: CollapseMaterialWorldOutcome1D
    after: MotionBudgetState1D | None


@dataclass(frozen=True)
class MotionBudgetHistory1D:
    """Finite multi-tick history, possibly halted by material underresolution."""

    initial: MotionBudgetState1D
    transitions: tuple[MotionBudgetTransition1D, ...]
    final: MotionBudgetState1D | None
    rebound_count: int
    transmission_count: int
    accept_count: int
    underresolved_count: int
    halted_underresolved: bool


def step_motion_budget_world(
    state: MotionBudgetState1D,
    wall: Wall1D,
    radius: int,
    collapse_factor: int,
    material_profile: MaterialCurveProfile,
) -> MotionBudgetTransition1D:
    """Advance one represented tick, or return an explicit unresolved transition."""
    proposed = state.center + state.signed_motion_budget
    outcome = collapse_material_wall_step(
        wall,
        state.center,
        proposed,
        radius,
        collapse_factor,
        material_profile,
    )
    if outcome.kind == UNDERRESOLVED:
        if outcome.after_center is not None or outcome.rebound is not None:
            raise AssertionError("underresolved outcome must not invent response state")
        return MotionBudgetTransition1D(
            before=state,
            proposed_end_center=proposed,
            wall_outcome=outcome,
            after=None,
        )

    if outcome.after_center is None:
        raise AssertionError("resolved material wall outcome lost its after-state")
    if outcome.kind == REBOUND:
        if outcome.rebound is None:
            raise AssertionError("rebound outcome lost returned budget")
        if state.signed_motion_budget > 0:
            next_budget = -outcome.rebound.returned_budget
        elif state.signed_motion_budget < 0:
            next_budget = outcome.rebound.returned_budget
        else:
            next_budget = 0
    elif outcome.kind in (ACCEPT, TRANSMIT):
        next_budget = state.signed_motion_budget
    else:
        raise AssertionError("unknown material wall outcome kind")

    after = MotionBudgetState1D(
        center=outcome.after_center,
        signed_motion_budget=next_budget,
    )
    return MotionBudgetTransition1D(
        before=state,
        proposed_end_center=proposed,
        wall_outcome=outcome,
        after=after,
    )


def run_motion_budget_world(
    initial: MotionBudgetState1D,
    wall: Wall1D,
    radius: int,
    collapse_factor: int,
    material_profile: MaterialCurveProfile,
    ticks: int,
) -> MotionBudgetHistory1D:
    """Run represented ticks, halting rather than guessing on underresolution."""
    if isinstance(ticks, bool) or not isinstance(ticks, int) or ticks < 0:
        raise ValueError("ticks must be a non-negative integer")
    state: MotionBudgetState1D | None = initial
    transitions: list[MotionBudgetTransition1D] = []
    for _ in range(ticks):
        if state is None:
            break
        transition = step_motion_budget_world(
            state,
            wall,
            radius,
            collapse_factor,
            material_profile,
        )
        transitions.append(transition)
        state = transition.after
        if state is None:
            break

    underresolved_count = sum(
        transition.wall_outcome.kind == UNDERRESOLVED for transition in transitions
    )
    return MotionBudgetHistory1D(
        initial=initial,
        transitions=tuple(transitions),
        final=state,
        rebound_count=sum(
            transition.wall_outcome.kind == REBOUND for transition in transitions
        ),
        transmission_count=sum(
            transition.wall_outcome.kind == TRANSMIT for transition in transitions
        ),
        accept_count=sum(
            transition.wall_outcome.kind == ACCEPT for transition in transitions
        ),
        underresolved_count=underresolved_count,
        halted_underresolved=underresolved_count > 0,
    )
