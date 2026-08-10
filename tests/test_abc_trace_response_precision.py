from fractions import Fraction

from enterprise_math.abc_trace_response_precision import (
    prefix_normal_form_path,
    stage106_arithmetic_order_boundary,
    stage106_path_not_minimal_collision,
    trace_equivalent,
    trace_response,
)
from enterprise_math.abc_merged_threshold_history import merged_threshold_history_signature


def test_gamma_predicts_full_trace_from_prefix_normal_forms() -> None:
    signature = merged_threshold_history_signature(
        (Fraction(1, 4),),
        (Fraction(1, 2),),
        (Fraction(3, 4), Fraction(5, 4)),
        (Fraction(1, 1), Fraction(2, 1)),
    )
    word = (("J", None), ("T", 1), ("T", 0), ("J", None))
    response = trace_response(signature, word)
    assert len(response.prefix_normal_forms) == len(word)
    assert len(response.area_trace) == len(word)
    assert sum(response.increment_sequence) == response.area_trace[-1] - signature.area


def test_endpoint_equal_words_can_have_different_trace_response() -> None:
    data = stage106_arithmetic_order_boundary()
    first = data["threshold_then_node"]
    second = data["node_then_threshold"]
    assert first.area_trace == (1, 3)
    assert second.area_trace == (2, 3)
    assert first.increment_sequence == (0, 2)
    assert second.increment_sequence == (1, 1)


def test_prefix_normal_form_path_is_state_independent_sufficient_word_abstraction() -> None:
    word = (("T", 1), ("J", None), ("T", 0))
    path = prefix_normal_form_path(word, 2, 1)
    assert path[0].selected_threshold_indices == (1,)
    assert path[0].future_prefix_length == 0
    assert path[1].selected_threshold_indices == (1,)
    assert path[1].future_prefix_length == 1
    assert path[2].selected_threshold_indices == (0, 1)
    assert path[2].future_prefix_length == 1


def test_prefix_path_is_not_coarsest_for_fixed_state_trace() -> None:
    data = stage106_path_not_minimal_collision()
    assert data["first"].prefix_normal_forms != data["second"].prefix_normal_forms
    assert data["first"].area_trace == data["second"].area_trace == (1, 2)
    assert data["first"].increment_sequence == data["second"].increment_sequence == (1, 1)


def test_trace_equivalence_is_increment_equivalence_for_fixed_area() -> None:
    signature = merged_threshold_history_signature(
        (),
        (Fraction(1, 1),),
        (Fraction(1, 2), Fraction(3, 4)),
        (),
    )
    assert trace_equivalent(
        signature,
        (("T", 0), ("T", 1)),
        (("T", 1), ("T", 0)),
    )
