from enterprise_math.p022_barlow_franel_holonomy import (
    composite_defect_product,
    cumulative_transfer_mismatch,
    defect_is_discrete_multiplicative_derivative,
    telescoping_transfer_mismatch,
)
from enterprise_math.p022_barlow_franel_transfer_defect import (
    boundary_transfer_defect,
)
from enterprise_math.p022_barlow_low_order_defect_reduction import (
    composite_indices,
)


def test_cumulative_mismatch_is_product_of_only_composite_defects() -> None:
    for maximum in range(1, 50):
        assert cumulative_transfer_mismatch(maximum) == composite_defect_product(
            maximum
        )


def test_factorial_double_factorial_telescoping_formula() -> None:
    for maximum in range(1, 35):
        assert cumulative_transfer_mismatch(maximum) == telescoping_transfer_mismatch(
            maximum
        )


def test_boundary_defect_is_exact_multiplicative_first_difference() -> None:
    for segment in range(2, 60):
        assert defect_is_discrete_multiplicative_derivative(segment)
        assert cumulative_transfer_mismatch(segment) == (
            cumulative_transfer_mismatch(segment - 1)
            * boundary_transfer_defect(segment)
        )


def test_mismatch_is_constant_across_prime_boundaries() -> None:
    composite = set(composite_indices(70))
    for segment in range(2, 71):
        previous = cumulative_transfer_mismatch(segment - 1)
        current = cumulative_transfer_mismatch(segment)
        if segment not in composite:
            assert current == previous
        else:
            assert current / previous == boundary_transfer_defect(segment)
