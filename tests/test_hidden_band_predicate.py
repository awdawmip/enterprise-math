import itertools
import unittest

from enterprise_math.hidden_band_predicate import (
    hidden_band_profile,
    hidden_band_profile_for_partition,
    least_absolute_residue,
    scalar_hidden_step,
)


class HiddenBandPredicateTests(unittest.TestCase):
    def test_scalar_hidden_step_is_gcd_of_within_block_coefficient_differences(self):
        weights = (0, 6, 10, 3, 15)
        partition = ((0, 1, 2), (3, 4))
        # first block differences 6,10 -> gcd 2; second difference 12;
        # total hidden image step gcd(2,12)=2.
        self.assertEqual(scalar_hidden_step(weights, partition), 2)

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


if __name__ == "__main__":
    unittest.main()
