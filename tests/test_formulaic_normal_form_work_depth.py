import unittest

from enterprise_math.formulaic_normal_form_work_depth import formulaic_or_work_depth


class FormulaicNormalFormWorkDepthTests(unittest.TestCase):
    def test_reference_k5_h20(self):
        report = formulaic_or_work_depth(5, 20)
        self.assertEqual(report.normalization_word_or_gates, 19)
        self.assertEqual(report.normalization_bit_work, 95)
        self.assertEqual(report.normalization_depth, 5)
        self.assertEqual(report.state_apply_bit_work, 5)
        self.assertEqual(report.total_bit_work, 100)
        self.assertEqual(report.total_depth, 6)

    def test_total_bit_work_is_k_times_word_length(self):
        for k in range(1, 9):
            for length in range(1, 65):
                report = formulaic_or_work_depth(k, length)
                self.assertEqual(report.total_bit_work, k * length)
                self.assertEqual(report.normalization_word_or_gates, length - 1)

    def test_parallel_depth_is_logarithmic_step_function(self):
        expected = {1: 1, 2: 2, 3: 3, 4: 3, 5: 4, 8: 4, 9: 5, 16: 5, 17: 6}
        for length, total_depth in expected.items():
            self.assertEqual(formulaic_or_work_depth(3, length).total_depth, total_depth)

    def test_validation(self):
        with self.assertRaises(ValueError):
            formulaic_or_work_depth(0, 2)
        with self.assertRaises(ValueError):
            formulaic_or_work_depth(2, 0)


if __name__ == "__main__":
    unittest.main()
