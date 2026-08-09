"""Finite hysteresis-cycle diagnostics from actually visited material states.

A pointwise difference between two complete branch tables is not automatically
the same quantity as a realized loading/return history.  A discrete schedule may
visit the peak only on LOADING and start RETURNING at the next lower deformation
index, so an unvisited return-branch peak must not be silently counted as part
of the realized loop.

This module pairs only deformation indices that were actually visited on both
LOADING and RETURNING branches.  The resulting sums are combinatorial history
diagnostics, not physical energy or work without an additional unit-bearing law.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_hysteresis import LOADING, RETURNING, MaterialHistoryState


@dataclass(frozen=True)
class RevisitedDeformationGap:
    """Loading/return samples actually observed at the same deformation index."""

    deformation_index: int
    loading_sample: int
    returning_sample: int
    signed_gap: int
    absolute_gap: int
    loading_excess: int
    returning_excess: int


@dataclass(frozen=True)
class MaterialCycleDiagnostics:
    """Finite path diagnostics for one material history trace."""

    state_count: int
    start_index: int
    end_index: int
    peak_index: int
    branch_switch_count: int
    revisited_gaps: tuple[RevisitedDeformationGap, ...]
    paired_signed_gap_sum: int
    paired_absolute_gap_sum: int
    paired_loading_excess_sum: int
    paired_returning_excess_sum: int
    residual_response: int
    closed_deformation: bool


def material_cycle_diagnostics(
    states: tuple[MaterialHistoryState, ...] | list[MaterialHistoryState],
) -> MaterialCycleDiagnostics:
    """Pair only branch values that occur in the supplied finite history."""
    history = tuple(states)
    if not history:
        raise ValueError("material history must be nonempty")

    by_index_loading: dict[int, set[int]] = {}
    by_index_returning: dict[int, set[int]] = {}
    for state in history:
        if state.deformation_index < 0 or state.response_sample < 0:
            raise ValueError("material history contains a negative finite state")
        if state.branch == LOADING:
            by_index_loading.setdefault(state.deformation_index, set()).add(
                state.response_sample
            )
        elif state.branch == RETURNING:
            by_index_returning.setdefault(state.deformation_index, set()).add(
                state.response_sample
            )
        else:
            raise ValueError("material history contains an unknown branch")

    gaps: list[RevisitedDeformationGap] = []
    for index in sorted(set(by_index_loading).intersection(by_index_returning)):
        load_values = by_index_loading[index]
        return_values = by_index_returning[index]
        if len(load_values) != 1 or len(return_values) != 1:
            raise ValueError("same branch/index produced multiple response samples")
        load = next(iter(load_values))
        ret = next(iter(return_values))
        signed = load - ret
        gaps.append(
            RevisitedDeformationGap(
                deformation_index=index,
                loading_sample=load,
                returning_sample=ret,
                signed_gap=signed,
                absolute_gap=abs(signed),
                loading_excess=max(signed, 0),
                returning_excess=max(-signed, 0),
            )
        )

    switches = sum(
        left.branch != right.branch
        for left, right in zip(history, history[1:])
    )
    start = history[0]
    end = history[-1]
    return MaterialCycleDiagnostics(
        state_count=len(history),
        start_index=start.deformation_index,
        end_index=end.deformation_index,
        peak_index=max(state.deformation_index for state in history),
        branch_switch_count=switches,
        revisited_gaps=tuple(gaps),
        paired_signed_gap_sum=sum(gap.signed_gap for gap in gaps),
        paired_absolute_gap_sum=sum(gap.absolute_gap for gap in gaps),
        paired_loading_excess_sum=sum(gap.loading_excess for gap in gaps),
        paired_returning_excess_sum=sum(gap.returning_excess for gap in gaps),
        residual_response=end.response_sample - start.response_sample,
        closed_deformation=end.deformation_index == start.deformation_index,
    )
