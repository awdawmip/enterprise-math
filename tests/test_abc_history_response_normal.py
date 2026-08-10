from fractions import Fraction

from enterprise_math.abc_history_response_normal import (
    area_trace_for_word,
    endpoint_area_for_word,
    endpoint_class_count,
    endpoint_fiber_size,
    normalize_action_word,
    raw_valid_word_count,
    recover_generator_from_endpoint_responses,
)
from enterprise_math.abc_merged_threshold_history import merged_threshold_history_signature
from enterprise_math.abc_signed_exponent_transport import dyadic_difference_pressure_tower


def test_interleavings_share_endpoint_normal_form() -> None:
    word_a = (("T", 1), ("J", None), ("T", 0), ("J", None))
    word_b = (("J", None), ("T", 0), ("J", None), ("T", 1))
    assert normalize_action_word(word_a, 2, 2) == normalize_action_word(word_b, 2, 2)


def test_endpoint_semantics_commute_but_trace_semantics_do_not() -> None:
    signature = merged_threshold_history_signature(
        (Fraction(1, 4),),
        (Fraction(1, 2),),
        (Fraction(3, 4),),
        (Fraction(1, 1),),
    )
    threshold_then_node = (("T", 0), ("J", None))
    node_then_threshold = (("J", None), ("T", 0))
    assert endpoint_area_for_word(signature, threshold_then_node) == 3
    assert endpoint_area_for_word(signature, node_then_threshold) == 3
    assert area_trace_for_word(signature, threshold_then_node) == (1, 3)
    assert area_trace_for_word(signature, node_then_threshold) == (2, 3)


def test_exact_arithmetic_trace_boundary() -> None:
    pressures = dyadic_difference_pressure_tower(3, 41, 2, 1).pressures
    signature = merged_threshold_history_signature(
        (Fraction(1, 25),),
        pressures[:1],
        (Fraction(11, 20),),
        pressures[1:],
    )
    threshold_then_node = (("T", 0), ("J", None))
    node_then_threshold = (("J", None), ("T", 0))
    assert endpoint_area_for_word(signature, threshold_then_node) == 3
    assert endpoint_area_for_word(signature, node_then_threshold) == 3
    assert area_trace_for_word(signature, threshold_then_node) == (1, 3)
    assert area_trace_for_word(signature, node_then_threshold) == (2, 3)


def test_endpoint_class_and_raw_word_counts() -> None:
    assert endpoint_class_count(2, 2) == 12
    assert raw_valid_word_count(2, 2) == 35
    assert endpoint_fiber_size(2, 2) == 12


def test_compact_generator_is_recoverable_from_endpoint_response_family() -> None:
    signature = merged_threshold_history_signature(
        (Fraction(1, 4), Fraction(1, 1)),
        (Fraction(1, 2), Fraction(3, 2)),
        (Fraction(3, 4), Fraction(2, 1), Fraction(5, 2)),
        (Fraction(2, 1), Fraction(3, 1)),
    )
    recovered = recover_generator_from_endpoint_responses(signature)
    assert recovered.threshold_spans == signature.threshold_spans
    assert recovered.future_total_ranks == signature.future_total_ranks
