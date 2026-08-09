import itertools
import unittest

from enterprise_math.hidden_band_predicate import (
    band_partition_globally_exact,
    global_band_profile,
    hidden_band_profile,
    hidden_band_profile_for_partition,
    least_absolute_residue,
    minimum_global_band_partition,
    scalar_global_image_step,
    scalar_hidden_step,
)


class HiddenBandPredicateTests(unittest.TestCase):
    def test_scalar_hidden_step_is_gcd_of_within_block_coefficient_differences(self):
        weights = (0, 6, 10, 3, 15)
        partition = ((0, 1, 2), (3, 4))
        # first block differences 6,10 -> gcd 2; second difference 12;
        # total hidden image step gcd(2,12)=2.
        self.assertEqual(scalar_hidden_step(weights, partition), 2)

    def test_global_scalar_image_step_is_gcd_of_coefficients(self):
        self.assertEqual(scalar_global_image_step((0, 6, 10, 14)), 2)
        self.assertEqual(scalar_global_image_step((0, 0, 0)), 0)

    def test_least_absolute_residue_matches_direct_integer_search(self):
        for modulus in range(1, 12):
            for value in range(-30, 31):
                expected = min(
                    abs(value + modulus * shift)
                    for shift in range(-50, 51)
                )
                self.assertEqual(
                    least_absolute_residue(value, modulus),
                    expected,
                )

    def test_nonzero_hidden_step_can_make_finite_band_exact_false(self):
        profile = hidden_band_profile(base_value=2, hidden_step=5, radius=1)
        self.assertEqual(profile.least_absolute_residue, 2)
        self.assertFalse(profile.has_supported_value)
        self.assertTrue(profile.has_unsupported_value)
        self.assertTrue(profile.exact)
        self.assertFalse(profile.exact_value)

    def test_nonzero_hidden_step_never_makes_finite_band_exact_true(self):
        for step in range(1, 8):
            for base in range(-10, 11):
                for radius in range(0, 5):
                    profile = hidden_band_profile(base, step, radius)
                    if profile.has_supported_value:
                        self.assertTrue(profile.has_unsupported_value)
                        self.assertFalse(profile.exact)
                        self.assertIsNone(profile.exact_value)

    def test_zero_hidden_step_is_ordinary_exact_observation(self):
        inside = hidden_band_profile(base_value=-2, hidden_step=0, radius=3)
        outside = hidden_band_profile(base_value=5, hidden_step=0, radius=3)
        self.assertTrue(inside.exact)
        self.assertTrue(inside.exact_value)
        self.assertTrue(outside.exact)
        self.assertFalse(outside.exact_value)

    def test_formula_matches_direct_progression_enumeration(self):
        for step in range(1, 9):
            for base in range(-12, 13):
                for radius in range(0, 6):
                    profile = hidden_band_profile(base, step, radius)
                    direct_supported = any(
                        abs(base + step * shift) <= radius
                        for shift in range(-30, 31)
                    )
                    self.assertEqual(profile.has_supported_value, direct_supported)

    def test_partition_example_can_answer_false_without_exact_scalar_visibility(self):
        weights = (0, 2, 4)
        partition = ((0, 2), (1,))
        self.assertEqual(scalar_hidden_step(weights, partition), 4)
        # Current fine-state/base relation value 2 lives in the residue class
        # 2 mod 4, which never enters [-1,1].
        profile = hidden_band_profile_for_partition(
            weights,
            partition,
            base_value=2,
            radius=1,
        )
        self.assertTrue(profile.exact)
        self.assertFalse(profile.exact_value)
        self.assertGreater(profile.hidden_step, 0)

    def test_globally_constant_false_band_needs_no_refinement(self):
        # Global scalar image is 1+4Z, which never reaches [-0,0].
        weights = (4, 8)
        bias = 1
        radius = 0
        profile = global_band_profile(weights, bias, radius)
        self.assertTrue(profile.globally_constant)
        self.assertFalse(profile.constant_value)
        initial = ((0, 1),)
        self.assertEqual(
            minimum_global_band_partition(weights, bias, radius, initial),
            initial,
        )
        self.assertTrue(
            band_partition_globally_exact(weights, bias, radius, initial)
        )

    def test_nonconstant_global_band_requires_exact_scalar_descent(self):
        weights = (0, 2, 4)
        bias = 0
        radius = 1
        profile = global_band_profile(weights, bias, radius)
        self.assertFalse(profile.globally_constant)
        self.assertTrue(profile.has_supported_state)
        self.assertTrue(profile.has_unsupported_state)

        coarse = ((0, 1, 2),)
        intermediate = ((0, 2), (1,))
        singleton = ((0,), (1,), (2,))
        self.assertFalse(
            band_partition_globally_exact(weights, bias, radius, coarse)
        )
        self.assertFalse(
            band_partition_globally_exact(weights, bias, radius, intermediate)
        )
        self.assertTrue(
            band_partition_globally_exact(weights, bias, radius, singleton)
        )
        self.assertEqual(
            minimum_global_band_partition(weights, bias, radius, coarse),
            singleton,
        )

    def test_global_minimum_partition_is_coarsest_scalar_visible_refinement(self):
        weights = (0, 2, 2, 5, 5)
        initial = ((0, 1, 2), (3, 4))
        # In the first block, coordinate 0 must split from equal-coefficient
        # coordinates 1,2. The second block is already scalar-visible.
        expected = ((0,), (1, 2), (3, 4))
        self.assertEqual(
            minimum_global_band_partition(weights, 0, 0, initial),
            expected,
        )
        self.assertTrue(
            band_partition_globally_exact(weights, 0, 0, expected)
        )

    def test_global_profile_matches_small_domain_truth_variability(self):
        cases = (
            ((2, 4), 1, 0),
            ((2, 4), 0, 0),
            ((3, 6), 1, 1),
            ((0, 0), 2, 1),
            ((0, 0), 1, 1),
        )
        for weights, bias, radius in cases:
            profile = global_band_profile(weights, bias, radius)
            truths = {
                abs(sum(weight * value for weight, value in zip(weights, state)) + bias)
                <= radius
                for state in itertools.product(range(-8, 9), repeat=len(weights))
            }
            if profile.globally_constant:
                self.assertEqual(truths, {profile.constant_value})
            else:
                self.assertEqual(truths, {False, True})


if __name__ == "__main__":
    unittest.main()
