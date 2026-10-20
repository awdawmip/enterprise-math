import unittest

from enterprise_math.p017_p018_core_adaptive_bonferroni import (
    core_adaptive_point_majorant,
    core_adaptive_signed_profile,
)


class P017P018CoreAdaptiveBonferroniTests(unittest.TestCase):
    def test_high_complete_core_removes_whole_order5_defect(self):
        data = core_adaptive_point_majorant(
            524_287,
            274_877_906_935,
            (5, 23, 29, 47, 97, 101, 179),
            5,
        )

        self.assertEqual(data["ordinary_defect"], 6)
        self.assertEqual(data["high_core_defect_correction"], 6)
        self.assertEqual(data["residual_core_excess"], 0)
        self.assertEqual(data["core_adaptive_value"], 1)

    def test_low_complete_core_retains_exact_point_defect(self):
        data = core_adaptive_point_majorant(
            524_287,
            435_435 * 631_271,
            (3, 5, 7, 11, 13, 29),
            3,
        )

        self.assertEqual(data["complete_transverse_core"], 435_435)
        self.assertEqual(data["ordinary_defect"], 10)
        self.assertEqual(data["high_core_defect_correction"], 0)
        self.assertEqual(data["residual_core_excess"], 10)
        self.assertEqual(data["core_adaptive_value"], 11)

    def test_k8191_order3_core_adaptive_certificate(self):
        data = core_adaptive_signed_profile(8_191, 3)

        self.assertEqual(data["signed_state_count"], 8_190)
        self.assertEqual(data["ordinary_bonferroni_sum"], 9_689)
        self.assertEqual(data["ordinary_defect"], 2_437)
        self.assertEqual(data["high_core_defect_correction"], 2_413)
        self.assertEqual(data["residual_core_excess"], 24)
        self.assertEqual(data["core_adaptive_sum"], 7_276)
        self.assertTrue(data["core_adaptive_certificate"])

    def test_order1_remains_too_coarse_at_k8191(self):
        data = core_adaptive_signed_profile(8_191, 1)

        self.assertEqual(data["ordinary_bonferroni_sum"], 16_048)
        self.assertEqual(data["high_core_defect_correction"], 5_508)
        self.assertEqual(data["residual_core_excess"], 3_288)
        self.assertEqual(data["core_adaptive_sum"], 10_540)
        self.assertFalse(data["core_adaptive_certificate"])


if __name__ == "__main__":
    unittest.main()
