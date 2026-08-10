"""Age/source precision for already-quantized whole-contact queues.

The causal material tick can aggregate old whole-contact queue ``Q_old`` and newly
quantized whole impulse ``J_new`` into one count when all whole quanta on the
same named contact are future-exchangeable.  This module pressure-tests the
first explicit failure of that quotient: a finite waiting-time / TTL law.

Represent one contact queue at a tick boundary by nonnegative age buckets

    q = (q_0,...,q_(D-1)),

where ``q_a`` counts unapplied whole quanta of age ``a`` and ``D`` is the finite
retention depth.  A pure aging step with ``new_quanta=J`` expires the oldest
bucket and shifts the rest:

    (q_0,...,q_(D-1))
      -> (J,q_0,...,q_(D-2)),

    expired = q_(D-1).

Hence total queue evolves as

    Q' = Q + J - q_(D-1).

Two queues with the same current total but different oldest bucket therefore
have different next total.  Once TTL/expiry belongs to the world law, aggregate
whole queue count is not a future-safe state even if the future observes only
total queue size.

The finite-horizon precision is exact.  With no new arrivals and no consumption,
let ``T_k`` be total queue after ``k`` aging steps.  For horizon ``h<=D-1``, the
trace ``T_0,...,T_h`` is equivalent to the key

    (sum_(a=0)^(D-h-1) q_a,
     q_(D-h),...,q_(D-1)).

Each extra horizon reveals one older bucket while all younger buckets remain one
aggregate.  At ``h=D-1`` the full age histogram is recovered.

Inside a fixed current-total fiber ``sum q=N``, the exact number of predictive
age classes is therefore

    C(N+h,h)                   for 0<=h<=D-1,

and remains ``C(N+D-1,D-1)`` for all later horizons.  This is the weak-
composition count of ``N`` into the ``h+1`` future-visible bins.

A second boundary concerns same-tick consumption.  If new quanta join age zero
and a declared count ``n`` is consumed before aging, FIFO and LIFO apply exactly
the same number of physical whole impulses but can leave different age
histograms.  Under finite TTL those different histograms can produce different
future queue totals.  Thus a source/age selector is a world-law choice whenever
age remains future-visible; it is safely quotiented only for an age-blind future
language.

For a linear source/age readout ``c.q``, aggregation to total ``Q=1.q`` is safe
exactly when ``c`` is constant across age buckets.  This is the same kernel
criterion used elsewhere in the project: ``ker(1^T) subseteq ker(c)``.

Finite FIFO/LIFO queues, shift registers, TTL expiry and weak compositions are
standard.  The E001/P023 value is the exact predictive-state boundary for the
whole-quantum causal queue introduced by the material contact tick.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb
from typing import Sequence


Vector = tuple[int, ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_nonnegative(name: str, value: int) -> None:
    _require_int(name, value)
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")


@dataclass(frozen=True)
class ContactWholeQueueAgeState:
    """One contact's finite-TTL whole-quantum age histogram."""

    buckets: Vector

    def __post_init__(self) -> None:
        if not self.buckets:
            raise ValueError("age queue must contain at least one bucket")
        for value in self.buckets:
            _require_nonnegative("age bucket", value)

    @property
    def retention_depth(self) -> int:
        return len(self.buckets)

    @property
    def total(self) -> int:
        return sum(self.buckets)

    @property
    def oldest(self) -> int:
        return self.buckets[-1]


@dataclass(frozen=True)
class ContactWholeQueueAgeStep:
    before: ContactWholeQueueAgeState
    new_quanta: int
    expired_quanta: int
    after: ContactWholeQueueAgeState


def age_queue_step(
    state: ContactWholeQueueAgeState,
    new_quanta: int = 0,
) -> ContactWholeQueueAgeStep:
    """Expire oldest whole quanta, age survivors, and insert new age-zero quanta."""
    if not isinstance(state, ContactWholeQueueAgeState):
        raise TypeError("state must be ContactWholeQueueAgeState")
    _require_nonnegative("new_quanta", new_quanta)
    expired = state.oldest
    after = ContactWholeQueueAgeState(
        (new_quanta, *state.buckets[:-1])
    )
    if after.total != state.total + new_quanta - expired:
        raise AssertionError("TTL queue total ledger failed")
    return ContactWholeQueueAgeStep(
        before=state,
        new_quanta=new_quanta,
        expired_quanta=expired,
        after=after,
    )


def pure_aging_total_trace(
    state: ContactWholeQueueAgeState,
    horizon: int,
) -> tuple[int, ...]:
    """Current/future total queue trace with no arrivals and no consumption."""
    if not isinstance(state, ContactWholeQueueAgeState):
        raise TypeError("state must be ContactWholeQueueAgeState")
    _require_nonnegative("horizon", horizon)
    current = state
    totals = [current.total]
    for _ in range(horizon):
        current = age_queue_step(current, 0).after
        totals.append(current.total)
    return tuple(totals)


