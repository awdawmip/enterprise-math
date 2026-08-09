"""Minimal declared material-to-kinematic coupling for stacked E001.

This module deliberately introduces one *engineering policy*, not a physical law.
Given a non-negative incoming motion budget ``B`` and one material response sample
``r`` on amplitude scale ``A``, define the returned budget by

    return = floor(B*r/A).

The multiplication remainder is retained explicitly.  The complementary
``unreturned_budget = B-return`` is only a finite bookkeeping quantity; it is
not automatically heat, energy loss, plastic work, or any other physical unit.

If the material sample/amplitude pair is refined together by a common integer
factor, the returned budget is exactly unchanged.  Refining the motion budget
itself produces one explicit bounded carry defect.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_hysteresis import MaterialHistoryState


@dataclass(frozen=True)
class ReboundBudget:
    """Exact integer split of one incoming motion budget by one material sample."""

    incoming_budget: int
    response_sample: int
    amplitude: int
    returned_budget: int
    unreturned_budget: int
    product_remainder: int


@dataclass(frozen=True)
class ReboundBudgetScaleReport:
    """Transport diagnostics under material-scale or motion-budget refinement."""

    base: ReboundBudget
    material_refinement: int
    material_refined: ReboundBudget
    motion_refinement: int
    motion_refined: ReboundBudget
    transported_motion_return: int
    motion_refinement_defect: int
    expected_motion_defect_from_remainder: int


def _validate(incoming_budget: int, response_sample: int, amplitude: int) -> None:
    if (
        isinstance(incoming_budget, bool)
        or not isinstance(incoming_budget, int)
        or incoming_budget < 0
    ):
        raise ValueError("incoming_budget must be a non-negative integer")
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude <= 0:
        raise ValueError("amplitude must be a positive integer")
    if (
        isinstance(response_sample, bool)
        or not isinstance(response_sample, int)
        or not 0 <= response_sample <= amplitude
    ):
        raise ValueError("response_sample must lie in 0..amplitude")


def rebound_budget(
    incoming_budget: int,
    response_sample: int,
    amplitude: int,
) -> ReboundBudget:
    """Split one integer motion budget by an explicit finite material ratio."""
    _validate(incoming_budget, response_sample, amplitude)
    product = incoming_budget * response_sample
    returned, remainder = divmod(product, amplitude)
    unreturned = incoming_budget - returned
    if not 0 <= returned <= incoming_budget:
        raise AssertionError("returned budget escaped incoming budget")
    if product != amplitude * returned + remainder:
        raise AssertionError("rebound budget failed exact quotient/remainder accounting")
    return ReboundBudget(
        incoming_budget=incoming_budget,
        response_sample=response_sample,
        amplitude=amplitude,
        returned_budget=returned,
        unreturned_budget=unreturned,
        product_remainder=remainder,
    )


def rebound_budget_from_material_state(
    incoming_budget: int,
    state: MaterialHistoryState,
    amplitude: int,
) -> ReboundBudget:
    """Couple one already-selected branch-aware material state to motion budget."""
    return rebound_budget(incoming_budget, state.response_sample, amplitude)


def rebound_budget_scale_report(
    incoming_budget: int,
    response_sample: int,
    amplitude: int,
    material_refinement: int,
    motion_refinement: int,
) -> ReboundBudgetScaleReport:
    """Verify exact material-scale invariance and motion-scale carry behavior."""
    for name, factor in (
        ("material_refinement", material_refinement),
        ("motion_refinement", motion_refinement),
    ):
        if isinstance(factor, bool) or not isinstance(factor, int) or factor <= 0:
            raise ValueError(f"{name} must be a positive integer")

    base = rebound_budget(incoming_budget, response_sample, amplitude)
    material_refined = rebound_budget(
        incoming_budget,
        material_refinement * response_sample,
        material_refinement * amplitude,
    )
    if material_refined.returned_budget != base.returned_budget:
        raise AssertionError("joint material refinement changed returned budget")

    motion_refined = rebound_budget(
        motion_refinement * incoming_budget,
        response_sample,
        amplitude,
    )
    transported = motion_refinement * base.returned_budget
    defect = motion_refined.returned_budget - transported
    expected = motion_refinement * base.product_remainder // amplitude
    if defect != expected:
        raise AssertionError("motion refinement defect disagrees with base remainder")
    if not 0 <= defect < motion_refinement:
        raise AssertionError("motion refinement defect escaped its carry range")

    return ReboundBudgetScaleReport(
        base=base,
        material_refinement=material_refinement,
        material_refined=material_refined,
        motion_refinement=motion_refinement,
        motion_refined=motion_refined,
        transported_motion_return=transported,
        motion_refinement_defect=defect,
        expected_motion_defect_from_remainder=expected,
    )
