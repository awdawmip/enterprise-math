"""E001.7 response-trigger diagnostics across spatial and transition semantics.

Spatial collapse-contact extinction does not by itself imply that an effective
hard-exclusion response disappears.  A response policy may subscribe to more
than one finite witness class:

* sampled macro contact at the start/end body supports;
* primitive transition conflict (shared endpoint/atomic-edge target).

This module keeps those witnesses separate and exposes simple trigger policies
without assigning them physical truth.  In particular, a point swap can lose
sampled static contact when refining from ``d=2`` to ``d=1`` while retaining a
primitive edge conflict.  A transition-aware hard-exclusion policy would still
trigger; a static-only policy would not.

Therefore a claimed rebound-extinction threshold is incomplete unless it names
both the spatial collapse semantics and the transition witness/response policy.
"""

from __future__ import annotations

from dataclasses import dataclass

from .collision_phase_diagram import macro_contact_from_gap, primitive_clearance
from .motion_collapse import BodyMotion2D, motion_conflict

SAMPLED_STATIC = "SAMPLED_STATIC"
TRANSITION_AWARE = "TRANSITION_AWARE"
TriggerPolicy = str


@dataclass(frozen=True)
class CollisionTriggerProfile2D:
    """Finite witnesses available to one pair under one spatial factor."""

    pair: tuple[int, int]
    collapse_factor: int
    start_primitive_gap: int
    end_primitive_gap: int
    start_macro_contact: bool
    end_macro_contact: bool
    transition_conflict: bool

    @property
    def sampled_static_trigger(self) -> bool:
        return self.start_macro_contact or self.end_macro_contact

    @property
    def transition_aware_trigger(self) -> bool:
        return self.sampled_static_trigger or self.transition_conflict


def collision_trigger_profile(
    left: BodyMotion2D,
    right: BodyMotion2D,
    collapse_factor: int,
) -> CollisionTriggerProfile2D:
    """Collect distinct static-collapse and primitive-transition pair witnesses."""
    if left.body_id == right.body_id:
        raise ValueError("trigger pair must contain distinct body ids")
    start_gap = primitive_clearance(left.body, right.body)
    end_gap = primitive_clearance(left.end_body, right.end_body)
    return CollisionTriggerProfile2D(
        pair=tuple(sorted((left.body_id, right.body_id))),
        collapse_factor=collapse_factor,
        start_primitive_gap=start_gap,
        end_primitive_gap=end_gap,
        start_macro_contact=macro_contact_from_gap(start_gap, collapse_factor),
        end_macro_contact=macro_contact_from_gap(end_gap, collapse_factor),
        transition_conflict=motion_conflict(left, right),
    )


def response_triggered(profile: CollisionTriggerProfile2D, policy: TriggerPolicy) -> bool:
    """Evaluate one explicitly named finite hard-exclusion trigger policy."""
    if policy == SAMPLED_STATIC:
        return profile.sampled_static_trigger
    if policy == TRANSITION_AWARE:
        return profile.transition_aware_trigger
    raise ValueError("unknown trigger policy")
