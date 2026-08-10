import unittest

from enterprise_math.abc_projective_capacity_stratified import (
    active_capacity_pair_bounds,
    high_capacity_active_bounds,
    low_capacity_active_slices,
)


class ProjectiveCapacityStratifiedTests(unittest.TestCase):
    def test_3_125_128_low_capacity_complements_are_prime_powers(self) -> None:
        bounds = active_capacity_pair_bounds(3, 125, 128, 4)
        self.assertEqual(len(bounds), 1)
        bound = bounds[0]
        self.assertEqual(bound.active_component_index, 2)
        self.assertEqual(bound.complement_capacities, (1, 3))
        self.assertEqual(bound.complement_capacity_max, 3)
        self.assertEqual(bound.controlling_complement_index, 1)
        self.assertEqual(bound.controlled_pair_indices, (2, 0))
        self.assertEqual(bound.controlled_pair_values, (128, 3))
        self.assertEqual(bound.controlled_pair_radical, 6)
        self.assertLessEqual(4 * 3 * 6, 128)

        low = low_capacity_active_slices(3, 125, 128, 4, 5)
        self.assertEqual(len(low), 1)
        self.assertTrue(low[0].both_prime_powers_below_five)
        classes = low[0].complement_classifications
        self.assertEqual(
            tuple((item.prime_power_base, item.prime_power_exponent) for item in classes),
            ((3, 1), (5, 3)),
        )

    def test_10_2187_2197_has_capacity_gain_seven(self) -> None:
        bounds = active_capacity_pair_bounds(10, 2187, 2197, 6)
        self.assertEqual(len(bounds), 1)
        bound = bounds[0]
        self.assertEqual(bound.active_component_index, 1)
        self.assertEqual(bound.complement_capacities, (7, 3))
        self.assertEqual(bound.complement_capacity_max, 7)
        self.assertEqual(bound.controlling_complement_index, 0)
        self.assertEqual(bound.controlled_pair_indices, (1, 2))
        self.assertEqual(bound.controlled_pair_radical, 39)
        self.assertLessEqual(6 * 7 * 39, 2187)

        high = high_capacity_active_bounds(10, 2187, 2197, 6, 7)
        self.assertEqual(high, bounds)
        self.assertEqual(low_capacity_active_slices(10, 2187, 2197, 6, 5), ())

    def test_stage51_cutoff_five_is_strict(self) -> None:
        # At cutoff 5 the complements of the active c-term are 3 and 5^3,
        # both prime powers.  Lowering to cutoff 3 excludes the C=3 block.
        self.assertEqual(len(low_capacity_active_slices(3, 125, 128, 4, 5)), 1)
        self.assertEqual(low_capacity_active_slices(3, 125, 128, 4, 3), ())

    def test_subthreshold_triple_has_no_active_bounds(self) -> None:
        self.assertEqual(active_capacity_pair_bounds(2, 3, 5, 1), ())


if __name__ == "__main__":
    unittest.main()
