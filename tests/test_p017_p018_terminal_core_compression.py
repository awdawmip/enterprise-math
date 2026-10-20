import unittest

from enterprise_math.p017_p018_terminal_core_compression import (
    terminal_core_point_majorant,
    terminal_core_signed_profile,
)


class P017P018TerminalCoreCompressionTests(unittest.TestCase):
    def test_even_j_high_support_row_compresses_all_defect_units_to_one_core_label(self):
        k = 524_287
        state = 274_877_906_935
        support = (5, 23, 29, 47, 97, 101, 179)

        data = terminal_core_point_majorant(k, state, support)

        self.assertEqual(data["transverse_primorial_depth"], 6)
        self.assertEqual(data["order"], 5)
        self.assertEqual(data["complete_transverse_core"], state)
        self.assertEqual(data["ordinary_defect"], 6)
        self.assertEqual(data["high_core_defect_correction"], 6)
        self.assertEqual(data["residual_core_excess"], 0)
        self.assertEqual(data["core_compressed_value"], 1)
        self.assertTrue(data["high_complete_core_row"])

    def test_k524287_low_terminal_rows_have_exactly_one_residual_bit(self):
        k = 524_287
        examples = (
            (
                435_435 * 631_271,
                (3, 5, 7, 11, 13, 29),
                435_435,
            ),
            (
                465_465 * 590_543,
                (3, 5, 7, 11, 13, 31),
                465_465,
            ),
        )

        for state, support, core in examples:
            data = terminal_core_point_majorant(k, state, support)
            self.assertEqual(data["ordinary_defect"], 1)
            self.assertEqual(data["high_core_defect_correction"], 0)
            self.assertEqual(data["residual_core_excess"], 1)
            self.assertEqual(data["complete_transverse_core"], core)
            self.assertTrue(data["low_terminal_full_core_row"])

    def test_k8191_terminal_core_compression_turns_failed_order3_into_certificate(self):
        data = terminal_core_signed_profile(8_191)

        self.assertEqual(data["transverse_primorial_depth"], 4)
        self.assertEqual(data["order"], 3)
        self.assertEqual(data["signed_state_count"], 8_190)
        self.assertEqual(data["ordinary_bonferroni_sum"], 9_689)
        self.assertEqual(data["ordinary_defect"], 2_437)
        self.assertEqual(data["high_core_defect_correction"], 2_413)
        self.assertEqual(data["residual_core_excess"], 24)
        self.assertEqual(data["core_compressed_sum"], 7_276)
        self.assertFalse(data["ordinary_bonferroni_sum"] < data["signed_state_count"])
        self.assertTrue(data["core_compressed_certificate"])
        self.assertEqual(len(data["residual_rows"]), 24)

    def test_k20000_terminal_low_core_residual_is_empty(self):
        data = terminal_core_signed_profile(20_000)

        self.assertEqual(data["transverse_primorial_depth"], 4)
        self.assertEqual(data["order"], 3)
        self.assertEqual(data["ordinary_defect"], 1_143)
        self.assertEqual(data["high_core_defect_correction"], 1_143)
        self.assertEqual(data["residual_core_excess"], 0)
        self.assertEqual(data["core_compressed_sum"], data["exact_nonempty_union"])


if __name__ == "__main__":
    unittest.main()
