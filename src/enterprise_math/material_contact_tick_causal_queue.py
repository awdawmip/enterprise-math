"""Causal consumption relation for a prequantized multi-contact material tick.

The batched material-contact tick first quantizes every local material reservoir
and obtains a nonnegative whole-impulse vector ``J``.  If a world then insists
on guarded unit-by-unit application, it may be impossible to consume all of
``J``.  The remaining whole quanta are not subquantum remainder and cannot be
silently discarded.

For initial contact scores ``r`` and coupling ``K``, a prefix count ``n`` is
reachable when some legal guarded word has that count.  A reachable prefix is
terminal relative to budget ``J`` when either ``n=J`` or no remaining required
contact is currently enabled.  The exact terminal relation is finite because
``0<=n<=J``.

For one terminal prefix define the unapplied whole-quantum queue

    Q = J - n.

If contact ``e`` had amplitude ``A_e``, initial local remainder ``delta_e`` and
material response total ``R_e``, local quantization already proved

    A_e*J_e + delta'_e = delta_e + S_e*R_e.

Splitting ``J_e=n_e+Q_e`` gives the causal ledger

    A_e*n_e + A_e*Q_e + delta'_e
      = delta_e + S_e*R_e.

Thus a guarded prequantized world needs ``Q`` as an explicit state whenever the
budget cannot be fully applied.  Dropping ``Q`` loses whole delivered quanta;
folding it into canonical ``delta'<A`` is impossible without changing semantics.

The terminal relation can itself be scheduler-valued.  Positive cross-coupling
may allow one order to consume all of ``J`` while another legal order dead-ends
with a nonzero queue.  By contrast, on a Z-coupled system, if ``J`` has one legal
completion then every maximal legal consumption word reaches ``J``; the
terminal relation is the singleton ``{J}``.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Sequence

from .material_contact_network_impulse_1d import (
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_coupling_gram,
    contact_relative_scores,
)
from .material_contact_network_tick_1d import ContactMaterialNetworkTick1D
from .material_contact_tick_policy import (
    coupling_is_z_matrix,
    enabled_remaining_contacts,
    score_after_counts,
)


Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


def _normalize(
    initial_scores: Sequence[int],
    coupling: Sequence[Sequence[int]],
    target_counts: Sequence[int],
) -> tuple[Vector, Matrix, Vector]:
    scores = tuple(initial_scores)
    target = tuple(target_counts)
    if not scores:
        raise ValueError("initial_scores must be nonempty")
    if len(target) != len(scores):
        raise ValueError("target_counts must match score dimension")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in scores):
        raise TypeError("initial scores must be integers")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in target
    ):
        raise ValueError("target counts must be nonnegative integers")
    matrix = tuple(tuple(row) for row in coupling)
    if len(matrix) != len(scores) or any(len(row) != len(scores) for row in matrix):
        raise ValueError("coupling matrix must match score dimension")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in matrix
        for value in row
    ):
        raise TypeError("coupling entries must be integers")
    return scores, matrix, target


@dataclass(frozen=True)
class GuardedTerminalPrefix:
    applied_counts: Vector
    queued_counts: Vector
    representative_word: tuple[int, ...]
    terminal_scores: Vector

    @property
    def fully_consumed(self) -> bool:
        return not any(self.queued_counts)


@dataclass(frozen=True)
class GuardedTerminalRelation:
    target_counts: Vector
    terminals: tuple[GuardedTerminalPrefix, ...]
    reachable_count_states: int
    z_coupled: bool

    @property
    def full_consumption_possible(self) -> bool:
        return any(terminal.fully_consumed for terminal in self.terminals)

    @property
    def scheduler_independent_full_consumption(self) -> bool:
        return (
            len(self.terminals) == 1
            and self.terminals[0].fully_consumed
        )


def guarded_terminal_prefix_relation(
    initial_scores: Sequence[int],
    coupling: Sequence[Sequence[int]],
    target_counts: Sequence[int],
) -> GuardedTerminalRelation:
    """Enumerate every reachable consume-until-stuck prefix count state."""
    scores, matrix, target = _normalize(
        initial_scores,
        coupling,
        target_counts,
    )
    zero = (0,) * len(target)
    queue: deque[Vector] = deque([zero])
    predecessor: dict[Vector, tuple[Vector, int] | None] = {zero: None}
    terminals: list[GuardedTerminalPrefix] = []

    while queue:
        prefix = queue.popleft()
        enabled = enabled_remaining_contacts(
            scores,
            matrix,
            prefix,
            target,
        )
        if prefix == target or not enabled:
            word: list[int] = []
            current = prefix
            while predecessor[current] is not None:
                previous, action = predecessor[current]
                word.append(action)
                current = previous
            word.reverse()
            queued = tuple(
                required - used
                for used, required in zip(prefix, target, strict=True)
            )
            terminals.append(
                GuardedTerminalPrefix(
                    applied_counts=prefix,
                    queued_counts=queued,
                    representative_word=tuple(word),
                    terminal_scores=score_after_counts(scores, matrix, prefix),
                )
            )
            continue

        for action in enabled:
            nxt = tuple(
                value + (1 if index == action else 0)
                for index, value in enumerate(prefix)
            )
            if nxt in predecessor:
                continue
            predecessor[nxt] = (prefix, action)
            queue.append(nxt)

    return GuardedTerminalRelation(
        target_counts=target,
        terminals=tuple(sorted(terminals, key=lambda item: item.applied_counts)),
        reachable_count_states=len(predecessor),
        z_coupled=coupling_is_z_matrix(matrix),
    )


@dataclass(frozen=True)
class MaterialCausalQueueOutcome:
    terminal: GuardedTerminalPrefix
    after: ContactNetworkMomentum1D
    local_ledger_residuals: Vector


@dataclass(frozen=True)
class MaterialCausalQueueRelation:
    tick: ContactMaterialNetworkTick1D
    terminal_relation: GuardedTerminalRelation
    outcomes: tuple[MaterialCausalQueueOutcome, ...]

    @property
    def has_nonzero_queue(self) -> bool:
        return any(
            any(outcome.terminal.queued_counts)
            for outcome in self.outcomes
        )


def material_tick_causal_queue_relation(
    tick: ContactMaterialNetworkTick1D,
) -> MaterialCausalQueueRelation:
    """Turn one prequantized batched tick into its guarded terminal/queue relation."""
    if not isinstance(tick, ContactMaterialNetworkTick1D):
        raise TypeError("tick must be ContactMaterialNetworkTick1D")
    initial_scores = contact_relative_scores(tick.before)
    gram = contact_coupling_gram(tick.before)
    relation = guarded_terminal_prefix_relation(
        initial_scores,
        gram,
        tick.delivered_impulse_vector,
    )

    outcomes: list[MaterialCausalQueueOutcome] = []
    for terminal in relation.terminals:
        network_step = apply_contact_impulse_vector(
            tick.before,
            terminal.applied_counts,
        )
        residuals = []
        for index, (
            reservoir_before,
            sequence,
            reservoir_after,
            applied,
            queued,
        ) in enumerate(
            zip(
                tick.reservoir_before,
                tick.channel_sequences,
                tick.reservoir_after,
                terminal.applied_counts,
                terminal.queued_counts,
                strict=True,
            )
        ):
            lhs = (
                reservoir_before.amplitude * applied
                + reservoir_before.amplitude * queued
                + reservoir_after.pending_numerator
            )
            rhs = (
                reservoir_before.pending_numerator
                + reservoir_before.impulse_scale * sequence.response_total
            )
            residual = lhs - rhs
            if residual != 0:
                raise AssertionError(
                    f"contact {index} causal applied/queue ledger failed"
                )
            residuals.append(residual)

        if network_step.after.total_momentum != tick.before.total_momentum:
            raise AssertionError("causal prefix changed total body momentum")
        outcomes.append(
            MaterialCausalQueueOutcome(
                terminal=terminal,
                after=network_step.after,
                local_ledger_residuals=tuple(residuals),
            )
        )

    return MaterialCausalQueueRelation(
        tick=tick,
        terminal_relation=relation,
        outcomes=tuple(outcomes),
    )
