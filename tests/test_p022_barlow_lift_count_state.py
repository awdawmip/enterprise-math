from enterprise_math.p022_barlow_higher_channel_repair import (
    path_lift_count,
    path_lift_factors,
)
from enterprise_math.p022_barlow_lift_count_state import (
    common_extension_preserves_count_alias,
    extend_lift_count_along_path,
    lift_count_state,
    rank_three_same_state_count_mechanism_alias,
)


def test_rank_three_alias_has_same_endpoint_and_count_but_different_mechanism() -> None:
    first, second, first_factors, second_factors, state = (
        rank_three_same_state_count_mechanism_alias()
    )
    assert first_factors == (8, 1, 8, 3)
    assert second_factors == (8, 3, 4, 2)
    assert first_factors != second_factors
    assert path_lift_count(first) == path_lift_count(second) == 192
    assert lift_count_state(first) == lift_count_state(second) == state
    assert state == ((0, 2, 2), 192)


def test_compressed_count_state_matches_full_recomputed_extension() -> None:
    first, second, *_ = rank_three_same_state_count_mechanism_alias()
    continuations = (
        ((1, 1, 3),),
        ((1, 1, 3), (0, 2, 2)),
        ((1, 1, 3), (0, 2, 4)),
    )
    for continuation in continuations:
        compressed = extend_lift_count_along_path(
            lift_count_state(first), continuation
        )
        assert compressed == extend_lift_count_along_path(
            lift_count_state(second), continuation
        )
        full_first = first + continuation
        full_second = second + continuation
        assert compressed == (full_first[-1], path_lift_count(full_first))
        assert compressed == (full_second[-1], path_lift_count(full_second))


def test_common_extension_helper_preserves_alias_exactly() -> None:
    first, second, *_ = rank_three_same_state_count_mechanism_alias()
    final_first, final_second = common_extension_preserves_count_alias(
        first,
        second,
        ((1, 1, 3), (0, 2, 2)),
    )
    assert final_first == final_second


def test_mechanism_query_cannot_factor_through_count_state() -> None:
    first, second, first_factors, second_factors, state = (
        rank_three_same_state_count_mechanism_alias()
    )
    assert lift_count_state(first) == lift_count_state(second) == state
    assert first_factors != second_factors
    # Therefore the observable "ordered local radix sequence" is not constant
    # on a fiber of the compressed state map and cannot factor through it.
