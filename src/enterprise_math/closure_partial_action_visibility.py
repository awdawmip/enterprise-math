"""Partial visibility of labelled helper actions.

For legal progress ideal I of helper poset P and visible helper set Q, observe
only En_P(I) intersect Q.  If Q is itself an order ideal (predecessor/ancestor
closed), then this signature is exactly the enabled frontier of projected ideal
I intersect Q in the induced poset Q and therefore reconstructs that projected
state.

If Q is not predecessor-closed, hidden predecessors can affect visible
enabledness.  The current enabled signature need not factor through I intersect
Q and need not recover that projection.
"""

from __future__ import annotations

from dataclasses import dataclass

from .balanced_binary_synergy import balanced_binary_synergy
from .closure_async_progress_poset import helper_ancestors, helper_ideals
from .closure_async_query_ladder import enabled_helpers


@dataclass(frozen=True)
class PartialVisibilityReport:
    arity: int
    visible_helpers: frozenset[str]
    predecessor_closed: bool
    projected_exact_if_closed: bool
    factorization_collision_left: frozenset[str] | None
    factorization_collision_right: frozenset[str] | None
    same_projection: frozenset[str] | None
    left_visible_enabled: frozenset[str] | None
    right_visible_enabled: frozenset[str] | None
    recovery_collision_left: frozenset[str] | None
    recovery_collision_right: frozenset[str] | None
    same_visible_enabled: frozenset[str] | None


def is_predecessor_closed_visible_set(arity: int, visible: frozenset[str]) -> bool:
    compiler = balanced_binary_synergy(arity)
    helpers = frozenset(compiler.helpers)
    if not visible.issubset(helpers):
        raise ValueError("visible set contains a non-helper label")
    ancestors = helper_ancestors(arity)
    return all(ancestors[helper].issubset(visible) for helper in visible)


def visible_enabled_signature(arity: int, ideal: frozenset[str], visible: frozenset[str]) -> frozenset[str]:
    return frozenset(enabled_helpers(arity, ideal).intersection(visible))


def induced_visible_enabled(arity: int, projected: frozenset[str], visible: frozenset[str]) -> frozenset[str]:
    """Enabled frontier in the induced visible subposet, using ancestor order."""
    if not is_predecessor_closed_visible_set(arity, visible):
        raise ValueError("induced exact visible frontier requires predecessor-closed visible set")
    ancestors = helper_ancestors(arity)
    if not projected.issubset(visible):
        raise ValueError("projected state must lie in visible set")
    result = []
    for helper in visible.difference(projected):
        visible_predecessors = ancestors[helper].intersection(visible)
        # For an ideal projection, all transitive predecessors must be complete.
        if visible_predecessors.issubset(projected):
            result.append(helper)
    # Only minimal incomplete helpers should be enabled. The transitive check
    # above already enforces that no incomplete predecessor remains.
    return frozenset(result)


def partial_visibility_report(arity: int, visible: frozenset[str]) -> PartialVisibilityReport:
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 4:
        raise ValueError("arity must be an integer >= 4")
    compiler = balanced_binary_synergy(arity)
    helpers = frozenset(compiler.helpers)
    if not visible.issubset(helpers):
        raise ValueError("visible set contains a non-helper label")
    ideals = tuple(helper_ideals(arity))
    closed = is_predecessor_closed_visible_set(arity, visible)

    projected_exact = True
    if closed:
        for ideal in ideals:
            projected = frozenset(ideal.intersection(visible))
            if visible_enabled_signature(arity, ideal, visible) != induced_visible_enabled(arity, projected, visible):
                projected_exact = False
                break

    factor_left = factor_right = same_projection = None
    left_sig = right_sig = None
    recovery_left = recovery_right = same_sig = None

    # Same projection but different visible enabledness => signature does not
    # factor through projected state.
    by_projection: dict[frozenset[str], list[frozenset[str]]] = {}
    for ideal in ideals:
        by_projection.setdefault(frozenset(ideal.intersection(visible)), []).append(ideal)
    for projection, bucket in by_projection.items():
        for i in range(len(bucket)):
            sig_i = visible_enabled_signature(arity, bucket[i], visible)
            for j in range(i + 1, len(bucket)):
                sig_j = visible_enabled_signature(arity, bucket[j], visible)
                if sig_i != sig_j:
                    factor_left, factor_right = bucket[i], bucket[j]
                    same_projection = projection
                    left_sig, right_sig = sig_i, sig_j
                    break
            if factor_left is not None:
                break
        if factor_left is not None:
            break

    # Same signature but different projection => signature cannot recover the
    # projected visible progress.
    by_signature: dict[frozenset[str], list[frozenset[str]]] = {}
    for ideal in ideals:
        sig = visible_enabled_signature(arity, ideal, visible)
        by_signature.setdefault(sig, []).append(ideal)
    for sig, bucket in by_signature.items():
        for i in range(len(bucket)):
            proj_i = frozenset(bucket[i].intersection(visible))
            for j in range(i + 1, len(bucket)):
                proj_j = frozenset(bucket[j].intersection(visible))
                if proj_i != proj_j:
                    recovery_left, recovery_right = bucket[i], bucket[j]
                    same_sig = sig
                    break
            if recovery_left is not None:
                break
        if recovery_left is not None:
            break

    return PartialVisibilityReport(
        arity=arity,
        visible_helpers=visible,
        predecessor_closed=closed,
        projected_exact_if_closed=projected_exact if closed else False,
        factorization_collision_left=factor_left,
        factorization_collision_right=factor_right,
        same_projection=same_projection,
        left_visible_enabled=left_sig,
        right_visible_enabled=right_sig,
        recovery_collision_left=recovery_left,
        recovery_collision_right=recovery_right,
        same_visible_enabled=same_sig,
    )
