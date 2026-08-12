from enterprise_math.p022_barlow_franel_integer_lagrange import (
    endpoint_derivative_lagrange_residues,
    endpoint_multiple_root_iff_previous_lagrange_zero,
    integer_lagrange_coordinate,
    integer_lagrange_recurrence,
)


def test_integer_lagrange_initial_values() -> None:
    assert [integer_lagrange_coordinate(n) for n in range(6)] == [
        3,
        12,
        684,
        20_064,
        829_740,
        35_870_832,
    ]


def test_integer_lagrange_affine_recurrence() -> None:
    for n in range(1, 16):
        actual, predicted = integer_lagrange_recurrence(n)
        assert actual == predicted


def test_endpoint_derivative_and_lagrange_have_identical_zero_status() -> None:
    # Includes simple primitive roots and the important deep-but-transverse
    # regression p=67 at rank 23.
    for rank, prime in (
        (6, 13),
        (6, 73),
        (15, 179),
        (23, 67),
        (30, 1361),
        (50, 149),
    ):
        derivative, lagrange, factor = endpoint_derivative_lagrange_residues(rank, prime)
        assert factor != 0
        assert lagrange == factor * derivative % prime
        assert not endpoint_multiple_root_iff_previous_lagrange_zero(rank, prime)


def test_F1_endpoint_uses_F0_equal_one() -> None:
    # F_1=2, so p=2 is excluded by the odd/strictly-larger endpoint theorem;
    # use this test only to freeze the integer coordinate at n=0 and ensure the
    # boundary convention does not silently substitute F_1 for F_0.
    assert integer_lagrange_coordinate(0) == 3
