from fractions import Fraction

from enterprise_math.abc_merged_threshold_history import (
    decode_future_column,
    history_area_from_merged_signature,
    merged_threshold_history_signature,
    verify_merged_generator_equivalence,
)
from enterprise_math.abc_signed_exponent_transport import dyadic_difference_pressure_tower


def test_merged_rank_decodes_old_rank_and_candidate_corners() -> None:
    signature = merged_threshold_history_signature(
        (Fraction(1, 2), Fraction(3, 1)),
        (Fraction(1, 1),),
        (Fraction(2, 1), Fraction(4, 1)),
        (Fraction(5, 2), Fraction(5, 1)),
    )
    first = decode_future_column(signature, 0)
    second = decode_future_column(signature, 1)
    assert first["old_threshold_rank"] == 1
    assert first["candidate_corner_column"] == (1, 0)
    assert second["old_threshold_rank"] == 2
    assert second["candidate_corner_column"] == (1, 1)


def test_merged_generator_matches_expanded_second_order_signature() -> None:
    assert verify_merged_generator_equivalence(
        (Fraction(1, 4), Fraction(1, 1)),
        (Fraction(1, 2), Fraction(3, 2)),
        (Fraction(3, 4), Fraction(2, 1), Fraction(5, 2)),
        (Fraction(2, 1), Fraction(3, 1)),
    )


def test_merged_history_area_handles_candidate_subsets() -> None:
    signature = merged_threshold_history_signature(
        (Fraction(1, 2), Fraction(3, 1)),
        (Fraction(1, 1),),
        (Fraction(2, 1), Fraction(4, 1)),
        (Fraction(5, 2), Fraction(5, 1)),
    )
    # Current area=1. Candidate 2 is not selected; only threshold 2 is selected.
    # Old-node candidate span is zero. Future contributions are:
    # v=5/2 -> old 1 + selected candidate 1; v=5 -> old 2 + selected candidate 1.
    assert history_area_from_merged_signature(signature, (0,), 2) == 6


def test_future_generator_state_count_depends_only_on_unresolved_merged_suffix() -> None:
    signature = merged_threshold_history_signature(
        (Fraction(1, 4), Fraction(3, 4), Fraction(5, 1)),
        (Fraction(1, 1),),
        (Fraction(1, 2), Fraction(2, 1), Fraction(4, 1)),
        (Fraction(3, 2), Fraction(3, 1)),
    )
    # M=1 resolves 1/4,1/2,3/4. Three merged thresholds remain unresolved: 2,4,5.
    assert signature.unresolved_merged_count == 3
    assert signature.future_rank_state_count == 10  # C(3+2,2)
    assert signature.unconstrained_future_rank_tuple_count == 16


def test_zero_unresolved_merged_thresholds_force_future_generator() -> None:
    signature = merged_threshold_history_signature(
        (Fraction(1, 4), Fraction(1, 2)),
        (Fraction(2, 1),),
        (Fraction(3, 4), Fraction(1, 1)),
        (Fraction(2, 1), Fraction(3, 1)),
    )
    assert signature.unresolved_merged_count == 0
    assert signature.future_rank_state_count == 1
    assert signature.future_total_ranks == (4, 4)


def test_arithmetic_dyadic_merged_generator() -> None:
    pressures = dyadic_difference_pressure_tower(3, 41, 2, 3).pressures
    assert verify_merged_generator_equivalence(
        (Fraction(1, 25), Fraction(1, 2), Fraction(20, 1)),
        pressures[:2],
        (Fraction(1, 1), Fraction(5, 1), Fraction(11, 1), Fraction(30, 1)),
        pressures[2:],
    )
