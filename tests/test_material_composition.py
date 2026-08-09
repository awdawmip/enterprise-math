import unittest

from enterprise_math.material_composition import (
    hardening_composition_report,
    softening_composition_report,
)


class MaterialCompositionTests(unittest.TestCase):
    def test_nested_transforms_never_exceed_product_power_on_small_domain(self):
        for amplitude in range(1, 25):
            for sample in range(amplitude + 1):
                for first in range(1, 5):
                    for second in range(1, 5):
                        hard = hardening_composition_report(
                            sample, amplitude, first, second
                        )
                        soft = softening_composition_report(
                            sample, amplitude, first, second
                        )
                        self.assertGreaterEqual(hard.forward_defect, 0)
                        self.assertGreaterEqual(hard.reverse_defect, 0)
                        self.assertGreaterEqual(soft.forward_defect, 0)
                        self.assertGreaterEqual(soft.reverse_defect, 0)

    def test_hardening_order_can_change_finite_result(self):
        report = hardening_composition_report(4, 5, first_power=2, second_power=3)
        self.assertEqual(report.forward, 0)
        self.assertEqual(report.reverse, 1)
        self.assertEqual(report.commutator, -1)
        self.assertNotEqual(report.forward, report.reverse)

    def test_softening_order_can_change_finite_result(self):
        report = softening_composition_report(1, 4, first_power=2, second_power=3)
        self.assertEqual(report.forward, 2)
        self.assertEqual(report.reverse, 3)
        self.assertEqual(report.commutator, -1)
        self.assertNotEqual(report.forward, report.reverse)

    def test_identity_power_commutes_exactly(self):
        for amplitude in range(1, 20):
            for sample in range(amplitude + 1):
                hard = hardening_composition_report(sample, amplitude, 1, 3)
                soft = softening_composition_report(sample, amplitude, 1, 3)
                self.assertEqual(hard.forward, hard.reverse)
                self.assertEqual(soft.forward, soft.reverse)
                self.assertEqual(hard.commutator, 0)
                self.assertEqual(soft.commutator, 0)

    def test_composition_can_be_strictly_below_product_power(self):
        hard = hardening_composition_report(4, 5, 2, 2)
        soft = softening_composition_report(1, 3, 2, 2)
        self.assertGreater(hard.forward_defect, 0)
        self.assertGreater(soft.forward_defect, 0)


if __name__ == "__main__":
    unittest.main()
