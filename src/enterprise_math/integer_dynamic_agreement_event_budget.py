"""Strict agreement-event budgets for exact and modular future filtrations.

Agreement sets shrink monotonically with future horizon, but unchanged horizons
can occur before a later refinement.  Therefore strict-change counts and the
horizon of the final change are different resources.

### Exact integer case

Every nonempty exact agreement set is an affine coset of a saturated kernel
sublattice.  A proper nonempty nested refinement must lower the free kernel rank.
Thus the number of nonempty strict refinements is at most the initial agreement
free rank (hence at most the state dimension).  There can be at most one further
EMPTY_COLLAPSE event.

### Fixed modulus M

Every nonempty modular agreement set is a coset of a subgroup of the finite state
torus.  Nested nonempty cosets are either equal or have subgroup cardinalities in
a proper-divisibility relation.  Therefore each strict nonempty refinement lowers
the agreement-state count to a proper divisor.  Starting from N states, the
number of strict nonempty refinements is at most ``Omega(N)``.  Again there can
be at most one subsequent EMPTY_COLLAPSE.

These are event-count bounds only.  They do not bound how many UNCHANGED horizon
steps may occur before a new future word creates the next strict event; full
future-module closure remains the timing certificate.
"""

from __future__ import annotations

from dataclasses import dataclass

from .integer_action_language_observability import prime_factor_multiplicity
from .integer_dynamic_affine_agreement_horizon import AffineAgreementHorizonReport
from .integer_dynamic_agreement_events import (
    EMPTY_COLLAPSE,
    FREE_RANK_SHRINK,
    MODULAR_TORSION_SHRINK,
    agreement_filtration_events,
)


@dataclass(frozen=True)
class AgreementEventBudgetReport:
    modulus: int | None
    initial_solvable: bool
    initial_exact_free_rank: int | None
    initial_modular_state_count: int | None
    strict_nonempty_event_bound: int
    empty_collapse_bound: int
    observed_strict_nonempty_events: int
    observed_empty_collapses: int
    last_observed_strict_event_horizon: int | None

    @property
    def within_bound(self) -> bool:
        return (
            self.observed_strict_nonempty_events <= self.strict_nonempty_event_bound
            and self.observed_empty_collapses <= self.empty_collapse_bound
        )


def agreement_event_budget_report(
    report: AffineAgreementHorizonReport,
) -> AgreementEventBudgetReport:
    if not isinstance(report, AffineAgreementHorizonReport):
        raise TypeError("report must be AffineAgreementHorizonReport")
    if not report.steps:
        raise ValueError("agreement report must contain horizon zero")
    initial = report.steps[0]
    events = agreement_filtration_events(report)
    strict_nonempty = tuple(
        event
        for event in events
        if event.event in {FREE_RANK_SHRINK, MODULAR_TORSION_SHRINK}
    )
    empty = tuple(event for event in events if event.event == EMPTY_COLLAPSE)

    if report.modulus is None:
        if not initial.solvable:
            bound = 0
            initial_free = None
        else:
            if initial.exact_agreement_free_rank is None:
                raise AssertionError("solvable exact initial state lost free rank")
            initial_free = initial.exact_agreement_free_rank
            bound = initial_free
        initial_count = None
    else:
        initial_free = initial.exact_agreement_free_rank
        initial_count = initial.modular_agreement_state_count
        if initial_count is None:
            raise AssertionError("modular report lost initial state count")
        bound = prime_factor_multiplicity(initial_count) if initial_count > 0 else 0

    result = AgreementEventBudgetReport(
        modulus=report.modulus,
        initial_solvable=initial.solvable,
        initial_exact_free_rank=initial_free,
        initial_modular_state_count=initial_count,
        strict_nonempty_event_bound=bound,
        empty_collapse_bound=1 if initial.solvable else 0,
        observed_strict_nonempty_events=len(strict_nonempty),
        observed_empty_collapses=len(empty),
        last_observed_strict_event_horizon=(
            max(event.to_horizon for event in events if event.is_strict_refinement)
            if any(event.is_strict_refinement for event in events)
            else None
        ),
    )
    if not result.within_bound:
        raise AssertionError("agreement filtration exceeded strict-event budget")
    return result
