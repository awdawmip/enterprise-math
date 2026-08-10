import ast
import inspect
import unittest

from enterprise_math import p017_p018_token_terminal_precision as terminal_module
from enterprise_math.p017_p018_token_terminal_precision import (
    least_single_use_order_is_one_step_terminal,
)


class P017P018TokenTerminalPrecisionTests(unittest.TestCase):
    def test_reference_scales_are_terminal_at_their_least_single_use_order(self):
        expected = {
            862: 3,
            8191: 5,
            65_536: 5,
            131_071: 5,
            524_287: 7,
            2_147_483_647: 9,
        }
        for k, order in expected.items():
            data = least_single_use_order_is_one_step_terminal(k)
            self.assertEqual(data["least_global_single_use_odd_order"], order)
            self.assertTrue(data["one_step_same_order_terminal"])
            self.assertTrue(data["criterion"]["all_defect_tokens_single_use"])
            self.assertTrue(
                data["criterion"]["all_parent_support_sizes_at_most_2m_plus_1"]
            )
            self.assertLess(data["child_square_root_scale_ceiling"], k)

    def test_bounded_scales_make_support_barrier_automatic_at_minimal_order(self):
        for k in range(4, 2000):
            data = least_single_use_order_is_one_step_terminal(k)
            self.assertTrue(data["criterion"]["one_step_same_order_terminal"])

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(terminal_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
