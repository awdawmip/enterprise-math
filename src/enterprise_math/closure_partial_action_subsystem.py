"""Exact projected subsystem for predecessor-closed helper action families.

If visible helper action set Q is an order ideal of the dependency poset, then
projection pi_Q(I)=I intersect Q is a homomorphism of the labelled partial
transition family restricted to Q:

* q is globally enabled at I iff q is enabled in projected ideal pi_Q(I);
* when enabled, pi_Q(I union {q}) = pi_Q(I) union {q}.

Hence every finite Q-action word, including prefix legality, factors through the
projected ideal. Combined with the enabled-frontier theorem, current visible
enabledness is already sufficient for the whole predecessor-closed Q future.
"""

from __future__ import annotations

from dataclasses import dataclass

from .closure_async_progress_poset import helper_ideals
from .closure_async_query_ladder import enabled_helpers
from .closure_partial_action_visibility import (
    induced_visible_enabled,
    is_predecessor_closed_visible_set,
    visible_enabled_signature,
)


@dataclass(frozen=True)
class PartialSubsystemReport:
    arity: int
    visible_helpers: frozenset[str]
    predecessor_closed: bool
    one_step_factorization_verified: bool
    current_enabled_recovers_projection: bool
    nonclosed_legality_collision: bool


def fire_global_helper(arity: int, ideal: frozenset[str], helper: str) -> frozenset[str] | None:
    if helper not in enabled_helpers(arity, ideal):
        return None
    return frozenset(set(ideal) | {helper})


def fire_projected_helper(
    arity: int,
    projected: frozenset[str],
    visible: frozenset[str],
    helper: str,
) -> frozenset[str] | None:
    if helper not in visible:
        raise ValueError("helper is not in visible action family")
    if helper not in induced_visible_enabled(arity, projected, visible):
        return None
    return frozenset(set(projected) | {helper})


def partial_subsystem_report(arity: int, visible: frozenset[str]) -> PartialSubsystemReport:
    ideals = tuple(helper_ideals(arity))
    closed = is_predecessor_closed_visible_set(arity, visible)
    one_step = True
    recover = True
    collision = False

    if closed:
        signature_to_projection: dict[frozenset[str], frozenset[str]] = {}
        for ideal in ideals:
            projected = frozenset(ideal.intersection(visible))
            signature = visible_enabled_signature(arity, ideal, visible)
            prior = signature_to_projection.get(signature)
            if prior is not None and prior != projected:
                recover = False
            signature_to_projection[signature] = projected
            for helper in visible:
                global_next = fire_global_helper(arity, ideal, helper)
                projected_next = fire_projected_helper(arity, projected, visible, helper)
                if (global_next is None) != (projected_next is None):
                    one_step = False
                    continue
                if global_next is not None:
                    if frozenset(global_next.intersection(visible)) != projected_next:
                        one_step = False
    else:
        # A length-one collision is enough to show that projection is not an
        # autonomous legality-sensitive subsystem.
        by_projection: dict[frozenset[str], list[frozenset[str]]] = {}
        for ideal in ideals:
            by_projection.setdefault(frozenset(ideal.intersection(visible)), []).append(ideal)
        for bucket in by_projection.values():
            for i in range(len(bucket)):
                sig_i = visible_enabled_signature(arity, bucket[i], visible)
                for j in range(i + 1, len(bucket)):
                    sig_j = visible_enabled_signature(arity, bucket[j], visible)
                    if sig_i != sig_j:
                        collision = True
                        break
                if collision:
                    break
            if collision:
                break
        one_step = False
        recover = False

    return PartialSubsystemReport(
        arity=arity,
        visible_helpers=visible,
        predecessor_closed=closed,
        one_step_factorization_verified=one_step if closed else False,
        current_enabled_recovers_projection=recover if closed else False,
        nonclosed_legality_collision=collision,
    )
