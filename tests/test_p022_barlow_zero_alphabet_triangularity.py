from enterprise_math.p022_barlow_zero_alphabet_triangularity import (
    left_half_twin_zero_digits,
    left_twin_terminal_collisions,
    left_twin_terminal_triangular_row,
    non_twin_local_triangular_row,
    triangular_free_columns_are_right_half_twins,
    triangular_pivot_rows_if_no_terminal_collision,
)


def test_known_left_twin_zeros_have_clean_terminal_rows() -> None:
    expected = {
        73: (6,),
        1373: (96,),
        2111: (411,),
        2731: (966,),
        3187: (1071,),
    }
    for prime, twins in expected.items():
        assert left_half_twin_zero_digits(prime) == twins
        assert left_twin_terminal_collisions(prime) == ()
        for source in twins:
            segment, row = left_twin_terminal_triangular_row(prime, source)
            assert segment == 2 * source - 1
            assert dict(row)[source] == 1
            assert all(index <= source for index, _ in row)


def test_non_twin_zero_rows_are_locally_triangular() -> None:
    # q=41 has left non-twin zeros 7,10 and right non-twin zero 33.
    expected_rows = {7: 8, 10: 11, 33: 33}
    for zero, segment in expected_rows.items():
        actual_segment, row = non_twin_local_triangular_row(41, zero)
        assert actual_segment == segment
        assert zero in dict(row)
        assert all(index <= zero for index, _ in row)


def test_conditional_triangular_pivots_match_rref_examples() -> None:
    expected = {
        41: ((7, 8), (10, 11), (33, 33)),
        73: ((6, 11), (66, 67)),
        1373: ((96, 191), (686, 686), (1276, 1277)),
        2731: ((966, 1931),),
        3187: ((1071, 2141),),
    }
    for prime, pivots in expected.items():
        assert left_twin_terminal_collisions(prime) == ()
        assert triangular_pivot_rows_if_no_terminal_collision(prime) == pivots
        assert triangular_free_columns_are_right_half_twins(prime)


def test_current_regression_primes_have_no_left_twin_terminal_collision() -> None:
    for prime in (
        13,
        29,
        41,
        59,
        67,
        73,
        149,
        157,
        179,
        337,
        521,
        937,
        1373,
        2111,
        2417,
        2557,
        2731,
        2819,
        3187,
        3433,
        4019,
    ):
        assert left_twin_terminal_collisions(prime) == ()
        assert triangular_free_columns_are_right_half_twins(prime)
