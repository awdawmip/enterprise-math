"""One-way event classification for future model-agreement filtrations.

Future language only accumulates constraints, so agreement sets satisfy

    A_(h+1) subseteq A_h.

For total-affine integer models, each nonempty exact agreement set is an affine
coset of a saturated kernel sublattice.  Therefore an exact proper nonempty
refinement must lower the free kernel rank; two nested nonempty cosets with the
same saturated kernel rank are equal.  The other exact event is affine IMAGE
inconsistency, which makes the agreement set empty forever.

Modulo M the finite agreement set is still nested, but there is one additional
refinement mode: with unchanged rational rank, the modular Smith kernel can
shrink because nonunit invariant factors are purified at the chosen coefficient
precision.

This module classifies adjacent horizon steps as:

* UNCHANGED;
* FREE_RANK_SHRINK;
* MODULAR_TORSION_SHRINK (modular only, same rational rank);
* EMPTY_COLLAPSE;
* EMPTY_ABSORBED.

The labels diagnose where precision increased.  They are not a claim that every
world must exhibit the events in one fixed order; only EMPTY is absorbing.
"""

from __future__ import annotations

from dataclasses import dataclass

from .integer_dynamic_affine_agreement_horizon import (
    AffineAgreementHorizonReport,
    AffineAgreementHorizonStep,
)


UNCHANGED = "UNCHANGED"
FREE_RANK_SHRINK = "FREE_RANK_SHRINK"
MODULAR_TORSION_SHRINK = "MODULAR_TORSION_SHRINK"
EMPTY_COLLAPSE = "EMPTY_COLLAPSE"
EMPTY_ABSORBED = "EMPTY_ABSORBED"


@dataclass(frozen=True)
class AgreementFiltrationEvent:
    from_horizon: int
    to_horizon: int
    event: str
    previous_solvable: bool
    next_solvable: bool
    previous_linear_rank: int
    next_linear_rank: int
    previous_modular_count: int | None
    next_modular_count: int | None

    @property
    def is_strict_refinement(self) -> bool:
        return self.event in {
            FREE_RANK_SHRINK,
            MODULAR_TORSION_SHRINK,
            EMPTY_COLLAPSE,
        }


def classify_agreement_transition(
    report: AffineAgreementHorizonReport,
    previous: AffineAgreementHorizonStep,
    nxt: AffineAgreementHorizonStep,
) -> AgreementFiltrationEvent:
    if nxt.horizon != previous.horizon + 1:
        raise ValueError("agreement transition must compare adjacent horizons")

    if not previous.solvable:
        if nxt.solvable:
            raise AssertionError("empty agreement set resurrected under added future constraints")
        event = EMPTY_ABSORBED
    elif not nxt.solvable:
        event = EMPTY_COLLAPSE
    else:
        if nxt.linear_rank < previous.linear_rank:
            raise AssertionError("future constraints lowered linear difference rank")

        if report.modulus is None:
            previous_free = previous.exact_agreement_free_rank
            next_free = nxt.exact_agreement_free_rank
            if previous_free is None or next_free is None:
                raise AssertionError("solvable exact steps lost agreement free rank")
            if next_free > previous_free:
                raise AssertionError("exact agreement free rank increased under future refinement")
            if next_free < previous_free:
                event = FREE_RANK_SHRINK
            else:
                if nxt.linear_rank != previous.linear_rank:
                    raise AssertionError("exact rank changed without free-rank change")
                event = UNCHANGED
        else:
            previous_count = previous.modular_agreement_state_count
            next_count = nxt.modular_agreement_state_count
            if previous_count is None or next_count is None:
                raise AssertionError("modular agreement report lost finite state counts")
            if next_count > previous_count:
                raise AssertionError("modular agreement count increased under future refinement")
            if nxt.linear_rank > previous.linear_rank:
                event = FREE_RANK_SHRINK
            elif next_count < previous_count:
                event = MODULAR_TORSION_SHRINK
            else:
                event = UNCHANGED

    return AgreementFiltrationEvent(
        from_horizon=previous.horizon,
        to_horizon=nxt.horizon,
        event=event,
        previous_solvable=previous.solvable,
        next_solvable=nxt.solvable,
        previous_linear_rank=previous.linear_rank,
        next_linear_rank=nxt.linear_rank,
        previous_modular_count=previous.modular_agreement_state_count,
        next_modular_count=nxt.modular_agreement_state_count,
    )


def agreement_filtration_events(
    report: AffineAgreementHorizonReport,
) -> tuple[AgreementFiltrationEvent, ...]:
    if not isinstance(report, AffineAgreementHorizonReport):
        raise TypeError("report must be AffineAgreementHorizonReport")
    return tuple(
        classify_agreement_transition(report, previous, nxt)
        for previous, nxt in zip(report.steps, report.steps[1:])
    )
