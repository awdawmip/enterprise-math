import ast
import inspect
import unittest

from enterprise_math import p017_p018_transverse_primorial as transverse_module
from enterprise_math.p017_p018_transverse_primorial import (
    residual_exact_bonferroni_order,
    residual_exactness_check,
    residual_transverse_defect_barrier,
    residual_transverse_defect_localization,
    transverse_odd_prime_prefix,
    transverse_odd_primorial,
    transverse_primorial_depth,
)


class P017P018TransversePrimorialTests(unittest.TestCase):
    def test_critical_scales_recover_universal_odd_primorial(self):
        for k in (65_536, 131_071):
            data = transverse_odd_primorial(k, 5)
            self.assertEqual(data["transverse_primes"], (3, 5, 7, 11, 13))
            self.assertEqual(data["product"], 15_015)
            self.assertTrue(data["complete"])
            self.assertFalse(residual_transverse_defect_barrier(k, 3)["residual_defect_impossible"])

    def test_anchor_primes_can_kill_order_three_residual_defect_jointly(self):
        data = transverse_odd_primorial(20_000, 5)
        self.assertEqual(data["transverse_primes"], (7, 11, 13, 17, 19))
        self.assertEqual(data["product"], 323_323)
        self.assertTrue(residual_transverse_defect_barrier(20_000, 3)["residual_defect_impossible"])

        data = transverse_odd_primorial(255_255, 5)
        self.assertEqual(data["transverse_primes"], (19, 23, 29, 31, 37))
        self.assertEqual(data["product"], 14_535_931)
        self.assertTrue(residual_transverse_defect_barrier(255_255, 3)["residual_defect_impossible"])

    def test_transverse_primorial_depth_gives_exact_residual_precision_ceiling(self):
        expected = {
            8_191: (4, 3),
            20_000: (4, 3),
            65_536: (5, 5),
            131_071: (5, 5),
            255_255: (3, 3),
            524_287: (6, 5),
        }
        for k, (depth, order) in expected.items():
            data = residual_exact_bonferroni_order(k)
            self.assertEqual(data["transverse_primorial_depth"], depth)
            self.assertEqual(data["least_guaranteed_exact_odd_order"], order)
            self.assertEqual(data["max_side_support_size"], max(0, depth - 1))

        data = transverse_primorial_depth(65_536)
        self.assertEqual(data["fitting_transverse_primes"], (3, 5, 7, 11, 13))
        self.assertEqual(data["largest_fitting_product"], 15_015)
        self.assertEqual(data["blocking_prime"], 17)
        self.assertEqual(data["first_blocking_product"], 255_255)

    def test_actual_first_band_defects_clear_dynamic_barrier(self):
        left = residual_transverse_defect_localization(65_536, 883, 3)
        self.assertTrue(left["defect_possible"])
        self.assertEqual(left["transverse_primorial_barrier"], 15_015)
        self.assertGreaterEqual(left["core_product"], left["transverse_primorial_barrier"])

        right = residual_transverse_defect_localization(131_071, 17_477, 3)
        self.assertTrue(right["defect_possible"])
        self.assertEqual(right["transverse_primorial_barrier"], 15_015)
        self.assertGreaterEqual(right["core_product"], right["transverse_primorial_barrier"])

    def test_guaranteed_ceiling_is_pointwise_exact_on_actual_residual_pairs(self):
        left = residual_exactness_check(65_536, 883)
        self.assertEqual(left["exact_odd_order"], 5)
        self.assertEqual(left["residual_pair_defect"], 0)
        self.assertLessEqual(left["lower_support_size"], 5)
        self.assertLessEqual(left["upper_support_size"], 5)

        right = residual_exactness_check(131_071, 17_477)
        self.assertEqual(right["exact_odd_order"], 5)
        self.assertEqual(right["residual_pair_defect"], 0)

    def test_nondefect_residual_cell_does_not_need_to_clear_barrier(self):
        data = residual_transverse_defect_localization(20_000, 67, 3)
        self.assertFalse(data["defect_possible"])
        self.assertTrue(data["residual_defect_impossible_at_scale"])

    def test_transverse_prefix_omits_anchor_primes(self):
        self.assertEqual(transverse_odd_prime_prefix(20_000, 5), (7, 11, 13, 17, 19))
        self.assertEqual(transverse_odd_prime_prefix(255_255, 5), (19, 23, 29, 31, 37))

    def test_invalid_even_order(self):
        with self.assertRaises(ValueError):
            residual_transverse_defect_barrier(100, 2)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(transverse_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
