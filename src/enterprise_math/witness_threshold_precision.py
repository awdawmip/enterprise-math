"""Generic threshold-observable precision induced by a witness cost.

This module is an elementary consequence of P023's future-observable repair
principle.  Given a cost/horizon ``mu`` with values in the natural numbers or
``None`` for infinity, a bounded task that asks only the predicates
``mu <= j`` for ``0 <= j <= K`` does not need the full value of ``mu``.  The
truncated coordinate

    tau_K(mu) = min(mu, K + 1)

(with infinity mapped to ``K+1``) is the complete and coarsest signature for
that threshold family.

The result is generic finite-precision plumbing, not an abc theorem and not a
novelty claim beyond the P023 minimal-repair framework.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping

State = Hashable
Cost = int | None


def _require_cutoff(cutoff: int) -> None:
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 0:
        raise ValueError("cutoff must be a non-negative integer")


def _require_cost(cost: Cost) -> None:
    if cost is None:
        return
    if isinstance(cost, bool) or not isinstance(cost, int) or cost < 0:
        raise ValueError("cost must be a non-negative integer or None for infinity")


def truncated_witness_cost(cost: Cost, cutoff: int) -> int:
    """Return ``min(cost, cutoff+1)``, mapping infinity to ``cutoff+1``."""
    _require_cost(cost)
    _require_cutoff(cutoff)
    overflow = cutoff + 1
    if cost is None or cost > cutoff:
        return overflow
    return cost


def threshold_profile(cost: Cost, cutoff: int) -> tuple[bool, ...]:
    """Return all threshold observations ``cost <= j`` for ``0<=j<=cutoff``."""
    _require_cost(cost)
    _require_cutoff(cutoff)
    if cost is None:
        return tuple(False for _ in range(cutoff + 1))
    return tuple(cost <= radius for radius in range(cutoff + 1))


def threshold_signature_equivalent(left: Cost, right: Cost, cutoff: int) -> bool:
    """Check the exact equivalence between threshold profile and truncation."""
    same_profile = threshold_profile(left, cutoff) == threshold_profile(right, cutoff)
    same_truncation = (
        truncated_witness_cost(left, cutoff)
        == truncated_witness_cost(right, cutoff)
    )
    if same_profile != same_truncation:
        raise AssertionError("threshold profile and truncated cost disagree")
    return same_profile


def project_truncated_cost(fine_value: int, coarse_cutoff: int) -> int:
    """Project a finer truncated coordinate to a lower cutoff."""
    _require_cutoff(coarse_cutoff)
    if isinstance(fine_value, bool) or not isinstance(fine_value, int) or fine_value < 0:
        raise ValueError("fine_value must be a non-negative integer")
    return min(fine_value, coarse_cutoff + 1)


def truncation_chain_compatible(cost: Cost, low: int, high: int) -> bool:
    """Verify exact projection compatibility along increasing witness cutoffs."""
    _require_cutoff(low)
    _require_cutoff(high)
    if low > high:
        raise ValueError("low cutoff must not exceed high cutoff")
    fine = truncated_witness_cost(cost, high)
    coarse = truncated_witness_cost(cost, low)
    return project_truncated_cost(fine, low) == coarse


def repaired_threshold_state(
    base_state: Hashable, cost: Cost, cutoff: int
) -> tuple[Hashable, int]:
    """Return the P023-style repair ``(q, tau_K(mu))`` for threshold tasks."""
    return (base_state, truncated_witness_cost(cost, cutoff))


def analyze_threshold_repair(
    base_states: Mapping[State, Hashable],
    costs: Mapping[State, Cost],
    cutoff: int,
) -> dict[str, object]:
    """Check finite exactness and coarsest-repair semantics on a state set.

    The returned partition groups states by ``(q(x), tau_K(mu(x)))``.  For every
    pair in one block all threshold observations ``mu<=j`` for ``j<=K`` agree.
    Conversely, two states with the same base state and the same full threshold
    profile necessarily lie in the same repaired block.  This is the finite
    executable form of the coarsest-refinement theorem.
    """
    _require_cutoff(cutoff)
    if set(base_states) != set(costs):
        raise ValueError("base_states and costs must have identical state keys")
    if not base_states:
        raise ValueError("state set must be nonempty")

    repaired = {
        state: repaired_threshold_state(base_states[state], costs[state], cutoff)
        for state in base_states
    }
    profiles = {
        state: threshold_profile(costs[state], cutoff)
        for state in base_states
    }

    states = tuple(base_states)
    for i, left in enumerate(states):
        for right in states[i + 1 :]:
            same_repair = repaired[left] == repaired[right]
            same_required_observations = (
                base_states[left] == base_states[right]
                and profiles[left] == profiles[right]
            )
            if same_repair != same_required_observations:
                raise AssertionError("threshold repair is not the exact coarsest signature")

    blocks: dict[tuple[Hashable, int], list[State]] = {}
    for state, signature in repaired.items():
        blocks.setdefault(signature, []).append(state)

    return {
        "cutoff": cutoff,
        "repaired_states": repaired,
        "threshold_profiles": profiles,
        "blocks": {key: tuple(value) for key, value in blocks.items()},
        "block_count": len(blocks),
    }
