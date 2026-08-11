import pytest

from enterprise_math.p022_barlow_twin_quadratic_reentry import (
    left_quadratic_high_support,
    left_quadratic_segment,
    quadratic_escape_outcomes,
    quadratic_transported_indices,
    right_quadratic_high_support,
    right_quadratic_segment,
)


def test_quadratic_neighbor_products_have_clean_high_support() -> None:
    for rank in (6, 9, 15, 21, 30, 36, 51, 90):
        left = left_quadratic_segment(rank)
        right = right_quadratic_segment(rank)
        assert left_quadratic_high_support(rank) == (
            (rank, 1),
            (left - 1, 1),
        )
        assert right_quadratic_high_support(rank) == (
            (rank, -1),
            (rank + 1, 1),
            (right - 1, 1),
        )


def test_transported_quadratic_indices_have_linear_separation() -> None:
    expected = {
        6: (50, 97),
        9: (128, 199),
        15: (392, 511),
        21: (800, 967),
        30: (1_682, 1_921),
    }
    for rank, pair in expected.items():
        assert quadratic_transported_indices(rank) == pair
        assert pair[1] - pair[0] == 8 * rank - 1


def test_known_primitive_twin_rows_are_already_seen_by_quadratic_pair() -> None:
    expected = {
        (6, 73): ((50, -1), (98, 1)),
        (9, 937): ((128, -1), (200, 1)),
        (15, 179): ((392, -1), (512, 1)),
        (21, 3019): ((800, -1), (968, 1)),
    }
    for key, value in expected.items():
        assert quadratic_escape_outcomes(*key) == value


def test_digit_band_is_not_claimed_before_terminal_horizon() -> None:
    # q=13 is primitive at r=6, but it lies below 3r-1.  The clean quadratic
    # relations still exist; only the one-extra-digit consequence is deferred.
    with pytest.raises(ValueError, match="terminal horizon"):
        quadratic_escape_outcomes(6, 13)
