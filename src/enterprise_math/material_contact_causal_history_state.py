"""History-aware causal material state without restoring full contact history.

The causal material tick owner retains two finite material coordinates:

* contact-local subquantum remainders ``delta``;
* already-quantized but not yet applied whole-contact queue ``Q``.

A history-dependent future law may additionally read an additive witness ``C j``
of the **actually applied** cumulative contact-impulse history ``j``.  Restoring
all of ``j`` is unnecessary.  Fix one spanning-forest section ``s`` of the
incidence map ``B`` and retain

    b   = B j,
    rho = C (j - s(b)).

Then the exact applied-history witness is

    W_applied = C s(b) + rho.

The causal state therefore needs only

    current network + delta + Q + b + rho,

for this declared history language.  ``b`` is kept explicit rather than inferred
from current momentum so this bridge does not assume that contact impulses are
the only process that can ever change body momentum.

If a tick quantizes new whole vector ``J`` and a guarded terminal branch actually
applies ``n``, then

    Q'   = Q + J - n,
    b'   = b + B n,
    rho' = rho + C (n - s(B n)).

Hence

    W'_applied - W_applied = C n.

The same state also exposes a second, different history semantics without one
extra coordinate.  If a future law counts all **committed / already-quantized**
whole impulses, including queue, define

    W_committed = C (j + Q)
                = W_applied + C Q.

Then the queue cancellation gives the scheduler-independent identity

    W'_committed - W_committed = C J.

Thus ``damage-on-application`` and ``damage-on-quantization`` are distinct world
laws:

* applied history can branch with guarded scheduling because it increments by
  ``C n``;
* committed history increments by ``C J`` and is invariant across all causal
  terminal branches of the same prequantized material tick.

The spanning forest is a gauge, not physical structure.  Changing forest shifts
``rho`` by the existing body-state-only gauge correction and leaves reconstructed
applied/committed witnesses invariant.

Graph sections, cycle-space repair and additive ledgers are standard mathematics.
The E001 contribution here is the exact composition of causal whole-quantum queue
with the previously derived task-relative cycle-history repair.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .contact_cycle_witness_repair import apply_integer_matrix
from .material_contact_causal_tick_state import (
    CausalMaterialContactState1D,
    CausalMaterialTickOutcome1D,
    causal_material_contact_tick,
)
from .material_contact_history_gauge import (
    repair_coordinate_with_forest,
    transform_repair_between_forests,
    tree_section_from_chosen_forest,
)
from .material_contact_network_impulse_1d import contact_incidence_matrix


Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _integer_vector(values: Sequence[int], length: int, *, name: str) -> Vector:
    result = tuple(values)
    if len(result) != length:
        raise ValueError(f"{name} must have length {length}")
    for value in result:
        _require_int(name, value)
    return result


def _witness_matrix(
    values: Sequence[Sequence[int]],
    edge_count: int,
) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError("witness_matrix must contain at least one row")
    if any(len(row) != edge_count for row in rows):
        raise ValueError("witness_matrix must match contact count")
    for row in rows:
        for value in row:
            _require_int("witness entry", value)
    return rows


def _add(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ValueError("vector dimensions must agree")
    return tuple(a + b for a, b in zip(left, right, strict=True))


@dataclass(frozen=True)
class HistoryAwareCausalMaterialState1D:
    """Compressed fixed-topology history state in one explicit forest gauge."""

    causal: CausalMaterialContactState1D
    applied_body_delta: Vector
    history_repair: Vector


def history_state_from_exact_applied_history(
    causal: CausalMaterialContactState1D,
    applied_history: Sequence[int],
    witness_matrix: Sequence[Sequence[int]],
    tree_edges: Sequence[int],
) -> HistoryAwareCausalMaterialState1D:
    """Project one exact applied edge history to ``(b,rho)`` plus causal state."""
    if not isinstance(causal, CausalMaterialContactState1D):
        raise TypeError("causal must be CausalMaterialContactState1D")
    incidence = contact_incidence_matrix(causal.network)
    edge_count = len(causal.network.contacts)
    history = _integer_vector(
        applied_history,
        edge_count,
        name="applied_history",
    )
    witness = _witness_matrix(witness_matrix, edge_count)
    body_delta = apply_integer_matrix(incidence, history)
    repair = repair_coordinate_with_forest(
        incidence,
        witness,
        history,
        tree_edges,
    )
    return HistoryAwareCausalMaterialState1D(
        causal=causal,
        applied_body_delta=body_delta,
        history_repair=repair,
    )


def reconstruct_applied_history_witness(
    state: HistoryAwareCausalMaterialState1D,
    witness_matrix: Sequence[Sequence[int]],
    tree_edges: Sequence[int],
) -> Vector:
    """Reconstruct ``Cj`` from body delta plus cycle repair."""
    if not isinstance(state, HistoryAwareCausalMaterialState1D):
        raise TypeError("state must be HistoryAwareCausalMaterialState1D")
    incidence = contact_incidence_matrix(state.causal.network)
    witness = _witness_matrix(
        witness_matrix,
        len(state.causal.network.contacts),
    )
    body = _integer_vector(
        state.applied_body_delta,
        len(state.causal.network.masses),
        name="applied_body_delta",
    )
    repair = _integer_vector(
        state.history_repair,
        len(witness),
        name="history_repair",
    )
    section = tree_section_from_chosen_forest(
        incidence,
        body,
        tree_edges,
    )
    return _add(apply_integer_matrix(witness, section), repair)


def reconstruct_committed_history_witness(
    state: HistoryAwareCausalMaterialState1D,
    witness_matrix: Sequence[Sequence[int]],
    tree_edges: Sequence[int],
) -> Vector:
    """Return ``C(j+Q)``: applied witness plus queued whole-contact witness."""
    applied = reconstruct_applied_history_witness(
        state,
        witness_matrix,
        tree_edges,
    )
    witness = _witness_matrix(
        witness_matrix,
        len(state.causal.network.contacts),
    )
    queued = apply_integer_matrix(witness, state.causal.whole_queue)
    return _add(applied, queued)


@dataclass(frozen=True)
class HistoryAwareCausalTickOutcome1D:
    causal_outcome: CausalMaterialTickOutcome1D
    after: HistoryAwareCausalMaterialState1D
    repair_increment: Vector
    applied_witness_before: Vector
    applied_witness_after: Vector
    committed_witness_before: Vector
    committed_witness_after: Vector
    applied_witness_increment: Vector
    committed_witness_increment: Vector


@dataclass(frozen=True)
class HistoryAwareCausalTickRelation1D:
    before: HistoryAwareCausalMaterialState1D
    newly_quantized: Vector
    outcomes: tuple[HistoryAwareCausalTickOutcome1D, ...]

    @property
    def applied_history_scheduler_independent(self) -> bool:
        return len({outcome.applied_witness_after for outcome in self.outcomes}) <= 1

    @property
    def committed_history_scheduler_independent(self) -> bool:
        return len({outcome.committed_witness_after for outcome in self.outcomes}) <= 1


def history_aware_causal_material_tick(
    state: HistoryAwareCausalMaterialState1D,
    response_sequences: Sequence[Iterable[int]],
    witness_matrix: Sequence[Sequence[int]],
    tree_edges: Sequence[int],
) -> HistoryAwareCausalTickRelation1D:
    """Advance causal material state and minimal applied-history repair together."""
    if not isinstance(state, HistoryAwareCausalMaterialState1D):
        raise TypeError("state must be HistoryAwareCausalMaterialState1D")
    incidence = contact_incidence_matrix(state.causal.network)
    edge_count = len(state.causal.network.contacts)
    witness = _witness_matrix(witness_matrix, edge_count)

    before_applied = reconstruct_applied_history_witness(
        state,
        witness,
        tree_edges,
    )
    before_committed = reconstruct_committed_history_witness(
        state,
        witness,
        tree_edges,
    )

    causal_relation = causal_material_contact_tick(
        state.causal,
        response_sequences,
    )
    expected_committed_increment = apply_integer_matrix(
        witness,
        causal_relation.newly_quantized,
    )

    outcomes: list[HistoryAwareCausalTickOutcome1D] = []
    for causal_outcome in causal_relation.outcomes:
        applied_increment_counts = causal_outcome.applied_impulse_vector
        body_increment = apply_integer_matrix(
            incidence,
            applied_increment_counts,
        )
        repair_increment = repair_coordinate_with_forest(
            incidence,
            witness,
            applied_increment_counts,
            tree_edges,
        )
        after_state = HistoryAwareCausalMaterialState1D(
            causal=causal_outcome.after,
            applied_body_delta=_add(
                state.applied_body_delta,
                body_increment,
            ),
            history_repair=_add(
                state.history_repair,
                repair_increment,
            ),
        )
        after_applied = reconstruct_applied_history_witness(
            after_state,
            witness,
            tree_edges,
        )
        after_committed = reconstruct_committed_history_witness(
            after_state,
            witness,
            tree_edges,
        )
        applied_increment = tuple(
            after - before
            for before, after in zip(
                before_applied,
                after_applied,
                strict=True,
            )
        )
        committed_increment = tuple(
            after - before
            for before, after in zip(
                before_committed,
                after_committed,
                strict=True,
            )
        )
        expected_applied_increment = apply_integer_matrix(
            witness,
            applied_increment_counts,
        )
        if applied_increment != expected_applied_increment:
            raise AssertionError("applied-history repair failed exact Cn increment")
        if committed_increment != expected_committed_increment:
            raise AssertionError(
                "committed-history witness failed scheduler-independent CJ increment"
            )
        outcomes.append(
            HistoryAwareCausalTickOutcome1D(
                causal_outcome=causal_outcome,
                after=after_state,
                repair_increment=repair_increment,
                applied_witness_before=before_applied,
                applied_witness_after=after_applied,
                committed_witness_before=before_committed,
                committed_witness_after=after_committed,
                applied_witness_increment=applied_increment,
                committed_witness_increment=committed_increment,
            )
        )

    result = HistoryAwareCausalTickRelation1D(
        before=state,
        newly_quantized=causal_relation.newly_quantized,
        outcomes=tuple(outcomes),
    )
    if not result.committed_history_scheduler_independent:
        raise AssertionError("committed history unexpectedly depended on scheduler")
    return result


def transform_history_state_gauge(
    state: HistoryAwareCausalMaterialState1D,
    witness_matrix: Sequence[Sequence[int]],
    from_tree_edges: Sequence[int],
    to_tree_edges: Sequence[int],
) -> HistoryAwareCausalMaterialState1D:
    """Change spanning-forest repair coordinates without changing physical state."""
    incidence = contact_incidence_matrix(state.causal.network)
    witness = _witness_matrix(
        witness_matrix,
        len(state.causal.network.contacts),
    )
    transform = transform_repair_between_forests(
        incidence,
        witness,
        state.applied_body_delta,
        state.history_repair,
        from_tree_edges,
        to_tree_edges,
    )
    return HistoryAwareCausalMaterialState1D(
        causal=state.causal,
        applied_body_delta=state.applied_body_delta,
        history_repair=transform.target_repair,
    )
