from fractions import Fraction

from enterprise_math.p017_p018_walsh_mobius_harmonic_aggregate import (
    mobius_harmonic_aggregate,
    reciprocal_mobius_kernel,
)


def test_first_two_odd_quotient_kernels_are_unsmoothed():
    for k in (46, 82):
        assert reciprocal_mobius_kernel(k, 1, 1) == 1
        assert reciprocal_mobius_kernel(k, 1, 2) == 1


def test_reciprocal_mobius_kernel_is_exact_fraction():
    value = reciprocal_mobius_kernel(46, 1, 7)
    assert isinstance(value, Fraction)


def test_low_product_biprimitive_axis_collapses_to_quotient_kernel_exactly():
    for k in (8, 17, 23):
        data = mobius_harmonic_aggregate(k)
        assert data["mobius_harmonic_aggregate_identity"] is True
        assert data["direct_ordered_low_product_sum"] == data["transformed_ordered_low_product_sum"]
        for row in data["rows"]:
            if row["quotient_strip"] in (1, 2):
                assert row["reciprocal_mobius_kernel"] == 1
