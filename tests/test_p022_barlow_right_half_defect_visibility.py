from enterprise_math.p022_barlow_right_half_defect_visibility import (
    above_midpoint_relation_support,
    right_half_defect_column,
    right_half_relation_occurrences,
    right_half_zero_column_iff_twin,
)


def test_right_half_twin_columns_are_completely_invisible_before_q() -> None:
    # q=41 has Franel zero digits 30 and 33 in the right half.  The index 30
    # is a twin center (59,61), hence its whole defect column below q is zero.
    assert right_half_relation_occurrences(41, 30) == ()
    assert right_half_defect_column(41, 30) == ()
    assert right_half_zero_column_iff_twin(41, 30)

    # 33 is not a twin center: 65 is composite, so D_33 sees it directly.
    assert right_half_defect_column(41, 33)[0] == (33, 1)
    assert not right_half_zero_column_iff_twin(41, 33)


def test_right_half_successor_is_the_only_relation_occurrence() -> None:
    # q=23, s=16: 31 is prime but 33 is composite.  D_17 is the unique
    # canonical relation below q containing A_16.
    assert right_half_relation_occurrences(23, 16) == ((17, 1),)
    assert right_half_defect_column(23, 16) == ((17, -1),)


def test_above_midpoint_high_support_is_one_path_edge() -> None:
    for prime in (29, 41, 73):
        midpoint = (prime - 1) // 2
        for segment in range(midpoint + 2, prime):
            odd_boundary = 2 * segment - 1
            # The helper is intentionally defined only on composite rows.
            if all(odd_boundary % d for d in range(2, int(odd_boundary**0.5) + 1)):
                continue
            assert above_midpoint_relation_support(prime, segment) == (
                (segment - 1, 1),
            )
