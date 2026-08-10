"""Linear future-observable invariance on the applied/queued/expired ledger.

After contact-local material quantization, every whole-contact quantum is in one
of three exact compartments for a declared contact channel:

    P = already applied to bodies,
    Q = still in the causal whole-quantum queue,
    X = expired/transferred to an explicit sink.

The quantized whole total is

    H = P + Q + X.

Two basic policy operations only redistribute this fixed total:

* guarded application of ``d`` queued units:

      (P,Q,X) -> (P+d,Q-d,X),

* expiry/transfer of ``d`` queued units:

      (P,Q,X) -> (P,Q-d,X+d).

For a scalar linear compartment readout

    L(P,Q,X) = u*P + v*Q + w*X,

invariance is exact:

* scheduler/application redistribution invariant iff ``u=v``;
* expiry redistribution invariant iff ``v=w``;
* invariant under both elementary redistribution families iff ``u=v=w``.

Thus the three material-history semantics developed in the TTL bridge are the
canonical simple examples:

* applied history ``(1,0,0)`` — sensitive to both redistribution families;
* live commitment ``(1,1,0)`` — scheduler-invariant, expiry-sensitive;
* ever-quantized history ``(1,1,1)`` — invariant under every redistribution
  preserving total quantized whole count.

The same statement extends contactwise to integer matrix readouts.  Let
``C_P,C_Q,C_X`` map the contact compartment vectors to one declared witness
space.  If arbitrary contacts may transfer independently, scheduler invariance
for every legal redistribution direction is equivalent to ``C_P=C_Q``; expiry
invariance is equivalent to ``C_Q=C_X``; full redistribution invariance is
``C_P=C_Q=C_X``.

For a restricted policy relation, these equalities can weaken to the ordinary
kernel condition on the actually generated redistribution lattice.  That is the
same P023 principle already used for scheduler terminal differences: a future
observable is deterministic precisely when it kills the hidden difference
lattice of the declared policy family.

This module is bookkeeping linear algebra, not a constitutive law.  Its value is
an exact reusable test for deciding whether a proposed material-history
observable depends on causal scheduling, TTL transfer, neither, or both.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


Vector3 = tuple[int, int, int]
Matrix = tuple[tuple[int, ...], ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _nonnegative_ledger(values: Sequence[int]) -> Vector3:
    result = tuple(values)
    if len(result) != 3:
        raise ValueError("ledger must be (applied, queued, expired)")
    for value in result:
        _require_int("ledger entry", value)
        if value < 0:
            raise ValueError("ledger entries must be nonnegative")
    return result  # type: ignore[return-value]


def whole_ledger_total(ledger: Sequence[int]) -> int:
    return sum(_nonnegative_ledger(ledger))


def apply_queued_whole(
    ledger: Sequence[int],
    amount: int,
) -> Vector3:
    """Move whole quanta from queued to applied."""
    applied, queued, expired = _nonnegative_ledger(ledger)
    _require_int("amount", amount)
    if amount < 0 or amount > queued:
        raise ValueError("application amount must lie in 0..queued")
    result: Vector3 = (applied + amount, queued - amount, expired)
    if whole_ledger_total(result) != applied + queued + expired:
        raise AssertionError("application redistribution changed whole total")
    return result


def expire_queued_whole(
    ledger: Sequence[int],
    amount: int,
) -> Vector3:
    """Move whole quanta from queued to the explicit expired/transfer sink."""
    applied, queued, expired = _nonnegative_ledger(ledger)
    _require_int("amount", amount)
    if amount < 0 or amount > queued:
        raise ValueError("expiry amount must lie in 0..queued")
    result: Vector3 = (applied, queued - amount, expired + amount)
    if whole_ledger_total(result) != applied + queued + expired:
        raise AssertionError("expiry redistribution changed whole total")
    return result


def scalar_ledger_readout(
    ledger: Sequence[int],
    weights: Sequence[int],
) -> int:
    values = _nonnegative_ledger(ledger)
    coefficients = tuple(weights)
    if len(coefficients) != 3:
        raise ValueError("weights must be (applied, queued, expired)")
    for value in coefficients:
        _require_int("weight", value)
    return sum(a * b for a, b in zip(values, coefficients, strict=True))


def scalar_scheduler_invariant(weights: Sequence[int]) -> bool:
    coefficients = tuple(weights)
    if len(coefficients) != 3:
        raise ValueError("weights must be (applied, queued, expired)")
    for value in coefficients:
        _require_int("weight", value)
    return coefficients[0] == coefficients[1]


def scalar_expiry_invariant(weights: Sequence[int]) -> bool:
    coefficients = tuple(weights)
    if len(coefficients) != 3:
        raise ValueError("weights must be (applied, queued, expired)")
    for value in coefficients:
        _require_int("weight", value)
    return coefficients[1] == coefficients[2]


def scalar_full_redistribution_invariant(weights: Sequence[int]) -> bool:
    coefficients = tuple(weights)
    if len(coefficients) != 3:
        raise ValueError("weights must be (applied, queued, expired)")
    for value in coefficients:
        _require_int("weight", value)
    return coefficients[0] == coefficients[1] == coefficients[2]


def _matrix(values: Sequence[Sequence[int]], width: int) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError("matrix must contain at least one row")
    if any(len(row) != width for row in rows):
        raise ValueError("matrix width mismatch")
    for row in rows:
        for value in row:
            _require_int("matrix entry", value)
    return rows


def contact_matrix_scheduler_invariant(
    applied_matrix: Sequence[Sequence[int]],
    queued_matrix: Sequence[Sequence[int]],
) -> bool:
    left_rows = tuple(tuple(row) for row in applied_matrix)
    if not left_rows:
        raise ValueError("matrix must contain at least one row")
    width = len(left_rows[0])
    left = _matrix(left_rows, width)
    right = _matrix(queued_matrix, width)
    return left == right


def contact_matrix_expiry_invariant(
    queued_matrix: Sequence[Sequence[int]],
    expired_matrix: Sequence[Sequence[int]],
) -> bool:
    left_rows = tuple(tuple(row) for row in queued_matrix)
    if not left_rows:
        raise ValueError("matrix must contain at least one row")
    width = len(left_rows[0])
    left = _matrix(left_rows, width)
    right = _matrix(expired_matrix, width)
    return left == right


def contact_matrix_full_redistribution_invariant(
    applied_matrix: Sequence[Sequence[int]],
    queued_matrix: Sequence[Sequence[int]],
    expired_matrix: Sequence[Sequence[int]],
) -> bool:
    left_rows = tuple(tuple(row) for row in applied_matrix)
    if not left_rows:
        raise ValueError("matrix must contain at least one row")
    width = len(left_rows[0])
    applied = _matrix(left_rows, width)
    queued = _matrix(queued_matrix, width)
    expired = _matrix(expired_matrix, width)
    return applied == queued == expired


@dataclass(frozen=True)
class MaterialLedgerObservableClass:
    scheduler_invariant: bool
    expiry_invariant: bool
    full_redistribution_invariant: bool


def classify_scalar_ledger_observable(
    weights: Sequence[int],
) -> MaterialLedgerObservableClass:
    return MaterialLedgerObservableClass(
        scheduler_invariant=scalar_scheduler_invariant(weights),
        expiry_invariant=scalar_expiry_invariant(weights),
        full_redistribution_invariant=scalar_full_redistribution_invariant(weights),
    )
