import ast
import inspect
import unittest

from enterprise_math import p017_p018_token_reuse_precision as reuse_module
from enterprise_math.p017_p018_token_reuse_precision import (
    defect_token_reuse_capacity,
    least_global_single_use_odd_order,
    residual_vs_token_precision_horizons,
)


class P017P018TokenReusePrecisionTests(unittest.TestCase):
    def test_critical_scales_exhibit_zero_or_one_odd_order_quantum_gap(self):
        expected = {
            8191: (4, 3, 5, 2),
            65_536: (5, 5, 5, 0),
            131_071: (5, 5, 5, 0),
            524_287: (6, 5, 7, 2),
            2_147_483_647: (8, 7, 9, 2),
        }
        for k, (depth, residual_order, token_order, gap) in expected.items():
            data = residual_vs_token_precision_horizons(k)
            self.assertEqual(data["transverse_primorial_depth"], depth)
            self.assertEqual(data["residual_exact_odd_order"], residual_order)
            self.assertEqual(data["global_token_single_use_odd_order"], token_order)
            self.assertEqual(data["odd_order_quantum_gap"], gap)
            self.assertIn(gap, (0, 2))
            self.assertEqual(data["one_additional_odd_order_quantum"], gap == 2)

    def test_524287_order_five_has_exact_three_slot_token_reuse_ceiling(self):
        data = defect_token_reuse_capacity(524_287, 5)
        self.assertEqual(
            data["minimum_transverse_token_primes"],
            (3, 5, 7, 11, 13, 17),
        )
        self.assertEqual(data["minimum_transverse_token_product"], 255_255)
        self.assertEqual(data["universal_signed_reuse_capacity"], 3)
        self.assertFalse(data["all_order_m_tokens_single_use"])

    def test_one_more_odd_order_quantum_restores_single_use_at_524287(self):
        data = defect_token_reuse_capacity(524_287, 7)
        self.assertEqual(
            data["minimum_transverse_token_primes"],
            (3, 5, 7, 11, 13, 17, 19, 23),
        )
        self.assertEqual(data["minimum_transverse_token_product"], 111_546_435)
        self.assertEqual(data["universal_signed_reuse_capacity"], 1)
        self.assertTrue(data["all_order_m_tokens_single_use"])
        self.assertEqual(
            least_global_single_use_odd_order(524_287)["least_global_single_use_odd_order"],
            7,
        )

    def test_bounded_horizon_gap_formula_is_always_zero_or_two(self):
        saw_zero = False
        saw_two = False
        for k in range(4, 2000):
            data = residual_vs_token_precision_horizons(k)
            gap = data["odd_order_quantum_gap"]
            self.assertIn(gap, (0, 2))
            if data["transverse_primorial_depth"] % 2:
                self.assertEqual(gap, 0)
                saw_zero = True
            else:
                self.assertEqual(gap, 2)
                saw_two = True
        self.assertTrue(saw_zero)
        self.assertTrue(saw_two)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(reuse_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
