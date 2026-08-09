"""E001.4 finite collision-response relation for the square-body pressure test.

The common-collapse contact certificate determines how much *relative* integer
translation is needed to separate two supports.  It does not, by geometry alone,
determine how that relative correction must be allocated between the two bodies.

This module therefore keeps response relational.  For every globally shortest
axis-only relative correction it enumerates all allocations whose total L1
translation is also minimal.  A secondary ``balanced`` view retains allocations
that minimize the maximum correction assigned to either body.  Explicit
anchoring can remove allocation freedom when an external constraint says that
one body is fixed.

Nothing here is a force, impulse, momentum, elasticity, mass, or energy law.  It
is an exact finite de-overlap construction used to determine what additional
state a later dynamics layer would need in order to choose one after-state.
"""

from __future__ import annotations

from dataclasses import dataclass

from .collapse_contact import Vector2D, collapse_contact_profile
from .engineering_collision import Body2D, Pair


def l1_steps(vector: Vector2D) -> int:
    """Return the integer L1 step count of one correction vector."""
    return abs(vector[0]) + abs(vector[1])


@dataclass(frozen=True, order=True)
class PairResponse2D:
    """One exact minimum-work allocation of a relative separation correction."""

    left_id: int
    right_id: int
    left_delta: Vector2D
    right_delta: Vector2D
    relative_delta: Vector2D
    total_steps: int
    max_body_steps: int

    @property
    def pair(self) -> Pair:
        return tuple(sorted((self.left_id, self.right_id)))


def _minimal_work_allocations(relative_delta: Vector2D) -> tuple[tuple[Vector2D, Vector2D], ...]:
    """Enumerate every minimum-total-L1 split of one axis-only relative delta.

    The required relation is

        right_delta - left_delta = relative_delta.

    By the triangle inequality, every allocation costs at least
    ``|relative_delta|_1`` in total.  For a positive axis correction ``n``, all
    minimum-cost solutions move the left body ``a`` steps in the negative
    direction and the right body ``n-a`` steps in the positive direction, for
    ``0 <= a <= n``.  The negative case is its sign reversal.
    """
    dx, dy = relative_delta
    if (dx == 0) == (dy == 0):
        raise ValueError("relative_delta must be nonzero and axis-only")

    along_x = dx != 0
    amount = dx if along_x else dy
    sign = 1 if amount > 0 else -1
    magnitude = abs(amount)

    allocations: list[tuple[Vector2D, Vector2D]] = []
    for left_share in range(magnitude + 1):
        left_component = -sign * left_share
        right_component = sign * (magnitude - left_share)
        if along_x:
            left_delta = (left_component, 0)
            right_delta = (right_component, 0)
        else:
            left_delta = (0, left_component)
            right_delta = (0, right_component)
        allocations.append((left_delta, right_delta))
    return tuple(allocations)


def minimal_pair_responses(left: Body2D, right: Body2D) -> tuple[PairResponse2D, ...]:
    """Return all minimum-total-step de-overlap responses for a colliding pair.

    Separate bodies have no response candidates because no correction is needed.
    For colliding bodies, every returned candidate has globally minimal total L1
    correction among all translations that make the two axis-aligned supports
    disjoint.
    """
    if left.body_id == right.body_id:
        raise ValueError("response pair must contain two distinct body ids")
    profile = collapse_contact_profile(left, right)
    if profile is None:
        return ()

    responses: set[PairResponse2D] = set()
    for relative in profile.minimum_relative_corrections:
        minimum = l1_steps(relative)
        for left_delta, right_delta in _minimal_work_allocations(relative):
            total = l1_steps(left_delta) + l1_steps(right_delta)
            if total != minimum:
                raise AssertionError("minimum-work allocation exceeded relative lower bound")
            responses.add(
                PairResponse2D(
                    left_id=left.body_id,
                    right_id=right.body_id,
                    left_delta=left_delta,
                    right_delta=right_delta,
                    relative_delta=relative,
                    total_steps=total,
                    max_body_steps=max(l1_steps(left_delta), l1_steps(right_delta)),
                )
            )
    return tuple(sorted(responses))


def balanced_pair_responses(left: Body2D, right: Body2D) -> tuple[PairResponse2D, ...]:
    """Keep minimum-work responses that also minimize the largest body correction."""
    responses = minimal_pair_responses(left, right)
    if not responses:
        return ()
    best = min(response.max_body_steps for response in responses)
    return tuple(response for response in responses if response.max_body_steps == best)


def anchored_pair_responses(
    left: Body2D,
    right: Body2D,
    fixed_body_id: int,
) -> tuple[PairResponse2D, ...]:
    """Return minimum-work responses compatible with one explicitly fixed body.

    Anchoring is an external constraint, not inferred from collision geometry.
    It is included to show how additional state can turn allocation ambiguity
    into a smaller response relation without encoding a hidden body-id priority.
    """
    if fixed_body_id not in (left.body_id, right.body_id):
        raise ValueError("fixed_body_id must identify one body in the response pair")
    responses = minimal_pair_responses(left, right)
    if fixed_body_id == left.body_id:
        return tuple(response for response in responses if response.left_delta == (0, 0))
    return tuple(response for response in responses if response.right_delta == (0, 0))


def apply_pair_response(
    left: Body2D,
    right: Body2D,
    response: PairResponse2D,
) -> tuple[Body2D, Body2D]:
    """Apply one oriented response candidate to the corresponding body pair."""
    if response.left_id != left.body_id or response.right_id != right.body_id:
        raise ValueError("response orientation does not match the supplied bodies")
    updated_left = Body2D(
        left.body_id,
        left.x + response.left_delta[0],
        left.y + response.left_delta[1],
        left.radius,
    )
    updated_right = Body2D(
        right.body_id,
        right.x + response.right_delta[0],
        right.y + response.right_delta[1],
        right.radius,
    )
    return updated_left, updated_right
