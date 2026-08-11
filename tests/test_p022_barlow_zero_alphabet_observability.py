import pytest

from enterprise_math.p022_barlow_zero_alphabet_observability import (
    canonical_unit_peeling_certificate,
    certified_zero_kernel_dimension,
    primitive_source_is_observable,
    upper_half_twin_zero_digits,
    upper_twin_columns_are_zero,
    zero_alphabet,
)


def test_q41_kernel_is_exactly_the_upper_twin_mode() -> None:
    assert zero_alphabet(41) == (7, 10, 30, 33)
    assert upper_half_twin_zero_digits(41) == (30,)
    assert upper_twin_columns_are_zero(41)
    free, pivots = canonical_unit_peeling_certificate(41)
    assert free == (30,)
    assert tuple(digit for digit, _, _ in pivots) == (7, 10, 33)
    assert certified_zero_kernel_dimension(41) == 1
    assert primitive_source_is_observable(41)


def test_q521_has_the_second_known_upper_twin_free_mode() -> None:
    assert zero_alphabet(521) == (199, 321)
    assert upper_half_twin_zero_digits(521) == (321,)
    free, pivots = canonical_unit_peeling_certificate(521)
    assert free == (321,)
    assert pivots == ((199, 200, -1),)
    assert certified_zero_kernel_dimension(521) == 1
    assert primitive_source_is_observable(521)


def test_twin_primitive_rows_peel_by_first_reentry() -> None:
    assert zero_alphabet(73) == (6, 66)
    free, pivots = canonical_unit_peeling_certificate(73)
    assert free == ()
    assert pivots[0] == (6, 11, 1)
    assert certified_zero_kernel_dimension(73) == 0
    assert primitive_source_is_observable(73)


def test_larger_multi_zero_alphabet_still_unit_peels() -> None:
    assert zero_alphabet(701) == (97, 245, 299, 350, 401, 455, 603)
    free, pivots = canonical_unit_peeling_certificate(701)
    assert free == ()
    assert len(pivots) == 7
    assert all(coefficient in (-1, 1) for _, _, coefficient in pivots)
    assert primitive_source_is_observable(701)


def test_q5_is_the_small_twin_reentry_exception() -> None:
    assert zero_alphabet(5) == (2,)
    with pytest.raises(AssertionError):
        canonical_unit_peeling_certificate(5)
