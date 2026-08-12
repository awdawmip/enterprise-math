import ast
import inspect
import unittest

from enterprise_math import p017_p018_token_support_descent as descent_module
from enterprise_math.p017_p018_token_support_descent import (
    certify_one_step_same_order_terminal,
    one_step_token_terminal_criterion,
    point_token_support_descent,
)


class P017P018TokenSupportDescentTests(unittest.TestCase):
    def test_known_critical_scales_have_expected_one_step_order_five_boundary(self):
        for k in (65_536, 131_071):
            data = one_step_token_terminal_criterion(k, 5)
            self.assertTrue(data["all_defect_tokens_single_use"])
            self.assertTrue(data["all_parent_support_sizes_at_most_2m_plus_1"])
            self.assertTrue(data["one_step_same_order_terminal"])

        # The no-effective-anchor critical scale 2^19-1 crosses the universal
        # six-prime token product 255255, so order-five defect tokens are no
        # longer globally single-use merely from the product threshold.
        data = one_step_token_terminal_criterion(524_287, 5)
        self.assertFalse(data["all_defect_tokens_single_use"])
        self.assertFalse(data["one_step_same_order_terminal"])

    def test_k862_order_three_is_one_step_terminal(self):
        data = one_step_token_terminal_criterion(862, 3)
        self.assertTrue(data["one_step_same_order_terminal"])
        self.assertGreater(
            data["single_use_token_barrier"]["product"],
            861,
        )

    def test_seven_support_row_descends_to_one_prime_power_direction(self):
        # k=8191, M+r with r=1363:
        # 67102035 = 3*5*7*11*13*41*109.
        k = 8191
        state = 67_102_035
        data = certify_one_step_same_order_terminal(k, state, 5)
        self.assertEqual(data["support"], (3, 5, 7, 11, 13, 41, 109))
        self.assertEqual(data["defect"], 6)
        self.assertEqual(len(data["token_rows"]), 6)
        for row in data["token_rows"]:
            self.assertTrue(row["single_use_product_regime"])
            self.assertEqual(row["support_drop"], 6)
            self.assertEqual(row["child_support_size"], 1)
            self.assertTrue(row["same_order_defect_terminal_by_support"])
            self.assertTrue(row["strict_scale_descent"])
            self.assertLess(row["child_root_scale"], k)
            self.assertEqual(
                tuple(row["omitted_support_primes"]),
                tuple(row["quotient_support"]),
            )

    def test_eight_support_row_descends_to_two_support_directions(self):
        # k=65536, M+r with r=64513:
        # 4295097345 = 3*5*7*11*17*19*29*397.
        k = 65_536
        state = 4_295_097_345
        data = certify_one_step_same_order_terminal(k, state, 5)
        self.assertEqual(data["support"], (3, 5, 7, 11, 17, 19, 29, 397))
        self.assertEqual(data["defect"], 21)
        self.assertEqual(len(data["token_rows"]), 21)
        for row in data["token_rows"]:
            self.assertEqual(row["child_support_size"], 2)
            self.assertLessEqual(row["child_low_support_size"], 2)
            self.assertLessEqual(len(row["child_large_tail_support"]), 1)
            self.assertTrue(row["same_order_defect_terminal_by_support"])
            self.assertTrue(row["strict_scale_descent"])

    def test_nondefect_state_cannot_be_certified_as_defect_descent(self):
        with self.assertRaises(ValueError):
            certify_one_step_same_order_terminal(31, 31 * 32 + 1, 5)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(descent_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
