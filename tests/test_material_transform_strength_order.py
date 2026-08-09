import unittest

from enterprise_math.material_transform_strength_order import (
    material_transform_activation_order,
    material_transform_sample_order,
)


class MaterialTransformStrengthOrderTests(unittest.TestCase):
    def test_samplewise_hardening_identity_softening_order_holds_exhaustively_on_small_scales(self):
        for amplitude in range(1, 40):
            for power in range(1, 7):
                for sample in range(amplitude + 1):
                    report = material_transform_sample_order(
                        sample, amplitude, power
                    )
                    self.assertLessEqual(report.hardening_sample, sample)
                    self.assertGreaterEqual(report.softening_sample, sample)

    def test_transform_order_moves_force_activation_layer_in_expected_directions(self):
        base = (0, 10, 20, 40, 80, 100)
        report = material_transform_activation_order(
            base,
            amplitude=100,
            power=2,
            required_response_sample=50,
        )
        self.assertEqual(report.hardening_branch, (0, 1, 4, 16, 64, 100))
        self.assertEqual(report.softening_activation_depth, 3)
        self.assertEqual(report.base_activation_depth, 4)
        self.assertEqual(report.hardening_activation_depth, 4)

        deeper = material_transform_activation_order(
            base,
            amplitude=100,
            power=2,
            required_response_sample=70,
        )
        self.assertEqual(deeper.softening_activation_depth, 4)
        self.assertEqual(deeper.base_activation_depth, 4)
        self.assertEqual(deeper.hardening_activation_depth, 5)

    def test_power_one_is_exact_identity(self):
        base = (0, 3, 7, 10)
        report = material_transform_activation_order(base, 10, 1, 6)
        self.assertEqual(report.hardening_branch, base)
        self.assertEqual(report.softening_branch, base)
        self.assertEqual(report.softening_activation_depth, 2)
        self.assertEqual(report.base_activation_depth, 2)
        self.assertEqual(report.hardening_activation_depth, 2)

    def test_softening_can_create_a_represented_activation_when_base_and_hardening_never_reach_threshold(self):
        base = (0, 1, 2, 3, 4)
        report = material_transform_activation_order(base, 100, 2, 10)
        self.assertIsNotNone(report.softening_activation_depth)
        self.assertIsNone(report.base_activation_depth)
        self.assertIsNone(report.hardening_activation_depth)

    def test_hardening_never_activates_earlier_than_base_across_bounded_branches(self):
        branches = (
            (0, 5, 10, 20, 40),
            (0, 0, 1, 8, 64),
            (0, 20, 20, 50, 100),
        )
        for base in branches:
            amplitude = 100
            for power in (2, 3, 4):
                for threshold in range(0, amplitude + 1, 7):
                    report = material_transform_activation_order(
                        base, amplitude, power, threshold
                    )
                    soft = 10**6 if report.softening_activation_depth is None else report.softening_activation_depth
                    identity = 10**6 if report.base_activation_depth is None else report.base_activation_depth
                    hard = 10**6 if report.hardening_activation_depth is None else report.hardening_activation_depth
                    self.assertLessEqual(soft, identity)
                    self.assertLessEqual(identity, hard)

    def test_invalid_curve_or_threshold_is_rejected(self):
        with self.assertRaises(ValueError):
            material_transform_activation_order((0, 5, 4), 10, 2, 5)
        with self.assertRaises(ValueError):
            material_transform_activation_order((0, 5, 10), 10, 2, 11)
        with self.assertRaises(ValueError):
            material_transform_sample_order(11, 10, 2)


if __name__ == "__main__":
    unittest.main()
