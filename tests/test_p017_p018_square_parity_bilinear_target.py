from enterprise_math.p017_p018_square_parity_bilinear_target import (
    mobius,
    square_shell_factor_fiber,
    square_shell_parity_bilinear_slice,
    truncated_mobius_divisor_sum,
)


def test_exact_mobius_and_truncated_divisor_weight() -> None:
    assert mobius(1) == 1
    assert mobius(2) == -1
    assert mobius(6) == 1
    assert mobius(12) == 0
    assert mobius(30) == -1

    assert truncated_mobius_divisor_sum(30, 1) == 1
    assert truncated_mobius_divisor_sum(30, 2) == 0
    assert truncated_mobius_divisor_sum(30, 5) == -1
    assert truncated_mobius_divisor_sum(30, 30) == 0


def test_square_shell_factor_fiber_is_exact_floor_interval() -> None:
    for k, n in ((10, 3), (17, 5), (100, 37), (203, 31), (500, 101)):
        row = square_shell_factor_fiber(k, n)
        expected = tuple(
            m
            for m in range(row["m_min"], row["m_max"] + 1)
            if k * k < m * n <= k * k + 2 * k
        )
        assert len(expected) == row["fiber_count"]
        assert row["fiber_count"] == (k * k + 2 * k) // n - (k * k) // n


def test_finite_bilinear_slice_retains_signed_mobius_weight() -> None:
    data = square_shell_parity_bilinear_slice(31, 7, 15, 5, p2_rough_only=True)
    assert data["status"] == "FINITE_PARITY_BILINEAR_ORACLE_ONLY"
    assert data["p2_rough_only"]
    assert data["term_count"] >= 0
    assert data["bilinear_absolute_outer_sum"] >= abs(
        data["signed_term_sum_before_outer_absolute_values"]
    )

    raw = square_shell_parity_bilinear_slice(31, 7, 15, 5, p2_rough_only=False)
    assert raw["term_count"] >= data["term_count"]
