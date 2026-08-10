"""Three exact additive history semantics for causal material ticks with TTL.

A finite-TTL material tick has, per named contact:

    J  = newly quantized whole impulse,
    n  = actually applied whole impulse,
    x  = expired/transferred whole impulse,
    Q' = Q + J - n - x.

For any integer linear contact-history readout matrix ``C``, three natural future
observables have different one-tick increments.

1. **Applied history** counts only impulses that actually acted on the body:

       Delta W_applied = C n.

   It may depend on guarded scheduler choice.

2. **Live committed history** counts applied history plus whole impulse still
   queued/available.  Queue cancellation removes scheduler allocation but expiry
   reduces the live commitment:

       Delta W_live = C (J - x).

   It is independent of how the same surviving whole budget was split between
   applied and queued, but can depend on TTL source policy / operation order via
   ``x``.

3. **Ever-quantized history** counts applied + still queued + cumulative expired
   sink.  The expiry sink cancels as well:

       Delta W_ever = C J.

   For fixed material quantization output ``J`` it is invariant under guarded
   scheduler, FIFO/LIFO token selection and apply-vs-expire ordering.

These are distinct world observables, not competing implementations of one
quantity.  A material model must state which history it reads.  The same exact
applied/queued/expired ledgers can support all three without restoring raw
subevent history.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .contact_cycle_witness_repair import apply_integer_matrix
from .material_contact_ttl_loss_ledger import TTLMaterialTickRelation1D


Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


def _witness_matrix(values: Sequence[Sequence[int]], width: int) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError("witness_matrix must contain at least one row")
    if any(len(row) != width for row in rows):
        raise ValueError("witness_matrix must match contact count")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("witness entries must be integers")
    return rows


def _nonnegative_vector(values: Sequence[int], width: int, *, name: str) -> Vector:
    result = tuple(values)
    if len(result) != width:
        raise ValueError(f"{name} must match contact count")
    for value in result:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} must contain nonnegative integers")
    return result


def _subtract(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ValueError("vector dimensions must agree")
    result = tuple(a - b for a, b in zip(left, right, strict=True))
    if any(value < 0 for value in result):
        raise ValueError("expired whole impulse cannot exceed newly/live committed increment in this helper")
    return result


@dataclass(frozen=True)
class TTLHistoryWitnessIncrement:
    applied: Vector
    live_committed: Vector
    ever_quantized: Vector


def ttl_history_witness_increment(
    witness_matrix: Sequence[Sequence[int]],
    newly_quantized: Sequence[int],
    applied: Sequence[int],
    expired: Sequence[int],
) -> TTLHistoryWitnessIncrement:
    """Return ``Cn``, ``C(J-x)`` and ``CJ`` for one declared tick branch."""
    width = len(tuple(newly_quantized))
    if width == 0:
        raise ValueError("contact vector must be nonempty")
    new = _nonnegative_vector(newly_quantized, width, name="newly_quantized")
    used = _nonnegative_vector(applied, width, name="applied")
    lost = _nonnegative_vector(expired, width, name="expired")
    witness = _witness_matrix(witness_matrix, width)

    # ``J-x`` need not be componentwise nonnegative when expired quanta came
    # from old queue rather than this tick's J.  The live-commitment increment
    # is therefore an integer vector, not a fresh whole-delivery vector.
    live_delta = tuple(
        new_value - lost_value
        for new_value, lost_value in zip(new, lost, strict=True)
    )
    return TTLHistoryWitnessIncrement(
        applied=apply_integer_matrix(witness, used),
        live_committed=apply_integer_matrix(witness, live_delta),
        ever_quantized=apply_integer_matrix(witness, new),
    )


@dataclass(frozen=True)
class TTLHistoryRelationReport:
    applied_values: tuple[Vector, ...]
    live_committed_values: tuple[Vector, ...]
    ever_quantized_values: tuple[Vector, ...]

    @property
    def applied_scheduler_independent(self) -> bool:
        return len(self.applied_values) <= 1

    @property
    def live_committed_policy_independent(self) -> bool:
        return len(self.live_committed_values) <= 1

    @property
    def ever_quantized_policy_independent(self) -> bool:
        return len(self.ever_quantized_values) <= 1


def ttl_history_relation_report(
    relation: TTLMaterialTickRelation1D,
    witness_matrix: Sequence[Sequence[int]],
) -> TTLHistoryRelationReport:
    """Project every causal/TTL terminal branch to the three history semantics."""
    if not isinstance(relation, TTLMaterialTickRelation1D):
        raise TypeError("relation must be TTLMaterialTickRelation1D")
    width = len(relation.newly_quantized)
    witness = _witness_matrix(witness_matrix, width)
    increments = tuple(
        ttl_history_witness_increment(
            witness,
            relation.newly_quantized,
            outcome.applied_impulse_vector,
            outcome.expired_whole_vector,
        )
        for outcome in relation.outcomes
    )
    report = TTLHistoryRelationReport(
        applied_values=tuple(sorted({item.applied for item in increments})),
        live_committed_values=tuple(
            sorted({item.live_committed for item in increments})
        ),
        ever_quantized_values=tuple(
            sorted({item.ever_quantized for item in increments})
        ),
    )
    if len(report.ever_quantized_values) != 1:
        raise AssertionError("ever-quantized history must depend only on fixed J")
    return report
