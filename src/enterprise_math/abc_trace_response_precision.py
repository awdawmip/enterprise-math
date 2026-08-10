"""Trace-sensitive operation precision over the Stage105 endpoint generator.

The compact state generator Gamma remains sufficient for full area traces: each
word prefix is mapped to its endpoint normal form and evaluated by Gamma.  What
changes from endpoint to trace semantics is the operation-word quotient, not
necessarily the state quotient.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence

from .abc_history_response_normal import (
    Action,
    EndpointWordNormalForm,
    area_trace_for_word,
    normalize_action_word,
)
from .abc_merged_threshold_history import MergedThresholdHistorySignature, merged_threshold_history_signature
from .abc_signed_exponent_transport import dyadic_difference_pressure_tower


@dataclass(frozen=True)
class TraceResponse:
    prefix_normal_forms: tuple[EndpointWordNormalForm, ...]
    area_trace: tuple[int, ...]
    increment_sequence: tuple[int, ...]


def prefix_normal_form_path(
    word: Sequence[Action],
    candidate_count: int,
    future_count: int,
) -> tuple[EndpointWordNormalForm, ...]:
    """Return the endpoint normal form of every non-empty word prefix."""
    return tuple(
        normalize_action_word(word[: index + 1], candidate_count, future_count)
        for index in range(len(word))
    )


def trace_response(
    signature: MergedThresholdHistorySignature,
    word: Sequence[Action],
) -> TraceResponse:
    trace = area_trace_for_word(signature, word)
    previous = signature.area
    increments: list[int] = []
    for area in trace:
        increments.append(area - previous)
        previous = area
    path = prefix_normal_form_path(
        word,
        len(signature.candidate_thresholds),
        len(signature.future_total_ranks),
    )
    return TraceResponse(path, trace, tuple(increments))


def trace_equivalent(
    signature: MergedThresholdHistorySignature,
    first_word: Sequence[Action],
    second_word: Sequence[Action],
) -> bool:
    """For fixed current area, equal increment sequences iff area traces agree."""
    first = trace_response(signature, first_word)
    second = trace_response(signature, second_word)
    return first.increment_sequence == second.increment_sequence


def stage106_arithmetic_order_boundary() -> dict[str, object]:
    """Exact P025 example: same endpoint, different trace increments."""
    pressures = dyadic_difference_pressure_tower(3, 41, 2, 1).pressures
    signature = merged_threshold_history_signature(
        (Fraction(1, 25),),
        pressures[:1],
        (Fraction(11, 20),),
        pressures[1:],
    )
    threshold_then_node = (("T", 0), ("J", None))
    node_then_threshold = (("J", None), ("T", 0))
    first = trace_response(signature, threshold_then_node)
    second = trace_response(signature, node_then_threshold)
    if first.area_trace[-1] != second.area_trace[-1]:
        raise AssertionError("fixture endpoints should agree")
    if first.increment_sequence == second.increment_sequence:
        raise AssertionError("fixture should separate trace increments")
    return {
        "signature": signature,
        "threshold_then_node": first,
        "node_then_threshold": second,
    }


def stage106_path_not_minimal_collision() -> dict[str, object]:
    """Different prefix-normal-form paths can still have the same fixed-state trace.

    With no old thresholds, old value 1, and two already-resolved candidate
    thresholds 1/2 and 3/4, either insertion order contributes increments (1,1).
    """
    signature = merged_threshold_history_signature(
        (),
        (Fraction(1, 1),),
        (Fraction(1, 2), Fraction(3, 4)),
        (),
    )
    first_word = (("T", 0), ("T", 1))
    second_word = (("T", 1), ("T", 0))
    first = trace_response(signature, first_word)
    second = trace_response(signature, second_word)
    if first.prefix_normal_forms == second.prefix_normal_forms:
        raise AssertionError("fixture paths should differ")
    if first.area_trace != second.area_trace:
        raise AssertionError("fixture traces should collide")
    return {
        "signature": signature,
        "first": first,
        "second": second,
    }
