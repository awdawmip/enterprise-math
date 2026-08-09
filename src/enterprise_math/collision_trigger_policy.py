"""E001.8 response-trigger diagnostics across spatial and transition semantics.

Spatial collapse-contact extinction does not by itself imply that an effective
hard-exclusion response disappears.  A response policy may subscribe to more
than one finite witness class:

* sampled macro contact at the start/end body supports;
* primitive transition conflict (shared endpoint/atomic-edge target).

For a fixed one-tick pair, the sampled-static trigger depends only on

    g_sample = min(g_start, g_end).

If ``g_sample>0``, sampled-static triggering exists exactly for spatial factors
``d>=g_sample+1`` and first extinguishes on refinement to ``d=g_sample``.  If
``g_sample=0``, sampled-static triggering persists at terminal factor 1.

For ``TRANSITION_AWARE``, a primitive transition conflict is independent of
spatial collapse factor in the current model.  Such a conflict therefore has no
pure-spatial extinction factor; if no transition conflict exists, the policy
shares the sampled-static threshold.

These are trigger thresholds, not physical rebound laws.  A named response law
may consume the trigger later, but no force/impulse/elasticity semantics is
assigned here.
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

    @property
    def sampled_static_primitive_gap(self) -> int:
        return min(self.start_primitive_gap, self.end_primitive_gap)


def _require_positive_factor(collapse_factor: int) -> None:
    if (
        isinstance(collapse_factor, bool)
        or not isinstance(collapse_factor, int)
        or collapse_factor <= 0
    ):
        raise ValueError("collapse_factor must be a positive integer")


def collision_trigger_profile(
    left: BodyMotion2D,
    right: BodyMotion2D,
    collapse_factor: int,
) -> CollisionTriggerProfile2D:
    """Collect distinct static-collapse and primitive-transition pair witnesses."""
    if left.body_id == right.body_id:
        raise ValueError("trigger pair must contain distinct body ids")
    _require_positive_factor(collapse_factor)
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


def sampled_static_trigger_first_resolving_factor(
    left: BodyMotion2D,
    right: BodyMotion2D,
) -> int | None:
    """First coarse-to-fine factor where sampled-static triggering disappears.

    ``None`` means at least one sampled endpoint has primitive contact, so the
    sampled-static trigger persists at terminal spatial factor 1.
    """
    if left.body_id == right.body_id:
        raise ValueError("trigger pair must contain distinct body ids")
    gap = min(
        primitive_clearance(left.body, right.body),
        primitive_clearance(left.end_body, right.end_body),
    )
    return None if gap == 0 else gap


def policy_spatial_extinction_factor(
    left: BodyMotion2D,
    right: BodyMotion2D,
    policy: TriggerPolicy,
) -> int | None:
    """Return the first factor where this trigger policy is spatially extinguished.

    ``None`` means the named trigger remains active at terminal spatial factor 1
    for this fixed pair motion.  For transition-aware policy this happens when
    the primitive transition relation itself conflicts, regardless of sampled
    endpoint gaps.
    """
    sampled = sampled_static_trigger_first_resolving_factor(left, right)
    if policy == SAMPLED_STATIC:
        return sampled
    if policy == TRANSITION_AWARE:
        if motion_conflict(left, right):
            return None
        return sampled
    raise ValueError("unknown trigger policy")
