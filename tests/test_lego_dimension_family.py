import unittest

from enterprise_math.lego_dimension_family import (
    expected_hard_single_row,
    expected_unrestricted_row,
    generate_dimension_rows,
    hard_single_occupancy_profile,
    nonnegative_multiplicity_profile,
    recover_shared_kernel_from_rows,
    unrestricted_occupancy_profile,
)


class LegoDimensionFamilyTests(unittest.TestCase):
    def test_unrestricted_single_block_generates_stars_and_bars_all_dimensions(self):
        maximum_total = 8
        profile = unrestricted_occupancy_profile(maximum_total)
        rows = generate_dimension_rows(profile, 6, maximum_total)
        for dimension, row in enumerate(rows, start=1):
            self.assertEqual(row, expected_unrestricted_row(dimension, maximum_total))
        self.assertEqual(recover_shared_kernel_from_rows(rows), profile)

    def test_hard_single_occupancy_generates_binomial_rows(self):
        maximum_total = 8
        profile = hard_single_occupancy_profile(maximum_total)
        rows = generate_dimension_rows(profile, 7, maximum_total)
        for dimension, row in enumerate(rows, start=1):
            self.assertEqual(row, expected_hard_single_row(dimension, maximum_total))
        self.assertEqual(recover_shared_kernel_from_rows(rows), profile)

    def test_internal_degeneracy_profile_repeats_across_dimensions(self):
        profile = (1, 2, 1, 0, 3, 0, 0)
        rows = generate_dimension_rows(profile, 5, 6)
        self.assertEqual(recover_shared_kernel_from_rows(rows), profile)
        self.assertTrue(nonnegative_multiplicity_profile(profile))

    def test_ambient_dimension_dependent_rows_fail_shared_kernel_test(self):
        profile_a = (1, 1, 1, 1, 1)
        profile_b = (1, 1, 0, 1, 1)
        rows_a = generate_dimension_rows(profile_a, 2, 4)
        # Build a third row using a different added-block law.
        from enterprise_math.lego_dimension_kernel import apply_dimension_kernel
        third = apply_dimension_kernel(rows_a[-1], profile_b)
        with self.assertRaises(ValueError):
            recover_shared_kernel_from_rows((rows_a[0], rows_a[1], third))

    def test_negative_recovered_profile_is_not_a_state_multiplicity_law(self):
        self.assertFalse(nonnegative_multiplicity_profile((1, 2, -1, 0)))


if __name__ == "__main__":
    unittest.main()
