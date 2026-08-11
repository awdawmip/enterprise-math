import pytest

from enterprise_math.p022_barlow_twin_source_reentry_barrier import (
    fivefold_reentry_or_barrier,
    left_threefold_high_support,
    right_fivefold_high_support,
    right_threefold_high_support,
    threefold_reentry_or_barrier,
)


def test_right_threefold_clean_support_when_segment_is_composite() -> None:
    assert right_threefold_high_support(6) == (
        (6, -1),
        (7, 1),
        (19, 1),
    )
    assert right_threefold_high_support(21) == (
        (21, -1),
        (22, 1),
        (64, 1),
    )
    assert right_threefold_high_support(30) == (
        (30, -1),
        (31, 1),
        (91, 1),
    )


def test_prime_right_threefold_uses_even_left_fallback() -> None:
    with pytest.raises(ValueError, match="left threefold fallback"):
        right_threefold_high_support(9)
    assert left_threefold_high_support(9) == ((9, 1), (25, 1))
    assert left_threefold_high_support(15) == ((15, 1), (43, 1))


def test_right_fivefold_support_is_uniform_from_rank_nine() -> None:
    expected = {
        9: ((9, -1), (10, 1), (47, 1)),
        15: ((15, -1), (16, 1), (77, 1)),
        21: ((21, -1), (22, 1), (107, 1)),
        30: ((30, -1), (31, 1), (152, 1)),
        51: ((51, -1), (52, 1), (257, 1)),
    }
    for rank, support in expected.items():
        assert right_fivefold_high_support(rank) == support


def test_rank_six_is_explicitly_kept_out_of_uniform_fivefold_statement() -> None:
    with pytest.raises(ValueError, match="at least nine"):
        right_fivefold_high_support(6)
    with pytest.raises(ValueError, match="finite exceptional"):
        fivefold_reentry_or_barrier(6, 73)


def test_known_primitive_twin_rows_are_captured_before_barrier_hypothesis() -> None:
    # These rows are genuine primitive twin examples, but their terminal defect
    # does not cancel.  The barrier theorem must therefore refuse to pretend the
    # later escape hypothesis holds.
    for rank, prime in ((6, 73), (9, 937), (15, 179), (21, 3019)):
        with pytest.raises(ValueError, match="terminal defect has not cancelled"):
            threefold_reentry_or_barrier(rank, prime)
