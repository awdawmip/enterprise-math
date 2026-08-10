"""Exact count-level defect between APPLY->EXPIRE and EXPIRE->APPLY TTL laws.

This module isolates one contact and one tick after the material layer has already
produced whole queued impulse.  It compares two explicit world orders under a
FIFO age policy:

* ``APPLY_THEN_EXPIRE`` — use the current guarded application capacity first,
  consuming oldest tokens first, then expire any oldest survivors;
* ``EXPIRE_THEN_APPLY`` — expire the entire oldest bucket first, then apply from
  the surviving queue with the same count capacity.

Let

    Q = current whole queue total,
    x = oldest-bucket count, 0<=x<=Q,
    c = whole-impulse application capacity for this contact in the current tick.

Then

    n_A = min(c,Q),
    loss_A = max(x-n_A,0),
    Q'_A = Q-n_A-loss_A,

while

    loss_E = x,
    n_E = min(c,Q-x),
    Q'_E = Q-loss_E-n_E.

Both conserve the same whole-quantum ledger

    Q = applied + expired + final_queue,

but their allocations among those ledgers need not agree.

The current body impulse differs exactly by ``n_A-n_E``.  Even when that defect
is zero, TTL loss/history can differ: ``Q=10,x=2,c=5`` applies five units under
both laws, but APPLY->EXPIRE loses zero oldest units while EXPIRE->APPLY loses
two.

This is another operation-order boundary, analogous in role to earlier impulse-
vs-drift ordering: the order is part of the declared world law, not a numerical
implementation detail.
"""

from __future__ import annotations

from dataclasses import dataclass


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")


@dataclass(frozen=True)
class TTLOperationOrderOutcome:
    policy: str
    applied_whole_quanta: int
    expired_whole_quanta: int
    final_queue: int

    @property
    def accounted_total(self) -> int:
        return (
            self.applied_whole_quanta
            + self.expired_whole_quanta
            + self.final_queue
        )


@dataclass(frozen=True)
class TTLOperationOrderReport:
    total_queue: int
    oldest_bucket: int
    apply_capacity: int
    apply_then_expire: TTLOperationOrderOutcome
    expire_then_apply: TTLOperationOrderOutcome

    @property
    def applied_impulse_defect(self) -> int:
        return (
            self.apply_then_expire.applied_whole_quanta
            - self.expire_then_apply.applied_whole_quanta
        )

    @property
    def expiry_sink_defect(self) -> int:
        return (
            self.expire_then_apply.expired_whole_quanta
            - self.apply_then_expire.expired_whole_quanta
        )

    @property
    def final_queue_defect(self) -> int:
        return (
            self.apply_then_expire.final_queue
            - self.expire_then_apply.final_queue
        )

    @property
    def current_body_impulse_same(self) -> bool:
        return self.applied_impulse_defect == 0

    @property
    def ttl_history_same(self) -> bool:
        return (
            self.apply_then_expire.expired_whole_quanta
            == self.expire_then_apply.expired_whole_quanta
        )


def ttl_operation_order_report(
    total_queue: int,
    oldest_bucket: int,
    apply_capacity: int,
) -> TTLOperationOrderReport:
    """Return both exact FIFO count-ledger outcomes for one contact."""
    _require_nonnegative("total_queue", total_queue)
    _require_nonnegative("oldest_bucket", oldest_bucket)
    _require_nonnegative("apply_capacity", apply_capacity)
    if oldest_bucket > total_queue:
        raise ValueError("oldest_bucket cannot exceed total_queue")

    applied_first = min(apply_capacity, total_queue)
    lost_after_apply = max(oldest_bucket - applied_first, 0)
    final_after_apply = total_queue - applied_first - lost_after_apply
    apply_then_expire = TTLOperationOrderOutcome(
        policy="APPLY_THEN_EXPIRE",
        applied_whole_quanta=applied_first,
        expired_whole_quanta=lost_after_apply,
        final_queue=final_after_apply,
    )

    lost_first = oldest_bucket
    surviving = total_queue - lost_first
    applied_after_expiry = min(apply_capacity, surviving)
    final_after_expiry = surviving - applied_after_expiry
    expire_then_apply = TTLOperationOrderOutcome(
        policy="EXPIRE_THEN_APPLY",
        applied_whole_quanta=applied_after_expiry,
        expired_whole_quanta=lost_first,
        final_queue=final_after_expiry,
    )

    if apply_then_expire.accounted_total != total_queue:
        raise AssertionError("APPLY_THEN_EXPIRE lost whole-queue accounting")
    if expire_then_apply.accounted_total != total_queue:
        raise AssertionError("EXPIRE_THEN_APPLY lost whole-queue accounting")

    return TTLOperationOrderReport(
        total_queue=total_queue,
        oldest_bucket=oldest_bucket,
        apply_capacity=apply_capacity,
        apply_then_expire=apply_then_expire,
        expire_then_apply=expire_then_apply,
    )


def expiry_first_reduces_current_applied_impulse(
    total_queue: int,
    oldest_bucket: int,
    apply_capacity: int,
) -> bool:
    """Exact predicate for whether TTL expiry changes the current applied count."""
    return ttl_operation_order_report(
        total_queue,
        oldest_bucket,
        apply_capacity,
    ).applied_impulse_defect > 0
