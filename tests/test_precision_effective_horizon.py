import unittest

from enterprise_math.precision_effective_horizon import (
    effective_refinement_factor,
    least_sufficient_scale,
    signature_factors_through_scale,
)


class PrecisionEffectiveHorizonTests(unittest.TestCase):
    def test_constant_future_language_needs_only_precision_one(self):
        signature = ("same",) * 8
        self.assertEqual(least_sufficient_scale(8, signature), 1)
        self.assertEqual(effective_refinement_factor(8, signature), 8)

    def test_binary_half_task_stops_at_scale_two(self):
        signature = (0, 0, 0, 0, 1, 1, 1, 1)
        self.assertFalse(signature_factors_through_scale(8, 1, signature))
        self.assertTrue(signature_factors_through_scale(8, 2, signature))
        self.assertEqual(least_sufficient_scale(8, signature), 2)
        self.assertEqual(effective_refinement_factor(8, signature), 4)

    def test_pair_block_task_stops_at_scale_four(self):
        signature = (0, 0, 1, 1, 2, 2, 3, 3)
        self.assertEqual(least_sufficient_scale(8, signature), 4)
        self.assertEqual(effective_refinement_factor(8, signature), 2)

    def test_parity_task_requires_full_scale(self):
        signature = (0, 1, 0, 1, 0, 1, 0, 1)
        self.assertEqual(least_sufficient_scale(8, signature), 8)
        self.assertEqual(effective_refinement_factor(8, signature), 1)

    def test_invalid_signature_fails_closed(self):
        with self.assertRaises(ValueError):
            least_sufficient_scale(8, (0, 1))


if __name__ == "__main__":
    unittest.main()