def age_total_future_key(
    state: ContactWholeQueueAgeState,
    horizon: int,
) -> Vector:
    """Exact minimal coordinate for pure-aging total observations through horizon."""
    if not isinstance(state, ContactWholeQueueAgeState):
        raise TypeError("state must be ContactWholeQueueAgeState")
    _require_nonnegative("horizon", horizon)
    effective = min(horizon, state.retention_depth - 1)
    young_count = state.retention_depth - effective
    return (
        sum(state.buckets[:young_count]),
        *state.buckets[young_count:],
    )


def age_key_matches_total_trace(
    left: ContactWholeQueueAgeState,
    right: ContactWholeQueueAgeState,
    horizon: int,
) -> bool:
    """Verify key equality iff the declared total-queue future traces agree."""
    if left.retention_depth != right.retention_depth:
        raise ValueError("age queues must have the same retention depth")
    key_equal = age_total_future_key(left, horizon) == age_total_future_key(
        right, horizon
    )
    trace_equal = pure_aging_total_trace(left, horizon) == pure_aging_total_trace(
        right, horizon
    )
    if key_equal != trace_equal:
        raise AssertionError("age future key disagreed with total trace")
    return key_equal


def fixed_total_age_class_count(
    total_quanta: int,
    retention_depth: int,
    horizon: int,
) -> int:
    """Exact number of predictive age classes inside one fixed-total queue fiber."""
    _require_nonnegative("total_quanta", total_quanta)
    _require_int("retention_depth", retention_depth)
    _require_nonnegative("horizon", horizon)
    if retention_depth <= 0:
        raise ValueError("retention_depth must be positive")
    effective = min(horizon, retention_depth - 1)
    return comb(total_quanta + effective, effective)


def linear_age_readout_descends_to_total(weights: Sequence[int]) -> bool:
    """Whether ``weights.q`` depends only on ``sum(q)`` for all integer queues."""
    values = tuple(weights)
    if not values:
        raise ValueError("weights must be nonempty")
    for value in values:
        _require_int("weight", value)
    return len(set(values)) == 1


def _consume_from_bucket_order(
    buckets: list[int],
    count: int,
    order: Sequence[int],
) -> None:
    remaining = count
    for index in order:
        if remaining == 0:
            break
        take = min(remaining, buckets[index])
        buckets[index] -= take
        remaining -= take
    if remaining:
        raise AssertionError("consumption order failed despite sufficient total queue")


@dataclass(frozen=True)
class ContactWholeQueueConsumeAgeStep:
    before: ContactWholeQueueAgeState
    new_quanta: int
    applied_quanta: int
    policy: str
    pre_age_survivors: ContactWholeQueueAgeState
    expired_quanta: int
    after: ContactWholeQueueAgeState


def consume_then_age_queue(
    state: ContactWholeQueueAgeState,
    new_quanta: int,
    applied_quanta: int,
    *,
    policy: str,
) -> ContactWholeQueueConsumeAgeStep:
    """Insert new age-zero quanta, consume FIFO/LIFO, then age and expire survivors."""
    if not isinstance(state, ContactWholeQueueAgeState):
        raise TypeError("state must be ContactWholeQueueAgeState")
    _require_nonnegative("new_quanta", new_quanta)
    _require_nonnegative("applied_quanta", applied_quanta)
    available = state.total + new_quanta
    if applied_quanta > available:
        raise ValueError("cannot apply more whole quanta than are available")
    if policy not in ("FIFO", "LIFO"):
        raise ValueError("policy must be FIFO or LIFO")

    buckets = list(state.buckets)
    buckets[0] += new_quanta
    if policy == "FIFO":
        order = tuple(range(len(buckets) - 1, -1, -1))
    else:
        order = tuple(range(len(buckets)))
    _consume_from_bucket_order(buckets, applied_quanta, order)
    survivors = ContactWholeQueueAgeState(tuple(buckets))
    aged = age_queue_step(survivors, 0)
    if aged.after.total != available - applied_quanta - aged.expired_quanta:
        raise AssertionError("consume/age total queue ledger failed")
    return ContactWholeQueueConsumeAgeStep(
        before=state,
        new_quanta=new_quanta,
        applied_quanta=applied_quanta,
        policy=policy,
        pre_age_survivors=survivors,
        expired_quanta=aged.expired_quanta,
        after=aged.after,
    )


def fifo_lifo_future_total_diverges(
    state: ContactWholeQueueAgeState,
    new_quanta: int,
    applied_quanta: int,
) -> bool:
    """Whether identical current applied count has different next total under FIFO/LIFO."""
    fifo = consume_then_age_queue(
        state,
        new_quanta,
        applied_quanta,
        policy="FIFO",
    )
    lifo = consume_then_age_queue(
        state,
        new_quanta,
        applied_quanta,
        policy="LIFO",
    )
    return fifo.after.total != lifo.after.total
