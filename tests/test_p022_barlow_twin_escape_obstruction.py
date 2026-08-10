import pytest

from enterprise_math.p022_barlow_twin_escape_obstruction import (
    complete_escape_signature,
    escape_geometry_primes,
    terminal_cancellation_is_equal_depth,
    terminal_reflection_index,
)


def test_known_primitive_twin_rows_do_not_completely_escape() -> None:
    for rank, prime in ((3, 7), (6, 13), (6, 73), (21, 3019), (30, 1361)):
        assert not terminal_cancellation_is_equal_depth(rank, prime)
        assert terminal_reflection_index(rank, prime) is None
        assert complete_escape_signature(rank, prime) is None


def test_escape_geometry_requires_the_endpoint_defect_to_be_absent() -> None:
    assert escape_geometry_primes(6) == (11, 13, 19)
    assert escape_geometry_primes(21) == (41, 43, 79)

    # r=30 is a twin center (59,61), but 4r-5=115 is composite; an endpoint
    # zero at F_58 would therefore be visible already at D_58.
    with pytest.raises(ValueError):
        escape_geometry_primes(30)
