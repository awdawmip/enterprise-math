"""Batch acceleration for the weighted 1D contact-chain least-action solver.

The unit-update owner ``material_weighted_chain_least_action_1d`` already proves
that an aligned weighted path has a unique componentwise-least feasible impulse.
This module changes only the update granularity, not the mathematical target.

For a current impulse vector ``j`` and contact score ``s_i<0``, let

    t_i = ceil((-s_i) / K_ii).

If ``v`` is any feasible impulse vector with ``j<=v``, the Z-matrix sign pattern
``K_ik<=0`` for ``k!=i`` gives

    0 <= score_i(v)
      = s_i + K_ii(v_i-j_i) + sum_{k!=i} K_ik(v_k-j_k)
      <= s_i + K_ii(v_i-j_i).

Hence ``v_i-j_i >= t_i``.  Increasing ``j_i`` by the whole batch ``t_i`` stays
componentwise below every feasible vector, exactly as the unit update does.
Repeatedly choosing any violated contact and applying its exact batch therefore
terminates at the same unique least impulse, independent of priority.

The explicit feasible upper witness from the unit owner remains a finite bound.
This is an E001 engineering acceleration of an already established Z-path
least-action theorem; no new generic M/Z-matrix or obstacle-algorithm novelty is
claimed.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import (
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_coupling_gram,
    contact_relative_scores,
)
from .material_weighted_chain_least_action_1d import (
    solve_weighted_chain_least_action,
    weighted_chain_feasible_upper_witness,
    weighted_chain_priority,
)


def _ceil_div_positive(numerator: int, denominator: int) -> int:
    if numerator <= 0 or denominator <= 0:
        raise ValueError("batch ceil-div requires positive numerator and denominator")
    return (numerator + denominator - 1) // denominator


@dataclass(frozen=True)
class WeightedChainBatchEvent1D:
    contact_index: int
    score_before: int
    diagonal_coupling: int
    batch_size: int
    impulse_before: int
    impulse_after: int
    scores_after: tuple[int, ...]


@dataclass(frozen=True)
class WeightedChainBatchSolution1D:
    before: ContactNetworkMomentum1D
    priority: tuple[int, ...]
    initial_scores: tuple[int, ...]
    feasible_upper_impulse: tuple[int, ...]
    impulse_vector: tuple[int, ...]
    final_scores: tuple[int, ...]
    final_momenta: tuple[int, ...]
    events: tuple[WeightedChainBatchEvent1D, ...]

    @property
    def batch_count(self) -> int:
        return len(self.events)

    @property
    def delivered_impulse_quanta(self) -> int:
        return sum(self.impulse_vector)


def solve_weighted_chain_batch_least_action(
    state: ContactNetworkMomentum1D,
    priority: tuple[int, ...] | list[int] | None = None,
) -> WeightedChainBatchSolution1D:
    """Return the same least impulse as the unit solver using exact safe batches."""
    contact_count = len(state.contacts)
    order = weighted_chain_priority(contact_count, priority)
    # Reuse the unit owner for hypothesis validation and a finite oracle target.
    unit = solve_weighted_chain_least_action(state, order)
    upper = weighted_chain_feasible_upper_witness(state).prefix_impulse_vector
    gram = contact_coupling_gram(state)
    scores = list(contact_relative_scores(state))
    impulses = [0] * contact_count
    events: list[WeightedChainBatchEvent1D] = []

    while True:
        violated = {index for index, score in enumerate(scores) if score < 0}
        if not violated:
            break
        chosen = next(index for index in order if index in violated)
        diagonal = gram[chosen][chosen]
        if diagonal <= 0:
            raise AssertionError("weighted-chain batch update lost positive diagonal")
        batch = _ceil_div_positive(-scores[chosen], diagonal)
        if impulses[chosen] + batch > upper[chosen]:
            raise AssertionError("safe batch escaped explicit feasible upper witness")

        score_before = scores[chosen]
        impulse_before = impulses[chosen]
        impulses[chosen] += batch
        for row in range(contact_count):
            scores[row] += gram[row][chosen] * batch
        if scores[chosen] < 0:
            raise AssertionError("batch failed to repair its selected contact")
        events.append(
            WeightedChainBatchEvent1D(
                contact_index=chosen,
                score_before=score_before,
                diagonal_coupling=diagonal,
                batch_size=batch,
                impulse_before=impulse_before,
                impulse_after=impulses[chosen],
                scores_after=tuple(scores),
            )
        )

    result = tuple(impulses)
    if result != unit.impulse_vector:
        raise AssertionError("batch least-action disagrees with canonical unit solver")
    step = apply_contact_impulse_vector(state, result)
    if step.relative_scores_after != tuple(scores):
        raise AssertionError("batch score ledger drifted from contact-network oracle")
    if any(score < 0 for score in step.relative_scores_after):
        raise AssertionError("batch solver terminated with a closing contact")

    return WeightedChainBatchSolution1D(
        before=state,
        priority=order,
        initial_scores=contact_relative_scores(state),
        feasible_upper_impulse=upper,
        impulse_vector=result,
        final_scores=step.relative_scores_after,
        final_momenta=step.after.momenta,
        events=tuple(events),
    )
