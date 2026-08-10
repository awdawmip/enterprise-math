import ast
import inspect
import unittest

from enterprise_math import p017_p018_terminal_mirror_exclusivity as exclusivity_module
from enterprise_math.p017_p018_terminal_mirror_exclusivity import (
    terminal_low_rows_are_radius_injective,
    terminal_mirror_exclusivity_criterion,
)


class P017P018TerminalMirrorExclusivityTests(unittest.TestCase):
    def test_reference_even_J_scales_have_two_side_primorial_exclusion(self):
        for k, depth in ((8191, 4), (524_287, 6), (2_147_483_647, 8)):
            data = terminal_mirror_exclusivity_criterion(k)
            self.assertEqual(data["transverse_primorial_depth"], depth)
            self.assertTrue(data["mirror_low_terminal_exclusive"])
            if data["two_side_prefix_complete"]:
                self.assertGreater(
                    data["two_side_minimum_transverse_product"],
                    data["low_core_product_ceiling"],
                )

    def test_k8191_twenty_four_terminal_bits_use_twenty_four_distinct_radii(self):
        data = terminal_low_rows_are_radius_injective(8191)
        self.assertEqual(data["terminal_order"], 3)
        self.assertEqual(data["terminal_low_row_count"], 24)
        self.assertEqual(data["terminal_low_radius_count"], 24)
        self.assertTrue(data["one_low_bit_per_radius"])

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(exclusivity_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
