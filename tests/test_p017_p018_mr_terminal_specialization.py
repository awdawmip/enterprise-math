from enterprise_math.p017_p018_mr_terminal_specialization import (
    half_rough_liouville,
    mr_h2_half_rough_bilinear_sum,
)


def test_half_rough_liouville_is_minus_prime_indicator_on_k_to_2k() -> None:
    for k in (9, 10, 17, 31, 100, 203):
        data = mr_h2_half_rough_bilinear_sum(k)
        assert data["long_half_rough_liouville_sum"] == -data["prime_count_k_to_2k"]
        assert data["status"] == "MR_H2_TERMINAL_SPECIALIZATION_ONLY"


def test_h2_bilinear_sum_is_terminal_pair_count_plus_two_boundary_terms() -> None:
    for k in (9, 10, 17, 31, 100, 203, 500):
        data = mr_h2_half_rough_bilinear_sum(k)
        assert data["bilinear_sum"] == (
            data["central_terminal_semiprime_count"]
            + data["lower_square_prime_term"]
            + data["twin_double_orientation_term"]
        )
        assert data["far_terminal_boundary_count"] <= 2
        assert all(
            q in (2 * k + 1, 2 * k + 3)
            for _p, q, _value in data["far_terminal_boundary_rows"]
        )


def test_half_rough_liouville_vanishes_on_small_prime_divisibility() -> None:
    k = 31
    assert half_rough_liouville(k, 15) == 0
    assert half_rough_liouville(k, 17) == -1
