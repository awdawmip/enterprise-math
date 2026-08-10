from enterprise_math.p022_barlow_two_rank_primitive_coverage import (
    two_rank_candidate_ranks,
    two_rank_certificate_diagonal,
    two_rank_certificate_is_unimodular,
    two_rank_primitive_pivot,
    two_rank_row_is_triangular,
)


def test_composite_columns_have_current_plus_optional_predecessor_rank() -> None:
    assert two_rank_candidate_ranks(5) == (5, 4)    # 9 composite, 7 prime
    assert two_rank_candidate_ranks(8) == (8, 7)    # 15 composite, 13 prime
    assert two_rank_candidate_ranks(11) == (11, 10) # 21 composite, 19 prime
    assert two_rank_candidate_ranks(14) == (14,)     # 27 and 25 composite


def test_predecessor_primitive_events_give_negative_triangular_pivots() -> None:
    examples = (
        (5, 4, 173),
        (8, 7, 41),
        (11, 10, 61),
        (13, 12, 176_459),
    )
    earlier = []
    for segment, source_rank, prime in examples:
        assert two_rank_primitive_pivot(segment, source_rank, prime) == -1
        assert two_rank_row_is_triangular(segment, source_rank, prime, tuple(earlier))
        earlier.append(segment)


def test_current_rank_primitive_event_remains_positive_pivot() -> None:
    assert two_rank_primitive_pivot(14, 14, 12_148_537) == 1


def test_mixed_current_and_predecessor_markers_give_unimodular_certificate() -> None:
    # Composite-boundary columns through 14 are 5,8,11,13,14.  Four are
    # deliberately pivoted from the previous prime-boundary rank, showing that
    # the old 'primitive divisor at every composite rank itself' hypothesis is
    # not required by the triangular certificate construction.
    markers = (
        (5, 4, 173),
        (8, 7, 41),
        (11, 10, 61),
        (13, 12, 176_459),
        (14, 14, 12_148_537),
    )
    assert two_rank_certificate_diagonal(14, markers) == (1, -1, -1, -1, -1, 1)
    assert two_rank_certificate_is_unimodular(14, markers)
