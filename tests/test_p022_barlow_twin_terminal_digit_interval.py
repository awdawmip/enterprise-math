from enterprise_math.p022_barlow_twin_terminal_digit_interval import (
    forced_source_high_affine_line,
    forced_source_high_hidden_twin_constellation,
    secondary_digit_prime_interval,
    source_high_interval,
    source_high_low_digits,
    source_high_prime_lines,
)


def test_source_high_band_collapses_to_six_consecutive_q_values() -> None:
    for rank in (51, 96, 105, 126):
        assert secondary_digit_prime_interval(rank, rank) == (
            8 * rank - 30,
            8 * rank - 25,
        )
        assert source_high_interval(rank) == (8 * rank - 30, 8 * rank - 25)


def test_twin_rank_primality_filter_leaves_two_affine_lines() -> None:
    # r=51 and r=96 are nontrivial twin centers.
    for rank in (51, 96):
        assert source_high_prime_lines(rank) == (8 * rank - 29, 8 * rank - 25)
        rows = source_high_low_digits(rank)
        assert rows == (
            (8 * rank - 29, 5 * rank + 18),
            (8 * rank - 25, rank + 18),
        )


def test_forced_midpoint_residue_class_keeps_only_q_8r_minus_25() -> None:
    for rank in (51, 96):
        prime, low = forced_source_high_affine_line(rank)
        assert prime == 8 * rank - 25
        assert prime % 24 == 23
        assert low == rank + 18


def test_hidden_low_digit_would_force_shifted_twin_constellation() -> None:
    rank = 51
    forms = forced_source_high_hidden_twin_constellation(rank)
    assert forms == (101, 103, 137, 139, 383)
