"""P023 future-language quotient of hidden balanced-cycle material histories.

The balanced-cycle bridge gives ``2s+1`` first-cycle contact histories that are
identical at body level.  A toy contact-reservoir law then makes one further
reload respond with the unique componentwise complement history.  This module
does not implement another minimizer; it compiles that finite material process
into canonical P023 ``stable_family_partition`` and compares three declared
future observation languages.

States are split into two protocol stages for each hidden shift ``t``:

    PRE(t)  : after the first cycle, before the reservoir-aware reload;
    POST(t) : after the reload has delivered the unique response j(-t).

The single total operation ``RELOAD`` maps ``PRE(t)->POST(t)`` and keeps every
``POST(t)`` absorbing.

Observation languages:

* BODY_ONLY: every represented state exposes only the common zero body state;
* AGGREGATE: POST additionally exposes only total second impulse ``4s``;
* CONTACT_LOCAL: POST exposes the full unique second response vector ``j(-t)``.

Consequently P023 returns:

* one stable class for all PRE histories under BODY_ONLY;
* one stable PRE class under AGGREGATE as well, because all totals agree;
* exactly ``2s+1`` stable PRE classes under CONTACT_LOCAL, because one RELOAD
  reveals an injective contact-local response.

This is an E001 specialization of generic future-language quotient/minimization,
whose ownership remains P023.  The reservoir law is a declared toy future
operation, not a physical damage model.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_cycle_history_precision_bridge import (
    balanced_four_cycle_minimum_relation,
)
from .material_cycle_reservoir_future import (
    balanced_cycle_history_shift,
    balanced_cycle_reservoir_future_report,
)
from .operation_quotient import class_count, stable_family_partition

BODY_ONLY = "BODY_ONLY"
AGGREGATE = "AGGREGATE"
CONTACT_LOCAL = "CONTACT_LOCAL"
CycleQuotientState = tuple[str, int]


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _language(value: str) -> str:
    if value not in (BODY_ONLY, AGGREGATE, CONTACT_LOCAL):
        raise ValueError("language must be BODY_ONLY, AGGREGATE, or CONTACT_LOCAL")
    return value


@dataclass(frozen=True)
class BalancedCycleP023HistoryReport:
    denominator: int
    language: str
    hidden_history_count: int
    domain: tuple[CycleQuotientState, ...]
    reload_operation: dict[CycleQuotientState, CycleQuotientState]
    initial_observation: dict[CycleQuotientState, tuple[object, ...]]
    stable_partition: dict[CycleQuotientState, int]
    stable_total_class_count: int
    stable_pre_history_class_count: int
    stable_post_history_class_count: int

    @property
    def all_hidden_histories_merge(self) -> bool:
        return self.stable_pre_history_class_count == 1

    @property
    def all_hidden_histories_future_distinguished(self) -> bool:
        return self.stable_pre_history_class_count == self.hidden_history_count


def balanced_cycle_p023_history_report(
    denominator: int,
    language: str,
) -> BalancedCycleP023HistoryReport:
    """Compile the one-reload material protocol into the canonical P023 quotient."""
    _positive("denominator", denominator)
    declared = _language(language)
    relation = balanced_four_cycle_minimum_relation(denominator)
    shifts = tuple(
        balanced_cycle_history_shift(denominator, history)
        for history in relation
    )
    pre_states = tuple(("PRE", shift) for shift in shifts)
    post_states = tuple(("POST", shift) for shift in shifts)
    domain = pre_states + post_states
    reload_operation: dict[CycleQuotientState, CycleQuotientState] = {}
    observation: dict[CycleQuotientState, tuple[object, ...]] = {}

    for history, shift in zip(relation, shifts):
        pre = ("PRE", shift)
        post = ("POST", shift)
        reload_operation[pre] = post
        reload_operation[post] = post
        future = balanced_cycle_reservoir_future_report(
            denominator,
            history,
        )
        if declared == BODY_ONLY:
            observation[pre] = ("BODY_ZERO",)
            observation[post] = ("BODY_ZERO",)
        elif declared == AGGREGATE:
            observation[pre] = ("BODY_ZERO", "AGGREGATE_PENDING", 4 * denominator)
            observation[post] = (
                "BODY_ZERO",
                "AGGREGATE_RELOAD",
                sum(future.next_unique_response),
            )
        else:
            observation[pre] = ("BODY_ZERO", "CONTACT_RELOAD_PENDING")
            observation[post] = (
                "BODY_ZERO",
                "CONTACT_RELOAD_RESPONSE",
                future.next_unique_response,
            )

    stable = stable_family_partition(
        domain,
        {"RELOAD": reload_operation},
        observation,
    )
    pre_count = len({stable[state] for state in pre_states})
    post_count = len({stable[state] for state in post_states})
    hidden = len(relation)
    if declared in (BODY_ONLY, AGGREGATE) and pre_count != 1:
        raise AssertionError("coarse future language failed to merge hidden cycle histories")
    if declared == CONTACT_LOCAL and pre_count != hidden:
        raise AssertionError("contact-local reload failed to recover all hidden histories")
    return BalancedCycleP023HistoryReport(
        denominator=denominator,
        language=declared,
        hidden_history_count=hidden,
        domain=domain,
        reload_operation=reload_operation,
        initial_observation=observation,
        stable_partition=stable,
        stable_total_class_count=class_count(stable),
        stable_pre_history_class_count=pre_count,
        stable_post_history_class_count=post_count,
    )
